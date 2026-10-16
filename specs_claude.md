# Context Curator — Architecture Specs (independent proposal)

*Written 2026-10-16. Sources: `overall_intent.md` (the only repo file read) plus the current Claude API reference (outside the repo). This is a planning document: the decisions below are deliberate calls, not locked in. Exact API facts and beta names are in Appendix A, so the body can stay high-level.*

**Markers:**
- **[DECISION]**: a fork I chose (the alternative is noted when the call is close).
- **[TRICKY]**: subtle logic that is easy to get wrong.
- **[RISKY]**: could sink a feature or the project.
- **[FRAGILE]**: correct today, breaks silently under change.

---

## 0. Summary: the decisions that shape everything

1. **Form factor.** A local-first app: a Node/TypeScript server plus a browser UI (React) in one repo, with a pure-TS core shared by both. The curator runs its own agent loop directly on the Messages API. No Agent SDK and no Managed Agents, because the curator must control every byte sent.
2. **Three logs are the source of truth.**
   - The *event log*: what happened, raw.
   - The *wire log*: the exact bytes sent and received on every call.
   - The *op log*: every edit.

   Everything else (KR, views, metrics) is derived from these.
3. **The API now charges for history edits, and this reshapes the design.** Current models bind each thinking block to the exact prefix that produced it: system prompt, tools and every earlier message. Editing an earlier turn invalidates all later reasoning. On accounts created on or after 2026-08-31, sending such a block back is a hard 400 error. Prompt caching is also an exact prefix match. So edits are **staged and applied in discrete commits**. Between commits the conversation is strictly **append-only**; I call that stretch an *epoch*. `overall_intent.md` assumes the prompt can be freely re-assembled on every step. This is the biggest correction.
4. **Assembler = patch-linker.** Unchanged history is copied from the stored wire bytes. Only what ops change is serialized again. The result is checked against API invariants before it can reach a gate.
5. **Curate at the door.** The cheapest curation happens before content is first sent: bounding tool outputs, trimming injections. It needs no commit. The UI shows the *frontier* between sent and pending content.
6. **Honest economics.** Every staged edit shows its commit cost (cache rewrite plus reasoning dropped) against its per-call savings and break-even point. Cache reads cost 0.05× on Opus 5.5, so pruning warm cached content rarely pays off in dollars. Curation is mainly a quality, focus and context-window tool. The best time to commit is when the cache is already cold.
7. **The KR has two tiers.**
   - A deterministic structural tier: always on, exact.
   - An LLM semantic tier: proposals with verified citations.

   The KR is extracted from the raw event log, with edit status overlaid, so pruned knowledge stays visible.
8. **LLM outputs are drafts until accepted.** Once accepted, they are frozen into the op log, so the log stays deterministic and replayable. This is how the core tension is contained.
9. **One policy engine** (auto / review / deny) governs every gate: prompt sends, tool calls, machine-proposed curation, injections, keep-alives and commits.
10. **Milestones are vertical slices:** Look → Talk → Edit → Structure → Understand → Experiment → Contain. M0 is a read-only viewer on real, large transcripts, because UI ergonomics is the core challenge.

## 1. Principles

- **WYSIWYS: what you see is what is sent.** The gate shows the exact request, and approval is tied to its hash.
- **Nothing that happened is ever modified.** Changes are ops, ops can be revoked, and a revocation is itself logged.
- **Deterministic core, probabilistic edges.** LLMs propose; deterministic code decides what gets sent.
- **Every cost is visible**, including the curator's own LLM spend: extraction, summaries, probes and keep-alives.
- **Fail closed** on execution. Anything the analyzer can't understand needs a human.
- **Opaque pass-through.** Unknown or signed API blocks are kept byte for byte and never "normalized".
- **Ergonomics is the product.** Judge every feature by whether it helps a human understand and act on 200k+ tokens.

## 2. The hard constraint: an append-only API vs. an editable history  [RISKY]

### 2.1 What the API enforces (October 2026)

- **Caching is an exact prefix match**, in the order tools → system → messages. A byte change at position N invalidates everything after N.
  - Writes cost 1.25× (5-minute TTL) or 2× (1-hour TTL).
  - Reads cost 0.1× (0.05× on Opus 5.5, 0.025× on Fable 5.1).
- **Preserved thinking** applies to Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5.
  - Each thinking block's signature binds the system prompt, the tool definitions and every earlier message.
  - Editing, reordering or removing an earlier turn invalidates every later thinking block, and so does rewriting the system prompt or tools.
  - Thinking blocks can only be removed from the front, from the back, or all at once. The ones you keep must stay contiguous.
  - In `drop_block` mode, the server discards invalid blocks instead of failing, at a measured cost in extra output tokens.
- **What stays valid:**
  - appending content, including mid-conversation `role:"system"` messages;
  - turn-scoped system messages left in place;
  - rewinding (dropping trailing turns);
  - changing request parameters outside system/tools/messages;
  - moving cache markers;
  - server-side context editing and compaction.
- **Byte-exact replay.** Thinking blocks and `tool_use` inputs must be echoed back exactly. Assistant prefill is not supported.
- **Model switches.** Caches are scoped to a model, and thinking that the target model can't read is dropped silently.

### 2.2 Consequences for the design

- **C1. Epochs and commits [DECISION].**
  - An *epoch* is a run of calls in which each request equals the previous request plus appended content, byte for byte. The cache stays warm and thinking stays valid.
  - A *commit* applies staged ops to content that was already sent and starts a new epoch. The cache restarts at the first changed position, and thinking after that position is stripped.
  - Ops on content not yet sent take effect at the next call, with no commit.
  - The intent's spine stays and still runs on every step. What changes is *when ops reach the wire*.
