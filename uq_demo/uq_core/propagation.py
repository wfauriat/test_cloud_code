"""Forward propagation of input uncertainty: Monte Carlo and first-order (FOSM)."""
from __future__ import annotations

import warnings

import numpy as np
from scipy import stats

from . import doe
from .params import QOIS, from_unit, full_inputs, marginal, nominal, run_model, uncertain_names


def summarize(y: np.ndarray) -> dict:
    y = np.asarray(y, dtype=float)
    q = np.percentile(y, [5, 25, 50, 75, 95])
    return {
        "mean": float(y.mean()),
        "std": float(y.std(ddof=1)) if len(y) > 1 else 0.0,
        "min": float(y.min()),
        "max": float(y.max()),
        "p05": float(q[0]), "p25": float(q[1]), "p50": float(q[2]), "p75": float(q[3]), "p95": float(q[4]),
    }


def kde(y: np.ndarray, n_points: int = 200) -> dict:
    y = np.asarray(y, dtype=float)
    lo, hi = y.min(), y.max()
    pad = 0.1 * (hi - lo) if hi > lo else 1.0
    xs = np.linspace(lo - pad, hi + pad, n_points)
    if y.std() < 1e-12:
        return {"x": xs.tolist(), "y": np.zeros_like(xs).tolist()}
    return {"x": xs.tolist(), "y": stats.gaussian_kde(y)(xs).tolist()}


def convergence(y: np.ndarray, n_points: int = 30) -> dict:
    """Running mean with its 95% confidence interval: the MC error shrinks as 1/sqrt(n)."""
    n = len(y)
    ns = np.unique(np.logspace(1, np.log10(n), n_points).astype(int))
    ns = ns[ns <= n]
    csum = np.cumsum(y)
    csum2 = np.cumsum(y**2)
    mean = csum[ns - 1] / ns
    var = np.maximum(csum2[ns - 1] / ns - mean**2, 0) * ns / np.maximum(ns - 1, 1)
    half = 1.96 * np.sqrt(var / ns)
    return {"n": ns.tolist(), "mean": mean.tolist(), "lo": (mean - half).tolist(),
            "hi": (mean + half).tolist(), "std": np.sqrt(var).tolist()}


def fosm(spec: dict, qoi: str, dt: float) -> dict:
    """First-order second-moment: Var[f] ~ sum_i (df/dx_i)^2 sigma_i^2 around the mean."""
    names = uncertain_names(spec)
    base = nominal(spec)
    if not names:
        y0 = float(run_model(full_inputs(spec, [], np.zeros((1, 0))), dt).qoi(qoi)[0])
        return {"mean": y0, "std": 0.0, "gradient": {}, "contrib": {}}
    d = len(names)
    x0 = np.array([base[n] for n in names])
    h = np.array([max(0.05 * spec[n]["std"], 1e-6) for n in names])
    X = np.repeat(x0[None, :], 2 * d + 1, axis=0)
    for j in range(d):
        X[1 + 2 * j, j] += h[j]
        X[2 + 2 * j, j] -= h[j]
    # Use a fine step so that the Euler discretisation does not pollute the gradient.
    y = run_model(full_inputs(spec, names, X), min(dt, 0.002)).qoi(qoi)
    grad = np.array([(y[1 + 2 * j] - y[2 + 2 * j]) / (2 * h[j]) for j in range(d)])
    sig = np.array([marginal(spec[n]).std() for n in names])
    terms = (grad * sig) ** 2
    var = terms.sum()
    return {
        "mean": float(y[0]),
        "std": float(np.sqrt(var)),
        "gradient": {n: float(g) for n, g in zip(names, grad)},
        "contrib": {n: float(t / var) if var > 0 else 0.0 for n, t in zip(names, terms)},
    }


def monte_carlo(spec: dict, n: int = 2000, sampling: str = "random", seed: int | None = 0,
                dt: float = 0.01, n_traj: int = 60, qoi: str = "range",
                target: float | None = None, tol: float | None = None,
                n_input_samples: int = 2000) -> dict:
    names = uncertain_names(spec)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")  # Sobol balance warning when n is not a power of 2
        U = doe.unit_design(sampling, n, len(names), seed) if names else np.zeros((n, 0))
    X = from_unit(spec, names, U) if names else U
    res = run_model(full_inputs(spec, names, X), dt, record=n_traj)
    out: dict = {"n": n, "uncertain": names, "qoi": {}}
    for q in QOIS:
        y = res.qoi(q)
        out["qoi"][q] = {"values": np.round(y, 4).tolist(), "stats": summarize(y), "kde": kde(y)}
    y = res.qoi(qoi)
    out["convergence"] = convergence(y)
    out["fosm"] = fosm(spec, qoi, dt)
    out["not_landed"] = int((~res.landed).sum())
    out["trajectories"] = [{"x": np.round(t[:, 0], 3).tolist(), "y": np.round(t[:, 1], 3).tolist()}
                           for t in (res.trajectories or [])]
    m = min(n_input_samples, n)
    out["inputs"] = {nm: np.round(X[:m, j], 5).tolist() for j, nm in enumerate(names)}
    if target is not None and tol is not None:
        miss = np.abs(y - target) > tol
        p = float(miss.mean())
        half = 1.96 * np.sqrt(max(p * (1 - p), 1e-12) / n)
        out["risk"] = {"target": target, "tol": tol, "p_miss": p, "p_miss_ci": [max(p - half, 0), min(p + half, 1)],
                       "p_short": float((y < target - tol).mean()), "p_long": float((y > target + tol).mean())}
    return out
