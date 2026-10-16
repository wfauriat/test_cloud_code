"""Local tool executor behind a narrow interface, confined to a workspace dir.  PLAN §5.3.

[RISKY] Approved commands run on this machine. Review-by-default (core/policy.py) is the only
barrier; `run_command` is not even declared unless the session enables it.
"""

from __future__ import annotations

import difflib
import re
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

MAX_OUTPUT_CHARS = 200_000
COMMAND_TIMEOUT_S = 60


def _tool(name: str, description: str, props: dict[str, Any]) -> dict[str, Any]:
    return {"name": name, "description": description, "strict": True, "eager_input_streaming": True,
            "input_schema": {"type": "object", "properties": props, "required": list(props),
                             "additionalProperties": False}}


S = {"type": "string"}
TOOL_DEFS: dict[str, dict[str, Any]] = {
    "read_file": _tool("read_file", "Read a text file in the workspace. Call it whenever you need a file's "
                       "current content, including after a curator placeholder removed an earlier read.",
                       {"path": S}),
    "list_dir": _tool("list_dir", "List a directory in the workspace.", {"path": S}),
    "grep": _tool("grep", "Search files under a workspace path for a regular expression.",
                  {"pattern": S, "path": S}),
    "write_file": _tool("write_file", "Create or overwrite a file in the workspace.", {"path": S, "content": S}),
    "edit_file": _tool("edit_file", "Replace exactly one occurrence of `old` with `new` in a workspace file.",
                       {"path": S, "old": S, "new": S}),
    "run_command": _tool("run_command", "Run a shell command in the workspace root (needs approval).",
                         {"command": S}),
}


class ToolError(Exception):
    pass


@dataclass
class ExecResult:
    output: str
    is_error: bool
    ms: int
    effects: dict[str, Any] = field(default_factory=dict)


class Executor:
    def __init__(self, root: str | Path, allow_commands: bool = False):
        self.root = Path(root).expanduser().resolve()
        self.allow_commands = allow_commands

    def tool_defs(self) -> list[dict[str, Any]]:
        return [d for n, d in TOOL_DEFS.items() if n != "run_command" or self.allow_commands]

    def path(self, p: str) -> Path:
        full = (self.root / p).resolve()  # resolves symlinks: a link pointing outside is refused
        if full != self.root and self.root not in full.parents:
            raise ToolError(f"path outside the workspace: {p}")
        return full

    def check_input(self, name: str, inp: Any) -> str | None:
        """Schema check of a parsed input copy before running (PLAN §5.3)."""
        d = TOOL_DEFS.get(name)
        if d is None or (name == "run_command" and not self.allow_commands):
            return f"unknown tool {name}"
        if not isinstance(inp, dict):
            return "input is not an object"
        props = d["input_schema"]["properties"]
        missing = [k for k in props if k not in inp]
        extra = [k for k in inp if k not in props]
        bad = [k for k in props if k in inp and not isinstance(inp[k], str)]
        if missing or extra or bad:
            return f"invalid input: missing {missing}, unexpected {extra}, not strings {bad}"
        return None

    def effects(self, name: str, inp: dict[str, Any]) -> dict[str, Any]:
        """What the call would do, for the tool gate: paths, writes, a diff for edits, unknowns."""
        eff: dict[str, Any] = {"writes": name in ("write_file", "edit_file", "run_command"),
                               "paths": [inp["path"]] if "path" in inp else [], "unknowns": []}
        try:
            if name == "write_file":
                p = self.path(inp["path"])
                old = p.read_text() if p.exists() else ""
                eff["diff"] = _diff(old, inp["content"], inp["path"])
                eff["creates"] = not p.exists()
            elif name == "edit_file":
                p = self.path(inp["path"])
                old = p.read_text()
                n = old.count(inp["old"])
                eff["matches"] = n
                if n == 1:
                    eff["diff"] = _diff(old, old.replace(inp["old"], inp["new"]), inp["path"])
            elif name == "run_command":
                eff["command"] = inp["command"]
                eff["unknowns"].append("shell command: effects not analysed (fail closed: always reviewed)")
                if re.search(r"\b(curl|wget|ssh|scp|git\s+push|pip|npm|uv)\b", inp["command"]):
                    eff["network"] = "possible"
        except (ToolError, OSError, KeyError) as e:
            eff["error"] = str(e)
        return eff

    def run(self, name: str, inp: dict[str, Any]) -> ExecResult:
        t0 = time.monotonic()
        try:
            out = self._run(name, inp)
            err = False
        except (ToolError, OSError, UnicodeDecodeError, re.error, subprocess.TimeoutExpired) as e:
            out, err = f"Error: {e}", True
        if len(out) > MAX_OUTPUT_CHARS:
            out = out[:MAX_OUTPUT_CHARS] + f"\n[output truncated at {MAX_OUTPUT_CHARS} characters]"
        return ExecResult(out, err, int(1000 * (time.monotonic() - t0)))

    def _run(self, name: str, inp: dict[str, Any]) -> str:
        if name == "read_file":
            return self.path(inp["path"]).read_text()
        if name == "list_dir":
            p = self.path(inp["path"])
            return "\n".join(sorted(f"{c.name}/" if c.is_dir() else c.name for c in p.iterdir()))
        if name == "grep":
            rx = re.compile(inp["pattern"])
            base = self.path(inp["path"])
            hits = []
            for f in sorted(base.rglob("*") if base.is_dir() else [base]):
                if f.is_file() and ".git" not in f.parts:
                    try:
                        for i, line in enumerate(f.read_text().splitlines(), 1):
                            if rx.search(line):
                                hits.append(f"{f.relative_to(self.root)}:{i}: {line}")
                    except UnicodeDecodeError:
                        continue
                if len(hits) >= 200:
                    hits.append("[stopped at 200 matches]")
                    break
            return "\n".join(hits) or "no matches"
        if name == "write_file":
            p = self.path(inp["path"])
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(inp["content"])
            return f"wrote {len(inp['content'])} characters to {inp['path']}"
        if name == "edit_file":
            p = self.path(inp["path"])
            text = p.read_text()
            n = text.count(inp["old"])
            if n != 1:
                raise ToolError(f"`old` must occur exactly once in {inp['path']}, found {n}")
            p.write_text(text.replace(inp["old"], inp["new"]))
            return f"edited {inp['path']}"
        if name == "run_command" and self.allow_commands:
            r = subprocess.run(["bash", "-c", inp["command"]], cwd=self.root, capture_output=True, text=True,
                               timeout=COMMAND_TIMEOUT_S)
            return f"exit {r.returncode}\n{r.stdout}{r.stderr}"
        raise ToolError(f"unknown tool {name}")


def _diff(old: str, new: str, path: str) -> str:
    return "".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), f"a/{path}", f"b/{path}"))
