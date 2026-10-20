"""Bayesian calibration: infer uncertain model parameters from noisy shots.

A synthetic experiment fires K shots at known launch angles with a hidden
"true" value of the parameters to calibrate (e.g. the drag coefficient), and
records the QoI(s) with Gaussian measurement noise. Optionally, unmodelled
wind gusts perturb each shot: the calibration model does not know about
them, which illustrates model error.

Bayes' rule:  p(params | data) ∝ p(data | params) p(params)

  prior       : the law of each parameter in the left panel
  likelihood  : prod_k N(obs_k | model(params, theta_k), sigma^2)

The posterior is computed either exactly on a grid (1-3 parameters, one big
vectorised simulator call), or sampled by an ensemble MCMC (affine-invariant
stretch move, Goodman & Weare 2010) on the simulator or on a Gaussian-process
emulator of it.
"""
from __future__ import annotations

import time

import numpy as np

from . import doe
from .ballistics import simulate
from .params import PARAMS, QOIS, box_from_spec, from_unit, marginal, nominal
from .propagation import kde, summarize
from .surrogate import Surrogate, scores, test_set

CALIBRATABLE = ["v0", "cd", "cl", "mass", "wind"]  # theta is the experimental condition


def check_names(spec: dict, names: list[str]):
    if not 1 <= len(names) <= 3:
        raise ValueError("calibrate one to three parameters")
    for n in names:
        if n not in CALIBRATABLE:
            raise ValueError(f"{n!r} cannot be calibrated (choose among {CALIBRATABLE})")
        if spec[n]["std"] <= 0:
            raise ValueError(f"the prior of {n} needs a positive std")


def simulate_shots(spec: dict, names: list[str], P: np.ndarray, thetas: np.ndarray, qois: list[str],
                   dt: float, gust: np.ndarray | None = None) -> dict[str, np.ndarray]:
    """Model output for every parameter set (rows of P) and every shot -> {qoi: (m, K)}."""
    P = np.atleast_2d(P)
    m, K = len(P), len(thetas)
    base = nominal(spec)
    inp = {n: np.full(m * K, base[n]) for n in PARAMS}
    for j, n in enumerate(names):
        inp[n] = np.repeat(P[:, j], K)
    inp["theta"] = np.tile(thetas, m)
    if gust is not None:
        inp["wind"] = inp["wind"] + np.tile(gust, m)
    res = simulate(inp["v0"], inp["theta"], inp["cd"], inp["cl"], inp["mass"], inp["wind"], dt=dt)
    return {q: res.qoi(q).reshape(m, K) for q in qois}


def make_experiment(spec: dict, names: list[str], truth: dict[str, float], n_obs: int = 8,
                    theta_range: tuple[float, float] = (15.0, 65.0), noise: float = 1.0,
                    gust_std: float = 0.0, qois: list[str] = ("range",), seed: int = 0,
                    dt: float = 0.01) -> dict:
    check_names(spec, names)
    qois = list(qois)
    rng = np.random.default_rng(seed)
    lo, hi = theta_range
    thetas = np.linspace(lo, hi, n_obs) if n_obs > 1 else np.array([(lo + hi) / 2])
    P = np.array([[truth[n] for n in names]])
    gust = rng.normal(0.0, gust_std, n_obs) if gust_std > 0 else None
    clean = simulate_shots(spec, names, P, thetas, qois, dt, gust)
    obs = {q: clean[q][0] + rng.normal(0.0, noise, n_obs) for q in qois}
    # the true model response (without gusts), for display only
    curve = np.linspace(5, 85, 81)
    true_curve = simulate_shots(spec, names, P, curve, qois, dt)
    return {"names": names, "truth": truth, "theta": thetas.tolist(), "noise": noise, "gust_std": gust_std,
            "obs": {q: v.tolist() for q, v in obs.items()},
            "true_curve": {"theta": curve.tolist(), **{q: v[0].tolist() for q, v in true_curve.items()}}}


class Posterior:
    """Unnormalised log-posterior over the calibrated parameters."""

    def __init__(self, spec, names, thetas, obs: dict, sigma: float, dt: float, emulators=None):
        self.spec, self.names, self.dt = spec, names, dt
        self.thetas = np.asarray(thetas, float)
        self.obs = {q: np.asarray(v, float) for q, v in obs.items()}
        self.qois = list(self.obs)
        self.sigma = sigma
        self.emulators = emulators  # {qoi: Surrogate on names + ["theta"]} or None
        self.marginals = [marginal(spec[n]) for n in names]
        self.lo = np.array([PARAMS[n].lo for n in names])
        self.hi = np.array([PARAMS[n].hi for n in names])
        self.model_runs = 0

    def log_prior(self, P: np.ndarray) -> np.ndarray:
        P = np.atleast_2d(P)
        with np.errstate(divide="ignore"):
            lp = sum(m.logpdf(P[:, j]) for j, m in enumerate(self.marginals))
        inside = np.all((P >= self.lo) & (P <= self.hi), axis=1)
        return np.where(inside, lp, -np.inf)

    def predict(self, P: np.ndarray) -> dict[str, np.ndarray]:
        P = np.atleast_2d(P)
        self.model_runs += len(P) * len(self.thetas)
        if self.emulators is None:
            return simulate_shots(self.spec, self.names, P, self.thetas, self.qois, self.dt)
        X = np.column_stack([np.repeat(P, len(self.thetas), axis=0), np.tile(self.thetas, len(P))])
        return {q: self.emulators[q].predict(X).reshape(len(P), -1) for q in self.qois}

    def log_lik(self, P: np.ndarray) -> np.ndarray:
        pred = self.predict(P)
        return sum(-0.5 * np.sum(((pred[q] - self.obs[q]) / self.sigma) ** 2, axis=1) for q in self.qois)

    def __call__(self, P: np.ndarray) -> np.ndarray:
        P = np.atleast_2d(P)
        lp = self.log_prior(P)
        ok = np.isfinite(lp)
        if ok.any():
            lp[ok] += self.log_lik(P[ok])
        return lp


