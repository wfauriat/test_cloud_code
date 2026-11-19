# Content Spec — Part III: De l'informatique classique à l'IA (ch. 10–13)

Read `00_global.md` first.

**Part page:** the theory of Part II, applied to the computing stack. What made classical software trustworthy, and what changes when the specification moves into data. Time-sensitive AI evidence goes in dated `.cas` blocks; the argument must survive the next model generation.

---

## Chapter 10 — Pourquoi l'on peut oublier les couches basses (~15–18 pages)

**Argument step:** S10. **Keys in:** ch. 6, 8. **Source threads:** `bits-to-composition`, `design-by-contract`, `front-loaded-verif`, `failure-has-address`.

**Sections:**
1. *Boîte à outils*: **contracts.** Pre- and postconditions; the Hoare triple {P} C {Q}; design by contract (Meyer).
2. **From elementary operations to composition.**
   - Add, compare, move, jump: trivial, fast and deterministic.
   - No special ingredient on the way up; what makes composition survivable is that each layer hides its machinery behind an exact promise.
   - The shipping-container analogy.
3. **Every layer is a written promise.**
   - TCP, sorting, the file system.
   - A specification is a written statement: in advance, readable by another, disputable, versionable, violable.
   - Define **composant spécifié** (`def:composant-specifie`), contrasted in advance with the learned component (ch. 11).
   - A contract protects only what it states, and only where something enforces it.
4. **Verifying once, before use.**
   - Types, unit tests, review, static analysis, fuzzing, formal proof: all check the component against its statement before deployment, covering every later call.
   - Dijkstra's limit bounds the certainty but not the kind of move.
   - The bridge load rating.
   - Define **vérification en amont**.
5. **Failures have an address.**
   - Mars Climate Orbiter told in full: SM_FORCES, lbf·s vs N·s, factor ≈ 4.45, 23 September 1999.
   - The organizational causes, and beneath them a written specification and its violation point.
   - Even undocumented code admits an "it should have…" afterwards.

**Blocks:**
- *Étude de cas*: the Mars Climate Orbiter Mishap Investigation Board report (1999).
- *Nuance*: written is not yet checked. Three tiers:
  - enforced contracts (types, schemas, tests): checked in advance, automatically;
  - written contracts: an address afterwards, front-loaded only if turned into a check;
  - writable but unwritten contracts: an address afterwards.

  A learned component has none of the three, for the component itself.
- *Question*: when a component of your pipeline fails, can you point to the rule it violated, and was that rule enforced by anything other than a document?

**Link:** Orbiter's units were laundered (ch. 8); here the same story yields an address.

**Keys out:** contract; specified component; front-loaded verification; address; the three tiers.

**Points clés (intended):**
- Each layer hides its machinery behind a written promise.
- Written promises can be checked once, in advance.
- Classical failures have an address.
- Written is not checked unless something enforces it.

---

## Chapter 11 — Quand la règle est tirée des données (~16–20 pages)

**Argument step:** S11. **Keys in:** ch. 10. **Source threads:** `spec-into-data`, `next-token-scale`, `plausibility-not-truth`, `steering-not-spec`.

**Sections:**
1. **The specification moves into the data.**
   - Handwriting, résumé fit, summaries: tasks that resisted software because nobody could write the rule.
   - Examples plus optimization produce a **composant appris** (`def:composant-appris`).
   - Gain: reach. Price: the guarantee and legibility.
   - The specification migrated into the training data, the objective and the curation.
   - The review question changes from "what does line 42 do?" to "who chose the examples?" (Sculley et al.).
   - The certainty was spent, not lost.
2. **The next-token engine.**
   - Predicting the next fragment at industrial scale; nobody types in grammar.
   - The logit lens: generic filler, then the right country, then the city near the top.
   - Reach is real: the BCG figures (dated `.cas`).
   - Because structure accumulated only where it helped prediction, competence has no clean boundary (forward link to ch. 12).
3. **Fluent and wrong without breaking anything.**
   - Plausibility is the objective; truth a frequent correlate.
   - A fluent falsehood contradicts nothing written.
   - Post-training makes errors rarer without making a guarantee.
   - Fluency is uniform across right and wrong answers.
4. **Steering is not specifying.**
   - System prompts, RLHF, guardrails, benchmark suites: real engineering that moves tendencies and states no invariant.
   - A preference dataset is more examples.
   - Goodhart's law (Strathern's formulation); reward hacking and sycophancy.
   - Training a dog vs wiring a circuit breaker.

