# Context Curator — plan v2 (exploratory build)

## Context
Date: 2026-10-16. Inputs: `overall_intent.md`, `plan_v1.md`, `specs_claude.md`, `critique_specs_v1.md`, plus a cross-analysis pass that checked the critique's open API items against the Claude API reference.

This plan targets a **first, exploratory build**, not the full product. The goal is to work with real material and see the quirks and tensions in action. The results feed a later spec revision and a full build. So the build favors:
- code that is easy to read and review;
- seams left open, not features finished;
- instruments that log what happens, so it can be analyzed afterward.

Target stack: **Python backend** (all logic lives there) and a **React/TypeScript frontend** (a thin view).

---

## 0. What this build is for

### Questions the build must help answer
Each question has an instrument in the build and leaves rows in the observations log (§5.5).

| # | Question | Instrument |
|---|---|---|
| Q1 | Where do the tokens go in real sessions (by kind: tool results, thinking, text, harness injections)? | Import + context map + composition table |
| Q2 | How often did the cache break in real sessions, and why? | Usage timeline from imported per-call usage (cache read / write / uncached) |
| Q3 | How much do deterministic rules find (oversized, stale, superseded, duplicate)? | Rule proposals with token totals |
| Q4 | What does an edit really cost (cache rewrite + reasoning lost), warm vs. cold? | Staging economics + prefix diff |
| Q5 | Does curated context change what the model does next? | Next-step A/B, including a server-side baseline arm |
| Q6 | How tiring are gates in a live session? | Gate timing log (time to decide, approvals per minute) |
| Q7 | How far is imported material from the exact wire? | Estimated vs. reported vs. `count_tokens` counts |
| Q8 | Does a short, human-written brief (goals, decisions, constraints) help? | Brief as an optional A/B arm and in live sessions |

### Non-goals for this build
- LLM-extracted KR (semantic tier), collateral analysis, retention probes.
- Surgical "patch" commits that keep the cache before the edit point beyond what a deterministic re-render gives for free (see §1, D2).
- Sandbox/containment, multi-agent, MCP, RAG, server compaction, keep-alive pings.
- A rich policy language, auth, multi-user, packaging, polished design.

---

## 1. Decisions carried in

From the critique's filter (`critique_specs_v1.md` §7) and the cross-analysis.

| # | Decision | Why |
|---|---|---|
| D1 | **Append-only between edits.** Within a run of calls, each request = the previous one + appended content. Validated on every live call. | Verified API constraint: an earlier change voids later thinking and the cache. |
| D2 | **Three edit levels**, named plainly in the UI: *free* (not yet sent), *rewind/branch* (keeps all reasoning), *rebuild* (re-render with ops; thinking kept before the first change, stripped after it, the strip recorded). | Replaces the spec's patch-linker with one pure render function plus a prefix diff. |
| D3 | **Wire log for live sessions.** Response content is stored as returned and replayed as stored, never rebuilt from domain objects. Imported material is labeled *approximate*. | Byte-exact replay is needed for caching and thinking validity. |
| D4 | **One assembler, one validator**, in the backend only. The UI asks the backend for every preview; it never re-implements logic. | Keeps the spec's constraint (same code for preview and send) with a Python backend. |
| D5 | **Ops:** `drop`, `replace`, `pin`, `insert`, plus `revoke`. Spans are authoritative. A pin protects and can be repeated in the brief. | `plan_v1` contract + spec §4.3. |
| D6 | **Ingestion curation is automatic by rule** (bound oversized tool output before it is sent). Manual review only above a size threshold. | Avoids two gate stops per tool call. |
| D7 | **Brief = user-authored items** (goal, decision, constraint, fact). Sent once per user turn as a mid-conversation `system` message right after the user's message (GA, no `clear_at` dependency). Only human-written or human-accepted text goes there. | Authority concern (critique §5.2); Sonnet 5.5 can read a system message right after a tool result as injection; `clear_at` is a limited beta on Opus 5.5. Also `plan_v1`'s "one ontology, one extraction process": user-authored. |
| D8 | **Gates:** a prompt gate and a tool gate, one policy function (`auto / review / deny`, most restrictive wins). Default: review everything + an allowlist of read-only tools. Approval is tied to the request hash. | `plan_v1` Decide early #3. |
| D9 | **Evaluation early: next-step A/B.** Replay a request under variants and compare the model's *proposed* next action, without executing it. No isolation needed. Arms: as-is, curated, server baseline (`clear_tool_uses`, keep N), optional + brief. | Moves the baseline ahead of editing (`plan_v1.md:89`); sidesteps "branching doesn't rewind the world". |
| D10 | **Server-side context editing is off in the main loop** and available only as an A/B arm. It selects only by age, threshold and tool-name exclusion, and it still invalidates the cache where it clears. | Docs check (context-editing page). |
| D11 | **Frozen preamble per live session:** system prompt and tool definitions are fixed at session start and stored as sent. | Spec C7. |
| D12 | **Imported Claude Code sessions never replay thinking.** We don't have the system prompt and tools those blocks are bound to, so every API call built from imported material strips all thinking, in every arm. | Follows from the binding rule; a quirk this build should make visible. |

