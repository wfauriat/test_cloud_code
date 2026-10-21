"""Notebook helpers for the ballistic UQ course.

A thin layer over `uq_core` (the tested numerics of the interactive app):
convenience wrappers to run the model and draw samples, and the matplotlib
figures used in the notebook, so that the notebook cells can focus on the
methods. Nothing here re-implements the numerics.
"""
from __future__ import annotations

import copy
import textwrap
import time
from contextlib import contextmanager

import matplotlib.pyplot as plt
import numpy as np

from uq_core import doe, params
from uq_core.ballistics import SimResult, simulate
from uq_core.params import PARAMS, QOIS

# --------------------------------------------------------------------------- #
# Labels and style
# --------------------------------------------------------------------------- #

SYMBOLS = {"v0": r"$v_0$", "theta": r"$\theta$", "cd": r"$C_d$", "cl": r"$C_l$", "mass": r"$m$", "wind": r"$w$"}
COLORS = plt.rcParams["axes.prop_cycle"].by_key()["color"]


def label(name: str) -> str:
    """Axis label with unit for an input or a QoI, e.g. 'Launch angle θ [deg]'."""
    if name in PARAMS:
        p = PARAMS[name]
        unit = "-" if p.unit == "-" else p.unit
        return f"{p.label.replace(' Cd', '').replace(' Cl', '')} {SYMBOLS[name]} [{unit}]"
    title, unit = QOIS[name]
    return f"{title} [{unit}]"


def setup_style():
    plt.rcParams.update({
        "figure.figsize": (7.5, 4.2), "figure.dpi": 90, "axes.grid": True, "grid.alpha": 0.3,
        "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False,
        "font.size": 10,
    })


def show(fig, caption: str):
    """Attach a one-sentence caption under the figure and display it."""
    if not getattr(fig, "manual_layout", False):
        fig.tight_layout()
    fig.text(0.5, 0.0, "\n".join(textwrap.wrap(caption, 115)), ha="center", va="top",
             fontsize=9.5, style="italic")
    plt.show()


@contextmanager
def timer(what: str = "elapsed"):
    """`with timer("MC"): ...` prints the wall time of the block."""
    t = time.perf_counter()
    yield
    print(f"{what}: {time.perf_counter() - t:.2f} s")


# --------------------------------------------------------------------------- #
# Model wrappers
# --------------------------------------------------------------------------- #

def spec_with(base: dict | None = None, **changes) -> dict:
    """Copy of a spec (default: the app defaults) with some entries changed,
    e.g. spec_with(cd={"dist": "lognormal"}, wind={"std": 4}).
    """
    spec = copy.deepcopy(base) if base is not None else params.default_spec()
    for name, entry in changes.items():
        spec[name] = {**spec[name], **entry}
    return params.normalize_spec(spec)


def run(dt: float = 0.01, scheme: str = "euler", record: int = 0, **inputs) -> SimResult:
    """Run the simulator; inputs not given take their default nominal value.
    Every input may be an array (vectorised)."""
    nom = params.nominal(params.default_spec())
    x = {**nom, **inputs}
    return simulate(x["v0"], x["theta"], x["cd"], x["cl"], x["mass"], x["wind"], dt=dt, scheme=scheme,
                    record=record)


def sample_inputs(spec: dict, n: int, method: str = "random", seed: int = 0, names: list[str] | None = None):
    """n samples of the uncertain inputs (columns = names) through the unit hypercube."""
    names = names or params.uncertain_names(spec)
    U = doe.unit_design(method, n, len(names), seed)
    return params.from_unit(spec, names, U), names


def qoi_samples(spec: dict, n: int, method: str = "random", seed: int = 0, qoi: str | list[str] = "range",
                dt: float = 0.01):
    """Monte Carlo samples of one QoI (array) or several (dict), plus the inputs."""
    X, names = sample_inputs(spec, n, method, seed)
    res = params.run_model(params.full_inputs(spec, names, X), dt)
    y = res.qoi(qoi) if isinstance(qoi, str) else {q: res.qoi(q) for q in qoi}
    return y, X, names


def params_table(spec: dict) -> str:
    """Markdown table of the inputs (display it with IPython.display.Markdown)."""
    rows = ["| input | meaning | unit | nominal / mean | std | law | uncertain | bounds |",
            "|---|---|---|---|---|---|---|---|"]
    for n, p in PARAMS.items():
        e = spec[n]
        rows.append(f"| `{n}` | {p.label} | {p.unit} | {e['value']:g} | {e['std']:g} | {e['dist']} | "
                    f"{'yes' if e['uncertain'] else 'no'} | [{p.lo:g}, {p.hi:g}] |")
    return "\n".join(rows)


