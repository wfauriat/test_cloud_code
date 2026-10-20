"""Input parameters, their probability distributions, and model evaluation.

A *spec* is a dict  name -> {"value", "std", "dist", "uncertain"}  where
`value` is the nominal value (= the mean when the parameter is uncertain).
Sampling always goes through the unit hypercube: a design U in [0, 1]^d
(random, LHS, Sobol...) is mapped to physical values by the inverse CDF of
each marginal. This makes Monte Carlo, DoE and Sobol share the same code.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import stats

from .ballistics import simulate


@dataclass(frozen=True)
class ParamInfo:
    name: str
    label: str
    unit: str
    lo: float  # physical bounds (samples are clipped to them)
    hi: float
    value: float  # default nominal value
    std: float  # default standard deviation
    uncertain: bool  # uncertain by default?
    step: float


PARAMS: dict[str, ParamInfo] = {
    p.name: p
    for p in [
        ParamInfo("v0", "Initial speed", "m/s", 1.0, 80.0, 30.0, 1.0, True, 0.5),
        ParamInfo("theta", "Launch angle", "deg", 1.0, 89.0, 40.0, 1.5, True, 0.5),
        ParamInfo("cd", "Drag coefficient Cd", "-", 0.0, 1.5, 0.25, 0.03, True, 0.01),
        ParamInfo("cl", "Lift coefficient Cl", "-", -0.5, 0.5, 0.10, 0.03, False, 0.01),
        ParamInfo("mass", "Mass", "kg", 0.05, 5.0, 0.43, 0.01, False, 0.01),
        ParamInfo("wind", "Wind speed (tail +)", "m/s", -25.0, 25.0, 0.0, 2.0, True, 0.5),
    ]
}
NAMES = list(PARAMS)
QOIS = {
    "range": ("Range", "m"),
    "max_height": ("Max height", "m"),
    "flight_time": ("Flight time", "s"),
    "impact_speed": ("Impact speed", "m/s"),
}
DISTS = ["normal", "uniform", "lognormal"]
_EPS = 1e-9


def default_spec() -> dict:
    return {
        n: {"value": p.value, "std": p.std, "dist": "normal", "uncertain": p.uncertain}
        for n, p in PARAMS.items()
    }


def normalize_spec(spec: dict | None) -> dict:
    """Fill missing entries with defaults and validate values."""
    full = default_spec()
    for name, entry in (spec or {}).items():
        if name not in full:
            raise ValueError(f"unknown parameter {name!r}")
        full[name].update({k: v for k, v in entry.items() if v is not None})
        e = full[name]
        if e["dist"] not in DISTS:
            raise ValueError(f"unknown distribution {e['dist']!r}")
        if e["std"] < 0:
            raise ValueError(f"negative std for {name}")
        if e["dist"] == "lognormal" and e["uncertain"] and e["value"] <= 0:
            raise ValueError(f"lognormal needs a positive mean ({name})")
    return full


def nominal(spec: dict) -> dict[str, float]:
    return {n: float(spec[n]["value"]) for n in NAMES}


def uncertain_names(spec: dict) -> list[str]:
    return [n for n in NAMES if spec[n]["uncertain"] and spec[n]["std"] > 0]


def marginal(entry: dict):
    """Frozen scipy distribution for one parameter."""
    m, s = float(entry["value"]), float(entry["std"])
    if entry["dist"] == "uniform":
        half = np.sqrt(3.0) * s  # uniform on [m - h, m + h] has std h / sqrt(3)
        return stats.uniform(loc=m - half, scale=2 * half)
    if entry["dist"] == "lognormal":
        sig2 = np.log1p((s / m) ** 2)
        return stats.lognorm(s=np.sqrt(sig2), scale=m * np.exp(-sig2 / 2))
    return stats.norm(loc=m, scale=s)


def from_unit(spec: dict, names: list[str], U: np.ndarray) -> np.ndarray:
    """Map U in (0,1)^d to physical values through the inverse CDFs."""
    U = np.clip(np.atleast_2d(U), _EPS, 1 - _EPS)
    X = np.empty_like(U, dtype=float)
    for j, n in enumerate(names):
        X[:, j] = np.clip(marginal(spec[n]).ppf(U[:, j]), PARAMS[n].lo, PARAMS[n].hi)
    return X


def box_from_spec(spec: dict, names: list[str], k: float = 3.0) -> list[tuple[float, float]]:
    """Default training box: mean +/- k std, clipped to physical bounds."""
    box = []
    for n in names:
        d = marginal(spec[n])
        q = stats.norm.cdf([-k, k])
        lo, hi = d.ppf(q) if spec[n]["std"] > 0 else (spec[n]["value"],) * 2
        lo, hi = max(lo, PARAMS[n].lo), min(hi, PARAMS[n].hi)
        if hi - lo < 1e-9:
            w = max(PARAMS[n].step, 1e-3)
            lo, hi = max(lo - w, PARAMS[n].lo), min(hi + w, PARAMS[n].hi)
        box.append((float(lo), float(hi)))
    return box


def full_inputs(spec: dict, names: list[str], X: np.ndarray) -> dict[str, np.ndarray]:
    """Columns of X for `names`, nominal values for every other parameter."""
    X = np.atleast_2d(X)
    base = nominal(spec)
    out = {n: np.full(X.shape[0], base[n]) for n in NAMES}
    for j, n in enumerate(names):
        out[n] = X[:, j].astype(float)
    return out


def run_model(inputs: dict[str, np.ndarray], dt: float = 0.01, record: int = 0):
    return simulate(
        inputs["v0"], inputs["theta"], inputs["cd"], inputs["cl"], inputs["mass"], inputs["wind"],
        dt=dt, record=record,
    )


def evaluate(spec: dict, names: list[str], X: np.ndarray, qoi: str, dt: float = 0.01) -> np.ndarray:
    """True model QoI at the points X (columns = names)."""
    return run_model(full_inputs(spec, names, X), dt).qoi(qoi)