- **C2. The frontier.**
  - Every view draws a line between *sent in this epoch* and *pending*.
    - Sent content is frozen; editing it means staging an op for a commit.
    - Pending content can be edited freely.
  - Day-to-day curation should happen below the line: bound tool outputs before they are sent, trim fetched documents, choose injections.
- **C3. Copy-through, patch-only [FRAGILE].** History is replayed from the stored wire bytes and never rebuilt from domain objects. A lossy round trip is the top way to silently destroy caching and reasoning continuity. Typical culprits: whitespace, key order, number formats, dropped empty fields, or a stream parser that loses signatures.
- **C4. Commit points [TRICKY].** By default, a commit happens only at a user-turn boundary, with no tool round in flight. A commit in the middle of an autonomous tool loop drops the reasoning behind the pending tool calls. It is allowed, with a warning, as an "emergency commit", for example when the window is about to overflow.
- **C5. Recorded strips, and undo has a cost [FRAGILE].** A stripped thinking block must stay stripped in every later request, because putting it back invalidates newer blocks. So the strip is itself an op, authored by the assembler. Likewise, revoking a committed op after new turns is another edit, with its own cost. The UI must say so.
- **C6. Two edit regimes [DECISION].**
  - *Preserve* (the default): epochs and commits as described above.
  - *Free-edit*: thinking from prior turns is never sent back (only an untouched in-flight turn keeps its own), so any edit can apply at the next call.
    - The cost: more output tokens, because the model re-derives its reasoning. Anthropic measured about +10% at medium/high effort and +67% at max when thinking is dropped every turn.
    - Long tasks also lose continuity.
  - Older models without the prefix check (per current docs, for example Opus 5 and Sonnet 5) allow free editing while keeping thinking. This capability is per-model data.
- **C7. Frozen session preamble [DECISION].**
  - The system prompt and tool definitions, descriptions included, are fixed at session start.
  - Changes during a session go out as appended `role:"system"` messages. New tools are declared at the start as deferred and surfaced later.
  - Rewriting the system prompt remains possible, but it is a full-cost commit.
  - So the preamble must contain from the first turn: the curator's stub convention, the full tool set and the stable injections.
- **C8. Edit cost grows with depth.**
  - Rewinding or branching keeps all earlier reasoning valid, and reuses the cache when the branch point is recent.
  - A deep edit rewrites everything after it and drops the most reasoning.
  - The context map shades this gradient. When a mistake is recent, prefer branching from before the mistake over editing it.
- **C9. Verify continuously.**
  - Every call is diffed against the previous one. Outside a declared commit range, the overlap must be byte-identical.
  - Tests and CI run against the real API with mismatch behavior set to "error".
  - Normal runs use `drop_block` as a safety net, with the controls header on so the server reports its transformations. Any transformation the assembler did not predict is surfaced as a curator bug, never absorbed silently.
  - The exact token count at the gate runs the same check, so it doubles as a free validity pre-check before the real call.
- **C10. Server-side context features are off by default [DECISION].**
  - Context editing and server compaction preserve thinking, because they don't count as edits. But they act on the server's copy, so the curator can no longer show exactly what the model saw.
  - They are offered as named *server strategies*: comparable in A/B runs, useful for long autonomous runs, with the as-sent view labeled as approximate.
  - On-demand compaction (beta) is the only way to summarize a prefix and keep later reasoning valid. The price is a server-written, signed summary that can't be edited.
  - That is a real fork: an *editable summary* (curator commit) vs. a *reasoning-preserving summary* (server). v1 uses curator commits; M5 evaluates the server option.

## 3. Architecture overview

```
┌───────────────────────────── Browser UI (React) ─────────────────────────────┐
│ Navigator (outline / KR) │ Document view + context map │ Inspector           │
│ Gate panel │ Staging panel │ Workbench (dashboards, runs, A/B)                │
└───────────────▲──────────────────────────────────────────┬───────────────────┘
                │ state stream (WebSocket)                 │ commands: ops, approvals, commits
┌───────────────┴───────────────── Local server (Node) ────▼───────────────────┐
│ Session service ─ Loop runner (state machine) ─ Gate service ─ Policy engine  │
│ Assembler (patch-linker) ─ Validator ─ Cache planner ─ Cost model             │
│ KR service: mechanical extractor (sync) · thread segmenter · LLM jobs (async) │
│ Curation: rule engine · proposal builder · LLM curation jobs                  │
│ Provider port (official Anthropic TS SDK) ─ Executor (local → sandbox)        │
│ Store: SQLite (append-only tables) + content-addressed blob store            │
└──────────────────────────────────────────────────────────────────────────────┘
core/ (pure TS, no I/O, shared by server and UI): schemas, op fold, assembler,
validator, segmenter, token estimator, policy evaluation, cost model
```

- **[DECISION] TypeScript end to end.**
  - Why:
    - The op model, assembler and validator must behave identically in the UI preview and in the real send.
    - One language for a solo builder.
    - The Anthropic SDK is first-class in TypeScript.
  - *Alternative:* a Python core (better NLP ecosystem) with types generated for the UI.
  - If heavy NLP becomes necessary, add a Python sidecar behind the extractor interface rather than splitting the core.
- **[DECISION] A local web app, not a TUI or a desktop shell.** Rich interaction (maps, diffs, drag-select, virtualized documents) needs a browser. Desktop packaging can come later.
- **Suggested building blocks (non-binding):**
  - server: Fastify or Hono with ws, SQLite;
  - UI: React with Vite, TanStack Virtual, CodeMirror 6 (editing and merge view), a light chart library;
  - a graph view (for example xyflow), only as a secondary KR view.

## 4. Data model (Layer 1)

