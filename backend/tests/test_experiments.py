"""Next-step A/B and the LLM draft summary, with a scripted provider."""

from factories import claude_code_jsonl

from curator.adapters.provider import ScriptedProvider
from curator.adapters.store import Store
from curator.services import experiments as X
from curator.services import sessions as S
from curator.services import staging


def setup(tmp_path):
    path = tmp_path / "s.jsonl"
    path.write_text("\n".join(claude_code_jsonl()))
    store = Store(":memory:")
    sid = S.import_claude_code(store, path)
    [p] = [p for p in S.proposals(S.load(store, sid)) if p.rule == "R2"]
    staging.create_op(store, sid, verb="drop", targets=[t.to_dict() for t in p.op.targets], rationale=p.rationale)
    store.add_brief_item(sid, "goal", "fix a.py")
    return store, sid


def test_preview_builds_four_valid_arms_that_differ_where_expected(tmp_path):
    store, sid = setup(tmp_path)
    pv = X.preview_ab(store, None, sid, {"call_n": 2, "arms": list(X.ARMS)})
    arms = {a["arm"]: a for a in pv["arms"]}
    assert set(arms) == set(X.ARMS) and all(a["validation"] == [] for a in arms.values())
    assert arms["curated"]["tokens_est"] < arms["as_is"]["tokens_est"]
    assert arms["server_clear"]["betas"] == [X.BETA_CONTEXT_MANAGEMENT]
    assert arms["as_is"]["shared_with_first"] == 0 and arms["curated"]["shared_with_first"] > 0
    assert arms["server_clear"]["shared_with_first"] == 0  # server clearing breaks the cache where it clears


def test_run_records_proposed_next_steps_without_executing(tmp_path):
    store, sid = setup(tmp_path)
    reply = {"content": [{"type": "text", "text": "Next I will run the tests."},
                         {"type": "tool_use", "id": "x", "name": "Bash", "input": {"command": "pytest"}}],
             "stop_reason": "tool_use"}
    p = ScriptedProvider([reply] * 4)
    out = X.run_ab(store, p, sid, {"call_n": 2, "arms": list(X.ARMS), "keep_n": 1})
    assert [a["arm"] for a in out["arms"]] == list(X.ARMS)
    assert out["arms"][0]["tool_calls"] == [{"name": "Bash", "input": {"command": "pytest"}}]
    server_body = p.requests[2]
    assert server_body["context_management"]["edits"][0]["keep"] == {"type": "tool_uses", "value": 1}
    assert p.betas[2] == [X.BETA_CONTEXT_MANAGEMENT]
    assert all(b["type"] != "thinking" for r in p.requests for m in r["messages"] for b in m["content"])  # D12
    assert p.requests[3]["messages"][-1]["role"] == "system"  # the brief arm
    X.record_verdict(store, sid, out["id"], {"preferred": "curated", "notes": "same plan, fewer tokens"})
    assert store.runs(sid)[0]["verdict"]["preferred"] == "curated"


def test_draft_summary_becomes_ops_only_when_accepted(tmp_path):
    store, sid = setup(tmp_path)
    view = S.load(store, sid)
    msg = next(e for e in view.messages if e.role == "assistant" and len(e.blocks) == 3)
    targets = [{"event_id": msg.id, "index": i} for i in range(3)]
    p = ScriptedProvider([{"content": [{"type": "text", "text": "Read a.py and listed files."}]}])
    d = X.draft_summary(store, p, sid, targets)
    assert d["draft"] == "Read a.py and listed files." and len(store.ops(sid)) == 1  # nothing staged yet
    assert p.requests[0]["model"] == X.SUMMARY_MODEL
    try:
        X.accept_summary(store, sid, targets, d["draft"], d["call"])
        raise AssertionError("an assistant message of thinking + tool calls has no block that can hold text")
    except staging.OpRejected:
        pass
    result_msg = next(e for e in view.messages if e.role == "user" and e.blocks[0].type == "tool_result")
    ops = X.accept_summary(store, sid, [{"event_id": result_msg.id, "index": 0}], d["draft"], d["call"])
    assert ops[0].verb == "replace" and ops[0].author == f"llm:{d['call']}"
