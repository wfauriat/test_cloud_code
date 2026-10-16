"""Live loop: a small state machine with two gates.  PLAN §5.3, D1, D2, D6, D7, D8.

States: idle → prompt_gate → (call) → tool_gate → prompt_gate → … → idle
        "blocked" when the validator or the prefix verifier refuses the next request.

Before a request is sent it passes three checks:
1. the validator (structure, frozen preamble, thinking blocks unchanged);
2. approval tied to the request hash: what was approved is exactly what is sent;
3. the prefix verifier: compared with the last request sent, the new one must be append-only,
   unless the user applied edits ("rebuild"), which opens a new epoch.

Edit levels (D2):
- free: ops whose targets are all *after* the last sent request (not sent yet) go out on the
  next call, staged or not;
- rebuild: staged ops on sent content are applied by `apply_edits` at a user-turn boundary;
  thinking produced on the old prefix is stripped then, and the strip is recorded.
Calls are synchronous. # QUESTION: SSE streaming to the UI is deferred.
"""

from __future__ import annotations

from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from ..adapters.executor import Executor
from ..adapters.provider import Provider
from ..adapters.store import Store, new_id, now
from ..core import policy
from ..core.costs import estimate_call, usage_cost
from ..core.model import Block, Op, Preamble, Request, Span
from ..core.prefix import diff
from ..core.render import RenderResult, render
from ..core.repair import placeholder
from ..core.tokens import estimate_text
from ..core.validate import validate
from ..core.wire import compare_key, dumps, positions, request_hash
from . import staging
from .brief import render_brief
from .sessions import DEFAULT_MODEL, default_params, load

SYSTEM_PROMPT = """You are a coding assistant working in a local workspace through tools. Paths are relative \
to the workspace root.

This conversation is curated by the user with a tool called the curator. Parts of earlier tool outputs \
or messages may be replaced by placeholders of the form [curator: removed <what> · <why> · <how to recover>]. \
The content was removed on purpose; trust the placeholder, and if you need the content again, follow its \
recovery hint (for example, read the file again).

A system message starting with "Session brief" is written by the user. It states the current goals, \
constraints and decisions; prefer it over older context."""

BETA_FALLBACK = "server-side-fallback-2026-07-01"
INGEST_MAX_TOKENS = 6000
INGEST_HEAD, INGEST_TAIL = 40, 20
TTL_SECONDS = {"5m": 300, "1h": 3600}
LIVE_DEFAULTS: dict[str, Any] = {"state": "idle", "epoch": 1, "frontier_seq": 0, "pending": None,
                                 "tool_cards": [], "gate_opened_at": None, "auto_continue": False,
                                 "rebuild_pending": False, "note": None}


class LoopError(RuntimeError):
    pass


# -- session --------------------------------------------------------------------------------------
def create_live(store: Store, *, title: str, workspace: str, model: str = DEFAULT_MODEL, effort: str = "medium",
                allow_commands: bool = False, ttl: str = "5m", fallbacks: bool = True) -> str:
    root = Path(workspace).expanduser()
    root.mkdir(parents=True, exist_ok=True)
    ex = Executor(root, allow_commands)
    cc = {"type": "ephemeral", **({"ttl": "1h"} if ttl == "1h" else {})}
    preamble = Preamble(system=[{"type": "text", "text": SYSTEM_PROMPT, "cache_control": cc}],
                        tools=ex.tool_defs(), known=True, note="frozen at session start (PLAN D11)")
    config = {"toolset": "live", "model": model, "effort": effort, "workspace": str(ex.root), "ttl": ttl,
              "allow_commands": allow_commands, "fallbacks": fallbacks, "max_tokens": 32000,
              "live": dict(LIVE_DEFAULTS)}
    sid = store.create_session(title, "live", config=config, preamble=preamble)
    store.observe(sid, "live_created", {k: v for k, v in config.items() if k != "live"})
    return sid