def train_emulators(spec, names, theta_range, qois, dt, n_train=250, seed=0):
    """GP emulator of the QoI as a function of (calibrated params, launch angle)."""
    inputs = names + ["theta"]
    box = box_from_spec(spec, names, k=4.0) + [tuple(map(float, theta_range))]
    X = doe.scale(doe.unit_design("lhs_opt", n_train, len(inputs), seed), box)
    out, info = {}, {}
    from .params import evaluate
    for q in qois:
        s = Surrogate("gp", inputs, box, q, dt, spec, X, evaluate(spec, inputs, X, q, dt)).fit(seed)
        Xt, yt = test_set(spec, inputs, box, q, dt, 300, seed)
        out[q] = s
        info[q] = {**scores(yt, s.predict(Xt)), "kernel": str(s.estimator.kernel_)}
    return out, {"n_train": n_train, "box": box, "scores": info}


def grid_posterior(post: Posterior, n_samples: int = 4000, seed: int = 0) -> dict:
    """Exact posterior on a regular grid over the prior box (mean +/- 4 std)."""
    d = len(post.names)
    n_per = {1: 400, 2: 70, 3: 22}[d]
    box = box_from_spec(post.spec, post.names, k=4.0)
    axes = [np.linspace(lo, hi, n_per) for lo, hi in box]
    mesh = np.meshgrid(*axes, indexing="ij")
    P = np.column_stack([m.ravel() for m in mesh])
    lp = post(P)
    w = np.exp(lp - lp.max())
    w /= w.sum()
    W = w.reshape(mesh[0].shape)
    steps = [a[1] - a[0] for a in axes]
    marg = []
    for j in range(d):
        other = tuple(k for k in range(d) if k != j)
        marg.append((W.sum(axis=other) if other else W) / steps[j])
    pairs = []
    for i in range(d):
        for j in range(i + 1, d):
            other = tuple(k for k in range(d) if k not in (i, j))
            Wij = W.sum(axis=other) if other else W
            pairs.append({"i": i, "j": j, "density": (Wij / (steps[i] * steps[j])).T.tolist()})  # rows = j
    rng = np.random.default_rng(seed)
    idx = rng.choice(len(w), size=n_samples, p=w)
    samples = P[idx] + (rng.random((n_samples, d)) - 0.5) * np.array(steps)
    return {"axes": [a.tolist() for a in axes], "marginals": [m.tolist() for m in marg], "pairs": pairs,
            "samples": samples, "map": P[np.argmax(lp)].tolist(), "n_points": int(len(P))}


def stretch_mcmc(post: Posterior, n_walkers: int = 32, n_iter: int = 300, burn: int = 100,
                 seed: int = 0, a: float = 2.0) -> dict:
    """Affine-invariant ensemble sampler: each half of the walkers moves along
    lines through walkers of the other half (no step size to tune)."""
    rng = np.random.default_rng(seed)
    d = len(post.names)
    W = n_walkers + n_walkers % 2
    X = from_unit(post.spec, post.names, rng.random((W, d)))  # start from the prior
    lp = post(X)
    chain = np.empty((n_iter, W, d))
    lps = np.empty((n_iter, W))
    accepted = 0
    halves = [np.arange(0, W, 2), np.arange(1, W, 2)]
    for it in range(n_iter):
        for h in (0, 1):
            S, C = halves[h], halves[1 - h]
            z = ((a - 1.0) * rng.random(len(S)) + 1.0) ** 2 / a
            Y = X[rng.choice(C, len(S))]
            prop = Y + z[:, None] * (X[S] - Y)
            lp_prop = post(prop)
            with np.errstate(invalid="ignore"):
                log_r = (d - 1) * np.log(z) + lp_prop - lp[S]
            acc = np.log(rng.random(len(S))) < log_r
            X[S[acc]] = prop[acc]
            lp[S[acc]] = lp_prop[acc]
            accepted += acc.sum()
        chain[it] = X
        lps[it] = lp
    burn = min(burn, n_iter - 1)
    samples = chain[burn:].reshape(-1, d)
    flat_lp = lps[burn:].ravel()
    return {"samples": samples, "map": samples[np.argmax(flat_lp)].tolist(),
            "acceptance": float(accepted / (n_iter * W)), "burn": burn, "n_walkers": W, "n_iter": n_iter,
            "traces": chain[:, : min(W, 8), :].transpose(2, 1, 0).tolist()}  # [param][walker][iteration]


