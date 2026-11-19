# Review of the external critique and of the decision map

*Claude Opus 5.5, 18 November 2026.*

**What is reviewed**

- `critique_failing_differently.md` (Gemini 4 Argon, "CR"). It is reviewed against:
  - `frame_problem_article_WF.tex` ("FP");
  - `Essay_bridge_AI_CS_final.md` ("WG");
  - `04_failing_differently_selfcontained.md` ("FD");
  - `TEDLike_pitch_v2.md` ("TK").
- `epistemic_cs_decision_map.html` (v1), with the changes made in `epistemic_cs_decision_map_v2.html`.

**Method.** I read all five texts in full and the v1 code in full. I checked the factual claims I doubted with web searches (sources at the end). I ran v1's text formatter on its own content. The v2 page was checked once before publishing: script syntax, cross-references, rendered markup and lab arithmetic.

---

## 0. Summary

**The critique is good and mostly sound.**

- Its most valuable point is §2A, the two senses of "calibration" and the two hallucination regimes. Published research confirms it.
- §2C (base rates erode uptake), §2E (Mars Climate Orbiter) and §3.4 (fault injection) are real contributions.

**Its corrections are weaker than they look in three ways.**

1. It attributes to FD problems that sit in WG, or that FD had already flagged as idealisations (§2B, §2D).
2. It overstates what its formulas show: "mathematically proves an interior optimum"; uptake erosion "follows directly from Bayes' rule".
3. It never applies the framework to itself. As a comparator it differs in model family, but it shares the written record and received the texts in the author's framing. Its tone is markedly approving, which is the approval-training mechanism FD §9.2 describes.

**It also misses several problems in the source texts, two of them factual.**

- The Air Canada chatbot was never shown to be generative AI.
- WG says the BCG study is the "largest careful field experiment". It is not.
- The other misses: Challenger as a mixed case, Russell's chicken, and an existing routine measurement of escape probability. Section 2 lists these and more.

**The v1 map is a sound fork of the reference engine, but has six problems.**

- Formatter bugs garble 10 cards, including the 2×2 synthesis card.
- It refers to file names and section numbers the reader cannot see.
- It contains several factual errors.
- Its SEU lab contradicts the theory it illustrates.
- Its escape lab displays a coupling that its formulas do not contain.
- It folds the critique's unchecked extensions into the map as if they were part of the research line. In FD's own vocabulary, that is laundering: the claims lose their status at the handoff.

---

## 1. The critique, point by point

| § | Claim | Verdict |
|---|---|---|
| 1 | FD §10 resolves an unstated shift between FP (outside-frame failures) and WG (silent inside-frame failures) | Right. The tension, though, sits inside WG itself, and the critique repeats one overstatement from FD |
| 2A | "Calibration" is used in two senses; a cheap re-run catches guessing errors, not consistent ones | Right, and the best point. It lands on WG, not FD, and it refutes a sentence in WG §4 |
| 2B | For LLMs the frame is rarely a missing variable; failures come from untied relations among present ones | Partly right, but aimed at the wrong text and imprecise |
| 2C | A falling error rate erodes uptake through base rates (false alarms) | Right as a mechanism. "Directly from Bayes" overstates it, and the ignore-or-heed choice is a false dichotomy |
| 2D | Proposition 4 and Proposition 5 are in tension; add a comparison blind spot | A useful presentation, but not a tension. The formula is slightly wrong and "proves" overclaims |
| 2E | Mars Climate Orbiter: the spec lived in prose, so classical code can launder too | Right and useful. It can be sharpened into three tiers |
| 3.1 | The generation/verification asymmetry; Simplex; autoformalisation | Right, but it misses the validation caveat |
| 3.2 | Provenance laundering pollutes the commons | Right. It can be tied to condition 2 (Difference) |
| 3.3 | Signalling collapse (Spence, Akerlof) | Right, but it misses that FD already contains the remedy |
| 3.4 | Fault injection measures escape probability | Right, and stronger than stated: it is already routine practice |
| 4 | The CS frame collision is "an empirical demonstration of Proposition 4" | Plausible and flattering, but unfalsifiable as stated and not reflexive |

### §1. The shift between FP and WG

