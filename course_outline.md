# Chapter Outline — Monograph (Option D)

**Status:** v0.1 for author review. Once approved, it is the basis for the content spec.
**Language:** working document in English. Chapter titles are given as proposed French titles (the monograph is written in French), with an English gloss.
**Traceability:** source threads are cited by their map ids (`map-territory`, …) so the content-spec writer can locate the material. These ids belong to the working documents only and never appear in the monograph (spec §6.1, §13.4).

---

## 0. Overview

| # | Part | Chapter (proposed French title) | English gloss |
| :-- | :-- | :-- | :-- |
| — | Front matter | Avant-propos | Preface: purpose, stance, hybrid process, how to read, block legend |
| 0 | — | Cartographier le terrain | Charting the map |
| 1 | I. Agir d'après une représentation | Boîte à outils : logique, conditionnement, probabilité | Primer: logic, conditioning, probability |
| 2 | I | Le cadre : ce qui compte et ce qu'on tait | The frame: what counts and what goes unsaid |
| 3 | I | Mondes possibles : la probabilité comme jugement | Possible worlds: probability as judgment |
| 4 | I | Décider d'après ce que l'on croit | Deciding on what we believe |
| 5 | II. Ce qui peut nous détromper | Trois incertitudes, et ce que mesure une barre d'erreur | Three uncertainties, and what an error bar measures |
| 6 | II | Détecter une erreur : comparateurs et cinq conditions | Detecting an error: comparators and five conditions |
| 7 | II | Le cadre, cause commune de nos contrôles | The frame as common cause of our checks |
| 8 | II | Indépendance, chaînes et contrôles croisés | Independence, chains and cross-checks |
| 9 | II | Sévérité, fausses alertes et probabilité d'échappement | Severity, false alarms and escape probability |
| 10 | III. De l'informatique classique à l'IA | Pourquoi l'on peut oublier les couches basses | Why the lower layers can be forgotten |
| 11 | III | Quand la règle est tirée des données | When the rule is drawn from data |
| 12 | III | Au sommet de la pile, un autre régime | A different regime at the top of the stack |
| 13 | III | Synthèse : deux axes et quatre sources de comparateurs | Synthesis: two axes and four sources of comparators |
| 14 | IV. L'automatisation et ses angles morts | Des chaînes qui agissent | Chains that act |
| 15 | IV | L'érosion des vérifications humaines | The erosion of human checks |
| 16 | IV | Angles morts collectifs | Collective blind spots |
| 17 | V. Décider et se prémunir | Décisions sans appel | Decisions without appeal |
| 18 | V | Un remède à trois niveaux | A three-level remedy |
| — | — | Conclusion : la méthode appliquée à elle-même | Conclusion: the method applied to itself |
| A–D | Appendices | Outils de référence · Glossaire · Notation · Paramètres des exemples quantitatifs | Reference toolkit · Glossary · Notation · Parameters |

That makes 19 numbered chapters plus a conclusion, slightly above the ~15–18 of §6.3. If a reduction is wanted, two merges are natural: 1 into 2–3 (primer distributed as *Boîte à outils* blocks), and 13 into 12. Both would lengthen their host chapters.

---

## 1. The Statements (renumbered in order of appearance)

Proposed statuses are for author review (D8). Slugs are fixed now because other chapters will reference them.