# --------------------------------------------------------------------------- #
# Plots: simulation and propagation
# --------------------------------------------------------------------------- #

def plot_trajectories(trajs, labels=None, ax=None, **kw):
    """trajs: list of (n, 2) arrays or (x, y) pairs."""
    ax = ax or plt.subplots()[1]
    for i, t in enumerate(trajs):
        x, y = (t[:, 0], t[:, 1]) if isinstance(t, np.ndarray) else t
        ax.plot(x, y, label=None if labels is None else labels[i], **kw)
    ax.set_xlabel("Horizontal distance x [m]")
    ax.set_ylabel("Height y [m]")
    ax.set_ylim(bottom=0)
    if labels is not None:
        ax.legend()
    return ax


def plot_spaghetti(trajs, ax=None, target=None, tol=None, color="C0"):
    ax = ax or plt.subplots()[1]
    for t in trajs:
        ax.plot(t[:, 0], t[:, 1], color=color, lw=0.7, alpha=0.35)
    if target is not None:
        ax.axvspan(target - tol, target + tol, color="C2", alpha=0.2, label=f"target {target:g} ± {tol:g} m")
        ax.legend(loc="upper left")
    ax.set_xlabel("Horizontal distance x [m]")
    ax.set_ylabel("Height y [m]")
    ax.set_ylim(bottom=0)
    return ax


def plot_hist_kde(y, ax=None, xlabel="Range [m]", target=None, tol=None, quantiles=(5, 50, 95), bins=50,
                  color="C0", label_=None):
    from uq_core.propagation import kde
    ax = ax or plt.subplots()[1]
    ax.hist(y, bins=bins, density=True, alpha=0.35, color=color, label=label_)
    k = kde(y)
    ax.plot(k["x"], k["y"], color=color, lw=2, label=None if label_ else "KDE")
    for q, v in zip(quantiles, np.percentile(y, quantiles)):
        ax.axvline(v, color=color, ls=":", lw=1)
        ax.text(v, ax.get_ylim()[1] * 0.97, f"p{q}", ha="center", va="top", fontsize=8, color=color)
    if target is not None:
        ax.axvspan(target - tol, target + tol, color="C2", alpha=0.15, label="target band")
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Probability density [1/unit]")
    ax.legend()
    return ax


def plot_convergence(conv: dict, ax=None, exact=None, ylabel="Mean range [m]"):
    ax = ax or plt.subplots()[1]
    ax.fill_between(conv["n"], conv["lo"], conv["hi"], alpha=0.25, label="95% confidence interval")
    ax.plot(conv["n"], conv["mean"], "o-", ms=3, label="running mean")
    if exact is not None:
        ax.axhline(exact, color="k", ls="--", lw=1, label="reference")
    ax.set_xscale("log")
    ax.set_xlabel("Number of samples n [-]")
    ax.set_ylabel(ylabel)
    ax.legend()
    return ax


# --------------------------------------------------------------------------- #
# Plots: design of experiments
# --------------------------------------------------------------------------- #

def plot_design_2d(U, ax, title="", strata: int | None = None):
    ax.scatter(U[:, 0], U[:, 1], s=18, zorder=3)
    if strata:
        for g in np.linspace(0, 1, strata + 1):
            ax.axvline(g, color="grey", lw=0.4)
            ax.axhline(g, color="grey", lw=0.4)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.grid(False)
    ax.set_title(title, fontsize=10)
    ax.set_xlabel(r"$u_1$ [-]")
    ax.set_ylabel(r"$u_2$ [-]")
    return ax


def plot_pairs(X, names, color=None, title=None, bins=8, box=None, cbar_label=None):
    """Pair plot (scatter of every pair of columns, histograms on the diagonal).
    With `box`, the histogram bins span the design box, so a stratified design shows flat marginals."""
    d = len(names)
    fig, axes = plt.subplots(d, d, figsize=(1.9 * d + 1, 1.9 * d + 0.5))
    sc = None
    for i in range(d):
        for j in range(d):
            ax = axes[i, j]
            ax.grid(False)
            if i == j:
                edges = bins if box is None else np.linspace(*box[j], bins + 1)
                ax.hist(X[:, j], bins=edges, color="C0", alpha=0.6)
                ax.set_yticks([])
            else:
                sc = ax.scatter(X[:, j], X[:, i], s=8, c=color, cmap="viridis")
            if i == d - 1:
                ax.set_xlabel(label(names[j]), fontsize=8)
            else:
                ax.set_xticklabels([])
            if j == 0 and i > 0:
                ax.set_ylabel(label(names[i]), fontsize=8)
            elif j > 0:
                ax.set_yticklabels([])
    if title:
        fig.suptitle(title)
    fig.subplots_adjust(left=0.1, bottom=0.1, right=0.86 if cbar_label else 0.97, top=0.95,
                        wspace=0.08, hspace=0.08)
    fig.manual_layout = True  # keep this layout in show()
    if color is not None and cbar_label:
        fig.colorbar(sc, cax=fig.add_axes([0.89, 0.3, 0.02, 0.45]), label=cbar_label)
    return fig