def live_view(store: Store, sid: str) -> dict[str, Any]:
    info = store.session(sid)
    live = info["config"].get("live")
    if live is None:
        raise LoopError("not a live session")
    ops = store.ops(sid)
    return {**live, "staged_ops": sum(o.state == "staged" for o in ops), "calls": len(store.calls(sid)),
            "model": info["config"].get("model"), "workspace": info["config"].get("workspace")}


def set_auto_continue(store: Store, sid: str, on: bool) -> dict[str, Any]:
    live = _live(store, sid)
    live["auto_continue"] = on
    _save(store, sid, live)
    return live_view(store, sid)


# -- user turn ------------------------------------------------------------------------------------
def send_user_message(store: Store, provider: Provider, sid: str, text: str) -> dict[str, Any]:
    live = _live(store, sid)
    if live["state"] not in ("idle", "blocked"):
        raise LoopError(f"cannot send a message while {live['state']}")
    _append(store, sid, "user", [Block({"type": "text", "text": text}, "user")], {"timestamp": now()})
    brief = render_brief(store.brief_items(sid))
    if brief:  # D7: once per user turn, right after the user's message, human-authored only
        _append(store, sid, "system", [Block({"type": "text", "text": brief}, "curator")],
                {"brief": True, "timestamp": now()})
    store.observe(sid, "user_message", {"chars": len(text), "brief": bool(brief)})
    return _open_prompt_gate(store, provider, sid, live)


def reset(store: Store, sid: str) -> dict[str, Any]:
    """Back to idle, keeping the history valid. Calls waiting at the tool gate get a "cancelled"
    result, so the model's tool_use is never left without its tool_result (validator V07)."""
    live = _live(store, sid)
    if live["state"] == "tool_gate" and live["tool_cards"]:
        results = [Block({"type": "tool_result", "tool_use_id": c["id"], "is_error": True,
                          "content": "Cancelled by the user (session reset); the call did not run."}, "tool")
                   for c in live["tool_cards"]]
        _append(store, sid, "user", results, {"timestamp": now(), "reset": True})
    store.observe(sid, "reset", {"from_state": live["state"]})
    live.update(state="idle", pending=None, tool_cards=[], note="reset: send a new message to continue")
    _save(store, sid, live)
    return live_view(store, sid)


def reject_prompt(store: Store, sid: str, reason: str = "") -> dict[str, Any]:
    live = _live(store, sid)
    _gate_observation(store, sid, live, "prompt", "reject", reason=reason)
    live.update(state="idle", pending=None, note="request rejected; edit and send a new message")
    _save(store, sid, live)
    return live_view(store, sid)