| New # | Slug | Statement (short) | Chapter | Proposed status | Robustness note to include |
| :-- | :-- | :-- | :-- | :-- | :-- |
| P1 | `prop:desaccord` | A quantitative statement of uncertainty summarizes disagreement within an admitted set of alternatives; an omitted alternative contributes none | 5 | *résultat sous hypothèses* (follows from the variance decomposition over an admitted set) | Unrecorded variation of an omitted factor does enter, as unexplained scatter; "silent" means unattributed, not always absent |
| P2 | `prop:comparateur` | An error is detected only when a claim is compared with something expected to agree, and the two disagree | 6 | *définition* (close to a tautology, made useful by the five conditions) | Its value lies in the five conditions, not in the statement itself |
| P3 | `prop:cause-commune` | (a) A comparator computed from the frame's own content cannot detect an error caused by a factor the frame omits; (b) observations can, only if the factor varied during collection, and only through what the frame records | 7 | (a) *résultat sous hypothèses*; (b) *résultat sous hypothèses*, illustrated by *constats empiriques* | (a) holds conditional on x; real comparators rarely condition that cleanly (salience omission, ch. 12) |
| P4 | `prop:independance` | Independence is relative to a class of errors and is paid for in comparability | 8 | first half *définition*; the trade-off *hypothèse de travail* (strong tendency, with known exceptions) | Cheap-and-different comparators exist (naive questions, orders of magnitude, conservation laws) |
| P5 | `prop:chaines` | Chains unite blind spots; cross-checks intersect them | 8 | *résultat sous hypothèses* (independence, perfect comparison and uptake) | Corrected comparison term; the optimal reviewer distance is suggested, not derived |

Supporting definitions with fixed slugs: `def:cadre` (ch. 2), `def:representation` (ch. 2), `def:affirmation`, `def:controle`, `def:comparateur`, `def:prise-en-compte` (ch. 6), `def:echappement` (ch. 6, quantified in ch. 9), `def:angle-mort` (ch. 8), `def:blanchiment` (ch. 8), `def:composant-specifie` (ch. 10), `def:composant-appris` (ch. 11), `def:severite` (ch. 9), `def:verrou`, `def:bac-a-sable` (ch. 17).

---

## 2. Chapters

Each entry gives:
- **Purpose:** the chapter's purpose;
- **Sections:** with source threads;
- **Keys in:** what the reader must already hold;
- **Keys out:** what the chapter establishes;
- **Notable blocks:** quantitative examples, case studies and nuances;
- **Links:** backward and forward links where they matter.

### Avant-propos
- **Purpose:** state the purpose (acting on the world through a picture, and the method of building that picture) and the stance (practical first; formality as a means; a working approach, not a prescription; self-critical about its own scaffold).
- **Content:**
  - who the book is for;
  - how to read it: block legend, the main-text rule, reading paths in ch. 0;
  - disclosure of the hybrid human–AI development process (spec §13.4 wording);
  - the arXiv article as the one self-reference;
  - "judge it by what it says".

### Chapter 0 — Cartographier le terrain
- **Purpose:** walk through the whole argument in plain language before walking the path.
- **Sections:**
  1. **Opening puzzle (case-driven):**
     - Mars Climate Orbiter: a failure with an address;
     - *Mata v. Avianca*: fluent, wrong, no contract broken;
     - METR: measured slower, felt faster.
  2. **The argument in five movements:** we act on a picture; errors are caught only by something that can fail differently; classical computing earned guarantees that learned models give up; automation removes and correlates checks; what we can still do.
  3. **Vocabulary, introduced narratively:** frame, picture, comparator, blind spot, escape.
  4. **One teaser in plain arithmetic:** 1 % error with 90 % escape vs 10 % error with 1 % escape.
  5. **Reading paths** (§5 below).
- **Keys out:** an informal version of every key concept; no formal definition.
- **Constraint:** at most two displayed formulas (the conditional-rule pattern `A ∩ (…) → B` and the go/no-go threshold idea), both in words first.

### Part I — Agir d'après une représentation
Part page: we never act on the world directly; this Part supplies the tools for reasoning and deciding inside a picture.

#### Chapter 1 — Boîte à outils : logique, conditionnement, probabilité
- **Purpose:** the unified primer (spec §13.1). Recalled, not taught from scratch, but stated cleanly in the book's own terms.
- **Sections:**
  1. Deduction and induction: validity, soundness, generalization.
  2. Conditional rules and hidden conditions.
  3. Probability: the axioms in brief; the frequency and judgment readings.
  4. Pr(B | A) read as a share of worlds.
  5. Bayes in odds form; the likelihood ratio.
  6. The logarithmic score (surprise).
- **Keys out:** conditional probability, Bayes in odds form, likelihood ratio, log score; frequency vs judgment interpretations.
- **Not here:** base rates and PPV (ch. 9); variance (ch. 5); reliability (ch. 8).

