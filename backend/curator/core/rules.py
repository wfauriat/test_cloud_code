"""Mechanical curation rules -> proposals.  PLAN §4 step 9.

Deterministic and free. A proposal is a draft op with a rationale and a token estimate; it
becomes an edit only when someone stages it. Rules never target pinned blocks.

Priority when a result matches several rules: stale read > superseded re-run > duplicate >
oversized (the first three remove the whole output, the last keeps head and tail).
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Any

from .model import Event, Op, Span
from .repair import placeholder
from .segment import text_of
from .tokens import estimate_raw, estimate_text

RULES_VERSION = 1

# Tool names and the input field that carries the path/command, per source.
# QUIRK: Claude Code in "bash-first" mode reads files with `cat`/`sed` through Bash, which R2
# cannot see; R3 still catches exact re-runs.
TOOLSETS: dict[str, dict[str, dict[str, str]]] = {
    "claude_code": {
        "read": {"Read": "file_path", "NotebookRead": "notebook_path"},
        "write": {"Edit": "file_path", "Write": "file_path", "MultiEdit": "file_path",
                  "NotebookEdit": "notebook_path"},
        "run": {"Bash": "command"},
    },
    "live": {
        "read": {"read_file": "path"},
        "write": {"write_file": "path", "edit_file": "path"},
        "run": {"run_command": "command"},
    },
}

OVERSIZE_TOKENS = 4000
KEEP_LINES = 15
MIN_DUPLICATE_TOKENS = 50


@dataclass
class Proposal:
    rule: str
    rationale: str
    op: Op
    tokens_before: int
    tokens_after: int

    @property
    def tokens_saved(self) -> int:
        return max(self.tokens_before - self.tokens_after, 0)


@dataclass
class _Result:
    order: int
    event_id: str
    index: int
    call: dict[str, Any]
    text: str
    tokens: int


def propose(events: list[Event], *, toolset: str = "claude_code",
            pinned: set[tuple[str, int]] = frozenset(), oversize_tokens: int = OVERSIZE_TOKENS,
            id_prefix: str = "p") -> list[Proposal]:
    ts = TOOLSETS[toolset]
    calls: dict[str, tuple[int, dict[str, Any]]] = {}
    results: list[_Result] = []
    order = 0
    for e in events:
        if not e.is_message:
            continue
        for i, b in enumerate(e.blocks):
            order += 1
            if b.type == "tool_use":
                calls[b.raw.get("id")] = (order, b.raw)
            elif b.type == "tool_result":
                _, call = calls.get(b.raw.get("tool_use_id"), (0, {}))
                results.append(_Result(order, e.id, i, call, text_of(b.raw), estimate_raw(b.raw)))

    writes: dict[str, list[int]] = {}
    for o, call in calls.values():
        field = ts["write"].get(call.get("name"))
        if field and (path := (call.get("input") or {}).get(field)):
            writes.setdefault(path, []).append(o)

    proposals: list[Proposal] = []
    claimed: set[tuple[str, int]] = set()

    def add(r: _Result, rule: str, why: str, verb: str = "drop", text: str | None = None) -> None:
        addr = (r.event_id, r.index)
        if addr in claimed or addr in pinned:
            return
        claimed.add(addr)
        after = estimate_text(text) if text is not None else estimate_text(placeholder("x" * 40, why))
        if after >= r.tokens:
            return  # a placeholder longer than the output saves nothing (small outputs)
        op = Op(id=f"{id_prefix}{len(proposals) + 1}", verb=verb, targets=[Span(r.event_id, r.index)],
                payload={"text": text} if text is not None else {},
                author=f"rule:{rule}@{RULES_VERSION}", rationale=why, state="draft")
        proposals.append(Proposal(rule, why, op, r.tokens, after))

    # R2 stale read: the file was modified after it was read.
    for r in results:
        field = ts["read"].get(r.call.get("name"))
        path = (r.call.get("input") or {}).get(field) if field else None
        if path and any(w > r.order for w in writes.get(path, [])):
            add(r, "R2", f"stale: {path} was modified later")

    # R3 superseded re-run: the same command ran again later.
    runs: dict[str, list[_Result]] = {}
    for r in results:
        field = ts["run"].get(r.call.get("name"))
        cmd = (r.call.get("input") or {}).get(field) if field else None
        if cmd:
            runs.setdefault(cmd, []).append(r)
    for rs in runs.values():
        for r in rs[:-1]:
            add(r, "R3", "superseded: the same command ran again later")

    # R4 exact duplicate output: keep the latest copy.
    dups: dict[str, list[_Result]] = {}
    for r in results:
        if r.tokens >= MIN_DUPLICATE_TOKENS:
            dups.setdefault(hashlib.sha256(r.text.encode()).hexdigest(), []).append(r)
    for rs in dups.values():
        for r in rs[:-1]:
            add(r, "R4", "duplicate: the same output appears again later")

    # R1 oversized output: keep head and tail.
    for r in results:
        if r.tokens > oversize_tokens:
            lines = r.text.splitlines()
            if len(lines) > 2 * KEEP_LINES:
                cut = len(lines) - 2 * KEEP_LINES
                cut_tokens = estimate_text("\n".join(lines[KEEP_LINES:-KEEP_LINES]))
                mid = placeholder(f"{cut} lines (~{cut_tokens:,} tokens) from the middle of this output",
                                  "oversized", "re-run with a narrower command if needed")
                text = "\n".join(lines[:KEEP_LINES] + [mid] + lines[-KEEP_LINES:])
                add(r, "R1", f"oversized: ~{r.tokens:,} tokens", "replace", text)
            else:
                add(r, "R1", f"oversized: ~{r.tokens:,} tokens in few lines")
    return proposals
