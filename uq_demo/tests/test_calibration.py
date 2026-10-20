import numpy as np
import pytest
from fastapi.testclient import TestClient

from api.main import app
from uq_core import calibration as cal
from uq_core import params


def _spec():
    return params.normalize_spec({"cd": {"std": 0.05}, "mass": {"std": 0.05}})


def test_experiment_is_reproducible_and_noisy():
    spec = _spec()
    a = cal.make_experiment(spec, ["cd"], {"cd": 0.3}, n_obs=6, noise=1.0, seed=3)
    b = cal.make_experiment(spec, ["cd"], {"cd": 0.3}, n_obs=6, noise=1.0, seed=3)
    assert a["obs"] == b["obs"] and len(a["theta"]) == 6
    clean = cal.simulate_shots(spec, ["cd"], np.array([[0.3]]), np.array(a["theta"]), ["range"], 0.01)["range"][0]
    assert 0 < np.std(np.array(a["obs"]["range"]) - clean) < 3


def test_grid_posterior_concentrates_on_truth():
    spec = _spec()
    ex = cal.make_experiment(spec, ["cd"], {"cd": 0.32}, n_obs=10, noise=0.5)
    out = cal.calibrate(spec, ["cd"], ex["theta"], ex["obs"], 0.5, method="grid", truth={"cd": 0.32})
    row = out["summary"][0]
    assert row["truth_in_ci"]
    assert row["post_std"] < 0.25 * row["prior_std"]
    assert out["prediction"]["posterior"]["std"] < out["prediction"]["prior"]["std"]


def test_grid_density_integrates_to_one():
    spec = _spec()
    ex = cal.make_experiment(spec, ["cd", "mass"], {"cd": 0.3, "mass": 0.43}, n_obs=5)
    out = cal.calibrate(spec, ["cd", "mass"], ex["theta"], ex["obs"], 1.0, method="grid")
    ax = out["grid"]["axes"]
    for j, m in enumerate(out["grid"]["marginals"]):
        assert np.trapezoid(m, ax[j]) == pytest.approx(1.0, abs=0.02)
    # only Cd/m enters the equations: drag and mass are strongly correlated a posteriori
    assert out["correlation"][0][1] > 0.8


@pytest.mark.parametrize("emulator", [True, False])
def test_mcmc_agrees_with_grid(emulator):
    spec = _spec()
    ex = cal.make_experiment(spec, ["cd"], {"cd": 0.3}, n_obs=8, noise=1.0)
    g = cal.calibrate(spec, ["cd"], ex["theta"], ex["obs"], 1.0, method="grid")["summary"][0]
    m = cal.calibrate(spec, ["cd"], ex["theta"], ex["obs"], 1.0, method="mcmc", use_emulator=emulator,
                      n_walkers=24, n_iter=200, burn=60)
    s = m["summary"][0]
    assert s["post_mean"] == pytest.approx(g["post_mean"], abs=0.3 * g["post_std"] + 1e-3)
    assert s["post_std"] == pytest.approx(g["post_std"], rel=0.3)
    assert 0.2 < m["mcmc"]["acceptance"] < 0.95


def test_invalid_requests():
    spec = _spec()
    with pytest.raises(ValueError):
        cal.check_names(spec, ["theta"])
    with pytest.raises(ValueError):
        cal.check_names(spec, ["v0", "cd", "cl", "wind"])
    client = TestClient(app)
    r = client.post("/api/calibration/experiment", json={"names": ["cd"], "truth": {}})
    assert r.status_code == 400


def test_calibration_endpoints():
    client = TestClient(app)
    ex = client.post("/api/calibration/experiment", json={"names": ["cd"], "truth": {"cd": 0.3}, "n_obs": 5,
                                                           "qois": ["range", "max_height"], "gust_std": 1.0}).json()
    assert set(ex["obs"]) == {"range", "max_height"}
    out = client.post("/api/calibration/run", json={"names": ["cd"], "theta": ex["theta"], "obs": ex["obs"],
                                                    "sigma": 1.0, "truth": {"cd": 0.3}}).json()
    assert out["summary"][0]["name"] == "cd" and len(out["predictive_curve"]["prior"]["p50"]) == 33


def test_unmodelled_gusts_make_the_posterior_overconfident():
    spec = params.normalize_spec(None)

    def coverage(gust, sigma):
        hits = 0
        for seed in range(10):
            ex = cal.make_experiment(spec, ["cd"], {"cd": 0.286}, n_obs=12, noise=1.0, gust_std=gust, seed=seed)
            r = cal.calibrate(spec, ["cd"], ex["theta"], ex["obs"], sigma, truth={"cd": 0.286})["summary"][0]
            hits += r["truth_in_ci"]
        return hits

    assert coverage(3.0, 1.0) <= 6  # model error ignored: the 95% interval misses the truth too often
    assert coverage(3.0, 4.0) >= 8  # inflating the noise to absorb it restores coverage