#### Chapter 2 — Le cadre : ce qui compte et ce qu'on tait
- **Purpose:** establish the picture and the frame.
- **Sections:**
  1. The world answers the action, not the picture (`map-territory`; satellite-phone example).
  2. Relevance and exceptions: boiling water, two failed tests, Mont Blanc (`relevance-frame`).
  3. The frame as a finite specification; the circularity of choosing variables (Formal Core: Pr(Y) by conditioning on X).
  4. Formality does not lift the limit: deduction and induction are both frame-relative; Pearl's calculus, conformal prediction, the clinical model (`deduction-induction`).
- **Keys in:** ch. 1.
- **Keys out:** `def:representation`, `def:cadre`; the conditional-rule pattern.
- **Links:** forward to the regress (ch. 7) and to the decision use of the picture (ch. 4).

#### Chapter 3 — Mondes possibles : la probabilité comme jugement
- **Purpose:** probability as weighing possible worlds; reasoning in reverse; why one outcome cannot grade a forecaster.
- **Sections:**
  1. Possible worlds and reasoning in reverse (`bayesian-judgment`).
  2. A forecast vs a forecaster: Mr X (5 %) and Mr Y (0.1 %); log score; likelihood ratio 50 vs ≈ 0.95 (`neither-right-nor-wrong`).
  3. Calibration (first sense): the 70 % rain forecaster over a year.
- **Keys in:** ch. 1–2.
- **Keys out:** possible worlds; calibration (confidence sense); "one outcome barely grades".
- **Notable blocks:**
  - *Exemple quantitatif*: the sailboat log-score comparison (computed table of scores and ratios).
  - *Question*: was the forecast bad, or a good forecast meeting its less likely outcome?
- **Links:** the turkey is announced here and developed in ch. 5.

#### Chapter 4 — Décider d'après ce que l'on croit
- **Purpose:** decision under SEU. We decide on what we think; one-shot stakes and the threshold p∗.
- **Sections:**
  1. Savage's SEU in a short *Boîte à outils*.
  2. The sailing race: light vs reinforced boat; derivation of p∗ = ΔU/(ΔU + L) (`seu-sailboat-roulette`, baseline).
  3. Russian roulette: p∗ → 0.
  4. One-shot vs repeated decisions, announced (developed in ch. 17).
- **Keys in:** ch. 1–3.
- **Keys out:** SEU, p∗, one-shot vs repeated.
- **Notable blocks:**
  - *Exemple quantitatif* **seu-a**: the threshold curve p∗ as a function of L/ΔU; Mr X and Mr Y placed on it; the roulette point.
  - *Nuance* (announced): what if the picture misses a factor? The question is posed here and answered in ch. 17.

### Part II — Ce qui peut nous détromper
Part page: what can tell us, in time, that we are wrong. General systems and quantitative reliability, grounded in non-AI cases (spec §13.1).

#### Chapter 5 — Trois incertitudes, et ce que mesure une barre d'erreur
- **Sections:**
  1. *Boîte à outils*: the law of total variance.
  2. Aleatory vs epistemic as a modelling choice (`aleatory-epistemic`).
  3. Ontological uncertainty and the inductivist turkey; the pre-2008 mortgage models (`ontological-residue`).
  4. Error bars measure disagreement: **P1** (`variance-disagreement`; the committee and the incomplete note).
  5. Why robustness tools and safety factors stay inside the frame; the bracket with a margin of 1.8 (`within-frame-defenses`).
- **Keys in:** ch. 1–3.
- **Keys out:** the three kinds of uncertainty; **P1**; admitted set.
- **Notable blocks:**
  - *Étude de cas*: pre-2008 mortgage models.
  - *Nuance*: Challenger is not a pure frame failure (data framing plus suppressed uptake), closed in ch. 6.