### 4.1 Entities

| Entity | Role |
|---|---|
| **Workspace** | A folder plus one SQLite DB; holds sessions. |
| **Session** | Model config, frozen preamble (system blocks and tool definitions as sent), edit regime, policies. |
| **Branch** | A head pointer into the event tree, with its own op log and epochs. |
| **Event** (immutable) | A raw entry: user message, assistant message as received, tool execution record (call, effective args, full raw output, exit status, timings), injection record (content snapshot and origin), gate decision, error. |
| **Call** (immutable) | Wire log: the exact request (stored as content-addressed block refs), the exact response, usage, cost, latency, model, betas, stop reason, transformations reported by the server. *What the model actually saw.* |
| **Epoch** | Branch, first call, base request hash, and the commit that opened it. |
| **Op / Op group** | Edits. Proposals and commits are groups (§4.3). |
| **KR delta / node / edge** | Event-sourced knowledge (§7), with snapshots materialized at each commit. |
| **Run** | An isolated execution outside the main line: A/B variant, probe, fork call, side call, replay, sandboxed agent run. Never appended to a branch unless promoted. |
| **Policy** | Rules for the gate engine (§6.4). |

### 4.2 Addressing  [TRICKY]

- An address is (event, block, [start, end)) over the block's immutable text. Because the text never changes, offsets stay valid forever.
- Offsets are counted in **Unicode code points**, so any future non-JS component computes the same spans. [FRAGILE: test with emoji and CJK.]
- **Segments** come from a versioned, deterministic segmenter: paragraphs, list items, code fences, headings, line chunks of tool output, JSON keys.
  - Segments are the unit of the UI and of LLM citations.
  - **Ops store spans, not segments**, so upgrading the segmenter never orphans an op.
- Opaque blocks can only be addressed whole: thinking, server-tool results with encrypted content, compaction blocks, unknown types.

### 4.3 Operations: the single contract

- **Verbs:** `drop(target)`, `replace(target, content)`, `pin(target, {hoist?})`, `insert(content, placement)`.
- **Meta-op:** `revoke(op | group)`.
- There is no `move`: it is a drop plus an insert with a `derived_from` link. The UI presents it as "move".
- **Targets** are span sets, or a KR node that is *converted to spans when the op is created*. Both are recorded, and the spans are authoritative. [TRICKY: node IDs can change on re-extraction; storing spans keeps replay stable.]
- **Fields:** id, group, verb, target, payload (content snapshot), author (`human` | `rule:<id>@<ver>` | `llm:<call>` | `assembler`), rationale, base (branch head and epoch), state `draft → staged → committed | revoked`.
- **Pin semantics [DECISION].** A pin never edits history by itself. This is how "emphasize" works. It has two parts:
  - *Protection*: no machine-authored op may drop or replace a pinned span, and budget eviction skips it.
  - An optional *hoist*: the item is repeated in the KR brief or in an appended pinned note.
- **Fold:** active ops are applied in log order. For each block, the fold computes intervals: keep, drop, replace or stub.
  - When ops overlap, the later one wins, and the UI flags the shadowed ones.
  - A manual op may override a pin after confirmation.
  - A machine op that conflicts with a pin is rejected as soon as it is proposed.
- **With epochs:** ops on pending content apply at the next call. Ops on sent content stay *staged* until a commit.

### 4.4 Branches and rewind

Events form a tree through parent pointers. Forking copies the active op set; copy-on-fork is simpler and more predictable than inherited logs. Rewinding means branching from an earlier event. That keeps all earlier thinking valid, and reuses the cache if a cache entry near that point is still alive.

### 4.5 Persistence  [DECISION]

- **Storage:** one SQLite file per workspace, with append-only tables and a content-addressed blob table.
  - Requests are stored as lists of block hashes, so the hundreds of near-identical prefixes in a long session cost almost nothing.
  - Raw tool output is stored in full up to a size cap. Beyond it: head, tail and a hash.
- **Portability:** sessions can be exported and imported as JSONL (portable and diffable).
- **API key:** taken from the environment, an `ant` profile or the OS keychain. It is never stored in the DB, logs or exports.

## 5. The assembler (compile pipeline)

**Inputs:** branch head, frozen preamble, epoch base (the previous request), active and staged ops, injections, model capabilities, edit regime.
**Outputs:** the request, a source map, and diagnostics.

1. **Base:** the last request of the epoch, as frozen bytes.
2. **Tail:** events since the last call become wire blocks, with ingestion ops applied (bounding, redaction, injections).
3. **Patch** (commits only): apply staged ops to regions of the base and copy everything else through unchanged.
4. **Lowering and repair:** deterministic rules, each one reported in the diagnostics.
   - Dropping or replacing a `tool_result` leaves a stub *inside* the result, so the tool_use/tool_result pair survives.
   - Dropping a `tool_use` removes it together with its result, and leaves a one-line note in the assistant text.
   - Dropping a whole turn merges its neighbors deterministically, or turns it into a stub.
   - Opaque blocks can only be kept or dropped whole.
   - Empty messages are removed, and the request must end on user content.
5. **Thinking validity [TRICKY]:**
   - For each thinking block, the wire log records the exact prefix it was produced on.
   - Find the earliest position where the new request differs from those prefixes.
   - Strip every thinking block after that position, and record the strip as an op.
6. **Validate.** A single pure function is the only place that encodes the API's structural rules: tool pairing and ordering, roles, placement of system messages, no prefill, contiguous thinking, frozen system/tools, intact opaque blocks. A request that fails never reaches a gate.
7. **Budget.** Compare the exact count against the context window and the user's budget. If over budget, refuse and propose cuts. Never evict silently.
8. **Cache plan.**
   - An explicit breakpoint on the frozen preamble, plus automatic caching for the growing tail.
   - An intermediate breakpoint if one request appends more than about 15 block positions, because the server looks back at most 20. [FRAGILE]
   - Thinking and effort settings are fixed per session, because changing them at the top level invalidates the messages cache.
