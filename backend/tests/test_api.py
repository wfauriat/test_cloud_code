"""API smoke test: every read route answers on an imported synthetic session."""

import importlib

from factories import claude_code_jsonl
from fastapi.testclient import TestClient


def test_routes(tmp_path, monkeypatch):
    monkeypatch.setenv("CURATOR_DB", str(tmp_path / "t.db"))
    from curator.api import app as app_module
    importlib.reload(app_module)
    c = TestClient(app_module.app)
    path = tmp_path / "s.jsonl"
    path.write_text("\n".join(claude_code_jsonl()))
    sid = c.post("/api/sessions/import", json={"path": str(path)}).json()["id"]
    d = c.get(f"/api/sessions/{sid}").json()
    assert d["messages"] > 0 and d["calls"] == 3
    msgs = c.get(f"/api/sessions/{sid}/messages").json()
    first_result = next(m for m in msgs if m["label"] == "tool results")
    assert c.get(f"/api/sessions/{sid}/blocks/{first_result['event_id']}/0").status_code == 200
    assert len(c.get(f"/api/sessions/{sid}/timeline").json()) == 3
    props = c.get(f"/api/sessions/{sid}/proposals").json()
    staged = c.post(f"/api/sessions/{sid}/proposals/stage", json={"ids": None}).json()
    assert len(staged) == len(props) > 0
    msgs = c.get(f"/api/sessions/{sid}/messages").json()
    assert any(b["status"]["pending"] for m in msgs for b in m["blocks"])
    pv = c.get(f"/api/sessions/{sid}/preview", params={"warm": False}).json()
    assert pv["validation_staged"] == []
    c.post(f"/api/sessions/{sid}/brief", json={"type": "goal", "text": "fix a.py"})
    r = c.get(f"/api/sessions/{sid}/request", params={"brief": True, "call": 2}).json()
    assert r["validation"] == [] and r["request"]["messages"][-1]["role"] == "system"
    # after a final assistant message a system message is not allowed: repair turns the brief into user text
    r = c.get(f"/api/sessions/{sid}/request", params={"brief": True}).json()
    assert r["request"]["messages"][-1]["role"] == "user"
    assert any(d["code"] == "repair.system_fold" for d in r["diagnostics"])
    bad = c.post(f"/api/sessions/{sid}/ops", json={"verb": "replace", "targets": [
        {"event_id": msgs[2]["event_id"], "index": 1}], "payload": {"text": "x"}})
    assert bad.status_code == 400
    assert c.post(f"/api/sessions/{sid}/ops/{staged[0]['id']}/revoke").json()["state"] == "revoked"
