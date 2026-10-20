"""Robust design: choose the means of 1-2 controllable inputs so that the QoI
hits a target despite uncertainty (input tolerances + nuisance parameters
such as the wind).

Every uncertain parameter contributes a random deviation e_j drawn from its
marginal (centred on its mean). For a candidate design mu, the samples are
x_j = mu_j + e_j for design variables and x_j = value_j + e_j otherwise.
The same deviations are reused for every design (common random numbers), so
the objective landscape is smooth and comparisons between designs are fair.

Three objectives are compared:
  deterministic : (f(mu, nominal noise) - T)^2         -- ignores uncertainty
  mean_var      : (E[f] - T)^2 + lambda * Var[f]        -- trade bias vs spread
  chance        : 1 - P(|f - T| <= tol)                  -- maximise hit probability
"""
from __future__ import annotations

import time
import warnings

import numpy as np
from scipy.optimize import minimize
from scipy.special import expit
from scipy.stats import norm, qmc

from . import doe
from .params import NAMES, PARAMS, box_from_spec, evaluate, from_unit, marginal, nominal, uncertain_names
from .propagation import kde, summarize
from .surrogate import Surrogate, scores, store, test_set

OBJECTIVES = {"deterministic": "Deterministic (nominal hit)", "mean_var": "Mean-variance",
              "chance": "Max hit probability"}


def _deviations(spec, names, n, seed):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        U = qmc.Sobol(max(len(names), 1), scramble=True, rng=np.random.default_rng(seed)).random(n)
    U = np.clip(U[:, :len(names)], 1e-9, 1 - 1e-9)
    E = np.empty((n, len(names)))
    for j, nm in enumerate(names):
        E[:, j] = marginal(spec[nm]).ppf(U[:, j]) - spec[nm]["value"]
    return E


class Problem:
    def __init__(self, spec, design, qoi, target, tol, lam, n_mc, dt, seed, fn, inputs):
        self.spec, self.design, self.qoi = spec, design, qoi
        self.target, self.tol, self.lam = target, tol, lam
        self.noise = uncertain_names(spec)
        self.E = _deviations(spec, self.noise, n_mc, seed)
        self.fn, self.inputs = fn, inputs  # fn takes X with columns = inputs
        self.base = nominal(spec)
        self.calls = 0

    def _points(self, M: np.ndarray, E: np.ndarray) -> np.ndarray:
        """All (design, sample) combinations -> rows of X (columns = self.inputs)."""
        g, n = len(M), len(E)
        X = np.empty((g, n, len(self.inputs)))
        for c, nm in enumerate(self.inputs):
            centre = M[:, self.design.index(nm)][:, None] if nm in self.design else np.full((g, 1), self.base[nm])
            dev = E[None, :, self.noise.index(nm)] if nm in self.noise else 0.0
            X[:, :, c] = np.clip(centre + dev, PARAMS[nm].lo, PARAMS[nm].hi)
        return X.reshape(g * n, -1)

    def stats(self, M: np.ndarray) -> dict:
        M = np.atleast_2d(M)
        n = len(self.E)
        y = self.fn(self._points(M, self.E)).reshape(len(M), n)
        y_nom = self.fn(self._points(M, np.zeros((1, len(self.noise))))).ravel()
        self.calls += y.size + y_nom.size
        dev = np.abs(y - self.target)
        return {"mean": y.mean(1), "std": y.std(1), "nominal": y_nom,
                "p_hit": (dev <= self.tol).mean(1),
                # smooth version of the indicator, used by the optimiser
                "p_smooth": expit((self.tol - dev) / (0.05 * self.tol + 1e-9)).mean(1)}

    def objective(self, kind: str, st: dict) -> np.ndarray:
        if kind == "deterministic":
            return (st["nominal"] - self.target) ** 2
        if kind == "mean_var":
            return (st["mean"] - self.target) ** 2 + self.lam * st["std"] ** 2
        return 1.0 - st["p_smooth"]


def _surrogate_fn(spec, design, bounds, qoi, dt, n_train, kind, seed):
    """Train a surrogate covering the design box widened by the input spread."""
    inputs = [n for n in NAMES if n in design or n in uncertain_names(spec)]
    box = []
    for nm in inputs:
        lo, hi = box_from_spec(spec, [nm], k=4.0)[0]
        if nm in design:
            spread = 4.0 * spec[nm]["std"] if spec[nm]["uncertain"] else 0.0
            b = bounds[design.index(nm)]
            lo, hi = max(b[0] - spread, PARAMS[nm].lo), min(b[1] + spread, PARAMS[nm].hi)
        box.append((float(lo), float(hi)))
    X = doe.scale(doe.unit_design("lhs_opt", n_train, len(inputs), seed), box)
    s = Surrogate(kind, inputs, box, qoi, dt, spec, X, evaluate(spec, inputs, X, qoi, dt)).fit(seed)
    store(s)
    Xt, yt = test_set(spec, inputs, box, qoi, dt, 400, seed)
    return s, inputs, scores(yt, s.predict(Xt))


