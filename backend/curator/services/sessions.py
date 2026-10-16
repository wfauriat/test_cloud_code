"""Sessions: import, load, and the derived views (composition, usage timeline, calibration).
PLAN §5.1. Services glue the store to the pure core; they hold no logic of their own beyond that.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..adapters.importers import claude_code
from ..adapters.store import Store
from ..core import rules
from ..core.model import Event, Op, Preamble
from ..core.ops import pinned_addresses
from ..core.render import ThinkingMode, render
from ..core.tokens import Calibration, calibrate, estimate_raw

DEFAULT_MODEL = "claude-opus-5-5"
CACHE_BREAK_MIN_TOKENS = 1024


@dataclass
class SessionView:
    id: str
    info: dict[str, Any]
    preamble: Preamble
    events: list[Event]  # the current chain, root to head
    ops: list[Op]

    @property
    def messages(self) -> list[Event]:
        return [e for e in self.events if e.is_message]

    @property
    def source(self) -> str:
        return self.info["source"]

    @property
    def is_import(self) -> bool:
        return self.source != "live"

    @property
    def toolset(self) -> str:
        return self.info["config"].get("toolset", "claude_code" if self.is_import else "live")


def import_claude_code(store: Store, path: str | Path) -> str:
    path = Path(path)
    with path.open(encoding="utf-8") as f:
        parsed = claude_code.parse(f, name=path.stem)
    sid = store.create_session(parsed.title, "claude_code_import", preamble=parsed.preamble, config={
        "source_path": str(path), "toolset": "claude_code", "model": parsed.model or DEFAULT_MODEL})
    parent = None
    for ev in parsed.events:
        e = store.add_event(sid, ev.kind, role=ev.role, blocks=ev.blocks, parent_id=parent, meta=ev.meta,
                            commit=False, set_head=False)
        parent = e.id
    if parent:
        store.set_head(sid, parent)
    store.commit()
    view = load(store, sid)
    cal = calibration(view)
    store.observe(sid, "import", {
        "path": str(path), "stats": parsed.stats, "preamble": parsed.preamble.note,
        "composition": composition(view), "calls": len(usage_timeline(view)),
        "cache_breaks": sum(1 for r in usage_timeline(view) if r["cache_break"]),
        "calibration": cal.__dict__ if cal else None})
    store.observe(sid, "rules", rules_summary(view))
    return sid


def load(store: Store, sid: str) -> SessionView:
    return SessionView(sid, store.session(sid), store.preamble(sid), store.chain(sid), store.ops(sid))


def block_tokens(view: SessionView) -> dict[tuple[str, int], int]:
    """Estimated tokens per block. Thinking text is empty under display "omitted", so for imports
    the thinking tokens reported in usage are split evenly over that message's thinking blocks."""
    out: dict[tuple[str, int], int] = {}
    for e in view.messages:
        thinking = [i for i, b in enumerate(e.blocks) if b.is_thinking]
        reported = ((e.meta.get("usage") or {}).get("output_tokens_details") or {}).get("thinking_tokens")
        hint = reported // len(thinking) if reported and thinking else None
        for i, b in enumerate(e.blocks):
            out[(e.id, i)] = estimate_raw(b.raw, hint=hint if b.is_thinking else None)
    return out


def category(e: Event, b) -> str:
    if b.origin == "harness" or e.role == "system":
        return "harness"
    if b.origin == "curator":
        return "curator"
    if b.is_thinking:
        return "thinking"
    if b.type in ("tool_use", "tool_result"):
        return b.type
    if b.type == "text":
        return "assistant_text" if e.role == "assistant" else "user_text"
    return b.type


def composition(view: SessionView) -> dict[str, int]:
    toks = block_tokens(view)
    out: dict[str, int] = {}
    for e in view.messages:
        for i, b in enumerate(e.blocks):
            c = category(e, b)
            out[c] = out.get(c, 0) + toks[(e.id, i)]
    return dict(sorted(out.items(), key=lambda kv: -kv[1]))


