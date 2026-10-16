"""HTTP API. Routes only: parse, call a service, shape the answer. No logic here.  PLAN §2.

Run:  uv run uvicorn curator.api.app:app --reload --port 8765
Binds to 127.0.0.1 only. # QUESTION: no auth token yet; the live loop (B4) adds an Origin check.
"""

from __future__ import annotations

import os
from dataclasses import asdict
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse

from ..adapters.provider import default_provider
from ..adapters.store import Store
from ..core import costs
from ..core.ops import active_ops, fold
from ..core.segment import segments, text_of
from ..core.tokens import estimate_raw
from ..core.validate import validate
from ..core.wire import dumps, request_hash
from ..services import experiments, export, loop, staging
from ..services import sessions as S
from . import schemas as A

DB = os.environ.get("CURATOR_DB", str(Path(__file__).resolve().parents[3] / "workspace" / "curator.db"))

app = FastAPI(title="Context Curator (exploratory)", version="0.1.0")
store = Store(DB)


def _view(sid: str) -> S.SessionView:
    try:
        return S.load(store, sid)
    except KeyError:
        raise HTTPException(404, f"no session {sid}") from None


# -- sessions -----------------------------------------------------------------------------------
@app.get("/api/sessions", response_model=list[A.SessionSummary])
def list_sessions():
    return store.sessions()


@app.post("/api/sessions/import", response_model=A.SessionSummary)
def import_session(body: A.ImportRequest):
    path = Path(body.path).expanduser()
    if not path.is_file():
        raise HTTPException(400, f"not a file: {path}")
    sid = S.import_claude_code(store, path)
    return next(s for s in store.sessions() if s["id"] == sid)


@app.get("/api/sessions/{sid}", response_model=A.SessionDetail)
def session_detail(sid: str):
    v = _view(sid)
    cal = S.calibration(v)
    stats = next((o["payload"].get("stats") for o in reversed(store.observations(sid)) if o["kind"] == "import"),
                 None)
    return A.SessionDetail(
        id=v.id, title=v.info["title"], source=v.source, config=v.info["config"],
        preamble_note=v.preamble.note, preamble_known=v.preamble.known,
        preamble_system_tokens=sum(estimate_raw(b) for b in v.preamble.system), preamble_tools=len(v.preamble.tools),
        composition=S.composition(v), calibration=A.CalibrationView(**cal.__dict__) if cal else None,
        messages=len(v.messages), calls=len(S.usage_timeline(v)), ops=len(v.ops), import_stats=stats)


@app.get("/api/sessions/{sid}/messages", response_model=list[A.MessageView])
def messages(sid: str):
    v = _view(sid)
    toks = S.block_tokens(v)
    plans_all = fold(active_ops(v.ops, True), _block_of(v))
    plans_applied = fold(active_ops(v.ops, False), _block_of(v))
    calls = {r["event_id"]: r["n"] for r in S.usage_timeline(v)}
    tool_names = {b.raw.get("id"): b.raw.get("name") for e in v.messages for b in e.blocks if b.type == "tool_use"}
    out = []
    for e in v.messages:
        blocks = []
        for i, b in enumerate(e.blocks):
            p, pa = plans_all.get((e.id, i)), plans_applied.get((e.id, i))
            state = "kept" if p is None or p.action == "keep" else ("dropped" if p.action == "drop" else "edited")
            applied_state = "kept" if pa is None or pa.action == "keep" else ("dropped" if pa.action == "drop"
                                                                              else "edited")
            tool_use_id = b.raw.get("id") if b.type == "tool_use" else b.raw.get("tool_use_id")
            blocks.append(A.BlockView(
                index=i, type=b.type, origin=b.origin, category=S.category(e, b), tokens=toks[(e.id, i)],
                text=text_of(b.raw), gist=_gist(b.raw, tool_names), tool_use_id=tool_use_id,
                tool_name=b.raw.get("name") if b.type == "tool_use" else tool_names.get(tool_use_id),
                is_error=bool(b.raw.get("is_error")),
                status=A.BlockStatus(state=state, pending=state != applied_state, pinned=bool(p and p.pinned),
                                     op_ids=p.op_ids if p else [], shadowed=p.shadowed if p else [])))
        out.append(A.MessageView(
            event_id=e.id, seq=e.seq, role=e.role or "user", label=_label(e), timestamp=e.meta.get("timestamp"),
            call_n=calls.get(e.id), tokens=sum(x.tokens for x in blocks), blocks=blocks))
    return out