def approve_prompt(store: Store, provider: Provider, sid: str, approved_hash: str) -> dict[str, Any]:
    live = _live(store, sid)
    if live["state"] != "prompt_gate":
        raise LoopError("no request is waiting for approval")
    a = _assemble(store, sid, provider=None)
    if a["hash"] != approved_hash:
        return _open_prompt_gate(store, provider, sid, live,
                                 note="the request changed since you saw it; review it again")
    if a["problems"]:
        return _open_prompt_gate(store, provider, sid, live)
    d = a["diff"]
    if d is not None and d.verdict != "append_only" and not live["rebuild_pending"]:
        store.observe(sid, "verifier_block", {"summary": d.summary()})
        live.update(state="blocked", note=f"verifier: next request is not append-only ({d.summary()})")
        _save(store, sid, live)
        return live_view(store, sid)
    _gate_observation(store, sid, live, "prompt", "approve")

    req: Request = a["render"].request
    body = req.to_api()
    betas = [BETA_FALLBACK] if store.session(sid)["config"].get("fallbacks") else []
    try:
        reply = provider.send(body, betas=betas)
    except Exception as e:  # noqa: BLE001 - every API error is an observation for the spec revision
        store.add_call(sid, epoch=live["epoch"], request=_compact(store, req), response=None, usage=None,
                       cost=None, latency_ms=None, model=body.get("model"), stop_reason=None, error=str(e))
        store.observe(sid, "api_error", {"error": str(e)[:4000]})
        live.update(state="prompt_gate", note=f"API error: {str(e)[:300]}")
        _save(store, sid, live)
        return live_view(store, sid)

    cost = usage_cost(reply.model, reply.usage)
    cid = store.add_call(sid, epoch=live["epoch"], request=_compact(store, req), response=reply.raw,
                         usage=reply.usage, cost=cost, latency_ms=reply.latency_ms, model=reply.model,
                         stop_reason=reply.stop_reason)
    for op_id in a["free_ops"]:  # free edits are on the wire now
        store.set_op_state(sid, op_id, "applied")
    note = None
    if reply.model and reply.model != body["model"]:
        note = f"refusal fallback: answered by {reply.model}; cache and thinking do not carry over"
    store.observe(sid, "call", {"call": cid, "epoch": live["epoch"], "verdict": d.verdict if d else "first",
                                "summary": d.summary() if d else "", "cost": cost, "usage": reply.usage,
                                "model": reply.model, "requested_model": body["model"],
                                "stop_reason": reply.stop_reason, "latency_ms": reply.latency_ms})
    live.update(frontier_seq=a["max_seq"], rebuild_pending=False, pending=None, note=note)
    if reply.content:
        _append(store, sid, "assistant", [Block(b, "model") for b in reply.content],
                {"usage": reply.usage, "model": reply.model, "stop_reason": reply.stop_reason, "call_id": cid,
                 "timestamp": now()})
    return _after_reply(store, provider, sid, live, reply.stop_reason, reply.content, reply.stop_details)


def _after_reply(store, provider, sid, live, stop, content, stop_details) -> dict[str, Any]:
    if stop == "tool_use":
        ex = _executor(store, sid)
        cards = []
        for b in content:
            if b.get("type") != "tool_use":
                continue
            err = ex.check_input(b["name"], b.get("input"))
            dec = policy.evaluate("tool_call", b["name"])
            cards.append({"id": b["id"], "name": b["name"], "input": b.get("input"), "policy": dec.decision,
                          "reason": dec.reason, "input_error": err,
                          "effects": ex.effects(b["name"], b["input"]) if not err else {}})
        live.update(tool_cards=cards, gate_opened_at=now())
        if cards and all(c["policy"] == "auto" and not c["input_error"] for c in cards):
            live["state"] = "tool_gate"
            _save(store, sid, live)
            return decide_tools(store, provider, sid, {}, auto=True)
        live["state"] = "tool_gate"
        _save(store, sid, live)
        return live_view(store, sid)
    notes = {
        "max_tokens": "stopped at max_tokens; send 'continue' to resume (tools from this turn were not run)",
        "refusal": f"refusal: {stop_details}",
        "model_context_window_exceeded": "context window exceeded: curate (stage drops, apply edits) and retry",
        # QUESTION: pause_turn needs a request ending on the assistant turn; only server tools pause,
        # and this build declares none.
        "pause_turn": "pause_turn received (server tools are not used here); send a message to continue",
    }
    live.update(state="idle", tool_cards=[], note=notes.get(stop, live.get("note")))
    _save(store, sid, live)
    return live_view(store, sid)


