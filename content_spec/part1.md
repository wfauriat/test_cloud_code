# Content Spec — Part I: Agir d'après une représentation (ch. 1–4)

Read `00_global.md` first. Source threads: `source_threads_en.md`.

**Part page (≈ 1 paragraph):** we never act on the world directly, but through a picture. This Part supplies the tools to reason and decide inside one: logic and probability (ch. 1), the frame (ch. 2), probability as judgment (ch. 3), deciding on belief (ch. 4).

---

## Chapter 1 — Boîte à outils : logique, conditionnement, probabilité (~15–20 pages)

**Argument step:** tooling for S2–S4. **Keys in:** none. **Source threads:** none (primer); draw on `relevance-frame`, `bayesian-judgment`, `neither-right-nor-wrong` for examples only.

**Purpose:** recall, cleanly and in the book's own terms, the logical and probabilistic tools the whole book uses. Recall, not a course: each tool is introduced by the question it answers.

**Sections:**
1. **Deduction and induction.** Validity vs soundness: a valid argument with a false premise. Induction as generalization from observed regularities; Hume's problem announced (developed in ch. 7). Each mode is "true provided that…".
2. **Conditional rules and hidden conditions.** "If A then B", in practice "A and (…) then B". Boiling water as a first glimpse (the full story is in ch. 2).
3. **Probability: rules and readings.**
   - Axioms in brief.
   - Two readings: frequency over repetitions vs degree of belief given knowledge.
   - Why the book adopts the judgment reading without discarding frequencies (which are what calibration measures, ch. 3).
4. **Conditional probability as a share of worlds.** Pr(B | A) = Pr(A ∩ B)/Pr(A), read as "among the worlds where A holds, the share where B also holds". The law of total probability.
5. **Updating: Bayes in odds form.** Posterior odds = prior odds × likelihood ratio. Worked numeric example (a test result).
6. **Scoring a forecast: surprise.** −ln Pr(outcome); the likelihood ratio as the ratio of surprises. Set up the tool used in ch. 3 without the sailboat numbers.

**Blocks:**
- *Noyau formel*: the axioms; Bayes in odds form with derivation; the log score and its link with the likelihood ratio.
- *Exemple quantitatif*: one simple Bayes update in odds form with a table (prior, likelihood ratio, posterior). Choose numbers distinct from ch. 9's screening example.

**Not here:** base rates and PPV (ch. 9); variance (ch. 5); reliability (ch. 8); SEU (ch. 4).

**Keys out:** deduction/induction (validity, conditionality); conditional probability; total probability; Bayes in odds form; likelihood ratio; log score; frequency vs judgment readings.

**Points clés (intended):**
- Both deduction and induction deliver conclusions "provided that…".
- Probability can be read as frequency or as judgment; this book reasons with judgment and checks it with frequencies.
- Pr(B | A) is a share of worlds.
- Updating multiplies odds by a likelihood ratio.
- Surprise, −ln Pr, measures how badly an outcome fits a forecast.

---

## Chapter 2 — Le cadre : ce qui compte et ce qu'on tait (~15–18 pages)

**Argument steps:** S1, S2. **Keys in:** ch. 1. **Source threads:** `map-territory`, `relevance-frame`, `deduction-induction`. The author's arXiv article covers this ground and is citable (sections "Acting through a constructed picture", "Relevance and conditioning", "Finite specification", "Formality does not lift the limit").

**Sections:**
1. **The world answers the action, not the picture** (`map-territory`).
   - Target, world, gap; the representation we build and act on.
   - The sailor's 5 % is a judgment within a chosen frame, not a property of the sea; yet it drives the decision, and the decision shapes what follows.
   - Satellite phone example: the world resolves to one outcome where the picture spread a distribution.
   - Korzybski with the operational twist: you steer by the map; the hull meets the rocks.
   - Define **représentation** (`def:representation`).
2. **Relevance and exceptions** (`relevance-frame`).
   - Boiling water told in full: 100 °C; the salted water at 101 °C; the sealed vessel at 104 °C; Mont Blanc at ≈ 85 °C.
   - The pattern `A ∩ (…) → B`; Pearl's minefield; "birds fly".
3. **The frame as a finite specification.**
   - Define **cadre** (`def:cadre`): variables, categories, model class, objective.
   - Formal core: Pr(Y) = Σ Pr(Y | X = x) Pr(X = x). The choice of X precedes the calculus and is circular.
   - The trade-off: more stated conditions make rules longer and more brittle; fewer leave silent exceptions.
4. **Formality does not lift the limit** (`deduction-induction`).
   - Deduction is true provided its axioms, boundary conditions and idealizations hold; induction provided the new context is similar enough.
   - Pearl's causal calculus is deductive relative to a given graph; conformal prediction is valid relative to exchangeability.
   - The clinical model deployed on a shifted population.
   - The reflex to formalize further only moves the choice one level up (forward link to ch. 7, the regress).
