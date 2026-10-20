"""FastAPI backend for the ballistic UQ demo.

Run:  uvicorn api.main:app --reload       (from the uq_demo/ folder)
All numerics live in `uq_core`; this module only validates requests and
shapes the JSON. If the front-end has been built (frontend/dist), it is
served at / as well.
"""
from __future__ import annotations

import functools
import json
import math
from pathlib import Path
from typing import Any, Literal

import numpy as np
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from uq_core import doe, params, propagation, robust, sensitivity, surrogate
from uq_core.ballistics import simulate, vacuum_trajectory


def _clean(obj: Any) -> Any:
    """numpy -> python, NaN/inf -> None, so the payload is valid JSON."""
    if isinstance(obj, dict):
        return {str(k): _clean(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_clean(v) for v in obj]
    if isinstance(obj, np.ndarray):
        return _clean(obj.tolist())
    if isinstance(obj, (np.floating, float)):
        f = float(obj)
        return f if math.isfinite(f) else None
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.bool_):
        return bool(obj)
    return obj


class SafeJSON(JSONResponse):
    def render(self, content: Any) -> bytes:
        return json.dumps(_clean(content), allow_nan=False, separators=(",", ":")).encode()


def safe_json(fn):
    """Return the endpoint result as SafeJSON, bypassing FastAPI's encoder (numpy-unaware)."""
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        return SafeJSON(fn(*args, **kwargs))
    return wrapper


app = FastAPI(title="Ballistic UQ demo")


@app.exception_handler(ValueError)
@app.exception_handler(KeyError)
async def _bad_request(_: Request, exc: Exception):
    return SafeJSON({"detail": str(exc).strip("'\"")}, status_code=400)


# ---------------------------------------------------------------- schemas

class ParamEntry(BaseModel):
    value: float | None = None
    std: float | None = None
    dist: Literal["normal", "uniform", "lognormal"] | None = None
    uncertain: bool | None = None


Qoi = Literal["range", "max_height", "flight_time", "impact_speed"]


class Base(BaseModel):
    spec: dict[str, ParamEntry] = Field(default_factory=dict)
    dt: float = Field(0.01, gt=1e-4, le=0.2)

    def full_spec(self) -> dict:
        return params.normalize_spec({k: v.model_dump() for k, v in self.spec.items()})


class SimulateReq(Base):
    scheme: Literal["euler", "rk4"] = "euler"


class PropagateReq(Base):
    n: int = Field(2000, ge=10, le=50000)
    sampling: Literal["random", "lhs", "sobol"] = "random"
    seed: int | None = 0
    n_traj: int = Field(60, ge=0, le=500)
    qoi: Qoi = "range"
    target: float | None = None
    tol: float | None = None


class DoeReq(Base):
    names: list[str] | None = None  # default: uncertain parameters
    box: list[tuple[float, float]] | None = None  # default: mean +/- k std
    box_override: dict[str, tuple[float, float]] = Field(default_factory=dict)  # per-parameter edits
    k: float = Field(3.0, gt=0, le=6)
    method: str = "lhs"
    n: int = Field(50, ge=2, le=5000)
    seed: int = 0


class TrainReq(Base):
    names: list[str]
    box: list[tuple[float, float]]
    X: list[list[float]]
    kind: str = "gp"
    qoi: Qoi = "range"
    n_test: int = Field(500, ge=20, le=5000)
    seed: int = 0


class LearningReq(Base):
    names: list[str]
    box: list[tuple[float, float]]
    kinds: list[str] = ["poly2", "gp", "rf"]
    sizes: list[int] = [10, 20, 40, 80, 160]
    method: str = "lhs"
    qoi: Qoi = "range"
    seed: int = 0


class SliceReq(BaseModel):
    model_id: str
    param: str


class SurfaceReq(BaseModel):
    model_id: str
    px: str
    py: str
    n_grid: int = Field(40, ge=5, le=80)


class SensitivityReq(Base):
    method: Literal["oat", "morris", "sobol"] = "sobol"
    qoi: Qoi = "range"
    model_id: str | None = None  # None -> true simulator
    r: int = Field(20, ge=2, le=500)
    levels: int = Field(4, ge=2, le=10)
    n_base: int = Field(1024, ge=16, le=16384)
    seed: int = 0