# -- tool gate --------------------------------------------------------------------------------------
def decide_tools(store: Store, provider: Provider, sid: str, decisions: dict[str, dict[str, Any]],
                 auto: bool = False) -> dict[str, Any]:
    live = _live(store, sid)
    if live["state"] != "tool_gate":
        raise LoopError("no tool calls are waiting")
    ex = _executor(store, sid)
    results, actions = [], {}
    for c in live["tool_cards"]:
        d = decisions.get(c["id"]) or ({"action": "approve"} if c["policy"] == "auto" else None)
        if d is None:
            raise LoopError(f"decide every call (missing {c['id']})")
        action = "deny" if c["policy"] == "deny" else d.get("action", "approve")
        actions[c["id"]] = action
        inp = d.get("input") if action == "modify" else c["input"]
        if action == "deny":
            out, is_error, ms = "Denied by the user" + (f": {d['reason']}" if d.get("reason") else "."), True, 0
        elif err := ex.check_input(c["name"], inp):
            out, is_error, ms = f"Error: {err}", True, 0
        else:
            r = ex.run(c["name"], inp)
            out, is_error, ms = r.output, r.is_error, r.ms
            if action == "modify":  # the model's tool_use stays as written; the result says what ran
                out = f"[the user modified this call before it ran; it ran with input {dumps(inp)}]\n{out}"
        _append(store, sid, None, [], {"tool_use_id": c["id"], "name": c["name"], "input": c["input"],
                                       "effective_input": inp, "action": action, "output": out,
                                       "is_error": is_error, "ms": ms}, kind="tool_exec")
        sent, bounded = _ingest(out)
        results.append(Block({"type": "tool_result", "tool_use_id": c["id"], "content": sent,
                              **({"is_error": True} if is_error else {})}, "tool"))
        if bounded:
            store.observe(sid, "ingest_bounded", {"tool_use_id": c["id"], "tokens": estimate_text(out)})
    _gate_observation(store, sid, live, "tool", "auto" if auto else "decided", calls=len(results), actions=actions)
    _append(store, sid, "user", results, {"timestamp": now()})
    live.update(tool_cards=[])
    if live["auto_continue"]:
        a = _assemble(store, sid, provider=None)
        if not a["problems"] and (a["diff"] is None or a["diff"].verdict == "append_only"):
            live.update(state="prompt_gate", gate_opened_at=now())
            _save(store, sid, live)
            return approve_prompt(store, provider, sid, a["hash"])
    return _open_prompt_gate(store, provider, sid, live)


def _ingest(out: str) -> tuple[str, bool]:
    """D6: bound oversized output before it is sent; the tool_exec event keeps it whole."""
    lines = out.splitlines()
    if estimate_text(out) <= INGEST_MAX_TOKENS or len(lines) <= INGEST_HEAD + INGEST_TAIL:
        return out, False
    cut = len(lines) - INGEST_HEAD - INGEST_TAIL
    mid = placeholder(f"{cut} lines from the middle of this output", "bounded at ingestion (oversized)",
                      "re-run with a narrower range or pattern if needed")
    return "\n".join(lines[:INGEST_HEAD] + [mid] + lines[-INGEST_TAIL:]), True


# -- rebuild ------------------------------------------------------------------------------------------
def apply_edits(store: Store, provider: Provider, sid: str) -> dict[str, Any]:
    live = _live(store, sid)
    if live["state"] not in ("idle", "prompt_gate", "blocked"):
        raise LoopError("edits to sent history apply only at a user-turn boundary, not during a tool round")
    view = load(store, sid)
    staged = [o for o in view.ops if o.state == "staged"]
    if not staged:
        raise LoopError("no staged edits")
    cfg = view.info["config"]
    pv = staging.preview(view, warm=_warm(store, sid)[0], ttl=cfg.get("ttl", "5m"))
    for o in staged:
        store.set_op_state(sid, o.id, "applied")
    stripped = 0
    for src in _invalid_thinking(store, sid, _assemble(store, sid, provider=None)["render"]):
        store.add_op(sid, Op(new_id(), "drop", [Span(src.event_id, src.index)], author="assembler", state="applied",
                             rationale="thinking produced on a prefix that changed (rebuild)"))
        stripped += 1
    live.update(rebuild_pending=True, epoch=live["epoch"] + 1)
    store.observe(sid, "rebuild", {"ops": len(staged), "thinking_stripped": stripped, "diff": pv["diff"]["summary"],
                                   "economics": pv["economics"], "epoch": live["epoch"]})
    if live["state"] in ("prompt_gate", "blocked"):
        return _open_prompt_gate(store, provider, sid, live,
                                 note=f"edits applied; {stripped} thinking block(s) stripped")
    live["note"] = f"edits applied; {stripped} thinking block(s) stripped; they go out with your next message"
    _save(store, sid, live)
    return live_view(store, sid)