@app.get("/api/sessions/{sid}/blocks/{event_id}/{index}", response_model=A.BlockDetail)
def block_detail(sid: str, event_id: str, index: int):
    v = _view(sid)
    b = _block_of(v)(_span(event_id, index))
    if b is None:
        raise HTTPException(404, "no such block")
    ops = [_op_view(o) for o in v.ops if any(t.address == (event_id, index) for t in o.targets)]
    props = [_proposal_view(p) for p in S.proposals(v) if p.op.targets[0].address == (event_id, index)]
    return A.BlockDetail(event_id=event_id, index=index, raw=b.raw,
                         segments=[asdict(s) for s in segments(text_of(b.raw), tool_output=b.type == "tool_result")],
                         ops=[o.model_dump() for o in ops], proposals=[p.model_dump() for p in props])


@app.get("/api/sessions/{sid}/timeline", response_model=list[A.TimelineRow])
def timeline(sid: str):
    v = _view(sid)
    model = v.info["config"].get("model")
    rows = []
    for r in S.usage_timeline(v):
        usage = next(e.meta.get("usage") for e in v.messages if e.id == r["event_id"])
        rows.append(A.TimelineRow(**{k: r[k] for k in A.TimelineRow.model_fields if k in r},
                                  cost=costs.usage_cost(model, usage)))
    return rows


@app.get("/api/sessions/{sid}/proposals", response_model=list[A.ProposalView])
def proposals(sid: str):
    return [_proposal_view(p) for p in S.proposals(_view(sid))]


@app.get("/api/sessions/{sid}/observations", response_model=list[A.Observation])
def observations(sid: str):
    return store.observations(sid)


@app.get("/api/observations.jsonl", response_class=PlainTextResponse)
def observations_jsonl():
    return "\n".join(dumps(o) for o in store.observations())


# -- curation (B3) --------------------------------------------------------------------------------
@app.get("/api/sessions/{sid}/ops", response_model=list[A.OpView])
def list_ops(sid: str):
    return [_op_view(o) for o in _view(sid).ops]


@app.post("/api/sessions/{sid}/ops", response_model=A.OpView)
def create_op(sid: str, body: A.OpCreate):
    try:
        op = staging.create_op(store, sid, verb=body.verb, targets=body.targets, payload=body.payload,
                               author=body.author, rationale=body.rationale)
    except staging.OpRejected as e:
        raise HTTPException(400, str(e)) from None
    return _op_view(op)


@app.post("/api/sessions/{sid}/ops/{op_id}/{action}", response_model=A.OpView)
def op_action(sid: str, op_id: str, action: str):
    states = {"revoke": "revoked", "stage": "staged", "unstage": "draft"}
    if action not in states:
        raise HTTPException(400, f"unknown action {action}")
    op = next((o for o in _view(sid).ops if o.id == op_id), None)
    if op is None:
        raise HTTPException(404, "no such op")
    if op.state == "applied" and action != "revoke":
        raise HTTPException(400, "applied ops can only be revoked (and that is a new edit, with its own cost)")
    store.set_op_state(sid, op_id, states[action])
    return _op_view(next(o for o in _view(sid).ops if o.id == op_id))


@app.post("/api/sessions/{sid}/proposals/stage", response_model=list[A.OpView])
def stage_proposals(sid: str, body: A.StageProposals):
    v = _view(sid)
    out = []
    for p in S.proposals(v):
        if body.ids is None or p.op.id in body.ids:
            op = staging.create_op(store, sid, verb=p.op.verb, targets=[t.to_dict() for t in p.op.targets],
                                   payload=p.op.payload, author=p.op.author, rationale=p.rationale)
            out.append(_op_view(op))
    return out


@app.get("/api/sessions/{sid}/preview")
def preview(sid: str, warm: bool = True, ttl: str = "5m", call: int | None = None, brief: bool = False):
    v = _view(sid)
    return staging.preview(v, events=S.cut(v, call_n=call) if call is not None else None, warm=warm, ttl=ttl,
                           brief=_brief_text(sid) if brief else None)


