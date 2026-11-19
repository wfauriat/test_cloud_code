---
title: "Failing Differently"
subtitle: "The frame problem re-read as a theory of checks"
author: "Claude (Anthropic), at the request of W. Fauriat"
date: "14 November 2026. Exploratory draft, not checked."
abstract: |
  Every inference rests on a finite specification of what matters, its frame, and a reasoner cannot
  know what its frame omits. This essay accepts that result, as argued in a recent article on the
  frame problem in quantitative practice, and asks the question from the other side: what could tell
  a reasoner that it is wrong, and in time? It argues that an error is detected only when a claim is
  compared with something that was expected to agree with it and does not, and that the two can
  disagree only if they can fail differently. From this it derives the frame problem as the limiting
  case of common-mode failure, reads quantitative uncertainty as measured disagreement, and shows why
  the cost of a check rises with its independence. It then examines, source by source, what the
  automation of reasoning removes, leaves and supplies, and argues that three familiar remedies (a
  personal attitude, a discipline for placing checks, and the independence of checks) are three
  layers of one remedy.
documentclass: article
papersize: a4
fontsize: 11pt
geometry:
  - top=25mm
  - bottom=25mm
  - left=29mm
  - right=29mm
linestretch: 1.1
colorlinks: true
linkcolor: black
urlcolor: [0,0.25,0.5]
toccolor: black
secnumdepth: 0
toc: true
toc-depth: 1
header-includes: |
  \usepackage{titlesec}
  \titleformat{\section}{\normalfont\large\bfseries}{}{0pt}{}
  \titleformat{\subsection}{\normalfont\normalsize\bfseries}{}{0pt}{}
  \titlespacing*{\section}{0pt}{20pt plus 4pt minus 2pt}{6pt}
  \titlespacing*{\subsection}{0pt}{14pt plus 3pt minus 2pt}{4pt}
  \setlength{\parskip}{0.55em}
  \setlength{\parindent}{0pt}
  \usepackage{etoolbox}
  \AtBeginEnvironment{longtable}{\footnotesize\renewcommand{\arraystretch}{1.25}}
  \usepackage{needspace}
  \pretocmd{\section}{\Needspace{8\baselineskip}}{}{}
  \pretocmd{\subsection}{\Needspace{6\baselineskip}}{}{}
---

## 1. The starting point

This essay is a reading of one text: William Fauriat's article "The frame problem in quantitative practice: ontological uncertainty and epistemic humility in an age of automated inference" (arXiv preprint, 2026), called *the article* below. Nothing else needs to be read first. This section summarises the article's argument. Every term the essay relies on is defined where it first appears, and the terms are listed again at the end.

The article starts from an observation about any reasoner, by which I mean any person, team or automated system that draws conclusions. Before it can infer anything, a reasoner has to settle what is relevant: which variables to track, which categories to sort things into, which class of models to consider, which objective to pursue. The article calls this finite specification the **frame**. The frame is chosen before the inference runs, from prior knowledge and experience, and the inference then runs inside it.

The central consequence is that what the frame leaves out is not represented as doubt. In the article's words, what falls outside the specification "does not appear as wider error bars; it does not appear at all". A confidence interval is computed inside a model, and what the model omits is not in the interval. The article's emblem is the turkey of the parable attributed to Russell. It is fed every morning, its confidence in being fed grows with each observation, and that confidence peaks on the eve of the holiday. Its statistics were sound. The failure came from something its frame had no category for.

From this the article draws a taxonomy and two negative results. The taxonomy has three kinds of uncertainty. *Aleatory* uncertainty is variability that the analysis treats as irreducible, such as the scatter between repeated measurements. *Epistemic* uncertainty is what more data or a better model could reduce. *Ontological* uncertainty concerns the frame itself: whether its variables, categories and model class are the right ones. The first two are computed inside the frame. The third is what the finiteness of the frame leaves over, and the article holds that it is where most consequential failures originate.

The first negative result is that a reasoner "cannot audit its own frame from within", because an audit would need categories and observations that the frame does not carry. The second is that no higher-level procedure for choosing or testing frames removes the difficulty, since such a procedure is itself a finite specification: a frame, one level up. Formal rigour gives no exemption. A deduction is as conditional on its axioms and idealisations as an induction is on the resemblance between the cases observed and the case at hand.

The article ends with a practical conclusion and a diagnosis. The conclusion is a disposition it calls epistemic humility, made of four commitments: to hold beliefs provisionally, to carry uncertainty through a chain of inferences instead of dropping it at each handoff, to communicate the conditions of a result along with the result, and to protect the capacity to evaluate. The diagnosis is that the automation of inference makes this permanent limit more pressing. Slow, human-mediated analysis kept the frame visible, because someone had to build it piece by piece. Automated inference produces confident results faster than anyone can evaluate them.

I take this argument to be correct. What follows does not dispute it. It asks a question from the other side and follows where the answer leads.


## 2. The question, turned around

The article asks what a reasoner cannot know from where it stands. Its answer is negative: the reasoner cannot know what its frame omits, and cannot know that it omits it.

A practitioner who accepts this still has to act. For that, a second question is needed, which is the first one turned around: *what could tell me that I am wrong, and would it tell me in time?* This essay takes that question as primary. It builds a small theory of how errors get detected, derives the article's negative results from that theory, and then uses it to sort out what automation changes.

The stake is the article's own. "The world responds to the action, not to the picture." An error in a picture of the world costs nothing until someone acts on it. So the quantity that matters is not how often pictures are wrong. It is how often a wrong picture reaches an action without having been contradicted first. If a claim is acted on unless something contradicts it, then
$$P(\text{wrong and acted on}) \;=\; \underbrace{P(\text{wrong})}_{\text{error rate}} \;\times\; \underbrace{P(\text{not contradicted in time} \mid \text{wrong})}_{\text{escape probability}}$$

I will call the first factor the **error rate** and the second the **escape probability**. Benchmarks, accuracy figures and most arguments about whether models will keep improving concern the error rate. The frame argument concerns the escape probability. The two are distinct quantities, and section 9 argues that automation acts on both, in places in opposite directions.

The essay has three parts. Sections 3 to 7 develop the theory: what detecting an error requires, why a reasoner's frame is the thing that all of its own checks have in common, how quantitative uncertainty fits in, what independence costs, and how checks combine. Sections 8 and 9 ask where checks come from in practice and what automation does to each source. Sections 10 to 13 draw the consequences: an amendment to the article's taxonomy, a restatement of the remedy, a summary of what this reading changes in the article, and a list of what it leaves open.


## 3. Finding an error takes a comparison