# --------------------------------------------------------------------------- #
# Plots: surrogates
# --------------------------------------------------------------------------- #

def plot_parity(y_true, y_pred, ax=None, title="", unit="m"):
    ax = ax or plt.subplots()[1]
    lo, hi = min(np.min(y_true), np.min(y_pred)), max(np.max(y_true), np.max(y_pred))
    ax.plot([lo, hi], [lo, hi], "k--", lw=1)
    ax.scatter(y_true, y_pred, s=6, alpha=0.5)
    ax.set_xlabel(f"Simulator [{unit}]")
    ax.set_ylabel(f"Surrogate [{unit}]")
    ax.set_title(title, fontsize=10)
    ax.set_aspect("equal")
    return ax


def plot_slice(sl: dict, param: str, ax=None, qoi="range", title="", near: float = 0.05):
    """1D slice of a surrogate (output of uq_core.surrogate.slice_1d) with its ±2σ band.
    Training points closer than `near` (unit-box distance) to the slice are drawn filled."""
    ax = ax or plt.subplots()[1]
    x, m, t = np.array(sl["x"]), np.array(sl["pred"]), np.array(sl["true"])
    ax.plot(x, t, "k-", lw=1.5, label="simulator")
    ax.plot(x, m, "C1-", lw=1.5, label="surrogate mean")
    if sl["std"] is not None:
        s = np.array(sl["std"])
        ax.fill_between(x, m - 2 * s, m + 2 * s, color="C1", alpha=0.25, label="±2σ")
    dist = np.array(sl["train_dist"])
    close = dist < near
    ax.scatter(np.array(sl["train_x"])[close], np.array(sl["train_y"])[close], c="C3", s=30, zorder=4,
               label="training point on the slice")
    ax.scatter(np.array(sl["train_x"])[~close], np.array(sl["train_y"])[~close], facecolors="none",
               edgecolors="grey", s=18, zorder=3, label="training points (projected)")
    ax.set_xlabel(label(param))
    ax.set_ylabel(label(qoi))
    ax.set_title(title, fontsize=10)
    ax.legend(fontsize=8)
    return ax


def plot_learning_curves(lc: dict, ax=None, metric="rmse", unit="m"):
    ax = ax or plt.subplots()[1]
    for kind, c in lc["curves"].items():
        ax.plot(lc["sizes"], c[metric], "o-", label=c["label"])
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Training-set size n [-]")
    ax.set_ylabel(f"Test RMSE [{unit}]" if metric == "rmse" else "1 − Q² [-]")
    ax.legend(fontsize=8)
    return ax


# --------------------------------------------------------------------------- #
# Plots: sensitivity analysis
# --------------------------------------------------------------------------- #

def plot_tornado(oat: dict, ax=None, xlabel="Range [m]"):
    ax = ax or plt.subplots()[1]
    rows = oat["rows"][::-1]
    base = oat["base"]
    for i, r in enumerate(rows):
        ax.barh(i, r["y_lo"] - base, left=base, color="C0", alpha=0.7, label="input at p5" if i == 0 else None)
        ax.barh(i, r["y_hi"] - base, left=base, color="C3", alpha=0.7, label="input at p95" if i == 0 else None)
    ax.axvline(base, color="k", lw=1)
    ax.set_yticks(range(len(rows)), [SYMBOLS[r["name"]] for r in rows])
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Input")
    ax.legend()
    return ax


def plot_morris(mo: dict, ax=None, unit="m"):
    ax = ax or plt.subplots()[1]
    for i, r in enumerate(mo["rows"]):
        ax.scatter(r["mu_star"], r["sigma"], s=50, color=COLORS[i % len(COLORS)])
        ax.annotate(SYMBOLS[r["name"]], (r["mu_star"], r["sigma"]), xytext=(6, 4), textcoords="offset points")
    top = max(max(r["mu_star"], r["sigma"]) for r in mo["rows"]) * 1.1
    ax.plot([0, top], [0, top], "k:", lw=1, label=r"$\sigma = \mu^*$")
    ax.set_xlim(0, top)
    ax.set_ylim(0, top)
    ax.set_xlabel(rf"$\mu^*$ (mean |elementary effect|) [{unit}]")
    ax.set_ylabel(rf"$\sigma$ (std of elementary effects) [{unit}]")
    ax.legend()
    return ax


