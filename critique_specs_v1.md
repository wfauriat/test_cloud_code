# Critique: specs_claude.md vs plan_v1.md

Date: 2026-10-16. A critic pass comparing the human-led plan (`plan_v1.md`) with the independent LLM proposal (`specs_claude.md`). The goal is to help filter the proposal into design choices for a v2 plan. Nothing here is locked in.

**Bottom line.** The spec's biggest correction is real; its API claims were checked against the docs. Changing anything already sent now costs both cache and reasoning, so history edits have to be batched into commits. Without seeing them, the spec also re-derived nearly all of plan_v1's "Decide early" and risk items, which supports those choices. Its strength is following one external constraint through every layer. Its weaknesses: it turns every concern into a mechanism, and it lacks context only the human side had.

## Method
The spec was generated from `overall_intent.md` alone (748 words, roughly the first half of plan_v1). It never saw plan_v1's KR strategy, Decide early, Defer, Risks and High-profile questions sections, nor `session.md` or `benchmark.md`. That makes those parts an answer key:
- What the spec found on its own is robust.
- What it missed is context only the human side had.
- What it added is either an insight or over-reach.

It turned 748 words into 7,815, with 47 risk/decision markers.

## 1. API facts: checked
Appendix A was checked against the Claude API reference bundled with the claude-api skill (dated 2026-10-06) and two docs pages (sources at the end).
- **Confirmed (everything the design rests on):**
  - Preserved thinking on Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5. A thinking block stays valid only if the system prompt, tools and every earlier message are unchanged.
  - A 400 error for accounts created on or after 2026-08-31.
  - `drop_block` mode and the `input_transformations` report; `count_tokens` runs the same check.
  - The append-only forms: mid-conversation system messages are GA; `clear_at`, tool changes and per-message effort are in beta.
  - Server-side context editing and compaction don't count as edits.
  - Prices, cache multipliers, the 512-token minimum, the 20-block lookback, the `max_tokens: 0` keep-alive, no prefill, forced `tool_choice` rejected.
  - The worked cost examples recompute exactly: break-even after 47 calls, $0.50 saved by committing on a cold cache, $0.06 vs $1.50 for a keep-alive.
- **Not found:** the "+2.5–20% / +4.6–67% extra output tokens" cost of dropped thinking (also used in C6), and the claim that some models treat a system message after a tool result as untrusted (§10.1). Treat both as unverified.
- **Missed by the spec:**
  - `clear_at` is a *limited* beta on Opus 5.5, and the per-turn KR brief (§7.7) depends on it.
  - On Opus 5.5, the model's narration between tool calls comes back as signed `thinking` blocks.

## 2. What it re-derived without seeing the plan
| Withheld (plan_v1 / benchmark) | Spec, independently |
|---|---|
| History as a tree of steps | Event tree with parent pointers; branches copy their ops when forked |
| Append-only step records | Event, wire and op logs in append-only tables |
| One gate with a policy hook | A prompt gate and a tool gate, one policy engine |
| Executor behind a narrow interface | `execute(call, ctx)`: local first, sandbox later |
| Extraction cost: make it incremental or lazy | Mechanical tier runs every step, free; semantic tier is async, batched and cached |
| Approval fatigue | Gates show only the delta, keyboard-driven, cards sorted by risk |
| A baseline before evaluating | A/B runs plus retention probes |
| v1 scoped to coding sessions | Same assumption |
| Elide; invalidate rather than delete | A stub *inside* the tool_result; supersession status plus `revoke` |
| Rewriting tool input at the gate (Claude Code hooks) | "Modify": the model's tool_use stays byte-exact; the edited command runs and is disclosed in the result |

plan_v1's "Decide early" list holds up.

## 3. The main lesson: the context is now append-only
`session.md` (item 6) and plan_v1 already knew that signed thinking blocks can't be edited, and that edits invalidate the cache. The missing piece: editing *anything earlier* also voids every later thinking block. That means a 400 error on new accounts, or dropped blocks under `drop_block`. The spine survives, but its timing changes. Views and proposals still run on every step, while writes to the wire are batched into commits. That is where the spec's epochs, frontier and staging come from.

The intent's four verbs, on the model side:
| Verb | Cost now |
|---|---|
| See | Free |
| Emphasize | Only by appending: a pin protects the item and can repeat it in the brief or a note |
| Prune | Free before the content is first sent; otherwise a commit (cache rewrite plus lost reasoning) |
| Organize | Free in the human's view; reordering what the model sees needs a commit (the spec has no `move`) |

The spec states the premises but not these conclusions:
- **The value moves.** Pruning a warm cache rarely saves money, since Opus 5.5 reads cached tokens at 0.05×. With 1M-token windows, running out of room is less often the binding constraint. What remains is focus and quality, the hardest benefit to measure. So evaluation has to come early: plan_v1 says so (`plan_v1.md:89`), but the spec schedules it at M5.
- **The API favors curation the user can't see.** Removing old tool results keeps reasoning valid when the server does it (context editing, compaction), and voids it when the client does. The benchmark's "stay client-side" principle now has a price, and it falls on the core feature. Open question: how many of the deterministic pruning rules could be expressed as server-side context-editing settings?
- **Complexity vs. value.** The most intricate subsystem serves the least certain value. That subsystem is the M2 patch-linker with its repair rules, thinking strip and validator; the value it serves is history editing. The solid value is in Look, the gates, curating before content is sent, and steering by appending.

## 4. Where the delicate parts are
The round trip has two hard halves. plan_v1 spotlights KR-to-ops. The spec shows that ops-to-wire (the assembler) is just as hard, has to be built first, and fails silently.