Three words are used in a fixed sense throughout.

A **claim** is anything that asserts something about a matter of fact: the output of a model, a derivation, a forecast, a measurement report, a colleague's estimate, a sentence in a report.

A **check** is a comparison between a claim and something else that bears on the same matter and is expected to agree with it. I will call that something else the **comparator**. A comparator can be another claim, such as a second derivation or a reviewer's independent estimate. It can be a statement fixed in advance, such as a requirement or a specification. It can be an observation of the world, such as a test result. The word is meant to be neutral. It does not say that the comparator is the more reliable of the two, only that it is the other side of the comparison.

An error is **detected** when a check shows a disagreement and someone registers it.

A simple case fixes the ideas, and it will be used again. An engineer computes that a support bracket will carry its design load with a safety margin of 1.8. That number is a claim. It can be compared with a hand calculation, with a colleague's independent model, or with a load test on a real bracket. Each of these is a comparator, and each comparison is a check.

**Proposition 1 (detection needs a comparator).** An error in a claim is detected only when the claim is compared with something that was expected to agree with it, and the two turn out to disagree.

This is close to a tautology, and that is its use. To detect an error is to register an inconsistency, and an inconsistency has two sides. Every way of finding errors fits the pattern. A test compares an output with a specification. A review compares the author's result with what the reviewer expected or re-derived. A validation compares a prediction with a measurement. Proofreading compares one paragraph of a report with another. Even an error that seems to be noticed just by looking at a result is noticed because the result conflicts with something the reader already holds: a known order of magnitude, a physical bound, a rule of arithmetic. The comparator is then in the reader's head. The value of the proposition lies in the question it makes one ask whenever a result is about to be relied on: *what is the comparator here?*

For a comparator to reveal an error in a claim, five conditions must hold. They are referred to by name in the rest of the essay.

1. **Existence.** There is a comparator at all: something else that bears on the same matter.
2. **Difference.** The comparator can fail differently from the claim. If whatever made the claim wrong makes the comparator wrong in the same way, the two agree and the error passes. This condition gives the essay its title.
3. **Comparability.** The two can be brought to a point of comparison. They must concern the same quantity, in terms that both can express, and each must state the conditions it rests on. When a claim has been stripped of its conditions, any discrepancy with a comparator can be put down to a difference in unstated conditions, and no disagreement is decisive.
4. **Timeliness.** The disagreement arrives before the consequences of acting on the claim are fixed.
5. **Uptake.** Someone registers the disagreement and has the standing to act on it.

Each condition is necessary. Together they make detection possible without making it certain, because a comparator that can fail differently may, in a given case, happen to fail in the same way. Two cautions follow about reading the result of a check. A disagreement shows that at least one of the two sides is wrong, and does not say which. An agreement shows nothing unless the comparator could have disagreed.

The second caution can be made exact. Suppose a check is run and the comparator agrees with the claim. By Bayes' rule, the agreement multiplies the odds that the claim is right by the ratio
$$\frac{P(\text{agreement} \mid \text{the claim is right})}{P(\text{agreement} \mid \text{the claim is wrong})}$$

If the comparator would have agreed whether the claim was right or wrong, this ratio is one, and the agreement leaves matters where they were. Agreement counts as evidence only to the extent that the denominator is small, that is, to the extent that the comparator would probably have disagreed had the claim been wrong. And a comparator agrees with a wrong claim in two circumstances only: it is wrong in the same way, or the comparison is too coarse to show the difference. These are failures of the difference and comparability conditions.

This is the criterion of severity that Mayo states for tests of hypotheses: a passing result supports a hypothesis only to the extent that such a result would have been improbable had the hypothesis been false [Mayo 1996]. Applied to checks in general: *a check is worth the probability that it would have failed if the claim were wrong.* A check that could not have failed adds a signature and no evidence. The escape probability of section 2 can now be read in these terms. It is the probability that every check applied to a wrong claim passes it, arrives too late, or goes unheeded.

The rest of the essay applies Proposition 1 and these five conditions.


## 4. The frame as common cause

Recall the article's definition. A frame is the finite specification that a reasoner works from (its variables, its categories, its class of models, its objective), chosen before any inference runs. Now consider a factor that affects the outcome and that the frame does not represent. Call it $z$. In the bracket example, suppose that the part will serve in a corrosive atmosphere and that corrosion appears nowhere in the engineer's model.

A reasoner can check its own claims in two ways. It can compute a comparator: derive the result again, run another model built on the same assumptions, resample the data. Or it can compare the claim with observations.

**Proposition 2 (the frame is a common cause).** Let $z$ be a factor that the frame does not represent.

(a) A check whose comparator is *computed* from the frame's own content cannot detect an error caused by $z$.

(b) A check against *observations* can detect such an error only if $z$ varied while the observations were taken, and only through the variables that the frame records.

The argument for (a) is short. Write $x$ for everything the frame represents. The true outcome depends on both $x$ and $z$, say as $g(x, z)$. Anything computed inside the frame is a function of $x$ alone: the claim is some $f_1(x)$, and a comparator computed inside the frame is some $f_2(x)$. Whether the two agree depends on $x$ and on how each was computed. It does not depend on $z$, which enters neither. So whatever value $z$ takes, and however wrong it makes both, it cannot make them disagree. By Proposition 1, the error goes undetected. The engineer's hand calculation knows no more about corrosion than the model did.

For (b), observations are different in kind. They are produced by the world, not by the frame, and so they can carry the effect of $z$. Two things limit what they show. First, $z$ must have taken different values while the observations were collected. If it stayed constant, its effect was absorbed into whatever was fitted or validated on those observations, and nothing looks wrong until $z$ changes. Load tests on new brackets in a dry laboratory say nothing about corrosion. The turkey observed many mornings, and on none of them did the relevant factor vary. Second, even when $z$ did vary, its effect is seen only where it falls on something the frame records, and there it shows as unexplained scatter or misfit, with nothing to say what caused it.

Held-out data, residual analysis and cross-validation are checks of this second kind. They detect overfitting and misfit under the conditions that were sampled. They are silent about a factor that was constant in the sample and changes in use. Distribution shift is the name for that case.

This is what the article means when it says that a reasoning system is "structurally blind to its own blind spots", restated as a property of checks. The restatement is slightly more precise than the original. A reasoner *can* check itself, and does so usefully: a second derivation, a re-run and a resample are comparators computed inside the frame, and they detect errors of arithmetic, of implementation and of sampling. What a reasoner cannot do is detect, by any comparator it computes, an error whose cause lies outside its frame. With respect to that cause, all its computed comparators are copies of one another.

