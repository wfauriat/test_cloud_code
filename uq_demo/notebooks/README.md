# UQ course notebook

`uq_ballistic_course.ipynb` is a hands-on course in uncertainty quantification on the ballistic model of
the Ballistic UQ Lab app. It covers simulation, uncertainty propagation, design of experiments, surrogate
models, sensitivity analysis, robust optimisation and Bayesian calibration. Each section has learning
goals, takeaways and exercises.

- The numerics come from the tested package `uq_core` (`../uq_core/`), which is shared with the app.
- `ballistic_helpers.py` holds the notebook wrappers (`run`, `sample_inputs`, `qoi_samples`, …) and the
  matplotlib figures.

## Install

From the `uq_demo/` directory:

```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev,notebook]"
```

## Run interactively

```bash
cd notebooks
jupyter lab uq_ballistic_course.ipynb                  # or: jupyter notebook
```

Run the cells top to bottom. A full run takes about 1–2 minutes on a laptop. All random seeds are fixed, so
the numbers you get match the text.

## Execute headlessly

```bash
# from uq_demo/: execute and keep the outputs in place
jupyter nbconvert --to notebook --execute --inplace notebooks/uq_ballistic_course.ipynb

# or as a test (deselected by default because it is slow)
pytest -m slow tests/test_notebook.py
```

Plain `pytest` runs the fast unit tests of `uq_core` and of the API only.
