"""Experiments: next-step A/B and the LLM draft summary.  PLAN §5.4, D9, D10, D12; Q5, Q8.

Next-step A/B: replay one cut point under several contexts and compare what the model *proposes*
to do next. Tools are declared but never executed, so no isolation is needed.
- Arms: as_is (history as it is), curated (staged ops applied), server_clear (as_is plus the
  server's clear_tool_uses, keep N; the baseline the curator must beat), curated_brief.
- All arms: same model, effort and stand-in preamble; all thinking stripped (D12).
- Arms run one after another with automatic caching, so later arms can read the prefix they
  share with earlier ones.

Draft summary: the core tension in its smallest form. A side call drafts text; it becomes an op
(author "llm:<call>") only when the user accepts it, and is frozen from then on.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from ..adapters.provider import Provider
from ..adapters.store import Store, new_id
from ..core.costs import estimate_call, usage_cost
from ..core.model import Preamble, Request, Span
from ..core.prefix import diff
from ..core.render import render
from ..core.segment import editable, text_of
from ..core.validate import validate
from ..core.wire import positions
from . import staging
from .brief import render_brief
from .sessions import DEFAULT_MODEL, SessionView, cut, load

ARMS = ("as_is", "curated", "server_clear", "curated_brief")
BETA_CONTEXT_MANAGEMENT = "context-management-2025-06-27"
STANDIN_SYSTEM = ("You are a coding agent continuing the session below. Decide and take your next step. "
                  "(Stand-in system prompt: the session's original prompt is not fully known to the curator.)")
EST_OUTPUT_TOKENS = 1500
SUMMARY_MODEL = "claude-haiku-5-5"
SUMMARY_PROMPT = ("Summarize this excerpt of a coding-agent session so that the summary can replace it in the "
                  "agent's context. Keep file paths, commands, decisions, errors and numbers exactly. Say what "
                  "was found, not how. Output only the summary.\n\n<excerpt>\n{excerpt}\n</excerpt>")


def standin_preamble(view: SessionView, system_text: str | None = None) -> Preamble:
    """Imports: the logged system prompt snapshot when there is one (or `system_text`), and tool
    definitions for every tool name used in the history. # QUIRK: definitions not in the log are
    stand-ins (open schema), so tool calls in the arms are only indicative."""
    if not view.is_import:
        return view.preamble
    known = {t["name"]: t for t in view.preamble.tools if t.get("name")}
    names = sorted({b.raw.get("name") for e in view.messages for b in e.blocks if b.type == "tool_use"} - {None})
    tools = [{k: known[n][k] for k in ("name", "description", "input_schema") if k in known[n]} if n in known else
             {"name": n, "description": "Stand-in: the original definition is not in the log.",
              "input_schema": {"type": "object", "additionalProperties": True}} for n in names]
    system = [{"type": "text", "text": system_text}] if system_text else (
        view.preamble.system or [{"type": "text", "text": STANDIN_SYSTEM}])
    return Preamble(system=system, tools=tools, known=False, note="stand-in for experiments")


def arm_request(view: SessionView, arm: str, spec: dict[str, Any], brief: str | None) -> tuple[Request, list[str], Any]:
    events = cut(view, call_n=spec.get("call_n"))
    params: dict[str, Any] = {"model": spec.get("model") or DEFAULT_MODEL, "max_tokens": spec.get("max_tokens", 4096),
                              "thinking": {"type": "adaptive", "display": "summarized"},
                              "output_config": {"effort": spec.get("effort", "medium")},
                              "cache_control": {"type": "ephemeral"}}
    betas: list[str] = []
    if arm == "server_clear":
        keep = int(spec.get("keep_n", 3))
        params["context_management"] = {"edits": [{"type": "clear_tool_uses_20250919",
                                                   "trigger": {"type": "tool_uses", "value": keep + 1},
                                                   "keep": {"type": "tool_uses", "value": keep}}]}
        betas.append(BETA_CONTEXT_MANAGEMENT)
    res = render(events, view.ops, preamble=standin_preamble(view, spec.get("system_text")), params=params,
                 thinking="strip_all", include_staged=arm in ("curated", "curated_brief"),
                 brief=brief if arm == "curated_brief" else None)
    return res.request, betas, res


def preview_ab(store: Store, provider: Provider | None, sid: str, spec: dict[str, Any]) -> dict[str, Any]:
    view = load(store, sid)
    brief = render_brief(store.brief_items(sid))
    arms = [a for a in spec.get("arms", ARMS) if a in ARMS and (a != "curated_brief" or brief)]
    out, first = [], None
    for arm in arms:
        req, betas, res = arm_request(view, arm, spec, brief)
        problems = validate(req, thinking_had=res.thinking_had, thinking_kept=res.thinking_kept)
        tokens = sum(p.tokens for p in positions(req))
        # server clearing invalidates the cache from where it clears, so that arm reads nothing (conservative)
        shared = diff(first, req).common_tokens if first is not None and arm != "server_clear" else 0
        first = first or req
        exact = None
        if provider is not None:
            try:
                exact = provider.count_tokens(req.to_api(), betas=betas)
            except Exception:  # noqa: BLE001 - the estimate stands
                exact = None
        est = estimate_call(req.params["model"], exact or tokens, shared, warm=shared > 0,
                            output_tokens=EST_OUTPUT_TOKENS)
        out.append({"arm": arm, "messages": len(req.messages), "tokens_est": tokens, "tokens_exact": exact,
                    "shared_with_first": shared, "validation": [asdict(x) for x in problems],
                    "cost_est": est.total, "betas": betas})
    return {"arms": out, "total_cost_est": sum(a["cost_est"] for a in out), "brief": bool(brief)}


def run_ab(store: Store, provider: Provider, sid: str, spec: dict[str, Any]) -> dict[str, Any]:
    view = load(store, sid)
    brief = render_brief(store.brief_items(sid))
    arms = [a for a in spec.get("arms", ARMS) if a in ARMS and (a != "curated_brief" or brief)]
    rid = store.add_run(sid, "next_step_ab", spec)
    results = []
    for arm in arms:
        req, betas, res = arm_request(view, arm, spec, brief)
        problems = validate(req, thinking_had=res.thinking_had, thinking_kept=res.thinking_kept)
        if problems:
            results.append({"arm": arm, "error": "invalid request: " + "; ".join(p.code for p in problems)})
            continue
        try:
            r = provider.send(req.to_api(), betas=betas)
        except Exception as e:  # noqa: BLE001 - recorded, the other arms still run
            results.append({"arm": arm, "error": str(e)[:2000]})
            continue
        results.append({
            "arm": arm, "stop_reason": r.stop_reason, "model": r.model, "usage": r.usage,
            "cost": usage_cost(r.model, r.usage),
            "text": "\n\n".join(b.get("text", "") for b in r.content if b.get("type") == "text"),
            "tool_calls": [{"name": b.get("name"), "input": b.get("input")} for b in r.content
                           if b.get("type") == "tool_use"],
            "thinking_summary": "\n".join(b.get("thinking", "") for b in r.content if b.get("type") == "thinking"),
            "applied_edits": (r.raw.get("context_management") or {}).get("applied_edits"),
        })
    result = {"arms": results, "total_cost": sum(a.get("cost", 0) for a in results)}
    store.set_run(rid, result=result)
    store.observe(sid, "ab_run", {"run": rid, "spec": spec, "costs": {a["arm"]: a.get("cost") for a in results},
                                  "errors": {a["arm"]: a["error"] for a in results if "error" in a}})
    return {"id": rid, **result}


def record_verdict(store: Store, sid: str, rid: str, verdict: dict[str, Any]) -> None:
    store.set_run(rid, verdict=verdict)
    store.observe(sid, "ab_verdict", {"run": rid, **verdict})


def draft_summary(store: Store, provider: Provider, sid: str, targets: list[dict[str, Any]],
                  model: str = SUMMARY_MODEL) -> dict[str, Any]:
    view = load(store, sid)
    index = {(e.id, i): (e, b) for e in view.messages for i, b in enumerate(e.blocks)}
    parts = []
    for t in targets:
        e, b = index[(t["event_id"], int(t["index"]))]
        label = f"{e.role} {b.type}" + (f" {b.raw.get('name')}" if b.type == "tool_use" else "")
        parts.append(f"[{label}]\n{text_of(b.raw)}")
    body = {"model": model, "max_tokens": 2000, "output_config": {"effort": "low"},
            "messages": [{"role": "user", "content": [{"type": "text", "text": SUMMARY_PROMPT.format(
                excerpt="\n\n".join(parts))}]}]}
    r = provider.send(body)
    cid = new_id()
    cost = usage_cost(r.model, r.usage)
    store.observe(sid, "side_call", {"call": cid, "purpose": "draft_summary", "model": r.model, "usage": r.usage,
                                     "cost": cost, "targets": len(targets)})
    text = "\n".join(b.get("text", "") for b in r.content if b.get("type") == "text").strip()
    return {"draft": text, "call": cid, "model": r.model, "cost": cost}


def accept_summary(store: Store, sid: str, targets: list[dict[str, Any]], text: str, call_id: str) -> list[Any]:
    """The accepted draft is frozen into ops: replace the first editable block, drop the rest (one group)."""
    view = load(store, sid)
    index = {(e.id, i): b for e in view.messages for i, b in enumerate(e.blocks)}
    group, author = new_id(), f"llm:{call_id}"
    spans = [Span(t["event_id"], int(t["index"])) for t in targets]
    first = next((s for s in spans if editable(index[s.address].raw)), None)
    if first is None:
        raise staging.OpRejected("the selection has no text block or tool result to hold the summary")
    text = f"[curator: summary of {len(spans)} block(s), drafted by {author}, accepted by the user]\n{text}"
    ops = [staging.create_op(store, sid, verb="replace", targets=[first.to_dict()], payload={"text": text},
                             author=author, rationale="replaced by an accepted LLM summary", group=group)]
    for s in spans:
        if s != first:
            ops.append(staging.create_op(store, sid, verb="drop", targets=[s.to_dict()], author=author,
                                         rationale="covered by an accepted LLM summary", group=group))
    return ops