| Component | Delicate part | How it fails |
|---|---|---|
| Wire store and stream parsing | History is replayed from the stored bytes, never re-serialized; signatures in streams must not be lost | Silently: cache misses, dropped reasoning, or a 400 |
| Assembler | Repair rules (stub inside a tool_result; drop a tool_use together with its result); thinking strips recorded as ops; one validator; nothing volatile in the prefix | Loudly (400) if the validator is wrong; silently if a repair is wrong |
| Loop and gates | Commits only at user-turn boundaries; approval tied to the request hash; the cache can expire while the user reviews | Reasoning lost mid-tool-round; approving a stale request; rubber-stamping |
| KR | Citations by segment ID, then verified; one span can support several nodes, so drops need a collateral check; re-extraction renumbers nodes, so ops store spans; async results can arrive late | Silently: a drop removes text that a still-current fact relied on |
| Curation and costs | Warm vs. cold cache arithmetic; the cost of stripped thinking; the model re-fetching what was pruned, wrong summaries taken as truth, dangling references | Silently: "savings" that cost more; quality loss nobody notices |
| UI | 200k–1M tokens; internal terms leaking to users (epoch, frontier, stub, hoist, break-even, TTL) | Loudly for performance, silently for cognitive load |

Most of these fail silently. That's why the spec adds continuous self-checks: a prefix diff on every call, the server's `input_transformations` report, cache-read checks, and CI with mismatches set to error. In effect that's a cross-cutting layer plan_v1 doesn't have yet.

## 5. Gaps the human context fills
1. **Branching doesn't rewind the world** (`plan_v1.md:96`, benchmark). The spec sees this for A/B runs (§10.2). But it ships branch/rewind in M2 with isolation only in M5, and its rewind analysis (§4.4) covers API validity only.
2. **The brief can raise untrusted text to system authority (new).** The brief is sent as a `role:"system"` message, the operator channel the docs describe as non-spoofable. If LLM extraction lifts text from tool output or fetched pages into the brief, untrusted content gets system authority. It needs a rule: only human-asserted or attributed content in that channel, or deliver the brief in the user role.
3. **More of the context is opaque.** On Opus 5.5, between-tool narration lives in thinking blocks, so it can't be edited or pruned piece by piece. Reasoning is only ever visible as a summary. "What you see is what is sent" can only mean "every byte is accounted for", not "everything is visible".
4. **Positioning is absent.** Even so, the spec's emphases match benchmark.md's differentiators: live gates that show blast radius, and a cache-aware workbench. Showing what an edit costs in cache and reasoning may be a new differentiator.
5. **Persistence format.** Replay must be byte-exact, so trace formats (OTel GenAI, Langfuse) fit as export targets, not as the store. That half-answers `plan_v1.md:98`.
6. **Standalone vs. companion, reshaped.** Committing edits requires owning the wire, which means standalone. A companion running on Claude Code hooks fits exactly the append-only half: observe, gate, inject. The spec's M0 (a read-only viewer over imported Claude Code logs) works for either path.

## 6. Where it overreaches against plan_v1's own principles
- **Variants before a second one exists.** Two edit regimes plus server strategies as A/B variants, from day one, conflict with `plan_v1.md:90`. The "free-edit" regime also strips thinking on every call, which the docs describe as a one-time recovery, not a normal mode.
- **A rich policy language.** Rules on argument patterns, path globs, thresholds and author, across 7 action kinds (§6.4), are what `plan_v1.md:80` defers. Keep the shape: one evaluation point, the most restrictive answer wins, review by default.
- **More than one ontology and one extraction process.** The spec has a two-tier KR and four extraction modes, against `plan_v1.md:71`. It also reframes the KR without saying so in §14. The v1 KR becomes transcript structure (threads, steps, artifacts), while the knowledge ontology slips to M4. That ontology (goals, decisions, facts) is what benchmark.md names as the differentiator.
- **The stack is locked** (TypeScript end to end, local web app, SQLite). Keep the constraint behind it: the same assembler and validator code for the preview and the real send. Choose the stack later; reusing ThoughtDAG depends on that choice.

## 7. A filter for the human pass
For each spec element, in order:
1. **Forced by a verified external constraint?** Adopt it: epochs and frontier, the wire log, a single validator, append-only injection channels, a system prompt and tool list frozen at session start.
2. **Follows from a principle plan_v1 already holds?** Adopt it: ops on spans with a lifecycle, pin as protect plus repeat, KR extracted from the raw log with edits shown as status, LLM outputs frozen once accepted, curating before content is sent.
3. **A plausible mechanism for a real risk?** Record the risk and defer the mechanism: probes, collateral analysis, keep-alives, edit regimes, the capability registry.
4. **A preference?** Park it: stack, layout, libraries.

Decisions for the human pass:
- Is history editing a v1 pillar? Or is v1 "see, gate, curate before sending, steer by appending", with commits later?
- Does the evaluation baseline move ahead of Edit?
- KR v1: structure first, or the knowledge ontology first because it's the differentiator?
- Which betas are acceptable dependencies, `clear_at` above all?
- Which channel carries the brief, and with what authority?

---

## Sources
- Claude API reference bundled with the claude-api skill (cached 2026-10-06):
  - `shared/model-migration.md`: "Migrating to Claude Fable 5.1 from Claude Fable 5" (breaking changes 2 and 3, new API features) and "Migrating to Claude Opus 5.5" (breaking change 3);
  - `shared/prompt-caching.md`.
- https://platform.claude.com/docs/en/build-with-claude/extended-thinking
- https://platform.claude.com/docs/en/build-with-claude/thinking-tool-workflows
