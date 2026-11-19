# Where the Guarantees End

**Why modern AI fails differently, and where the verifying step belongs**

*William Fauriat*

*Draft 2, 2026-07-25. Essay, ~4,650 words. Target venue: Harvard Data Science Review. Written venue-agnostic with light numbered references.*

---

## 1. Two post-mortems

On 23 September 1999 the Mars Climate Orbiter fired its engine to enter orbit around Mars and was
never heard from again. A ground-based program that modelled the small forces of thruster firings had
been writing its results in pound-force-seconds. The interface specification — a document, written in
advance, agreed between two teams — said newton-seconds. Every number downstream was wrong by a
factor of 4.45, the spacecraft flew too low, and the atmosphere did the rest.

The Mishap Investigation Board named the file [1]. It named a good deal else besides: a navigation
team too thin to chase discrepancies it had already noticed, anomalies that went unescalated, no
independent check on the trajectory. Root causes in engineering are usually organisational, and this
one was. But underneath sat something the organisation had failed to protect — a program, an
interface, a stated expectation, and the exact point where it was contradicted. The failure had an
address.

In February 2024 the British Columbia Civil Resolution Tribunal ordered Air Canada to compensate a
passenger who had asked the airline's website chatbot about bereavement fares. The chatbot answered
fluently and in specifics: book now, apply within ninety days, and the discount can be claimed
retroactively. The airline's actual policy said the opposite. Air Canada argued that the chatbot was
"a separate legal entity" responsible for its own words; the tribunal was unimpressed, called it
negligent misrepresentation, and awarded damages [2]. What nobody produced — what nobody could have
produced — was the place where the invented policy lived. There is no such place. The system was not
misconfigured. It was working.

Both systems failed. Only one failure has an address.

Something changed in the machinery between those two worlds, and it is not that the second system is
less mature than the first. It is that the second rests on a different kind of promise — or, more
exactly, on the deliberate absence of one. This essay is about what changed, why it cannot be patched
back, and what to build instead. The stakes are no longer confined to text on a screen: these systems
increasingly *act* — they book, execute, commit, file — and an answer that has become an act is an
answer whose errors do not wait to be read.

## 2. The stack below earned its silence

Start at the bottom, because that is where the promises come from.

A bit is not an atom of meaning. It is a physical pattern — a voltage, a charge, a magnetised region
— plus an agreement about how to read it. On these patterns a processor performs elementary
operations: add, compare, move, jump. Individually they are dumb. They are also blindingly fast and,
absent hardware fault, perfectly deterministic: the same inputs give the same outputs, on another
machine, in another decade. Everything above is those operations composed — an operating system, a
database, a compiler, a payroll run, this page. There is never a special ingredient. There is only
composition.

What makes composition survivable at that scale is a single idea, worth naming precisely because the
rest of this essay concerns what happens when it stops holding. Each layer is a **contract**: it
hides the machinery beneath it and, in exchange, promises something exact. Bertrand Meyer gave the
idea its canonical software form — a routine states what it requires of its caller and what it
guarantees in return [3] — but the practice long predates the name and runs the length of the stack.
TCP promises that bytes arrive in order or not at all. A sort function promises an ordered
permutation of its input. A file system promises that after a successful write and flush the bytes
are on the disk. The common element is that a **specification is a statement**: it can be written
down, read by someone who did not write it, checked, disputed, versioned — and violated.

That last word carries the section. This stack fails constantly, sometimes spectacularly.
Abstractions leak; components are reused outside the envelope they were built for; the Orbiter's
small-forces file was, after all, part of a mature aerospace pipeline. But notice the *kind* of
failure. In every case something stated, or statable after the fact, was contradicted, and the
contradiction sits somewhere — in a line, at an interface, in an assumption a reviewer could have
questioned. Post-mortems in this world converge on a place.

And that property bought something historic, so ordinary now as to be invisible. Because the promises
are statements, verification could be **front-loaded**: types, unit tests, code review, static
analysis, fuzzing, formal proof where the stakes justify the cost — work done ahead of time, against
a statement, then largely retired from the runtime. Nobody stands beside the payroll system watching
it add. Dijkstra's famous limit — testing shows the presence of bugs, never their absence [4] —
bounds how much certainty the front-loading buys; it does not touch whether it can be bought at all.
Call the regime **exact, inspectable, reproducible**. The stack below earned its silence.