9. **Source map.** Each region of the request maps back to its origin: an event span, an op, an injection or a repair. It powers the as-sent view, the context map, and "why is this here?".

**Determinism [FRAGILE]:**
- Nothing that feeds the prefix may contain timestamps, random IDs or unordered maps.
- Injections are linted for volatile content.
- The tool list is stored and replayed exactly as sent.

## 6. Control layer: loop, gates, policy, executor

### 6.1 Loop state machine

```
Idle ─▶ Composing ─▶ Assembling ─▶ PromptGate ─▶ Calling(stream) ─▶ Parsing
  ▲                       ▲                                           │
  │                       └── Ingesting ◀── Executing ◀── ToolGate ◀──┤ tool_use
  └───────────────────────────────────────────────────────────────────┤ end_turn
        max_tokens → offer "continue" · pause_turn → re-send as-is (no extra user msg)
        refusal → show category, offer fallback (reasoning won't transfer)
        context window exceeded → curation/commit required · errors → retry policy
```

- The state machine is persisted: after a crash or restart, it resumes at the last gate.
- **Commit window:** Idle or Composing, that is, at a user-turn boundary. At a tool gate, history edits stay staged unless the user forces an emergency commit.

### 6.2 Gates

- **Prompt gate.**
  - It shows:
    - the delta since the last call: new content, plus any commit being applied;
    - exact tokens;
    - a cost split: cache read, cache write, uncached, estimated output;
    - the cache state: warm or cold, with a TTL countdown;
    - the thinking blocks that will be stripped;
    - the validity report.
  - **Actions:** approve, edit (the pending part freely, history through staging), reject, branch.
  - **Approval is tied to the request hash.** Any change after approval re-opens the gate.
