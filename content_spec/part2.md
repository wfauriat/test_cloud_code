# Content Spec — Part II: Ce qui peut nous détromper (ch. 5–9)

Read `00_global.md` first (statements §3, models §4, parameters §7).

**Part page:** what can tell us, in time, that we are wrong. Ground every chapter in non-AI cases: bracket and corrosion, *Challenger*, medical screening, Knight & Leveson, multiphysics chains. Part II reads as general reliability of reasoning, not as a delayed AI argument. **This Part carries the book's formal core (M1, M3); state assumptions explicitly.**

---

## Chapter 5 — Trois incertitudes, et ce que mesure une barre d'erreur (~15–18 pages)

**Argument step:** S5. **Keys in:** ch. 1–3. **Source threads:** `aleatory-epistemic`, `ontological-residue`, `variance-disagreement`, `within-frame-defenses`. The arXiv article's section "Three kinds of uncertainty" is citable.

**Sections:**
1. *Boîte à outils*: **the law of total variance**, Var(Y) = E_θ[Var(Y | θ)] + Var_θ(E[Y | θ]), stated over an admitted set Θ.
2. **Aleatory vs epistemic, a modelling choice.** Scatter treated as irreducible vs lack of knowledge reducible by data. The die throw measured or not. Where to stop refining is the analyst's decision.
3. **Ontological uncertainty.**
   - Doubt about whether the frame's variables fit at all (Wynne; Walker et al.; Lempert; Knight).
   - The inductivist turkey, with Russell's chicken noted.
   - Pre-2008 mortgage models: no wide interval on nationally correlated defaults, because the coupling was absent from the frame.
4. **Error bars measure disagreement: P1.**
   - State **P1** (`prop:desaccord`) with its status.
   - Justification: every spread is computed within an admitted ensemble.
   - A varying unrecorded factor appears as unattributed scatter; a constant one leaves no trace.
   - The committee reading the same incomplete note.
   - Ontological uncertainty is not a third quantity awaiting a formula; it is what all admitted alternatives are silent about.
5. **Why robustness tools stay inside.**
   - Safety factors, prior sensitivity, Bayesian model averaging, out-of-distribution scores: indispensable within scope.
   - The bracket with a margin of 1.8 in a corrosive atmosphere absent from the model.
   - Treating bounded robustness as pricing the frame is the risk.

**Blocks:**
- *Noyau formel*: both terms of the decomposition are averages over Θ, so a hypothesis outside Θ has zero weight in both.
- *Étude de cas*: the pre-2008 mortgage risk models.
- *Nuance* (`.nuance`): *Challenger* is easy to read as a pure frame failure, but the record is mixed. The chart examined the night before showed only flights with O-ring damage, hiding the temperature trend that all 23 earlier flights reveal: a frame problem in the data. Engineers who objected were overruled: an uptake problem. Forward link to ch. 6.
- *Nuance* on P1's robustness (global §3).
- *Question*: which of your uncertainties are computed over an explicit admitted set, and what does that set exclude?

**Figures:** a schematic of the three uncertainties as nested regions (inside Θ: aleatory, epistemic; outside: ontological); the bracket's design-load margin.

**Keys out:** the three kinds of uncertainty; admitted set; **P1**.

**Points clés (intended):**
- Aleatory and epistemic are modelling choices.
- Ontological doubt bears on the frame itself.
- Every error bar measures disagreement within an admitted set.
- What the frame omits leaves no bar, at most unattributed scatter.
- Robustness tools widen alternatives without leaving the frame.

---

## Chapter 6 — Détecter une erreur : comparateurs et cinq conditions (~12–15 pages)

**Argument step:** S6. **Keys in:** ch. 5. **Source threads:** `five-conditions`; the comparability material of `uncertainty-laundering` is announced only.

**Sections:**
1. **Claim, check, comparator.** Define **affirmation**, **contrôle**, **comparateur** (`def:affirmation`, `def:controle`, `def:comparateur`), with everyday and technical examples. A comparator can be another claim, a statement fixed in advance, or an observation of the world (announces the four sources, ch. 13).
2. **P2 and the five conditions.**
   - State **P2** (`prop:comparateur`) as near-definitional.
   - Unfold the five conditions: existence, difference (*se tromper autrement*), comparability (same quantity, conditions stated), timeliness, uptake (`def:prise-en-compte`).
3. **Escape.** Define **taux d'erreur** and **probabilité d'échappement** (`def:echappement`) qualitatively: if any condition fails for a class of errors, their escape probability is 1. Quantified in ch. 9.
4. ***Challenger* through the five conditions.** Difference and comparability failed in the data; uptake failed in the room.
5. **What agreement and disagreement show.** A disagreement shows that at least one side is wrong, not which. An agreement shows nothing unless the comparator could have disagreed (announces severity, ch. 9).