#### Chapter 6 — Détecter une erreur : comparateurs et cinq conditions
- **Sections:**
  1. Claim, check, comparator: definitions.
  2. **P2** and the five conditions: existence, difference, comparability, timeliness, uptake (`five-conditions`).
  3. Escape probability, introduced qualitatively (`def:echappement`).
  4. Challenger read through the five conditions (full case).
  5. Agreement and disagreement: what each shows.
- **Keys in:** ch. 5.
- **Keys out:** `def:affirmation`, `def:controle`, `def:comparateur`, `def:prise-en-compte`, `def:echappement`; **P2**; "failing differently".
- **Notable blocks:**
  - *Formel*: P(detected | wrong) = 0 when any condition fails.
  - *Question*: what is the comparator for your next claim?
- **Links:** comparability announces laundering (ch. 8).

#### Chapter 7 — Le cadre, cause commune de nos contrôles
- **Sections:**
  1. Common-mode failure: two pumps on one power supply (*Boîte à outils*).
  2. **P3a**: self-checks catch slips, not omissions; the finite-element vs hand calculation of the bracket (`frame-common-cause`).
  3. **P3b**: when observations catch frame errors; distribution shift; Google Flu Trends; dry-lab load tests; the wire-colour agent (`limits-of-data`).
  4. The meta-level regress: no free lunch; Hume, Goodman (`meta-nfl`).
  5. How new relevance enters: being told, finding out; the cost of exploring (`two-routes-in`).
- **Keys in:** ch. 2, 5, 6.
- **Keys out:** common-mode failure; **P3**; the two routes in.
- **Notable blocks:**
  - *Formel*: the likelihood ratio = 1 argument, with its conditioning assumption explicit.
  - *Nuance*: the conditioning is idealized (forward to salience omission, ch. 12).
- **Links:** forward to sandboxes (ch. 17).

#### Chapter 8 — Indépendance, chaînes et contrôles croisés
- **Sections:**
  1. *Boîte à outils*: series and parallel reliability.
  2. Blind spots (`def:angle-mort`).
  3. Independence is relative and paid for in comparability: **P4**; the comparator table; Knight & Leveson's 27 versions; Levins (`independence-cost-curve`).
  4. Composing steps (`divide-and-orchestrate`, engineering side: multiphysics chains).
  5. Chains vs cross-checks: **P5** (`series-vs-parallel`).
  6. Laundering at handoffs: the thermal field passed as a bare array; Orbiter's units; the cousins (units and definitions, provenance) (`uncertainty-laundering`).
- **Keys in:** ch. 6–7.
- **Keys out:** **P4**, **P5**; blind spot; `def:blanchiment`; cross-check.
- **Notable blocks:**
  - *Exemple quantitatif* **chain-a**: N steps, per-step error p, shared omitted factor q; unchecked chain vs per-step cross-checks; share of residual failures due to q.
  - *Nuance*: the corrected comparison term; the trade-off is not a proof; "cost rises with independence" is a tendency, not a law.

#### Chapter 9 — Sévérité, fausses alertes et probabilité d'échappement
- **Sections:**
  1. *Boîte à outils*: base rates and PPV, through a medical screening example.
  2. Severity (Mayo): a passing check is evidence only if it could have failed (`severity-bayes`).
  3. The false-alarm trap: a 1 % producer and a 10 % reviewer; PPV formula; 1/PPV investigations per real error.
  4. Probability matching and "cry wolf"; resolving disagreement with a third comparator.
  5. Risk = error rate × escape probability (`error-times-escape`), including the 1 %/90 % vs 10 %/1 % comparison.
- **Keys in:** ch. 1, 6, 8.
- **Keys out:** severity, PPV, the error × escape decomposition.
- **Notable blocks:**
  - *Exemple quantitatif* **escape-a**: a fixed checker; sensitivity (1 − c)(1 − m), PPV, uptake, escape and risk, under two policies (flags heeded at PPV rate vs every flag investigated).
  - *Nuance*: Bayes fixes PPV; behaviour decides uptake. The two must not be conflated.
- **Links:** this closes Part II; ch. 16 reuses escape-a with shared models.

### Part III — De l'informatique classique à l'IA
Part page: the same theory, applied to the computing stack; what changes when the specification moves into data.

