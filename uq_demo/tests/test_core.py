import numpy as np
import pytest

from uq_core import doe, params, propagation, robust, sensitivity, surrogate
from uq_core.ballistics import G, simulate, vacuum_trajectory


def test_euler_converges_to_vacuum_parabola_at_first_order():
    exact = vacuum_trajectory(30, 45)["range"]
    errs = [abs(simulate(30, 45, dt=dt).range[0] - exact) for dt in (0.02, 0.01, 0.005)]
    assert errs[2] < errs[1] < errs[0]
    assert errs[0] / errs[1] == pytest.approx(2.0, rel=0.3)  # O(dt)


def test_rk4_matches_vacuum_parabola():
    sim = simulate(25, 30, dt=0.01, scheme="rk4")
    assert sim.range[0] == pytest.approx(25**2 * np.sin(np.radians(60)) / G, rel=1e-5)


def test_drag_shortens_and_tailwind_lengthens():
    base = simulate(30, 40, cd=0.25, mass=0.43).range[0]
    assert base < vacuum_trajectory(30, 40)["range"]
    assert simulate(30, 40, cd=0.25, mass=0.43, wind=5).range[0] > base
    assert simulate(30, 40, cd=0.25, mass=0.43, wind=-5).range[0] < base
    # heavier ball -> drag matters less
    assert simulate(30, 40, cd=0.25, mass=2.0).range[0] > base
    # backspin lift carries the ball further
    assert simulate(30, 40, cd=0.25, cl=0.15, mass=0.43).range[0] > base


def test_vectorised_matches_scalar():
    v0 = np.array([20.0, 30.0, 40.0])
    vec = simulate(v0, 35, 0.3, 0.05, 0.43, 2.0)
    for i, v in enumerate(v0):
        assert vec.range[i] == pytest.approx(simulate(v, 35, 0.3, 0.05, 0.43, 2.0).range[0])


def test_per_trajectory_dt():
    r = simulate(30, 45, dt=np.array([0.02, 0.001]))
    assert abs(r.range[1] - vacuum_trajectory(30, 45)["range"]) < abs(r.range[0] - vacuum_trajectory(30, 45)["range"])


def test_trajectory_recording_ends_on_ground():
    r = simulate(np.full(5, 30.0), 40, record=3, max_points=50)
    assert len(r.trajectories) == 3
    for t in r.trajectories:
        assert t[0].tolist() == [0.0, 0.0]
        assert t[-1, 1] == 0.0
        assert len(t) <= 51


@pytest.mark.parametrize("dist", ["normal", "uniform", "lognormal"])
def test_marginals_have_requested_moments(dist):
    d = params.marginal({"value": 2.0, "std": 0.3, "dist": dist})
    assert d.mean() == pytest.approx(2.0)
    assert d.std() == pytest.approx(0.3)


def test_monte_carlo_matches_fosm_for_small_uncertainty():
    spec = params.normalize_spec({"wind": {"std": 0.5}, "cd": {"std": 0.01}})
    out = propagation.monte_carlo(spec, 4000, "sobol", target=50, tol=2)
    mc = out["qoi"]["range"]["stats"]
    assert out["fosm"]["std"] == pytest.approx(mc["std"], rel=0.1)
    assert 0 <= out["risk"]["p_miss"] <= 1


@pytest.mark.parametrize("method", doe.METHODS)
def test_doe_in_unit_cube(method):
    U = doe.unit_design(method, 27, 3)
    assert U.min() >= 0 and U.max() <= 1 and U.shape[1] == 3


def test_lhs_is_stratified():
    U = doe.unit_design("lhs", 10, 2)
    for j in range(2):
        assert sorted(np.floor(U[:, j] * 10).astype(int)) == list(range(10))