**Deferred, with the risk recorded:** collateral checks for KR-driven drops; re-fetch loop detection; keep-alive during review; per-model capability registry beyond a small dict; LLM thread labels.

---

## 2. Architecture

```
┌──────────── React + TS (Vite) — a thin view ─────────────┐
│ Sessions │ Outline │ Document + context map │ Inspector  │
│ Staging  │ Request view (as-sent, diff) │ Gate │ A/B      │
└───────────────▲───────────────────────────────┬──────────┘
                │ JSON over HTTP, SSE for live  │
┌───────────────┴───── FastAPI (127.0.0.1) ─────▼──────────┐
│ api/      routes only: parse, call a service, return     │
│ services/ import, sessions, staging, loop, experiments   │
│ core/     PURE functions, no I/O  ← review this first    │
│ adapters/ sqlite store, Anthropic SDK, executor, importers│
└──────────────────────────────────────────────────────────┘
```

- **The core is pure Python with no I/O.** It can be reviewed alone, tested alone, and used from a notebook or the CLI (`from curator.core import render`).
- **Types cross the boundary once:** pydantic models → OpenAPI → generated TS types (`openapi-typescript`). Nothing is typed by hand on both sides.

### Stack
| Part | Choice | Note |
|---|---|---|
| Python | 3.12+, `uv` | |
| Web | FastAPI + uvicorn | SSE for live loop events |
| Models | pydantic v2 for API shapes; dataclasses in core | |
| Store | stdlib `sqlite3`, explicit SQL in one module | No ORM: every query is readable |
| Claude | official `anthropic` Python SDK | Streaming + `get_final_message()`; `count_tokens` |
| Tests | pytest | Fixtures are synthetic; real transcripts stay local |
| Lint | ruff | |
| Frontend | Vite + React 18 + TS, `@tanstack/react-virtual` | No UI kit, no state library, hand-made SVG charts |

### Layout
```
backend/
  pyproject.toml
  curator/
    core/
      model.py      # Block, Message, Event, Span, Op, Request, SourceMap
      wire.py       # canonical JSON, block hashing, position flattening
      segment.py    # deterministic segmenter (v1: paragraphs, code fences, line chunks)
      tokens.py     # estimator + calibration against reported usage
      ops.py        # fold active ops → per-block intervals (keep/drop/replace/stub)
      render.py     # events + ops + preamble (+ brief) → request + source map + diagnostics
      repair.py     # tool_use/tool_result pairing, stubs, merges
      validate.py   # THE validator (only place that encodes API structure rules)
      prefix.py     # diff two requests: first divergence, cache impact, thinking voided
      costs.py      # price table + call cost + edit economics
      rules.py      # mechanical rules → proposals
      policy.py     # gate policy evaluation
    adapters/
      store.py
      importers/claude_code.py
      provider.py   # real SDK client + FakeProvider for tests
      executor.py   # local tools confined to a workspace dir
    services/
      sessions.py  staging.py  loop.py  experiments.py  observations.py
    api/
      app.py  routes/…
    cli.py          # inspect without the UI
  tests/
frontend/
  src/ api/ (generated types + client)  views/  components/
docs/
  REVIEW_GUIDE.md   # reading order, where the provisional calls are
  quirks.md         # quirks met during the build, for the spec revision
```

---

## 3. Data model