#### Chapter 10 — Pourquoi l'on peut oublier les couches basses
- **Sections:**
  1. *Boîte à outils*: contracts, pre- and postconditions, Hoare triples.
  2. From elementary operations to composition; the shipping-container analogy (`bits-to-composition`).
  3. Every layer is a written promise: specified component (`design-by-contract`).
  4. Verifying once, before use; Dijkstra's limit (`front-loaded-verif`).
  5. Failures have an address: Mars Climate Orbiter (`failure-has-address`).
- **Keys in:** ch. 6, 8.
- **Keys out:** `def:composant-specifie`; front-loaded verification; "address".
- **Notable blocks:**
  - *Étude de cas*: the Orbiter investigation.
  - *Nuance*: written is not checked; the three tiers of contracts (enforced, written, writable but unwritten).

#### Chapter 11 — Quand la règle est tirée des données
- **Sections:**
  1. The specification moves into the data: reach gained, guarantee and legibility spent (`spec-into-data`).
  2. The next-token engine; the logit lens; the BCG reach figures (`next-token-scale`).
  3. Fluent and wrong without breaking anything (`plausibility-not-truth`).
  4. Steering is not specifying: RLHF, Goodhart/Strathern (`steering-not-spec`).
- **Keys in:** ch. 10.
- **Keys out:** `def:composant-appris`; reach vs guarantee; plausibility as objective.
- **Notable blocks:**
  - *Étude de cas* (dated): *Mata v. Avianca*.
  - *Nuance*: *Moffatt v. Air Canada* is weaker evidence than it is usually taken to be.
  - *Boîte à outils*: Goodhart's law.

#### Chapter 12 — Au sommet de la pile, un autre régime
- **Sections:**
  1. Three properties flip together (`three-flips`).
  2. Verifying the layer vs checking outputs one by one (`layer-vs-output`).
  3. The jagged frontier (`jagged-frontier-bcg`).
  4. Calibration, the long tail and consistent errors: Kalai–Vempala; generative vs confidence calibration; semantic entropy (`kalai-vempala-tail`).