**Blocks:**
- *Noyau formel*: if any condition fails, P(detected | wrong) = 0 for the errors concerned.
- *Étude de cas*: *Challenger* (Rogers Commission; Tufte).
- *Question*: before acting on your next claim, what is its comparator, and which of the five conditions is weakest?

**Figures:** the five conditions as a pipeline of gates, any one of which lets the error through.

**Keys out:** claim, check, comparator, failing differently, uptake, error rate, escape probability (qualitative), **P2**.

**Points clés (intended):**
- Detection is a registered disagreement.
- Five conditions must all hold.
- Any failed condition sends the escape probability to 1.
- Agreement is evidence only if disagreement was possible.

---

## Chapter 7 — Le cadre, cause commune de nos contrôles (~15–18 pages)

**Argument step:** S7. **Keys in:** ch. 2, 5, 6. **Source threads:** `frame-common-cause`, `limits-of-data`, `meta-nfl`, `two-routes-in`. The arXiv article's section "The meta-level no-free-lunch" is citable.

**Sections:**
1. *Boîte à outils*: **common-mode failure.** Two backup pumps on one power supply.
2. **P3a: the frame as common cause.**
   - Self-checks (re-derivation, re-run, resample) catch slips.
   - No comparator computed inside the frame can detect an error caused by an omitted factor; with respect to that factor, all internal checks are copies of one another.
   - The bracket: finite elements vs a hand calculation with the same idealizations agree to three decimals, and both ignore corrosion.
   - State **P3** (`prop:cause-commune`), part (a).
3. **P3b: when observations catch frame errors.**
   - Observations come from the world, so they *can* carry an omitted factor's imprint, but only if it varied during collection, and only through recorded variables, as unexplained scatter.
   - Distribution shift (*dérive de distribution*).
   - Google Flu Trends.
   - Dry-lab load tests vs five years in salt air.
   - The wire-colour agent.
4. **The meta-level regress.**
   - A procedure to audit frames is itself a finite frame.
   - The no-free-lunch theorems (Wolpert & Macready) as a formal shadow.
   - Hume on induction; Goodman's "vert/vleu".
   - "Better methodology" defers the framing choice; it never derives it from nowhere.
5. **How new relevance enters.**
   - Being told (another witness, another discipline, an adversarial reviewer); finding out (exploration, Sutton & Barto).
   - Being told is finding out at second hand.
   - Exploration is not free: explore where it is cheap, reversible and guided by some intuition (forward link to sandboxes, ch. 17).

**Blocks:**
- *Noyau formel* **M3** (global §4): the likelihood-ratio-equals-1 argument with its conditioning assumption explicit.
- *Nuance*: conditioning on x is idealized. Learned models can represent a factor without mobilizing it (forward link to ch. 12, salience omission).
- *Étude de cas*: Google Flu Trends (Lazer et al., 2014).
- *Question*: when did your model class or problem formulation last change fundamentally, and did the trigger come from an internal metric, an outside critic or a field failure?

**Figures:** a diagram of claim and comparator both downstream of x, with z acting on the outcome only (a causal sketch).

**Keys out:** common-mode failure; **P3**; distribution shift; the regress; the two routes in.

**Points clés (intended):**
- Self-checks catch slips, not omissions.
- The frame is a common cause of every check computed from it.
- Data reveal an omitted factor only if it varied, and only as scatter.
- No meta-procedure escapes the regress.
- New relevance comes from outside: told or found.

---

## Chapter 8 — Indépendance, chaînes et contrôles croisés (~18–22 pages)

**Argument step:** S8. **Keys in:** ch. 6–7. **Source threads:** `independence-cost-curve`, `series-vs-parallel`, `uncertainty-laundering` (engineering side), `divide-and-orchestrate` (engineering side).