@pytest.mark.parametrize("kind", list(surrogate.KINDS))
def test_surrogates_learn_the_model(kind):
    spec = params.normalize_spec(None)
    names = ["v0", "theta"]
    box = [(20.0, 40.0), (20.0, 60.0)]
    X = doe.scale(doe.unit_design("lhs_opt", 60, 2), box)
    out = surrogate.train(spec, names, box, X, kind, "range", n_test=200)
    assert out["test"]["r2"] > (0.85 if kind in ("rf", "poly1", "mlp") else 0.97)
    s = surrogate.get(out["model"]["id"])
    assert len(surrogate.slice_1d(s, "theta")["x"]) == 120


def test_sobol_indices_on_additive_function():
    # f = x1 + 2 x2 with independent N(0,1)-like inputs -> S = (1/5, 4/5), no interactions
    spec = params.normalize_spec({"v0": {"value": 30, "std": 1.0}, "theta": {"value": 40, "std": 1.0}})
    fn = lambda X: X[:, 0] + 2 * X[:, 1]  # noqa: E731
    out = sensitivity.sobol(fn, spec, ["v0", "theta"], n_base=2048, n_boot=20)
    s1 = {r["name"]: r["S1"] for r in out["rows"]}
    st = {r["name"]: r["ST"] for r in out["rows"]}
    assert s1["v0"] == pytest.approx(0.2, abs=0.03) and s1["theta"] == pytest.approx(0.8, abs=0.03)
    assert st["v0"] == pytest.approx(0.2, abs=0.03) and st["theta"] == pytest.approx(0.8, abs=0.03)
    assert out["cost"]["evaluations"] == 2048 * 4


def test_morris_and_oat_rank_wind_first():
    spec = params.normalize_spec({"wind": {"std": 4.0}})
    names = params.uncertain_names(spec)
    fn = lambda X: params.evaluate(spec, names, X, "range")  # noqa: E731
    assert sensitivity.oat(fn, spec, names)["rows"][0]["name"] == "wind"
    mo = sensitivity.morris(fn, spec, names, r=10)
    assert max(mo["rows"], key=lambda r: r["mu_star"])["name"] == "wind"


def test_robust_beats_deterministic_on_hit_probability():
    spec = params.normalize_spec(None)
    out = robust.optimize(spec, ["v0", "theta"], [(20, 45), (15, 70)], target=55, tol=3,
                          n_mc=128, grid=15, n_train=120)
    det, ch = out["optima"]["deterministic"], out["optima"]["chance"]
    assert det["nominal"] == pytest.approx(55, abs=0.5)
    assert ch["validation"]["p_hit"] > det["validation"]["p_hit"]
    assert ch["x"]["theta"] < det["x"]["theta"]  # flatter shots are less wind-sensitive


def test_tolerance_study_probability_decreases_with_spread():
    spec = params.normalize_spec({"wind": {"uncertain": False}, "cd": {"uncertain": False}})
    out = robust.tolerance_study(spec, ["v0"], "range", 52.3, 2, [4.0], grid=6, n_mc=200)
    p = np.array(out["p_hit"])
    assert p[0] == pytest.approx(1.0) and p[-1] < p[0]


def test_gp_std_vanishes_at_training_points_and_slices_through_them():
    spec = params.normalize_spec(None)
    names = params.uncertain_names(spec)
    box = params.box_from_spec(spec, names)
    X = doe.scale(doe.unit_design("lhs_opt", 40, len(names)), box)
    s = surrogate.get(surrogate.train(spec, names, box, X, "gp", "range")["model"]["id"])
    _, sd = s.predict(s.X, return_std=True)
    assert sd.max() < 2e-3  # deterministic simulator: the GP interpolates the training points
    # a slice through training point 0 passes through it: distance 0 and minimal std there
    p0 = dict(zip(names, s.X[0]))
    sl = surrogate.slice_1d(s, names[0], anchor=p0)
    assert sl["train_dist"][0] == pytest.approx(0.0, abs=1e-12)
    k = int(np.argmin(np.abs(np.array(sl["x"]) - s.X[0, 0])))
    assert sl["std"][k] < 0.5 * max(sl["std"])
    sf = surrogate.surface_2d(s, names[0], names[1], 10, anchor=p0)
    assert len(sf["train_dist"]) == len(s.X)
