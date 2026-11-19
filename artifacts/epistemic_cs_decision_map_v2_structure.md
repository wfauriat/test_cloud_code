# Epistemic CS Decision Map (v2) — Structure & Reference

> **Root (`root`):** **Acting Through a Picture**  
> *Core thesis:* We act on a finite picture of the world, and the world answers the action, not the picture. One argument across four territories: how a frame bounds every inference, how classical software earned guarantees that learned models give up, what automation does to error detection, and what can still tell us we are wrong in time.

**Scale:** 4 Territories (2 left, 2 right) · 12 Angles (3 per territory) · 50 Threads · 5 Propositions · 29 Glossary Terms · 8 Guided Paths · 4 Interactive Labs · 6 Sources

---

## 1. Visual Hierarchy at a Glance

```
                         ┌─────────────────────────────────────┐
                         │   Acting Through a Picture (root)   │
                         └──────────────────┬──────────────────┘
                 ┌──────────────────────────┴──────────────────────────┐
           [LEFT SIDE]                                           [RIGHT SIDE]
   ┌─────────────┴─────────────┐                         ┌─────────────┴─────────────┐
   ▼                           ▼                         ▼                           ▼
1. Epistemics &          2. Computing stack        3. Automation &          4. Decisions, risk
   the frame                & the AI inversion        chains                   & checks
   (3 angles, 13)           (3 angles, 12)            (3 angles, 12)           (3 angles, 13)
   ├─ Constructed picture   ├─ Earned silence          ├─ Chains & laundering   ├─ One-shot decisions
   ├─ Three uncertainties   ├─ The ML inversion        ├─ Erosion of checks     ├─ Theory of checks
   └─ No self-audit         └─ The regime flip         └─ Collective blind spots└─ Three-layer remedy
```

**Drawer legend on threads:** `⊢` Formal core · `→` Concrete case · `≈` Analogy · `▸` Interactive lab · `!` The catch · `Δ` Amended (`CR`/`RV`) · `?` Diagnostic question  
**Source tags:** `TK` Talk draft · `FP` Frame Problem preprint · `WG` Where the Guarantees End · `FD` Failing Differently · *Proposed/unverified:* `CR` External critique · `RV` Review of critique & v1

---

## 2. Full Territory → Angle → Thread Breakdown

### Territory 1: Epistemics & the frame (`epistemics` · side: left · 3 angles · 13 threads)
*What can be concluded from hypotheses and data: why deduction and induction both run inside a finite specification, why error bars cannot show what that specification omits, and why no reasoner can audit its own frame from within.*

#### 1.1 Reasoning inside a constructed picture (`picture` · `Constructed picture` · 5 threads)
*We never touch the world directly; we act on a simplified picture of what matters. The world does not consult the picture before answering.*

| ID | Thread Title | Core Gist | Sources | Drawers |
| :--- | :--- | :--- | :--- | :--- |
| `map-territory` | **The world answers the action, not the picture** | We decide on what we think might happen, never on what will happen; yet what we decide changes what happens. | `FP` `TK` | `≈` `→` `?` |
| `relevance-frame` | **Relevance, exceptions & the frame** | Before any inference runs (`A ∩ (…) → B`), a reasoner settles what matters: what to state vs. leave in the unstated background `(…)`. | `TK` `FP` | `⊢` `≈` `!` |
| `deduction-induction` | **Formality does not lift the limit** | Deductive necessity and inductive generalisation are both conditional on a frame; rigour inside a frame never certifies it. | `FP` `TK` | `⊢` `→` `!` |
| `bayesian-judgment` | **Possible worlds & probability as judgment** | Instead of chasing the single right answer, reason in reverse over what hides in `(…)` and weigh possible worlds. | `TK` `FP` | `!` `?` |
| `neither-right-nor-wrong` | **Neither right nor wrong: a forecast vs. a forecaster** | Before an event, two coherent forecasts (5% vs. 0.1%) are neither right nor wrong; one outcome barely grades them—only a track record does. | `TK` `FP` `FD` `RV` | `⊢` `→` `?` |

#### 1.2 Three uncertainties & measured disagreement (`three-uncertainties` · `Three uncertainties` · 4 threads)
*Quantitative methods price variability and parameter doubt inside a chosen model class. What the frame omits produces no disagreement, so no error bars.*