class RobustReq(Base):
    design: list[str]
    bounds: list[tuple[float, float]]
    qoi: Qoi = "range"
    target: float = 55.0
    tol: float = Field(3.0, gt=0)
    lam: float = Field(1.0, ge=0)
    n_mc: int = Field(256, ge=16, le=4096)
    grid: int = Field(31, ge=5, le=61)
    use_surrogate: bool = True
    surrogate_kind: str = "gp"
    n_train: int = Field(200, ge=20, le=2000)
    seed: int = 0


class ToleranceReq(Base):
    design: list[str]
    qoi: Qoi = "range"
    target: float = 55.0
    tol: float = Field(3.0, gt=0)
    std_max: list[float]
    grid: int = Field(15, ge=3, le=41)
    n_mc: int = Field(400, ge=16, le=4096)
    seed: int = 0


def _check_names(names: list[str]):
    bad = [n for n in names if n not in params.PARAMS]
    if bad or not names:
        raise ValueError(f"invalid parameter list {names}")


# ---------------------------------------------------------------- endpoints

@app.get("/api/meta")
@safe_json
def meta():
    return {
        "params": [p.__dict__ for p in params.PARAMS.values()],
        "qois": {k: {"label": v[0], "unit": v[1]} for k, v in params.QOIS.items()},
        "dists": params.DISTS,
        "doe_methods": doe.METHODS,
        "surrogates": surrogate.KINDS,
        "objectives": robust.OBJECTIVES,
        "default_spec": params.default_spec(),
    }


@app.post("/api/simulate")
@safe_json
def api_simulate(req: SimulateReq):
    spec = req.full_spec()
    p = params.nominal(spec)
    res = simulate(p["v0"], p["theta"], p["cd"], p["cl"], p["mass"], p["wind"], dt=req.dt,
                   scheme=req.scheme, record=1, max_points=400)
    traj = res.trajectories[0]
    # QoIs as a function of the launch angle, everything else fixed
    thetas = np.linspace(2, 88, 87)
    sweep = simulate(p["v0"], thetas, p["cd"], p["cl"], p["mass"], p["wind"], dt=req.dt)
    vac = vacuum_trajectory(p["v0"], p["theta"])
    return {
        "trajectory": {"x": traj[:, 0], "y": traj[:, 1]},
        "qoi": {q: float(res.qoi(q)[0]) for q in params.QOIS},
        "landed": bool(res.landed[0]),
        "vacuum": vac,
        "sweep": {"theta": thetas, "range": sweep.range, "max_height": sweep.max_height,
                  "vacuum_range": p["v0"] ** 2 * np.sin(np.radians(2 * thetas)) / 9.81},
    }


@app.post("/api/simulate/convergence")
@safe_json
def api_convergence(req: Base):
    """Error of explicit Euler vs a fine RK4 reference, as a function of dt."""
    spec = req.full_spec()
    p = params.nominal(spec)
    args = (p["v0"], p["theta"], p["cd"], p["cl"], p["mass"], p["wind"])
    ref = simulate(*args, dt=1e-3, scheme="rk4")
    dts = np.logspace(np.log10(0.0005), np.log10(0.2), 14)
    eul = simulate(*(np.full(len(dts), a) for a in args), dt=dts)
    return {"dt": dts, "range_error": np.abs(eul.range - ref.range[0]),
            "height_error": np.abs(eul.max_height - ref.max_height[0]),
            "range": eul.range, "reference_range": float(ref.range[0])}


@app.post("/api/propagate")
@safe_json
def api_propagate(req: PropagateReq):
    return propagation.monte_carlo(req.full_spec(), req.n, req.sampling, req.seed, req.dt, req.n_traj,
                                   req.qoi, req.target, req.tol)