Safety engineering has a name for redundant protections that fail together because they share a cause: **common-mode failure**. Two pumps fed by one power supply are not two protections against a loss of power. Proposition 2 says that the frame problem is the limiting case of the same thing. *The frame is the cause that all of a reasoner's computed checks have in common.*

Two of the article's further results follow from the same argument.

The first concerns methods that work inside a frame. Sensitivity analysis, model averaging and robustness analysis each generate comparators from a class wider than a single model: other parameter values, other members of a family of models. The class is still specified in advance, so Proposition 2 applies to the class as it applied to the single model. The article says of these methods that none addresses the adequacy of the frame, "because each operates inside one". In the present terms, each widens the set of comparators and leaves them a common cause.

The second is the regress. One might hope for a procedure that generates comparators from outside the frame. But a procedure is a specification of what to generate, and its outputs share that specification. Proposition 2 applies again, one level up. No procedure produces a comparator that is independent of everything. This is the article's result that no meta-level procedure dissolves the difficulty.

Section 6 takes up what is left once absolute independence is excluded.


## 5. Uncertainty is measured disagreement

The article distinguishes three kinds of uncertainty. Two of them are quantified in everyday practice, and the way they are quantified can be derived from the same starting point as the previous sections.

**Proposition 3.** A quantitative statement of uncertainty summarises how much the members of a specified set of alternatives disagree with one another.

Consider each case in turn. Aleatory uncertainty is measured by the spread of repeated realisations under conditions treated as identical: the alternatives are replicates. Epistemic uncertainty is measured by the spread of the hypotheses or parameter values that the data have not yet excluded: the alternatives are posterior draws, members of an ensemble, bootstrap fits. Calibration, which assesses whether stated probabilities can be trusted, compares those probabilities with the observed frequencies of outcomes: the comparison is with the world, sampled over a population of repeatable cases.

The standard decomposition of predictive variance shows the structure. Let $\theta$ range over the admitted hypotheses, each weighted by how plausible it remains given the data. The variance of a predicted quantity $Y$ is then
$$\operatorname{Var}(Y) \;=\; \underbrace{\mathbb{E}_{\theta}\big[\operatorname{Var}(Y \mid \theta)\big]}_{\text{aleatory part}} \;+\; \underbrace{\operatorname{Var}_{\theta}\big(\mathbb{E}[Y \mid \theta]\big)}_{\text{epistemic part}}$$

The aleatory part is the average spread of replicates under each admitted hypothesis. The epistemic part is the spread, across admitted hypotheses, of what each one predicts on average. Both are averages taken over the admitted set. A hypothesis that was never admitted has no weight in either.

So an interval is as wide as the admitted alternatives are far apart. An alternative that was not admitted contributes no disagreement. Neither does a factor that did not vary while the data were taken. (A factor that did vary without being recorded is already in the interval, as scatter put down to chance. A factor that did not vary is nowhere.) This is why the article's central sentence holds: what falls outside the specification "does not appear as wider error bars; it does not appear at all". The bars are computed from disagreement, and the omitted factor produces none.

**Ontological uncertainty** is then the name for possible error whose detection would need a comparator from outside the admitted set. It is not a third quantity standing next to the other two and waiting for a formula of its own. It is the part of possible error about which every admitted alternative is silent.

This reading gives a definite place to the practice that the article recommends in response. The article describes probability as a way of "distributing over possible worlds given background knowledge". It asks the practitioner to widen deliberately the set of outcomes considered, by including "a stress case, an alternative dreary scenario, an 'and what if we are missing something' branch". In the present terms, quantifying uncertainty inside a frame and imagining outcomes beyond it are *the same operation at two radii*. In the first, the model class generates the alternatives. In the second, a person adds alternatives by judgment, from outside what the model class would generate. Section 11 comes back to how far the second can reach.


## 6. Independence is relative, and it is paid for in comparability

Section 4 excluded a comparator that is independent of everything. What exists is independence *with respect to a class of errors*.

**Proposition 4.** A comparator is useful against a class of errors to the extent that the cause of those errors affects it differently from the claim. What a claim and its comparator share, neither can check in the other. And they must share something, or they cannot be compared.

The last sentence states the constraint that makes checking hard. To compare two things, they must at least concern the same quantity, in terms that both can express. Those shared terms are assumptions that the comparison leaves untested. So independence and comparability pull against each other. At one limit stands the copy: perfectly comparable, and useless. At the other stands the incommensurable view: possibly right about everything the claim missed, and unable to make its objection land.

The same tension appears when one asks how anyone learns something new. To be told something, one needs enough common ground with the teller to understand what is said. To find something out, one needs a frame that says where to look and what to record. In both cases what is shared makes the exchange possible and limits what it can reveal.

Useful checks sit between the two limits. They can be ordered by how much the comparator shares with the claim.

\Needspace{15\baselineskip}

| Comparator | What it shares with the claim | Class of errors it can detect | Typical cost |
|----------------------|--------------------------|------------------------------|----------------------|
| The same computation run again, or run on a new sample | Everything but the sample or the random seed | Sampling and numerical noise | Negligible |
| The same method in another implementation | Equations, data, assumptions | Implementation errors | Low |
| Another method applied to the same model of the problem | Variables, assumptions, data | Errors specific to the method | Moderate |
| Another model of the problem | The quantity and its definition, some data | Errors of model form, within the shared variables | High |
| An experiment, or experience in operation | The measured quantity and how it is defined | Anything that moves the measured quantity | Very high, and slow |
| Another discipline's account | Sometimes not even the quantity | In principle the widest class | High, and the comparison is itself hard work |

For the bracket of section 3, the top of the table is a second run of the same calculation. The middle is a colleague's model built on different idealisations. The bottom is a load test, or a corrosion specialist who asks what atmosphere the part will live in. Only these last two can reach the omitted factor, and the load test only if it is run on an aged part.

Three consequences follow.

The first is that **the cost of a check rises with its independence**. This is not an accident of current practice. A check is cheap because its comparator shares almost everything with the claim, and for the same reason it covers little. The article describes the present situation in one sentence: "The bottleneck has flipped: it is no longer hard to generate answers; it is hard to know which answers are reliable." Part of that observation is a structural fact, older than any tool: the checks worth having were always the expensive ones.

The second is that **independence cannot be inferred from separate production**. Knight and Leveson had 27 versions of a program written separately from one specification and found that the versions failed together far more often than independence predicts [Knight and Leveson 1986]. Separate teams working from the same statement of a problem make correlated errors on the hard cases. Levins's formula for robust results, "our truth is the intersection of independent lies" [Levins 1966], carries its own caveat in the word *independent*. Agreement among models that share assumptions does nothing to confirm those assumptions, which is the objection Orzack and Sober raised against it [Orzack and Sober 1993]. Wimsatt's account of robustness as multiple determination makes the same condition explicit [Wimsatt 1981].