| ID | Thread Title | Core Gist | Sources | Drawers |
| :--- | :--- | :--- | :--- | :--- |
| `aleatory-epistemic` | **Aleatory vs. epistemic is a modelling choice** | Aleatory is scatter treated as irreducible; epistemic is what more data/modelling could shrink. The analyst chooses the split. | `FP` `FD` | `⊢` `!` |
| `ontological-residue` | **Ontological uncertainty: the turkey’s blind spot** | Doubt about whether the frame's variables, categories, and model class fit the problem at all (Knightian/deep uncertainty). | `FP` `TK` `RV` | `→` `!` `Δ` |
| `variance-disagreement` | **Error bars measure disagreement** | **Prop. 3:** Uncertainty summarises how far a specified set of alternatives disagree; an omitted factor produces no disagreement. | `FD` | `⊢` `≈` `!` |
| `within-frame-defenses` | **Why robustness tools and safety factors stay inside** | Sensitivity analysis, model averaging, OOD scoring, and safety factors widen alternatives inside one shared frame. | `FP` `FD` | `→` `!` |

#### 1.3 The impossibility of self-audit (`self-audit` · `No self-audit` · 4 threads)
*A reasoner cannot audit its own frame from within, and no second-order procedure dissolves the regress. New relevance enters only from outside.*

| ID | Thread Title | Core Gist | Sources | Drawers |
| :--- | :--- | :--- | :--- | :--- |
| `frame-common-cause` | **The frame is a common cause (Proposition 2a)** | Every check computed from a reasoner's own frame shares that frame (common-mode failure) and is blind to what it omits. | `FD` `CR` | `⊢` `≈` |
| `limits-of-data` | **When observations catch frame errors (Proposition 2b)** | Held-out data/cross-validation register an omitted factor only if it varied during collection and moved something recorded. | `FD` `WG` | `→` `≈` |
| `meta-nfl` | **The meta-level no-free-lunch** | A second-order procedure to audit frames is itself a finite frame (Wolpert-Macready NFL, Hume, Goodman). | `FP` | `⊢` `!` |
| `two-routes-in` | **How new relevance enters a frame** | Only from outside: (1) *being told* by another witness/frame, or (2) *finding out* by acting on and running into the world. | `FP` `FD` | `!` `?` |

---

### Territory 2: Computing stack & the AI inversion (`stack` · side: left · 3 angles · 12 threads)
*How classical computing built reliable silence out of explicit contracts checked in advance, and what changes when machine learning moves the specification into the data.*

#### 2.1 How the stack below earned its silence (`earned-silence` · `Earned silence` · 4 threads)
*From voltages to databases, classical computing scales because each layer exposes an explicit, checkable contract.*

| ID | Thread Title | Core Gist | Sources | Drawers |
| :--- | :--- | :--- | :--- | :--- |
| `bits-to-composition` | **From dumb determinism to deep composition** | Deterministic operations scale to OSes and flight controllers because each layer hides complexity behind an exact promise. | `WG` | `≈` |
| `design-by-contract` | **Every layer is a stated contract** | **Stated components** expose pre/postconditions (`{P} C {Q}`): written in advance, readable, disputable, versionable, violable. | `WG` `FD` | `⊢` `!` |
| `front-loaded-verif` | **Front-loaded verification: check the layer once** | Written contracts allow types, tests, fuzzing, and proofs to check the component *once* before deployment for all future runs. | `WG` `FD` | `≈` |
| `failure-has-address` | **Definable divergence: failures have an address** | Classical failures contradict a stated or statable rule (e.g., Mars Climate Orbiter). *Amended:* enforced vs. written vs. unwritten tiers. | `WG` `CR` `RV` | `→` `Δ` `?` |

#### 2.2 The machine-learning inversion (`ml-inversion` · `The ML inversion` · 4 threads)
*For seventy years software stopped where our ability to write explicit rules stopped. Machine learning crosses that wall by moving the specification into the data.*