## 3. The inversion: the specification moves into the data

For seventy years that regime had a hard edge. Software could automate only what someone could state
exactly: an unambiguous rule, written in advance, covering every case. Tasks that resist statement —
read this handwriting, judge whether this résumé fits this role, tell me what this messy document
says — sat outside. Not because they were computationally difficult, but because nobody could write
the rule.

Machine learning inverts the workflow. Instead of writing a rule and applying it to cases, you supply
the cases — examples of the *what* — and let an optimisation procedure search an enormous space of
candidate rules for one that fits them. The gain is **reach**, and it lands precisely on the tasks
that had no writable specification.

The spend is twofold, and both halves matter later. The first is the **guarantee**: a learned rule
fits the examples, and nothing whatsoever promises that it fits the world. The second is
**legibility**: the rule is millions or billions of numerical parameters. It is not a paragraph
anyone can read, diff, or review.

Hence the claim to hold onto, stated in the native idiom: **the specification did not disappear. It
moved into the data.** What was once written in reviewable code — the conditions, the exceptions, the
definition of correct — is now absorbed from a training distribution, an objective function, a
curation policy, and later from sets of human preference judgements. Sculley and colleagues made the
engineering consequence famous a decade ago: in a machine-learning system the data is a dependency at
least as load-bearing as any library, and a far less disciplined one [5]. The code-review question of
this regime is therefore no longer "what does this line do?" but **"who chose the examples?"** —
because whatever is systematic in the examples, including their omissions, becomes systematic in the
program.

It is tempting to reply that modern practice has restored the specification: system prompts,
evaluation suites, preference training, published model policies. These are real and they work, but
they are **steering**, not specification. A preference dataset is more examples — data becoming
program, one more time. Steering moves a tendency; it does not state a contract, and it inherits
Goodhart's problem, that a measure adopted as a target ceases to measure what it stood for [6] — the
mechanism behind reward hacking and specification gaming generally [7]. Steering can be excellent and
still leave nothing for anyone to read.

The general form of this claim — that every reasoning system works from a finite specification it
cannot audit from within, and that what falls outside that specification is not merely uncertain but
invisible — is the frame problem, argued at length elsewhere [8, 9]. Here the computational instance
is enough.

## 4. The new top layer

A large language model is that inversion at industrial scale, aimed at a single objective: predict
the next token — the next fragment of text, roughly a word or part of one. Training is one move
repeated at absurd volume: hide the next fragment of a document, let the model guess, measure how
wrong the guess was, nudge billions of parameters a hair in the direction that would have improved
it, repeat trillions of times over a corpus the size of a good fraction of the public internet. That
is the entire procedure. There is no later phase in which someone types in the rules of grammar.

The striking part of the result deserves stating carefully rather than mystically. Grammar, factual
association, translation, style, and behaviour that looks like step-by-step reasoning were never
programmed. They accumulated in the parameters **because they helped predict the next fragment** —
and they can be watched doing it in small open models that run on a laptop. GPT-2's
124-million-parameter version, public since 2019, can be read one layer at a time by a technique
called the logit lens, which decodes the model's running guess at every intermediate stage rather
than only at the end [10]. On a factual prompt — *the Eiffel Tower is located in the city of* — the
early layers offer generic filler, the middle layers settle on the right country, and only near the
top does the specific city emerge and harden. Nobody built that staircase. It was kept because it
paid.

Two consequences of this arrangement carry the rest of the essay.

First, **the output is optimised to be plausible.** Plausibility is the objective; truth is not. Truth
is a frequent correlate of plausibility in the training data, which is why the thing works at all.
But it follows that fluency is *uniform* across right and wrong answers. A well-formed, confident,
appropriately hedged paragraph is what the system produces when it knows, and what it produces when
it does not. There is no out-of-competence signal at the surface, because nothing in the mechanism
computes one.

Second, **the interface itself is unspecified.** Every layer below exposes a contract; this one
exposes a text box. Natural language in, probably-right out. Unspecified layers are not themselves
new — search ranking, spam filters and recommendation feeds have been unspecified, mainstream and
touched by everyone for two decades. What is new is that this one is *general-purpose* and
*compositional*. It is not a statistical component buried inside somebody's product and fenced by it,
but a layer arbitrary software now calls, for arbitrary purposes, carrying no statement of what it
requires or what it guarantees.

