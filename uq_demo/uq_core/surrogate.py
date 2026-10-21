"""Surrogate models (scikit-learn) trained on a design of experiments.

Fitted models are kept in a small in-memory store and referenced by id, so
that the front-end can train once, then query slices / surfaces / sensitivity.
Inputs are always rescaled to the unit box before fitting.
"""
from __future__ import annotations

import time
import uuid
import warnings
from collections import OrderedDict
from dataclasses import dataclass, field

import numpy as np
from sklearn.compose import TransformedTargetRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.exceptions import ConvergenceWarning
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel, WhiteKernel
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

from . import doe
from .params import evaluate, nominal

KINDS = {
    "poly1": "Linear regression",
    "poly2": "Quadratic polynomial",
    "poly3": "Cubic polynomial",
    "gp": "Gaussian process (kriging)",
    "rf": "Random forest",
    "mlp": "Neural network (MLP)",
}
_MAX_STORE = 30


def make_estimator(kind: str, d: int, seed: int = 0, nugget: bool = False):
    if kind.startswith("poly"):
        deg = int(kind[4:])
        return make_pipeline(PolynomialFeatures(deg), Ridge(alpha=1e-8))
    if kind == "gp":
        # The simulator is deterministic, so the GP interpolates (kriging), with a tiny
        # jitter for numerical stability. A fitted nugget (WhiteKernel) is only the
        # fallback when the covariance matrix is too ill-conditioned.
        kernel = ConstantKernel(1.0, (1e-3, 1e3)) * RBF(np.full(d, 0.5), (1e-2, 1e2))
        if nugget:
            kernel = kernel + WhiteKernel(1e-6, (1e-10, 1e-1))
        return GaussianProcessRegressor(kernel, alpha=1e-8, normalize_y=True, n_restarts_optimizer=2, random_state=seed)
    if kind == "rf":
        return RandomForestRegressor(n_estimators=200, random_state=seed)
    if kind == "mlp":
        mlp = MLPRegressor(hidden_layer_sizes=(64, 64), activation="tanh", max_iter=4000, learning_rate_init=3e-3, random_state=seed)
        return TransformedTargetRegressor(regressor=mlp, transformer=StandardScaler())
    raise ValueError(f"unknown surrogate kind {kind!r}")


@dataclass
class Surrogate:
    kind: str
    names: list[str]
    box: list[tuple[float, float]]
    qoi: str
    dt: float
    spec: dict
    X: np.ndarray
    y: np.ndarray
    estimator: object = None
    id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    train_time: float = 0.0

    def fit(self, seed: int = 0):
        t = time.perf_counter()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ConvergenceWarning)
            U = doe.to_unit(self.X, self.box)
            self.estimator = make_estimator(self.kind, len(self.names), seed)
            try:
                self.estimator.fit(U, self.y)
            except (np.linalg.LinAlgError, ValueError):
                if self.kind != "gp":
                    raise
                self.estimator = make_estimator(self.kind, len(self.names), seed, nugget=True)
                self.estimator.fit(U, self.y)
        self.train_time = time.perf_counter() - t
        return self

    def predict(self, X: np.ndarray, return_std: bool = False, batch: int = 20000):
        U = doe.to_unit(np.atleast_2d(X), self.box)
        means, stds = [], []
        for i in range(0, len(U), batch):
            u = U[i:i + batch]
            if self.kind == "gp" and return_std:
                m, s = self.estimator.predict(u, return_std=True)
                # sklearn's std includes the fitted WhiteKernel noise (a floor that never
                # vanishes, even at the training points); report the latent-function std.
                s = np.sqrt(np.maximum(s**2 - self._gp_noise_var(), 0.0))
            elif self.kind == "rf" and return_std:
                per_tree = np.stack([t.predict(u) for t in self.estimator.estimators_])
                m, s = per_tree.mean(0), per_tree.std(0)
            else:
                m, s = self.estimator.predict(u), None
            means.append(m)
            stds.append(s)
        mean = np.concatenate(means) if means else np.zeros(0)
        if not return_std:
            return mean
        std = None if stds[0] is None else np.concatenate(stds)
        return mean, std

    def _gp_noise_var(self) -> float:
        """Variance of the WhiteKernel term, in the units of y (normalize_y=True rescales it)."""
        white = getattr(self.estimator.kernel_, "k2", None)
        level = float(white.noise_level) if isinstance(white, WhiteKernel) else 0.0
        y_std = float(np.atleast_1d(getattr(self.estimator, "_y_train_std", 1.0))[0])
        return level * y_std**2

    @property
    def has_std(self) -> bool:
        return self.kind in ("gp", "rf")

    def anchor(self, values: dict | None = None) -> np.ndarray:
        """Point through which slices are taken: `values` where given, else the
        nominal values, clipped into the box."""
        base = {**nominal(self.spec), **(values or {})}
        return np.array([np.clip(base[n], lo, hi) for n, (lo, hi) in zip(self.names, self.box)])

    def distance_to_slice(self, a: np.ndarray, free: list[int]) -> np.ndarray:
        """Distance of each training point to the slice through `a` (free dims ignored),
        in unit-box coordinates: a projected point is only meaningful when it is small."""
        fixed = [k for k in range(len(self.names)) if k not in free]
        if not fixed:
            return np.zeros(len(self.X))
        U = doe.to_unit(self.X, self.box)[:, fixed]
        ua = doe.to_unit(a[None, :], self.box)[0, fixed]
        return np.sqrt(((U - ua) ** 2).sum(axis=1))

    def describe(self) -> dict:
        info = {"id": self.id, "kind": self.kind, "label": KINDS[self.kind], "names": self.names,
                "box": self.box, "qoi": self.qoi, "n_train": int(len(self.y)),
                "train_time": self.train_time}
        if self.kind == "gp":
            info["kernel"] = str(self.estimator.kernel_)
        return info


