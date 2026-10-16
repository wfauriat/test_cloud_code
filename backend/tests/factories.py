"""Small synthetic sessions for tests. Real transcripts never go into the repo (PLAN §8)."""

from __future__ import annotations

import json
from itertools import count

from curator.core.model import Block, Event

SRC_V1 = "def f():\n" + "    x = 1  # padding so the output is worth stubbing\n" * 40 + "    return 1\n"
SRC_V2 = SRC_V1.replace("return 1", "return 2")
LS = "".join(f"file_{i}.py\n" for i in range(60))


def ev(eid: str, role: str, *raws: dict, origin: str | None = None, seq: int = 0, **meta) -> Event:
    org = origin or {"user": "user", "assistant": "model", "system": "harness"}[role]
    blocks = [Block(r, "tool" if r.get("type") == "tool_result" else org) for r in raws]
    return Event(eid, seq, "message", role, blocks, meta=meta)


def text(s: str) -> dict:
    return {"type": "text", "text": s}


def thinking(sig: str) -> dict:
    return {"type": "thinking", "thinking": "", "signature": sig}


def call(cid: str, name: str, **inp) -> dict:
    return {"type": "tool_use", "id": cid, "name": name, "input": inp}


def result(cid: str, content: str) -> dict:
    return {"type": "tool_result", "tool_use_id": cid, "content": content}


def coding_session() -> list[Event]:
    """user asks; model reads a.py and lists (parallel); edits a.py; reads a.py again;
    lists again (same command); answers."""
    return [
        ev("u1", "user", text("Fix the bug in a.py")),
        ev("a1", "assistant", thinking("sig-a1"), call("t1", "Read", file_path="a.py"),
           call("t2", "Bash", command="ls")),
        ev("u2", "user", result("t1", SRC_V1), result("t2", LS)),
        ev("a2", "assistant", thinking("sig-a2"), call("t3", "Edit", file_path="a.py", old="1", new="2")),
        ev("u3", "user", result("t3", "ok")),
        ev("a3", "assistant", call("t4", "Read", file_path="a.py"), call("t5", "Bash", command="ls")),
        ev("u4", "user", result("t4", SRC_V2), result("t5", LS)),
        ev("a4", "assistant", thinking("sig-a4"), text("Fixed: f() now returns 2.")),
        ev("u5", "user", text("Thanks. Now add a test.")),
    ]


def claude_code_jsonl(*, cache_break: bool = False) -> list[str]:
    """A Claude Code-shaped log with the quirks the importer must handle: parallel tool calls
    logged as a branch, attachments rendered as system messages, a prompt snapshot, one line per
    assistant content block, an unrendered attachment."""
    n = count(1)
    lines: list[dict] = []

    def add(d: dict, parent: str | None) -> str:
        u = f"uuid-{next(n)}"
        lines.append({"uuid": u, "parentUuid": parent, "isSidechain": False, "timestamp":
                      f"2026-10-16T10:00:{len(lines):02d}.000Z", **d})
        return u

    def usage(read: int, write: int, out: int = 50) -> dict:
        return {"input_tokens": 2, "cache_read_input_tokens": read, "cache_creation_input_tokens": write,
                "output_tokens": out, "cache_creation": {"ephemeral_1h_input_tokens": write,
                                                          "ephemeral_5m_input_tokens": 0}}

    def asst(mid: str, block: dict, parent: str, u: dict) -> str:
        return add({"type": "assistant", "message": {"id": mid, "role": "assistant", "model": "claude-opus-5-5",
                                                     "content": [block], "usage": u, "stop_reason": "tool_use"}},
                   parent)

    p = add({"type": "user", "message": {"role": "user", "content": "Fix the bug in a.py"}}, None)
    p = add({"type": "attachment", "attachment": {"type": "date", "date": "2026-10-16"},
             "rendered": [{"content": "<system-reminder>Today is 2026-10-16.</system-reminder>"}],
             "renderedRole": "system"}, p)
    p = add({"type": "attachment", "attachment": {"type": "credential_org"}}, p)  # not rendered
    p = add({"type": "attachment", "attachment": {"type": "prompt_snapshot",
                                                  "systemPrompt": ["You are a coding agent.",
                                                                   "__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__",
                                                                   "Be brief."]}}, p)
    u1 = usage(0, 5000)
    p = asst("m1", thinking("sig-1"), p, u1)
    c1 = asst("m1", call("t1", "Read", file_path="a.py"), p, u1)
    c2 = asst("m1", call("t2", "Bash", command="ls"), c1, u1)
    add({"type": "user", "message": {"role": "user", "content": [result("t1", SRC_V1)]}}, c1)
    p = add({"type": "user", "message": {"role": "user", "content": [result("t2", "a.py\nb.py\n")]}}, c2)
    u2 = usage(1000 if cache_break else 5000, 400)
    p = asst("m2", call("t3", "Edit", file_path="a.py", old="1", new="2"), p, u2)
    p = add({"type": "user", "message": {"role": "user", "content": [result("t3", "ok")]}}, p)
    u3 = usage(5400, 100)
    p = add({"type": "assistant", "message": {"id": "m3", "role": "assistant", "model": "claude-opus-5-5",
                                              "content": [text("Fixed.")], "usage": u3, "stop_reason": "end_turn"}}, p)
    lines.append({"type": "system", "subtype": "stop_hook_summary", "uuid": "uuid-x", "parentUuid": p})
    return [json.dumps(d) for d in lines]