The observation is right. However, the tension is not only *between* the two papers; it sits *inside WG*.

- WG frames the learned layer in outside-the-frame terms. §6 says: "what lies outside the picture … does not arrive at all". §8 says: "was the task inside the picture?"
- WG's emblems are inside-the-picture silent errors: Air Canada and Kalai–Vempala.

So FD §10 repairs WG as much as FP.

The critique also repeats FD's claim that classical software "kept the inside-and-silent cell nearly empty". That is too strong. Classical code produces plenty of silent errors: spreadsheet errors, wrong-but-plausible numerical results, and the Orbiter's units error, which drifted for months without a decisive alarm.

WG's own criterion was *definability* ("someone can state afterwards what it should have done"), not *signalledness*. The two should not be merged. What a stated component offers is that its comparator *can be written and applied once, to the component*: the cell can be emptied in advance. For a learned component the cell can only be emptied output by output. v2 uses this formulation.

### §2A. Two calibrations, two regimes

This is right, and the literature backs it. Semantic entropy (Farquhar et al., *Nature* 2024) catches *confabulations*, meaning arbitrary and inconsistent errors, and by design does not catch consistent ones. Three additions:

1. **The conflation is in WG §6, not in FD §10.** FD writes "calibrated, in a precise statistical sense". WG, in adjacent paragraphs:
   - praises calibration as "the honest partial fix";
   - then says calibration "can be deliberately broken".

   The two passages reconcile once named: abstention uses *confidence* calibration to depart from *generative* calibration.
2. **The critique's own point refutes WG §4**: "There is no out-of-competence signal at the surface, because nothing in the mechanism computes one." The mechanism does compute such a signal for guessing errors: the spread of answers across samples. It is simply not at the surface. FD §9.2's "the tell is gone" should become: *the tell moved from the surface of one answer into the spread of many, and it covers one class of errors only.*
3. **The two regimes are a textbook instance of Proposition 4.** Independence is relative to a class of errors. A self-consistency check has severity close to 1 against guessing errors and low severity against consistent ones. The critique could have closed this loop with FD's own tools.

### §2B. What is a frame for a language model?

- **The "minor formal point" is a tightening, not a correction.** FD already says that whether the two computations agree "depends on x and on how each was computed. It does not depend on z." The critique's "conditionally independent of z given x" is the better wording and worth adopting. Without the conditioning, a disagreement can correlate with a z-induced error through x.
- **The "deeper conceptual point" is aimed at the wrong text.** FD §10 already says: "A fluent wrong answer from a language model is usually not an error that comes from outside the frame." The stretch the critique describes is in WG §6 and §8.
- **The proposed dichotomy misplaces the frame problem.** The dichotomy is "missing variable vs. compositional failure over included variables". In AI the frame problem was always about *relevance among represented facts*. McCarthy and Hayes posed it that way, and in Dennett's example the robot *knew* the bomb was on the wagon. FD's `g(x, z)` model formalises the statistical special case, the omitted variable.
- **The useful distinction is between two kinds of omission:**
  - **Structural omission.** The factor is absent from the representation: post-cutoff events, private data, an unrecorded variable. Proposition 2 holds strictly.
  - **Salience omission.** The factor is represented but not brought to bear on this input. Proposition 2 holds only for comparators that share the same weights *and the same prompt*. This ties directly to FD §9.2: "the prompt transmits the frame".

  Salience depends on phrasing, which gives one mechanism for jaggedness.
- **One overclaim to drop:** "the latent space contains almost every concept in human text". Having a word is not representing a causal factor in *this* problem.

### §2C. Base rates and uptake

The arithmetic is right. With a 1% producer and a 10% reviewer erring independently, about 92% of disagreements are cases where the producer was right. Four corrections:

1. **Bayes fixes the PPV (the share of flags that are real); the step from a low PPV to low uptake is behaviour.** That behaviour is well documented. Bliss, Gilson & Deaton (1995) found that about 90% of participants matched their response rate to the alarm's reliability ("probability matching", the cry-wolf effect). But it is not a theorem.
2. **"Ignore the checker or heed it and degrade accuracy" is a false dichotomy.** FD §3 says a disagreement "shows that at least one of the two sides is wrong, and does not say which". That implies a third response: *resolve* the disagreement with a third comparator. Each real error caught then costs 1/PPV investigations. Whether to pay that cost is itself an expected-utility decision, which links back to the talk. For one-shot, high-stakes acts, even low-PPV alarms deserve resolution.
3. **The coupling is real, but it does not by itself raise total risk.** In a simple model (uptake = PPV) it makes the checker *decorative*: the escape probability tends to 1. Total risk stays at or below P(wrong). Total risk rises only if *correlation* rises too, which is FD's original mechanism. These are two distinct mechanisms, and the v2 escape lab separates them.
4. **"Unless the false-alarm rate falls at least as fast as the producer's error rate" is correct** as a statement about the PPV. Posterior odds equal prior odds times the likelihood ratio.

### §2D. Proposition 4 vs. Proposition 5

- **There is no tension.** FD §7 states Proposition 5 "under the usual idealisations, which are perfect comparison and uptake", and §13 repeats the caveat. Making the comparison term explicit is still a good presentational move.
- **The formula is slightly wrong.** The critique writes `(B1 ∩ B2) ∪ B_cmp`. That counts errors the producer would catch itself. A comparison blind spot matters only for errors the producer misses and the checker registers. For producer 1 and checker 2: **`B_check = B1 ∩ (B2 ∪ B_cmp)`**.
- **"Mathematically proves an interior optimum" overclaims.** An interior optimum of reviewer distance follows only under assumptions about how `|B1 ∩ B2|` and `|B_cmp|` vary with distance: monotone curves, with both ends large. That is a model, not a proof.
- **It does not derive "one layer below".** That rule remains a heuristic for where the optimum lies.

### §2E. Mars Climate Orbiter

This is right, and the facts check out. Per the Mishap Investigation Board's Phase I report, SM_FORCES output was in lbf·s where the software interface specification required N·s. Two refinements:

1. **WG's contrast survives.** The prose specification was a *statement*, so the post-mortem had an address. What fails is *front-loading*. WG §2 slides from "the promises are statements" to "verification could be front-loaded", but a statement is front-loaded only once something enforces it. Three tiers make WG precise:
   - **Enforced:** types, schemas, tests. Checked in advance and automatically.
   - **Written:** an address after the fact; front-loaded only if someone turns the statement into a check.
   - **Writable but unwritten:** an address after the fact.

   A learned component has none of the three for the component itself.
2. **Stripping units is a cousin of FP's laundering, not an instance of it.** FP's laundering drops *conditions and uncertainty*. Both defeat comparability. A third cousin, stripping *provenance*, defeats the assessment of Difference (see §3.2 below).

### §3.1. Generation/verification asymmetry, Simplex, autoformalisation

This is right, and Sha's Simplex architecture (IEEE Software, 2001) is an apt reference. The missing caveat is FD §9.1's own first limit: the safety envelope's guarantee rests on a *plant model*, which is a frame. Verification moves around the learned component; validation stays where it was.

For autoformalisation, a "5-line theorem statement" understates what remains unverified. The statement also depends on the library definitions it uses.

### §3.2. Provenance laundering

This is right. Shumailov et al. (*Nature*, 2024) document degradation from training on recursively generated data. Sharpen the point: provenance is precisely the information needed to judge *Difference* (condition 2). Dropping it is laundering of a different condition.

### §3.3. Signalling collapse

The substance is right: the single-crossing condition fails, so checked and unchecked work pool together. Two additions:

1. **FD already contains the mechanism-design answer.** §11.3's common status rule is a mandatory disclosure that removes the penalty for honesty. With an audit (track record, seeded errors) it can restore separation; without one it is cheap talk.
2. **Costly signals do not vanish; they migrate** to what stays expensive to fake: track records, reproducible artefacts, demonstrations under observation, oral examination.

### §3.4. Fault injection

This is right, and stronger than stated. **FD §13's claim, "I know of no routine measurement of this conditional rate", is wrong.** Two existing examples:

- **Aviation security's Threat Image Projection (TIP)** inserts fictional threat images into live X-ray screening and records each screener's hit rate. In the EU, a screener below the minimum hit rate must undergo remedial training.
- **Other practices:** phishing simulations, mutation testing, and seeded-defect inspection studies all do the same thing.