def _invalid_thinking(store: Store, sid: str, res: RenderResult) -> list:
    """Exact check: a thinking block stays valid only if the request that produced it is still a
    prefix of the new request, and the blocks before it in its own message are unchanged."""
    events = {e.id: e for e in store.events(sid)}
    calls = {c["id"]: c for c in store.calls(sid)}
    pos = positions(res.request)
    at = {p.path: i for i, p in enumerate(pos)}
    cache: dict[str, list] = {}
    bad = []
    for (k, j), src in sorted(res.source_map.items()):
        raw = res.request.messages[k]["content"][j]
        if raw.get("type") not in ("thinking", "redacted_thinking") or src.event_id is None:
            continue
        ev = events[src.event_id]
        cid = ev.meta.get("call_id")
        if cid not in calls:
            bad.append(src)  # unknown producer (e.g. imported): cannot be valid here
            continue
        if cid not in cache:
            cache[cid] = positions(expand(store, calls[cid]["request"]))
        prod = cache[cid]
        i = at[f"messages[{k}].content[{j}]"]
        before = [compare_key(b.raw) for b in ev.blocks[:src.index]]
        here = [p.key for p in pos[i - len(before):i]] if before else []
        if len(prod) > i or any(pos[t].key != prod[t].key for t in range(len(prod))) or here != before:
            bad.append(src)
    return bad


# -- internals ---------------------------------------------------------------------------------------
def _live(store: Store, sid: str) -> dict[str, Any]:
    live = store.session(sid)["config"].get("live")
    if live is None:
        raise LoopError("not a live session")
    return {**LIVE_DEFAULTS, **live}


def _save(store: Store, sid: str, live: dict[str, Any]) -> None:
    cfg = store.session(sid)["config"]
    cfg["live"] = live
    store.update_config(sid, cfg)


def _executor(store: Store, sid: str) -> Executor:
    cfg = store.session(sid)["config"]
    return Executor(cfg["workspace"], cfg.get("allow_commands", False))


def _append(store: Store, sid: str, role: str | None, blocks: list[Block], meta: dict, kind: str = "message"):
    return store.add_event(sid, kind, role=role, blocks=blocks, parent_id=store.session(sid)["head"], meta=meta)


def _compact(store: Store, req: Request) -> dict[str, Any]:
    """Requests are stored as block hashes: hundreds of near-identical prefixes cost almost nothing."""
    return {"params": req.params, "system": [store.put_block(b) for b in req.system],
            "tools": [store.put_block(t) for t in req.tools],
            "messages": [{"role": m["role"], "content": [store.put_block(b) for b in m["content"]]}
                         for m in req.messages]}


def expand(store: Store, c: dict[str, Any]) -> Request:
    hashes = c["system"] + c["tools"] + [h for m in c["messages"] for h in m["content"]]
    blocks = store.get_blocks(hashes)
    return Request(c["params"], [blocks[h] for h in c["system"]], [blocks[h] for h in c["tools"]],
                   [{"role": m["role"], "content": [blocks[h] for h in m["content"]]} for m in c["messages"]])


def _last_request(store: Store, sid: str) -> Request | None:
    ok = [c for c in store.calls(sid) if c["response"] is not None and not c["error"]]
    return expand(store, ok[-1]["request"]) if ok else None