| ID | Thread Title | Core Gist | Sources | Drawers |
| :--- | :--- | :--- | :--- | :--- |
| `spec-into-data` | **The specification moves into the data** | **Learned components** replace written rules with examples + optimisation: buying *reach*, spending the *guarantee* and *legibility*. | `WG` `FD` | `≈` `!` |
| `next-token-scale` | **The next-token engine** | Next-token prediction at scale builds grammar, facts, and reasoning (observable via *logit lens*) only where it lowers prediction error. | `WG` | `→` `!` |
| `plausibility-not-truth` | **Fluent and wrong, as designed** | Plausibility is the objective; a fluent falsehood breaks no contract (*Mata v. Avianca*; *Δ* notes *Moffatt v. Air Canada* wasn't proven GenAI). | `WG` `RV` | `→` `Δ` `!` |
| `steering-not-spec` | **Steering is not specification** | System prompts, RLHF, guardrails, and benchmarks shift distributions/tendencies (subject to Goodhart's law); they do not state invariants. | `WG` | `≈` `!` |

#### 2.3 The regime flip at the top layer (`regime-flip` · `The regime flip` · 4 threads)
*Between the classical middle of the stack and its learned top, three properties flip together, and with them what verification can in principle do.*

| ID | Thread Title | Core Gist | Sources | Drawers |
| :--- | :--- | :--- | :--- | :--- |
| `three-flips` | **Three properties flip together** | Contract → tendency; definable divergence → uniform fluency; address in code → training distribution (no patch merges into a distribution). | `WG` `RV` | `!` `Δ` |
| `layer-vs-output` | **Verifying the layer vs. checking outputs one by one** | Because a general-purpose LLM is compositional and lacks a spec, once-for-all layer verification disappears; outputs must be checked individually. | `WG` | `?` |
| `jagged-frontier-bcg` | **The jagged competence frontier** | Competence boundaries are uneven (BCG study: +40% quality inside, −19 pp just outside). *Δ:* structural vs. salience omission. | `WG` `CR` `RV` | `→` `Δ` `!` |
| `kalai-vempala-tail` | **Calibration, the long tail & consistent errors** | Generative calibration forces hallucinations at ≥ Good–Turing monofact rate. Re-runs catch guessing (semantic entropy), not consistent errors. | `WG` `FD` `CR` `RV` | `⊢` `▸` `Δ` `!` |

---

### Territory 3: Automation & chains (`automation` · side: right · 3 angles · 12 threads)
*How complex goals are assembled from chains of simpler steps, how chaining launders uncertainty, and what automation removes from individual and collective error detection.*

#### 3.1 Chains, cross-checks & laundering (`chains-laundering` · `Chains & laundering` · 4 threads)
*Complex goals are reached by passing results from one model or step to the next. How the steps are wired decides whether blind spots add up or cancel.*

| ID | Thread Title | Core Gist | Sources | Drawers |
| :--- | :--- | :--- | :--- | :--- |
| `divide-and-orchestrate` | **Complex goals as orchestrated sequences** | Multiphysics and AI pipelines split high-level unformalizable goals into local steps, passing intermediate outputs rapidly. | `FP` `FD` | `≈` |
| `series-vs-parallel` | **Chains vs. cross-checks (Proposition 5)** | Chains unite blind spots (`B_chain ⊇ ∪B_i ∪ B_interfaces`); cross-checks intersect them (`B_1 ∩ (B_2 ∪ B_cmp)`). Self-review is a near-copy. | `FD` `CR` `RV` | `⊢` `▸` `Δ` `!` |
| `uncertainty-laundering` | **Laundering at handoffs** | Dropping a claim's conditions, units, uncertainty, or provenance at handoffs turns conditional estimates into bare, uncheckable facts. | `FP` `FD` `CR` `RV` | `→` `Δ` `?` |
| `agentic-compounding` | **Agents as multi-step chains** | Tool-calling loops create *N*-link chains where the least-guaranteed layer executes state-changing actions (cf. Knight Capital). | `FD` `WG` | `→` `!` |

#### 3.2 The silent erosion of human checks (`human-erosion` · `Erosion of human checks` · 4 threads)
*Slow analysis produced checks as a by-product of effort. One-step generation removes both the checks the analyst used to make along the way and the visible hesitation of a producer out of its depth.*

| ID | Thread Title | Core Gist | Sources | Drawers |
| :--- | :--- | :--- | :--- | :--- |
| `friction-as-generator` | **Friction had a function: it generated comparators** | Slow step-by-step work built expectations and intermediate cross-checks; one-step generation silently deletes those comparators. | `FP` `FD` | `≈` |
| `loss-of-the-tell` | **The lost tell & the METR sign error** | LLMs erase human hesitation/hedging ("tells") and warp judgment (METR trial: devs measured 19% slower, felt 20% faster). | `FD` `WG` | `→` `!` |
| `signaling-collapse` | **When polish stops failing differently from substance** | Form and substance used to share understanding as a cause; free polish pools checked & unchecked work (Spence/Akerlof collapse). | `FD` `CR` `RV` | `≈` `Δ` |
| `bainbridge-prompt-trap` | **Bainbridge’s irony & the two prompt traps** | Automation erodes operator skill; using a model to check fails when prompts transmit the frame and sycophancy training favours agreement. | `FD` | `?` |

#### 3.3 Collective epistemics & shared blind spots (`collective-epistemics` · `Collective blind spots` · 4 threads)
*When a whole community adopts the same models, individual error rates fall while the errors that remain become correlated across authors and reviewers.*

| ID | Thread Title | Core Gist | Sources | Drawers |
| :--- | :--- | :--- | :--- | :--- |
| `rate-vs-escape-shift` | **Error rate falls, escape probability rises** | Shared models cut individual errors (`P(wrong)`) but correlate remaining blind spots across authors & reviewers, raising `P(escape)`. | `FD` `CR` `RV` | `⊢` `Δ` `!` |
| `same-lender` | **One lender for all borrowers** | A foundation model is "being told" industrialised into one store: useful against a borrower's slips, useless against the lender's blind spots. | `FD` | `≈` |
| `provenance-laundering` | **Pollution of the epistemic commons** | Unmarked model output re-entering the web/literature creates fake independent witnesses and recursive model collapse (Shumailov et al.). | `CR` `RV` | `!` |
| `throughput-hollowing` | **The institutional throughput squeeze** | Generation is nearly free while checking stays costly; organisations fund generation and starve evaluative capacity. | `FP` `WG` | `?` |

---

### Territory 4: Decisions, risk & checks (`decisions` · side: right · 3 angles · 13 threads)
*How uncertain pictures turn into one-shot decisions with real stakes, what it takes to detect an error in time, and the three layers of a remedy.*

#### 4.1 Deciding on a picture: one-shot stakes (`seu-oneshot` · `One-shot decisions` · 5 threads)
*What we believe decides what we do. When one action carries a catastrophic downside, going ahead requires a failure probability you can justify calling tiny.*

| ID | Thread Title | Core Gist | Sources | Drawers |
| :--- | :--- | :--- | :--- | :--- |
| `seu-sailboat-roulette` | **The sailboat race & Russian roulette** | Under Savage's SEU, a risky act pays iff `p < p∗ = ΔU/(ΔU + L)`. Omitted risk cannot enter `p` directly; only a deliberate humility buffer can. | `TK` `RV` | `⊢` `▸` `→` `Δ` `?` |
| `error-times-escape` | **Risk = error rate × escape probability** | `P(wrong & acted on) = P(wrong) · P(¬contradicted in time | wrong)`. Benchmarks measure the first; safety depends on the second. | `FD` `CR` | `⊢` `▸` `!` |
| `calibrate-vs-gate` | **Calibrate where repeatable; gate where one-shot** | Calibration works over large populations of repeatable trials; irreversible one-shot acts require an independent pre-action **gate** + buffer. | `FD` `WG` | `≈` `!` |
| `sandboxes-and-gates` | **Sandboxes and gates: an architecture for exploration** | Actions are questions to the world: explore freely in reversible **sandboxes**; place **gates** wherever real-world cost/irreversibility begins. | `FD` `WG` | `→` |
| `four-questions` | **Receiving a confident number** | Non-experts can audit claims via 4 questions (conditions, sensitivities, likeliest error, unmodelled factors); demands institutional capacity. | `FP` `FD` | `→` `!` `?` |

#### 4.2 The theory of checks & the two-axis map (`theory-of-checks` · `Theory of checks` · 4 threads)
*An error is detected only when a claim meets a comparator that was expected to agree, could fail differently, and is heeded in time.*

| ID | Thread Title | Core Gist | Sources | Drawers |
| :--- | :--- | :--- | :--- | :--- |
| `five-conditions` | **Proposition 1 & the five conditions of detection** | Detection requires a comparator and 5 conditions: **Existence**, **Difference**, **Comparability**, **Timeliness**, and **Uptake**. | `FD` `RV` | `⊢` `→` `!` |
| `severity-bayes` | **Severity & the false-alarm trap** | A passing check is evidence only by Mayo's *severity*; as errors get rarer, fixed checkers drop in PPV, causing "cry-wolf" uptake collapse. | `FD` `CR` `RV` | `⊢` `Δ` `!` |
| `independence-cost-curve` | **Independence is paid for in comparability (Proposition 4)** | Independence is relative to error classes and trades off against comparability; cost tends to rise with independence (with cheap bargains). | `FD` `RV` | `→` `≈` `Δ` |
| `two-axes-matrix` | **Two axes instead of three kinds** | Cross *Cause* (inside vs. outside frame) × *Signal* (signalled vs. silent). You can't shift rows from inside; you shift columns by adding comparators. | `FD` `CR` `RV` | `⊢` `Δ` `?` |

#### 4.3 Four sources & the three-layer remedy (`three-layer-remedy` · `Three-layer remedy` · 4 threads)
*Where comparators come from, what automation does to each source, and how attitude, placement and organisation combine into one defence.*

| ID | Thread Title | Core Gist | Sources | Drawers |
| :--- | :--- | :--- | :--- | :--- |
| `four-sources` | **Four sources of comparators** | (1) Advance statement, (2) Own checks, (3) Another reasoner, (4) The world. Generation helps mechanical verification, not physical validation. | `FD` `CR` `RV` | `→` `Δ` |
| `layer1-attitude` | **Layer 1: attitude, comparators you supply yourself** | Humility is the *first* comparator: pre-model estimates, pre-mortems, deliberately widened worlds/buffers. Necessary, never sufficient. | `FD` `FP` `TK` | `!` |
| `layer2-placement` | **Layer 2: placement, where, who, what, how much** | Place checks at *regime boundaries*, staffed by people reading *one layer below*, checking both *output* and *picture*, sized to stakes. | `WG` `FD` | `→` `!` |
| `layer3-organization` | **Layer 3: organisation, independence, status, measurement** | Cap output to review capacity, mandate claim status disclosure, track forecasts vs. outcomes, and measure escape with *seeded errors*. | `FD` `WG` `CR` `RV` | `Δ` `?` |

---

## 3. Core Theoretical Frameworks & Propositions

### The Five Propositions (`PROPS`)
1. **Detection needs a comparator** (`five-conditions`) — An error is detected only when a claim is compared with something expected to agree with it, and the two disagree.
2. **The frame is a common cause** (`frame-common-cause`, `limits-of-data`) — *(2a)* A comparator computed from the frame's own content cannot detect an error caused by a factor the frame omits. *(2b)* Observations can, only if that factor varied while they were taken, and only through what the frame records.
3. **Uncertainty is measured disagreement** (`variance-disagreement`) — A quantitative statement of uncertainty summarises how far the members of a specified set of alternatives disagree; an omitted alternative contributes none.
4. **Independence is relative, and paid for in comparability** (`independence-cost-curve`) — A comparator helps against a class of errors to the extent their cause affects it differently. What claim and comparator share, neither can check in the other; and they must share something to be compared.
5. **Chains unite blind spots; cross-checks intersect them** (`series-vs-parallel`) — In a chain the blind spot contains every component's, plus errors born at interfaces; in a cross-check it shrinks to what both share, under perfect comparison and uptake.

### Key Matrices & Taxonomies

| Framework | Dimensions / Elements | Anchor Thread |
| :--- | :--- | :--- |
| **Three Regime Flips** | 1. *Promise:* Contract → Statistical tendency<br>2. *Failure presentation:* Definable divergence → Uniform fluency<br>3. *Post-mortem target:* Address in code/interface → Training distribution | `three-flips` |
| **Five Conditions of Detection** | 1. **Existence** (comparator exists) · 2. **Difference** (fails differently) · 3. **Comparability** (shared quantity + stated conditions) · 4. **Timeliness** (before action) · 5. **Uptake** (registered & acted on) | `five-conditions` |
| **Two-Axis Error Matrix** | **Inside frame + Signalled:** test failure, crash, residual<br>**Inside frame + Silent:** fluent wrong answer, laundered chain *(ML crowds here)*<br>**Outside frame + Signalled:** anomaly, outsider objection, drift alarm<br>**Outside frame + Silent:** turkey's last morning, unmodelled scenario | `two-axes-matrix` |
| **Four Comparator Sources** | 1. *Stated in advance* (specs, proofs, Simplex monitors)<br>2. *Your own checks* (pre-run expectations, friction)<br>3. *Another reasoner* (peers, models, other disciplines)<br>4. *The world* (compilers/tests vs. physical experiments) | `four-sources` |
| **Three-Layer Remedy** | **Layer 1 (Attitude):** self-made comparators, pre-mortems, humility buffer<br>**Layer 2 (Placement):** at regime boundaries, reviewers reading 1 layer below, output + picture checks<br>**Layer 3 (Organisation):** cap output to review capacity, mandatory status tags, track records, seeded-error audits | `layer1-attitude` `layer2-placement` `layer3-organization` |
| **Four Questions for a Number** | 1. Under what conditions does this hold? · 2. What would change the number? · 3. What is the most likely way this is wrong? · 4. What was deliberately not modelled? | `four-questions` |
| **Five Questions Before Acting** | 1. What is the comparator? · 2. How can it fail differently? · 3. Are conditions stated? · 4. Does comparison precede action? · 5. Who has to listen, and will they? | `layer3-organization` |

---

## 4. Vocabulary & Concepts

### A. Formal Glossary (`GLOSSARY` — 29 terms)

| Term | Definition | Anchor |
| :--- | :--- | :--- |
| **Aleatory, epistemic, ontological** | Variability treated as irreducible; doubt that more data or modelling could reduce; doubt about whether the frame itself fits. | `ontological-residue` |
| **Blind spot** | The set of error causes a component (person, team, code, model) cannot register. | `series-vs-parallel` |
| **Calibration** | Stated probabilities match observed frequencies over many cases. Distinct from generative calibration (Kalai & Vempala). | `calibrate-vs-gate` |
| **Chain, cross-check** | Components in series, each taking the previous output as given; or in parallel, two bearing on one claim with disagreement registered. | `series-vs-parallel` |
| **Check** | A comparison between a claim and a comparator expected to agree with it. | `five-conditions` |
| **Claim** | Anything that asserts a matter of fact: a model output, a forecast, a measurement report. | `five-conditions` |
| **Common-mode failure** | Redundant protections failing together from a cause they share. | `frame-common-cause` |
| **Comparator** | Whatever a claim is compared with: another claim, a statement fixed in advance, or an observation of the world. | `five-conditions` |
| **Error rate** | The probability that a claim is wrong (`P(wrong)`). | `error-times-escape` |
| **Escape probability** | The probability that a wrong claim reaches an action without being contradicted in time (`P(¬contradicted in time | wrong)`). | `error-times-escape` |
| **Failing differently** | A comparator fails differently from a claim, for a given cause of error, when that cause does not make both wrong in the same way. | `independence-cost-curve` |
| **Frame** | The finite specification a reasoner works from: which variables, categories, model class, and objective count. Chosen before inference runs. | `relevance-frame` |
| **Front-loaded verification** | Checking a component once, against its statement, so that the check covers all future runs. | `front-loaded-verif` |
| **Jagged frontier** | The uneven, hard-to-predict boundary of a model's competence (Dell'Acqua et al., 2023). | `jagged-frontier-bcg` |
| **Laundering** | Dropping a claim's conditions at a handoff, so a conditional result arrives as an unconditional one. | `uncertainty-laundering` |
| **Learned component** | A component whose rules were fitted to examples and exist only as parameters. | `spec-into-data` |
| **Picture** | The constructed representation an agent acts on. The world answers the action, not the picture. | `map-territory` |
| **Possible worlds** | The situations compatible with what is known. A probability says how they are weighted. | `bayesian-judgment` |
| **PPV** | Positive predictive value: the share of a checker's alarms that are real errors. | `severity-bayes` |
| **RAG** | Retrieval-augmented generation: answering from documents fetched at query time, which a reviewer can open. | `layer2-placement` |
| **RLHF** | Reinforcement learning from human feedback: post-training a model on human preference judgements. | `steering-not-spec` |
| **Sandbox, gate** | An environment where actions have no outside effect; a point where an action waits for approval. | `sandboxes-and-gates` |
| **SEU, $p^*$** | Subjective expected utility (Savage): choose the act with best expected utility under your probabilities. $p^* = \Delta U / (\Delta U + L)$ is the failure probability above which the risky act stops paying. | `seu-sailboat-roulette` |
| **Severity** | A passing check is evidence only to the extent it would have failed had the claim been wrong (Mayo). | `severity-bayes` |
| **Signalled, silent error** | An error some comparator disagrees with; an error none does. | `two-axes-matrix` |
| **Stated component** | A component whose rules someone wrote, and which can be given a checkable specification: a contract. | `design-by-contract` |
| **Tell** | The visible sign of a producer's uncertainty: hesitation, hedging, rough form. | `loss-of-the-tell` |
| **Uptake** | Someone registers a disagreement and has the standing to act on it. | `five-conditions` |
| **Verification, validation** | Solving the stated problem right; stating a problem that represents reality well enough for the intended use. | `four-sources` |

### B. Additional Concepts, Mechanisms & Empirical Anchors (in the text)

- **Reasoning in reverse (*raisonner à l'envers*):** Listing likely variations in `(…)` to see which flip the conclusion (`bayesian-judgment`).
- **Logarithmic score / Surprise:** $-\ln \Pr(\text{outcome})$ for grading forecasts over track records (`neither-right-nor-wrong`).
- **Law of total variance split:** $\mathrm{Var}(Y) = \mathbb{E}_\theta[\mathrm{Var}(Y\mid\theta)] + \mathrm{Var}_\theta(\mathbb{E}[Y\mid\theta])$ — aleatory vs. epistemic inside admitted $\Theta$ (`aleatory-epistemic`).
- **Three contract tiers:** *Enforced* (types/schemas/tests), *Written* (prose spec, address post-mortem), *Writable-but-unwritten* (`failure-has-address`).
- **Logit lens:** Decoding intermediate transformer layers to observe emergent next-token structure (`next-token-scale`).
- **Goodhart's law (Strathern) & Sycophancy:** Target metrics and user-approval tuning corrupt comparator independence (`steering-not-spec`, `bainbridge-prompt-trap`).
- **Structural vs. Salience omission:** Factor absent from representation vs. present in weights/corpus but not retrieved/weighted under a prompt (`jagged-frontier-bcg`).
- **Generative vs. Confidence calibration & Monofact rate:** Kalai–Vempala lower bound (Good–Turing singleton rate); *semantic entropy* (Farquhar et al.) catches guessing, not consistent errors (`kalai-vempala-tail`).
- **Provenance laundering & Recursive collapse:** Unmarked AI outputs creating fake independent confirmation and degrading future training corpora (`uncertainty-laundering`, `provenance-laundering`).
- **METR sign error & Signaling collapse:** Measured −19% speed vs. perceived +20% speed (Becker et al., 2025); Spence/Akerlof pooling equilibrium when polish becomes free (`loss-of-the-tell`, `signaling-collapse`).
- **Bainbridge's irony of automation:** Automating routine tasks degrades human skill needed for rare overrides (`bainbridge-prompt-trap`).
- **Probability matching ("cry-wolf" effect):** Alarm response rates track PPV (Bliss, Gilson & Deaton, 1995) (`severity-bayes`).
- **Simplex architecture & Autoformalisation:** Trusted verified monitor/kernel wrapping an unverified learned generator (`four-sources`).
- **Seeded-error auditing:** Threat image projection (aviation security) and mutation testing to measure empirical escape probability (`layer3-organization`).
- **Named historical cases:** *Mars Climate Orbiter* (1999), *Challenger* O-rings, *Google Flu Trends* (Lazer et al.), *Knight Capital* (2012), *Mata v. Avianca* (2023), *Moffatt v. Air Canada* (2024), *Knight & Leveson* 27-version experiment (1986), *BCG jagged frontier* (Dell'Acqua et al., 2023).

---

## 5. Guided Paths (`PATHS` — 8 Perspectives)

| Path ID | Label | Target Audience / Arc | Route (Thread IDs in order) |
| :--- | :--- | :--- | :--- |
| `spine` | **The core argument** | Complete 9-stop arc from picture & frame to checks & institution | `map-territory` → `relevance-frame` → `variance-disagreement` → `frame-common-cause` → `front-loaded-verif` → `spec-into-data` → `rate-vs-escape-shift` → `two-axes-matrix` → `layer3-organization` |
| `sailboats` | **Sailboats, boiling water & possible worlds** | Probability as judgment, reasoning in reverse, one-shot decisions | `map-territory` → `relevance-frame` → `bayesian-judgment` → `neither-right-nor-wrong` → `ontological-residue` → `seu-sailboat-roulette` → `calibrate-vs-gate` → `layer1-attitude` |
| `evolution` | **How the claims were amended** | Tour of the 10 `Δ` drawers (sharpened, narrowed, or corrected claims) | `ontological-residue` → `two-axes-matrix` → `failure-has-address` → `plausibility-not-truth` → `kalai-vempala-tail` → `jagged-frontier-bcg` → `seu-sailboat-roulette` → `severity-bayes` → `series-vs-parallel` → `layer3-organization` |
| `engineer` | **The engineer: safety factors, chains & V&V** | Physical & safety-critical builders: margins, chains, V&V | `within-frame-defenses` → `uncertainty-laundering` → `failure-has-address` → `frame-common-cause` → `independence-cost-curve` → `four-sources` → `layer2-placement` |
| `stat-math` | **The statistician & the mathematician** | Conditionality, variance split, regress, calibration, severity | `deduction-induction` → `aleatory-epistemic` → `variance-disagreement` → `meta-nfl` → `neither-right-nor-wrong` → `kalai-vempala-tail` → `severity-bayes` |
| `cs-ml` | **The CS & AI builder: stack to agents** | Contracts vs. weights, regime flip, agents, sandboxes & gates | `design-by-contract` → `three-flips` → `jagged-frontier-bcg` → `kalai-vempala-tail` → `agentic-compounding` → `loss-of-the-tell` → `four-sources` → `sandboxes-and-gates` |
| `decision-org` | **The decision-maker & the institution** | Governance, signaling collapse, throughput pressure, alarm fatigue | `error-times-escape` → `signaling-collapse` → `bainbridge-prompt-trap` → `throughput-hollowing` → `same-lender` → `layer3-organization` |
| `recipient` | **The recipient of a confident number** | Auditing forecasts/outputs you did not build | `map-territory` → `neither-right-nor-wrong` → `four-questions` → `plausibility-not-truth` → `signaling-collapse` → `calibrate-vs-gate` |

---

## 6. Interactive Labs & Sources

### Interactive Labs (4)
1. **`plausibility`** (on `kalai-vempala-tail`) — Compares 5-sample self-consistency across *Well-known fact*, *Arbitrary rare fact*, and *Popular misconception* (demonstrating semantic entropy vs. consistent blind spots).
2. **`chain`** (on `series-vs-parallel`) — Compares an *Unchecked N-step chain* vs. *Every step cross-checked*, toggling per-step rate $p$ and shared omitted factor $q$.
3. **`seu`** (on `seu-sailboat-roulette`) — Separates *what you think* ($p$, stakes $L/\Delta U \to p^*$, humility buffer $b$) from *the world* (hidden omitted risk $z$), with presets (Mr Y, Mr X, Mr Y + unseen crack, + buffer, Russian roulette).
4. **`escape`** (on `error-times-escape`) — Models $\text{Risk} = P(\text{wrong}) \times P(\text{escape}\mid\text{wrong})$ with common-mode sharing $c$, miss rate $m$, false-alarm rate $f$, PPV, and uptake policy (*probability matching* vs. *investigate every flag*).

### Sources (`SOURCES` — 6)
- **`TK`** — *Talk draft (TED-style, in French)*, W. Fauriat (no model). Thesis: chasing the "right answer" is not the right attitude.
- **`FP`** — *The frame problem in quantitative practice*, W. Fauriat (arXiv preprint, 2026). Finite specification, three uncertainties, regress, epistemic humility.
- **`WG`** — *Where the Guarantees End*, W. Fauriat (essay, draft 2, July 2026). Stack contracts, learned top layer, check placement.
- **`FD`** — *Failing Differently*, Claude (Fable 5.2) at W. Fauriat's request (Nov 2026, exploratory). Re-reads the frame problem as a theory of checks.
- **`CR`** *(proposed, unchecked)* — *External critique*, Gemini 4 Argon (Nov 2026). Proposed extensions and objections.
- **`RV`** *(proposed, unchecked)* — *Review of the critique and of map v1*, Claude Opus 5.5 (18 Nov 2026). Proposed amendments (`Δ` drawers).
