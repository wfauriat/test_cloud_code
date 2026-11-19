# Source Threads (English) — Raw Material for Builders

> **Internal working material. Never cite, quote as a source, or mention in the monograph.** Map ids, source tags (TK, WG, FD, CR, RV) and the word "amendment" must not appear in chapter text (authoring conventions §9).
> Source tags indicate provenance status only: `FP` = the author's arXiv article (citable); `TK`, `WG` = the author's unpublished drafts; `FD` = AI-written essay; `CR`, `RV` = AI critique/review, **not verified by the author**. Material from `CR`/`RV` enters the monograph only as nuance or open discussion, under the statuses fixed in the content spec.
> Tables and grids in the source are HTML; builders re-express them as Markdown tables per the content spec.

Generated mechanically from the English map; the content spec takes precedence wherever they differ.


## Territory: 1. Epistemics & the frame (`epistemics`)

What can be concluded from hypotheses and data: why deduction and induction both run inside a finite specification, why error bars cannot show what that specification omits, and why no reasoner can audit its own frame from within.


### Angle: Reasoning inside a constructed picture (`picture`)

We never touch the world directly; we act on a simplified picture of what matters. The world does not consult the picture before answering.


#### `map-territory` — The world answers the action, not the picture

*Source tags:* FP TK

**Gist.** We decide on what we think might happen, never on what will happen. Yet what we decide changes what happens.

**Body.**

Any rational endeavour has a target, a world, and a gap between them. To close the gap we build a representation (measurements, categories, equations, probabilities) and act on that construction.

Put bluntly, reality does not care what we expect: «le réel se moque de nos anticipations». A sailor who puts the chance of breaking at 5% is not facing a 5% crossing: the mast breaks or it holds. The 5% describes the sailor's judgment under a chosen frame, not a property of the sea. It still decides what the sailor does, and the decision shapes what happens next. See the sailboat race [→ `seu-sailboat-roulette`].

**Concrete case.** 

A sailor weighs taking a satellite phone on a sea crossing and puts the chance of needing it at 20%. The crossing happens once; the phone is used or it is not. The world resolves to one outcome along an axis the picture had spread over a distribution.

**Analogy.** 

Korzybski: the map is not the territory. With an operational twist: you steer by the map, but the hull meets the territory's rocks.

**Diagnostic question.** 

In your current project, which numbers describe measured properties of the world, and which describe the team's degree of belief inside its chosen model?


#### `relevance-frame` — Relevance, exceptions & the frame

*Source tags:* TK FP

**Gist.** Before any inference can run, a reasoner must settle what matters: which conditions to state, and which to leave in an unstated background.

**Body.**

Water boils at 100 °C: three observations agree, so we generalise a rule. A colleague tests it at 101 °C and nothing boils: the water was heavily salted. We refine: *pure* water at 100 °C. Another test at 104 °C, no boiling: the vessel was sealed, like a pressure cooker. We refine again: pure water, at atmospheric pressure, at 100 °C. And on the summit of Mont Blanc, water boils at about 85 °C.

Every usable rule therefore has the form `A ∩ (…) → B`, where `(…)` hides an open-ended background of unstated conditions. Choosing which conditions to state, and which to leave in `(…)`, is choosing the **frame**: the finite specification of variables, categories, model class and objective that an inference works inside.

**Formal core.** 

Prediction conditions on a finite set *X* = (*X*1, …, *X**k*): `Pr(Y) = Σx Pr(Y | X = x) · Pr(X = x)`. The conditionals carry the modelling work, the weights carry the assumptions, and both sit inside a choice of which *X* to consider. That choice comes before the calculus and is circular: to know what to include, you already need a view of what matters.

**Analogy.** 

Pearl (1988) likens reasoning with exceptions to crossing a minefield: most steps are harmless, but some are devastating. Rules such as “birds fly” or “smoke suggests fire” have exceptions nobody can list in full.

**The catch.** 

Stating more conditions makes rules longer and more brittle; stating fewer leaves silent exceptions waiting for the day the background shifts. No setting removes both risks.


#### `deduction-induction` — Formality does not lift the limit

*Source tags:* FP TK

**Gist.** Deductive necessity and inductive generalisation are both conditional on a frame. Rigour inside a frame never certifies the frame.

**Body.**

It is tempting to think the frame problem afflicts only messy pattern-fitting, and that deduction escapes it. It does not.

*Deduction* delivers true conclusions **provided** its axioms, boundary conditions and idealisations hold. *Induction* carries past regularities forward **provided** the new context is similar enough to the observed one. Both guarantees are real and both are conditional: on the description in one case, on the judgment of similarity in the other. Necessity inside a poorly framed problem is only necessity inside a poor frame.

**Formal core.** 

Pearl's causal calculus (*d*-separation, `do(·)`, identification theorems) is deductive relative to a specified causal graph; the calculus does not certify the graph. Conformal prediction guarantees finite-sample coverage relative to exchangeability between calibration and deployment data; the method does not certify exchangeability.

**Concrete case.** 

A clinical prediction model validated on one cohort degrades when deployed where disease severity or diagnostic coding has shifted. It was correct relative to its frame; the frame was applied to a population it did not cover.

**The catch.** 

Challenged on an applied failure, a formal discipline's reflex is to formalise further. That moves the framing choice one level up; it does not remove it (the regress [→ `meta-nfl`]).


#### `bayesian-judgment` — Possible worlds & probability as judgment

*Source tags:* TK FP

**Gist.** Instead of chasing the single right answer, probabilistic reasoning weighs the possible worlds compatible with what we know.

**Body.**

Russell and Norvig draw the contrast: logical assertions say which possible worlds are ruled out; probabilistic assertions say how probable the remaining worlds are. Read this way, `Pr(B | A) = Pr(B ∩ A) / Pr(A)` is the share of the worlds where *A* holds in which *B* holds too: the share of the situations hidden in `(…)` where the rule works.