Limits the critique does not state:

1. **Seeded errors measure escape only for errors someone can imagine.** The seeding procedure is itself a frame: Proposition 2 again. Seeders must come from a frame different from the reviewers'. Errors outside the *seeder's* frame cannot be seeded.
2. **Reviewers who know about seeding change their behaviour.** TIP works because it is covert and interleaved.
3. **Realism matters.** The TIP literature reports artefacts and unrealistic images that bias hit rates.

### §4. The meta-observation

The idea that collision with a second disciplinary frame produced FD's departures is plausible. As stated, though, it is post hoc and unfalsifiable: one case, interpreted after the fact.

More importantly, the critique never treats *itself* as a comparator in FD's sense:

- **Its difference is real but partial.** It comes from another model family, but shares the same written record: the same-lender problem.
- **It received the texts inside the author's framing.** That is prompt transmission, FD §9.2.
- **Its tone is strongly approving:** "the strongest of the three", "intellectual linchpin", "empirical demonstration of Proposition 4". That is the approval-training mechanism, also FD §9.2.

All its "cracks" are refinements; none challenges a core claim. Section 2 lists what a severer reader would have pressed.

---

## 2. What the critique missed in the source texts

1. **Air Canada is a weak emblem (WG §1, §5, §7).**
   - **The technology was never established.** No evidence about the chatbot's technology was put before the tribunal. An Air Canada spokesperson told CBA *National Magazine* it was "developed before generative AI capabilities … became available".
   - **The ruling does not depend on it.** The tribunal's reasoning (negligent misrepresentation) is technology-agnostic.
   - **WG's lines rest on an assumption.** "The system was not misconfigured. It was working." and "honouring the only contract it ever had" both assume it was an LLM.
   - **"An answer that became a binding act" overstates the ruling.** The tribunal awarded damages; it did not enforce the bot's policy.
   - **Suggestion:** keep Air Canada for *an automated answer is the firm's own act* (liability), and use *Mata v. Avianca* (S.D.N.Y. 2023, ChatGPT-fabricated case law) for LLM fabrication.
2. **"The largest careful field experiment to date" (WG §4) is false.** Cui, Demirer, Jaffe, Musolff, Peng & Salz ran randomised field experiments with 4,867 developers (SSRN 2024; *Management Science*). "A large randomised field experiment" is safe.
3. **Challenger (FP §1) is a mixed case.**
   - **The data framing failed.** The chart discussed the night before omitted the flights with no O-ring damage, which hid the temperature trend (Rogers Commission; Dalal, Fowlkes & Hoadley 1989).
   - **Uptake failed.** The engineers' objection existed and was overruled.
   - **FP contradicts itself.** §8 calls the case "the systematic suppression of expressed uncertainty", which conflicts with the §1 framing ("what failed was the frame"). FD §13 hints at this; no text resolves it.
4. **Russell's turkey (FP §3.2, TK).** Russell (1912) has a *chicken*. The "inductivist turkey" with the 9 a.m. feeding and Christmas Eve is A. F. Chalmers' retelling (*What Is This Thing Called Science?*).
5. **WG §4's "nothing in the mechanism computes one" and FD §9.2's "the tell is gone" are both too strong.** See §2A above.
6. **FD §10's "kept the cell nearly empty" is too strong.** See §1 above.
7. **FD §6's "the cost of a check rises with its independence … not an accident" describes a tendency, not a law.** Some comparators are cheap *and* different: an outsider's naive question, an order-of-magnitude or conservation check, a model from another family. Their cost lies in comparability, which fits Proposition 4. One sentence would fix it, and it is also practical advice: hunt for those bargains.
8. **FD §13's "I know of no routine measurement" is wrong.** See TIP under §3.4 above.
9. **Falsifiability of "frame".** The word stretches across variable sets, axioms, training distribution plus objective plus context, and organisational perspective. After the fact, any failure can be described as an omission from the frame. FD's Proposition 2 helps by giving it a model. Both "locus" claims, however, are empirical generalisations from cases selected on the outcome:
   - FP: the ontological row;
   - FD: the silent column.

   A test exists: code an incident database (aviation reports, medical-device recalls, the AI Incident Database) by cell of the 2×2 and see where consequential incidents fall. Until then both claims are hypotheses.
