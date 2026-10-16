"""Repair rules: keep a rendered request structurally valid after ops.  PLAN §4 step 5.

Every rule that fires is reported as a Diagnostic, so nothing is changed silently.
The rules are deterministic: the same input always gives the same bytes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .model import Diagnostic, Source

DEFAULT_HOW = "re-run the tool if it is needed again"


def placeholder(what: str, why: str, how: str = DEFAULT_HOW) -> str:
    """The stub convention (spec §8.2): what was here · why removed · how to recover.
    # QUESTION: the live preamble explains this convention to the model; imports have no such
    # explanation, so A/B arms on imports see unexplained placeholders.
    """
    return f"[curator: removed {what} · {why} · {how}]"


@dataclass
class Item:
    raw: dict[str, Any]
    source: Source


@dataclass
class RMsg:
    role: str
    items: list[Item] = field(default_factory=list)
    had_thinking: bool = False


def repair(msgs: list[RMsg], dropped_calls: set[str]) -> tuple[list[RMsg], list[Diagnostic]]:
    diags: list[Diagnostic] = []
    msgs = _remove_orphan_results(msgs, dropped_calls, diags)
    msgs = _drop_empty(msgs, diags)
    msgs = _merge_same_role(msgs, diags)
    msgs = _fix_system_placement(msgs, diags)
    msgs = _merge_same_role(msgs, diags)
    _tool_results_first(msgs, diags)
    msgs = _no_trailing_assistant(msgs, diags)
    return msgs, diags


def _remove_orphan_results(msgs, dropped_calls, diags):
    if not dropped_calls:
        return msgs
    n = 0
    for m in msgs:
        keep = [it for it in m.items
                if not (it.raw.get("type") == "tool_result" and it.raw.get("tool_use_id") in dropped_calls)]
        n += len(m.items) - len(keep)
        m.items = keep
    if n:
        diags.append(Diagnostic("repair.orphan_results", f"removed {n} result(s) of dropped tool calls"))
    return msgs


def _drop_empty(msgs, diags):
    keep = [m for m in msgs if m.items]
    if len(keep) != len(msgs):
        diags.append(Diagnostic("repair.empty", f"removed {len(msgs) - len(keep)} empty message(s)"))
    return keep


def _merge_same_role(msgs, diags):
    out: list[RMsg] = []
    merged = 0
    for m in msgs:
        if out and out[-1].role == m.role:
            out[-1].items.extend(m.items)
            out[-1].had_thinking = out[-1].had_thinking or m.had_thinking
            merged += 1
        else:
            out.append(RMsg(m.role, list(m.items), m.had_thinking))
    if merged:
        diags.append(Diagnostic("repair.merge", f"merged {merged} adjacent same-role message(s)"))
    return out


def _fix_system_placement(msgs, diags):
    """A mid-conversation system message must follow a user message and be last or be
    followed by an assistant message. Imports break this (Claude Code renders some harness
    text as system messages in places we cannot reproduce), so misplaced ones are folded into
    the neighbouring user message as text.  # QUIRK: see docs/quirks.md
    """
    out: list[RMsg] = []
    folded = 0
    for k, m in enumerate(msgs):
        if m.role != "system":
            out.append(m)
            continue
        prev_ok = bool(out) and out[-1].role == "user"
        nxt = msgs[k + 1] if k + 1 < len(msgs) else None
        next_ok = nxt is None or nxt.role == "assistant"
        if prev_ok and next_ok:
            out.append(m)
        elif nxt is not None and nxt.role == "user":
            nxt.items[:0] = m.items  # fold forward into the next user message
            folded += 1
        elif out and out[-1].role == "user":
            out[-1].items.extend(m.items)
            folded += 1
        else:
            out.append(RMsg("user", m.items))
            folded += 1
    if folded:
        diags.append(Diagnostic("repair.system_fold",
                                f"folded {folded} misplaced system message(s) into user messages"))
    return out


def _tool_results_first(msgs, diags):
    moved = 0
    for m in msgs:
        if m.role != "user":
            continue
        results = [it for it in m.items if it.raw.get("type") == "tool_result"]
        if not results:
            continue
        others = [it for it in m.items if it.raw.get("type") != "tool_result"]
        reordered = results + others
        if [id(i) for i in reordered] != [id(i) for i in m.items]:
            m.items = reordered
            moved += 1
    if moved:
        diags.append(Diagnostic("repair.results_first",
                                f"moved tool results first in {moved} user message(s)"))


def _no_trailing_assistant(msgs, diags):
    n = 0
    while msgs and msgs[-1].role == "assistant":
        msgs = msgs[:-1]
        n += 1
    if n:
        diags.append(Diagnostic("repair.trailing_assistant",
                                "removed a trailing assistant message (no prefill on current models)"))
    return msgs