def _warm(store: Store, sid: str) -> tuple[bool, float | None]:
    ok = [c for c in store.calls(sid) if c["response"] is not None]
    if not ok:
        return False, None
    ttl = TTL_SECONDS.get(store.session(sid)["config"].get("ttl", "5m"), 300)
    age = (datetime.now(UTC) - datetime.fromisoformat(ok[-1]["created_at"])).total_seconds()
    return age < ttl, max(ttl - age, 0)


def _wire_ops(view, frontier_seq: int) -> tuple[list[Op], list[str]]:
    seq = {e.id: e.seq for e in view.events}
    free = [o for o in view.ops if o.state == "staged" and o.targets
            and all(seq.get(t.event_id, 0) > frontier_seq for t in o.targets)]
    return [o for o in view.ops if o.state == "applied"] + free, [o.id for o in free]


def _assemble(store: Store, sid: str, provider: Provider | None) -> dict[str, Any]:
    view = load(store, sid)
    cfg = view.info["config"]
    live = {**LIVE_DEFAULTS, **cfg["live"]}
    ops, free = _wire_ops(view, live["frontier_seq"])
    ttl = cfg.get("ttl", "5m")
    params = {**default_params(view), "cache_control": {"type": "ephemeral", **({"ttl": "1h"} if ttl == "1h" else {})},
              **({"fallbacks": "default"} if cfg.get("fallbacks") else {})}
    res: RenderResult = render(view.events, ops, preamble=view.preamble, params=params, thinking="keep")
    problems = validate(res.request, preamble=view.preamble, thinking_had=res.thinking_had,
                        thinking_kept=res.thinking_kept, known_hashes=store.known_block_hashes(sid))
    last = _last_request(store, sid)
    d = diff(last, res.request) if last is not None else None
    tokens = sum(p.tokens for p in positions(res.request))
    warm, expires = _warm(store, sid)
    est = estimate_call(cfg.get("model"), tokens, d.common_tokens if d else 0, warm=warm, ttl=ttl)
    exact = None
    if provider is not None:
        try:
            exact = provider.count_tokens(res.request.to_api(), betas=[])
        except Exception:  # noqa: BLE001 - exact count is a bonus; the estimate stands
            exact = None
    return {"render": res, "problems": problems, "diff": d, "hash": request_hash(res.request), "tokens_est": tokens,
            "tokens_exact": exact, "warm": warm, "cache_expires_in": expires,
            "cost": asdict(est) | {"total": est.total},
            "free_ops": free, "max_seq": max((e.seq for e in view.events if e.is_message), default=0)}


def _open_prompt_gate(store, provider, sid, live, note: str | None = None) -> dict[str, Any]:
    a = _assemble(store, sid, provider)
    d = a["diff"]
    new_blocks = [] if d is None else [p.path for p in positions(a["render"].request)[d.divergence or 0:]
                                       if p.kind not in ("role", "params", "model")]
    live.update(state="blocked" if a["problems"] else "prompt_gate", gate_opened_at=now(), note=note, pending={
        "hash": a["hash"], "tokens_est": a["tokens_est"], "tokens_exact": a["tokens_exact"],
        "verdict": d.verdict if d else "first", "summary": d.summary() if d else "first request of the session",
        "new_blocks": len(new_blocks) if d else len(a["render"].request.messages),
        "validation": [asdict(x) for x in a["problems"]], "diagnostics": [asdict(x) for x in a["render"].diagnostics],
        "cost": a["cost"], "warm": a["warm"], "cache_expires_in": a["cache_expires_in"],
        "free_ops": a["free_ops"], "rebuild_pending": live["rebuild_pending"]})
    _save(store, sid, live)
    return live_view(store, sid)


def _gate_observation(store, sid, live, gate: str, decision: str, **extra) -> None:
    opened = live.get("gate_opened_at")
    seconds = (datetime.now(UTC) - datetime.fromisoformat(opened)).total_seconds() if opened else None
    store.observe(sid, "gate", {"gate": gate, "decision": decision, "seconds": seconds, **extra})