STORE: "OrderedDict[str, Surrogate]" = OrderedDict()


def store(s: Surrogate) -> Surrogate:
    STORE[s.id] = s
    while len(STORE) > _MAX_STORE:
        STORE.popitem(last=False)
    return s


def get(model_id: str) -> Surrogate:
    if model_id not in STORE:
        raise KeyError(f"unknown or expired surrogate {model_id!r}; retrain it")
    return STORE[model_id]


def scores(y_true, y_pred) -> dict:
    return {"r2": float(r2_score(y_true, y_pred)),
            "rmse": float(np.sqrt(mean_squared_error(y_true, y_pred))),
            "mae": float(mean_absolute_error(y_true, y_pred))}


def test_set(spec, names, box, qoi, dt, n_test, seed):
    rng = np.random.default_rng(seed + 12345)
    Xt = doe.scale(rng.random((n_test, len(names))), box)
    return Xt, evaluate(spec, names, Xt, qoi, dt)


def train(spec: dict, names: list[str], box, X: np.ndarray, kind: str, qoi: str,
          dt: float = 0.01, n_test: int = 500, seed: int = 0) -> dict:
    t0 = time.perf_counter()
    y = evaluate(spec, names, X, qoi, dt)
    t_sim = time.perf_counter() - t0
    s = Surrogate(kind, names, [tuple(b) for b in box], qoi, dt, spec, np.asarray(X, float), y).fit(seed)
    store(s)
    Xt, yt = test_set(spec, names, box, qoi, dt, n_test, seed)
    t0 = time.perf_counter()
    yp_test = s.predict(Xt)
    t_pred = time.perf_counter() - t0
    yp_train = s.predict(s.X)
    return {
        "model": s.describe(),
        "train": {**scores(y, yp_train), "y": y.tolist(), "pred": yp_train.tolist()},
        "test": {**scores(yt, yp_test), "y": yt.tolist(), "pred": yp_test.tolist()},
        "timing": {"simulator_per_1000": 1000 * t_sim / len(y), "surrogate_per_1000": 1000 * t_pred / n_test,
                   "train": s.train_time},
    }


def learning_curve(spec, names, box, kinds, sizes, method, qoi, dt=0.01, n_test=400, seed=0) -> dict:
    Xt, yt = test_set(spec, names, box, qoi, dt, n_test, seed)
    out = {"sizes": list(sizes), "curves": {}}
    for kind in kinds:
        r2, rmse = [], []
        for n in sizes:
            X = doe.scale(doe.unit_design(method, n, len(names), seed), box)
            s = Surrogate(kind, names, box, qoi, dt, spec, X, evaluate(spec, names, X, qoi, dt)).fit(seed)
            sc = scores(yt, s.predict(Xt))
            r2.append(sc["r2"])
            rmse.append(sc["rmse"])
        out["curves"][kind] = {"label": KINDS[kind], "r2": r2, "rmse": rmse}
    return out


def slice_1d(s: Surrogate, param: str, n_points: int = 120, anchor: dict | None = None) -> dict:
    j = s.names.index(param)
    lo, hi = s.box[j]
    xs = np.linspace(lo, hi, n_points)
    a = s.anchor(anchor)
    X = np.repeat(a[None, :], n_points, axis=0)
    X[:, j] = xs
    mean, std = s.predict(X, return_std=True)
    true = evaluate(s.spec, s.names, X, s.qoi, s.dt)
    return {"x": xs.tolist(), "pred": mean.tolist(), "std": None if std is None else std.tolist(),
            "true": true.tolist(), "train_x": s.X[:, j].tolist(), "train_y": s.y.tolist(),
            "train_dist": s.distance_to_slice(a, [j]).tolist(), "anchor": dict(zip(s.names, a.tolist()))}


def surface_2d(s: Surrogate, px: str, py: str, n_grid: int = 40, anchor: dict | None = None) -> dict:
    i, j = s.names.index(px), s.names.index(py)
    xs = np.linspace(*s.box[i], n_grid)
    ys = np.linspace(*s.box[j], n_grid)
    gx, gy = np.meshgrid(xs, ys)
    a = s.anchor(anchor)
    X = np.repeat(a[None, :], gx.size, axis=0)
    X[:, i] = gx.ravel()
    X[:, j] = gy.ravel()
    mean, std = s.predict(X, return_std=True)
    true = evaluate(s.spec, s.names, X, s.qoi, s.dt)
    shape = gx.shape
    return {"x": xs.tolist(), "y": ys.tolist(), "pred": mean.reshape(shape).tolist(),
            "true": true.reshape(shape).tolist(),
            "std": None if std is None else std.reshape(shape).tolist(),
            "error": (mean - true).reshape(shape).tolist(),
            "train_x": s.X[:, i].tolist(), "train_y": s.X[:, j].tolist(),
            "train_dist": s.distance_to_slice(a, [i, j]).tolist(), "anchor": dict(zip(s.names, a.tolist()))}