None of which is deflation, because the reach is real and it has been measured. In the largest
careful field experiment to date, 758 Boston Consulting Group consultants were randomised across
realistic tasks. On tasks inside the model's competence, those with access to GPT-4 completed 12.2%
more of them, 25.1% faster, and at quality rated some 40% higher; the weakest performers gained the
most [11]. Those are not marketing numbers, and this essay does not walk them back. The reach is the
whole point of the purchase. The question is what was paid.

## 5. The regime change

Between the middle of the stack and its new top, three properties flip. Not gradually, and not
independently — together, and in kind.

**What is promised.** Below: an explicit contract, stated in advance, checkable against a statement.
Above: a statistical tendency. The system is likely to be right, in a sense measurable in aggregate
over a test set and assertable about no particular answer.

**How failure presents.** Below: a definable divergence — a crash, a failing test, a wrong unit, a
number that violates an invariant someone wrote down. Above: fluent output, indistinguishable from
success *at the point of use*.

This second property has no precedent in the stack, and it is worth being exact about why. Every
earlier layer, when it broke, either broke loudly or left a trace: a segfault, a corrupted file, a
timeout, a number so wrong that whoever read it flinched. Even the quiet failures — a flipped bit, a
race condition, the Orbiter's thruster arithmetic — eventually surfaced as an inconsistency between
two things that were supposed to agree. That is the structural point: somewhere in a classical system
there are two representations of the same fact, and a discrepancy between them is detectable by
machinery rather than only by judgement. The learned layer has no second representation to disagree
with the first. It delivers its errors in the same voice, with the same grammar, at the same
confidence, in the same format, as its successes — and the only detector that has ever reliably
worked on that is a reader who already knows enough to catch it.

**Where the post-mortem lands.** Below: an address. Above: a distribution. The causes of a
hallucinated refund policy are real and they are upstream — in what the training corpus contained, in
what the objective rewarded, in what the preference data taught about being helpful under
uncertainty. But there is nothing to point at, and "fixing" it means re-steering a tendency rather
than repairing a part. You cannot merge a patch into a distribution.

The obvious objection is a good one. *Classical software has no real guarantees either.*
Specifications are rarely written; where written they are wrong; most production code is undocumented
behaviour held together by tests nobody runs. All true, and none of it touches the claim
— because the regime is defined not by anyone's diligence but by whether failure is **definable**. In
the sloppiest classical codebase, when something goes wrong, someone can state afterwards what it
should have done and locate where it did otherwise. The expectation may never have been written; it
was always *writable*. The learned layer offers nothing of the kind, and for an exact reason:

> **Hallucination is not the system breaking its contract. It is the system honouring the only
> contract it ever had.**

The confident wrong answer satisfies the objective perfectly. It is a high-probability continuation,
which is what the mechanism computes and all it was ever asked to compute. There is no violated
statement because there is no statement.

One guardrail, because the tempting version of this argument is false. The claim is *not* that
reliability degrades as you climb the stack. It plainly does not: a frontier model summarising a
document will produce fewer errors than a great deal of buggy deterministic code, and anyone who has
debugged a distributed system knows determinism is no defence against chaos. Frequency is not the
axis. The axis is what verification **can in principle do** — ahead of time, against a statement,
once, for all future runs. Below the line, the *layer* can be verified: you check the sort function,
not each sorted list, and the check covers every call that will ever be made. Above the line only
*outputs* can be checked, one at a time, after they exist. That work is real and §7 is about doing it
well. What is gone is the once-and-for-all move — and
failing to notice which of the two you are buying is what produces the characteristic unpleasant
surprise of a system that is right 95% of the time and cannot tell you which 95%.

So the certainty was not lost. It was **spent** — deliberately, in exchange for tasks that had no
writable specification and therefore sat outside software's reach for seventy years. Asking the top
layer for the guarantees of the middle is asking it to stop being the thing that was bought.

## 6. Why you cannot buy it back

The natural next hope is that this is an immaturity: bigger models, better training, a verification
layer bolted on, and the guarantees return. It is worth being exact about why they do not.