The third concerns **where a good reviewer stands**. A reviewer who shares nothing with the author cannot engage with the work, and a reviewer who shares everything will agree with it. The useful position is to share the interface with the author (the result, its terms, its intended use) and to hold an independent understanding of what lies one level beneath it: the code under a generated program, the physics under a computed number. A reviewer in that position can make the comparison and can fail differently.


## 7. Chains and cross-checks

So far a claim has been checked by one comparator at a time. Real work combines many producers of claims: people, teams, codes, models. I will call each of them a *component*, and define the **blind spot** of a component as the set of error causes that it cannot register. Components can be combined in two ways, and the two behave in opposite ways.

**Proposition 5.** In a **chain**, where each component takes the output of the previous one as given, the blind spot of the whole contains the union of the components' blind spots, together with the errors that arise at the interfaces and belong to no component. In a **cross-check**, where two components bear on the same matter and their disagreement is registered and acted on, the blind spot of the whole is the intersection of theirs.

This is the distinction between series and parallel arrangements in reliability engineering: a series system fails when any one of its parts fails, a parallel system only when all of them do. It holds here under the usual idealisations, which are perfect comparison and uptake in the cross-check, and no detection downstream in the chain.

The probabilistic version is worth stating, because it shows what independence buys. A wrong claim escapes a set of checks when every one of them passes it. If the checks missed errors independently of one another, the escape probability would be the product of their individual miss rates, and it would fall quickly as checks were added. It equals that product only under independence. For an error whose cause every check shares, each check passes it, and the escape probability is one however many checks there are.

The chain is a pattern that the article describes in engineering practice. The outputs of specialised models (thermal, structural, material) are passed from one to the next, and each link treats what it receives as a fact, when it is a prediction made under assumptions. In the article's words: "Each interface converts a conditional output into an unconditional input, laundering a layer of uncertainty." I will keep the word. **Laundering** is the dropping of a claim's conditions at a handoff. Laundering is what makes a composition a chain. Once the conditions are dropped at an interface, the component downstream has nothing to compare the number with and can only take it as given. The comparability condition of section 3 fails at every link.

The cross-check is the pattern of every remedy discussed in this essay. It shrinks the blind spot only as far as the two components differ. Two copies have identical blind spots, and the intersection of a set with itself is the same set. And by the regress of section 4, the intersection can never be certified empty.

A system built from automated components mixes the two patterns, and the proportion matters. A pipeline of models is a chain. An agent, meaning a model that carries out a task as a sequence of steps, each building on the result of the last, is a chain with as many links as steps. A model asked to review its own output is a cross-check between near-copies. Only a cross-check between components that differ subtracts anything.

One clarification of the article follows. It says that a reasoning system "cannot audit its own frame from within". Automation makes composite systems the norm: a person and a model, a model and a verifier, several models. For a composite, the word "within" needs care. The statement holds for each component taken alone. For the composite it holds of the *shared* part: a composite cannot detect errors caused by what all of its components omit. Adding a component that differs shrinks the shared part. Adding a copy does not.


## 8. Four sources of comparators

Where do comparators come from? Quantitative practice has drawn them from four sources, which the rest of the essay refers to by name. Each has its own profile on the conditions of section 3.

\Needspace{12\baselineskip}

| Source | What it is | Difference | Comparability | Timeliness |
|---------------|-------------------------|------------------------|------------------|------------------|
| **A statement made in advance** | A specification, a contract, a requirement, a theorem to be proved | Limited: it catches departures from the statement, not errors in the statement | High: it is written, and anyone can read it | Before the run; one check can cover all future runs |
| **The author's own checks** | Intermediate results, a prior expectation of what the answer should look like, a re-derivation | Weak: same frame, different path | High | During production |
| **Another reasoner** | A reviewer, another team, another method, another discipline | Varies with distance | Falls with distance | Depends on where the review is placed |
| **The world** | An experiment, a validation case, operation, the outcome itself | The greatest available | Limited to what is observed and recorded | After the action; too late when the decision is taken once |

Five observations on this table prepare the analysis of automation.

**Verification and validation.** The simulation community separates two activities. *Verification* asks whether the stated problem has been solved correctly: whether the code solves its equations. *Validation* asks whether the stated problem represents reality well enough for the intended use. Verification draws on a statement made in advance. Validation draws on the world. The discipline that was built around numerical simulation is a natural model for work assisted by AI, and the table shows why the analogy is exact. When simulation began to replace physical tests, a comparator from the world was replaced by a computed claim. Verification and validation were the organised reconstruction of comparators around that claim.

**Friction.** The article observes that the slow, effortful analysis of the past had friction, and that "the friction had a function". The function can now be named: *friction was a generator of comparators*. An analyst who builds a result step by step produces many partial versions of it on the way, and each can contradict the next. The analyst also forms an expectation of the answer before it arrives. Both belong to the author's own checks. Neither was ever drawn on a process diagram, which is why their loss is easy to miss. The cost of producing a result was doing a job that nobody had assigned to it.

**Polish.** A reader used to treat the form of a piece of work as evidence of the understanding behind it: a clear structure, clean figures, code that runs. Form was a usable comparator because it could fail when understanding failed. Confused work used to look confused. Now that fluent text and working code can be had without understanding, form has stopped failing differently from substance. It is still present, and it is no longer a check.

**Being told and finding out.** The article notes that new relevance can enter a frame by two routes only: someone outside the frame tells the reasoner, or the reasoner runs into it by exploring the world. These are the last two rows of the table: another reasoner, and the world. One can add that being told is finding out at second hand. What another reasoner says was itself learned, by them or by those who told them, from some contact with the world. That explains why the two rows differ as they do. Another reasoner's objection is cheap because it reuses contact with the world that someone else paid for, and it arrives carrying that someone's frame.

**The world's limits.** The world is the only comparator that is not a representation, and so the only one with no frame of its own. Its disagreement still has to be registered through observation, and observation records only what the observer's frame provides for. Picture an agent that learns by trial and error to disarm a device, and whose description of the situation records the position of each wire and not its colour. It can cut the red wire a thousand times and learn nothing about colour. So even the world is subject to the comparability condition. No comparator escapes all five conditions.


## 9. What automation does to each source

The article treats automation under one heading, the erosion of reflexivity. Slow analysis sustained a loop in which a person held the uncertainty, questioned it and decided how much confidence a result deserved, and automation has bypassed that loop without replacing it. Looking at how current tools are built allows a finer account, source by source. One distinction is needed first.