| Entity | Role |
|---|---|
| **Session** | `source`: `claude_code_import` or `live`. Model config, frozen preamble (live), workspace dir (live). |
| **Event** | Immutable, in a tree (`parent_id`). Kinds: `message` (role + ordered block refs), `tool_exec` (call id, effective args, raw output, exit, timing), `gate` (decision, time to decide), `import_meta`, `error`. |
| **Block** | Immutable content, stored once by hash (content-addressed). Kind: text, thinking, redacted_thinking, tool_use, tool_result, harness_injection, unknown. |
| **Call** | Wire log (live only): request as block hashes + params, raw response, usage, cost, latency, model, stop reason, epoch. |
| **Epoch** | A run of append-only calls; opened by the session start or by a rebuild. |
| **Op** | `verb`, `target` (spans), `payload`, `author` (`human`, `rule:<id>@v1`, `llm:<call>`, `assembler`), `rationale`, `state` (`draft → staged → applied | revoked`), group id. |
| **BriefItem** | Type (goal / decision / constraint / fact), text, status, author (always human, or human-accepted). |
| **Run** | One A/B run: arms, requests, responses, costs, user verdict. |
| **Observation** | `(ts, session, kind, payload_json)`; append-only; exportable as JSONL. |

**Addressing:** `(event_id, block_index, [start, end))` in Unicode code points over the block's text. Opaque blocks (thinking, redacted, unknown) are addressed whole only.

**Claude Code import mapping (approximate wire):**
- Assistant lines that share a `message.id` are one message; their blocks are merged in order and usage is taken once.
- Follow the `parentUuid` chain from the last entry back to the root. Other branches and `isSidechain` lines are counted, not imported, in v1.
- `attachment` entries (system reminders, hook output) become `harness_injection` blocks, placed where Claude Code rendered them when that is known.
- There is no system prompt and no tool definition in the log. The preamble stays empty and is marked unknown.
- Per-call `usage` (input, cache read, cache write, output) is kept on the assistant event. It gives the **exact total context size at each call**, which feeds Q2 and Q7 and calibrates the estimator.

---

## 4. Core pipeline (pure functions)

1. **`segment(block)`** → segments with spans. Versioned; ops never store segment IDs.
2. **`estimate(block)`** → tokens, marked `estimated`. A per-session ratio is calibrated against reported usage when available. Exact counts come only from `count_tokens` or usage.
3. **`fold(ops)`** → per-block intervals. Later op wins on overlap; shadowed ops are flagged. A machine op on a pinned span is rejected at creation.
4. **`render(events, ops, preamble, brief, mode)`** → `Request` + `SourceMap` + diagnostics.
   - `mode="append"`: the previous request plus the new tail, as stored (live).
   - `mode="rebuild"`: a full re-render with active ops. The caller passes the last sent request; thinking before the first divergence is kept, thinking after it is stripped, and the strip is recorded as an `assembler` op (so it stays stripped later).
   - `mode="replay"` (imports, A/B): a full re-render with **all** thinking stripped (D12).
5. **Repair rules** (each one reported in the diagnostics):
   - dropping or replacing a `tool_result` keeps the block and puts a placeholder inside it: `[curator: removed <what> · <why> · <how to recover>]`;
   - dropping a `tool_use` drops its result too and leaves a one-line note in the assistant text;
   - messages left empty are removed; adjacent same-role messages are merged;
   - the request must end on user content (no prefill).
6. **`validate(request, context)`** → list of violations. v1 rules: first message is `user`; tool_use/tool_result pairing by id, all results of one turn in one user message; placement of `system` messages (after a user message, not first); no empty text blocks; no trailing assistant message; kept thinking forms one contiguous run; opaque blocks match their stored hash; system and tools equal the frozen preamble (live). **Every 400 seen live becomes a new rule + test.**
7. **`prefix_diff(a, b)`** → requests flattened to positions (`tools[i]`, `system[j]`, `messages[k].content[l]`), compared on canonical JSON with `cache_control` ignored. Returns the first divergence, tokens before/after it, the thinking blocks after it (voided), and a verdict: `append_only` or `edit_at(position)`.
8. **`costs`** → for a request: cache read / cache write / uncached / estimated output, in $. For staged edits: next-call cost with vs. without the edit, savings per later call, "pays back after N calls", warm vs. cold. Reasoning lost is shown as *blocks and original thinking tokens*, with the documented drop-cost range as a reference, not as a computed price.
9. **`rules(events)`** → proposals (op groups with rationale and tokens saved per call):
   - R1 oversized tool output → head + tail + placeholder;
   - R2 stale file read (the file was edited or written later);
   - R3 superseded re-run (same command run again later);
   - R4 exact duplicate tool output (hash).

   Tool names are mapped per source (Claude Code: `Read`, `Edit`, `Write`, `Bash`…; live: our tool set).
10. **`policy(action)`** → `auto | review | deny` with the matching rule.