**The layer computes from a finite picture.** What the system has to work with is fixed by three
things: the distribution it was trained on, the objective it was trained against, and the material it
is handed at the moment of use. Call that the picture. It is enormous. It is also finite — and here
is the structural part: **what lies outside the picture does not arrive as wider error bars. It does
not arrive at all.** From the inside, the absence of a consideration and confidence in its
irrelevance are the same state.

**And the picture cannot audit itself.** To ask "is my picture missing something that matters here?"
is to ask a question that requires precisely the information the picture excludes. This is not a
limitation of any particular architecture; it holds of any system that filters relevance from a
finite specification, ourselves included. What is new is that the human tell — hesitation, hedging,
the visible groping of someone out of their depth — has been engineered away.

Google Flu Trends remains the cleanest emblem, and it is not even a language model. It estimated
influenza prevalence from search queries, beautifully, for years — then search behaviour changed and
it did not. Its accuracy collapsed while its confidence did not move [13]. The technical name is
distribution shift [12]; the operational description is that it went wrong quietly and on schedule.

**Calibration is the honest partial fix, and it is genuinely valuable.** A system that says "70%" and
is right about 70% of the time when it says so offers something real: a number a decision-maker can
act on, combine, and audit after the fact — and modern distribution-free methods make it cheaper than
it used to be [14]. But it has two structural edges. It prices
variability *inside* the picture: the omitted possibility gets no bars, not wider ones. And
calibration is a property of repeatable populations, whereas consequential decisions are usually
one-shot. The world does not deliver 73% of an Atlantic crossing. You sail or you do not, and the sea
answers the action, not the forecast that produced it.

For this audience the sharpest form of the argument is a theorem rather than an anecdote. Kalai and
Vempala showed that a language model *well calibrated* to its training distribution must hallucinate
on a specific and very large class of facts: the arbitrary ones, whose truth cannot be inferred from
any regularity the model could have learned — which birthday, which clause, which citation. For that
class the hallucination rate is bounded below by roughly the fraction of facts appearing exactly once
in training, the long tail, which for arbitrary particulars is most of them [15]. Later work with
Nachum and Zhang carries the point into the training pipeline: because most evaluations score an
abstention the same as a wrong answer and below a lucky guess, the optimisation demonstrably selects
for confident guessing [16].

The theorem is often over-read, so note its shape. The bound binds *calibrated* models, and
calibration can be deliberately broken: a model can be trained to abstain, to say it does not know,
to decline the long tail. That is what the second paper recommends and what an evaluation culture
scoring abstention below guessing punishes. Hallucination is therefore better described as an
equilibrium than as a curse — an entailment of calibrated prediction over a long tail, held in place
by how the field grades its own work. That is less tractable than a patch and more tractable than
fatalism, because moving it means changing an incentive shared across an industry.

A fair concession, because the progress is real: models that spend more computation at inference
time, decompose problems, and check their own work do catch a great many errors and push the
competence boundary outward. They do not change the regime. The self-check runs inside the same
picture; a model verifying its own answer is consulting the same finite specification that produced
it. The boundary moves. Its kind does not.

## 7. Place the verifying step

If verification of the layer is unavailable, verification of the output has to be *placed*. That is
the design discipline this regime demands, and "keep a human in the loop" is not it — a slogan
satisfied by anyone who clicks accept. Placement asks four questions, and each has an answer.

**Where?** At regime boundaries. Concretely: wherever un-guaranteed output stops being read and
starts being *relied on* — where it becomes an input that executes, commits, publishes, bills, or is
quoted downstream as established fact. Inside a drafting loop an error costs a minute. At the moment
output crosses into a system that acts on it, the same error acquires a blast radius. The boundary is
a real line on the architecture diagram, and it is usually not where the org chart has placed the
reviewer.

**Who?** Someone who understands **one layer below** the interface they are checking. A reviewer who
cannot read the code cannot review generated code; a reviewer without the domain cannot catch a
plausible, well-formatted, wrong number. Where that condition fails the check is not merely weak, it
is theatre — and worse than nothing, because it manufactures a signature that others downstream will
rely on. Most "human oversight" requirements now appearing in policy are silent on this condition,
and it is very nearly the whole of the matter.