@app.post("/api/doe")
@safe_json
def api_doe(req: DoeReq):
    spec = req.full_spec()
    names = req.names or params.uncertain_names(spec)
    _check_names(names)
    box = req.box or params.box_from_spec(spec, names, req.k)
    box = [tuple(req.box_override.get(n, b)) for n, b in zip(names, box)]
    if len(box) != len(names) or any(hi <= lo for lo, hi in box):
        raise ValueError("box must give one (lo < hi) pair per parameter")
    U = doe.unit_design(req.method, req.n, len(names), req.seed)
    compare = {m: doe.metrics(doe.unit_design(m, req.n, len(names), req.seed))
               for m in doe.METHODS if m != "factorial"}
    return {"names": names, "box": box, "U": U, "X": doe.scale(U, box), "metrics": doe.metrics(U),
            "compare": compare}


@app.post("/api/surrogate/train")
@safe_json
def api_train(req: TrainReq):
    _check_names(req.names)
    X = np.asarray(req.X, float)
    if X.ndim != 2 or X.shape[1] != len(req.names) or len(X) < 3:
        raise ValueError("X must be an (n >= 3, len(names)) matrix")
    return surrogate.train(req.full_spec(), req.names, req.box, X, req.kind, req.qoi, req.dt, req.n_test, req.seed)


@app.post("/api/surrogate/learning_curve")
@safe_json
def api_learning(req: LearningReq):
    _check_names(req.names)
    sizes = [s for s in req.sizes if 3 <= s <= 1000]
    return surrogate.learning_curve(req.full_spec(), req.names, req.box, req.kinds, sizes, req.method,
                                    req.qoi, req.dt, seed=req.seed)


@app.post("/api/surrogate/slice")
@safe_json
def api_slice(req: SliceReq):
    return surrogate.slice_1d(surrogate.get(req.model_id), req.param)


@app.post("/api/surrogate/surface")
@safe_json
def api_surface(req: SurfaceReq):
    return surrogate.surface_2d(surrogate.get(req.model_id), req.px, req.py, req.n_grid)


@app.post("/api/sensitivity")
@safe_json
def api_sensitivity(req: SensitivityReq):
    spec = req.full_spec()
    names = params.uncertain_names(spec)
    if not names:
        raise ValueError("mark at least one parameter as uncertain")
    if req.model_id:
        s = surrogate.get(req.model_id)
        missing = [n for n in names if n not in s.names]
        if missing:
            raise ValueError(f"the surrogate was not trained on {missing}; retrain it with these inputs")
        if s.qoi != req.qoi:
            raise ValueError(f"the surrogate predicts {s.qoi}, not {req.qoi}")
        base = params.nominal(spec)
        cols = [names.index(n) if n in names else None for n in s.names]

        def fn(X):
            Z = np.empty((len(X), len(s.names)))
            for c, j in enumerate(cols):
                Z[:, c] = X[:, j] if j is not None else base[s.names[c]]
            return s.predict(Z)
    else:
        def fn(X):
            return params.evaluate(spec, names, X, req.qoi, req.dt)

    if req.method == "oat":
        out = sensitivity.oat(fn, spec, names)
    elif req.method == "morris":
        out = sensitivity.morris(fn, spec, names, req.r, req.levels, req.seed)
    else:
        out = sensitivity.sobol(fn, spec, names, req.n_base, req.seed)
    out["model"] = "surrogate" if req.model_id else "simulator"
    return out


@app.post("/api/robust")
@safe_json
def api_robust(req: RobustReq):
    _check_names(req.design)
    if len(req.bounds) != len(req.design) or any(hi <= lo for lo, hi in req.bounds):
        raise ValueError("bounds must give one (lo < hi) pair per design variable")
    return robust.optimize(req.full_spec(), req.design, req.bounds, req.qoi, req.target, req.tol, req.lam,
                           req.n_mc, req.grid, req.use_surrogate, req.surrogate_kind, req.n_train, req.dt,
                           req.seed)


@app.post("/api/robust/tolerance")
@safe_json
def api_tolerance(req: ToleranceReq):
    _check_names(req.design)
    if len(req.std_max) != len(req.design):
        raise ValueError("std_max must give one value per design variable")
    return robust.tolerance_study(req.full_spec(), req.design, req.qoi, req.target, req.tol, req.std_max,
                                  req.grid, req.n_mc, req.dt, req.seed)


_DIST = Path(__file__).resolve().parent.parent / "frontend" / "dist"
if _DIST.is_dir():
    app.mount("/", StaticFiles(directory=_DIST, html=True), name="frontend")
