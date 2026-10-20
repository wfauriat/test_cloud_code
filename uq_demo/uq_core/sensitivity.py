"""Sensitivity analysis: one-at-a-time (tornado), Morris screening, Sobol indices.

Every method takes a model function  fn(X) -> y  where the columns of X are
the uncertain parameters `names` in physical units. That function is either
the true simulator or a trained surrogate, which is the whole point: Sobol
indices need N (d + 2) runs, cheap on a surrogate.
"""
from __future__ import annotations

import time
import warnings
from typing import Callable

import numpy as np
from scipy.stats import qmc

from .params import from_unit, marginal, nominal

ModelFn = Callable[[np.ndarray], np.ndarray]


class CountingModel:
    """Wraps a model function to count evaluations and time them."""

    def __init__(self, fn: ModelFn):
        self.fn, self.calls, self.seconds = fn, 0, 0.0

    def __call__(self, X):
        t = time.perf_counter()
        y = self.fn(X)
        self.seconds += time.perf_counter() - t
        self.calls += len(X)
        return y

    def cost(self) -> dict:
        return {"evaluations": self.calls, "seconds": self.seconds}


def oat(fn: ModelFn, spec: dict, names: list[str], q_lo: float = 0.05, q_hi: float = 0.95) -> dict:
    """Tornado: move one input from its q_lo to its q_hi quantile, others at nominal."""
    model = CountingModel(fn)
    base = nominal(spec)
    x0 = np.array([base[n] for n in names])
    X = [x0]
    lows, highs = [], []
    for j, n in enumerate(names):
        d = marginal(spec[n])
        lo, hi = x0.copy(), x0.copy()
        lo[j], hi[j] = d.ppf(q_lo), d.ppf(q_hi)
        lows.append(float(lo[j]))
        highs.append(float(hi[j]))
        X += [lo, hi]
    y = model(np.array(X))
    rows = [{"name": n, "x_lo": lows[j], "x_hi": highs[j], "y_lo": float(y[1 + 2 * j]),
             "y_hi": float(y[2 + 2 * j]), "swing": float(abs(y[2 + 2 * j] - y[1 + 2 * j]))}
            for j, n in enumerate(names)]
    rows.sort(key=lambda r: -r["swing"])
    return {"base": float(y[0]), "rows": rows, "quantiles": [q_lo, q_hi], "cost": model.cost()}


def morris(fn: ModelFn, spec: dict, names: list[str], r: int = 20, levels: int = 4, seed: int = 0) -> dict:
    """Morris elementary effects on r random one-at-a-time trajectories (r (d+1) runs).

    The grid lives in probability space (quantiles 1%..99%), so each input is
    explored according to its distribution. mu* ranks importance; a large
    sigma signals non-linearity or interactions.
    """
    model = CountingModel(fn)
    rng = np.random.default_rng(seed)
    d = len(names)
    delta = levels / (2 * (levels - 1))
    grid = np.arange(levels) / (levels - 1)
    starts = grid[grid <= 1 - delta + 1e-12]
    ee = np.zeros((r, d))
    for t in range(r):
        u = rng.choice(starts, d)
        order = rng.permutation(d)
        pts = [u.copy()]
        for j in order:
            u = u.copy()
            u[j] += delta
            pts.append(u)
        P = 0.01 + 0.98 * np.array(pts)  # avoid the infinite tails of the ppf
        y = model(from_unit(spec, names, P))
        for k, j in enumerate(order):
            ee[t, j] = (y[k + 1] - y[k]) / delta
    rows = [{"name": n, "mu": float(ee[:, j].mean()), "mu_star": float(np.abs(ee[:, j]).mean()),
             "sigma": float(ee[:, j].std(ddof=1))} for j, n in enumerate(names)]
    return {"rows": rows, "r": r, "levels": levels, "cost": model.cost(),
            "effects": {n: ee[:, j].tolist() for j, n in enumerate(names)}}


def sobol(fn: ModelFn, spec: dict, names: list[str], n_base: int = 1024, seed: int = 0,
          n_boot: int = 200) -> dict:
    """First-order (Saltelli 2010) and total (Jansen) Sobol indices, N (d + 2) runs."""
    model = CountingModel(fn)
    d = len(names)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        U = qmc.Sobol(2 * d, scramble=True, rng=np.random.default_rng(seed)).random(n_base)
    A, B = U[:, :d], U[:, d:]
    blocks = [A, B]
    for j in range(d):
        AB = A.copy()
        AB[:, j] = B[:, j]
        blocks.append(AB)
    y = model(from_unit(spec, names, np.vstack(blocks))).reshape(d + 2, n_base)
    y = y - y[:2].mean()  # centring does not change the indices but greatly reduces estimator variance
    fA, fB, fAB = y[0], y[1], y[2:]

    def indices(idx):
        a, b, ab = fA[idx], fB[idx], fAB[:, idx]
        var = np.var(np.r_[a, b])
        if var < 1e-15:
            return np.zeros(d), np.zeros(d), var
        s1 = np.mean(b * (ab - a), axis=1) / var
        st = 0.5 * np.mean((a - ab) ** 2, axis=1) / var
        return s1, st, var

    s1, st, var = indices(np.arange(n_base))
    rng = np.random.default_rng(seed + 1)
    boot = [indices(rng.integers(0, n_base, n_base)) for _ in range(n_boot)]
    b1 = np.array([b[0] for b in boot])
    bt = np.array([b[1] for b in boot])
    rows = [{"name": n, "S1": float(s1[j]), "ST": float(st[j]),
             "S1_ci": np.percentile(b1[:, j], [2.5, 97.5]).tolist(),
             "ST_ci": np.percentile(bt[:, j], [2.5, 97.5]).tolist()} for j, n in enumerate(names)]
    return {"rows": rows, "variance": float(var), "sum_S1": float(s1.sum()), "n_base": n_base,
            "cost": model.cost()}
