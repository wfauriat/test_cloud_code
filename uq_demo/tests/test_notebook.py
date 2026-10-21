"""Execute the teaching notebook headlessly, top to bottom (slow: about 1-2 minutes).

Run it with `pytest -m slow`; it is deselected by default.
"""
from pathlib import Path

import pytest

nbformat = pytest.importorskip("nbformat")
nbclient = pytest.importorskip("nbclient")
pytest.importorskip("matplotlib")

NOTEBOOK_DIR = Path(__file__).resolve().parents[1] / "notebooks"
NOTEBOOK = NOTEBOOK_DIR / "uq_ballistic_course.ipynb"


@pytest.mark.slow
def test_notebook_runs_top_to_bottom():
    nb = nbformat.read(NOTEBOOK, as_version=4)
    client = nbclient.NotebookClient(nb, timeout=600, kernel_name="python3",
                                     resources={"metadata": {"path": str(NOTEBOOK_DIR)}})
    client.execute()  # raises CellExecutionError on the first failing cell
    errors = [o for c in nb.cells if c.cell_type == "code" for o in c.get("outputs", [])
              if o.get("output_type") == "error"]
    assert not errors
