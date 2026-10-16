"""THE validator: the only place that encodes the API's structural rules.  PLAN §4 step 6, D4.

A request with violations never reaches a gate. Rules are deliberately few and literal; every
400 seen live should become a new rule here plus a test (tests/test_render.py).
"""

from __future__ import annotations

from .model import THINKING_TYPES, Diagnostic, Preamble, Request
from .wire import block_hash, compare_key


def validate(req: Request, *, preamble: Preamble | None = None,
             thinking_had: list[int] | None = None, thinking_kept: list[int] | None = None,
             known_hashes: set[str] | None = None) -> list[Diagnostic]:
    v: list[Diagnostic] = []
    msgs = req.messages

    def err(code: str, msg: str, where: str = "") -> None:
        v.append(Diagnostic(code, msg, where))

    if not msgs:
        err("V01.empty", "no messages")
        return v
    if msgs[0]["role"] != "user":
        err("V02.first", f"first message must be user, got {msgs[0]['role']}", "messages[0]")
    if msgs[-1]["role"] == "assistant":
        err("V05.prefill", "request ends with an assistant message (prefill is not supported)",
            f"messages[{len(msgs) - 1}]")

    for k, m in enumerate(msgs):
        where = f"messages[{k}]"
        role, content = m["role"], m["content"]
        if role not in ("user", "assistant", "system"):
            err("V03.role", f"unknown role {role}", where)
        if not content:
            err("V06.empty_content", "message has no content", where)
        for j, b in enumerate(content if isinstance(content, list) else []):
            if b.get("type") == "text" and not str(b.get("text", "")).strip():
                err("V06.empty_text", "text blocks must contain non-whitespace text", f"{where}.content[{j}]")

        if role == "system":
            if k == 0 or msgs[k - 1]["role"] != "user":
                err("V04.system_after", "a system message must follow a user message", where)
            if k + 1 < len(msgs) and msgs[k + 1]["role"] != "assistant":
                err("V04.system_before", "a system message must be last or followed by assistant", where)

        if role == "assistant":
            ids = [b.get("id") for b in content if b.get("type") == "tool_use"]
            if ids and k + 1 < len(msgs):
                nxt = msgs[k + 1]
                got = [b.get("tool_use_id") for b in nxt["content"] if b.get("type") == "tool_result"] \
                    if nxt["role"] == "user" else []
                missing = set(ids) - set(got)
                if missing:
                    err("V07.missing_result", f"tool_use without result: {sorted(missing)}", where)

        if role == "user":
            got = [b.get("tool_use_id") for b in content if b.get("type") == "tool_result"]
            if got:
                prev = msgs[k - 1] if k > 0 else None
                ids = {b.get("id") for b in prev["content"] if b.get("type") == "tool_use"} \
                    if prev and prev["role"] == "assistant" else set()
                extra = set(got) - ids
                if extra:
                    err("V07.orphan_result", f"tool_result without a matching tool_use just before: "
                        f"{sorted(extra)}", where)
                if len(got) != len(set(got)):
                    err("V07.duplicate_result", "duplicate tool_result ids", where)
                types = [b.get("type") for b in content]
                first_other = next((i for i, t in enumerate(types) if t != "tool_result"), len(types))
                if "tool_result" in types[first_other:]:
                    err("V08.results_first", "tool_result blocks must come first in the message", where)

    if thinking_had is not None and thinking_kept is not None and thinking_kept:
        pos = [thinking_had.index(k) for k in thinking_kept if k in thinking_had]
        if len(pos) != len(thinking_kept) or pos != list(range(pos[0], pos[0] + len(pos))):
            err("V09.thinking_gap", "kept thinking must form one contiguous run of turns "
                "(remove from the front, the back, or all)")

    if preamble is not None and preamble.known:
        if compare_key(req.system) != compare_key(preamble.system):
            err("V10.preamble_system", "system prompt differs from the frozen preamble")
        if compare_key(req.tools) != compare_key(preamble.tools):
            err("V10.preamble_tools", "tool definitions differ from the frozen preamble")

    if known_hashes is not None:
        for k, m in enumerate(msgs):
            for j, b in enumerate(m["content"]):
                if b.get("type") in THINKING_TYPES and block_hash(b) not in known_hashes:
                    err("V11.opaque_changed", "thinking block does not match any stored block",
                        f"messages[{k}].content[{j}]")
    return v