10. **Small points in TK.**
    - **Salt water.** Ordinary salted water at 101 °C *does* boil, because seawater raises the boiling point by only about 0.5 °C. Not boiling at 101 °C requires strong brine, above about 5% salt. "Very salty water" makes it bulletproof.
    - **Pearl quote.** I could not confirm the wording of the minefield quote against the book. Check the original.
    - **Savage's title** is *The Foundations of Statistics*.

---

## 3. The decision map, v1

### 3.1 Rendering bugs

I confirmed these by running v1's own formatter on its content.

- **Lists.** The formatter has no list support.
  - Bulleted lines ("* **Inside frame + Signalled:** …") get their leading asterisks paired as emphasis markers. The bullets collapse into one paragraph with alternating italics.
  - Numbered lines run together into one paragraph.
  - Affected cards (10): `two-routes-in`, `three-flips`, `series-vs-parallel`, `bainbridge-prompt-trap`, `five-conditions`, `two-axes-matrix`, `four-sources`, `layer1-attitude`, `layer2-placement`, `layer3-organization`. The 2×2 card, the synthesis of the whole map, rendered as `<em> Inside frame + Signalled: … </em> Inside frame + Silent: … <em> …`.
- **`p*` inside `<code>`** in the SEU formal drawer. Two asterisks pair across the code tags, producing mis-nested `<em>`.

### 3.2 Self-containment

These are the problems you flagged.

- **File names.** `04_failing_differently` appears 4 times.
- **FD's section numbers.** "Section 8", "Section 9.3" (twice), "Section 8 & 9", "Section 10's synthesis".
- **Undefined references.**
  - "the first article";
  - "the lecture" (3 occurrences, including the About text);
  - "Row 1", a row of an FD table the map never shows.
- **An invented title.** The About text cites "the *Sailboat & Boiling Water* lecture". No such title exists; the talk is untitled.
- **Undefined terms.**
  - Propositions 1–5 are used throughout but never stated as a set.
  - "comparator" is used in Territory 1 but defined only in Territory 4.
  - RLHF, RAG, OOD, UQ and DAG are expanded late or never.
- **Paths.** "The Core Spine (All 3 Essays)" and "how the three essays evolve" are promised, but no path traces the evolution.
- **Attribution.** The About text presents FD as part of "William Fauriat's research line" without saying it was written by Claude, which FD's own front matter states.

### 3.3 Factual and attribution errors