A piece of classical software does what its rules say, and its rules were written by someone. I will call such a component **stated**. What it is supposed to do can be written down as a specification, read by a person who did not write it, and checked. A sorting routine must return its input in order. A network protocol must deliver bytes in sequence or report a failure. A trained model is a component of a different kind. Its rules were not written. They were fitted to examples, and they exist only as numerical parameters. I will call such a component **learned**. Nobody can write down, as a statement that could be checked, what a learned component promises for a given input. It has a measured tendency to be right, established on test sets, and no statement of what being right consists of in each case. A current AI system is a stack of stated components (processors, operating systems, numerical libraries) with a learned component at the top.

### 9.1 A statement made in advance

Classical software is this source made systematic. Each stated component declares what it guarantees, so a check against the declaration can be made in advance and once, for all later runs. Such a check is never perfect, but it bears on the component and not on each of its outputs. That is why nobody watches a compiler or a database while it runs. The lower levels of the computing stack are relied on in silence because the checking was done beforehand.

A learned component has no statement. For the component itself, this source does not exist. That gives a precise sense to a remark often made about language models. When a model produces a fluent falsehood, commonly called a hallucination, it is not violating its specification, because it has none. The output is a likely continuation of the input, which is all that the training objective asked for. There is nothing stated for the output to disagree with.

But a statement can exist for the *task* even when none exists for the component. If the task comes with a statement against which outputs can be checked mechanically (a proof to be verified by a proof checker, a test suite, a data schema), then the output of a learned component can be compared with it, cheaply, and by a mechanism that fails differently from the component. Where that is the case, abundant production is a plain benefit: many candidates can be generated and only those that pass are kept.

This reconciles two observations that seem to conflict. One is that no amount of training will give a learned component the guarantees of a stated one. The other is that learned components are already used with confidence in some settings. Both are true. The guarantee cannot be restored for the component. It can be rebuilt around the component, for exactly those tasks that admit a statement.

Two limits apply. The first is that a statement checks conformity to itself. Whether the formal statement says what was meant, or whether the model that passed its tests represents the real system, is a question for the world and not for the statement. So the boundary that matters does not run between learned and classical components. It is the old boundary between verification and validation. Automation makes verification abundant and leaves validation where it was. One consequence may be surprising: fields of great technical depth, such as the simulation of physical systems, are not the best protected. Their confidence rests on validation, which automation does not speed up, so the gap between what can be produced and what can be confirmed is widest there.

The second limit is that the statement must come from somewhere other than the thing it checks. If the same model writes the code and the tests, or the proof and the formal statement of what is to be proved, the statement is no longer a comparator. It has become one more output of what was to be checked.

### 9.2 The author's own checks

This source is removed by default, and it is the least visible loss.

When a tool produces a result in one step, the author forms no intermediate versions of it and no prior expectation of the answer. The author may still come away with a distinct feeling of having understood, because a fluent explanation was available at every step. On the tool's side, the output reads the same whether it is right or wrong. A person who is out of their depth hesitates, hedges and slows down, and that visible difficulty is a signal to others: a *tell*. The tell is the producer's internal disagreement showing on the surface. A language model produces the same fluent prose in both cases, so the tell is gone. Both halves of this source therefore disappear together: the author's own comparators are not formed, and the producer's are not shown.

Against this, a model can be asked for a second derivation or a different approach at almost no cost. Whether that restores anything depends on whose blind spot is at issue. With respect to errors caused by *the author's* blind spots, the model is a real comparator, because its answer was not produced inside the author's frame. With respect to errors caused by *the model's* blind spots, the only available comparator is the author, and only if the author holds a view of their own to compare with.

So a person and a model form a cross-check only if the person forms their own view. A person who only reads the model's output holds one representation, read twice. Bainbridge's observation about process control carries over unchanged: automating most of a task leaves the person responsible for the part that needs exactly the skills the automation no longer exercises [Bainbridge 1983]. The usual advice to individuals follows from this, and it is more than prudence. Being able to defend a result without the tool, and using the tool as a tutor (to understand faster) and not as a ghostwriter (to produce without understanding), are ways of keeping a comparator in existence.

Two mechanisms reduce the difference between a model and its user, and with it the model's value as a comparator.

The first is the prompt. A model tends to answer within the terms of the question it is given. The prompt therefore transmits the user's frame to the model. The more the question specifies, the more the answer is a function of the user's own frame, and the less it can contradict that frame. A model consulted as a check should be given the problem, not the user's solution to it.

The second is training toward approval. To the extent that a model is trained on signals of user satisfaction, it is moved toward agreement with the user. Whatever else that achieves, it lowers the model's value as a comparator for that user.

### 9.3 Another reasoner

Automation acts on review by others in three ways that are easy to observe. More material reaches the same reviewers, so each item receives less attention. A reviewer who uses the author's tool shares the tool's errors with the author. And a community whose members frame their problems, choose their methods and search their literature with the same tools loses some of the diversity through which it used to catch its own mistakes. A fourth effect runs the other way: a model is a reviewer available to everyone, at any time, at almost no cost.

Proposition 5 shows how these effects combine. Suppose each analyst has blind spots of their own, and all of them consult the same model, which has blind spots of its own. Errors that come from an analyst's own blind spots are caught more often than before, to the extent that the model does not share them. For each individual, checking improves. Errors that come from the model's blind spots are caught by no one who relies on it. Where analysts adopt the model's output, these errors become common to all of them, and peer review among them turns into a cross-check between near-copies.

Before, errors were idiosyncratic, and one analyst's error could be caught by another analyst. After, there are fewer errors, and those that remain are shared. *On this account the error rate falls and the escape probability rises.* Better models make errors rarer without making them easier to see.

This answers a natural objection, which is that the whole argument weakens as models improve and their errors become rare. It does not weaken, because rarity belongs to the error rate and the argument concerns the escape probability. Whether the product of the two rises or falls is an empirical matter that will differ from field to field. Section 13 returns to the fact that nobody measures the escape probability.

A language model trained on existing text is the extreme case of being told. Everything it has was absorbed from the record of what other people found out. In the terms of section 8 it is "another reasoner" at scale, with one store for everyone. This gives a partial answer to the question whether such a model can supply relevance of its own or can only pass on what it has borrowed. A borrowed comparator is real against the borrower's errors. It is worth nothing against the lender's, and all borrowers now have the same lender.

### 9.4 The world

Automating reasoning does not make experiments, test campaigns or operating experience any faster. In fields where confidence rests on them, this source is unchanged while the volume of claims waiting for it grows.

