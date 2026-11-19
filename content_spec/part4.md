# Content Spec — Part IV: L'automatisation et ses angles morts (ch. 14–16)

Read `00_global.md` first.

**Part page:** what automation does to checks. It **chains** them (ch. 14), **removes** them (ch. 15) and **correlates** them (ch. 16). Each chapter reuses a Part II model rather than introducing new formalism.

---

## Chapter 14 — Des chaînes qui agissent (~12–15 pages)

**Argument step:** S14 (chaining). **Keys in:** ch. 8 (P5, laundering), ch. 11–12. **Source threads:** `divide-and-orchestrate` (AI side), `agentic-compounding`, `uncertainty-laundering` (AI side).

**Sections:**
1. **AI pipelines as orchestrated chains.** Retrieve → summarize → plan → execute code. The higher the goal ("refactor this repository", "resolve the customer's dispute"), the less formally it can be stated, while intermediate results move ever faster.
2. **Agents.**
   - A language model pursuing a goal in a loop: plan, call a tool, read the result, take the next step.
   - Structurally, an N-step trajectory is an N-link chain.
   - Operationally, the system moves from *answers*, which wait for a reader, to *actions*, which change state, call services and commit code at once.
   - A wrong answer costs the time to read it; a wrong action executes.
3. **Laundering in AI pipelines.** Results passed between steps as bare strings, stripped of assumptions, provenance and uncertainty (the ch. 8 definition applied).
4. **Authority and guarantees.** Giving the least-guaranteed layer the most authority to act inverts the pattern that made the stack safe (forward link to sandboxes and gates, ch. 17).

**Blocks:**
- *Étude de cas* (dated): Knight Capital (2012). A deployment error left dormant order-routing code live; in about 45 minutes, millions of unintended orders and a loss of over $460 million (SEC, 2013). No language model was involved; the pattern is automated action outrunning oversight.
- *Exemple quantitatif* **chain-b**:
  - **mise en place:** an agent trajectory of N steps, up to 12, with p = 6 % and a shared factor q = 3 % (e.g., a misread instruction carried through every step);
  - **figure:** the chain-a curves extended to N = 12;
  - **calcul:** the N = 12 rows of global §7;
  - **lecture:** without checks, more than half of 12-step trajectories fail. Per-step cross-checks cut this to about 7 %, but the shared factor still accounts for about 42 % of residual failures, and checks of the same kind cannot touch it.
- *Question*: where in your architecture does output leave a learned component and enter a system that executes, bills, commits or publishes?

**Keys out:** agent as chain; answers vs actions; authority–guarantee inversion.

**Points clés (intended):**
- An agent is a chain whose errors execute.
- Laundering between steps turns pipelines into chains.
- The least-guaranteed layer should not hold the most authority.

---

## Chapter 15 — L'érosion des vérifications humaines (~15–18 pages)

**Argument step:** S14 (removal). **Keys in:** ch. 6, 9, 11. **Source threads:** `friction-as-generator`, `loss-of-the-tell`, `signaling-collapse`, `bainbridge-prompt-trap`.

**Sections:**
1. **Friction generated comparators.**
   - Slow work made the analyst form expectations and partial results, each able to contradict the next: the analyst's own checks.
   - Nobody drew that loop on a process chart, so its loss goes unnoticed until an absurd number slips through.
   - The ridge walked vs the summit reached by helicopter in fog.
2. **The lost tell.**
   - A guessing colleague hesitates and hedges, and that **signe révélateur** prompts scrutiny.
   - Model answers come in the same voice right or wrong.
   - Fluency distorts self-assessment: the METR sign error (dated `.cas`).
   - *Measure, don't testify.*
3. **Polish no longer signals substance.**
   - Form and substance shared a cause, understanding, so form could fail differently from a careless claim.
   - Fluent text and running code no longer require understanding.
   - In economic terms, polish was a costly signal (Spence). When it becomes free while checking stays expensive, checked and unchecked work pool together, and cheap unchecked output can drive out expensive checked work (Akerlof).