**Prices** live in one table in `costs.py` ($/MTok). Opus 5.5: 4 / 20, cache read 0.20, cache write 5.00 (5 min) or 8.00 (1 h). Sonnet 5.5: 2 / 10, read 0.20. Haiku 5.5: 0.10 / 0.50 up to 100k-token prompts. Values not in the bundled reference are marked `# QUESTION: verify`.

---

## 5. Services

### 5.1 Import and sessions
- `curator import <path.jsonl>` (CLI and UI): imports one Claude Code session. Originals are never modified.
- Computes composition, the usage timeline, and rule proposals at import. Writes observations (Q1–Q3, Q7).

### 5.2 Staging and rebuild
- Create, stage, revoke ops; pin; replace with your own text; insert a note.
- Preview the as-sent request for any mode, with the validator report and the prefix diff against the last sent request (live) or the original (import).
- Apply (live, only when idle = at a user-turn boundary): rebuild, start a new epoch, log the economics as an observation (Q4).

### 5.3 Live loop (thin)
- State machine: `idle → assembling → prompt_gate → calling → tool_gate → executing → ingesting → assembling …`, back to `idle` on `end_turn`. Persisted, so a restart resumes at the gate.
- **Prompt gate:** shows the delta since the last call, exact tokens (`count_tokens`), the cost split, the cache state (expires in mm:ss) and the validator report. Approve / reject / edit pending content.
- **Tool gate:** one card per call. A diff for file edits, the command and its paths for commands. Approve / deny with a reason / modify (the `tool_use` stays as the model wrote it; the edited call runs and the result says so).
- **Per-call verifier:** `prefix_diff(previous sent, next)` must be `append_only` unless a rebuild was applied. Otherwise the call is blocked and the mismatch logged.
- **Tools** (custom, `strict: true`, declared at session start): `read_file`, `list_dir`, `grep` (allowlisted); `write_file`, `edit_file` (review, diff); `run_command` (off by default, always review). The executor is confined to the session's workspace dir (canonical paths, timeouts, output cap, full raw output stored).
- **Request settings:** model `claude-opus-5-5` by default (selectable); adaptive thinking with `display: "summarized"`; effort explicit (default `medium`, selectable); streaming with `eager_input_streaming` on tools and inputs validated before execution; top-level automatic caching + a breakpoint on the preamble; refusal fallback `fallbacks: "default"` on, and when it fires the UI says the model changed (cache and thinking reset).
- **Budget guard for your own API spend:** per-call cap and per-session cap in config; the gate refuses above them.
- Needs `ANTHROPIC_API_KEY` on your machine. In this build container it is tested against `FakeProvider` only.

### 5.4 Experiments: next-step A/B (thin)
- Pick a cut point (a user turn or a tool-result turn) in a session. Arms: as-is, curated (staged ops), server baseline (`clear_tool_uses`, keep N), and optionally + brief.
- All arms: same model and effort, the same stand-in preamble (for imports: a system prompt you choose + stand-in definitions for the tool names seen in history), all thinking stripped (D12).
- **Before running:** exact `count_tokens` per arm and a cost estimate; you confirm. Arms run one after another with a cache breakpoint, so later arms read the prefix they share with arm 1.
- Tools are declared but never executed: the result is the *proposed* next step (text + tool calls). The view shows the arms side by side; you record a verdict. Everything is logged (Q5, Q8).
- **LLM draft summary (thin):** "summarize this selection" sends the selected blocks to a side call and returns a draft `replace` payload. It becomes an op only when you accept it (author `llm:<call>`), the core tension in its smallest form.

### 5.5 Observations
Auto-logged: import stats, rule findings, staged economics, live prefix verdicts, gate timings, API errors (full body), A/B runs and verdicts. `GET /observations.jsonl` and `curator export` give the raw rows for your analysis.

---

## 6. UI (React/TS)

- **Sessions:** list, import, create a live session.
- **Session view:**
  - left: outline (turns → blocks, one-line gist for tool steps, e.g. "Read src/app.py · 2.1k tok");
  - center: document (virtualized, a gutter with tokens and status) + the **context map** (a vertical strip proportional to tokens, colored by kind, with overlays for staged, dropped, pinned and the sent / not-yet-sent line);
  - right: inspector (block JSON, tokens exact/estimated, origin, ops, rule findings).
- **Bottom dock:** staging (ops, totals, economics, apply / discard) and the gate (live).
- **Request view:** as-sent JSON (collapsible), validator report, prefix diff between any two requests.
- **Usage timeline** (imports): per-call bars for cache read / cache write / uncached / output, with cache breaks marked.
- **A/B view:** set up, cost preview, side-by-side results, verdict.
- **Keyboard:** `j/k` move, `d` drop, `p` pin, `r` replace, `u` revoke, `a` approve, `x` deny. Text selection inside a block targets a span.