**Blocks:**
- *Étude de cas* (dated): *Mata v. Avianca* (S.D.N.Y. 2023).
- *Étude de cas* (dated): BCG reach figures (Dell'Acqua et al., 2023).
- *Nuance*: *Moffatt v. Air Canada* (2024) is often cited as a hallucinating chatbot, but no evidence on the chatbot's technology was before the tribunal. The case shows that an automated answer is the firm's own act; it is not evidence about language models. (Verify the airline's later statement before using it, global §8.)
- *Boîte à outils*: Goodhart's law; RLHF in two sentences.
- *Question*: in your system, which behaviours are specified, and which are only steered?

**Terminology:** *consigne* (gloss *prompt* once); *test de référence* (gloss *benchmark* once); *token* kept in italics.

**Keys out:** learned component; reach vs guarantee; plausibility as objective; steering vs specification.

**Points clés (intended):**
- Learning moves the rule into data.
- Reach is bought with the guarantee.
- A fluent falsehood breaks no contract.
- Steering moves distributions; it does not state invariants.

---

## Chapter 12 — Au sommet de la pile, un autre régime (~18–22 pages)

**Argument step:** S12. **Keys in:** ch. 3 (calibration), 7 (P3), 9 (severity), 10–11. **Source threads:** `three-flips`, `layer-vs-output`, `jagged-frontier-bcg`, `kalai-vempala-tail`.

**Sections:**
1. **Three properties flip together.**
   - What is promised: contract → tendency.
   - How failure presents: definable divergence → fluency indistinguishable from success.
   - Where the post-mortem lands: an address → a distribution ("you cannot merge a patch into a distribution").
   - Frequency is not the axis; definability and front-loadability are.
2. **Verifying the layer vs checking outputs.**
   - Statistical components are old (spam filters, ranking); what is new is a general-purpose model *composed* into arbitrary software.
   - The once-for-all move is gone. Verification must be rebuilt around tasks that admit a mechanical check (ch. 13) or placed on outputs before they become actions (ch. 18).
3. **The jagged frontier.**
   - The BCG task just outside GPT-4's competence; −19 points (dated `.cas`).
   - Strong on one task, weak on a neighbouring one; the boundary moves with each version; both sides look the same from inside the conversation.
   - Mapping the frontier is an ongoing deployment activity.
4. **Calibration, the long tail and consistent errors.**
   - Kalai–Vempala: for arbitrary facts, a model calibrated to its training distribution must hallucinate at roughly the singleton (monofact) rate.
   - Evaluations that grade "I don't know" below a guess select for confident guessing (Kalai et al., 2025).
   - Two regimes: guessing errors scatter across samples, so re-asking flags them; consistent errors repeat, so re-asking passes them.
   - Semantic entropy (Farquhar et al.).
   - Breaking the equilibrium: train and grade abstention.

**Blocks:**
- *Noyau formel*: the Kalai–Vempala bound stated roughly (hallucination rate ≥ singleton rate − miscalibration − small terms), with *generative* calibration defined.
- *Exemple quantitatif* **plausibility**:
  - **mise en place:** three kinds of question, five samples each;
  - **figure:** the three answer distributions (bar charts), with severity and false-flag rate annotated;
  - **calcul:** the table of global §7;
  - **lecture:** re-asking is a severe check for guessing errors (99.9 %) and a weak one for misconceptions (42 %), and it flags right answers too when the model is unsure.
- *Nuance* (three):
  1. "Below: a definable divergence" does not mean errors are loud; Orbiter's unit error ran for months without a decisive alarm.
  2. **Structural vs salience omission:** the frame problem in AI was always about relevance among represented facts (McCarthy & Hayes; Dennett's robot). Under salience omission, P3a holds only for comparators that reuse the same weights and prompt. This refines P3 (ch. 7) and explains part of the jaggedness.
  3. Two senses of calibration: confidence calibration is an honest partial fix, while generative calibration entails hallucination and has to be departed from. The tell did not vanish; it moved into the spread of many answers, for one class of errors only.

**Keys out:** regime flip; output-level checking; jagged frontier; generative calibration; guessing vs consistent errors; structural vs salience omission.

**Points clés (intended):**
- At the top of the stack, promise, failure and post-mortem change regime together.
- Checks move from the layer to outputs.
- Competence is jagged.
- Calibrated generation must invent rare facts.
- Re-asking catches guessing, not consistency.

---

## Chapter 13 — Synthèse : deux axes et quatre sources de comparateurs (~12–15 pages)

**Argument step:** S13. **Keys in:** Parts II–III. **Source threads:** `two-axes-matrix`, `four-sources`.

**Sections:**
1. **Two axes instead of three kinds.**
   - Cross where the cause lies (inside or outside the frame) with whether any comparator disagrees (signalled or silent).
   - The 2 × 2 table, filled with the book's examples:
     - failing test or crash / fluent wrong answer;
     - colleague's objection or drift alarm / the turkey's last morning.
   - The row is set by the frame and cannot be inspected from inside; the column is set by what stands nearby, and can be designed.
   - Adding comparators that fail differently moves errors from right to left.
   - Define **erreur signalée / silencieuse**.
2. **Four sources of comparators.**
   - A statement made in advance; your own checks; another reasoner; the world.
   - A table (`tbl:ch13-sources`) contrasting specified and learned components.
   - Where a task admits a mechanical check, abundant generation becomes a plain benefit: generate, keep what passes.
   - Proof checkers (Lean autoformalization), compilers and tests, schemas, Simplex architectures.
   - Two limits: a statement checks conformity to itself; and it must not come from the thing it checks (one model writing both code and tests).
3. **Verification vs validation.** Solving the stated problem right vs stating the right problem. Why fields resting on validation (physical simulation) gain least from abundant generation.

**Blocks:**
- *Noyau formel*: formality changes the column, not the row. Deduction and induction, specified and learned components, are equal as to the adequacy of their frames and unequal as to how their errors can be found.
- *Nuance*:
  - specified components *can empty the silent cell in advance*; they do not keep it empty by nature (classical code has many silent errors);
  - on Simplex and run-time assurance, verification moves around the learned component, while validation stays where it was (the envelope rests on a plant model, itself a frame).
- *Étude de cas*: Lean autoformalization (dated if specific systems are named).
- *Question*: which cell does your test suite actually cover, and what sits in the two silent cells?

**Figures:** the 2 × 2 matrix as a figure (`fig:ch13-deux-axes`), with arrows "adding comparators" (right → left) and "no method from inside" (no arrow bottom → top).

**Keys out:** signalled and silent errors; the four sources; V&V.

**Points clés (intended):**
- Errors sort on two axes.
- The row is fixed by the frame; the column can be designed.
- Learned components crowd the inside-and-silent cell.
- Comparators come from four sources, and automation reshapes each.
- Verification can be rebuilt around a model; validation cannot be automated away.