- **Tool gate.**
  - One card per call; parallel calls are batched. Each card shows an effect analysis:
    - for file edits, a diff;
    - for commands: executables, paths, network access, destructiveness, reversibility and *unknowns*.
  - After execution, it shows a preview of the result with ingestion curation: bound or trim it before it is sent.
  - **Per call:** approve, deny (returns an error result with the user's reason), modify, branch.
  - **[TRICKY] Modify:** the model's `tool_use` block stays byte-exact, which is mandatory. The edited command is what actually runs, and the result states "the user modified the command to …". The record stays honest and the replay stays valid.
- **Keep-alive during review.**
  - If a large warm prefix would expire while the user reviews, the curator re-sends the previous request with `max_tokens: 0`, which is billed only as a cache read.
  - On Opus 5.5 that costs about $0.06 for 300k cached tokens, against about $1.50 to rewrite them.
  - Keep-alives are controlled by policy.
- **[RISKY] Approval fatigue.** The v1 policy, "review everything", will get rubber-stamped unless gates are fast. That means: approval by keyboard, display limited to the delta, cards sorted by risk, and a one-keystroke "always allow this".

### 6.3 Turn handling details  [FRAGILE]

- Build up streams with the SDK's helpers. A hand-rolled parser that loses signature deltas breaks the replay of thinking blocks.
- Store the final message's wire JSON verbatim. A cancelled stream stays in the event log but is never sent back.
- For tool inputs:
  - parse a *copy* for execution and validate it against the schema;
  - never run tools from a turn that stopped on `max_tokens` or `refusal`.
- Request the "summarized" thinking display so reasoning is visible. The default, "omitted", returns empty text. The display setting never changes what is sent back.

### 6.4 Policy engine  [DECISION]

- **One engine for every action kind:** prompt send, tool call, machine curation proposal, injection, side or fork call, keep-alive, commit.
- **A rule** matches on kind, tool, argument patterns, path globs, token or cost thresholds and author. It returns `auto | review | deny` with an explanation.
- **The most restrictive result wins** (deny > review > auto), so an allow rule can never hide a deny.
- **The default is `review`.**
- **v1:** review everything, plus an allowlist: read-only tools inside the workspace, and command patterns the user defines.

### 6.5 Tools and executor

- **[DECISION] Tool set.** Typed tools make blast-radius analysis exact; bash is analyzed on a best-effort basis.
  - Anthropic's text-editor tool: typed view, create, replace and insert, which give exact diffs.
  - Anthropic's bash tool, for breadth.
  - A few custom read-only tools (glob, grep, list), marked safe to run in parallel.
- **[RISKY] Command analysis fails closed.** Commands go through a real shell parser. The following always go to review, never to auto:
  - anything unparseable;
  - compound commands: pipes, subshells, `eval`, `bash -c`;
  - anything that touches paths outside the workspace or accesses the network.
- **Executor interface:** `execute(call, ctx) → {output, exit, effects, timing}`, with capabilities declared per tool.
- **v1 runs locally**, confined to a workspace root: canonical path resolution, symlink checks, timeouts, full output capture.
  - **[RISKY]** Approved commands run on the real machine. Review-by-default is the only barrier until M6.
- **Later:** a rootless container with an overlay workspace, network off by default, and a diff/apply step for the results.

## 7. KR spine (Layer 2)

### 7.1 An ontology driven by use  [DECISION]

A node type exists only if it powers a navigation feature, a curation rule, the brief or a probe.

- **Structural tier (deterministic):** Thread, Turn, Step, Block, Segment, ToolCall/Result, Artifact (file, URL, command, symbol), Error, Attempt.
- **Semantic tier (LLM or human):** Goal (levels: objective → task → subtask), Decision (with rationale and rejected alternatives), Fact, Constraint, Question.
  - Notions (a glossary) are deferred.
  - Domains are tags, not nodes.
- **Status matters more than type:**
  - Goals: open, done or abandoned.
  - Decisions: active, superseded or reverted.
  - Facts: current, stale or contradicted.
  - Questions: open or answered.

  *Supersession is what makes pruning safe.*
- **Edges:**
  - `part_of`: the primary hierarchy;
  - `supersedes`, `answers`, `depends_on`;
  - `about`: points to an Artifact;
  - `cites`: points to spans.

### 7.2 Representation  [DECISION]

- **Shape:** a property graph with one primary hierarchy. Humans navigate an outline (goals → threads → items); the graph view is secondary.
- **Storage:** event-sourced.
  - Each delta (create, update, link, status) is appended with its author and extractor version.
  - A materialized view serves the reads.
- **Source:** the KR is extracted from the raw event log (plus injections), *not* from the curated view, and edit status is overlaid. Otherwise, pruning something would also erase it from the KR.

### 7.3 Extraction

1. **Mechanical** (every step, synchronous, free):
   - file lifecycle: read → edited → stale read;
   - re-runs of the same command, which supersede the older outputs;
   - errors and dead ends;
   - duplicates (exact hash and near-duplicates);
   - later references, which mean the content is still in use;
   - sizes;
   - secrets.
2. **Threads:** heuristics (artifact overlap, user cue phrases, goal shifts, time gaps), plus optional LLM labels.
3. **Semantic** (batched per user turn, async):
   - Side calls (§8.3) receive the new segments with their IDs and a compact current KR: open goals, active decisions and facts, with IDs.
   - They return a KR delta through structured outputs. Forced tool choice is rejected on current models.
   - Results are cached by input hash.
   - Re-extracting a thread is a user action.
4. **Human edits** are deltas authored by the user, and they are sticky: a machine may only *propose* changes to nodes a human asserted.

### 7.4 Provenance  [TRICKY]

LLMs produce unreliable character offsets. So:
- The extractor sees pre-segmented text and must cite **segment IDs**.
- For finer anchoring it may add a short quote, which is matched deterministically, with a fuzzy fallback.
- Every citation is verified.
- Claims that can't be verified are marked *unsupported* and never trigger automatic ops.

### 7.5 Round trip from KR to ops  [TRICKY]

Spans and nodes are many-to-many: one paragraph can support a superseded decision *and* a fact that is still current. Before a node-level action is applied, the curator computes its **collateral**: the other active nodes that would lose their supporting text. If there is any collateral, it proposes a `replace` instead of a `drop`. The replacement is either a rewrite that keeps the surviving content or a stub rendered from the KR.

### 7.6 Stability and concurrency  [FRAGILE]

- **Re-extraction can renumber nodes** (after a new model or prompt). Mitigations:
  - append-only deltas instead of regeneration;
  - ops that store spans rather than node IDs;
  - re-extraction presented as a diff to review.
- **Async jobs can finish after the session has moved on.**
  - Deltas carry the transcript position they were computed at, and applying them is idempotent.
  - A late delta is rebased if its inputs are unchanged, otherwise discarded.

### 7.7 The KR brief

- A deterministic template renders a compact brief with node IDs, covering:
  - active goals, decisions and constraints;
  - key facts and open questions;
  - hoisted pins.
- **Delivery:** a *turn-scoped* system message each turn, rendered for that turn only, free afterwards, and append-only (beta).
- Without that beta, the brief is injected only at commits, because copies would otherwise pile up in the history.
- The brief is what lets a commit drop large parts of the history safely.

## 8. Curation and analysis (Layer 3)

### 8.1 Position on the core tension

- **Deterministic rules** are always on and may run automatically under policy.
- **LLM outputs are always proposals**, with provenance (call, model, prompt version) and the cost shown up front.
- **Accepted outputs become fixed op payloads.** Nondeterminism stays confined to generating proposals, and the log stays replayable.
- **Money is no longer the main objection.** At current Haiku prices, LLM extraction over a 200k-token session costs a few cents. What remains is predictability, latency and trust, and the design targets those.

### 8.2 Proposals and rules

- **A proposal** is an op group with a rationale, an author and an impact estimate: tokens per call, commit cost, thinking stripped, break-even, collateral KR nodes. Proposals appear in *Suggested moves*; accepting one moves it to *Staging*.
- **Rule catalog v1** (deterministic):
  - bound oversized tool outputs **at ingestion**: head, tail and a stub; the full raw output is kept; free;
  - stub stale file reads;
  - stub the older outputs of a command that was re-run;
  - keep only the latest copy of duplicates;
  - collapse dead ends (error → retry → success) into a one-line note;
  - redact secrets: high priority, ideally at ingestion;
  - trim the oldest thinking at a commit;
  - under budget pressure, evict by priority score, never pinned items.
- **Stub convention:** `[curator: what was here · why removed · how to recover]`. It is explained in the frozen preamble, so the model trusts stubs and knows it may re-fetch.

### 8.3 LLM-assisted curation: two kinds of calls  [DECISION]

- **Side calls** run on Haiku 5.5 with their own prompt.
  - Used for: extraction, thread labels, relevance scores.
  - Cheap and parallel, but they share no cache with the session.
- **Fork calls** use the same model and a byte-identical prefix, with an instruction appended.
  - Used for: summaries and briefs of the current session.
  - They reuse the session's cache (cheap reads), and in a fork the model can read its own earlier reasoning, which gives better summaries.
  - They pay the main model's output prices.

### 8.4 Economics model  [TRICKY]

- **For a staged commit:**
  - rewrite cost = tokens after the first changed position × write price;
  - savings per call = removed tokens × (read price if the cache is warm, input price if it is cold);
  - plus the penalty for stripped thinking and the latency of a cold prefill.
- **Worked example:** Opus 5.5, 300k-token context, prune 100k near the top.
  - *Cache warm:* the next call costs about $1.00 to rewrite, against $0.06 if left untouched. Savings are $0.02 per call, so break-even comes after about 47 calls.
  - *Cache already cold* (user away for more than 5 minutes): the rewrite happens anyway, so the commit **saves** about $0.50 immediately.
- **Hence** the TTL indicator on the dashboard, and the **"commit when cold"** action.

### 8.5 Metrics

- **Per call:** uncached input, cache read, cache write (by TTL), output (including thinking), time to first token, latency, cost, stop reason, server transformations.
- **Per session:** totals, plus the curator's own overhead on a separate line.
- **Composition by kind:** preamble, user, assistant text, thinking, tool use, tool result, injections.
- **Per item:** tokens, age, staleness, duplication, later references, KR coverage.
- **Health:** cache-hit ratio, share of thinking preserved, number of commits, prune→re-fetch events.
- **[DECISION]** Repetition and staleness first: they are deterministic and actionable. "Density" and "vagueness" come later: they are weak signals and easy to over-invest in.

### 8.6 Evaluating curation  [RISKY]

Users can't tell whether a prune hurt. Two instruments help.

- **A/B sub-calls.**
  - The same next prompt runs against curated vs. uncurated context (or other variants), side by side, with a diff and metrics.
  - An optional LLM judge is itself a costed and noisy run, so show where judges disagree rather than a single score.
- **Retention probes.**
  - Questions are generated from KR facts and decisions.
  - Before committing, fork calls ask them against the *proposed* curated context, and the answers are graded.
  - A failed probe shows what the commit would lose. (Bonus: a probe on the proposed context also pre-warms the cache for the commit.)

### 8.7 Failure modes on the model side  [TRICKY]

- **Prune→re-fetch loops:** the model re-reads what was stubbed. Detect it, show it, and keep stubs explicit about what can be recovered.
- **Summary poisoning:** a wrong summary becomes ground truth for the model. Summaries are marked, carry provenance and can be reviewed.
- **Dangling references** ("as shown above"): stubs keep anchors in place.

## 9. Interaction (Layer 4)

The guiding pattern is: overview first, then zoom and filter, then details on demand.

### 9.1 Layout

- **Left:** the Navigator, with tabs for Outline (threads → turns → blocks), KR and Search.
  - Each thread and turn shows a one-line gist.
  - For tool steps the gist is deterministic (for example "ran tests → 3 failures"); for prose it comes from a side call.
- **Center:** the Document view, with the context map along its edge.
- **Right:** the Inspector: current selection, provenance, KR cards, proposals.
- **Bottom dock:** Gate and Staging.
- **Workbench:** a separate view for dashboards, runs and comparisons.

### 9.2 The context map: the main tool for getting the big picture

- A vertical strip representing the whole request as sent. Height is proportional to tokens; color shows the kind of content.
- **Overlays:**
  - the cached region (from the last usage report);
  - the frontier line;
  - staged edits (hatched);
  - pins;
  - stale and duplicate flags;
  - thread bands;
  - the edit-cost gradient.
- **Interaction:** click to jump, drag to select.
- **Modes:** raw, as-sent, staged preview.

### 9.3 Document view

- The conversation reads as a document.
  - Each segment has a gutter showing tokens, a status color and KR badges.
  - Tool outputs are collapsed to their head and tail.
- **Diff modes:** raw vs. as-sent, current vs. staged, call *n* vs. call *n+1*.
- Selecting a KR node highlights its source spans.

### 9.4 Interaction model

- **Keyboard-first:** move, drop, pin, replace, summarize, revoke, expand, branch, approve, plus a command palette.
- **Selection queries** for bulk work. For example, `kind:tool_result tokens>2000 age>10 stale -pinned` selects every match, which can then be stubbed in one action. With thousands of segments, bulk operations *are* the ergonomics.
- **Staging panel (git-like):**
  - staged groups;
  - totals: tokens per call, commit cost, thinking stripped, break-even;
  - actions: commit, discard, commit when cold.
- **Live feedback:**
  - Totals update on every staged change.
  - Every number is marked *exact* or *~estimated*.
  - Estimates are calibrated against reported usage; exact counts are computed at the gate.

### 9.5 Performance  [RISKY]

Sessions of 200k to 1M tokens mean megabytes of text and thousands of segments. Required from day one:
- virtualized rendering and lazy markdown;
- collapsed tool outputs;
- heavy work (segmentation, diffs, estimates) in a worker;
- incremental pushes from the server.

## 10. Extensions (D)

### 10.1 Injection channels, from most to least stable

| Channel | Use | Effect on cache and thinking |
|---|---|---|
| Frozen preamble | persona, skills index, stable docs | cached; free after the first write |
| Appended system message | operator info during the session, pinned notes, tool changes | append-only; cached afterwards |
| Turn-scoped system message (beta) | per-turn KR brief, status, reminders | rendered for one turn, then free; append-only |
| Retroactive insert | content placed at an earlier position | requires a commit (full cost) |

- **Every injection** is stored as a content snapshot, an origin and a hash, so replay is deterministic. It is rendered with a visible source tag.
- **Sources:** skills and library files, fetched URLs, persona, the KR brief, harness results. RAG comes later.
- **Placement rules depend on the model.** Some models treat a system message placed right after a tool result as untrusted, so these rules live in a capability registry.

### 10.2 Harness and sandbox

- Sub-calls (A/B runs, probes, test calls) and agentic runs feed their results back as injections or tool results.
- **[DECISION] Keep isolation and containment separate.**
  - **Isolation** is for comparisons: a git worktree or a temporary copy. It is cheap and comes in M5.
  - **Containment** is for security: a container, no network, resource limits. It comes in M6.
- Agentic A/B runs are impossible without isolation, because the variants would write to the same files.

### 10.3 Multi-agent

This comes later. The data model already allows child sessions whose final output returns to the parent as a tool result, which is append-only. Parallel children that share a prefix should be started a little apart, because a cache entry becomes readable only once the first response starts streaming.

### 10.4 Other providers

Keep the provider port thin, store raw provider payloads, and don't abstract early. The epoch/commit model carries over: any API with prefix caching, or with opaque reasoning state tied to the prefix, needs it.

## 11. Cross-cutting concerns

- **Security [RISKY].**
  - The server binds to 127.0.0.1 and requires a per-launch token, with Host and Origin checks. It can run commands, and DNS rebinding or CSRF from a browser tab is the realistic attack.
  - File access is confined to the workspace.
  - Secrets in the context are detected.
  - The API key is never written to disk.
- **Cost controls:**
  - session and daily budgets;
  - a per-call cap;
  - a cap on the curator's own overhead;
  - hard stops at the gate.
- **Testing:**
  - golden assembler tests: events plus ops must produce exact request bytes;
  - property-based tests: random op sequences must always pass the validator, and unchanged blocks must stay byte-identical;
  - live contract tests: mismatch mode set to "error", and a second identical request must read the cache;
  - recorded fixtures for loop tests;
  - a small labeled set of sessions for evaluating KR extraction.
- **API drift [FRAGILE].** Beta names and semantics change, and new block types appear. Mitigations:
  - a per-model capability registry, refreshed from the Models API where possible;
  - opaque pass-through of unknown blocks;
  - contract tests in CI.

## 12. Milestones

### M0 — Look
- **Scope:**
  - data model and a wire-faithful store;
  - import of API logs, plus your Claude Code session logs as a development corpus (their format is internal and unstable, which is acceptable here);
  - a viewer with the context map, outline and document view;
  - exact and estimated token counts.
- **Exit criterion:** in a real 300k-token session, find "where the tokens went" in under a minute.

### M1 — Talk
- **Scope:**
  - a live loop with streaming and a frozen preamble;
  - minimal tools;
  - prompt and tool gates (review everything, plus an allowlist);
  - a local executor;
  - append-only epochs and ingestion curation;
  - cost and cache metrics, a TTL indicator, keep-alive;
  - a per-call prefix verifier.
- **Exit criterion:** a 50-step coding session, verified 100% append-only, with cache reads on every call after the first.

### M2 — Edit
- **Scope:**
  - ops, staging and commits (patch-linker, repair, thinking strip, validator);
  - an economics preview;
  - branch and rewind;
  - revoke semantics;
  - the two edit regimes.
- **Exit criterion:** property tests pass, and 20 random commits on a live session produce no 400s and no transformations the assembler did not predict.

### M3 — Structure
- **Scope:**
  - the mechanical KR tier and threads;
  - rule proposals with economics;
  - selection queries and bulk ops.
- **Exit criterion:** on real sessions, the rules find most prunable tokens without ever flagging pinned or still-referenced items.

### M4 — Understand
- **Scope:**
  - the semantic KR tier (side calls) and the KR navigator;
  - provenance highlighting;
  - KR-to-ops with collateral checks;
  - fork-call summaries;
  - the KR brief.
- **Exit criterion:** at least 90% of semantic nodes carry verified citations, and a commit based on the brief passes the retention probes.

### M5 — Experiment
- **Scope:**
  - the workbench: runs, A/B runs started apart to share the cache, probes, dashboards;
  - server strategies as A/B variants;
  - worktree isolation.
- **Exit criterion:** a curated vs. uncurated A/B run with probes, readable on one screen.

### M6 — Contain and extend
- **Scope:**
  - a container sandbox;
  - injection sources;
  - MCP tools;
  - multi-agent sub-sessions.
- **Exit criterion:** an agentic run in a sandbox, with its diff reviewed and applied.

## 13. Risk register (ranked)

1. **[RISKY] An append-only API vs. a product built on editing history.**
   - Mitigations: epochs and commits, the patch-linker, the validator, CI in "error" mode, the two edit regimes, honest economics.
   - *Residual:* heavy curation now costs reasoning continuity, and that is inherent.
2. **[FRAGILE] Wire fidelity.** Mitigations: verbatim storage and replay, SDK stream helpers, a prefix diff on every call.
3. **[RISKY] Negative economics on warm caches.** Mitigations: visible break-even, "commit when cold", and value framed as focus and quality.
4. **[RISKY] UI ergonomics and performance at scale** (the main feature). Mitigations: M0 on real data, the context map, selection queries, virtualization.
5. **[TRICKY] KR provenance and extraction drift.** Mitigations: segment-ID citations, verification, append-only deltas, sticky human edits.
6. **[TRICKY] Collateral when KR actions become ops.** Mitigations: collateral analysis, and replace-with-preserve instead of drop.
7. **[TRICKY] Model behavior after edits** (re-fetch loops, summary poisoning, dangling references). Mitigations: the stub convention, metrics, probes.
8. **[RISKY] Security of the executor and the local server.** Mitigations: fail-closed analysis, workspace confinement, token and origin checks.
9. **Approval fatigue.** Mitigations: delta-only gates, keyboard flow, quick allowlists.
10. **[FRAGILE] API drift.** Mitigations: the capability registry, opaque pass-through, contract tests.
11. **Scope creep** across four layers plus extensions. Mitigations: vertical milestones, with M0 and M1 kept strictly small.
12. **Noisy quality evaluation.** Mitigations: A/B runs plus probes, and uncertainty shown rather than a single score.
13. **[TRICKY] Async races** between extraction, the loop and edits. Mitigations: idempotent deltas stamped with their position, and approval tied to the request hash.

## 14. Where this departs from or sharpens `overall_intent.md`

1. **Epochs, commits and the frontier.** The intent assumes the prompt can be freely re-assembled on every step; the API no longer allows that without a cost.
2. **A third source of truth, the wire log**, because byte-exact replay is mandatory.
3. **The KR is extracted from the raw event log**, with edits overlaid as status. The intent derives it from the transcript plus the edit log.
4. **Ops gain `revoke` and groups.** Pin is defined as protection plus an optional hoist. Move is a drop plus an insert.
5. **Gate edits are free below the frontier and staged above it.** Approval is tied to the request hash.
6. **A single policy engine for all gates**, including machine curation, injections, keep-alives and commits.
7. **The curator's own LLM calls are split** into side calls (cheap model) and fork calls (same model, shared cache).
8. **Server-side context editing and compaction are addressed explicitly:** off by default, available as strategies.
9. **The economics are reframed.** Pruning a warm cache rarely saves money; the value is focus, quality and fitting the context window.
10. **Metrics put staleness and repetition** ahead of density and vagueness.

## 15. Assumptions and open questions

- **Assumed:**
  - The main use is agentic and coding sessions, where tool output dominates the context. A chat-heavy use would put more weight on the semantic KR.
  - Single user, running locally with their own API key; no collaboration features.
  - Default models: the main session on Opus 5.5 with an explicit effort setting (thinking can't be disabled on that model); side calls on Haiku 5.5. Fable 5.1 is optional.
- **Open:**
  - Which betas are acceptable dependencies? Turn-scoped system messages, tool changes, thinking-binding controls and on-demand compaction are beta; mid-conversation system messages are GA.
  - Should commits ever be automatic, for example "auto when the cache is cold, deterministic rules only"? v1 only proposes.
  - How far should the semantic KR go before the mechanical tier proves insufficient?

## Appendix A — API facts relied upon (verified 2026-10-16)

### Models and prices

Prices are $ per million tokens (input / output):

| Model | Input / output | Cache read |
|---|---|---|
| Opus 5.5 | $4 / $20 | $0.20 (0.05×) |
| Sonnet 5.5 | $2 / $10 | $0.20 |
| Haiku 5.5 | $0.10 / $0.50 for prompts ≤ 100k tokens ($0.50 / $2.50 beyond) | — |
| Fable 5.1 | $10 / $50 | $0.25 |

- All four have a 1M-token context and 128k output.
- Cache writes cost 1.25× (5-minute TTL) or 2× (1-hour TTL).

### Caching

- At most 4 breakpoints. The minimum cacheable prefix is 512 tokens on current models.
- The TTL counts from the start of the request and is refreshed by reads.
- Lookback is at most 20 block positions; a run of tool_use or tool_result blocks counts as one. Top-level automatic caching is available.
- A cache entry is readable only after the first response starts streaming. Caches are scoped to a model.
- A `max_tokens: 0` re-send works as a cheap keep-alive or pre-warm. It is not allowed with streaming, structured outputs or batches.
- Cache diagnostics beta: `cache-diagnosis-2026-04-07`.

### Preserved thinking

- Applies to Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5. Enforced for accounts created on or after 2026-08-31; opt-in otherwise.
- Controls beta: `thinking-binding-controls-2026-08-01`.
  - It sets `thinking.block_binding.prefix_mismatch_behavior: "error" | "drop_block"`.
  - Responses then report `input_transformations`.
- Without the beta, the recovery is to strip all thinking and retry.
- Anthropic's measured cost of `drop_block`: +2.5–20% output tokens when it happens once per session, +4.6–67% when it happens every turn, depending on effort level.
- `count_tokens` runs the same check.
- Tool definitions are compared in full; reordering tools is allowed.

### Append-only forms

- Mid-conversation `role:"system"` messages: GA on Opus 5.5, Fable 5.1, Sonnet 5.5 and Haiku 5.5; not available on Sonnet 5.
- Turn-scoped `clear_at: "next_user_message"`: beta `mid-conversation-system-clear-at-2026-08-21`.
- Tool changes via `tool_addition` / `tool_removal`: beta `mid-conversation-tool-changes-2026-07-01`, or by value under `inline-tools-2026-09-15`.
- Per-message effort: beta `mid-conversation-output-config-2026-07-01`.

### Server-side features

- Context editing: `context-management-2025-06-27`, with strategies `clear_tool_uses_20250919` and `clear_thinking_20251015`.
- Compaction: `compact-2026-01-12`; on-demand compaction: `compact-2026-09-04`.

### Request shape

- No assistant prefill on current models.
- Forced `tool_choice` (any or tool) is rejected on Opus 5.5, Sonnet 5.5 and Fable 5.1. Use structured outputs or `strict: true` tools instead.
- All results for one assistant turn go in one user message, matched by id.
- The thinking display defaults to "omitted"; set "summarized" to see reasoning.
- Thinking can't be disabled on Opus 5.5. Effort is the control, and it defaults to medium.

### Stop reasons to handle

- `end_turn`, `tool_use`, `max_tokens`, `stop_sequence`, `pause_turn`.
- `refusal`: check it before reading the content.
- `model_context_window_exceeded`.
- `compaction`, returned by on-demand compaction requests.

### Token counting

- `POST /v1/messages/count_tokens` gives exact counts and is specific to each model.
- Never use tiktoken-family tokenizers: they undercount Claude tokens by 15–20% or more.
