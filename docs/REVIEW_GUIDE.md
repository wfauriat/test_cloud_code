# Review guide

Reading order, and where the provisional calls are. Grep for `# QUESTION:` (a provisional call you may want to revisit), `# QUIRK:` (behaviour met while building, see `quirks.md`) and `PLAN §` (link to `plan_v2.md`).

## 1. The pure core: `backend/curator/core/`
No I/O. Every function can be called from a notebook: `from curator.core.render import render`.

| Module | What it does | Solid / provisional |
|---|---|---|
| `model.py` | Block, Event, Span, Op, Preamble, Request, RenderResult | Solid. Origin is metadata, never sent. |
| `wire.py` | hashing, comparison keys, the flattened request (`positions`) | Comparison keeps JSON key order (conservative). |
| `segment.py` | text of a block; deterministic segmenter | Segmenter v1 is minimal; ops never store segment ids. |
| `tokens.py` | estimates + calibration against reported usage | `chars / 3.2` prior; calibration fixes it per session. |
| `ops.py` | fold ops into per-block plans; op checks | Overlap rule: the later op wins. Tool calls can be dropped, not rewritten. |
| `render.py` | THE assembler: events + ops → request + source map | Thinking modes `keep` / `strip_all`. |
| `repair.py` | structural repairs after ops, each reported | System-message folding exists for imports. |
| `validate.py` | THE validator | v1 rule list; every 400 seen live should add a rule + test. |
| `prefix.py` | where two requests diverge; thinking at risk / lost | The central "see the tension" tool. |
| `costs.py` | prices, call cost, edit economics | Simplified cache model; Haiku cache prices unverified. |
| `rules.py` | R1–R4 deterministic proposals | Tool-name mapping per source. |
| `policy.py` | auto / review / deny | Allowlist only; default review. |

## 2. Adapters and services
- `adapters/store.py`: all SQL. Two mutable fields only (`sessions.head`, `ops.state`).
- `adapters/importers/claude_code.py`: the log format and its quirks.
- `services/sessions.py`: import, composition, usage timeline, calibration.
- `services/staging.py`: op creation (checked) and the staged preview (diff + economics).
- `cli.py`: everything above from the command line.

## 3. API and UI
- `backend/curator/api/schemas.py`: the API contract. TS types are generated from it (`frontend/src/api/schema.d.ts`).
- `backend/curator/api/app.py`: routes only.
- `frontend/src/api/client.ts`: the typed client. `Preview` is hand-typed (marked QUESTION).
- `frontend/src/views/Look.tsx`: outline, context map, document (virtualized), inspector, keyboard.
- `frontend/src/views/Timeline.tsx`: per-call usage chart and table.
- `frontend/src/views/Curate.tsx`: proposals, ops, brief, preview, request view.
- The UI never computes anything the backend owns (PLAN D4): every preview is a backend call.

## 4. Tests
`backend/tests/`: `test_render.py` (one test per render, repair or validator rule), `test_core.py` (ops, prefix, costs with the spec's worked example, rules, calibration, policy), `test_import.py` (a synthetic log reproducing the format's quirks).