**Sections:**
1. *Boîte à outils*: **series and parallel reliability.** A series system fails if any part fails; a parallel system fails only if all fail; the effect of correlated failure.
2. **Blind spots.** Define **angle mort** (`def:angle-mort`): the set of error causes a component cannot register.
3. **Independence and its cost: P4.**
   - State **P4** (`prop:independance`).
   - Independence is relative to a class of errors and pulls against comparability: a copy is perfectly comparable and useless; an incommensurable view may see what you missed but cannot make its objection land.
   - The comparator table (Markdown table, label `tbl:ch08-comparateurs`), ordered by what each comparator shares with the claim, from the same computation with a new seed to another discipline, with a cost line.
   - The bracket placed on the table (second run at the top; a colleague's model in the middle; an aged-part load test or a corrosion specialist at the bottom).
   - Knight & Leveson's 27 versions; Levins' "intersection of independent lies" (with Orzack & Sober; Wimsatt).
4. **Composing steps.** Multiphysics chains (thermal → structural → materials). Complex goals are met by assembling modules, and the higher the goal, the less it can be stated formally.
5. **Chains vs cross-checks: P5.**
   - State **P5** (`prop:chaines`) with **M1**: the chain contains every component's blind spot plus interface errors; the cross-check reduces to what both share.
   - A model reviewing its own output looks like a cross-check on the diagram, and is a copy with respect to its own blind spot.
6. **Laundering at handoffs.**
   - Define **blanchiment** (`def:blanchiment`).
   - A thermal field passed as a bare array leaves the next link nothing to compare with.
   - Eight significant digits after five stages.
   - Orbiter: impulse values crossed an interface as bare numbers, with the unit only in a prose document.
   - Laundering is a failure of comparability at every link.
   - Two cousins: dropping units or definitions (comparability again); dropping provenance (independence can no longer be judged; forward link to ch. 16).

**Blocks:**
- *Noyau formel* **M1**: B_chain ⊇ ∪B_i ∪ B_interfaces; B_check = B₁ ∩ (B₂ ∪ B_cmp); P(escape) = Π m_i under independence; = 1 for a shared cause.
- *Exemple quantitatif* **chain-a**:
  - **mise en place:** N steps, per-step error p = 6 %, a peer as competent as the producer, a shared omitted factor q;
  - **figure:** failure probability vs N, for the unchecked chain and the cross-checked chain, with q = 0 and q = 3 %;
  - **calcul:** the N = 4 rows of global §7;
  - **lecture:** cross-checking crushes the independent part; with q = 3 %, the shared factor causes 68 % of the residual failures, and more checks of the same kind cannot touch it.
- *Nuance*:
  - the corrected comparison term;
  - the trade-off suggests, but does not derive, an optimal reviewer distance;
  - "cost rises with independence" is a tendency (cheap-and-different comparators exist).
- *Étude de cas*: Knight & Leveson (1986).
- *Question*: at the handoffs in your workflow, do results travel with their assumptions, units, uncertainty and origin?

**Keys out:** blind spot; **P4**; **P5**; chain and cross-check; laundering; producer and checker.

**Points clés (intended):**
- Independence is always relative to a class of errors.
- It is paid for in comparability.
- Chains unite blind spots; cross-checks intersect them.
- Laundering makes compositions into chains.
- Checks of the same kind cannot touch a shared cause.

---

## Chapter 9 — Sévérité, fausses alertes et probabilité d'échappement (~16–20 pages)

**Argument step:** S9. **Keys in:** ch. 1, 6, 8. **Source threads:** `severity-bayes`, `error-times-escape`.

**Sections:**
1. *Boîte à outils*: **base rates and PPV.** The screening example: prevalence 1 %, sensitivity 90 %, false-positive rate 5 % give PPV = 15.4 %. Most positives are false when the condition is rare.
2. **Severity.**
   - Define **sévérité** (`def:severite`, Mayo).
   - Agreement multiplies the odds by P(agree | right)/P(agree | wrong); if the comparator would have agreed anyway, the ratio is 1, and the check adds a signature, not evidence.
3. **The false-alarm trap.**
   - A producer wrong 1 % of the time and a reviewer wrong 10 %, independent: 91.7 % of their disagreements are cases where the producer was right.
   - As producers improve, a fixed checker's alarms become mostly false.
   - The PPV formula; 1/PPV investigations per real error caught.
4. **What people do with alarms.**
   - Probability matching and the cry-wolf effect (Bliss, Gilson & Deaton, 1995).
   - Bayes fixes PPV; behaviour decides uptake.
   - The theory's own answer to a disagreement is to resolve it with a third comparator, at a cost of 1/PPV per real error. Paying it is an expected-utility choice, nearly always worth it for one-shot, high-stakes acts (link back to ch. 4).
5. **Risk = error rate × escape probability.**
   - P(wrong and acted on) = P(wrong) × P(not contradicted in time | wrong).
   - Benchmarks, leaderboards and scaling curves measure the first factor; safety engineering and the frame argument concern the second.
   - The teaser revisited (0.9 % vs 0.1 %).
   - The two factors are not independent: as P(E) falls, alarms are more often false, which may lower uptake.

**Blocks:**
- *Noyau formel* **M1, checker model**: s, PPV, u, escape and risk (global §4), with assumptions stated.
- *Exemple quantitatif* **escape-a**:
  - **mise en place:** the *peers* preset (and *independent + precise* for contrast);
  - **figure:** escape probability and risk vs P(E) for a fixed checker, under both policies (heeded at PPV vs every flag investigated);
  - **calcul:** the corresponding rows of global §7;
  - **lecture:** precision keeps flags worth reading; independence widens what the checker can see; uptake is the hidden lever.
- *Nuance*: falling error rates do not erode uptake "by Bayes alone".
- *Question*: what share of your checker's alarms are real, and how are they treated?

**Keys out:** severity; base rate; PPV; probability matching; the error × escape decomposition; the checker model.

**Points clés (intended):**
- A pass counts only if failure was possible.
- Rare errors make most alarms false.
- Uptake is behaviour, not arithmetic.
- Risk is the product of error rate and escape probability, and only the first is routinely measured.