def _band(values: np.ndarray) -> dict:
    p = np.percentile(values, [5, 50, 95], axis=0)
    return {"p05": p[0].tolist(), "p50": p[1].tolist(), "p95": p[2].tolist()}


def calibrate(spec: dict, names: list[str], thetas, obs: dict, sigma: float, method: str = "grid",
              use_emulator: bool = True, n_walkers: int = 32, n_iter: int = 300, burn: int = 100,
              theta_range=(15.0, 65.0), theta_new: float = 45.0, pred_qoi: str = "range",
              truth: dict | None = None, seed: int = 0, dt: float = 0.01) -> dict:
    check_names(spec, names)
    if pred_qoi not in QOIS:
        raise ValueError(f"unknown QoI {pred_qoi!r}")
    if not obs or any(len(v) != len(thetas) for v in obs.values()):
        raise ValueError("each observed QoI needs one value per shot")
    t0 = time.perf_counter()
    out: dict = {"names": names, "method": method}
    emus = None
    if method == "mcmc" and use_emulator:
        lo, hi = min(theta_range[0], min(thetas)), max(theta_range[1], max(thetas))
        emus, out["emulator"] = train_emulators(spec, names, (lo, hi), list(obs), dt, seed=seed)
    post = Posterior(spec, names, thetas, obs, sigma, dt, emus)
    if method == "grid":
        res = grid_posterior(post, seed=seed)
        out["grid"] = {k: res[k] for k in ("axes", "marginals", "pairs", "n_points")}
    elif method == "mcmc":
        res = stretch_mcmc(post, n_walkers, n_iter, burn, seed)
        out["mcmc"] = {k: res[k] for k in ("acceptance", "burn", "n_walkers", "n_iter", "traces")}
    else:
        raise ValueError(f"unknown method {method!r}")
    out["seconds"] = time.perf_counter() - t0
    out["model_runs"] = post.model_runs  # evaluations of the likelihood's model (simulator or emulator)
    out["simulator_runs"] = out["emulator"]["n_train"] * len(obs) if emus else post.model_runs

    rng = np.random.default_rng(seed + 7)
    post_s = res["samples"]
    prior_s = from_unit(spec, names, rng.random((4000, len(names))))
    out["samples"] = {"prior": prior_s[:2000].round(6).tolist(), "posterior": post_s[:: max(1, len(post_s) // 3000)].round(6).tolist()}

    summary = []
    for j, n in enumerate(names):
        pr, po = prior_s[:, j], post_s[:, j]
        ci_pr, ci_po = np.percentile(pr, [2.5, 97.5]), np.percentile(po, [2.5, 97.5])
        row = {"name": n, "prior_mean": float(pr.mean()), "prior_std": float(pr.std()), "prior_ci": ci_pr.tolist(),
               "post_mean": float(po.mean()), "post_std": float(po.std()), "post_ci": ci_po.tolist(),
               "map": float(res["map"][j]), "prior_kde": kde(pr), "post_kde": kde(po)}
        if truth and n in truth:
            row["truth"] = float(truth[n])
            row["truth_in_ci"] = bool(ci_po[0] <= truth[n] <= ci_po[1])
        summary.append(row)
    out["summary"] = summary
    out["correlation"] = np.corrcoef(post_s.T).tolist() if len(names) > 1 else [[1.0]]

    # Predictions with the simulator: prior vs posterior uncertainty
    curve = np.linspace(5, 85, 33)
    k = 150
    pick = lambda S: S[rng.choice(len(S), min(k, len(S)), replace=False)]  # noqa: E731
    pc = simulate_shots(spec, names, pick(prior_s), curve, [pred_qoi], dt)[pred_qoi]
    qc = simulate_shots(spec, names, pick(post_s), curve, [pred_qoi], dt)[pred_qoi]
    out["predictive_curve"] = {"theta": curve.tolist(), "qoi": pred_qoi, "prior": _band(pc), "posterior": _band(qc)}
    m = 1500
    pa = simulate_shots(spec, names, prior_s[:m], np.array([theta_new]), [pred_qoi], dt)[pred_qoi][:, 0]
    pb = simulate_shots(spec, names, post_s[rng.choice(len(post_s), min(m, len(post_s)), replace=False)],
                        np.array([theta_new]), [pred_qoi], dt)[pred_qoi][:, 0]
    out["prediction"] = {"theta": theta_new, "qoi": pred_qoi,
                         "prior": {**summarize(pa), "kde": kde(pa)}, "posterior": {**summarize(pb), "kde": kde(pb)}}
    if truth:
        tv = simulate_shots(spec, names, np.array([[truth[n] for n in names]]), np.array([theta_new]), [pred_qoi], dt)
        out["prediction"]["truth"] = float(tv[pred_qoi][0, 0])
    return out
