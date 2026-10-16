# Context Curator — working plan (planning phase, living doc)

## Context
Planning is still at an early stage. The user leads, step by step, from broad objectives down to specs.
This file records the current shared understanding. No specs or implementation yet.

## Project in one-liners
- **What:** a "context curator" for working sessions with an LLM. It makes what the model receives visible, organized and editable by a human.
- **Two faces:** (1) an interactive context/history editor where you see, emphasize, prune and organize; (2) a workbench dashboard showing tokens, usage and cost, proposing moves, and running test calls, A/B sub-calls and sandboxed agentic runs.
- **Core challenge:** turning a large mass of unstructured text into a form a human can grasp and act on. UI ergonomics is the main feature, not finishing polish.
- **Core tension:** deterministic, rule-based curation (predictable, free) versus LLM-assisted curation (more capable, but costly and less predictable).
- **Frame:** start with the Claude API (direct calls with the user's own key) and its message data model. Other endpoints and models stay an open perspective, to generalize once there's enough experience.

---

## Coherent view: one pipeline, four layers around it

### The spine (a data pipeline that runs on every turn)
```
 Transcript ─┐                                   ┌─> UI rendering (C)
 Edit log  ──┼─> Extraction ─> KR (derived view) ┤
 Injections ─┘      ▲                            └─> Curation (B) ──> Operations
                    │                                                 (drop/replace/pin/insert)
                    │                                                      │
 API response <── API call <── Assembler (compiles the prompt) <───────────┘
      │                                                               Edit log
      └────────────────────────> Transcript (append)
```
- **Source of truth:** the transcript (what happened, never modified) plus the edit log. KR is always derived from them, with links back to the source text.
- **One contract:** every change, from a human or a machine, is an operation: drop, replace, pin or insert.
- **The assembler** compiles the prompt actually sent: transcript + edits + injections → system prompt + messages.

### Control layer: the agent loop and its gates (the driver of the spine)
- The spine runs at each **loop step**, not once per user turn. A step is an API call, a batch of tool calls, or an output from another agent.
- The loop is a small state machine: assemble → **gate** → call API → parse → (tool_use → **gate** → execute → append results → loop) | (end_turn → wait for the user).
- **Gate:** the single checkpoint before any action runs. It holds a *pending action*: either the next assembled prompt or the proposed list of tool calls. At the gate the user can approve, reject, edit (through the pipeline: KR → operations → reassemble) or branch.
- **Gate policy:** a per-action decision of auto, review or deny. The tension between automation and safety lives in this policy configuration, not in loop code. v1 policy: review everything, plus a simple allowlist.
- **Tool-call visualization (C):** render each pending tool call by its effect: a diff for edits, the command with the paths it touches, network access, reversibility. This shows the blast radius. Analysis is deterministic first.
- **Executor:** a narrow interface (tool call → result), local in v1 and in a sandbox later.

### Layer 1 — Foundation (A): data & transport
- API port: messages, roles, system, tool turns, caching. The API is stateless, so the full prompt is re-sent on every call.
- Schema: parse responses into the transcript; assemble the prompt from it.
- State model and persistence: transcript, edit log, KR snapshots, runs (for A/B tests, metrics and replay).

### Layer 2 — KR spine
- **Ontology (what):** domains, levels of objectives, notions, facts, decisions, and so on.
- **Representation (how):** graph, hierarchy, or a mix.
- **Extraction:** text → KR, by rules, an LLM, or the user.
- **Provenance:** each KR node points to its source spans, which makes the round trip possible.

### Layer 3 — Curation & analysis (B)
- Operations on context through KR (filter, sort, prune, summarize, emphasize).
- Policy per operation: manual, rule-based, or LLM-in-the-loop.
- Metrics: tokens, cost, cache hits and invalidations, length, density and depth, repetitions, vagueness.

### Layer 4 — Interaction (C)
- Conversation view (low-level rendering).
- KR/history navigator and editor: edits made there become operations.
- Workbench dashboard: metrics, suggested moves, A/B runs.

### Extensions (D): plugged into the spine
- **Injection sources** (skills/library, fetched content, RAG, persona): feed the assembler through **insert**, tagged with their origin.
- **Harness/sandbox** (tests, grounding): uses the pipeline to run sub-calls and feeds results back as injections.
- **Multi-agent breakdown:** several pipelines or sub-sessions; this comes later.

---

## KR strategy (agreed)
1. Treat the KR pipeline and its risks as **high profile**: the round trip is the app's core.
2. **v1:** commit to one concrete ontology and one extraction process. Build around it and test both ergonomics and curation effectiveness.
3. **Open design:** leave room for other KR models and extraction methods.

## Decide early (cheap now, expensive to retrofit)
1. **History as a tree of steps** (parent pointers), not a flat list, so branching, A/B runs and "edit then retry" are native.
2. **Append-only step/event records:** API call, response, tool proposal, gate decision, tool result, edit.
3. **One gate point** in the loop with a policy hook. Automation is added later as policy, without changing the loop.
4. **Executor behind a narrow interface.**

**Defer:** multi-agent orchestration, a rich policy language, LLM-based risk assessment, running branches in parallel.

## Risks and constraints to keep in view
- **Per-step pipeline cost:** extracting KR at every loop step may be slow or costly. Extraction should be incremental, or done lazily at the gates where the user actually looks.
- **Approval fatigue vs. blast radius:** review everything is safe but tiring; auto is fast but risky. Grading the policy by risk class tunes this.
- **Round trip:** without provenance, editing KR can't become real edits of the context.
- **API message rules:** role alternation, tool_use/tool_result pairs and signed thinking blocks limit which operations are valid.
- **Caching cost:** an edit invalidates the cache from the edit point onward, and a system or persona change invalidates all of it. Stable content goes first and volatile content last, and the dashboard should show what each edit costs.
- **LLM extraction:** results may differ between runs, it costs money on every turn, and it raises the choice between updating as messages arrive and re-extracting everything.
- **Measuring effectiveness:** it needs a baseline (curated vs. uncurated), so persistence and A/B testing must come before v1 can be evaluated.
- **Premature abstraction:** build v1 concretely; define the plug-in interfaces once a second variant exists.
- **Scope:** tie the v1 ontology to one target use case (e.g. coding sessions). D is broad and close to a full agent harness.

## High-profile questions / to decide (tracking v1 → v2)
- **Standalone vs. companion:** our own loop and API calls, or beside existing harnesses (Claude Code transcripts and hooks), or both? See `benchmark.md`.
- **KR v1:** pick the ontology and the extraction mode (user-authored / LLM-extracted / rules).
- **Side effects:** how to mark steps and snapshot or sandbox them before branching or replay is allowed.
- **Differentiation:** a clear statement of what sets us apart from ThoughtDAG, Context Viewer and Letta ADE.
- **Persistence format:** our own, or aligned with existing trace formats (OpenTelemetry GenAI, LangSmith/Langfuse).

## Next
- The user reviews this view, then we set the order and strategy and go deeper into each layer.
