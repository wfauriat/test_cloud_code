# Context Curator: exploratory build

A first build for experimenting with real material. Its scope and the questions it is meant to answer are in [`plan_v2.md`](plan_v2.md). The other files at the root are the planning trail: `overall_intent.md` → `plan_v1.md` → `specs_claude.md` → `critique_specs_v1.md` → `plan_v2.md`.

- `backend/`: Python. All the logic lives here; `backend/curator/core/` is pure (no I/O) and is the place to start reading ([`docs/REVIEW_GUIDE.md`](docs/REVIEW_GUIDE.md)).
- `frontend/`: React + TypeScript, a thin view over the backend API (step B2).
- `docs/quirks.md`: API and format surprises met while building.
- `workspace/` (git-ignored): your database and the transcripts you import. Real transcripts contain personal context and must not be committed.

## Try it (step B1: backend + CLI)

```bash
cd backend
uv sync
uv run pytest -q

# import one of your Claude Code sessions (they live in ~/.claude/projects/<project>/<session>.jsonl)
uv run curator import ~/.claude/projects/<project>/<session>.jsonl
uv run curator sessions
uv run curator show <sid>          # composition by kind, calibration (hidden preamble size)
uv run curator timeline <sid>      # per-call cache read/write, cache breaks (Q2)
uv run curator rules <sid>         # deterministic proposals (Q3); add --stage to stage them all
uv run curator diff <sid> --staged         # what the staged edits change and cost, warm cache (Q4)
uv run curator diff <sid> --staged --cold  # same, cold cache
uv run curator render <sid> --call 5 --out req.json   # the reconstructed request of call 5
uv run curator cost --before 300000 --after 200000 --prefix 0   # edit economics by hand
uv run curator export <sid>        # observations as JSONL, for your analysis
```

The database defaults to `workspace/curator.db` (`--db` or `CURATOR_DB` to change it).

## Try it (steps B2–B3: UI)

Two terminals:

```bash
cd backend && uv run uvicorn curator.api.app:app --host 127.0.0.1 --port 8765
cd frontend && npm install && npm run dev     # http://127.0.0.1:5173
```

- **Look**:
  - outline (left) and context map (thin strip, height ∝ tokens, colored by kind; hatched = dropped or edited, bar at right = pinned);
  - document (center) and inspector (right).
  - Keys: `j`/`k` move, `d` drop, `p` pin, `r` replace, `i` note after, `u` revoke. Select text inside a block, then "Drop selection" or "Replace selection" targets a span.
- **Timeline**: input per call split into cache read / write / uncached, with cache breaks marked (Q2).
- **Curate**:
  - rule proposals, ops, and the brief;
  - the preview of what staged edits change and cost, warm or cold, with or without the brief (Q3, Q4, Q8);
  - "Render" shows the exact request that would be sent.

After changing `backend/curator/api/schemas.py`, run `npm run gen:api` in `frontend/` to regenerate the TS types.
