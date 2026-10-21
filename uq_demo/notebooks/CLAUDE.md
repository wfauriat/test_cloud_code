# Task: a teaching notebook on uncertainty quantification (UQ), built on the ballistic example

## Context
- `uq_demo/` contains a working interactive app (FastAPI + React). Its numerics live in the Python package **`uq_demo/uq_core/`**, which is tested (`uq_demo/tests/`, 41 tests). Install it with `pip install -e "uq_demo[dev]"`. Do not change the app's behaviour. If you touch `uq_core`, keep it backward compatible and keep `pytest` green.
- Goal: a notebook (Jupyter) that walks through the UQ themes on the same ballistic case: simulation, uncertainty propagation, design of experiments (DoE), surrogate modelling, sensitivity analysis, robust optimisation and Bayesian calibration. A side helper module holds the boilerplate (ODE, distributions, plotting).

## The physical model (keep it identical to the app)
- Point mass, state (x, y, vx, vy). Relative air velocity u = v − w (w = horizontal wind, + = tailwind), k = ½ ρ S:
  `a = −g ŷ − (k Cd/m)|u| u + (k Cl/m)|u| perp(u)`, with perp(u) = (−u_y, u_x).
- Constants: g = 9.81, ρ = 1.225, ball diameter 0.22 m (S = πd²/4), flight-time cap 60 s.
- Explicit Euler with step dt (default 0.01 s). Impact found by linear interpolation of the ground crossing. RK4 is available as a reference.
- Inputs: `v0` [m/s], `theta` [deg], `cd`, `cl`, `mass` [kg], `wind` [m/s].
  Defaults (value ± std): v0 30 ± 1, theta 40 ± 1.5, cd 0.25 ± 0.03, cl 0.10 ± 0.03, mass 0.43 ± 0.01, wind 0 ± 2.
  Physical bounds: v0 [1, 80], theta [1, 89], cd [0, 1.5], cl [−0.5, 0.5], mass [0.05, 5], wind [−25, 25].
- Quantities of interest (QoI): range, max_height, flight_time, impact_speed. Default target: range 55 ± 3 m.

## Reusable code in `uq_demo/uq_core/` (import it; don't copy it)
- `ballistics.py`: `simulate(v0, theta_deg, cd, cl, mass, wind, dt=0.01, scheme="euler"|"rk4", record=0, max_points=200) -> SimResult` (fields `.range .max_height .flight_time .impact_speed .landed .trajectories`, method `.qoi(name)`). **Vectorised:** every argument may be an array of shape (N,), including `dt`. 10 000 trajectories take about 0.2 s, but each call has about 10 ms of fixed overhead, so batch your calls. `vacuum_trajectory(v0, theta)` gives the exact drag-free parabola.
- `params.py`: `PARAMS` (metadata and bounds), `QOIS`, `default_spec()`, `normalize_spec(dict)`, `nominal(spec)`, `uncertain_names(spec)`, `marginal(entry)` (frozen scipy distribution), `from_unit(spec, names, U)` (unit-hypercube points → physical values through the inverse CDFs), `box_from_spec(spec, names, k)` (mean ± kσ box), `full_inputs`, `run_model`, `evaluate(spec, names, X, qoi, dt)` (QoI at the rows of X; the other inputs stay at nominal).
  A *spec* is `{name: {"value", "std", "dist", "uncertain"}}`, and `value` is the mean when the input is uncertain.