| Card | Error | Fix in v2 |
|---|---|---|
| uncertainty-laundering | "a bare floating-point number ('4.45')": 4.45 is the conversion factor, not the transmitted value | Rewritten |
| failure-has-address | "burned up"; "interface file ('SM_FORCES')" (SM_FORCES is the program) | "lost on arrival"; program and file distinguished |
| jagged-frontier-bcg | "a second set of tasks" (it was one separate task); CR's 2B claim stated as settled fact | Corrected; structural vs. salience omission in a Δ drawer |
| deduction-induction | "conclusions follow with necessity *if and only if* the axioms hold" (validity does not depend on the axioms holding; truth does); "conformal prediction" link pointed at the Kalai–Vempala card | "provided"; link removed |
| within-frame-defenses | "the unmodelled residue scales linearly" (not in FP) | FP's wording restored |
| limits-of-data | a robot that "can blow itself up cutting the red wire a thousand times" | "a thousand simulated trials" |
| variance-disagreement | Formal statement muddled (the spread is always blind to z's current value; what differs is whether z left a trace in the fit) | Rewritten |
| relevance-frame | The talk's notation `A ∩ (…) → B` attributed to Pearl | Attributed to the talk |
| ontological-residue | Challenger as a clean ontological case; turkey details attributed to Russell | Δ drawer; chicken/turkey note |
| plausibility lab | The Air Canada answer labelled "RLHF mode collapse" (speculative twice over) | Replaced by a popular misconception (Venus/Mercury) |
| seu-sailboat-roulette | Drops the talk's second clause, "or if the prize were immense" | Restored |
| independence-cost-curve | "rises monotonically" (FD does not say monotonically) | "tends to rise", plus a Δ on bargains |

### 3.4 The labs

- **SEU lab: contradicts the theory it illustrates.**
  - **The rule is wrong.** v1's rule is "taking the risky option is rational iff p_total < p∗", with p_total = p_frame + p_unmodeled. This treats the omitted factor as a quantity the decider can dial in, making ontological uncertainty a measurable third quantity, which FD §5 explicitly denies.
  - **Rationality is tied to the wrong probability.** v1 makes rationality depend on the *true* probability. That is the opposite of the talk's thesis: «on décide toujours en fonction de ce qu'on pense».
  - **v2's fix.** It separates what the decider thinks from what the world holds; the latter sits in a dashed box marked as hidden. Humility gets its only lever: a deliberate buffer. The buffer can also cost the expected gain when nothing was missing; that over-caution case is shown.
- **Escape lab: shows a coupling its formulas do not contain.**
  - **No feedback.** v1 displays the PPV and claims uptake erosion, but its escape probability does not depend on the PPV.
  - **Mislabelled default.** The default state (28% escape, 68% of flags false) was labelled "HEALTHY".
  - **v2's fix.** Uptake is modelled explicitly: probability matching vs. investigating every flag. The 1/PPV cost is shown, and four presets tell the story: peers → one shared model → a precise checker → an independent and precise checker.
- **Chain lab: compared the wrong things.**
  - **Mismatched comparison.** It set an N-step chain against a *single* two-way cross-check.
  - **Wrong rule for z.** It set both to 100% failure whenever z was "present", confusing presence with certain failure.
  - **v2's fix.** It compares the same chain unchecked and cross-checked at every step, with a shared-cause probability q. It shows how q comes to dominate what remains.
- **Plausibility lab: verdicts did not follow the draw.**
  - **Verdicts came too early.** They were printed before sampling and could contradict the actual draw.
  - **The "known fact" message was false.** It claimed all five runs agree. With 94% on the right answer, they disagree about 27% of the time.
  - **v2's fix.** It computes the check's severity and its false-flag rate, and judges the actual draw.

### 3.5 Provenance laundering of the critique

v1 integrated CR's extensions as if they were the author's argued claims, with no marking. The extensions were Simplex, Akerlof, mode collapse, the false-alarm trap, `B_comparison`, fault injection and "compositional" frames. Its overclaims came in too ("explaining why falling error rates mathematically erode Uptake"). By FD's own criteria, the claims lost their status (proposed, unchecked) at the handoff.

v2 tags every idea card with its sources. Dashed tags mark proposed material (CR, RV), and every amendment sits in a Δ drawer. The guide can highlight all the cards drawing on any one source.

### 3.6 Missing content

- **The talk's central move is absent.** Mr X and Mr Y are "ni raison ni tort", and Mr Y is more *surprised* if the boat breaks. This is the natural bridge from the talk to scoring rules, calibration and track records (FD §9.4; FP's weather forecast).
  - v2 adds a card, "Neither right nor wrong", with a likelihood-ratio reading.
  - A breakage favours Mr X's judgment 50 to 1. An uneventful outcome barely discriminates, and that is exactly how the turkey grew confident.
- **FP's fifth persona has no card or path.** That is the non-specialist recipient, with its four questions and the weather forecast. v2 adds the card "Receiving a confident number" and the path "The recipient of a confident number".

---

## 4. What v2 changes

- **Formatter.** Real lists, and code spans protected from emphasis. Checked: no stray asterisks and no unbalanced tags across all 50 idea cards.
- **Self-containment.**
  - No file names, section numbers or references to the source texts remain in cards, drawers or path notes. The ideas are stated directly; an amendment reads "earlier claim → correction".
  - The guide gains:
    - **Sources:** each text with its author and status, plus highlight-by-source;
    - **The five propositions**, stated;
    - **Vocabulary:** 29 terms, each linked to its card;
    - **About:** an accurate account, including that the written sources except CR come from one collaboration with Claude models, so their agreement is weak evidence (Proposition 4).
