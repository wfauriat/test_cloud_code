"""The assembler: events + ops (+ preamble, brief) -> the request actually sent.  PLAN §4 step 4.

One pure function, called by the UI preview, the CLI, experiments and the live loop (PLAN D4).

Thinking modes
- "keep":      thinking blocks go out as stored, unless an op dropped them. Live sessions use
               this; a rebuild records its strips as `assembler` drop ops (see plan_rebuild), so
               they stay stripped on every later request.
- "strip_all": no thinking at all. Used for imports and A/B arms (PLAN D12): imported thinking
               is bound to a system prompt and tools we do not have.
"""

from __future__ import annotations

from typing import Any, Literal

from .model import Diagnostic, Event, Op, Preamble, RenderResult, Request, Source, Span
from .ops import active_ops, fold, inserts_by_anchor
from .repair import Item, RMsg, placeholder, repair
from .segment import text_of
from .tokens import estimate_raw

ThinkingMode = Literal["keep", "strip_all"]


def render(messages: list[Event], ops: list[Op], *, preamble: Preamble, params: dict[str, Any],
           thinking: ThinkingMode = "keep", brief: str | None = None,
           include_staged: bool = True) -> RenderResult:
    events = [e for e in messages if e.is_message]
    index = {(e.id, i): b for e in events for i, b in enumerate(e.blocks)}

    def block_of(s: Span):
        return index.get(s.address)

    act = active_ops(ops, include_staged)
    by_id = {o.id: o for o in act}
    plans = fold(act, block_of)
    inserts = inserts_by_anchor(act)
    calls = {b.raw.get("id"): b.raw for e in events for b in e.blocks if b.type == "tool_use"}

    diags: list[Diagnostic] = []
    rmsgs: list[RMsg] = []
    dropped_calls: set[str] = set()
    stripped = 0

    for e in events:
        m = RMsg(e.role or "user", had_thinking=any(b.is_thinking for b in e.blocks))
        for i, b in enumerate(e.blocks):
            plan = plans.get((e.id, i))
            ids = tuple(plan.op_ids) if plan else ()
            why = "; ".join(by_id[x].rationale for x in ids if x in by_id and by_id[x].rationale) \
                or "removed by the user"
            if b.is_thinking and thinking == "strip_all":
                stripped += 1
            elif plan is None or plan.action == "keep":
                m.items.append(Item(b.raw, Source("event", e.id, i)))
            elif plan.action == "drop":
                if b.type == "tool_result":
                    m.items.append(Item(_stub_result(b.raw, calls, why), Source("placeholder", e.id, i, ids)))
                elif b.type == "tool_use":
                    dropped_calls.add(b.raw.get("id"))
                    note = placeholder(f"a call to {b.raw.get('name')} and its result", why,
                                       "call the tool again if it is needed")
                    m.items.append(Item({"type": "text", "text": note}, Source("note", e.id, i, ids)))
                # other dropped blocks (text, thinking, images) simply disappear
            else:  # rewrite
                new = _rewrite(b.raw, plan.text or "", calls, why)
                if new is not None:
                    m.items.append(Item(new, Source("edited", e.id, i, ids)))
            for op in inserts.get((e.id, i), []):
                m.items.append(Item({"type": "text", "text": op.payload["text"]},
                                    Source("inserted", op_ids=(op.id,))))
        rmsgs.append(m)

    if stripped:
        diags.append(Diagnostic("render.thinking_stripped", f"stripped {stripped} thinking block(s)"))
    if brief:
        rmsgs.append(RMsg("system", [Item({"type": "text", "text": brief}, Source("brief"))]))

    rmsgs, rdiags = repair(rmsgs, dropped_calls)
    diags += rdiags

    out_msgs: list[dict[str, Any]] = []
    smap: dict[tuple[int, int], Source] = {}
    had, kept = [], []
    for k, m in enumerate(rmsgs):
        out_msgs.append({"role": m.role, "content": [it.raw for it in m.items]})
        for j, it in enumerate(m.items):
            smap[(k, j)] = it.source
        if m.role == "assistant":
            if m.had_thinking:
                had.append(k)
            if any(it.raw.get("type") in ("thinking", "redacted_thinking") for it in m.items):
                kept.append(k)

    req = Request(params=dict(params), system=list(preamble.system), tools=list(preamble.tools),
                  messages=out_msgs)
    return RenderResult(req, smap, diags, thinking_had=had, thinking_kept=kept)


def _stub_result(raw: dict[str, Any], calls: dict[str, dict], why: str) -> dict[str, Any]:
    call = calls.get(raw.get("tool_use_id"), {})
    tokens = estimate_raw(raw)
    what = f"the output of {_call_label(call)} (~{tokens:,} tokens)"
    out = {k: v for k, v in raw.items() if k not in ("content", "cache_control")}
    out["content"] = placeholder(what, why)
    return out


def _rewrite(raw: dict[str, Any], text: str, calls: dict[str, dict], why: str) -> dict[str, Any] | None:
    if raw.get("type") == "tool_result":
        if not text.strip():
            return _stub_result(raw, calls, why)
        out = {k: v for k, v in raw.items() if k not in ("content", "cache_control")}
        out["content"] = text
        return out
    if not text.strip():
        return None  # an empty text block is invalid; the whole block goes
    out = {k: v for k, v in raw.items() if k not in ("text", "citations", "cache_control")}
    out["text"] = text
    return out


def _call_label(call: dict[str, Any]) -> str:
    if not call:
        return "a tool call"
    inp = call.get("input") or {}
    arg = next((str(v) for k, v in inp.items() if k in ("file_path", "path", "command", "pattern")), "")
    if len(arg) > 60:
        arg = arg[:57] + "..."
    return f"{call.get('name')}({arg})" if arg else str(call.get("name"))


def block_text(raw: dict[str, Any]) -> str:  # re-export for callers that only import render
    return text_of(raw)