- `doe.py`: `unit_design(method, n, d, seed)` with methods `random | lhs | lhs_opt | sobol | halton | factorial`, `scale`, `to_unit`, `metrics(U)` (min distance, centred discrepancy).
- `propagation.py`: `monte_carlo(...)`, `fosm(spec, qoi, dt)` (first-order second-moment), `summarize`, `kde`, `convergence`.
- `surrogate.py`: `make_estimator(kind)` with kinds `poly1|poly2|poly3|gp|rf|mlp`; `Surrogate(...).fit()` and `.predict(X, return_std=True)`; `train(...)`, `learning_curve(...)`, `slice_1d(..., anchor=)`, `surface_2d(..., anchor=)`.
- `sensitivity.py`: `oat`, `morris`, `sobol(fn, spec, names, n_base, seed, n_boot)` (Saltelli first-order + Jansen total, bootstrap confidence intervals, model-call counter). `fn(X)` takes the uncertain inputs as columns.
- `robust.py`: `optimize(spec, design, bounds, qoi, target, tol, lam, n_mc, grid, use_surrogate, ...)` and `tolerance_study(...)`.
- `calibration.py`: `make_experiment(...)`, `Posterior` (log prior + Gaussian log-likelihood), `grid_posterior`, `stretch_mcmc` (affine-invariant ensemble sampler), `train_emulators` (GP emulator), `calibrate(...)`.

## Lessons learned while building the app (reflect them in the notebook)
1. **Lognormal convention:** "mean" and "std" are the moments of X itself. σ_ln² = ln(1 + cv²), μ_ln = ln(mean) − σ_ln²/2. State this explicitly.
2. **Interpolating GP:** the simulator is deterministic, so the GP uses a 1e-8 jitter, not a fitted nugget. Report the latent std, which is about 0 at the training points. In more than two dimensions, a 1D or 2D slice through nominal values passes near no training point; slice *through a training point* to show σ dropping to zero there.
3. **Inputs nearly linear:** within ±3σ of the defaults the response is close to linear, so quadratic polynomials and the GP reach Q² ≈ 1. Use wider boxes (k = 4–5), small designs (n ≈ 10–20) or the max-height QoI to make surrogate comparisons interesting.
4. **Sobol estimators:** centre the outputs before the Saltelli/Jansen estimators (huge variance reduction). Base sizes N = 2^m. Cost N(d + 2).
5. **Default sensitivity ranking:** wind > Cd > v0 > θ for the range (S₁ ≈ 0.52 / 0.30 / 0.15 / 0.01; Σ S₁ ≈ 0.98, nearly additive).
6. **Robust optimisation:** use common random numbers so the objective landscape is smooth. With wind σ = 2 and target 55 ± 3: the deterministic optimum (θ ≈ 39°, v0 ≈ 31) hits the target about 42% of the time; robust optima move to flatter, faster shots (θ ≈ 18–20°, v0 ≈ 33–35), about 47–48%. Always re-check optima on the true simulator with fresh samples. Wind caps the achievable hit probability (tolerance study).
7. **Calibration:**
   - Calibrating Cd from 8 shots (θ from 15 to 65°, 1 m noise) shrinks the posterior std about 6×, and the predictive std at 45° falls from about 2.7 m to about 0.4 m.
   - **Identifiability:** only Cd/m enters the equations, so a joint Cd–mass posterior is a correlated ridge (widen the mass prior to about 0.1 to see it).
   - **Model error:** unmodelled wind gusts (σ = 3 m/s) cut the 95% interval coverage to about 4/10 datasets unless the assumed noise is inflated (σ = 4 → 9/10).
   - θ is the experimental condition, so it is not calibrated.
8. Landed trajectories are integrated below ground (cheaper than freezing them); outputs are recorded at impact. Euler error is first order in dt.

## Deliverables
- `uq_demo/notebooks/uq_ballistic_course.ipynb`: one notebook. Split it into numbered notebooks (`01_…` to `08_…`) only if a full run takes more than about 5 minutes.
- `uq_demo/notebooks/ballistic_helpers.py`: a thin, readable layer over `uq_core`:
  - notebook-friendly wrappers, e.g. `run(**inputs)`, `sample_inputs(spec, n, method)`, `qoi_samples(...)`;
  - matplotlib plotting helpers (trajectories, spaghetti plot, histogram + KDE, pair plot of a design, parity plot, slice with ±2σ band, tornado, Morris μ*–σ, Sobol bars, robust landscape, prior/posterior).
  - Keep plotting out of the notebook cells where it would distract from the method.
