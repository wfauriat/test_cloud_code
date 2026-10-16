"""Staging: create and check ops, and preview what staged ops would do.  PLAN §5.2.

The preview answers the question at the heart of the build (Q4): compared with sending the
history as it is, what does sending it with these edits change, and what does it cost?
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from ..adapters.store import Store, new_id
from ..core.costs import edit_economics
from ..core.model import Event, Op, Span
from ..core.ops import check_op, pinned_addresses
from ..core.prefix import diff
from ..core.validate import validate
from .sessions import SessionView, calibration, load, render_view


class OpRejected(ValueError):
    pass


def create_op(store: Store, sid: str, *, verb: str, targets: list[dict], payload: dict | None = None,
              author: str = "human", rationale: str = "", state: str = "staged", group: str | None = None) -> Op:
    view = load(store, sid)
    index = {(e.id, i): b for e in view.messages for i, b in enumerate(e.blocks)}
    op = Op(new_id(), verb, [Span.from_dict(t) for t in targets], payload or {}, author, rationale, state, group)
    errors = check_op(op, lambda s: index.get(s.address), pinned_addresses(view.ops))
    if errors:
        raise OpRejected("; ".join(errors))
    store.add_op(sid, op)
    store.observe(sid, "op_created", {"op": op.id, "verb": verb, "author": author, "state": state})
    return op


def preview(view: SessionView, *, events: list[Event] | None = None, warm: bool = True,
            ttl: str = "5m", brief: str | None = None) -> dict[str, Any]:
    """Render without staged ops (what is on the wire now) and with them; diff and price both."""
    base = render_view(view, events=events, include_staged=False)
    staged = render_view(view, events=events, include_staged=True, brief=brief)
    d = diff(base.request, staged.request)
    cal = calibration(view)
    scale, pre = (cal.scale, cal.preamble_tokens) if cal and cal.scale > 0 else (1.0, 0.0)

    def t(x: int) -> int:
        return int(x * scale + pre)

    tokens_before = d.common_tokens + d.a_after_tokens
    tokens_after = d.common_tokens + d.b_after_tokens
    econ = edit_economics(view.info["config"].get("model"), tokens_before=t(tokens_before),
                          tokens_after=t(tokens_after), divergence_tokens=t(d.common_tokens), warm=warm, ttl=ttl,
                          thinking_blocks_lost=len(d.thinking_lost))
    return {
        "diff": {**asdict(d), "summary": d.summary(), "safe": d.safe},
        "economics": {**asdict(econ), "summary": econ.summary()},
        "calibrated": cal is not None,
        "validation_base": [asdict(x) for x in validate(base.request, thinking_had=base.thinking_had,
                                                         thinking_kept=base.thinking_kept)],
        "validation_staged": [asdict(x) for x in validate(staged.request, thinking_had=staged.thinking_had,
                                                           thinking_kept=staged.thinking_kept)],
        "diagnostics": [asdict(x) for x in staged.diagnostics],
        "messages_base": len(base.request.messages),
        "messages_staged": len(staged.request.messages),
    }
