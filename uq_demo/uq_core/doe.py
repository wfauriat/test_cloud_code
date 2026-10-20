"""Designs of experiments in the unit hypercube, plus space-filling metrics."""
from __future__ import annotations

import warnings

import numpy as np
from scipy.spatial.distance import pdist
from scipy.stats import qmc

METHODS = ["random", "lhs", "lhs_opt", "sobol", "halton", "factorial"]


def unit_design(method: str, n: int, d: int, seed: int | None = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    if method == "random":
        return rng.random((n, d))
    if method == "lhs":
        return qmc.LatinHypercube(d, rng=rng).random(n)
    if method == "lhs_opt":  # LHS improved for centred discrepancy
        return qmc.LatinHypercube(d, optimization="random-cd", rng=rng).random(n)
    if method == "sobol":
        with warnings.catch_warnings():  # balance is only exact for n = 2^m; fine for teaching
            warnings.simplefilter("ignore")
            return qmc.Sobol(d, scramble=True, rng=rng).random(n)
    if method == "halton":
        return qmc.Halton(d, scramble=True, rng=rng).random(n)
    if method == "factorial":
        levels = max(2, int(round(n ** (1.0 / d))))
        axes = [np.linspace(0, 1, levels)] * d
        return np.stack(np.meshgrid(*axes, indexing="ij"), -1).reshape(-1, d)
    raise ValueError(f"unknown DoE method {method!r}")


def scale(U: np.ndarray, box) -> np.ndarray:
    lo = np.array([b[0] for b in box])
    hi = np.array([b[1] for b in box])
    return lo + U * (hi - lo)


def to_unit(X: np.ndarray, box) -> np.ndarray:
    lo = np.array([b[0] for b in box])
    hi = np.array([b[1] for b in box])
    return (X - lo) / (hi - lo)


def metrics(U: np.ndarray) -> dict:
    """Space-filling quality: larger min-distance and smaller discrepancy are better."""
    U = np.clip(U, 0, 1)
    md = float(pdist(U).min()) if len(U) > 1 else float("nan")
    return {
        "min_distance": md,
        "discrepancy": float(qmc.discrepancy(U, method="CD")),
        "n": int(len(U)),
    }