@app.get("/api/sessions/{sid}/request", response_model=A.RenderedRequest)
def rendered_request(sid: str, call: int | None = None, staged: bool = True, brief: bool = False):
    v = _view(sid)
    res = S.render_view(v, events=S.cut(v, call_n=call) if call is not None else None, include_staged=staged,
                        brief=_brief_text(sid) if brief else None)
    problems = validate(res.request, thinking_had=res.thinking_had, thinking_kept=res.thinking_kept)
    smap = [{"message": k, "content": j, **asdict(src)} for (k, j), src in sorted(res.source_map.items())]
    tokens = sum(estimate_raw(b) for m in res.request.messages for b in m["content"])
    return A.RenderedRequest(request=res.request.to_api(), source_map=smap,
                             diagnostics=[asdict(d) for d in res.diagnostics],
                             validation=[asdict(d) for d in problems], tokens_estimated=tokens,
                             hash=request_hash(res.request))


# -- brief (PLAN D7: user-authored only) -------------------------------------------------------------
@app.get("/api/sessions/{sid}/brief", response_model=list[A.BriefItemView])
def brief_items(sid: str):
    return store.brief_items(sid)


@app.post("/api/sessions/{sid}/brief", response_model=A.BriefItemView)
def add_brief_item(sid: str, body: A.BriefItemCreate):
    bid = store.add_brief_item(sid, body.type, body.text)
    return next(b for b in store.brief_items(sid) if b["id"] == bid)


@app.patch("/api/sessions/{sid}/brief/{bid}", response_model=A.BriefItemView)
def update_brief_item(sid: str, bid: str, body: A.BriefItemUpdate):
    store.update_brief_item(sid, bid, text=body.text, status=body.status)
    return next(b for b in store.brief_items(sid) if b["id"] == bid)


@app.get("/api/sessions/{sid}/brief/text", response_class=PlainTextResponse)
def brief_text(sid: str):
    return _brief_text(sid) or ""


# -- live loop (B4) ------------------------------------------------------------------------------
_provider = None


def provider():
    global _provider
    if _provider is None:
        try:
            _provider = default_provider()
        except Exception as e:  # noqa: BLE001
            raise HTTPException(503, f"no model provider ({e}). Set ANTHROPIC_API_KEY, or run the backend with "
                                     "CURATOR_PROVIDER=echo to try the loop without a model.") from None
    return _provider


def _loop(fn, *args):
    try:
        return fn(*args)
    except loop.LoopError as e:
        raise HTTPException(409, str(e)) from None


@app.post("/api/live", response_model=A.SessionSummary)
def create_live(body: A.LiveCreate):
    sid = loop.create_live(store, title=body.title, workspace=body.workspace, model=body.model, effort=body.effort,
                           allow_commands=body.allow_commands, ttl=body.ttl, fallbacks=body.fallbacks)
    return next(s for s in store.sessions() if s["id"] == sid)


@app.get("/api/sessions/{sid}/live")
def live_state(sid: str):
    return _loop(loop.live_view, store, sid)


@app.post("/api/sessions/{sid}/live/message")
def live_message(sid: str, body: A.LiveMessage):
    return _loop(loop.send_user_message, store, provider(), sid, body.text)


@app.post("/api/sessions/{sid}/live/approve")
def live_approve(sid: str, body: A.LiveApprove):
    return _loop(loop.approve_prompt, store, provider(), sid, body.hash)


@app.post("/api/sessions/{sid}/live/reset")
def live_reset(sid: str):
    return _loop(loop.reset, store, sid)


@app.post("/api/sessions/{sid}/live/reject")
def live_reject(sid: str, body: A.LiveReject):
    return _loop(loop.reject_prompt, store, sid, body.reason)


@app.post("/api/sessions/{sid}/live/tools")
def live_tools(sid: str, body: A.LiveTools):
    return _loop(loop.decide_tools, store, provider(), sid, body.decisions)


@app.post("/api/sessions/{sid}/live/apply-edits")
def live_apply(sid: str):
    return _loop(loop.apply_edits, store, provider(), sid)


@app.post("/api/sessions/{sid}/live/settings")
def live_settings(sid: str, body: A.LiveSettings):
    return _loop(loop.set_auto_continue, store, sid, body.auto_continue)


@app.get("/api/sessions/{sid}/calls/{call_id}")
def call_detail(sid: str, call_id: str):
    """The exact request body sent for this call ("latest" for the last one) and the raw response."""
    try:
        return export.call_detail(store, sid, None if call_id == "latest" else call_id)
    except KeyError as e:
        raise HTTPException(404, str(e)) from None


