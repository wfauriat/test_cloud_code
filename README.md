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

## Try it (step B4: live loop)

The **Live** tab creates a live session: a workspace folder, a model, and an effort. The system prompt and tool list are frozen at creation.

- **Calls:** each call stops at the prompt gate (approve with `a`). Write tools stop at the tool gate (approve / deny with a reason / modify the input). Read-only tools in the workspace run without a stop.
- **Checks:** every request is checked append-only against the previous one. Staged edits on already-sent content wait for **Apply staged edits to history**, which strips the thinking produced on the old prefix and starts a new epoch.
- **Logging:** gate timings, calls, verifier blocks and API errors go to the observations log.

Live calls use your key: run the backend with `ANTHROPIC_API_KEY` set. To try the gates without a model or a key:

```bash
cd backend && CURATOR_PROVIDER=echo uv run uvicorn curator.api.app:app --port 8765   # "ls" in a message triggers a list_dir call
```

## Try it (step B5: experiments)

- **A/B tab (next-step A/B, Q5, Q8):**
  - Pick a cut point (before call N) and the arms: as is, curated (your staged ops), the server's `clear_tool_uses` with keep N (the baseline the curator must beat), and curated + brief.
  - **Preview cost** gives tokens and an estimate per arm. **Run** sends each arm once (tools declared, never executed; thinking stripped in all arms) and shows the proposed next steps side by side. Record a verdict.
  - Real calls on your key: preview first.
- **LLM draft summary (inspector, Look tab):**
  - A side call (Haiku 5.5) drafts a summary of a block or a message. You can edit it.
  - **Accept** freezes it into staged ops (replace + drop, author `llm:<call>`); nothing changes before that.
- **Observations:** `curator export` or `GET /api/observations.jsonl` give every logged measurement for your analysis.

## Exporting a session and seeing the exact wire

- **Full export** (one JSONL file: session + frozen preamble, events, ops, calls with the exact request and raw response, brief, runs, observations): **Export session** in the Live tab, `GET /api/sessions/<sid>/export.jsonl`, or `uv run curator export-session <sid> --out session.jsonl`.
- **The exact request sent to the API:**
  - for a past call, click its row in the Live tab's Calls table, or run `uv run curator wire <sid> --call N [--response] [--out req.json]` (default: the last call);
  - for the request waiting at the prompt gate, **View request JSON**.
  - Imported sessions have no wire log; `curator render` reconstructs their requests (approximate).

## Build status

| Step | Status |
|---|---|
| B1 core + import + CLI | done, tested |
| B2 Look + Timeline | done |
| B3 Curate (ops, staging, preview, brief, request view) | done |
| B4 Live loop (gates, executor, verifier, rebuild) | thin: tested with fakes only; not yet run against the real API |
| B5 Experiments (A/B, draft summary) | thin: tested with fakes only |

Not built (PLAN §0, §1 "Deferred"): SSE streaming, semantic KR, collateral checks, retention probes, sandbox, keep-alive, an API-log importer.

After changing `backend/curator/api/schemas.py`, run `npm run gen:api` in `frontend/` to regenerate the TS types.