4. **Bainbridge's irony and the two prompt traps.**
   - Automating the routine part leaves the operator responsible for the rare failures, which need exactly the unexercised skills.
   - Reading the model's draft is one representation read twice.
   - **Trap 1:** the prompt transmits the frame, so the more it specifies a solution, the less the answer can contradict it.
   - **Trap 2:** training toward approval leads to complaisance (*complaisance* as the French term for sycophancy, glossed).
   - A person and a model form a cross-check only if the person forms an independent view first.

**Blocks:**
- *Boîte à outils*: costly signalling and pooling (Spence; Akerlof's lemons).
- *Étude de cas* (dated): METR (Becker et al., 2025): about 19 % slower measured, about 20 % faster estimated. The figure is tied to particular tools at a particular moment; the durable finding is the sign error.
- *Nuance*: the standard way out of pooling is credible disclosure (every result states its status, what was independently checked), effective only if audited by a track record and seeded errors (forward link to ch. 18). An unaudited label is cheap talk.
- *Question*: when you use a model to check your work, do you hand it the problem, or your solution with a request to look it over?

**Keys out:** the tell; costly signal; pooling; the irony of automation; the two prompt traps.

**Points clés (intended):**
- Slow work produced checks as a by-product.
- Fluency removed the visible sign of doubt.
- Polish stopped failing differently from substance.
- A human–model pair is a cross-check only if the human thinks first.

---

## Chapter 16 — Angles morts collectifs (~15–18 pages)

**Argument step:** S14 (correlation). **Keys in:** ch. 8–9, 15. **Source threads:** `rate-vs-escape-shift`, `same-lender`, `provenance-laundering`, `throughput-hollowing`.

**Sections:**
1. **Error rate falls, escape probability rises.**
   - Each analyst has idiosyncratic blind spots; all consult one model.
   - Against each analyst's own blind spots the model is a real comparator, so the error rate falls.
   - Errors from the model's blind spots become common to authors and reviewers alike; peer review becomes a cross-check between near-copies, so the escape probability rises.
   - Whether the product rises or falls is an empirical question, field by field.
2. **One lender for all borrowers.**
   - Another reasoner's objection is cheap because it reuses someone else's contact with the world. A model trained on the written record is that, industrialized.
   - It catches the borrower's slips, never the lender's.
   - The twenty journalists checking each other against the same wire dispatch.
3. **Provenance laundering and the epistemic commons.**
   - Model output re-enters repositories, papers and the web without provenance. Copies look like independent witnesses; the apparent number of witnesses grows while genuine contacts with the world do not.
   - Model collapse on recursively generated data (Shumailov et al., 2024).
   - Ten sources tracing back to one model add signatures, not evidence (severity, ch. 9).
4. **The institutional throughput squeeze.**
   - Generating answers is no longer the bottleneck; knowing which are reliable is.
   - Incentives reward throughput; budgets drift toward generation tools and away from evaluators.
   - Evaluative capacity hollows just as unchecked volume grows fastest.

**Blocks:**
- *Exemple quantitatif* **escape-b**:
  - **mise en place:** the producer improves (P(E) from 10 % to 2 %) while the checker comes to share 60 % of its error causes (a shared model); then the checker becomes precise (f = 0.5 %);
  - **figure:** escape and risk across the presets *peers* → *shared model* → *shared + precise* (bars, both uptake policies);
  - **calcul:** global §7;
  - **lecture:** under a shared model, 96 % of errors escape when flags are heeded at the PPV rate. Precision restores uptake, but 68 % still escape because of the shared causes. Only a comparator that fails differently lowers that floor.
- *Nuance*: a second mechanism adds to correlation. As errors become rare, most of a fixed checker's alarms are false, so people stop heeding it. In a simple model this makes the checker decorative without, by itself, raising total risk; total risk rises when correlation rises too. The example separates the two effects.
- *Question*: in your organization, is evaluative capacity a named number that caps production, or whatever time is left over?

**Keys out:** correlated errors across users; provenance laundering; throughput squeeze.

**Points clés (intended):**
- Shared models lower individual error rates and can raise escape.
- A borrowed comparator cannot check the lender.
- Copies without provenance pose as witnesses.
- Evaluation, now the scarce resource, is the one being starved.