@app.get("/api/sessions/{sid}/live/pending-request")
def pending_request(sid: str):
    return _loop(export.pending_request, store, sid)


@app.get("/api/sessions/{sid}/export.jsonl", response_class=PlainTextResponse)
def export_session(sid: str):
    _view(sid)
    return PlainTextResponse(export.export_jsonl(store, sid), headers={
        "content-disposition": f'attachment; filename="curator-session-{sid}.jsonl"'})


@app.get("/api/sessions/{sid}/calls", response_model=list[A.CallSummary])
def calls(sid: str):
    return [{k: c[k] for k in A.CallSummary.model_fields} for c in store.calls(sid)]


# -- experiments (B5) ---------------------------------------------------------------------------
def _provider_or_none():
    try:
        return provider()
    except HTTPException:
        return None


@app.post("/api/sessions/{sid}/ab/preview")
def ab_preview(sid: str, body: A.ABSpec):
    return experiments.preview_ab(store, _provider_or_none(), sid, body.model_dump())


@app.post("/api/sessions/{sid}/ab/run")
def ab_run(sid: str, body: A.ABSpec):
    return experiments.run_ab(store, provider(), sid, body.model_dump())


@app.get("/api/sessions/{sid}/ab/runs")
def ab_runs(sid: str):
    return store.runs(sid)


@app.post("/api/sessions/{sid}/ab/runs/{rid}/verdict")
def ab_verdict(sid: str, rid: str, body: A.ABVerdict):
    experiments.record_verdict(store, sid, rid, body.model_dump())
    return {"ok": True}


@app.post("/api/sessions/{sid}/summarize")
def summarize(sid: str, body: A.SummaryRequest):
    return experiments.draft_summary(store, provider(), sid, body.targets, body.model)


@app.post("/api/sessions/{sid}/summarize/accept", response_model=list[A.OpView])
def summarize_accept(sid: str, body: A.SummaryAccept):
    try:
        return [_op_view(o) for o in experiments.accept_summary(store, sid, body.targets, body.text, body.call_id)]
    except staging.OpRejected as e:
        raise HTTPException(400, str(e)) from None


# -- helpers --------------------------------------------------------------------------------------
def _brief_text(sid: str) -> str | None:
    from ..services.brief import render_brief
    return render_brief(store.brief_items(sid))


def _span(event_id: str, index: int):
    from ..core.model import Span
    return Span(event_id, index)


def _block_of(v: S.SessionView):
    index = {(e.id, i): b for e in v.messages for i, b in enumerate(e.blocks)}
    return lambda s: index.get(s.address)


def _label(e) -> str:
    if e.meta.get("attachment_type"):
        return f"harness: {e.meta['attachment_type']}"
    if e.role == "user" and e.meta.get("is_meta"):
        return "harness: injected"
    if e.role == "user" and e.blocks and all(b.type == "tool_result" for b in e.blocks):
        return "tool results"
    return e.role or "?"


def _gist(raw: dict, tool_names: dict) -> str:
    t = raw.get("type")
    if t == "tool_use":
        inp = raw.get("input") or {}
        arg = next((str(v) for k, v in inp.items() if k in ("file_path", "path", "command", "pattern", "url")), "")
        return f"{raw.get('name')}({arg[:80]})"
    if t == "tool_result":
        body = text_of(raw)
        n = body.count("\n") + 1 if body else 0
        return f"→ {tool_names.get(raw.get('tool_use_id'), 'result')}: {n} line{'s' if n != 1 else ''}"
    if t in ("thinking", "redacted_thinking"):
        return "thinking (hidden)" if not raw.get("thinking") else raw["thinking"].strip().splitlines()[0][:100]
    body = text_of(raw).strip()
    return body.splitlines()[0][:100] if body else f"[{t}]"


def _op_view(o) -> A.OpView:
    return A.OpView(id=o.id, verb=o.verb, targets=[t.to_dict() for t in o.targets], payload=o.payload,
                    author=o.author, rationale=o.rationale, state=o.state, seq=o.seq)


def _proposal_view(p) -> A.ProposalView:
    return A.ProposalView(id=p.op.id, rule=p.rule, rationale=p.rationale, verb=p.op.verb,
                          targets=[t.to_dict() for t in p.op.targets], payload=p.op.payload,
                          tokens_before=p.tokens_before, tokens_after=p.tokens_after, tokens_saved=p.tokens_saved)