**What?** Two different checks, only one of them familiar. **Output-checking** asks "is this answer
right?" That is classical review, and much of it can be automated: tests, sandboxes, schema
validation, retrieval against a source of truth, a second model as judge. **Picture-checking** asks
the other question: "was this task inside the tool's competence at all?" That one the machine cannot
perform on itself, and stacking machines does not escape it — a judge model has its own picture.
Automated verifiers are excellent placement instruments and should be used liberally, but they are
not *terminal* ones. For consequential, one-shot, or irreversible acts the last check has to be
something that can be held accountable, and machines cannot be.

**How much?** As much as generation — the part nobody budgets. The economics inverted: producing a
confident, fluent, well-structured answer now costs almost nothing, while checking one costs what it
always did in domain knowledge, attention and time. Throughput outruns scrutiny, scrutiny degrades
into spot-checking, and the result is a factory running at full speed with no quality control.

"Invest in evaluation" is one more slogan. The prescription is that evaluative capacity become a
*named quantity that something else is sized against*. Review throughput is a measurable rate; merge
rate should be capped by it rather than by how fast proposals arrive. Evaluation headcount should be
a budget line with a number on it rather than the residual after the generation budget is spent. And
the people who can actually do the checking in a given domain should be counted, by name, because
that inventory — not compute, not licences — is the real constraint on how much of this technology an
organisation can absorb safely. Organisations that read fluency as competence stop growing that
inventory at exactly the moment they need more of it.

Four patterns follow.

**The reviewer owns the diff.** For code and documents, generation is cheap and review is the
product. The discipline is that there is always an author of record and it is not the model: someone
who read the change, understands it, and answers for it.

**Ground and cite.** Retrieval moves claims out of frozen parameters and into documents a person can
open. This does not make the model more truthful; it converts unverifiable output into output that is
verifiable at the point of use. The regime boundary does not vanish — the retrieval step has a picture of its own, and a citation can be genuinely relevant and
still fail to support the sentence attached to it — but it moves close to the task, where somebody
with the domain can stand.

**Calibrate where repeatable; gate where one-shot.** Classifiers, forecasts, triage queues, anything
that runs thousands of times against a reasonably stable distribution can spend calibration
profitably: set thresholds, let the system abstain, route the uncertain cases to people. Reward
abstention in your own evaluations, since the public ones do not. But for decisions taken once and
not undone, no score substitutes for a gate, because a rate is not a promise about this instance.

**For agents, gate the action, not the answer.** A wrong answer costs the time it takes to read; a
wrong *action* executes, and its consequences compound before anyone reads anything. Giving the
least-guaranteed layer of the stack the greatest authority to act inverts the pattern that made the
stack safe. The design response is unglamorous and well understood: approval before execution for
anything irreversible, sandboxes with real boundaries rather than instructions, and an explicit
reversibility budget for what the system may do unsupervised. Air Canada is the small version of the
failure — an answer that became a binding act. Knight Capital is the large one, and it predates
language models entirely: a deployment error left a dormant code path live, and in some forty-five
minutes the firm took a loss of over $460 million [17]. The pattern is automated action outrunning
human oversight. Language models did not invent it. They generalised it to systems nobody specified.

Two field results should discipline all of the above. The BCG experiment that produced those gains
produced a second finding: on tasks deliberately placed just outside the model's competence, consultants using AI were markedly *more* likely to be wrong — by around 19
percentage points — than colleagues working without it [11]. The frontier is **jagged**. It does not
track human intuitions about difficulty, and it is invisible from inside the interaction, because the
output looks identical on both sides. Mapping it for your own tasks is a deployment activity, not an
afterthought.

And the sharpest single datum on record: METR's randomised trial of experienced open-source
developers, working in repositories they knew well, found that early-2025 AI tooling made them about
**19% slower** — while the same developers estimated afterwards that it had made them about 20%
faster [18]. That is a snapshot of particular tools at a particular moment, and METR has since said as
much. The durable finding is not the number; it is the sign error. Fluent output *feels* like
progress, and perception is not an instrument. **Measure, don't testify.**

## 8. Where the guarantees end

Return to the two post-mortems. The Orbiter's loss had an address because somebody had written down
what that interface was supposed to carry; the entire apparatus of front-loaded verification depends
on writing of that kind existing. Air Canada's chatbot had nothing to violate. The difference is not
diligence, or era, or maturity. It is that the second system's rules were never stated by anyone —
they were absorbed from data, in exchange for the ability to answer questions nobody could have
written rules for.

