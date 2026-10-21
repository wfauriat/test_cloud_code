# Ballistic UQ Lab

An interactive app for teaching **uncertainty quantification** (UQ) on a simple case: a ball launched
through air with drag, lift and wind, integrated with the explicit Euler scheme.

- **Python core** (`uq_core/`): the model and all UQ numerics (numpy, scipy, scikit-learn).
- **FastAPI backend** (`api/`): a stateless JSON API over the core. Trained surrogates are cached in memory.
- **React + Vite + TypeScript front-end** (`frontend/`): Plotly.js for the charts, D3 for the trajectory view.

## Quick start

```bash
cd uq_demo
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest                                                 # 40 tests, ~25 s

# Option A, one process: build the front-end once; FastAPI serves it
cd frontend && npm install && npm run build && cd ..
uvicorn api.main:app                                   # open http://127.0.0.1:8000

# Option B, development with hot reload: two terminals
uvicorn api.main:app --reload                          # terminal 1 (in uq_demo/)
cd frontend && npm install && npm run dev              # terminal 2, open http://localhost:5173
```

Requires Python ≥ 3.10 and Node ≥ 18. Each tab can be opened directly with `?tab=sim|mc|doe|sur|sa|rob|cal`.

## The model

State (x, y, vx, vy), relative air velocity u = v − w (w = horizontal wind, positive = tailwind), and k = ½ρS:

    a = −g ŷ − (k Cd / m) |u| u + (k Cl / m) |u| perp(u)

Inputs: initial speed `v0`, launch angle `theta`, drag `cd`, lift `cl`, mass `mass` (it scales drag and lift as
Cd/m and Cl/m), wind `wind`. Ball diameter 0.22 m, ρ = 1.225 kg/m³. QoIs: range, max height, flight time,
impact speed. Integration is vectorised over samples: 10 000 Monte Carlo trajectories take about 0.2 s.

Every input has a nominal value and can be switched to **uncertain** (normal, uniform or lognormal law with a
given mean and std). Sampling always goes through the unit hypercube and the inverse CDFs, so Monte Carlo,
DoE and Sobol share one code path.
For every law, "mean" and "std" are the moments of the input itself. For a lognormal, the parameters of
ln X are derived from them: σ_ln² = ln(1 + (std/mean)²) and μ_ln = ln(mean) − σ_ln²/2. The panel displays them.

The Gaussian-process surrogate interpolates (kriging with a 1e-8 jitter), because the simulator is
deterministic. Its σ is the latent-function std: zero at the training points. A fitted nugget is used only
as a fallback when the covariance matrix is ill-conditioned.

## The seven tabs (lessons)

| # | Tab | What it teaches |
|---|-----|-----------------|
| 1 | Simulator | The deterministic model; comparison with the vacuum parabola; range vs angle (the best angle is < 45° with drag); Euler first-order convergence vs dt. |
| 2 | Uncertainty propagation | Monte Carlo (random / LHS / Sobol): spaghetti plot, histogram + KDE, quantiles, P(miss target), 1/√n convergence, FOSM (linearised) comparison, output vs each input. |
| 3 | Design of experiments | Random, LHS, optimized LHS, Sobol, Halton, full factorial; pairwise projections; min distance and discrepancy compared across methods; editable input box. |
| 4 | Surrogate model | Polynomial (1–3), Gaussian process, random forest, MLP; test Q²/RMSE, parity plot, 1D slice with the GP ±2σ band, 2D response surface (prediction / truth / error / GP std), learning curves. |
| 5 | Sensitivity analysis | One-at-a-time tornado, Morris (μ*, σ), Sobol S₁/S_T with bootstrap CIs, on the simulator or on the surrogate, with a cost table ("what if one run took 1 min?"). |
| 6 | Robust design | Choose the means of 1–2 design variables; wind, Cd… act as nuisance parameters. Compares deterministic, mean–variance and chance-constraint optima on a landscape, re-checks each on the true simulator, and runs a tolerance-allocation study (P(hit) vs the std of the design variables). |
| 7 | Bayesian calibration | Infer 1–3 parameters (Cd, Cl, mass, v0, wind) from synthetic noisy shots at known angles. Exact grid posterior or ensemble MCMC (stretch move) on the simulator or a GP emulator; prior → posterior marginals, joint posterior (Cd/mass identifiability ridge), traces, posterior predictive bands, prediction of a new shot. Unmodelled wind gusts show the effect of model error. |

With the defaults (target range 55 ± 3 m, wind σ = 2 m/s), the deterministic design (θ ≈ 39°) hits the
target only about 42% of the time. The robust designs pick flatter, faster shots (θ ≈ 18–20°), which are less
sensitive to the wind, and reach about 47–48%.

## Layout

```
uq_core/   ballistics.py  params.py  propagation.py  doe.py  surrogate.py  sensitivity.py  robust.py  calibration.py
api/       main.py                      FastAPI endpoints (/api/...)
frontend/  src/App.tsx, src/tabs/*.tsx, src/components/{TrajectoryView (D3), Plot (Plotly), ParamPanel}
tests/     test_core.py (numerics), test_api.py (endpoints), test_calibration.py
```

With the defaults in tab 7 (Cd prior 0.25 ± 0.03, true Cd 0.286, 8 shots, 1 m noise), the posterior std of
Cd shrinks about 6×, and the predicted range of a new 45° shot goes from ±2.7 m to ±0.4 m. With 3 m/s
unmodelled gusts, the 95% interval covers the truth in only about 4 out of 10 datasets, unless the assumed
noise is inflated.