def plot_sobol(results: dict, ax=None):
    """results: {label: output of uq_core.sensitivity.sobol}; grouped S1 / ST bars with bootstrap CIs."""
    ax = ax or plt.subplots()[1]
    names = [r["name"] for r in next(iter(results.values()))["rows"]]
    k = len(results)
    w = 0.8 / (2 * k)
    x = np.arange(len(names))
    for i, (lab, res) in enumerate(results.items()):
        rows = {r["name"]: r for r in res["rows"]}
        for jdx, key in enumerate(("S1", "ST")):
            v = np.array([rows[n][key] for n in names])
            ci = np.array([rows[n][key + "_ci"] for n in names])
            off = (2 * i + jdx - (2 * k - 1) / 2) * w
            ax.bar(x + off, v, w, yerr=[v - ci[:, 0], ci[:, 1] - v], capsize=2,
                   color=COLORS[i % len(COLORS)], alpha=1.0 if key == "S1" else 0.45,
                   label=f"{key} ({lab})")
    ax.set_xticks(x, [SYMBOLS[n] for n in names])
    ax.set_xlabel("Input")
    ax.set_ylabel("Sobol index [-]")
    ax.legend(fontsize=8)
    return ax


# --------------------------------------------------------------------------- #
# Plots: robust optimisation and calibration
# --------------------------------------------------------------------------- #

OPT_STYLE = {"deterministic": ("o", "w"), "mean_var": ("s", "C1"), "chance": ("*", "C3")}


def plot_landscape(out: dict, field: str, target: float, ax=None, title="", cbar_label="", optima=True, levels=20,
                   log=False):
    """Contour of a robust.optimize grid field over the 2 design variables (v0, theta order)."""
    ax = ax or plt.subplots()[1]
    ax0, ax1 = (np.array(a) for a in out["grid"]["axes"])
    Z = out["grid"]["objective"][field] if field in out["grid"]["objective"] else out["grid"][field]
    Z = np.array(Z)
    if log:
        Z = np.log10(Z + 1e-6)
    cs = ax.contourf(ax0, ax1, Z, levels=levels, cmap="viridis")
    plt.colorbar(cs, ax=ax, label=cbar_label)
    ax.contour(ax0, ax1, np.array(out["grid"]["nominal"]), levels=[target], colors="w",
               linewidths=1, linestyles="--")
    if optima:
        for kind, o in out["optima"].items():
            mk, c = OPT_STYLE[kind]
            ax.plot(*[o["x"][d] for d in out["design"]], mk, color=c, mec="k", ms=10, label=kind)
        ax.legend(fontsize=8, loc="upper right")
    ax.set_xlabel(label(out["design"][0]))
    ax.set_ylabel(label(out["design"][1]))
    ax.set_title(title, fontsize=10)
    ax.grid(False)
    return ax


def plot_prior_posterior(prior_samples, post_samples, name, ax=None, truth=None, grid=None):
    """Prior and posterior densities of one parameter (KDE of samples, optional exact grid curve)."""
    from uq_core.propagation import kde
    ax = ax or plt.subplots()[1]
    for s, lab, c in ((prior_samples, "prior", "C0"), (post_samples, "posterior", "C3")):
        k = kde(np.asarray(s))
        ax.plot(k["x"], k["y"], color=c, lw=2, label=lab)
        ax.fill_between(k["x"], k["y"], color=c, alpha=0.15)
    if grid is not None:
        ax.plot(grid[0], grid[1], "k--", lw=1, label="grid posterior")
    if truth is not None:
        ax.axvline(truth, color="k", lw=1, label="truth")
    ax.set_xlabel(label(name))
    ax.set_ylabel("Probability density [1/unit]")
    ax.legend()
    return ax


def plot_traces(chain, names, burn=None, ax=None, title=""):
    """chain: (n_iter, n_chains, d). One panel per parameter."""
    d = chain.shape[2]
    if ax is None:
        _, ax = plt.subplots(d, 1, figsize=(7.5, 2.2 * d), squeeze=False)
        ax = ax[:, 0]
    for j in range(d):
        ax[j].plot(chain[:, :, j], lw=0.6, alpha=0.8)
        if burn:
            ax[j].axvspan(0, burn, color="grey", alpha=0.2)
        ax[j].set_ylabel(label(names[j]))
    ax[-1].set_xlabel("Iteration [-]")
    ax[0].set_title(title, fontsize=10)
    return ax
