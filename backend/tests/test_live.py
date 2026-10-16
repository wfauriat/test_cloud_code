"""Live loop with a scripted provider: gates, the append-only verifier, ingestion, rebuild."""

import pytest

from curator.adapters.provider import ScriptedProvider
from curator.adapters.store import Store
from curator.core.prefix import diff
from curator.services import loop, staging


def thinking(sig):
    return {"type": "thinking", "thinking": "", "signature": sig}


@pytest.fixture
def env(tmp_path):
    ws = tmp_path / "ws"
    ws.mkdir()
    (ws / "a.py").write_text("def f():\n    return 1\n")
    store = Store(":memory:")
    sid = loop.create_live(store, title="t", workspace=str(ws))
    return store, sid, ws


def test_read_only_tool_runs_without_a_tool_gate_and_requests_stay_append_only(env):
    store, sid, _ = env
    p = ScriptedProvider([
        {"content": [thinking("s1"), {"type": "tool_use", "id": "t1", "name": "read_file", "input": {"path": "a.py"}}],
         "stop_reason": "tool_use"},
        {"content": [thinking("s2"), {"type": "text", "text": "It returns 1."}], "stop_reason": "end_turn"},
    ])
    v = loop.send_user_message(store, p, sid, "What does f return?")
    assert v["state"] == "prompt_gate" and v["pending"]["verdict"] == "first"
    v = loop.approve_prompt(store, p, sid, v["pending"]["hash"])
    assert v["state"] == "prompt_gate"  # read_file is allowlisted: ran without a tool gate
    assert v["pending"]["verdict"] == "append_only"
    v = loop.approve_prompt(store, p, sid, v["pending"]["hash"])
    assert v["state"] == "idle" and v["calls"] == 2
    r1, r2 = p.requests
    assert r2["messages"][2]["content"][0]["content"] == "def f():\n    return 1\n"
    assert r2["messages"][: len(r1["messages"])] == r1["messages"]  # byte-identical prefix
    assert r1["system"] == r2["system"] and r1["tools"] == r2["tools"]
    kinds = [o["kind"] for o in store.observations(sid)]
    assert kinds.count("gate") == 3 and kinds.count("call") == 2, kinds


def test_approval_is_tied_to_the_hash(env):
    store, sid, _ = env
    p = ScriptedProvider([])
    v = loop.send_user_message(store, p, sid, "hi")
    v = loop.approve_prompt(store, p, sid, "stale-hash")
    assert v["state"] == "prompt_gate" and "changed" in v["note"] and p.requests == []


def test_write_needs_review_and_modify_runs_the_edited_call(env):
    store, sid, ws = env
    p = ScriptedProvider([
        {"content": [{"type": "tool_use", "id": "t1", "name": "write_file", "input": {"path": "b.py", "content": "x"}}],
         "stop_reason": "tool_use"},
        {"content": [{"type": "text", "text": "done"}], "stop_reason": "end_turn"},
    ])
    v = loop.send_user_message(store, p, sid, "write b.py")
    v = loop.approve_prompt(store, p, sid, v["pending"]["hash"])
    assert v["state"] == "tool_gate" and v["tool_cards"][0]["effects"]["creates"]
    v = loop.decide_tools(store, p, sid, {"t1": {"action": "modify", "input": {"path": "b.py", "content": "y"}}})
    assert (ws / "b.py").read_text() == "y"
    v = loop.approve_prompt(store, p, sid, v["pending"]["hash"])
    sent = p.requests[1]["messages"]
    assert sent[1]["content"][0]["input"] == {"path": "b.py", "content": "x"}  # the model's call, byte-exact
    assert sent[2]["content"][0]["content"].startswith("[the user modified this call")


def test_path_outside_workspace_is_refused(env):
    store, sid, _ = env
    p = ScriptedProvider([
        {"content": [{"type": "tool_use", "id": "t1", "name": "read_file", "input": {"path": "../secret"}}],
         "stop_reason": "tool_use"},
    ])
    v = loop.send_user_message(store, p, sid, "read it")
    v = loop.approve_prompt(store, p, sid, v["pending"]["hash"])
    result = store.events(sid)[-1].blocks[0].raw
    assert result["is_error"] and "outside the workspace" in result["content"]