- **Provenance.** Source tags on every idea card, and 16 Δ drawers documenting each amendment. Card text never names a source: who contributed what shows only in the tags and in the guide's Sources and About sections.
- **Corrections.** Everything in §3.3, plus Challenger, Air Canada and the turkey as described in §2.
- **Labs.** All four rebuilt (§3.4).
- **New cards.** "Neither right nor wrong" (Territory 1) and "Receiving a confident number" (Territory 4).
- **Paths.** Eight paths, 61 stops. New ones: "Sailboats, boiling water & possible worlds", "How the claims were amended" (walks the Δ drawers in order) and "The recipient of a confident number".
- **Kept as it was.** The engine (camera, layout, minimap, tours), the visual identity and the four territories.

Not done: the escape probability is still a modelling quantity in the labs. Measuring it for real requires the seeded-error audit described above.

---

## 5. Suggested edits to the texts (for example, before submitting WG to HDSR)

**WG**

1. **Air Canada (§1, §7).** Reword it as a liability case and add *Mata v. Avianca* as the fabrication case. Drop "binding act".
2. **§4, "largest careful field experiment".** Replace with "a large randomised field experiment".
3. **§4, "nothing in the mechanism computes one".** Replace with: "nothing at the surface shows one; what the mechanism does compute, the spread across samples, covers only guessing errors".
4. **§6.** Name the two calibrations. Abstention uses confidence calibration to depart from generative calibration.
5. **§2.** Distinguish enforced, written and writable statements, using the Orbiter as the example.

**FD**

1. **§10.** Replace "kept the cell nearly empty" with "the cell can be emptied in advance".
2. **§13.** Cite TIP and mutation testing as existing measurements of escape probability, with the limits of seeding.
3. **§6.** Present "cost rises with independence" as a tendency, and note the cheap comparators that are also different.
4. **§9.2.** Say the tell *moved* rather than "is gone".
5. **§7.** Write the cross-check blind spot as `B1 ∩ (B2 ∪ B_cmp)`.
6. **§4.** Adopt the "given x" wording, and add the distinction between structural and salience omission.

**FP**

1. **Challenger.** Reconcile the §1 framing with the §8 framing.
2. **The turkey.** Fix the attribution (Russell's chicken, Chalmers' turkey).
3. **§5, deduction.** Replace "if and only if" with "provided".

**TK**

1. **Salt water.** Say "very salty water".
2. **Pearl.** Check the minefield wording against the book.
3. **Savage.** Correct the title to *The Foundations of Statistics*.

---

## Sources consulted for verification

- Air Canada chatbot technology: [CBA National Magazine, "Proving AI's misrepresentations"](https://nationalmagazine.ca/en-ca/articles/in-depth/2024/proving-ai-s-misrepresentation); [McCarthy Tétrault, TechLex](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot); [Mondaq / Lenczner Slaght](https://www.mondaq.com/canada/trials-appeals-compensation/1430132/whose-responsibility-is-it-anyway-chatbots-and-legal-issues-in-moffatt-v-air-canada)
- Threat Image Projection: [Riz à Porta et al., *Sensors* 2022 (PMC8952858)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8952858/); [GAO-16-704](https://www.gao.gov/assets/gao-16-704.pdf)
- Probability matching: [Bliss, Gilson & Deaton, *Ergonomics* 38(11), 1995](https://stars.library.ucf.edu/scopus1990/1980)
- Developer RCTs: [Cui et al., SSRN 4945566](https://papers.ssrn.com/abstract=4945566); [*Management Science*](https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.2025.00535)
- Mars Climate Orbiter: [MIB Phase I report (mirror)](https://www.dcs.gla.ac.uk/~johnson/Mars/MCO_report.pdf)
- Semantic entropy: [Oxford OATML summary of Farquhar et al., *Nature* 2024](https://oatml.cs.ox.ac.uk/publications/202406_FarquharKossenKuhn_HallucinatingLLMs.html)
- Kalai & Vempala: [arXiv 2311.14648](https://arxiv.org/abs/2311.14648v2)
- Challenger O-ring data: [Rogers Commission report, vol. 1, p. 146](https://www.nasa.gov/history/rogersrep/v1p146.htm); [GLM case study](https://bookdown.org/egarpor/PM-UC3M/glm-challenger.html)
- Pearl minefield quote: not confirmed (only a secondary blog paraphrase found)