**UI words vs. internal words** (critique §4: internal terms must not leak):

| Internal | UI label |
|---|---|
| epoch / frontier | "sent" / "not sent yet" |
| rebuild commit | "Apply edits to history" |
| stub | placeholder |
| hoist | "repeat in brief" |
| break-even | "pays back after N calls" |
| TTL | "cache expires in mm:ss" |

---

## 7. Build scope and order

The build goes in five steps. Each step ends with tests passing, a short "try it" section in the README, and one commit.

| Step | Content | Depth |
|---|---|---|
| **B1 Core + import** | `core/` modules for model, wire, segment, tokens, ops, render (replay mode), repair, validate, prefix, costs, rules; sqlite store; Claude Code importer; CLI (`import`, `show`, `render`, `diff`, `rules`, `cost`); tests | **Core**: full and tested |
| **B2 Look** | FastAPI read routes; UI for sessions, outline, document, context map, inspector, usage timeline | **Core** |
| **B3 Curate** | Ops API + staging; rule proposals in the UI; request view (validator + prefix diff); economics; brief items | **Core** |
| **B4 Talk** | Provider wrapper + FakeProvider; loop state machine; prompt and tool gates; tools + executor; append and rebuild modes; per-call verifier; SSE | **Thin**: one happy path + the guards, tested with fakes |
| **B5 Experiment** | Next-step A/B with cost preview; LLM draft summary; observations export | **Thin** |

**Left out on purpose:** everything in §0 Non-goals and §1 Deferred, the API-log importer (unless you have such logs), and UI polish beyond legibility.

---

## 8. Review and testing aids
- **`docs/REVIEW_GUIDE.md`:** reading order (`core/model.py → render.py → repair.py → validate.py → prefix.py → costs.py → rules.py`, then the importer, then the loop). One paragraph per module on what is solid and what is provisional.
- **Greppable markers:**
  - `# QUESTION:` marks a provisional call you may want to revisit;
  - `# QUIRK:` marks API or format behavior met during the build, also listed in `docs/quirks.md`;
  - `# PLAN §x` links code to this plan.
- **Docstrings explain *why*,** not what.
- **Tests as examples:** golden render tests on small synthetic sessions, validator cases, prefix-diff cases, rule cases, an importer test on a synthetic Claude Code-shaped file, and loop tests with FakeProvider.
- **CLI for backend review without the UI:** e.g. `curator diff <session> --call 12 --call 13`, `curator render <session> --mode replay --at <event>`.
- **Real material stays local:** a `workspace/` folder (git-ignored) holds the DB and imported transcripts. The repo is public and transcripts contain personal context.

---

## 9. Build process and cost guard
- **Git:** work on branch `exploratory-build`, never `main`; this plan is its first commit; one commit per step, pushed after each step so you can review on GitHub.
- **Cost watcher:** a background script sums the token usage logged in this session's transcripts (main + any subagents) and prices it at API list price for Opus 5.5. At each $10 step I get woken and send you a push notification with the total and the step in progress. The watcher is a script, not an LLM loop, so it costs nothing itself. The figure is a list-price equivalent from logged usage; your actual billing may differ.
- **Budget:** target ≤ $45 for the build (planning so far is counted in the baseline at "go"). Rough split: B1 ~$10, B2 ~$9, B3 ~$10, B4 ~$8, B5 ~$5. Later steps cost more per action because the context is larger. **Hard rule:** I won't start a step whose estimate would cross $50. If the budget runs short I stop at a clean commit, and B5 then B4 get cut first.
- **Keeping it cheap:** no subagents for building (each starts cold), files written in whole pieces, tests run in batches, the frontend checked by type-check, build and one headless smoke test, not by screenshots. Practical UI testing is yours.

---

## 10. After the build: what the analysis should feed back
- **Q1–Q8 results** → which curation levers matter, and whether history editing deserves the surgical commit machinery (D2) or whether rewind + rebuild is enough.
- **`docs/quirks.md`** → corrections to the API assumptions and the import format.
- **Gate timing** → the shape of the policy (risk classes, what to auto-allow).
- **A/B verdicts** → whether a semantic KR (LLM-extracted) is worth its cost, and where it should plug in (brief first, drops later).
- **Open decisions kept for the spec revision:**
  - standalone vs. companion;
  - persistence format (own store vs. trace formats as exports);
  - which betas to depend on;
  - when commits could become automatic.