def test_oversized_output_is_bounded_at_ingestion(env):
    store, sid, ws = env
    (ws / "big.txt").write_text("".join(f"line {i} " + "x" * 80 + "\n" for i in range(2000)))
    p = ScriptedProvider([
        {"content": [{"type": "tool_use", "id": "t1", "name": "read_file", "input": {"path": "big.txt"}}],
         "stop_reason": "tool_use"},
    ])
    v = loop.send_user_message(store, p, sid, "read big")
    loop.approve_prompt(store, p, sid, v["pending"]["hash"])
    sent = store.events(sid)[-1].blocks[0].raw["content"]
    assert "bounded at ingestion" in sent and sent.count("\n") < 70
    full = [e for e in store.events(sid) if e.kind == "tool_exec"][0].meta["output"]
    assert full.count("\n") == 2000


def test_editing_sent_history_needs_a_rebuild_which_strips_later_thinking(env):
    store, sid, _ = env
    p = ScriptedProvider([
        {"content": [thinking("s1"), {"type": "tool_use", "id": "t1", "name": "read_file", "input": {"path": "a.py"}}],
         "stop_reason": "tool_use"},
        {"content": [thinking("s2"), {"type": "text", "text": "returns 1"}], "stop_reason": "end_turn"},
        {"content": [{"type": "text", "text": "ok"}], "stop_reason": "end_turn"},
    ])
    v = loop.send_user_message(store, p, sid, "read a.py")
    v = loop.approve_prompt(store, p, sid, v["pending"]["hash"])
    v = loop.approve_prompt(store, p, sid, v["pending"]["hash"])
    result_event = [e for e in store.events(sid) if e.is_message and e.blocks[0].type == "tool_result"][0]
    staging.create_op(store, sid, verb="drop", targets=[{"event_id": result_event.id, "index": 0}], rationale="test")
    v = loop.send_user_message(store, p, sid, "next")
    # a staged op on sent content does not reach the wire before a rebuild: still append-only
    assert v["pending"]["verdict"] == "append_only" and v["pending"]["free_ops"] == []
    v = loop.apply_edits(store, p, sid)
    assert "1 thinking block" in v["note"] and v["epoch"] == 2
    assert v["pending"]["verdict"] == "diverge" and v["pending"]["validation"] == []
    v = loop.approve_prompt(store, p, sid, v["pending"]["hash"])
    r2, r3 = p.requests[1], p.requests[2]
    assert "[curator: removed" in r3["messages"][2]["content"][0]["content"]
    assert [b["type"] for b in r3["messages"][1]["content"]] == ["thinking", "tool_use"]  # before the edit: kept
    assert [b["type"] for b in r3["messages"][3]["content"]] == ["text"]  # after the edit: stripped
    d = diff(loop.expand(store, store.calls(sid)[1]["request"]), loop.expand(store, store.calls(sid)[2]["request"]))
    assert d.thinking_at_risk == []
    # the stripped block came from call 2's response, not its request: the strip is a recorded op
    assert [o.author for o in store.ops(sid) if o.verb == "drop"] == ["human", "assembler"]
    assert r2["messages"][:2] == r3["messages"][:2]


def test_reset_from_the_tool_gate_keeps_the_history_valid(env):
    store, sid, _ = env
    p = ScriptedProvider([
        {"content": [{"type": "tool_use", "id": "t1", "name": "write_file", "input": {"path": "b.py", "content": "x"}}],
         "stop_reason": "tool_use"},
        {"content": [{"type": "text", "text": "ok"}], "stop_reason": "end_turn"},
    ])
    v = loop.send_user_message(store, p, sid, "write b.py")
    v = loop.approve_prompt(store, p, sid, v["pending"]["hash"])
    assert v["state"] == "tool_gate"
    v = loop.reset(store, sid)
    assert v["state"] == "idle"
    v = loop.send_user_message(store, p, sid, "never mind")
    assert v["state"] == "prompt_gate" and v["pending"]["validation"] == []


def test_export_carries_the_exact_wire_requests(env):
    import json

    from curator.services import export
    store, sid, _ = env
    p = ScriptedProvider([{"content": [{"type": "text", "text": "hi"}], "stop_reason": "end_turn"}])
    v = loop.send_user_message(store, p, sid, "hello")
    assert export.pending_request(store, sid)["hash"] == v["pending"]["hash"]
    loop.approve_prompt(store, p, sid, v["pending"]["hash"])
    assert export.call_detail(store, sid)["request"] == p.requests[0]  # byte-for-byte what was sent
    rows = [json.loads(x) for x in export.export_jsonl(store, sid).splitlines()]
    kinds = {r["kind"] for r in rows}
    assert {"session", "event", "call", "observation"} <= kinds
    assert next(r for r in rows if r["kind"] == "call")["request"] == p.requests[0]
