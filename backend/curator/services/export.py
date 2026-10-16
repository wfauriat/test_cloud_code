"""Session export and the exact wire requests.  PLAN §4.5 (portable, diffable JSONL).

One JSON object per line, each with a "kind": session, event, op, call, brief_item, run, observation.
Calls carry the request exactly as sent (expanded from the content-addressed store) and the raw
response, so the file is enough to replay or diff the session outside the curator.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from ..adapters.store import Store
from ..core.wire import dumps
from .loop import _assemble, expand


def call_detail(store: Store, sid: str, call_id: str | None = None) -> dict[str, Any]:
    """The exact request body sent for a call (default: the latest), with its raw response."""
    calls = store.calls(sid)
    if not calls:
        raise KeyError("no calls in this session")
    c = next((x for x in calls if x["id"] == call_id), None) if call_id else calls[-1]
    if c is None:
        raise KeyError(call_id)
    return {"id": c["id"], "n": calls.index(c), "epoch": c["epoch"], "created_at": c["created_at"],
            "request": expand(store, c["request"]).to_api(), "response": c["response"], "usage": c["usage"],
            "cost": c["cost"], "error": c["error"]}


def pending_request(store: Store, sid: str) -> dict[str, Any]:
    """What would be sent if the waiting request were approved now (same assembly as the send)."""
    a = _assemble(store, sid, provider=None)
    return {"hash": a["hash"], "request": a["render"].request.to_api(),
            "validation": [p.__dict__ for p in a["problems"]]}


def export_lines(store: Store, sid: str) -> Iterator[str]:
    info = store.session(sid)
    yield dumps({"kind": "session", **info})
    for e in store.events(sid):
        yield dumps({"kind": "event", "id": e.id, "seq": e.seq, "parent_id": e.parent_id, "type": e.kind,
                     "role": e.role, "meta": e.meta, "blocks": [{"origin": b.origin, "raw": b.raw} for b in e.blocks]})
    for o in store.ops(sid):
        yield dumps({"kind": "op", "id": o.id, "seq": o.seq, "verb": o.verb,
                     "targets": [t.to_dict() for t in o.targets],
                     "payload": o.payload, "author": o.author, "rationale": o.rationale, "state": o.state,
                     "group": o.group})
    for c in store.calls(sid):
        row: dict[str, Any] = {k: v for k, v in c.items() if k != "request"}
        row["request"] = expand(store, c["request"]).to_api()
        yield dumps({"kind": "call", **row})
    for b in store.brief_items(sid):
        yield dumps({"kind": "brief_item", **b})
    for r in store.runs(sid):
        yield dumps({"kind": "run", **_rename_kind(r, "run_kind")})
    for o in store.observations(sid):
        yield dumps({"kind": "observation", **_rename_kind(o, "observation_kind")})


def _rename_kind(row: dict[str, Any], name: str) -> dict[str, Any]:
    """Rows that have their own `kind` keep it under another name; `kind` is the record type."""
    return {(name if k == "kind" else k): v for k, v in row.items()}


def export_jsonl(store: Store, sid: str) -> str:
    return "\n".join(export_lines(store, sid)) + "\n"