The practical consequence: stop chasing “the right answer” and reason *in reverse* («raisonner à l'envers»). Ask what could be hiding in `(…)`, what could vary, and which variations would flip the conclusion. Probability is then a tool for judgment under background knowledge (de Finetti, Savage, Jaynes, Lindley). “Subjective” does not mean arbitrary; it names where the inference is anchored.

**The catch.** 

Reasoning in reverse is not inventing far-fetched scenarios. It means listing the variations of context that are likely, or that cannot reasonably be ruled out, and checking which of them the conclusion is sensitive to.

**Diagnostic question.** 

Are we trying to show that our baseline forecast is the right answer, or mapping which variations of context would reverse our decision?


#### `neither-right-nor-wrong` — Neither right nor wrong: a forecast vs. a forecaster

*Source tags:* TK FP FD RV

**Gist.** Mr X says 5%, Mr Y says 0.1%. Before the race neither is right or wrong. One outcome barely settles it; only a track record can.

**Body.**

Two sailors assess the same light boat and reach different numbers: Mr X puts its chance of breaking at 5%, Mr Y at 0.1%. Who is right? Neither, and not for lack of rigour: each number says what that sailor thinks, given what he took into account.

After the race the outcome says something, but less than it seems. If the boat breaks, Mr Y is far more *surprised* than Mr X. If it holds, both saw their likelier outcome happen, and the result barely tells them apart. One outcome grades a forecaster weakly; many outcomes, scored with proper scoring rules and checked for calibration, grade him well. That is why calibration needs repetition [→ `calibrate-vs-gate`].

**Formal core.** 

Surprise is the logarithmic score, `−ln Pr(outcome)`. Boat breaks: Mr X scores −ln 0.05 ≈ 3.0, Mr Y −ln 0.001 ≈ 6.9, and the outcome favours X's judgment by a likelihood ratio of 0.05 / 0.001 = 50. Boat holds: 0.95 / 0.999 ≈ 0.95, almost no information. Each uneventful morning is weak evidence, which is how the turkey grew confident.

**Concrete case.** 

A forecast of “70% chance of rain” is not refuted by one dry day. A forecaster whose 70% days turn out rainy about 70% of the time over a year is calibrated; one whose 70% days are rainy 40% of the time is not.

**Diagnostic question.** 

When a forecast in your organisation “turned out wrong”, did anyone check whether it was a bad forecast, or a good one meeting its less likely outcome?


### Angle: Three uncertainties & measured disagreement (`three-uncertainties`)

Quantitative methods price variability and parameter doubt inside a chosen model class. What the frame omits produces no disagreement, so no error bars.


#### `aleatory-epistemic` — Aleatory vs. epistemic is a modelling choice

*Source tags:* FP FD

**Gist.** Aleatory uncertainty is scatter treated as irreducible; epistemic uncertainty is what more data or finer modelling could shrink. The analyst chooses the boundary.

**Body.**

Engineering uncertainty quantification and risk analysis split within-frame uncertainty in two. *Aleatory*: variability across replicates treated as identical, represented by distributions and propagated (Monte Carlo). *Epistemic*: lack of knowledge about parameters or sub-models, reducible by data or refinement.

The split is functional, not metaphysical. A die roll is aleatory if you do not measure the throw, epistemic if you do. Where to stop refining is the analyst's decision, not a property of the world.

**Formal core.** 

Over an admitted set of hypotheses Θ, predictive variance splits as `Var(Y) = Eθ[Var(Y | θ)] + Varθ(E[Y | θ])`. The first term is the aleatory part (average spread of replicates under each admitted hypothesis); the second is the epistemic part (spread of what the admitted hypotheses predict).

**The catch.** 

Both terms are averages over the *admitted* set Θ. A hypothesis that was never admitted has no weight in either. That is where the third kind of uncertainty lives.


#### `ontological-residue` — Ontological uncertainty: the turkey’s blind spot

*Source tags:* FP TK RV

**Gist.** The third kind sits upstream: doubt about whether the frame's variables, categories and model class fit the problem at all.

**Body.**

Called *ontological* (Wynne; Walker et al.), *deep* (Lempert) or *Knightian* (Knight) uncertainty, it is neither “I do not know the value of *X*” nor “my error bars on *Y* are wide”. It is “I am not sure *X*, as I defined it, is the right thing to look at”.

The emblem is the inductivist turkey. Fed every morning, it grows more confident with each confirming observation, and its confidence peaks on the eve of the holiday. Its statistics were sound; the failure came from something its frame had no category for. (Russell's 1912 original is a chicken whose neck is wrung by the man who fed it every day; the turkey is a later retelling.)

**Concrete case.** 

Pre-2008 mortgage risk models did not report wide intervals on nationwide correlated defaults; their frame did not contain that coupling, so the scenario did not appear at all.

**The catch.** 

For a single reasoner checking its own work, this kind of error is structurally silent, which makes it a natural suspect for the most consequential failures. Silence also has inside-the-frame sources: see the two-axis map [→ `two-axes-matrix`].

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

Challenger is easy to read as a pure failure of the frame. The record is mixed. The O-ring chart discussed the night before the launch showed only flights with O-ring damage, which hid the temperature trend that all 23 earlier flights reveal: a frame problem in the data. But engineers did object to launching in the cold and were overruled: an uptake problem, in which a comparator existed and the uncertainty it expressed was suppressed. See the five conditions [→ `five-conditions`].


#### `variance-disagreement` — Error bars measure disagreement

*Source tags:* FD

**Gist.** Proposition 3: a statement of uncertainty summarises how far the members of a specified set of alternatives disagree. An omitted factor produces no disagreement.

**Body.**

Why does what falls outside the frame not appear as wider error bars, but not appear at all? Because every quantitative uncertainty is computed from *disagreement* within a specified ensemble: replicates for the aleatory spread; posterior draws, ensemble members or bootstrap fits for the epistemic spread.

An alternative that was never admitted contributes no disagreement. A factor that varied unrecorded while the data were taken is already in the bars, as scatter put down to chance. A factor that stayed constant is nowhere.

**Formal core.** 

The admitted predictions `fθ(x)`, θ ∈ Θ, take only the recorded variables *x* as input, so any spread computed from them is blind to the present value of an omitted factor *z*. If *z* varied while the data were collected, it widened the aleatory term without being named; if it was constant, it left no trace.

**Analogy.** 

Ten committee members who all read the same incomplete briefing note agree unanimously. Their agreement measures the note's consistency, not whether page 2 was missing. See widening the set of alternatives on purpose [→ `layer1-attitude`].

**The catch.** 

Read this way, ontological uncertainty is not a third quantity awaiting its own formula. It is the part of possible error about which every admitted alternative is silent.


#### `within-frame-defenses` — Why robustness tools and safety factors stay inside

*Source tags:* FP FD

**Gist.** Sensitivity analysis, model averaging and safety factors widen the set of alternatives considered, while leaving them one shared frame.

**Body.**

Each practice has built defences against error: engineers apply safety factors; statisticians run prior-sensitivity analysis and Bayesian model averaging; machine-learning practitioners score inputs for being out of distribution.

These tools are indispensable within their scope. But a safety factor of 1.5 on a load assumes that the failure modes on the analyst's list are the relevant ones, and that what is missing from the list resembles what is on it. Perturbing parameters inside a model class never relaxes the class; averaging over a specified set of models never reaches a model outside it.

**Concrete case.** 

An engineer computes that a support bracket carries its design load with a margin of 1.8. If the bracket will serve in a corrosive atmosphere and corrosion appears nowhere in the model, neither a parameter sweep nor the margin addresses corrosion.

**The catch.** 

Treating bounded within-frame robustness as if it priced the frame lulls a team into thinking the ontological risk has already been paid for.


### Angle: The impossibility of self-audit (`self-audit`)

A reasoner cannot audit its own frame from within, and no second-order procedure dissolves the regress. New relevance enters only from outside.


#### `frame-common-cause` — The frame is a common cause (Proposition 2a)

*Source tags:* FD CR

**Gist.** Every check a reasoner computes from its own frame shares that frame, and is blind to whatever the frame omits.

**Body.**

Safety engineers call it *common-mode failure*: two backup pumps fed by one power supply are not two protections against a power cut. Proposition 2a says the frame problem is the limiting case of the same thing for reasoning.

A reasoner *can* usefully check itself: a re-derivation, a re-run or a resample catches slips of arithmetic, coding and sampling. What it cannot do is detect, with any comparator computed inside its frame, an error caused by a factor the frame omits. With respect to that factor, all its internal checks are copies of one another. (A *comparator* is whatever a claim is compared with: see Proposition 1 [→ `five-conditions`].)

**Formal core.** 

Let the outcome be `g(x, z)`, with *x* represented in the frame and *z* omitted. A claim `f1(x)` and a comparator `f2(x)` computed inside the frame are functions of *x* alone. Whether they agree is fixed once *x* is fixed, so, given *x*, their agreement carries no information about the error `g(x, z) − f1(x)`: the likelihood ratio is 1.

**Analogy.** 

Checking a finite-element calculation of a bracket with a hand calculation that makes the same idealisations: the two agree to three decimals, and both ignore corrosion.


#### `limits-of-data` — When observations catch frame errors (Proposition 2b)

*Source tags:* FD WG

**Gist.** Held-out data and cross-validation register an omitted factor only if it varied while the data were collected, and only through what the frame records.

**Body.**

Observations come from the world, not from the frame, so they *can* carry the imprint of an omitted factor *z*. Proposition 2b names two limits.

First, *z* must have *varied* while the observations were taken. If it stayed constant, its effect was absorbed into whatever was fitted or validated, and every check passes until *z* moves in deployment: *distribution shift*. Second, even when *z* varied, its effect shows only where it moves something the frame records, and there it appears as unexplained scatter, with nothing to say what caused it.

**Concrete case.** 

Google Flu Trends estimated influenza prevalence from search queries, well, for years. Then search behaviour changed, and its estimates went badly wrong while it kept producing them the same way (Lazer et al., 2014). Load tests on new brackets in a dry laboratory say nothing about five years in salt air.

**Analogy.** 

A trial-and-error agent learning to disarm a device records each wire's position but not its colour. It can cut the red wire in a thousand simulated trials and learn nothing about colour.


#### `meta-nfl` — The meta-level no-free-lunch

*Source tags:* FP

**Gist.** Why not formalise a second-order procedure that tests whether the frame is adequate? Because that procedure is itself a finite frame.

**Body.**

Confronted with framing limits, the methodologist's instinct is to build a meta-procedure that selects or audits frames. The argument forecloses this. Any such procedure must specify what to check, what counts as passing and which alternatives to search: a finite specification one level up, with the same problem.

Wolpert and Macready's no-free-lunch theorems formalise a shadow of this: averaged over all possible problems, no algorithm beats another; any advantage comes from assumptions about the problem class, and imposing those assumptions *is* choosing a frame.

**Formal core.** 

Hume (1748): induction rests on a uniformity assumption that induction cannot certify without circularity. Goodman (1955): the *respects* in which the future is taken to resemble the past (“green” or “grue”) are themselves an upstream choice.

**The catch.** 

“We just need better methodology” defers the framing choice. It never derives it from nowhere.


#### `two-routes-in` — How new relevance enters a frame

*Source tags:* FP FD

**Gist.** A frame cannot open itself from within. New relevance enters by two routes: being told by someone outside it, or running into the world.

**Body.**

If a frame cannot audit itself, how do frames ever improve? Only through contact with something outside them:

1. *Being told*: another witness, another discipline, an adversarial reviewer whose frame contains what yours omits.
2. *Finding out*: exploring and experimenting, so that unmodelled reality pushes back on an action (Sutton and Barto).

Being told is finding out at second hand: what another reasoner tells you was paid for by someone's earlier contact with the world. Both routes are sources of comparators: see the four sources [→ `four-sources`].

**The catch.** 

Exploration is not free: what to explore is itself frame-dependent, and some explorations are ruled out by cost, risk or irreversibility. Hence a working maxim: explore where it is cheap, reversible and supported by some intuition of what might be learned (sandboxes and gates [→ `sandboxes-and-gates`]).

**Diagnostic question.** 

When did your model class or problem formulation last change fundamentally? Did the trigger come from an internal metric, an outside critic, or a failure in the field?


## Territory: 2. Computing stack & the AI inversion (`stack`)

How classical computing built reliable silence out of explicit contracts checked in advance, and what changes when machine learning moves the specification into the data.


### Angle: How the stack below earned its silence (`earned-silence`)

From voltages to databases, classical computing scales because each layer exposes an explicit, checkable contract.


#### `bits-to-composition` — From dumb determinism to deep composition

*Source tags:* WG

**Gist.** A bit is a physical state plus an agreement on how to read it. Everything above, from compilers to payroll, is composition.

**Body.**

At the bottom of the stack sit elementary operations: add, compare, move, jump. Individually trivial; also blindingly fast and, absent hardware fault, deterministic: the same inputs give the same outputs, on another machine, a decade later.

There is no special ingredient on the way up from silicon to an operating system or a flight controller. What makes composition survivable at that scale is that each layer hides its machinery behind an exact promise.

**Analogy.** 

Shipping containers: the crane and the ship never need to know what is inside the box, because its dimensions and fittings obey an exact contract.


#### `design-by-contract` — Every layer is a stated contract

*Source tags:* WG FD

**Gist.** Design by contract (Meyer): a component states what it requires of its caller and what it guarantees in return. A specification is a statement.

**Body.**

TCP promises that bytes arrive in order or not at all. A sort routine promises an ordered permutation of its input. A file system promises that after a successful write and flush, the bytes are on the disk.

The load-bearing property is that *a specification is a statement*: written in advance, readable by someone who did not write the code, disputable, versionable, and violable. Call a component whose rules were written this way a **stated component**, as opposed to a **learned component**, whose rules were fitted to examples (the inversion [→ `spec-into-data`]).

**Formal core.** 

Hoare triple: `{P} C {Q}`. If the caller establishes precondition *P*, running *C* establishes postcondition *Q*.

**The catch.** 

A contract protects only what it states, and only where something enforces it. Units, environments and assumptions left in prose outside the enforced interface can still be laundered [→ `uncertainty-laundering`] in classical code.


#### `front-loaded-verif` — Front-loaded verification: check the layer once

*Source tags:* WG FD

**Gist.** Because the promise is a written statement, it can be checked in advance, on the component itself, once for all future runs.

**Body.**

Nobody stands beside a payroll system watching it add. Because the contracts are statements, verification can be *front-loaded*: types, unit tests, code review, static analysis, fuzzing, and formal proof where the stakes justify it, all check the *component* against its statement before deployment, and the check covers every later call.

Dijkstra's limit (testing shows the presence of bugs, never their absence) bounds how much certainty this buys. It does not change the kind of move: work done in advance on the layer, then retired from the runtime.

**Analogy.** 

Load-rating a bridge design before opening it, rather than weighing every vehicle after it has crossed.


#### `failure-has-address` — Definable divergence: failures have an address

*Source tags:* WG CR RV

**Gist.** Classical software fails constantly. But when it does, a stated or statable expectation was contradicted somewhere you can point to.

**Body.**

On 23 September 1999 the Mars Climate Orbiter was lost on arrival at Mars. Ground software (SM_FORCES) had written thruster impulse in pound-force-seconds where the interface specification required newton-seconds; the navigation software read the numbers as metric, and its estimates of those small forces were off by a factor of about 4.45.

The investigation also found thin staffing, unescalated anomalies and missing independent checks. But under the organisational causes sat a written specification and the exact place where it was violated. Even in an undocumented codebase, someone can state afterwards what the code *should* have done and locate where it diverged. Post-mortems converge on an address.

**Concrete case.** 

Mars Climate Orbiter Mishap Investigation Board, Phase I report (1999): the root cause named a specific ground software file and the interface specification it contradicted.

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

A written statement is not yet a checked one. The Orbiter's unit requirement lived in a prose interface document; the data file carried bare numbers that no type or schema could reject. Three tiers follow:

- *Enforced* contracts (types, schemas, tests) are checked in advance and automatically.
- *Written* ones give an address after the fact, but are front-loaded only if someone turns them into a check.
- *Writable but unwritten* ones give an address after the fact.

A learned component has none of the three, for the component itself.

**Diagnostic question.** 

When a component of your pipeline produces a bad result, can you point to the rule it violated, and was that rule enforced by anything other than a document?


### Angle: The machine-learning inversion (`ml-inversion`)

For seventy years software stopped where our ability to write explicit rules stopped. Machine learning crosses that wall by moving the specification into the data.


#### `spec-into-data` — The specification moves into the data

*Source tags:* WG FD

**Gist.** Instead of writing the rule, you supply examples and let optimisation fit billions of parameters. You buy reach and spend the guarantee.

**Body.**

Reading handwriting, judging whether a résumé fits a role, summarising a messy document: these resisted software for decades, not because they were computationally hard but because *nobody could write the rule*.

Machine learning inverts the workflow: examples plus optimisation produce a **learned component**, whose rules exist only as fitted parameters. The gain is *reach*, landing exactly on tasks with no writable specification. The price is twofold: the *guarantee* (the rule fits the examples; nothing promises it fits the world) and *legibility* (billions of parameters cannot be read, diffed or reviewed). The specification did not disappear. It moved into the training data, the objective and the curation choices.

**Analogy.** 

The code-review question changes from “what does line 42 do?” to “who chose the examples, and what did they leave out?” (Sculley et al., 2015, on data as an undisciplined dependency).

**The catch.** 

The certainty was not lost by accident; it was *spent*, to reach tasks that had no writable specification. Asking a learned layer for the guarantees of a stated one is asking it to stop being what was bought.


#### `next-token-scale` — The next-token engine

*Source tags:* WG

**Gist.** A large language model is trained on one objective at industrial scale: predict the next fragment of text. Grammar, facts and reasoning patterns accumulate because they help.

**Body.**

Hide the next fragment (a *token*) of a document, let the network guess, measure the error, nudge billions of parameters slightly, and repeat trillions of times. Nobody types in the rules of grammar.

The resulting structure can be watched in small open models. The *logit lens* decodes the model's running guess at each intermediate layer: on “The Eiffel Tower is located in the city of”, early layers offer generic filler, middle layers settle on the right country, and the specific city emerges near the top. Nobody built that staircase; it was kept because it reduced prediction error.

**Concrete case.** 

The reach is real and measured. In a randomised field experiment with 758 BCG consultants (Dell'Acqua et al., 2023), those using GPT-4 on tasks inside its competence completed 12.2% more tasks, 25.1% faster, at quality rated about 40% higher.

**The catch.** 

Because structure accumulated only where it helped predict text, competence has no clean boundary: see the jagged frontier [→ `jagged-frontier-bcg`].


#### `plausibility-not-truth` — Fluent and wrong, as designed

*Source tags:* WG RV

**Gist.** Plausibility is the objective; truth is a frequent correlate. A fluent falsehood is not a component breaking its contract: there was no contract to break.

**Body.**

A stated component that returns a wrong result contradicts its specification. A learned text model that produces a fluent falsehood contradicts nothing written: a well-formed, confident paragraph is a likely continuation of the prompt, which is what pre-training optimised. Post-training steers toward accuracy and makes such errors rarer; it does not turn the tendency into a guarantee (steering is not specification [→ `steering-not-spec`]).

The consequence: fluency is uniform across right and wrong answers. A single output carries no surface sign of having left the model's competence.

**Concrete case.** 

*Mata v. Avianca* (S.D.N.Y., 2023): lawyers filed a brief citing court decisions that ChatGPT had invented, with plausible case names, citations and quotations, and were sanctioned. Nothing in the text marked the fabricated cases.

**The catch.** 

No surface tell, but sometimes a signal underneath: a model guessing an arbitrary fact tends to give different answers when asked again. See calibration and the long tail [→ `kalai-vempala-tail`] and the lost tell [→ `loss-of-the-tell`].

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

*Moffatt v. Air Canada* (2024) is often cited as the emblem of a hallucinating chatbot: a website chatbot told a passenger that a bereavement discount could be claimed retroactively, contrary to the airline's policy, and the tribunal held the airline liable. But no evidence about the chatbot's technology was put before the tribunal, and an Air Canada spokesperson later said it predated generative AI. The case shows that an automated answer is the firm's own act. It is not evidence about language models; *Mata v. Avianca* is the cleaner emblem of fabrication.


#### `steering-not-spec` — Steering is not specification

*Source tags:* WG

**Gist.** System prompts, preference tuning and evaluation suites are real engineering, but they move tendencies; they do not state contracts.

**Body.**

Modern systems wrap the raw model in system prompts, post-training on human preference judgements (RLHF, reinforcement learning from human feedback), guardrails and benchmark suites. Does this restore the specification?

Not in the sense that matters here. A preference dataset is more examples: data becoming program once more. Steering moves a distribution; it does not state an invariant that can be checked once for all runs. And it inherits Goodhart's law, in Strathern's formulation: a measure adopted as a target ceases to measure what it stood for. That is the mechanism behind reward hacking and sycophancy.

**Analogy.** 

Training a dog versus wiring a circuit breaker. Training makes bad behaviour much rarer; it is not a tripwire.

**The catch.** 

Steering can be excellent and still leave nothing for anyone to read, sign or check in advance.


### Angle: The regime flip at the top layer (`regime-flip`)

Between the classical middle of the stack and its learned top, three properties flip together, and with them what verification can in principle do.


#### `three-flips` — Three properties flip together

*Source tags:* WG RV

**Gist.** What is promised: contract becomes tendency. How failure presents: divergence becomes fluency. Where the post-mortem lands: an address becomes a distribution.

**Body.**

Move from a database call to a language-model call and three properties invert at once:

1. **What is promised.** Below: an explicit contract, checkable against a statement. Above: a statistical tendency, measurable in aggregate on a test set and assertable about no single answer.
2. **How failure presents.** Below: a definable divergence, such as a crash, a failing test, or two representations of one fact that disagree. Above: fluent output, indistinguishable from success at the point of use.
3. **Where the post-mortem lands.** Below: a line or an interface. Above: a training distribution and an objective. *You cannot merge a patch into a distribution.*

**The catch.** 

The claim is not that learned models fail more often than buggy classical code; often they fail less. Frequency is not the axis. The axis is whether an error is definable against a statement, and whether verification can be done once, in advance.

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

“Below: a definable divergence” should not be read as “below, errors are loud”. Classical software has plenty of silent errors; the Orbiter's unit error ran for months without a decisive alarm. The difference is that a classical error is *definable*: a comparator can be written and applied once, to the component. For a learned component, comparators exist only per task and per output.


#### `layer-vs-output` — Verifying the layer vs. checking outputs one by one

*Source tags:* WG

**Gist.** Below the line you verify the sort routine once, for every list. Above it, only outputs can be checked, one at a time, after they exist.

**Body.**

Statistical components are not new: spam filters, search ranking and recommendation feeds have been unspecified for decades. But they were fenced inside particular products. A general-purpose language model is *compositional*: arbitrary software calls it through a text interface and passes its output on.

Since the learned layer has no writable specification, the once-for-all move is gone. Verification has to be rebuilt around the task [→ `four-sources`] where the task admits a mechanical check, or placed on individual outputs [→ `layer2-placement`] before they turn into actions.

**Diagnostic question.** 

Where in your architecture does output leave a learned component and enter a system that executes, bills, commits or publishes?


#### `jagged-frontier-bcg` — The jagged competence frontier

*Source tags:* WG CR RV

**Gist.** Model competence does not follow human intuitions of difficulty. Just outside its boundary, AI-assisted experts did worse than unassisted ones.

**Body.**

In the BCG field experiment with 758 consultants (Dell'Acqua et al., 2023), a separate task was designed to lie just outside GPT-4's competence while looking just as routine. On it, consultants using the model were **19 percentage points less likely** to reach a correct answer than those working without it.

The frontier is *jagged*: strong on one task, weak on a neighbouring one that looks no harder, and the boundary moves with each model version. From inside the conversation both sides look the same, because the output is equally fluent.

**Concrete case.** 

Dell'Acqua et al. (2023), “Navigating the jagged technological frontier”: fluency plus an invisible competence boundary produced negative value where users relaxed their own checking.

**The catch.** 

Mapping the frontier for your own tasks is an ongoing deployment activity. Public benchmarks do not tell you where it runs.

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

An objection: for a language model the frame is rarely a missing variable, since its training text mentions almost everything; failures come from relations among things it does represent. Reply: the frame problem in AI was always about relevance among represented facts (McCarthy and Hayes, 1969; Dennett's robot knew the bomb was on its wagon). Two cases should be kept apart:

- *Structural omission*: the factor is absent from the representation (events after the training cut-off, private data, an unrecorded variable). Proposition 2 holds strictly.
- *Salience omission*: the factor is represented but not brought to bear on this input. Proposition 2 holds only for comparators that reuse the same weights and the same prompt.

Salience depends on phrasing, which is one reason the frontier is jagged.


#### `kalai-vempala-tail` — Calibration, the long tail & consistent errors

*Source tags:* WG FD CR RV

**Gist.** A model calibrated to its training distribution must hallucinate on rare arbitrary facts. Some of those errors are caught by asking again; consistent ones are not.

**Body.**

Kalai and Vempala (2024) proved a lower bound: for *arbitrary* facts, those no regularity can predict (a birth date, a citation, a clause), a language model calibrated to its training distribution must generate falsehoods at a rate close to the share of such facts that appear exactly once in training (the Good–Turing “monofact” rate). Kalai, Nachum, Vempala and Zhang (2025) add that most evaluations score “I don't know” like a wrong answer and below a lucky guess, so training selects for confident guessing.

Two regimes need separating. A model *guessing* an arbitrary fact spreads its probability over many answers: ask five times and you get several, so a cheap re-run flags the error. A model that is *consistently* wrong (a misconception common in its training text, or post-training that rewards one confident answer) repeats the same falsehood, and the re-run passes it.

**Formal core.** 

Roughly: hallucination rate on arbitrary facts ≥ monofact rate − miscalibration − small terms. “Calibrated” here means *generative* calibration: the model's distribution over statements matches the training distribution. Abstaining (“I don't know”) deliberately departs from it.

**Interactive lab.** lab `plausibility` (see content spec, quantitative examples)

**The catch.** 

Breaking the hallucination equilibrium means training models to abstain and grading abstention above a wrong guess. Public evaluations mostly do not; your own can.

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

Two senses of “calibration” are easily mixed up. Confidence calibration (“70% means right 70% of the time”) is an honest partial fix; generative calibration entails hallucination, and has to be departed from. The two connect: abstention uses confidence to depart from generative calibration. And it is too strong to say that nothing in the mechanism computes an out-of-competence signal. The spread of repeated samples is such a signal for guessing errors (semantic entropy, Farquhar et al., Nature 2024), though not for consistent ones. The tell did not vanish; it moved from the surface of one answer into the spread of many.


## Territory: 3. Automation & chains (`automation`)

How complex goals are assembled from chains of simpler steps, how chaining launders uncertainty, and what automation removes from individual and collective error detection.


### Angle: Chains, cross-checks & laundering (`chains-laundering`)

Complex goals are reached by passing results from one model or step to the next. How the steps are wired decides whether blind spots add up or cancel.


#### `divide-and-orchestrate` — Complex goals as orchestrated sequences

*Source tags:* FP FD

**Gist.** Goals too large for one model are decomposed into pipelines of specialised steps, in engineering as in AI.

**Body.**

In multiphysics engineering (thermal → structural → materials) as in AI workflows (retrieve → summarise → plan → execute code), complex goals are met by assembling simpler modules.

The higher the goal (“keep the plant safe”, “refactor this repository”, “resolve the customer's dispute”), the less it can be stated formally, while intermediate results move ever faster from one module to the next.

**Analogy.** 

An assembly line where each station does a well-defined local job, and no station sees whether the finished vehicle suits the road it will drive on.


#### `series-vs-parallel` — Chains vs. cross-checks (Proposition 5)

*Source tags:* FD CR RV

**Gist.** In a chain, blind spots add up, plus the errors born at interfaces. In a cross-check, they shrink toward what both components share.

**Body.**

Call a component's **blind spot** the set of error causes it cannot register. Components combine in two ways that behave oppositely, like series and parallel arrangements in reliability engineering:

- **Chain (series):** each component takes the previous output as given. An error escapes if any link misses it, and errors born at the interfaces belong to no link.
- **Cross-check (parallel):** two components bear on the same claim and their disagreement is registered. An error escapes only if both miss it, or if the comparison is too coarse to show their disagreement.

A model asked to review its own output looks like a cross-check on the diagram; with respect to its own blind spot it is a copy.

**Formal core.** 

Chain: `Bchain ⊇ B1 ∪ … ∪ Bn ∪ Binterfaces`. Cross-check of producer 1 by checker 2: `Bcheck = B1 ∩ (B2 ∪ Bcmp)`, where `Bcmp` holds the errors the comparison cannot express. If checks miss independently, `P(escape) = Πi mi`; for an error whose cause they all share, `P(escape) = 1` however many there are.

**Interactive lab.** lab `chain` (see content spec, quantitative examples)

**The catch.** 

A model checking its own work has `B2 ≈ B1`, so the intersection is nearly the whole blind spot.

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

The cross-check rule assumes perfect comparison and uptake. A comparison term relaxes that, but it matters only for errors the checker does register: hence `B1 ∩ (B2 ∪ Bcmp)`, not `(B1 ∩ B2) ∪ Bcmp`, which would also count errors the producer catches by itself. And the trade-off (the shared blind spot shrinks with distance while the comparison blind spot grows) suggests an optimal reviewer distance without proving one: that needs assumptions about both curves. The trade-off itself is Proposition 4 [→ `independence-cost-curve`].


#### `uncertainty-laundering` — Laundering at handoffs

*Source tags:* FP FD CR RV

**Gist.** Laundering: dropping a claim's conditions at a handoff, so a conditional result arrives downstream as an unconditional fact.

**Body.**

What turns a composition into a chain? **Laundering.** A thermal model computes a temperature field under stated boundary assumptions. Handed to a structural model as a bare array, stripped of its conditions and uncertainty, it gives the downstream link nothing to compare with: it can only be taken as given.

By the end of a five-stage pipeline the output has eight significant digits (or crisp executive prose) and a stack of unpropagated assumptions underneath. In terms of the five conditions of detection [→ `five-conditions`], laundering is a failure of *comparability* at every link.

**Concrete case.** 

The Orbiter's impulse values crossed an interface as bare numbers in a file. The unit (lbf·s rather than N·s) travelled only in a prose document, so nothing at the receiving end could notice the mismatch.

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

Two cousins of laundering are worth naming. Dropping a claim's *units or definitions* defeats comparability just as dropping its assumptions does. Dropping its *provenance* defeats something else: without knowing where a claim came from, nobody can judge whether a second source is independent of it (see provenance laundering [→ `provenance-laundering`]).

**Diagnostic question.** 

At the handoffs in your workflow, do results travel with their assumptions, units, uncertainty and origin, or as bare numbers and strings?


#### `agentic-compounding` — Agents as multi-step chains

*Source tags:* FD WG

**Gist.** An AI agent running a sequence of tool calls is a chain with as many links as steps, and its errors execute before anyone reads them.

**Body.**

An *agent* is a language model that pursues a goal through a loop: plan, call a tool, read the result, take the next step. It combines two hazards.

Structurally, an *N*-step trajectory in which each step builds on the last is an *N*-link chain: misreadings and framing assumptions propagate. Operationally, the system moves from producing *answers*, which wait for a reader, to taking *actions*, which change state, call services and commit code at once. A wrong answer costs the time it takes to read; a wrong action executes.

**Concrete case.** 

Knight Capital (2012): a deployment error left dormant order-routing code live; in about 45 minutes the firm sent millions of unintended orders and lost over $460 million (SEC, 2013). No language model was involved. The pattern is automated action outrunning oversight, which agents extend to tasks nobody specified.

**The catch.** 

Giving the least-guaranteed layer of the stack the most authority to act inverts the pattern that made the stack safe. See sandboxes and gates [→ `sandboxes-and-gates`].


### Angle: The silent erosion of human checks (`human-erosion`)

Slow analysis produced checks as a by-product of effort. One-step generation removes both the checks the analyst used to make along the way and the visible hesitation of a producer out of its depth.


#### `friction-as-generator` — Friction had a function: it generated comparators

*Source tags:* FP FD

**Gist.** Slow, step-by-step work made the analyst form expectations and intermediate results that could contradict one another.

**Body.**

For most of the history of quantitative work, producing a result was slow. While cleaning data, choosing variables and deriving equations, the analyst formed an expectation of what the answer should look like and produced partial versions of it, each able to contradict the next.

Friction, in other words, **generated comparators**: the analyst's *own checks*. Nobody ever drew that loop on a process chart, which is why its disappearance under one-step generation goes unnoticed until an absurd number slips through.

**Analogy.** 

Walking up a ridge versus being dropped on the summit in fog: the walker knows how steep it was, because their legs climbed it.


#### `loss-of-the-tell` — The lost tell & the METR sign error

*Source tags:* FD WG

**Gist.** A person out of their depth hesitates and hedges. A language model writes the same fluent prose either way, and fluency feels like speed even when it slows you down.

**Body.**

When a colleague is guessing, their uncertainty shows: hesitation, rough structure, hedging. That **tell** prompts others to look harder. A language model's wrong answers come in the same voice and format as its right ones.

Fluency also distorts self-assessment. In METR's randomised trial, experienced open-source developers working in their own repositories were **about 19% slower** with early-2025 AI tools, while estimating afterwards that the tools had made them **about 20% faster** (Becker et al., 2025). The number describes particular tools at a particular moment; the durable finding is the sign error.

**Concrete case.** 

Perceived: 20% faster. Measured: 19% slower. Fluent output feels like progress, and perception is not an instrument.

**The catch.** 

*Measure, don't testify.* Self-reported productivity and confidence are not evidence when the tool's output is designed to read well.


#### `signaling-collapse` — When polish stops failing differently from substance

*Source tags:* FD CR RV

**Gist.** Clean prose, neat figures and running code used to be evidence of understanding, because confused work looked confused. That signal has collapsed.

**Body.**

Reviewers, teachers and managers long relied on the *form* of work as evidence of its quality. In human production, form and substance shared a cause, understanding: when understanding failed, form usually failed with it. Form was a usable comparator because it could fail differently from a careless claim.

Now that fluent text and running code can be had without understanding, form no longer fails when substance does. It is still present; it is no longer a check. In economic terms (Spence; Akerlof), polish was a *costly signal*. When the signal becomes free while checking stays expensive, checked and unchecked work pool together, and cheap unchecked output can drive out expensive checked work.

**Analogy.** 

Akerlof's market for used cars: when buyers cannot tell a sound engine from a lemon by the paint job, the price falls to the average, and owners of sound cars stop selling.

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

The standard way out of a pooling equilibrium is credible disclosure. A common rule that every result states its status (exploratory or established, what was independently checked) is such a disclosure, provided it is audited by a track record and by seeded errors (Layer 3 [→ `layer3-organization`]). A label nobody audits is cheap talk.


#### `bainbridge-prompt-trap` — Bainbridge’s irony & the two prompt traps

*Source tags:* FD

**Gist.** A person and a model form a cross-check only if the person forms an independent view first, and two mechanisms pull the model toward agreeing.

**Body.**

Bainbridge (1983) named the *irony of automation*: automating the routine part of a task leaves the operator responsible for the rare failures that need exactly the skills the automation no longer exercises.

If an analyst only reads the model's draft, there is one representation, read twice. And two mechanisms shrink the difference between user and model:

1. **The prompt transmits the frame.** A model answers within the terms of the question; the more the prompt specifies a solution, the less the answer can contradict it.
2. **Training toward approval.** Models tuned on user-satisfaction signals drift toward agreeing with the user's premises (sycophancy), which lowers their value as a comparator.

**Diagnostic question.** 

When you use a model to check your work, do you hand it the problem, or your solution with a request to look it over?


### Angle: Collective epistemics & shared blind spots (`collective-epistemics`)

When a whole community adopts the same models, individual error rates fall while the errors that remain become correlated across authors and reviewers.


#### `rate-vs-escape-shift` — Error rate falls, escape probability rises

*Source tags:* FD CR RV

**Gist.** Better models make errors rarer. When everyone shares the same model, the errors that remain are shared too, and harder to catch.

**Body.**

Two quantities must be kept apart: the **error rate**, the probability that a claim is wrong, and the **escape probability**, the probability that a wrong claim reaches an action without being contradicted in time (the decomposition [→ `error-times-escape`]).

Suppose each analyst has idiosyncratic blind spots, and all of them consult one model. Against each analyst's own blind spots the model is a real comparator, so the error rate falls. But errors that come from the *model's* blind spots become common to everyone who relies on it, authors and reviewers alike. Peer review turns into a cross-check between near-copies, and the escape probability rises.

**Formal core.** 

`Risk = P(wrong) × P(escape | wrong)`. Rarity belongs to the first factor; correlation governs the second. Whether their product rises or falls is an empirical question, field by field.

**The catch.** 

Nobody routinely measures the escape probability of human–AI review, though the method exists (seeded errors [→ `layer3-organization`]).

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

A second mechanism adds to correlation: as errors become rare, most of a fixed checker's alarms are false, so people stop heeding it. In a simple model this makes the checker decorative (escape probability toward 1) without by itself making total risk rise; total risk rises when correlation rises as well. The escape lab [→ `error-times-escape`] lets you separate the two.


#### `same-lender` — One lender for all borrowers

*Source tags:* FD

**Gist.** A language model is “being told” industrialised into one store. A borrowed comparator works against the borrower's errors, never against the lender's.

**Body.**

Another reasoner's objection is cheap because it reuses contact with the world that someone else paid for (being told [→ `two-routes-in`]). A model trained on the written record is the extreme case: what many people found out, absorbed into one set of weights.

Used as a second opinion, it genuinely catches the borrower's own slips. It is worth nothing against the lender's blind spots, and whole communities now borrow from the same few lenders.

**Analogy.** 

Twenty journalists fact-checking each other against the same unverified wire dispatch.


#### `provenance-laundering` — Pollution of the epistemic commons

*Source tags:* CR RV

**Gist.** As model output flows back into the web, the literature and codebases without provenance, copies of one source start to look like independent witnesses.

**Body.**

Run the same-lender problem forward in time. Model-generated text, code and syntheses re-enter public repositories, papers and the web, often with no mark of how they were produced: *provenance laundering*.

When people, and the next generation of models, read that record, copies of the lender's earlier outputs look like independent confirmations. The apparent number of witnesses grows while the number of genuine contacts with the world does not. Models trained on recursively generated data also degrade (Shumailov et al., Nature 2024).

**The catch.** 

Ten sources that all trace back to one model add signatures and almost no evidence: their agreement had little chance to fail (severity [→ `severity-bayes`]). Provenance is what lets anyone judge whether a second source fails differently.


#### `throughput-hollowing` — The institutional throughput squeeze

*Source tags:* FP WG

**Gist.** As confident answers become nearly free, organisations starve the resource that has become the bottleneck: independent evaluation.

**Body.**

The bottleneck has flipped: it is no longer hard to generate answers; it is hard to know which answers are reliable. Yet incentives reward throughput: shipped features, published papers, rapid slide decks.

Producing a confident, fluent answer now costs almost nothing; checking one costs what it always did in domain knowledge, attention and time. Budgets drift toward generation tools and away from evaluators, hollowing out evaluative capacity just as the volume of unchecked claims grows fastest.

**Diagnostic question.** 

In your organisation, is evaluative capacity a named number that caps how much is produced, or whatever time is left over?


## Territory: 4. Decisions, risk & checks (`decisions`)

How uncertain pictures turn into one-shot decisions with real stakes, what it takes to detect an error in time, and the three layers of a remedy.


### Angle: Deciding on a picture: one-shot stakes (`seu-oneshot`)

What we believe decides what we do. When one action carries a catastrophic downside, going ahead requires a failure probability you can justify calling tiny.


#### `seu-sailboat-roulette` — The sailboat race & Russian roulette

*Source tags:* TK RV

**Gist.** In a one-shot decision with a severe downside, the risky option pays only below a small threshold of believed failure. The world does not consult your belief.

**Body.**

In a sailing race, each crew chooses between a **light, fast boat** and a **reinforced, slower one**. A breakage at sea means a tow that costs more than the prize. Mr X puts the light boat's chance of breaking at 5%, Mr Y at 0.1%; both put the reinforced boat at 0.01%.

Savage's *subjective expected utility* (SEU) makes the point exact: we decide on what we think, never on what will happen. With gain Δ*U* if the light boat holds and loss *L* if it breaks, both relative to the safe choice, the light boat pays when the believed failure probability *p* is below *p*∗ = Δ*U* / (Δ*U* + *L*). Mr X and Mr Y can both choose rationally, and choose differently.

Push the stakes to the limit: **Russian roulette**. You would play only if utterly convinced the chamber is empty, or if the prize were immense. And if your conviction came from a frame that missed a loaded chamber, nothing in your reasoning will warn you.

**Formal core.** 

Treat the reinforced boat as a sure baseline. Go iff `(1−p)·Uwin + p·Ufail > Usafe`, that is iff *p* < *p*∗ = (Uwin − Usafe) / (Uwin − Ufail) = Δ*U* / (Δ*U* + *L*). As *L* / Δ*U* grows, *p*∗ tends to 0.

**Concrete case.** 

If Mr Y inspects the light boat before the start and finds a wide crack in the mast, his picture changes, his *p* jumps above *p*∗, and he switches boats. A frame is revised by contact with the world: here, a look at the mast.

**Interactive lab.** lab `seu` (see content spec, quantitative examples)

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

It is tempting to put the omitted risk into the decision rule: go iff the *true* total risk is below the threshold. But under SEU, rationality is relative to what the decider believes, and the omitted factor is precisely what the decider cannot see. Treating it as a dial the decider can read would make ontological uncertainty a measurable third quantity, which Proposition 3 [→ `variance-disagreement`] denies. The lab therefore separates what you think from what the world holds, and gives humility its only lever: a deliberate buffer, which is a judgment, not a measurement.

**Diagnostic question.** 

For your next irreversible deployment: what is L/ΔU, what threshold p∗ does it imply, and is your failure estimate, plus a buffer for what you may be missing, below it?


#### `error-times-escape` — Risk = error rate × escape probability

*Source tags:* FD CR

**Gist.** An error in a picture costs nothing until someone acts on it. What matters is how often a wrong claim reaches an action uncontradicted.

**Body.**

Because the world answers the action rather than the picture, a wrong claim does harm only if it reaches an action without being contradicted first:

`P(wrong and acted on) = P(wrong) × P(not contradicted in time | wrong)`

Call the first factor the **error rate** and the second the **escape probability**. Benchmarks, leaderboards and scaling curves measure the first. The frame argument and safety engineering are about the second. Automation can push the first down while pushing the second up (shared blind spots [→ `rate-vs-escape-shift`]).

**Formal core.** 

With *E* = “the claim is wrong” and *C* = “a check contradicts it before the action”: `P(E ∩ ¬C) = P(E) · P(¬C | E)`. The two factors are not independent: as *P(E)* falls, a fixed checker's alarms are more often false, which can lower uptake and so raise *P(¬C | E)* (the false-alarm trap [→ `severity-bayes`]).

**Interactive lab.** lab `escape` (see content spec, quantitative examples)

**The catch.** 

A 1% error rate with a 90% escape probability lets 0.9% of claims reach action wrong; a 10% error rate with a 1% escape probability lets 0.1% through. The more accurate producer is the riskier system, nine times over.


#### `calibrate-vs-gate` — Calibrate where repeatable; gate where one-shot

*Source tags:* FD WG

**Gist.** Calibration uses the world as a comparator over many repetitions. For a one-off, irreversible decision, no score replaces a gate.

**Body.**

When a decision repeats thousands of times against a reasonably stable distribution (triage queues, weather forecasts, credit scoring), *calibration* works: set thresholds, let the system abstain on uncertain cases, compare stated probabilities with observed frequencies, adjust.

A one-shot decision (a sea crossing, a surgical intervention, a major architectural commitment, an irreversible agent action) has no population of trials, and the world's answer arrives after the act. A rate is not a promise about this instance. What protects it is a **gate**, an independent check before the action, plus a deliberate buffer for what the picture may be missing.

**Analogy.** 

A 70% rain forecast lets a commuter tune umbrella habits over a year. A one-time launch needs a go/no-go on every subsystem.

**The catch.** 

Calibration is also the only way to grade a forecaster [→ `neither-right-nor-wrong`]; that is why it needs repetition to exist at all.


#### `sandboxes-and-gates` — Sandboxes and gates: an architecture for exploration

*Source tags:* FD WG

**Gist.** Every action is also a question put to the world. Explore freely where the answer is cheap and reversible; gate where it would cost too much.

**Body.**

Exploring the world is one of the two ways a frame learns what it omitted (being told, finding out [→ `two-routes-in`]), yet prudence says automated agents must be restricted. Both hold, because *an action is also a question put to the world*.

A **sandbox** is an isolated environment in which actions have no outside effect: there, asking the world is cheap and reversible, and an agent may explore freely. A **gate** is a point at which an action waits for approval: it marks where the world's answer would be too expensive or irreversible, so another comparator, a person's judgment or a formal check, must stand in for it.

**Concrete case.** 

Coding agents do best where compilers and test suites give an instant, free, reversible answer from a computational world, inside a sandbox.


#### `four-questions` — Receiving a confident number

*Source tags:* FP FD

**Gist.** A number given without its conditions transfers responsibility dressed as information. Four questions anyone can ask, without technical training.

**Body.**

Most people meet expert and machine claims as recipients: they bear the consequences of a frame they did not choose and cannot audit. They do not need to redo the technical work. They need to know that its *conditions* are part of what is communicated, and to ask for them when they are missing:

1. Under what conditions does this hold?
2. What would change the number?
3. What is the most likely way this is wrong?
4. What was deliberately not modelled?

The questions require no expertise, only the willingness to hear “we don't know” or “we did not consider that” as substantive answers rather than failures.

**Concrete case.** 

“It will rain tomorrow” is a directive in the costume of information. “70% chance of rain” supports a decision in proportion to the stakes: how much getting wet matters to *you*, which no forecaster's frame contains.

**The catch.** 

When the output comes from an automated system, the questions stay the same but must be put to an institution rather than a person, and the institutional capacity to answer them is what throughput pressure [→ `throughput-hollowing`] erodes.

**Diagnostic question.** 

The next time a single number reaches you for a decision, can its producer answer the four questions in a few sentences? If not, the number is not ready to carry the decision.


### Angle: The theory of checks & the two-axis map (`theory-of-checks`)

An error is detected only when a claim meets a comparator that was expected to agree, could fail differently, and is heeded in time.


#### `five-conditions` — Proposition 1 & the five conditions of detection

*Source tags:* FD RV

**Gist.** To detect an error is to register a disagreement between a claim and a comparator. Five conditions decide whether any check can work.

**Body.**

A **claim** asserts something about a matter of fact: a model output, a forecast, a measurement report. A **check** compares it with a **comparator** expected to agree with it: another claim, a statement fixed in advance, or an observation of the world. *Proposition 1*: an error is detected only when such a comparison shows a disagreement and someone registers it. For that, five conditions must hold:

1. **Existence:** there is a comparator bearing on the same matter.
2. **Difference:** it can *fail differently* from the claim, with respect to the cause of the error.
3. **Comparability:** the two can be brought to a point of comparison, the same quantity with its conditions stated (no laundering [→ `uncertainty-laundering`]).
4. **Timeliness:** the disagreement arrives before the consequences are fixed.
5. **Uptake:** someone registers it and has the standing to act.

**Formal core.** 

If any condition fails, `P(detected | wrong) = 0` for the errors concerned: their escape probability is 1.

**Concrete case.** 

Challenger shows several failing at once. In the data: the chart examined the night before left out the flights without O-ring damage, which hid the cold-temperature trend (difference and comparability). In the room: engineers who objected to a cold launch were overruled (uptake).

**The catch.** 

A disagreement shows that at least one side is wrong, not which. An agreement shows nothing unless the comparator could have disagreed.


#### `severity-bayes` — Severity & the false-alarm trap

*Source tags:* FD CR RV

**Gist.** A passing check is evidence only to the extent it would have failed had the claim been wrong. And when errors are rare, most alarms are false.

**Body.**

When a comparator agrees with a claim, Bayes' rule multiplies the odds that the claim is right by `P(agree | right) / P(agree | wrong)`. If the comparator would have agreed anyway, the ratio is 1: the check adds a signature and no evidence. This is Mayo's **severity** criterion: a check is worth the probability that it would have failed if the claim were wrong.

Now turn to disagreements. If a producer is wrong 1% of the time and a reviewer 10% of the time, independently, then over 90% of their disagreements are cases where the producer was right. As producers improve, a fixed checker's alarms become mostly false.

**Formal core.** 

Share of flags that are real errors (positive predictive value): `PPV = P(wrong)·s / [P(wrong)·s + (1 − P(wrong))·f]`, with *s* the checker's sensitivity and *f* its false-alarm rate. Each real error caught costs, on average, `1/PPV` investigations.

**The catch.** 

To keep uptake as producers improve, a checker must be not only independent but *precise*: its false-alarm rate has to fall roughly as fast as the producer's error rate.

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

It is tempting to say that falling error rates erode uptake by Bayes' rule alone. Bayes fixes the PPV; what people do with low-PPV alarms is behaviour. That behaviour is well documented: most people respond to alarms at a rate matching their reliability (probability matching, Bliss, Gilson and Deaton, 1995), the “cry-wolf” effect. The framework's own answer to a disagreement is neither to ignore it nor to defer, but to *resolve* it with a third comparator, at 1/PPV investigations per real error. Whether to pay that is itself an expected-utility decision, and for one-shot, high-stakes acts [→ `seu-sailboat-roulette`] it nearly always is worth paying.


#### `independence-cost-curve` — Independence is paid for in comparability (Proposition 4)

*Source tags:* FD RV

**Gist.** What a claim and its comparator share, neither can check in the other. Yet they must share something to be compared, so the checks worth having tend to be the costly ones.

**Body.**

There is no comparator independent of everything; independence is always *relative to a class of errors* (Proposition 4). And independence pulls against comparability: a copy is perfectly comparable and useless; an incommensurable view may see what you missed but cannot make its objection land. Ordered by what they share with the claim:

<div class="mt-wrap"><table class="mt"><thead><tr><th>Comparator</th><th>Shares with the claim</th><th>Can catch</th></tr></thead><tbody><tr><td>Same computation, new seed or sample</td><td>Everything but the seed</td><td>Sampling and numerical noise</td></tr><tr><td>Same method, other implementation</td><td>Equations, data, assumptions</td><td>Implementation errors</td></tr><tr><td>Other method, same model</td><td>Variables, assumptions, data</td><td>Errors specific to the method</td></tr><tr><td>Other model of the problem</td><td>The quantity, some data</td><td>Model-form errors, within shared variables</td></tr><tr><td>Experiment, operating experience</td><td>The measured quantity</td><td>Anything that moves it</td></tr><tr><td>Another discipline</td><td>Sometimes not even the quantity</td><td>The widest class, in principle</td></tr></tbody><caption>Cost tends to rise down the table: negligible, low, moderate, high, very high and slow, high plus translation work.</caption></table></div>

For the bracket: a second run of the calculation sits at the top; a colleague's model with other idealisations in the middle; a load test on an aged part, or a corrosion specialist asking what atmosphere the part will live in, at the bottom. Only the last two can reach corrosion.

**Concrete case.** 

Knight and Leveson (1986): 27 versions of a program, written separately from one specification, failed together on hard inputs far more often than independence predicts. Separate production from a shared statement does not buy independence.

**Analogy.** 

Levins (1966): “our truth is the intersection of independent lies”, provided the lies do not share an assumption (Orzack and Sober, 1993; Wimsatt, 1981).

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

“The cost of a check rises with its independence” is a strong tendency, not a law. Some comparators are cheap *and* different: an outsider's naive question (“what atmosphere will it live in?”), an order-of-magnitude or conservation-law check, a model from another family. Their cost lies in comparability, in making the objection land, which is Proposition 4's point. Hunting for these bargains is part of placing checks.


#### `two-axes-matrix` — Two axes instead of three kinds

*Source tags:* FD CR RV

**Gist.** Cross where an error's cause lies (inside or outside the frame) with whether any comparator disagrees (signalled or silent). Learned components crowd the inside-and-silent cell.

**Body.**

The three kinds of uncertainty sort errors by where their cause lies, and outside-the-frame errors look like the natural home of the most consequential failures. How learned components fail calls for a second axis: whether any comparator disagrees.

<div class="g2"><div class="h"></div><div class="h">Signalled: a comparator disagrees</div><div class="h">Silent: none does</div><div class="h">Cause inside the frame</div><div>A failing test, a crash, a residual out of bounds, a run that does not converge</div><div class="silent">A fluent wrong answer; a clean number at the end of a laundered chain</div><div class="h">Cause outside</div><div>An anomaly someone notices; a colleague's objection; a drift alarm</div><div class="silent">The turkey's last morning; a scenario no model contained</div></div>

The consequential failures are those of the silent column, in either row. *The row is decided by the frame and cannot be inspected from inside. The column is decided by what else stands nearby, and can be designed.* No method applied from inside moves an error from the bottom row to the top; adding comparators that fail differently moves errors from right to left.

**Formal core.** 

Formality does not change the row: a deduction from a poor description is still inside a poor frame. It does change the column: a frame written as a statement can serve as a comparator for whatever must conform to it, and can be read and challenged by others. Deduction and induction, stated and learned components, are equal as to the adequacy of their frames and unequal as to how their errors can be found.

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

It is tempting to say that classical software kept the inside-and-silent cell nearly empty. Too strong: classical code has many silent errors. What a stated component offers is that the cell *can be emptied in advance*: its comparator can be written and applied once, to the component. For a learned component the cell can only be emptied output by output.

**Diagnostic question.** 

Which cell does your current test suite actually cover, and what sits in the two silent cells?


### Angle: Four sources & the three-layer remedy (`three-layer-remedy`)

Where comparators come from, what automation does to each source, and how attitude, placement and organisation combine into one defence.


#### `four-sources` — Four sources of comparators

*Source tags:* FD CR RV

**Gist.** Comparators come from four sources: a statement made in advance, your own checks, another reasoner, and the world. Automation reshapes each.

**Body.**

<div class="mt-wrap"><table class="mt"><thead><tr><th>Source</th><th>Stated components</th><th>Learned components</th></tr></thead><tbody><tr><td>A statement made in advance</td><td>Systematic: verified once, in advance</td><td>Absent for the component; rebuildable around tasks that admit a mechanical check</td></tr><tr><td>Your own checks</td><td>Preserved: someone had to write the rules</td><td>Removed by default; restored only if you form a view first</td></tr><tr><td>Another reasoner</td><td>Unaffected</td><td>Cheap, but diluted by volume and correlated across users</td></tr><tr><td>The world</td><td>Unaffected</td><td>Cheap where computational; as slow as ever where physical</td></tr></tbody></table></div>

Where a task admits a mechanical check, abundant generation becomes a plain benefit: generate many candidates, keep those that pass. A proof checker, a compiler and test suite, a data schema, or a *Simplex* architecture (Sha, 2001), in which a small verified monitor keeps an unverified controller inside a safety envelope, all rebuild a guarantee *around* a learned component. Two limits: a statement checks conformity to itself (whether it says what was meant is a question for the world: verification, not validation), and it must not come from the thing it checks, as when one model writes both the code and its tests.

**Concrete case.** 

Autoformalisation: a model writes a proof in Lean, and Lean's small trusted kernel checks every step. What remains unverified shrinks from a twenty-page derivation to whether the formal statement, and the definitions it relies on, say what the human meant.

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

On Simplex and run-time assurance: the monitor is verified in advance, but the safety envelope rests on a model of the plant, which is itself a frame. Verification moves around the learned component; validation stays where it was. This is why fields whose confidence rests on validation, such as physical simulation, gain least from abundant generation.


#### `layer1-attitude` — Layer 1: attitude, comparators you supply yourself

*Source tags:* FD FP TK

**Gist.** Humility is not the residue left when methods run out. It is the earliest source of comparators, available before any other check runs.

**Body.**

Before anyone else is involved, the only comparators available are those you make. A person's frame is wider than any model they write down or prompt, so self-made comparators can reach beyond the model's frame:

- Form an order-of-magnitude expectation *before* running the model or reading the draft.
- Run a **pre-mortem**: assume the system failed badly six months from now, and write down how.
- Widen the set of possible worlds on purpose: a stress case, a dreary alternative, an “and what if we are missing something” branch (the humility buffer [→ `seu-sailboat-roulette`]).

Humility is often cast as what remains when methods run out. The order should be reversed: it is the first source of comparators, and under automation the one that disappears unless kept on purpose. And a change of attitude only holds if it is *collective*; Layer 3 [→ `layer3-organization`] is what makes it collective.

**The catch.** 

By Proposition 2, self-made comparators reach beyond the model's frame but never beyond your own. That is why this layer is necessary and never sufficient.


#### `layer2-placement` — Layer 2: placement, where, who, what, how much

*Source tags:* WG FD

**Gist.** Where guarantees on the layer end, checks on outputs must be placed deliberately: at regime boundaries, by people who understand one layer below.

**Body.**

“Keep a human in the loop” is satisfied by anyone who clicks Accept. Placement answers four questions, each tied to a condition of detection:

- **Where (timeliness):** at regime boundaries, where output stops being read and starts being relied on: it executes, commits, bills, publishes, or is quoted downstream as established.
- **Who (difference and comparability):** someone who shares the interface (the goal, the quantity) and holds an independent understanding *one layer below* it: the code under a generated program, the physics under a computed number.
- **What:** *output-checking* (“is this answer right?”) and *picture-checking* (“was this task inside the tool's competence at all?”). The second cannot be done by the tool, or by another tool sharing its frame.
- **How much:** sized to the stakes, along the cost of independence [→ `independence-cost-curve`]. Review capacity is a rate, and it should cap production.

**Concrete case.** 

Grounding and citation (retrieval-augmented generation, RAG) does not make a model truthful. It moves claims out of frozen parameters into documents a reviewer can open at the point of use, though a cited source can still fail to support the sentence attached to it.

**The catch.** 

A reviewer who cannot read one layer below the output is not weak oversight but theatre, and worse than none, because it manufactures a signature others will rely on.


#### `layer3-organization` — Layer 3: organisation, independence, status, measurement

*Source tags:* FD WG CR RV

**Gist.** Protect independent evaluative capacity as a budget line, make every claim state its status, keep a track record, and measure escape rates with seeded errors.

**Body.**

An organisation can have ten review steps on its chart and no comparator in any of them. One test cuts through: *what error could this step catch that the producer could not have caught itself?* If none, the step is a signature.

1. **Size production to independent review capacity**, and count the people able to check each domain, by name.
2. **Make every result that reaches a decision state its status**: exploratory or established, what was checked independently, under which main assumptions. A rule binding everyone removes the penalty on the team honest enough to state its conditions.
3. **Keep a track record**: record claims with their conditions, and go back when outcomes are known.
4. **Measure the escape probability**: route claims or changes with seeded errors through review, and count how many get through.

**Refinement (origin: critique/review material — use as nuance, never as "amendment").** 

The escape probability can be measured, and in some fields it is measured routinely: aviation security projects fictitious threat images into live X-ray screening (threat image projection) and tracks each screener's hit rate; EU rules attach remedial training to it. Software has mutation testing. Two limits: seeded errors measure escape only for errors someone could imagine, so they must come from a different frame than the reviewers' (a corrosion specialist seeding the structural review); and seeding works best when reviewers cannot tell seeded items from real ones.

**Diagnostic question.** 

Five questions before acting on any claim: (1) What is the comparator? (2) How can it fail differently from the claim? (3) Are the claim's conditions stated, so the two can be compared? (4) Does the comparison happen before the action? (5) Who has to listen, and will they?


## Propositions (map numbering — superseded by the content spec numbering P1–P5)

- **Map Prop. 1 — Detection needs a comparator** (`five-conditions`): An error is detected only when the claim is compared with something expected to agree with it, and the two disagree.
- **Map Prop. 2 — The frame is a common cause** (`frame-common-cause`): (a) A comparator computed from the frame’s own content cannot detect an error caused by a factor the frame omits. (b) Observations can, only if that factor varied while they were taken, and only through what the frame records.
- **Map Prop. 3 — Uncertainty is measured disagreement** (`variance-disagreement`): A quantitative statement of uncertainty summarises how far the members of a specified set of alternatives disagree; an omitted alternative contributes none.
- **Map Prop. 4 — Independence is relative, and paid for in comparability** (`independence-cost-curve`): A comparator helps against a class of errors to the extent their cause affects it differently. What claim and comparator share, neither can check in the other; and they must share something to be compared.
- **Map Prop. 5 — Chains unite blind spots; cross-checks intersect them** (`series-vs-parallel`): In a chain the blind spot contains every component’s, plus errors born at interfaces; in a cross-check it shrinks to what both share, under perfect comparison and uptake.

## Glossary (English, map version)

- **Frame** (`relevance-frame`): The finite specification a reasoner works from: which variables, categories, model class and objective count. Chosen before any inference runs.
- **Picture** (`map-territory`): The constructed representation an agent acts on. The world answers the action, not the picture.
- **Possible worlds** (`bayesian-judgment`): The situations compatible with what is known. A probability says how they are weighted.
- **Aleatory, epistemic, ontological** (`ontological-residue`): Variability treated as irreducible; doubt that more data or modelling could reduce; doubt about whether the frame itself fits.
- **Claim** (`five-conditions`): Anything that asserts a matter of fact: a model output, a forecast, a measurement report.
- **Comparator** (`five-conditions`): Whatever a claim is compared with: another claim, a statement fixed in advance, or an observation of the world.
- **Check** (`five-conditions`): A comparison between a claim and a comparator expected to agree with it.
- **Failing differently** (`independence-cost-curve`): A comparator fails differently from a claim, for a given cause of error, when that cause does not make both wrong in the same way.
- **Common-mode failure** (`frame-common-cause`): Redundant protections failing together from a cause they share.
- **Error rate** (`error-times-escape`): The probability that a claim is wrong.
- **Escape probability** (`error-times-escape`): The probability that a wrong claim reaches an action without being contradicted in time.
- **Uptake** (`five-conditions`): Someone registers a disagreement and has the standing to act on it.
- **Severity** (`severity-bayes`): A passing check is evidence only to the extent it would have failed had the claim been wrong (Mayo).
- **PPV** (`severity-bayes`): Positive predictive value: the share of a checker’s alarms that are real errors.
- **Blind spot** (`series-vs-parallel`): The set of error causes a component (a person, a team, a code, a model) cannot register.
- **Chain, cross-check** (`series-vs-parallel`): Components in series, each taking the previous output as given; or in parallel, two bearing on one claim with their disagreement registered.
- **Laundering** (`uncertainty-laundering`): Dropping a claim’s conditions at a handoff, so a conditional result arrives as an unconditional one.
- **Stated component** (`design-by-contract`): A component whose rules someone wrote, and which can be given a checkable specification: a contract.
- **Learned component** (`spec-into-data`): A component whose rules were fitted to examples and exist only as parameters.
- **Front-loaded verification** (`front-loaded-verif`): Checking a component once, against its statement, so that the check covers all future runs.
- **Verification, validation** (`four-sources`): Solving the stated problem right; stating a problem that represents reality well enough for the intended use.
- **Tell** (`loss-of-the-tell`): The visible sign of a producer’s uncertainty: hesitation, hedging, rough form.
- **Signalled, silent error** (`two-axes-matrix`): An error some comparator disagrees with; an error none does.
- **Calibration** (`calibrate-vs-gate`): Stated probabilities match observed frequencies over many cases. Distinct from the generative calibration of Kalai and Vempala.
- **SEU, p∗** (`seu-sailboat-roulette`): Subjective expected utility (Savage): choose the act with the best expected utility under your own probabilities. p∗ is the failure probability above which the risky act stops paying.
- **Sandbox, gate** (`sandboxes-and-gates`): An environment where actions have no outside effect; a point where an action waits for approval.
- **Jagged frontier** (`jagged-frontier-bcg`): The uneven, hard-to-predict boundary of a model’s competence (Dell’Acqua et al., 2023).
- **RLHF** (`steering-not-spec`): Reinforcement learning from human feedback: post-training a model on human preference judgements.
- **RAG** (`layer2-placement`): Retrieval-augmented generation: answering from documents fetched at query time, which a reviewer can open.
