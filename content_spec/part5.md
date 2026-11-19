# Content Spec — Part V: Décider et se prémunir (ch. 17–18)

Read `00_global.md` first. **Register of recommendations (D16) is still open.** Until decided, write the remedies as *working practices with their rationale and limits*, not as rules. Mark the strength of evidence for each (documented practice vs proposal).

**Part page:** from diagnosis to practice: deciding once, placing checks, organizing them.

---

## Chapter 17 — Décisions sans appel (~16–20 pages)

**Argument step:** S15 (deciding). **Keys in:** ch. 3–4, 7, 9. **Source threads:** `seu-sailboat-roulette` (extended), `calibrate-vs-gate`, `sandboxes-and-gates`, `four-questions`.

**Sections:**
1. **The sailing race revisited.**
   - Mr Y inspects the boat and finds a crack: the picture changes, p jumps above p∗, he switches boats. A frame is revised by contact with the world.
   - The crack he does not see: the world's odds p_w = 1 − (1 − p)(1 − z), outside the picture.
   - The four outcomes of model M2: correct go; silent trap; saved by the buffer; over-caution and its price.
   - Define **marge d'humilité** (humility buffer).
2. **Calibrate where repeatable; gate where one-shot.**
   - Repeated decisions against a stable distribution (triage, weather, credit) can be calibrated: thresholds, abstention, stated vs observed frequencies.
   - A one-shot decision (a sea crossing, surgery, an architecture commitment, an irreversible agent action) has no population, and a rate is no promise about this instance.
   - What protects it is a **verrou** (`def:verrou`): an independent check before the action, plus a deliberate buffer.
   - Calibration is also the only way to grade a forecaster (back-link to ch. 3).
3. **Sandboxes and gates.**
   - Exploration is how a frame learns what it omitted (ch. 7); prudence says restrict automated agents. Both hold, because an action is also a question put to the world.
   - **bac à sable** (`def:bac-a-sable`): asking the world is cheap and reversible, so explore freely.
   - **verrou**: the world's answer would be too costly or irreversible, so another comparator must stand in.
   - Coding agents thrive where compilers and tests answer instantly, freely and reversibly.
4. **Receiving a confident number: four questions.**
   - A number given without its conditions transfers responsibility dressed as information.
   - The four questions:
     1. Under what conditions does this hold?
     2. What would change the number?
     3. What is the most likely way it is wrong?
     4. What was deliberately not modelled?
   - Accept "we don't know" as a substantive answer.
   - "It will rain tomorrow" is a directive in the costume of information; "70 %" supports a decision in proportion to *your* stakes.
   - For automated outputs, the questions go to an institution (link to ch. 16).

**Blocks:**
- *Noyau formel* **M2** (full): the decider cannot condition on z; b is a judgment, not an estimate.
- *Exemple quantitatif* **seu-b**:
  - **mise en place:** the presets of global §7 (Mr Y, unseen crack, crack plus buffer, roulette, plus an over-caution case with z = 0 and b = 4 %);
  - **figure:** a 2 × 2 outcome grid (decision on p + b × world risky or not), with each preset placed, plus a plot of p_w vs p + b against p∗;
  - **calcul:** the table rows;
  - **lecture:** the buffer is the decider's only lever against what the picture omits; it has a price, small when L/ΔU is large compared with what it insures.
- *Nuance*: it is tempting to put the omitted risk into the decision rule ("go iff the true total risk is below the threshold"). Under SEU, rationality is relative to belief, and z is precisely what cannot be seen. Treating it as a readable dial would make ontological uncertainty a measurable third quantity, contradicting P1 and P3.
- *Question*: for your next irreversible deployment, what is L/ΔU, what threshold does it imply, and is your estimate plus a buffer below it?

**Keys out:** humility buffer; gate; sandbox; calibrate vs gate; the four questions.

**Points clés (intended):**
- The world holds odds the picture cannot show.
- A buffer is a judgment with a price.
- Calibrate what repeats; gate what happens once.
- Explore where the world answers cheaply.
- Ask for the conditions of any confident number.

---

## Chapter 18 — Un remède à trois niveaux (~16–20 pages)

**Argument step:** S15 (organizing). **Keys in:** all previous chapters. **Source threads:** `layer1-attitude`, `layer2-placement`, `layer3-organization`. The arXiv article's sections "Epistemic humility as structural commitment" and "Implications for practice, organisation, and pedagogy" are citable.

**Sections:**
1. **Level 1, attitude: comparators you supply yourself.**
   - Humility is not the residue when methods run out; it is the earliest source of comparators.
   - An order-of-magnitude expectation *before* running the model or reading the draft.
   - The pre-mortem.
   - Widening possible worlds on purpose: a stress case, a dreary alternative, a "what are we missing" branch (the buffer, ch. 17).
   - Limit (P3): self-made comparators reach beyond the model's frame, never beyond one's own. Necessary, never sufficient.
   - An attitude holds only if it is collective, which is level 3.
2. **Level 2, placement: where, who, what, how much.**
   - "A human in the loop" is satisfied by anyone who clicks Accept.
   - **Where (timeliness):** at regime boundaries, where output starts being relied on.
   - **Who (difference, comparability):** someone who shares the interface and understands one layer below.
   - **What:** output-checking vs picture-checking (was the task inside the tool's competence?). The second cannot be done by the tool or a tool sharing its frame.
   - **How much:** sized to stakes along the cost of independence (P4). Review capacity is a rate and should cap production.
   - RAG moves claims into documents a reviewer can open, without making a model truthful.
3. **Level 3, organization: independence, status, track record, measurement.**
   - The test for any review step: what error could it catch that the producer could not?
   - Four practices:
     1. size production to independent review capacity, naming who can check each domain;
     2. make every result reaching a decision state its status;
     3. keep a track record;
     4. measure the escape probability with seeded errors.
4. **Five questions before acting on any claim** (closing synthesis):
   1. What is the comparator?
   2. How can it fail differently?
   3. Are the conditions stated so the two can be compared?
   4. Does the comparison happen before the action?
   5. Who has to listen, and will they?

**Blocks:**
- *Étude de cas*: threat image projection in airport screening (fictitious threat images projected into live X-ray screening; per-screener hit rates; EU rules linking results to training; verify the regulation reference). Mutation testing in software.
- *Nuance*:
  - seeded errors measure escape only for errors someone could imagine, so they must come from a different frame than the reviewers' (a corrosion specialist seeding the structural review);
  - seeding works best when seeded items are indistinguishable from real ones;
  - a reviewer who cannot read one layer below is theatre, worse than none, because they manufacture a signature others rely on.
- *Question*: the five questions, as a closing checklist.

**Figures:** a schematic of the three levels mapped onto the five conditions (which level secures which condition).

**Keys out:** the three levels; regime-boundary placement; seeded-error measurement; the five questions.

**Points clés (intended):**
- Humility is the first source of comparators.
- Place checks where output starts being relied on, with reviewers one layer deeper.
- Make status explicit and measure escape.
- None of the three levels suffices alone.