def optimize(spec: dict, design: list[str], bounds: list[tuple[float, float]], qoi: str = "range",
             target: float = 60.0, tol: float = 2.0, lam: float = 1.0, n_mc: int = 256,
             grid: int = 31, use_surrogate: bool = True, surrogate_kind: str = "gp",
             n_train: int = 200, dt: float = 0.01, seed: int = 0, n_validate: int = 4000) -> dict:
    if not 1 <= len(design) <= 2:
        raise ValueError("choose one or two design variables")
    t0 = time.perf_counter()
    out: dict = {"design": design, "bounds": bounds, "noise": uncertain_names(spec)}
    if use_surrogate:
        s, inputs, sc = _surrogate_fn(spec, design, bounds, qoi, dt, n_train, surrogate_kind, seed)
        fn = s.predict
        out["surrogate"] = {**s.describe(), "test": sc}
    else:
        inputs = [n for n in NAMES if n in design or n in uncertain_names(spec)]
        fn = lambda X: evaluate(spec, inputs, X, qoi, dt)  # noqa: E731
    pb = Problem(spec, design, qoi, target, tol, lam, n_mc, dt, seed, fn, inputs)

    # 1) Landscape on a grid of candidate designs.
    axes = [np.linspace(lo, hi, grid if len(design) == 2 else 4 * grid) for lo, hi in bounds]
    mesh = np.meshgrid(*axes, indexing="xy")
    M = np.column_stack([m.ravel() for m in mesh])
    st = pb.stats(M)
    shape = mesh[0].shape
    out["grid"] = {"axes": [a.tolist() for a in axes],
                   **{k: st[k].reshape(shape).tolist() for k in ("mean", "std", "nominal", "p_hit")}}
    out["grid"]["objective"] = {k: pb.objective(k, st).reshape(shape).tolist() for k in OBJECTIVES}

    # 2) Optimum of each objective: best grid point, then Nelder-Mead refinement.
    lo = np.array([b[0] for b in bounds])
    hi = np.array([b[1] for b in bounds])
    start_nom = np.clip([nominal(spec)[d] for d in design], lo, hi)
    optima = {}
    for kind in OBJECTIVES:
        J = pb.objective(kind, st)
        # The deterministic optimum is a whole curve of designs; start from the
        # current nominal design, as a naive engineer would.
        x_start = start_nom if kind == "deterministic" else M[np.argmin(J)]

        def f(x, kind=kind):
            x = np.clip(x, lo, hi)
            return float(pb.objective(kind, pb.stats(x[None, :]))[0])

        res = minimize(f, x_start, method="Nelder-Mead",
                       options={"xatol": 1e-3 * float(np.max(hi - lo)), "fatol": 1e-10, "maxiter": 300})
        x = np.clip(res.x, lo, hi)
        s_opt = pb.stats(x[None, :])
        optima[kind] = {"x": dict(zip(design, x.tolist())), "objective": float(pb.objective(kind, s_opt)[0]),
                        "mean": float(s_opt["mean"][0]), "std": float(s_opt["std"][0]),
                        "nominal": float(s_opt["nominal"][0]), "p_hit": float(s_opt["p_hit"][0])}
    out["optima"] = optima
    out["model_calls"] = pb.calls
    out["seconds_optim"] = time.perf_counter() - t0

    # 3) Check each optimum on the true model with fresh samples.
    names = uncertain_names(spec)
    rng = np.random.default_rng(seed + 99)
    for kind, opt in optima.items():
        sp = {k: dict(v) for k, v in spec.items()}
        for d_name, val in opt["x"].items():
            sp[d_name]["value"] = val
        if names:
            X = from_unit(sp, names, rng.random((n_validate, len(names))))
            y = evaluate(sp, names, X, qoi, dt)
        else:
            y = evaluate(sp, [], np.zeros((1, 0)), qoi, dt)
        opt["validation"] = {**summarize(y), "p_hit": float((np.abs(y - target) <= tol).mean()),
                             "kde": kde(y), "values": np.round(y[:2000], 3).tolist()}
    return out


def tolerance_study(spec: dict, design: list[str], qoi: str, target: float, tol: float,
                    std_max: list[float], grid: int = 15, n_mc: int = 400, dt: float = 0.01,
                    seed: int = 0) -> dict:
    """P(hit) as a function of the std (tolerance) of the design variables,
    the other uncertainties being fixed, at the current means. Uses the true
    model and normal tolerances."""
    noise = [n for n in uncertain_names(spec) if n not in design]
    inputs = list(dict.fromkeys(design + noise))
    E = _deviations(spec, noise, n_mc, seed) if noise else np.zeros((n_mc, 0))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        Z = norm.ppf(np.clip(qmc.Sobol(len(design), scramble=True, rng=np.random.default_rng(seed + 7)).random(n_mc),
                             1e-9, 1 - 1e-9))
    axes = [np.linspace(0, smax, grid) for smax in std_max]
    mesh = np.meshgrid(*axes, indexing="xy")
    S = np.column_stack([m.ravel() for m in mesh])
    base = nominal(spec)
    g = len(S)
    X = np.empty((g, n_mc, len(inputs)))
    for c, nm in enumerate(inputs):
        if nm in design:
            j = design.index(nm)
            X[:, :, c] = base[nm] + S[:, j][:, None] * Z[None, :, j]
        else:
            X[:, :, c] = base[nm] + E[None, :, noise.index(nm)]
        X[:, :, c] = np.clip(X[:, :, c], PARAMS[nm].lo, PARAMS[nm].hi)
    y = evaluate(spec, inputs, X.reshape(g * n_mc, -1), qoi, dt).reshape(g, n_mc)
    shape = mesh[0].shape
    p_hit = (np.abs(y - target) <= tol).mean(1)
    return {"design": design, "axes": [a.tolist() for a in axes], "p_hit": p_hit.reshape(shape).tolist(),
            "mean": y.mean(1).reshape(shape).tolist(), "std": y.std(1).reshape(shape).tolist(),
            "current_std": [float(spec[d]["std"]) if spec[d]["uncertain"] else 0.0 for d in design]}
