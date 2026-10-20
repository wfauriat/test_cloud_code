from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_meta():
    r = client.get("/api/meta")
    assert r.status_code == 200
    assert {p["name"] for p in r.json()["params"]} == {"v0", "theta", "cd", "cl", "mass", "wind"}


def test_simulate_and_convergence():
    r = client.post("/api/simulate", json={"spec": {"v0": {"value": 25}}}).json()
    assert r["qoi"]["range"] > 0 and len(r["trajectory"]["x"]) > 10 and len(r["sweep"]["theta"]) == 87
    c = client.post("/api/simulate/convergence", json={}).json()
    assert c["range_error"][0] < c["range_error"][-1]


def test_full_workflow():
    p = client.post("/api/propagate", json={"n": 500, "target": 55, "tol": 3}).json()
    assert len(p["qoi"]["range"]["values"]) == 500 and "risk" in p
    d = client.post("/api/doe", json={"n": 40, "method": "lhs_opt"}).json()
    t = client.post("/api/surrogate/train", json={"names": d["names"], "box": d["box"], "X": d["X"], "kind": "gp"}).json()
    mid = t["model"]["id"]
    assert t["test"]["r2"] > 0.95
    assert client.post("/api/surrogate/slice", json={"model_id": mid, "param": "wind"}).status_code == 200
    assert client.post("/api/surrogate/surface", json={"model_id": mid, "px": "v0", "py": "theta", "n_grid": 10}).status_code == 200
    s = client.post("/api/sensitivity", json={"method": "sobol", "model_id": mid, "n_base": 256}).json()
    assert s["model"] == "surrogate" and len(s["rows"]) == len(d["names"])
    for m in ("oat", "morris"):
        assert client.post("/api/sensitivity", json={"method": m}).status_code == 200
    lc = client.post("/api/surrogate/learning_curve", json={"names": d["names"], "box": d["box"], "kinds": ["poly2"], "sizes": [10, 20]}).json()
    assert len(lc["curves"]["poly2"]["r2"]) == 2


def test_robust_endpoints():
    r = client.post("/api/robust", json={"design": ["theta"], "bounds": [[10, 60]], "grid": 8, "n_mc": 64, "n_train": 60}).json()
    assert set(r["optima"]) == {"deterministic", "mean_var", "chance"}
    t = client.post("/api/robust/tolerance", json={"design": ["v0", "theta"], "std_max": [2, 3], "grid": 4, "n_mc": 64}).json()
    assert len(t["p_hit"]) == 4


def test_errors_are_400():
    assert client.post("/api/surrogate/slice", json={"model_id": "nope", "param": "v0"}).status_code == 400
    assert client.post("/api/doe", json={"names": ["foo"]}).status_code == 400
    assert client.post("/api/robust", json={"design": ["v0", "theta", "cd"], "bounds": [[1, 2]] * 3}).status_code == 400