def usage_timeline(view: SessionView) -> list[dict[str, Any]]:
    """One row per API call found in the log (assistant messages carrying usage). PLAN Q2, Q7.

    A cache break is a call that read clearly less than the previous call had cached
    (read + written). The reason is a guess: a long gap suggests expiry, a new system prompt
    snapshot suggests a rewrite, anything else is "prefix changed".
    """
    toks = block_tokens(view)
    rows: list[dict[str, Any]] = []
    est_before = 0
    snapshot_changed = False
    last_system = None
    prev = None
    for e in view.events:
        if e.kind == "import_meta" and e.meta.get("system_hash"):
            if last_system is not None and e.meta["system_hash"] != last_system:
                snapshot_changed = True
            last_system = e.meta["system_hash"]
            continue
        if not e.is_message:
            continue
        u = e.meta.get("usage")
        if e.role == "assistant" and u:
            cc = u.get("cache_creation") or {}
            write = u.get("cache_creation_input_tokens", 0)
            row = {
                "n": len(rows), "event_id": e.id, "seq": e.seq, "timestamp": e.meta.get("timestamp"),
                "uncached": u.get("input_tokens", 0), "cache_read": u.get("cache_read_input_tokens", 0),
                "cache_write": write, "output": u.get("output_tokens", 0),
                "ttl": "1h" if cc.get("ephemeral_1h_input_tokens") else "5m",
                "est_messages_before": est_before, "cache_break": False, "lost": 0, "reason": None,
            }
            row["total_input"] = row["uncached"] + row["cache_read"] + row["cache_write"]
            if prev is not None:
                cached_before = prev["cache_read"] + prev["cache_write"]
                lost = cached_before - row["cache_read"]
                if lost > max(CACHE_BREAK_MIN_TOKENS, 0.02 * cached_before):
                    gap = _gap_seconds(prev["timestamp"], row["timestamp"])
                    ttl_s = 3600 if prev["ttl"] == "1h" else 300
                    row.update(cache_break=True, lost=lost, gap_seconds=gap, reason=(
                        f"expired? ({gap:.0f}s gap > {prev['ttl']} TTL)" if gap and gap > ttl_s
                        else "system prompt changed" if snapshot_changed else "prefix changed"))
            snapshot_changed = False
            rows.append(row)
            prev = row
        est_before += sum(toks[(e.id, i)] for i in range(len(e.blocks)))
    return rows


def _gap_seconds(a: str | None, b: str | None) -> float | None:
    from datetime import datetime
    if not a or not b:
        return None
    try:
        return (datetime.fromisoformat(b.replace("Z", "+00:00"))
                - datetime.fromisoformat(a.replace("Z", "+00:00"))).total_seconds()
    except ValueError:
        return None


def calibration(view: SessionView) -> Calibration | None:
    return calibrate([(r["est_messages_before"], r["total_input"]) for r in usage_timeline(view)])


def proposals(view: SessionView) -> list[rules.Proposal]:
    """Rule proposals for blocks that no active op already targets."""
    taken = {t.address for o in view.ops if o.state != "revoked" and o.verb != "pin" for t in o.targets}
    props = rules.propose(view.messages, toolset=view.toolset, pinned=pinned_addresses(view.ops))
    return [p for p in props if p.op.targets[0].address not in taken]


def rules_summary(view: SessionView) -> dict[str, Any]:
    by_rule: dict[str, dict[str, int]] = {}
    for p in proposals(view):
        r = by_rule.setdefault(p.rule, {"count": 0, "tokens_saved": 0})
        r["count"] += 1
        r["tokens_saved"] += p.tokens_saved
    return {"by_rule": by_rule, "total_tokens_saved": sum(r["tokens_saved"] for r in by_rule.values())}


def default_params(view: SessionView) -> dict[str, Any]:
    cfg = view.info["config"]
    return {
        "model": cfg.get("model", DEFAULT_MODEL),
        "max_tokens": cfg.get("max_tokens", 16000),
        "thinking": {"type": "adaptive", "display": cfg.get("thinking_display", "summarized")},
        "output_config": {"effort": cfg.get("effort", "medium")},
    }


def messages_before_call(view: SessionView, call_n: int) -> list[Event]:
    """The chain up to (not including) the n-th assistant call: what that call was sent."""
    row = usage_timeline(view)[call_n]
    out = []
    for e in view.events:
        if e.id == row["event_id"]:
            break
        out.append(e)
    return out


def cut(view: SessionView, at_event: str | None = None, call_n: int | None = None) -> list[Event]:
    if call_n is not None:
        return messages_before_call(view, call_n)
    if at_event is None:
        return view.events
    out = []
    for e in view.events:
        out.append(e)
        if e.id == at_event:
            break
    return out


def render_view(view: SessionView, *, events: list[Event] | None = None, include_staged: bool = True,
                brief: str | None = None, thinking: ThinkingMode | None = None):
    mode: ThinkingMode = thinking or ("strip_all" if view.is_import else "keep")
    return render(events if events is not None else view.events, view.ops, preamble=view.preamble,
                  params=default_params(view), thinking=mode, brief=brief, include_staged=include_staged)