- Add `notebook = ["jupyter", "matplotlib", "nbclient"]` (or similar) as an optional dependency group in `uq_demo/pyproject.toml`.
- A short `uq_demo/notebooks/README.md`: how to install, run and execute it headlessly.
- A test that executes the notebook headlessly (for example pytest + `nbclient`, or `jupyter nbconvert --to notebook --execute`). Mark it slow if needed.

## Pedagogical principles
- Each section starts with **learning goals** and ends with **takeaways** and 1–3 **exercises** ("change X and observe Y"), with hints.
- **Show the core algorithms explicitly in the notebook**, short and readable, then cross-check them against the `uq_core` implementation in one line:
  - the Monte Carlo loop, LHS stratification and the space-filling metric;
  - fitting a GP with scikit-learn;
  - the Saltelli/Jansen formulas;
  - a random-walk Metropolis sampler (simple), compared with the grid posterior and with `stretch_mcmc`.
  - Black-box calls only for the plumbing.
- Text in English. Equations in Markdown/LaTeX. Every figure has axis labels with units and a one-sentence caption that says what to notice.
- Fixed random seeds everywhere; the notebook must be reproducible and run top to bottom.
- Runtime budget: under about 3–5 minutes on a laptop. Use small N in the first pass and point to bigger N in the exercises.

## Outline (adapt as needed)
0. **Setup and the model:** equations, Euler scheme, parameters table, one trajectory vs the vacuum parabola; Euler convergence vs dt (log-log, slope 1) against an RK4 reference.
1. **Deterministic exploration:** QoI vs angle (best angle < 45° with drag, flat optimum); effect of Cd, mass (Cd/m), lift and wind.
2. **Uncertainty propagation:** input laws; Monte Carlo of the QoI (histogram, KDE, quantiles, P(miss target)); 1/√n convergence and confidence intervals; plain MC vs LHS vs Sobol sampling; FOSM vs MC, and where FOSM breaks (large std); range vs max-height joint distribution.
3. **Design of experiments:** random vs LHS vs optimised LHS vs Sobol/Halton vs full factorial; pair plots; min distance and discrepancy; the curse of dimensionality.
4. **Surrogate models:**
   - polynomial, GP, random forest and optionally MLP;
   - train/test split, Q², RMSE and parity plot;
   - learning curves;
   - the GP σ band and its calibration (how often |error| < 2σ);
   - slices through a training point;
   - speed-up vs the simulator.
5. **Sensitivity analysis:** tornado (one-at-a-time) → Morris → Sobol on the simulator and on the surrogate; cost comparison; convergence of the indices with N; interactions (Σ S₁ vs 1).
6. **Robust optimisation:** design variables = means of v0 and θ, with wind and Cd as nuisance parameters; deterministic vs mean–variance vs chance-constraint objectives on a 2D landscape with common random numbers; optima re-checked on the simulator; tolerance allocation (P(hit) vs std of v0 and θ).
7. **Bayesian calibration:** synthetic shots; prior → likelihood → posterior on a grid (1D, then Cd–mass in 2D showing the ridge); hand-written Metropolis vs ensemble MCMC (traces, acceptance rate, burn-in); GP emulator for the likelihood; posterior predictive; model error with unmodelled gusts and inflated noise.
8. **Wrap-up:** the UQ workflow (model → input uncertainty → DoE → surrogate → SA → optimisation / calibration), pointers to the interactive app (`uq_demo/README.md`) and further reading.

## Acceptance criteria
- `pip install -e "uq_demo[dev,notebook]"`, then executing the notebook headlessly finishes without error within the budget, and the existing 41 tests still pass.
- The numbers quoted in the markdown match the executed outputs (do not hard-code numbers that the code then contradicts).