- **Keys in:** ch. 3 (calibration), ch. 7 (P3), ch. 9 (severity), ch. 10–11.
- **Keys out:** the regime flip; generative calibration; guessing vs consistent errors; structural vs salience omission.
- **Notable blocks:**
  - *Exemple quantitatif* **plausibility**: known fact, arbitrary fact, popular misconception; per-mode probability of a wrong answer, severity of a 5-sample check, false-flag rate.
  - *Nuance* (×3):
    - definable is not loud (Orbiter's silent months);
    - structural vs salience omission (refines P3a);
    - two senses of calibration; the tell moved into the spread of answers.

#### Chapter 13 — Synthèse : deux axes et quatre sources de comparateurs
- **Sections:**
  1. Two axes instead of three kinds: where the cause lies × whether a comparator disagrees (`two-axes-matrix`).
  2. Four sources of comparators, for specified vs learned components; Simplex; Lean autoformalization (`four-sources`).
  3. Verification vs validation.
- **Keys in:** Parts II and III.
- **Keys out:** signalled vs silent errors; the four sources; V&V.
- **Notable blocks:**
  - *Formel*: formality changes the column, not the row.
  - *Nuance*: specified components can empty the silent cell in advance, not keep it empty by nature; Simplex moves verification, not validation.

### Part IV — L'automatisation et ses angles morts
Part page: what automation does to checks: it chains them, removes them, and correlates them.

#### Chapter 14 — Des chaînes qui agissent
- **Sections:**
  1. AI pipelines as orchestrated chains (`divide-and-orchestrate`, AI side).
  2. Agents as multi-step chains whose errors execute; answers vs actions (`agentic-compounding`).
  3. Laundering in AI pipelines: bare strings at handoffs (`uncertainty-laundering`, revisited).
- **Keys in:** ch. 8, 11–12.
- **Keys out:** agent as chain; action vs answer.
- **Notable blocks:**
  - *Étude de cas* (dated): Knight Capital.
  - *Exemple quantitatif* **chain-b**: an agent trajectory, N up to 12, with a shared factor; checking more of the same kind does not touch q.
- **Links:** forward to sandboxes and gates (ch. 17).

#### Chapter 15 — L'érosion des vérifications humaines
- **Sections:**
  1. Friction generated comparators (`friction-as-generator`).
  2. The lost tell; the METR sign error (`loss-of-the-tell`).
  3. Polish no longer signals substance (`signaling-collapse`).
  4. Bainbridge's irony and the two prompt traps (`bainbridge-prompt-trap`).
- **Keys in:** ch. 6, 9, 11.
- **Keys out:** the tell; costly signal and pooling; the irony of automation.
- **Notable blocks:**
  - *Boîte à outils*: Spence and Akerlof (signalling, lemons).
  - *Étude de cas* (dated): METR.
  - *Nuance*: credible disclosure as the way out of pooling, effective only if audited (forward to ch. 18).
  - *Question*: do you hand the model the problem or your solution?

#### Chapter 16 — Angles morts collectifs
- **Sections:**
  1. Error rate falls, escape probability rises (`rate-vs-escape-shift`).
  2. One lender for all borrowers (`same-lender`).
  3. Provenance laundering and the epistemic commons (`provenance-laundering`).
  4. The institutional throughput squeeze (`throughput-hollowing`).
- **Keys in:** ch. 8–9, 15.
- **Keys out:** correlation of errors across users; provenance.
- **Notable blocks:**
  - *Exemple quantitatif* **escape-b**: lower P(wrong), higher common-mode share c, alarm fatigue; separating the correlation effect from the false-alarm effect.
  - *Nuance*: the second mechanism (rarity makes the checker decorative) does not by itself raise total risk.

### Part V — Décider et se prémunir
Part page: from diagnosis to practice: deciding once, placing checks, organizing them.

#### Chapter 17 — Décisions sans appel
- **Sections:**
  1. The sailing race revisited: the unseen crack, the humility buffer, the world's odds vs your odds (`seu-sailboat-roulette`, extended).
  2. Calibrate where repeatable; gate where one-shot (`calibrate-vs-gate`).
  3. Sandboxes and gates: an action is also a question put to the world (`sandboxes-and-gates`).
  4. Receiving a confident number: four questions (`four-questions`).
- **Keys in:** ch. 3–4, 7, 9.
- **Keys out:** humility buffer; `def:verrou`, `def:bac-a-sable`; the four questions.
- **Notable blocks:**
  - *Exemple quantitatif* **seu-b**: the four outcomes (go/no-go × world risky or not); presets Mr Y, unseen crack, crack plus buffer, roulette.
  - *Nuance*: the omitted risk cannot enter the decision rule; the buffer is a judgment, not a measurement.

#### Chapter 18 — Un remède à trois niveaux
- **Sections:**
  1. Level 1, attitude: self-supplied comparators, the pre-mortem (`layer1-attitude`).
  2. Level 2, placement: where, who, what, how much; RAG as a placement aid (`layer2-placement`).
  3. Level 3, organization: independence, stated status, track record, seeded errors (`layer3-organization`).
  4. The five questions before acting.
- **Keys in:** everything above.
- **Keys out:** the three levels; seeded-error measurement.
- **Notable blocks:**
  - *Étude de cas*: threat image projection in airport screening; mutation testing.
  - *Nuance*: seeded errors measure only imaginable errors.
  - The register of recommendations follows D16 (still open).

#### Conclusion — La méthode appliquée à elle-même
- **Purpose:** apply the book's principles to the book.
- **Content:**
  - a status table of P1–P5 and the main claims;
  - an inventory of open tensions;
  - what would weaken the scaffold;
  - the book's own provenance and comparators (where its claims could fail differently);
  - closing on the working stance: subjective expected, *faute de mieux*.

### Appendices
- **A.** Outils de référence: consolidated primers (logic, probability, variance, reliability, SEU, contracts, signalling).
- **B.** Glossaire: generated from the register.
- **C.** Notation.
- **D.** Paramètres des exemples quantitatifs: canonical parameter sets.

Plus the bibliography and an index.

---

## 3. Quantitative Examples (spiral map)

| Id | First appearance | Return | Mechanism shown | Canonical parameter sets (initial, from the labs; to be frozen in `parametres.py`) |
| :-- | :-- | :-- | :-- | :-- |
| **seu-a / seu-b** | ch. 4 (baseline) | ch. 17 (omitted factor z, buffer b) | threshold p∗; deciding on belief while the world holds its own odds | L/ΔU = 25 (p∗ ≈ 3.85 %); Mr Y p = 0.1 %; Mr X p = 5 %; crack z = 8 %; buffer b = 4 %; roulette L/ΔU = 10 000, p = 0.001 %, z = 1/6 |
| **log-score** | ch. 3 | — | one outcome barely grades a forecaster | p = 5 % vs 0.1 %; breaks: ratio 50; holds: ≈ 0.95 |
| **chain-a / chain-b** | ch. 8 | ch. 14 (agent trajectory) | series vs parallel; a shared factor passes every check of the same kind | N = 4, p = 6 %, q ∈ {0, 3 %}; ch. 14: N up to 12 |
| **escape-a / escape-b** | ch. 9 | ch. 16 (shared models) | PPV, uptake, escape, risk; common mode vs precision | peers: P(wrong) = 10 %, c = 10 %, m = 20 %, f = 5 %; shared: 2 %, 60 %, 20 %, 5 %; precise: f = 0.5 %; independent and precise: 2 %, 10 %, 10 %, 0.5 % |
| **plausibility** | ch. 12 | — | guessing errors scatter, consistent errors repeat; severity of a 5-sample check | three modes (known, arbitrary, misconception) with the lab's answer distributions |
| **teaser** | ch. 0 | ch. 9 | the more accurate producer can be the riskier system | 1 % × 90 % vs 10 % × 1 % |

---

## 4. Running Examples (initial register)

| Example | Appears in | What each appearance adds |
| :-- | :-- | :-- |
| Sailboats, Mr X and Mr Y | 0, 3, 4, 17 | forecast vs forecaster → SEU threshold → omitted factor and buffer |
| Boiling water | 1, 2, 5 | hidden conditions → frame → unrecorded constant factor |
| The bracket (ferrure) | 5, 7, 8, 18 | safety factor in-frame → common-mode self-check → comparator table → corrosion specialist seeding errors |
| Mars Climate Orbiter | 0, 8, 10, 12 | hook → units laundered at an interface → address and contract tiers → definable but silent |
| The turkey | 3, 5, 13 | weak evidence from uneventful mornings → ontological uncertainty → silent cell outside the frame |
| Challenger | 5, 6 | not a pure frame failure → read through the five conditions |
| 70 % rain forecast | 3, 17 | calibration → calibrate vs gate; directive vs information |
| BCG field experiment | 11, 12 | reach → jagged frontier |
| Mata v. Avianca / METR | 0, 11 / 0, 15 | hook → fluent and wrong / hook → the lost tell |

---

## 5. Reading Paths (for Chapter 0)

| Path | Chapters | Notes |
| :-- | :-- | :-- |
| L'argument principal (the core argument) | 0, 2, 5, 6, 7, 10, 11, 13, 16, 18, Conclusion | |
| Voiliers, eau bouillante et mondes possibles | 0, 1, 2, 3, 4, 5, 17 | |
| L'ingénieur | 0, 2, 5, 7, 8, 10, 13, 18 | |
| Le statisticien et le mathématicien | 0, 1, 3, 5, 7, 9, 12 | |
| L'informaticien et le concepteur d'IA | 0, 8, 9, 10, 11, 12, 13, 14, 17 | |
| Le décideur et l'institution | 0, 4, 9, 15, 16, 17, 18 | |
| Le destinataire d'un chiffre sûr de lui | 0, 3, 4, 11, 15, 17 | |
| Parcours critique (tensions and limits) | 0, then the *Nuance* blocks of 5, 8, 9, 12, 13, 17, and the Conclusion | replaces the map's "amendments" path, which cannot exist in the monograph |

Readers on a path skip prerequisites. Each chapter therefore opens with its "keys in" stated in one or two lines, pointing back to the chapter that provides them.

> **TODO (2026-11-19): "Parcours critique" extended in chapter 0.**
> - **Change:** chapter 0 (`#tbl:ch00-parcours`) now also lists the *Nuance* blocks of **ch. 7** ("Portée réelle du conditionnement sur le cadre") and **ch. 16** ("Séparer la corrélation des causes et l'usure des alertes"). Both hold open tensions inventoried by the conclusion: salience omission and P3a; correlation of causes vs alarm fatigue.
> - **Outline:** the row above has not been updated yet. Add 7 and 16 to it once the change is approved.
> - **Possible building:** neither block is written to be read on its own.
>   - The ch. 7 block assumes P3 and the conditioning vector $x$.
>   - The ch. 16 block assumes PPV (ch. 9), the shared-cause share $c$, and the `escape-b` example just before it.
>   - Check whether a reader who jumps straight to these blocks can follow them. If not, add a one-line lead-in with back-references (and check the other blocks on this path the same way). Then decide whether the ch. 18 *Nuance* (seeded errors measure only imaginable errors), also used by the conclusion, should join the path.

---

## 6. Coverage Check (all 50 map threads)

| Part | Threads |
| :-- | :-- |
| I | `map-territory` 2 · `relevance-frame` 2 · `deduction-induction` 2 · `bayesian-judgment` 3 · `neither-right-nor-wrong` 3 · `seu-sailboat-roulette` 4 (and 17) |
| II | `aleatory-epistemic` 5 · `ontological-residue` 5 · `variance-disagreement` 5 · `within-frame-defenses` 5 · `five-conditions` 6 · `frame-common-cause` 7 · `limits-of-data` 7 · `meta-nfl` 7 · `two-routes-in` 7 · `independence-cost-curve` 8 · `series-vs-parallel` 8 · `uncertainty-laundering` 8 (and 14) · `divide-and-orchestrate` 8 (and 14) · `severity-bayes` 9 · `error-times-escape` 9 |
| III | `bits-to-composition` 10 · `design-by-contract` 10 · `front-loaded-verif` 10 · `failure-has-address` 10 · `spec-into-data` 11 · `next-token-scale` 11 · `plausibility-not-truth` 11 · `steering-not-spec` 11 · `three-flips` 12 · `layer-vs-output` 12 · `jagged-frontier-bcg` 12 · `kalai-vempala-tail` 12 · `two-axes-matrix` 13 · `four-sources` 13 |
| IV | `agentic-compounding` 14 · `friction-as-generator` 15 · `loss-of-the-tell` 15 · `signaling-collapse` 15 · `bainbridge-prompt-trap` 15 · `rate-vs-escape-shift` 16 · `same-lender` 16 · `provenance-laundering` 16 · `throughput-hollowing` 16 |
| V | `calibrate-vs-gate` 17 · `sandboxes-and-gates` 17 · `four-questions` 17 · `layer1-attitude` 18 · `layer2-placement` 18 · `layer3-organization` 18 |

All 50 are placed. Three appear twice by design: `seu-sailboat-roulette`, `uncertainty-laundering` and `divide-and-orchestrate`.

---

## 7. Points for Author Review Before the Content Spec

1. **Chapter count** (19 + conclusion) vs the ~15–18 target: keep, or merge 1 → 2–3 and/or 13 → 12?
2. **Proposed statuses of P1–P5** (§1): confirm or revise (D8).
3. **Laundering defined in Part II** (ch. 8, engineering cases) rather than Part IV: this places it before the computing Part, which needs it (contracts left in prose, ch. 10).
4. **Escape probability introduced qualitatively in ch. 6** and quantified in ch. 9, because P2's formal note and P5 already use it.
5. **The "Parcours critique" reading path** replaces the map's amendments tour.
6. **Proposed French chapter titles:** working titles, open to change.