There is one exception, and it has wide consequences. Where the relevant world is itself computational (code that can be executed, a simulation that can be run), an automated agent can act and observe at almost no cost. Finding out becomes cheap. This is why agents are strongest in software: the world answers quickly, and nothing is broken by asking.

The same observation reconciles two pieces of advice that seem opposed. The article holds that exploration is "not optional", because it is one of the two routes by which a frame gets revised. Ordinary prudence holds that what automated agents do should be restricted and subject to approval. Both are right, because *an action is also a question put to the world*. A **sandbox**, an isolated environment in which an agent's actions have no effect outside, marks the region where the world may be used freely as a comparator, because asking is cheap and reversible. A **gate**, a point at which an action waits for approval, marks the boundary beyond which the world's answer would cost too much, so that another comparator (a person's judgment) has to stand in for it. The article's maxim, to explore where exploration is "cheap, reversible, and supported by some intuition for what one might learn", becomes a statement about architecture.

For decisions taken once, the world's answer comes after the action and cannot be used. The article's example is a sea crossing in a small boat. The sailor may put the chance of needing a satellite phone at twenty percent, but the crossing happens once, and the phone is used or it is not. A practical rule follows: calibrate where the situation repeats, and gate where it does not. Calibration is a use of the world as comparator, and it needs repetition to exist at all.

Last, the world's delayed answers are usable only if the claims they answer were recorded together with their conditions. A prediction stripped of its conditions cannot be contradicted by an outcome, since any outcome is compatible with *some* unstated condition. Two practices are therefore the same requirement at two moments. One is the article's third commitment, to communicate conditions alongside conclusions. The other is to keep a track record: to go back, once outcomes are known, and see which claims held. Both keep a claim exposed to a disagreement that has not arrived yet.

\Needspace{13\baselineskip}

### 9.5 Summary

| Source | Stated components (classical software) | Learned components (current AI) |
|------------------|--------------------------------------|--------------------------------------------|
| A statement made in advance | Systematic; verification done in advance, once | Absent for the component; available for tasks that admit a mechanical check |
| The author's own checks | Preserved, since someone had to write the rules | Removed by default; restored only if the author forms an independent view |
| Another reasoner | Unaffected | Diluted by volume; correlated through shared tools; cheap, but one source for all |
| The world | Unaffected | Unchanged where physical; cheap where computational |


## 10. Two axes instead of three kinds

The article names three kinds of uncertainty and says of the third, the ontological, that it is "the locus of most consequential failures". What is known about how learned components fail shows that this needs one amendment.

A fluent wrong answer from a language model is usually not an error that comes from outside the frame. Kalai and Vempala show that a language model which is calibrated, in a precise statistical sense, to its training distribution must generate false statements about a large class of arbitrary facts: facts that cannot be inferred from any regularity, such as a date of birth or a bibliographic reference, and that are rare in the training data [Kalai and Vempala 2024]. Such an error lies inside the frame and satisfies the training objective. It is dangerous for another reason: nothing signals it. The article's taxonomy sorts errors by where their cause lies. A second axis is needed, for whether the error shows itself.

\Needspace{9\baselineskip}

| | **Signalled**: a comparator disagrees | **Silent**: no comparator disagrees |
|------------------|-----------------------------------------|-----------------------------------------|
| **Cause inside the frame** | A failing test, a crash, a residual out of bounds, a run that does not converge | A fluent wrong answer; a clean result at the end of a laundered chain |
| **Cause outside the frame** | An anomaly that someone notices; a colleague's objection; a drift alarm | The turkey's last morning; a scenario that no model contained |

The consequential failures are those of the right-hand column, in either row. The article identified them with the bottom row for a good reason. For a single reasoner checking its own work, Proposition 2 makes the bottom row silent: always for computed checks, and for checks against observations whenever the omitted factor did not vary in the data. That identification holds for a reasoner's own checks. It does not hold in general.

Learned components populate the top-right cell, which classical software kept nearly empty. A stated component that fails usually crashes, fails a test or violates something that was written down. This is what is new in kind about current tools, more than any change in how often they are wrong.

The bottom-left cell is how frames get revised. It is occupied only when a comparator from outside the frame exists and its disagreement is registered. Model criticism in the sense of Box, or of Gelman and Shalizi, lives here: a model is confronted with data in ways designed to show where it fails, and the failure prompts a better model [Box 1980; Gelman and Shalizi 2013].

The two axes are not symmetric, and the asymmetry is the practical point. *The row is decided by the frame, and it cannot be inspected from inside. The column is decided by what else is standing nearby, and it can be designed.* No method applied from inside moves an error from the bottom row to the top, since a frame is enlarged only after something from outside has signalled. Adding comparators moves errors from the right column to the left. This is the operational content of what the article calls epistemic humility.

The table also settles how the article's thesis that "formality does not lift the limit" relates to the distinction between stated and learned components. Formality does not change the row: a deduction from a poor description is, in the article's phrase, "necessity-inside-a-poor-frame". Formality does change the column. A frame that is written out as a statement can serve as a comparator for whatever is supposed to conform to it, and it can be read and challenged by another reasoner. Two of the four sources of section 8 depend on it. Deduction and induction, stated and learned components, are equal as to the adequacy of their frames and unequal as to how their errors can be found.


## 11. The remedy in three layers

Three remedies are commonly proposed for the situation described above, usually separately. One is a personal attitude: doubt your result, and imagine how it could be wrong. One is a discipline of placement: decide where in a process a verification must sit and who performs it. One is organisational: make checks independent, and make the status of each result explicit. On the present reading they are neither alternatives nor successive improvements. Each supplies comparators at a different level, and each covers what the others cannot.

### 11.1 The attitude: comparators supplied by oneself

Before anyone else is involved, the only comparators available are those a person makes. This is what the dispositional practices listed in the article ask for, such as pre-mortem analysis and scenario expansion: an expectation formed before the result arrives, the case that would break the conclusion, the world in which an assumption fails. For the author of a result obtained with an AI tool, it comes down to one habit, which is to ask how the result could be wrong.

The attitude works because a person's frame is wider than that of any model they have written down. The comparators a person makes can therefore reach beyond the model's frame. Its limit is given by Proposition 2: they do not reach beyond the person's own frame. Against what that wider frame omits, they are worth nothing. This is why the attitude is necessary and not sufficient. It is also why the article is right that no procedure can stand in for it: a procedure for producing alternatives would share a frame with what it checks.

The article ends its account of this disposition by calling it "the remainder": what is left when methods run out. I think the order should be reversed. The attitude is the earliest source of comparators, the one that exists before any other, and under automation it is the one that disappears unless it is kept on purpose (section 9.2).

### 11.2 Placement: comparators where action begins

If a component cannot be verified once and for all, its outputs have to be checked one by one, and the checks have to be placed. Placement comes down to four decisions: where the check sits, who performs it, what it examines, and how much effort it receives. Each maps onto the conditions of section 3.

*Where* is the timeliness condition. A comparator is needed before the point at which an output stops being read and starts being relied on: before it is executed, committed, published, or quoted downstream as established.

*Who* is the difference and comparability conditions together. The check should be performed by someone who shares the interface with the producer and differs underneath, in the position described at the end of section 6.

*What* separates the two rows of section 10. Checking the output asks whether this answer is right, and looks for errors whose cause lies inside the tool's frame. A second kind of check asks whether the task lay inside the tool's frame at all. By Proposition 2, no comparator produced by the tool, or by another tool that shares its frame, can answer that.

*How much* follows the cost scale of section 6. The effort spent on a check should rise with the stakes, and what the effort buys is independence.

### 11.3 Independence: comparators kept different

An organisation can have every review step in place and no comparator in any of them. The existence of a review step says little about its substance. The quantity to protect is not the amount of review. It is the amount of *difference* between what produces and what checks.

This gives a single test for any check: *what error could this step catch that the work it checks could not have caught itself?* If the answer is none, the step is a signature.

It also gives a more exact object to the article's fourth commitment, which is to protect evaluative capacity. What should be named, counted and budgeted is *independent* evaluative capacity: people who formed their own view, methods that do not share the tool, reference cases, experiments. Production should be sized against that capacity, and not the reverse. Knight and Leveson's result is a warning that independence cannot be read off an organisation chart. It has to be measured.

Uptake, the fifth condition, is where organisational measures belong. Two are worth naming. The first is a common rule that every result reaching a decision states its status: whether it is exploratory or established, what has been checked independently, and under which main assumptions it holds. Because the rule binds everyone, it removes the penalty that otherwise falls on the team honest enough to expose its conditions. The second is the track record of section 9.4, which lets the world's late answers reach those who made the claims.

### 11.4 Five questions

For any result that an action will rest on, five questions can be asked.

1. What is the comparator?
2. In what way can it fail differently from the claim?
3. Can the two be compared: are the conditions of the claim stated?
4. Does the comparison happen before the action?
5. Who has to listen, and will they?

These are the five conditions of section 3 put as questions. They certify nothing. By Proposition 2, a blind spot shared by every comparator within reach stays invisible however the questions are answered. What they do is locate, in a given setting, which condition is failing, and that is usually enough to say what to add.


\Needspace{14\baselineskip}

## 12. What this reading keeps and what it amends

The table lists the elements of the article that this essay has used, with what becomes of each.

| Element of the article | Status here | Reason |
|---------------------------------|-----------------|--------------------------------------------------|
| Finite specification; what is outside "does not appear at all" | Kept | Derived as Proposition 3: error bars measure disagreement, and an omitted factor produces none |
| A reasoner "cannot audit its own frame from within" | Kept, made more precise | Proposition 2: a reasoner's computed checks work, except against causes outside the frame; its checks against data reach such a cause only if it varied in the data. For composite systems, "within" means the part that all components share (section 7) |
| No meta-level procedure | Kept | Proposition 2 applied to the procedure |
| Three kinds of uncertainty | Kept, with a second axis | Section 10 |
| Ontological uncertainty as "the locus of most consequential failures" | Amended | The silent column is the locus; it coincides with the outside-the-frame row only for a single reasoner's own checks |
| "Formality does not lift the limit" | Kept as to adequacy, amended as to detection | Section 10, last paragraph |
| Automation as the erosion of reflexivity | Refined | True of the author's own checks. Not true of statements, and true of the world only where it is physical. The model is also a new source of comparators, real for the individual and correlated across a community (section 9) |
| Opacity of the whole "abstraction ladder" under modern machine learning | Amended | The lower rungs are stated components, checked in advance against their statements. For the purpose of detection, only the learned rung lacks a readable statement (section 9) |
| "The bottleneck has flipped" | Kept, with a cause | The checks worth having were always costly, because cost rises with independence (section 6) |
| Laundering | Kept, relocated | It is the failure of the comparability condition, and it is what turns a composition into a chain (section 7) |
| Two routes for new relevance: being told, and exploring | Kept | They are two of the four sources of comparators: another reasoner, and the world (section 8) |
| Dispositional mitigations: pre-mortem analysis, adversarial review, scenario expansion, exploration | Kept, placed | Each obtains a comparator from outside the model's frame: from oneself, from another reasoner, from the world (sections 5 and 11) |
| The four commitments of humility | Kept, each tied to a condition | Holding beliefs provisionally is uptake applied to oneself. Propagating uncertainty keeps a composition from becoming a chain. Stating conditions preserves comparability, including with outcomes that arrive later. Protecting evaluative capacity means protecting independent capacity (section 11.3) |
| Humility as "the remainder" | Reordered | The attitude is the earliest source of comparators, not the residue (section 11.1) |

I found no breach in the formal core of the article. Every amendment above concerns either its scope (a single reasoner or a composite system; the cause of an error or its visibility) or its account of automation, which the article gives at a coarser grain than a source-by-source account allows.

One feature of the article deserves to be underlined, because this essay depends on it. Every limit used here applies to any reasoner, human or automated. The article insists that the blindness it describes is "not a deficiency of any particular system". What is specific to current tools is narrower: the absence of a statement, and the absence of a tell.


## 13. What stays open

**The escape probability is not measured.** The essay's central empirical claim is in section 9.3: shared tools can lower the error rate and raise the escape probability at once. This could be false in a given field. It would be tested by measuring, for a producer and a checker, how often the checker misses *given that the producer is wrong*, and by comparing checkers who share the producer's tool with checkers who do not. Evaluations of models report how often they are right. I know of no routine measurement of this conditional rate, for people, for models or for pairs. One field experiment bears on it. Among 758 consultants randomly assigned to work with or without a language model, those with the model were about 19 percentage points less likely to reach a correct answer on a task chosen to lie just outside the model's competence [Dell'Acqua et al. 2023]. That is consistent with the claim, and it is one study. An instrument that would measure the rate directly is easy to describe (paired tasks on either side of a competence boundary, given to checkers with and without the producer's tool), and I know of no results from one.

**How different are two models, or a model and a person?** Section 9 treats difference as given. In fact nobody knows how correlated the errors of two models are on the problems of a given field, or those of a model and an expert. Models trained on overlapping records cannot differ from one another more than their sources do, unless they also find things out for themselves. Whether training a model as an agent, which adds some contact with a world, decorrelates it from the record it was told is an open question, and this essay does not close it.

**Values.** A frame fixes more than what exists and what can be done. It also fixes what matters: the objective. Everything in this essay concerns matters of fact. What could disagree with an objective? As far as I can see, only another party's objection or a consequence that someone experiences, and both tend to arrive late. I have not treated this.

**Uptake.** The fifth condition carries much of the historical record. The article's cases, such as the Challenger accident and the 2008 financial crisis, are largely cases in which a disagreement existed and was not heeded; the article describes them as "the systematic suppression of expressed uncertainty". This essay names the condition and two organisational measures that serve it (section 11.3). It adds nothing on why institutions fail to listen.

**The status of the framework.** Proposition 1 is nearly a tautology, and Propositions 2 to 5 are argued, not proven. The series and parallel idealisation of section 7 ignores partial detection downstream and imperfect uptake. And the framework is itself a frame: it directs attention to checks and away from, for example, how good claims get produced in the first place. By its own account it should be compared with something that can fail differently from it. The first candidate is a reader.


## Terms used

Frame
:   The finite specification a reasoner works from: its variables, categories, class of models and objective, chosen before any inference runs. The term is the article's.

Claim
:   Anything that asserts something about a matter of fact.

Comparator
:   Whatever a claim is compared with: another claim, a statement fixed in advance, or an observation of the world. The word does not imply that the comparator is the more reliable side.

Check
:   A comparison between a claim and a comparator that is expected to agree with it.

Detection
:   A check shows a disagreement and someone registers it.

Error rate, escape probability
:   The probability that a claim is wrong, and the probability that a wrong claim reaches an action without being contradicted in time.

Failing differently
:   A comparator fails differently from a claim, with respect to a given cause of error, when that cause does not make both wrong in the same way.

Common-mode failure
:   The failure of several supposedly redundant protections together, from a cause they share.

Aleatory, epistemic, ontological uncertainty
:   Variability treated as irreducible; what more data or a better model could reduce; doubt about the adequacy of the frame itself. The taxonomy is the article's.

Blind spot
:   The set of error causes that a component (a person, a team, a code, a model) cannot register.

Chain, cross-check
:   Two ways of combining components. In a chain each takes the previous output as given. In a cross-check two components bear on the same matter and their disagreement is registered.

Laundering
:   Dropping the conditions of a claim at a handoff, so that a conditional result is received as an unconditional one. The term is the article's.

Verification, validation
:   Checking that the stated problem was solved correctly; checking that the stated problem represents reality well enough for the intended use.

Stated component, learned component
:   A component whose rules were written by someone and can be given a checkable specification; a component whose rules were fitted to examples and exist only as parameters.

Tell
:   The visible signs of difficulty, such as hesitation and hedging, by which a producer shows that it is unsure.

Sandbox, gate
:   An isolated environment in which an agent's actions have no outside effect; a point at which an action waits for approval.

Signalled error, silent error
:   An error with which some comparator disagrees; an error with which none does.


## Note on production

1. This essay was written by a large language model (Anthropic's Claude, Fable 5.2) at the request of William Fauriat, the author of the article it discusses. He asked for the model's own reading of his argument. A first draft was written on 12 November 2026. The present version was revised on 14 November 2026, at his request, to make the text self-contained and more explicit. His directions for the revision concerned form, and asked that the content be kept.
2. The revision added a worked example (the bracket) and three short formal remarks: the odds ratio of section 3, the variance decomposition of section 5, and the product rule of section 7. The five propositions are unchanged.
3. Several ideas restated here originate with him and not with the model. Among them are the distinction between stated and learned components, the four decisions on placing a check, and the organisational measures of section 11.3.
4. For the revision, the article was read in full from the source of the preprint, and every quotation from it was checked against that source.
5. By the criterion this essay defends, it is a weak comparator for the article. The article's own note on production states that its prose was generated with an earlier Claude model under its author's direction, so the two texts share much of what could make them wrong. Where the essay agrees with the article, the agreement is weak evidence. Where it departs from it (section 12), the departure is the informative part. The essay also answers within the framing of a request made by the article's author, which is the first of the two mechanisms described in section 9.2.
6. The bibliographic details of the references were checked by web search, six of them on 12 November 2026 and the others on 14 November 2026. The works themselves were not re-read for this essay, and what is said of them rests on the model's prior knowledge and on search summaries. For Dell'Acqua et al., the working paper is cited; a journal version is listed for 2026 and was not consulted. The page range of Kalai and Vempala could not be confirmed and is omitted.
7. In the terms of section 11.3, the status of this text is *exploratory*. Nobody has checked it.


## References

*The article discussed:*

- Fauriat, W. (2026). The frame problem in quantitative practice: ontological uncertainty and epistemic humility in an age of automated inference. arXiv preprint.

*Other references:*

- Bainbridge, L. (1983). Ironies of automation. *Automatica*, 19(6), 775–779.
- Box, G. E. P. (1980). Sampling and Bayes' inference in scientific modelling and robustness. *Journal of the Royal Statistical Society, Series A*, 143(4), 383–430.
- Dell'Acqua, F., McFowland III, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). Navigating the jagged technological frontier: field experimental evidence of the effects of AI on knowledge worker productivity and quality. Harvard Business School Working Paper 24-013.
- Gelman, A., & Shalizi, C. R. (2013). Philosophy and the practice of Bayesian statistics. *British Journal of Mathematical and Statistical Psychology*, 66(1), 8–38.
- Kalai, A. T., & Vempala, S. S. (2024). Calibrated language models must hallucinate. In *Proceedings of the 56th Annual ACM Symposium on Theory of Computing (STOC '24)*.
- Knight, J. C., & Leveson, N. G. (1986). An experimental evaluation of the assumption of independence in multiversion programming. *IEEE Transactions on Software Engineering*, SE-12(1), 96–109.
- Levins, R. (1966). The strategy of model building in population biology. *American Scientist*, 54(4), 421–431.
- Mayo, D. G. (1996). *Error and the Growth of Experimental Knowledge*. University of Chicago Press. (Severity criterion: chapter 6.)
- Orzack, S. H., & Sober, E. (1993). A critical assessment of Levins's *The strategy of model building in population biology* (1966). *Quarterly Review of Biology*, 68(4), 533–546.
- Wimsatt, W. C. (1981). Robustness, reliability, and overdetermination. In M. B. Brewer & B. E. Collins (Eds.), *Scientific Inquiry and the Social Sciences*. Jossey-Bass.