So the operative question shifts. For seventy years the question about a computation was *is the
answer right?*, and enormous ingenuity went into answering it in advance and permanently. The
question now is *was the task inside the picture?* — and that second question is, structurally, the
one the machine cannot answer about itself. Not yet, and not with a larger model: checking whether a
picture is missing something requires standing outside it.

That is not a gap awaiting a patch. Within this regime it is a job description. Someone has to know
where the guarantee changes, has to understand one layer below the interface they are checking, and
has to be positioned where un-guaranteed output turns into consequence — before it turns, not after.

The certainty was spent on purpose, and it bought something extraordinary. The discipline is to know
exactly what it bought, to stop expecting a refund, and to refuse to let the spending be silent.

Where the guarantees end, someone has to be standing.

---

## References

[1] Mars Climate Orbiter Mishap Investigation Board (1999). *Phase I Report*. NASA, 10 November 1999.

[2] *Moffatt v. Air Canada*, 2024 BCCRT 149 (British Columbia Civil Resolution Tribunal, 14 February
2024).

[3] Meyer, B. (1992). Applying "Design by Contract". *IEEE Computer*, 25(10), 40–51.

[4] Dijkstra, E. W. (1972). The humble programmer. *Communications of the ACM*, 15(10), 859–866.

[5] Sculley, D., Holt, G., Golovin, D., Davydov, E., Phillips, T., Ebner, D., Chaudhary, V., Young,
M., Crespo, J.-F., & Dennison, D. (2015). Hidden technical debt in machine learning systems.
*Advances in Neural Information Processing Systems*, 28.

[6] Strathern, M. (1997). "Improving ratings": audit in the British University system. *European
Review*, 5(3), 305–321. (The formulation restates Goodhart's 1975 observation.)

[7] Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Mané, D. (2016). Concrete
problems in AI safety. arXiv:1606.06565.

[8] Fauriat, W. The frame problem in quantitative practice: ontological uncertainty and epistemic
humility in an age of automated inference. Preprint.

[9] Fauriat, W. (2022). *Un discours de la méthode au XXIe siècle: Risques et limites de
l'« intelligence artificielle »*. Auto-édition. ISBN 979-10-40-50265-4.

[10] nostalgebraist (2020). Interpreting GPT: the logit lens. LessWrong, 31 August 2020. For the
method's limitations and a corrected variant, see Belrose, N., Furman, Z., Smith, L., Halawi, D.,
Ostrovsky, I., McKinney, L., Biderman, S., & Steinhardt, J. (2023). Eliciting latent predictions from
transformers with the tuned lens. arXiv:2303.08112.

[11] Dell'Acqua, F., McFowland III, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran,
S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). Navigating the jagged technological frontier:
field experimental evidence of the effects of AI on knowledge worker productivity and quality.
*Harvard Business School Working Paper* 24-013.

[12] Quiñonero-Candela, J., Sugiyama, M., Schwaighofer, A., & Lawrence, N. D. (Eds.) (2009). *Dataset
Shift in Machine Learning*. MIT Press.

[13] Lazer, D., Kennedy, R., King, G., & Vespignani, A. (2014). The parable of Google Flu: traps in
big data analysis. *Science*, 343(6176), 1203–1205.

[14] Angelopoulos, A. N., & Bates, S. (2023). Conformal prediction: a gentle introduction.
*Foundations and Trends in Machine Learning*, 16(4), 494–591.

[15] Kalai, A. T., & Vempala, S. S. (2024). Calibrated language models must hallucinate. In
*Proceedings of the 56th Annual ACM Symposium on Theory of Computing (STOC '24)*, 160–171.

[16] Kalai, A. T., Nachum, O., Vempala, S. S., & Zhang, E. (2025). Why language models hallucinate.
arXiv:2509.04664.

[17] U.S. Securities and Exchange Commission (2013). *In the Matter of Knight Capital Americas LLC*.
Administrative Proceeding File No. 3-15570, 16 October 2013.

[18] Becker, J., Rush, N., Barnes, E., & Rein, D. (2025). Measuring the impact of early-2025 AI on
experienced open-source developer productivity. METR. arXiv:2507.09089.