5. **A word on "the frame problem".** Its AI origin (McCarthy & Hayes; Dennett's robot), and the broader epistemic sense used in this book. One paragraph, to lift ambiguity.

**Blocks:**
- *Noyau formel*: conditioning on X; the frame-relativity of deductive and inductive guarantees (graph, exchangeability).
- *Étude de cas*: the clinical prediction model under shift (generic; cite literature if a specific case is used).
- *Nuance*: stating more vs fewer conditions; no setting removes both risks.
- *Question*: in your project, which numbers describe measured properties of the world, and which describe the team's degree of belief inside its model?

**Figures:** a schematic of target, world, picture and action; the boiling-water rule refined step by step (a small table).

**Keys out:** `def:representation`, `def:cadre`; the conditional-rule pattern; frame-relativity of rigour.

**Points clés (intended):**
- We act on pictures, and the world answers actions.
- Every rule hides an open background.
- Choosing what to state is choosing a frame.
- Rigour inside a frame never certifies it.
- The AI frame problem is a special case of a general epistemic one.

---

## Chapter 3 — Mondes possibles : la probabilité comme jugement (~12–15 pages)

**Argument step:** S3. **Keys in:** ch. 1–2. **Source threads:** `bayesian-judgment`, `neither-right-nor-wrong`.

**Sections:**
1. **Possible worlds** (`bayesian-judgment`). Logical assertions exclude worlds; probabilistic assertions weight the remaining ones (Russell & Norvig). Pr(B | A) as the share of situations hidden in `(…)` where the rule works.
2. **Reasoning in reverse.** Stop chasing "the right answer". Ask what could hide in `(…)`, what could vary, and which variations would flip the conclusion. This is not inventing far-fetched scenarios, but listing likely or non-excludable variations. "Subjective" does not mean arbitrary (de Finetti, Savage, Jaynes, Lindley).
3. **A forecast vs a forecaster** (`neither-right-nor-wrong`).
   - Mr X (5 %) and Mr Y (0.1 %) assess the same light boat. Neither is right or wrong before the race.
   - After the race: if the boat breaks, Y is far more surprised; if it holds, the outcome barely separates them.
   - Uneventful mornings are weak evidence; the turkey is announced here and developed in ch. 5.
4. **Calibration (first sense) and the track record.**
   - The 70 % rain forecaster over a year.
   - Proper scoring rules; calibration needs repetition (forward link to ch. 17, calibrate vs gate).
   - Introduce **historique** (track record) informally.

**Blocks:**
- *Exemple quantitatif* **log-score**:
  - **mise en place:** the two forecasts;
  - **figure:** bar chart of surprise (−ln Pr) for X and Y under both outcomes;
  - **calcul:** the table of global §7 (3.00 / 6.91; 0.051 / 0.001; ratios 50 and 0.951);
  - **lecture:** a single outcome grades weakly, especially the likely one.
- *Noyau formel*: proper scoring rules (log score as an example), stated briefly.
- *Question*: when a forecast "turned out wrong", did anyone check whether it was a bad forecast, or a good forecast meeting its less likely outcome?

**Keys out:** possible worlds; reasoning in reverse; calibration (confidence sense); track record; "one outcome barely grades".

**Points clés (intended):**
- A probability weighs possible worlds.
- Reasoning in reverse looks for the variation that would flip the conclusion.
- A single outcome barely grades a forecaster.
- Only repetition, scored properly, can.

---

## Chapter 4 — Décider d'après ce que l'on croit (~12–16 pages)

**Argument steps:** S1 (decision side), S4. **Keys in:** ch. 1–3. **Source threads:** `seu-sailboat-roulette` (baseline only: no omitted factor, no buffer).

**Sections:**
1. *Boîte à outils*: **Savage's subjective expected utility**. Acts, states, consequences; choosing on one's own probabilities. One sentence on why SEU and not a frequency rule: the decision is made before the world answers.
2. **The sailing race.**
   - Light, fast boat vs reinforced, slower boat; a breakage means a tow costing more than the prize.
   - Treat the reinforced boat as a sure baseline. Derive p∗ = ΔU/(ΔU + L) = 1/(1 + L/ΔU) (equation `eq:ch04-seuil`).
   - Mr X and Mr Y can both choose rationally, and choose differently.
3. **Russian roulette.** As L/ΔU grows, p∗ tends to 0: you play only if utterly convinced, or if the prize is immense.
4. **Once, or many times.** A one-shot decision has no population of trials, and the world's answer arrives after the act. Announce that calibration helps only with repetition, and that one-shot acts need something else (ch. 17).
5. **The question left open.** What if the conviction came from a frame that missed a loaded chamber? Nothing in the reasoning would warn. Pose it; answer it in ch. 17.

**Blocks:**
- *Noyau formel*: the derivation of p∗.
- *Exemple quantitatif* **seu-a**:
  - **mise en place:** stakes ratio 25;
  - **figure:** p∗ as a function of L/ΔU on log axes, with Mr X (5 %) and Mr Y (0.1 %) plotted against p∗ = 3.85 % and the roulette point (L/ΔU = 10 000, p∗ = 0.0100 %);
  - **calcul:** the seu-a rows of global §7;
  - **lecture:** the same rule gives opposite choices to two rational sailors, and the threshold collapses as stakes grow.
- *Nuance* (announcement): the world does not consult our belief. Forward link to ch. 17.
- *Question*: for your next irreversible deployment, what is L/ΔU, and what threshold does it imply?

**Keys out:** SEU; p∗; stakes ratio; one-shot vs repeated decision.

**Points clés (intended):**
- We decide on what we believe.
- The threshold p∗ falls as the stakes ratio grows.
- Two rational deciders can disagree.
- One-shot acts are not protected by averages.
