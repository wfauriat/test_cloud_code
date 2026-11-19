# Course Specification Draft: Acting Through a Picture

**Status:** Decision log (sections in chronological order; §13 is the locked summary, §25 the current state). Specs locked; build infrastructure ready; first builder session (Part 0) about to start.  
**Source Corpus:** [epistemic_cs_decision_map_v2.html](file:///home/ai-user/Documents/Sandbox/review_epist_ag/epistemic_cs_decision_map_v2.html) · [epistemic_cs_decision_map_v2_structure.md](file:///home/ai-user/Documents/Sandbox/review_epist_ag/epistemic_cs_decision_map_v2_structure.md)  
**Format Goal:** Full academic-style linear course (textbook / lecture-notes monograph)

---

## 1. Audience & Pedagogical Mandate

### 1.1 Target Reader
- **Primary audience:** Non-expert, scientifically or technically literate readers (engineers, data/CS practitioners, quantitative analysts, research managers, curious generalists).
- **No assumed fluency in edge disciplines:** Readers may not remember—or may never have unified—formal logic, Bayesian probability, Savage decision theory, software contracts, or reliability engineering.
- **Explicit re-introduction of "taken-for-granted" tools:** Foundational apparatus often assumed in scientific curricula must be re-introduced cleanly on its own terms so the entire course forms one coherent conceptual vision. Core toolkit items include:
  - Deductive vs. inductive inference and conditional rules (`A ∩ (…) → B`);
  - Probability calculus (conditional probability, Bayes' rule in odds form, PPV/base rates, law of total variance, log score / likelihood ratios);
  - Interpretations of probability (frequentist frequency vs. subjective/Bayesian judgment);
  - Decision theory (Subjective Expected Utility, risk thresholds $p^*$, one-shot vs. repeated bets);
  - Software & ML primitives (pre/postconditions & Hoare triples, optimization vs. specification, generative vs. confidence calibration);
  - Signaling & systems concepts (common-mode failure, series vs. parallel reliability, Goodhart's law, Akerlof/Spence pooling).

### 1.2 Dual-Track Accessibility (Gist-First, Formal-Justified)
Every chapter, angle, and major thread should serve two reading depths simultaneously without fragmenting the prose:
1. **Intuitive / Visual-Practical Track (Mandatory first):** Ground every theoretical, methodological, epistemic, or risk claim in concrete practical examples and simple visualizations (diagrams, 2×2 tables, plotted trade-off curves, concrete scenarios like sailboats, boiling water, brackets, Mars Climate Orbiter) so a reader uncomfortable with equations grasps the *gist* and the *why*.
2. **Formal / Technical Track (Integrated & Signaled):** Present formal definitions, proofs/derivations, and technical edge cases so formally inclined readers see *how everything connects* and *why the formal apparatus is justified*, while keeping a coarse reading of the curriculum effortless.
3. **Non-disruptive Signaling:** Optional, deeper, or highly technical subsections/boxes must be clearly marked (e.g., `[Technical Note]`, `[Formal Core]`, `[Optional Deep Dive]`) so a reader can skip them without losing the main argumentative thread.

---

## 2. Structural & Narrative Architecture

### 2.1 Single Linear Narrative (With Perspective Reading Guides)
- Unlike the interactive HTML canvas, a linear book/course cannot branch dynamically; we must commit to **one single narrative ordering** of parts and chapters.
- **Logical key-unlocking rule:** Concepts must be introduced in dependency order so the reader already holds the "keys" needed to unlock each core principle or Proposition when it arrives.
- **Territory-level Foundations:** At the start of each major Part (corresponding to a territory or thematic block), lay out its foundational tools and definitions explicitly—lifting terminology ambiguity and supplying the theoretical apparatus needed to interpret the chapters that follow.

### 2.2 Chapter 0 / Introductory Session ("Charting the Map")
The course opens with a broad, accessible introductory chapter that:
- Covers the **entire scope** of the argument from start to finish in plain, "layman-friendly" prose;
- Prunes heavy formalism (keeping only very high-level intuitions where unavoidable—e.g., the pattern of inductive rules with hidden conditions, or the basic idea of expected-stakes trade-offs—without full symbolic machinery);
- Introduces key vocabulary narratively rather than through dense formal definitions;
- Closes with **suggested reading paths** tailored to different reader profiles (mirroring the 8 perspectives in the HTML map, e.g., *"Read Chapters 0, 1, 3, 6..."* for the Decision-Maker, the CS/AI Builder, the Physical Engineer, the Statistician, or the Recipient of a Confident Number).

---

## 3. Translation Requirements (From Map v2 to Course)

| Map v2 Element | Proposed Course Role | Open Question / Constraint |
| :--- | :--- | :--- |
| **4 Territories & 12 Angles** | Parts & Chapters (exact grouping depends on chosen sequence) | Should we keep the 4-part split or reorganize into 5 parts so foundations & theory of checks precede AI/automation? |
| **50 Threads** | Sections / Subsections within chapters | Some closely paired threads may merge into one cohesive section; others (e.g., probability foundations) may need expansion. |
| **5 Propositions** | Anchor theorems/principles highlighted across the text | Currently split across T1 (`Prop 2, 3`), T3 (`Prop 5`), T4 (`Prop 1, 4`). Ordering must avoid forward-reference dependency gaps. |
| **Drawers (`⊢`, `→`, `≈`, `!`, `Δ`, `?`)** | Standardized pedagogical blocks (e.g., *Case Study*, *Formal Box*, *Caveat / Nuance*, *Self-Audit Question*) | Decide how `Δ` (*Amended*, from `CR`/`RV`) is treated: woven silently into authoritative text, or preserved as explicit *"Refinements & Open Debates"* boxes? |
| **4 Interactive Labs** | Static worked figures, parameter tables, and step-by-step numerical walkthroughs (plus optional companion web links/exercises) | Needs clear 2D visual equivalents (charts/tables) for `seu`, `escape`, `chain`, and `plausibility`. |
| **29 Glossary Terms** | Defined in-line at first appearance + consolidated Glossary / Concept Index | Needs clean cross-referencing with the foundational primers. |

---

## 4. Candidate Narrative Sequences (For Discussion)

*(To be debated and converged on before drafting an outline.)*

- **Option A — The Map's Original Arc (`Epistemics → Stack & AI → Automation → Decisions & Checks`)**  
  - *Narrative logic:* Philosophical root → Computational medium → Amplification by automation → Decision & check theory as the remedy.
  - *Challenge:* Prop. 1 (`comparator`), Prop. 4 (`cost-independence`), PPV/Bayes, and `Error × Escape` appear in Part IV even though Parts I–III repeatedly rely on them. Requires either a light "Preview Toolkit" in Ch. 0 or splitting Part IV's concepts.
- **Option B — Dependency-Clean Deductive Arc (`Epistemics & Decisions → Theory of Checks → Computing Stack & AI → Automation & Institutional Remedy`)**  
  - *Narrative logic:* Build the full epistemic, probabilistic, decision-theoretic, and check-theoretic toolkit first (unlocking Propositions 1–5 cleanly); then inspect the computing stack & ML inversion through that lens; then analyze automation chains & human/collective erosion; finally synthesize the 3-layer architectural/institutional remedy.
  - *Challenge:* CS/AI readers wait until Part III for LLMs (mitigated by Ch. 0 charting the whole arc upfront).
- **Option C — Crisis-First Inductive Spiral (`Stack & AI Crisis → Epistemic Root Cause → Chains & Collective Risk → Decisions, Checks & Remedy`)**  
  - *Narrative logic:* Open with the striking empirical puzzle (classical contract reliability vs. fluent-but-wrong AI, METR sign error, BCG jagged frontier), motivate *why* via the Frame Problem & self-audit impossibility, then build the theory of checks and remedies.
  - *Challenge:* Harder to keep formal concepts cleanly scaffolded before they are first encountered.

---

## 5. Archive: Initial Author Prompt

> I'd be interesting in turning this material into a full course, academic style. Let's discuss it, don't build yet. Here, multiple paths or perspective walkthrough will not be technically possible (even if guidance can be given : namely, read chapter 1,2 then 4,6 then 9, etc...). So we will have to pick a narrative and stick with it, order it according to a particular arrangement (we may discuss alternative upfront, but then converge on a single solution). Something I'd be extra careful about is to make sure that the reader can be introduced to the different concepts in a logical order, to have the "keys" to unlock the core of the principle statement (optionnal, or very technical session can be signaled without distrupting), so that the narrative and argumentative flow can be followed : as best for the non-expert, possibly scientifically literate reader (even if core tools and notions will have to be re-introduced for clarity, and for presenting facts in a cohenrent vision, e.g. deductive / inductive logic, probability calculus, bayesian interpretation, and other notions [list is non exhaustive here] "often taken as a given in a scientific curricula" (but of particular interest to the discussion here). Also, I want than in each particular territory, the foundationnals tools and concepts are laid out properly (lifting ambiguity and providing theoretical material needed for interpretation). Also, I want that, in each chapter / angle, important thread, to display practical example as much as possible, to ground theoretical and methodological (and epistemics, and risks) in simple visualisation setting, so that two things are offered : the reader that is not moved or at ease with formality can get the "gist" and grasp the "why", before being drown in formal setting and, the reader that may be more at ease with formal setting can see how things connect and grasp the justification of the formal apparatus while it has a coarse reading of the whole course curriculum. Last, I think that it is good that an introductory covers the whole scope from the start, with a more "layman" approach, pruning too much formal setting (some may remain necessary, say inductive patterns, say SEU framework, but "equation" should be light and very high level), introducting notions in writting with describing their formal definition in details, so painting a broad picture (kind of like charting the map before walking the actual path). That introductory session could close by suggesting reading paths (for different perspectives, kind of like the paths in the html document). Try to convert my input in a first draft of specs (in makdown), paste in my initial prompt for archiving purpose. Then let us iterate on the possible sequence of notions and chapter, and anything you feel necessary to discuss before actually converging on an outline.


---

## 6. Author Refinements & Constraints (Update 1)

### 6.1 Citation, Provenance & Epistemic Hygiene (Strict Self-Containedness)
- **No internal document leakage:** Make **zero** mention of prior drafts, maps, or internal working documents (`TK`, `WG`, `FD`, `CR`, `RV`, map v1/v2, etc.) anywhere in the course text.
- **Permitted references:** Cite only:
  1. Verifiable published literature and empirical/legal cases; and
  2. The author's arXiv article: *"The frame problem in quantitative practice: ontological uncertainty and epistemic humility in an age of automated inference"*.
- **Integration of substantive refinements:** Do not frame refinements or counterarguments as "amendments" or external review deltas. Draw on their substance directly inside the prose—presenting them organically as **open discussions**, **analytical tensions**, **nuances**, or **risks** where relevant.

### 6.2 Quantitative Visualization Examples (First-Class Monograph Material)
- The quantitative examples (corresponding to the interactive models and numerical scenarios) are core course material, not optional sidebars.
- Each quantitative example should be presented **simultaneously in three forms**, treated structurally like a derivation in an academic monograph (while explicitly flagged as an illustrative *quantitative example* rather than a formal lemma or theorem):
  1. **Prose narrative** (explaining setup, intuition, and takeaway),
  2. **Figures** (clean plots/diagrams showing regimes, thresholds, and curves), and
  3. **Concrete numbers** (explicit numerical tables / worked calculations).

### 6.3 Granularity, Toolkits & Chapter Apparatus
- **Target scale:** Governed by what a self-contained argumentative structure requires; roughly **1 chapter per angle + introductory chapter (Ch. 0) + dedicated toolkit chapter(s)** (~15–18 chapters depending on how toolkits and parts are organized).
- **Chapter takeaways:** Every chapter must end with **Key Takeaways**.
- **Deferred apparatus:** Exercises, problem sets, or diagnostic checklists will be decided when building the chapters.

### 6.4 Next Step Pending
- Author is running a cross-read with another model on the three candidate narrative sequences (Options A, B, C in Section 4) before converging on the final chapter outline.

---

## 7. Archive: Author Prompt — Update 1

> Here are a few things on the specs. Do not make any mention of any previous document, other than existing citations and literature references you can verify (the only reference on my material is the arXiv article "The frame problem in quantitative practice: ontological uncertainty and epistemic humility in an age of automated inference"). So no mention of amendements between CR and RV, but the proper writting of the course can draw from these amendments in themselves (say they appear as open discussion (if relevent), or tensions, or risks (if relevent)). Quantitative visualization exemple are course material, they should appear both in text, in figures, in numbers, just like a derivation in an academic monograph, albeit a quantative exemple, not a form lemma or theorem per say. On length I am not exactly sure what will be needed for a proper self-contained argumentative structure, somehow 1 chapter per angle + introductory chapter + toolkit chapter would be ok). Chapter should indeed include key takeaways, we will see about the rest when building. Append this to the spec file, I'll also have a cross read by another model on the suggest narrative sequence options.


---

## 8. Review Notes (Update 2): Sequencing Analysis, Proposed Option D, Risks

### 8.1 Concept Dependency Constraints
A dependency trace through the material yields the following hard constraints on any linear ordering:

- **Prop. 1 → Prop. 2.** Prop. 2 ("the frame is a common cause of checks") is stated in terms of *comparators*, which Prop. 1 defines.
- **Prop. 3 depends only on the probability toolkit** (variance decomposition, admitted hypothesis set), not on the theory of checks. It belongs with the three kinds of uncertainty.
- **Props. 4 and 5 depend on Prop. 1 and the notion of a *blind spot*,** not on computing or AI. Their best examples (Knight & Leveson's N-version programming, the bracket, series/parallel reliability) need no AI background.
- **Two concepts cannot be stated before the computing material:** the *two-axes matrix* (whose point is that learned components crowd the silent, inside-the-frame cell) and the *four sources of comparators* (whose columns contrast specified and learned components).
- **Decision theory is needed from the first chapter.** "We decide on what we think" opens the argument; SEU and one-shot stakes cannot wait until a final Part.

### 8.2 Assessment of Options A, B, C
- **Option A:** violates three of the constraints above. The map's non-linear format absorbed these forward references; a linear text cannot. Not recommended.
- **Option B:** closest to dependency-clean, but (i) it cannot be fully clean, because the two-axes matrix and the four sources need the specified/learned distinction; (ii) it front-loads 5–6 chapters of abstract foundations before the material most readers came for. This affects engineers and statisticians as much as CS/AI readers, and a Ch. 0 preview only partly offsets it.
- **Option C:** the strongest opening, but as a full architecture it breaks scaffolding exactly where it matters: explaining *why* fluent-but-wrong output is dangerous requires comparators and escape probability.

### 8.3 Proposed Option D: Dependency-Ordered Arc with a Crisis Hook
B's dependency order, with three modifications:

1. **Open on C's puzzle.** Ch. 0 starts from the contrast between Mars Climate Orbiter (a failure that traces to an address) and *Mata v. Avianca* (fluent, wrong, no written contract broken), plus the METR perceived-vs-measured sign error. It then charts the whole argument and closes with reading paths.
2. **Distribute the toolkit.** Each Part opens with the primers it needs (logic and conditional rules; probability and its interpretations; contracts and Hoare triples; series/parallel reliability), with a consolidated reference appendix, instead of one monolithic toolkit chapter.
3. **Split the theory of checks along its real dependencies.** Core theory (Props. 1–5, severity/PPV, error × escape) in Part II; the two-axes matrix and the four sources move to the end of the computing Part as its synthesis.

Sketch (~17 chapters):

| Part | Chapters | Key ideas established |
| :--- | :--- | :--- |
| 0 | Ch. 0 Charting the map (opening puzzle, whole argument, reading paths) | vocabulary, narratively |
| I. Acting on a picture | primer: logic & probability · relevance and the frame · possible worlds & probability as judgment · deciding on a picture (SEU, one-shot stakes, forecast vs. forecaster) | frame, SEU, p∗, calibration (first sense) |
| II. How errors get caught | primer: conditional probability, Bayes in odds form, variance · three uncertainties (Prop. 3) · comparators & five conditions (Prop. 1) · the frame as common cause & limits of data (Prop. 2) · independence & its cost (Prop. 4), chains vs. cross-checks (Prop. 5) · severity, PPV, error × escape | all five Propositions, escape probability |
| III. The computing stack | primer: contracts & Hoare triples · how the classical stack earned its silence · the ML inversion · regime flip, jagged frontier, the two senses of calibration · **synthesis: two axes & four sources** | specified vs. learned components, the silent cell |
| IV. Composition & erosion | laundering & agents · erosion of human checks · collective blind spots & provenance | rate-vs-escape shift |
| V. Deciding & remedying | one-shot decisions revisited (calibrate vs. gate, sandboxes) · four questions for recipients · the three-layer remedy | |

**Spiral device.** Running examples (sailboat, boiling water, bracket, Orbiter) return across Parts, each return adding a layer. Example: the SEU model is introduced in Part I without the omitted factor; the quantitative example returns in Part V with the hidden factor and the humility buffer. A *running-example register* should track where each example appears and what it establishes.

### 8.4 Risks & Tensions Not Yet Covered by the Specs
1. **Provenance of the substance (highest priority).** Much of the material originates in AI-generated or AI-reviewed texts not yet verified by the author (the five Propositions, the error × escape framing, the four sources, and the refinements). Presenting them in an authored monograph with no trace of origin would enact the *provenance laundering* the course warns against; by the course's own Prop. 4, agreement among AI-assisted sources is weak evidence. This does not require citing internal drafts. It requires (a) the author reviewing and owning every Proposition before inclusion, and (b) a short methods/acknowledgements note disclosing AI assistance in developing the material.
2. **Citation verification.** Empirical specifics were drafted with model assistance and must be checked against primary sources, for example:
   - BCG / Dell'Acqua et al. figures;
   - METR −19 % / +20 %;
   - Knight Capital loss;
   - the Air Canada chatbot's technology;
   - EU threat-image-projection rules;
   - Bliss, Gilson & Deaton (1995);
   - Kalai et al. (2025);
   - Challenger chart details;
   - Russell's 1912 chicken.
   Plan this as an explicit pass.
3. **Epistemic status of the Propositions.** "Anchor theorems" overstates them: Prop. 1 is close to a tautology; the others are argued, not proven. The formal track will expose weak points: Prop. 2a's "likelihood ratio = 1 given x" (real comparators rarely condition that cleanly); the blind-spot set notation (a sketch, not a model); the suggested-but-underived optimal reviewer distance. Each Proposition needs an explicit status label, or the book's humility thesis contradicts its own presentation.
4. **Depth of the formal track.** "Formal sketches" (as in the map) versus "real models with stated assumptions" (a probabilistic blind-spot model; a decision model with an unrepresented state variable). The second roughly doubles the work on Parts II–III and is what distinguishes a monograph from an essay.
5. **Toolkit chapter vs. per-Part foundations.** §1.1/§6.3 ("dedicated toolkit chapter(s)") and §2.1 ("foundations at the start of each Part") pull in different directions; a single early toolkit chapter is where non-expert readers drop out.
6. **Audience breadth.** Re-introducing Bayes bores statisticians; Hoare triples lose managers. Reading paths help, but one *primary* reader should be named to calibrate default depth.
7. **Dating of AI evidence.** Results tied to specific models and 2023–2025 tools will date quickly; the epistemic core will not. Time-stamped evidence should live in dated case boxes, and the argument must never depend on a model generation.
8. **Terminology and notation.** Overloaded terms need one source of truth before drafting:
   - *frame*: AI sense (McCarthy–Hayes, Fodor) vs. the broader epistemic sense used here;
   - *calibration*: two senses;
   - *check*, *comparator*, *picture*, *uncertainty*: consistent use throughout.
   The Glossary should be generated from this register.
9. **Production decisions not yet made:** output format, figure toolchain, citation style, page target (rough estimate: 250–350 pages), language(s).
10. **Prescriptive tone of the remedies.** The organizational remedies rest on thinner evidence than the epistemic and technical Parts; their register (recommendations vs. hypotheses for practice) should be set explicitly.

---

## 9. Open Decisions (To Settle Before Outlining)

*Status of each decision updated at Update 9 (✔ locked, ◐ partly done, ◻ open).*

### 9.1 Narrative & Structure
- [x] **D1. Narrative sequence:** Option A, B, C, or D (§8.3); or a variant. — **✔ Option D (§13.1)**
- [x] **D2. Number and boundaries of Parts:** 4 parts (map territories) vs. 5 parts (as in Option D). — **✔ five Parts (§13.1)**
- [x] **D3. Toolkit placement:** one dedicated toolkit chapter, per-Part primers, or per-Part primers plus a reference appendix. — **✔ per-Part primers + reference appendix (§13.1)**
- [x] **D4. Placement of decision theory (SEU, one-shot stakes):** foundations (Part I), final Part, or split (basics early, omitted-factor version late). — **✔ split: Part I baseline, Part V omitted factor (§13.1)**
- [x] **D5. Placement of the two-axes matrix and the four sources:** inside the theory of checks, or as the synthesis of the computing Part. — **✔ synthesis of Part III (§13.1)**
- [x] **D6. Spiral reuse of running examples:** adopt as a deliberate device (with a running-example register) or keep each example local. — **✔ adopted, running-example register (§13.1)**
- [x] **D7. Chapter 0 opening:** crisis hook (Orbiter vs. *Mata v. Avianca*, METR) or a conceptual opening (map vs. territory). — **✔ crisis hook (outline, content spec `part0_front.md`)**

### 9.2 Epistemic Hygiene & Provenance
- [ ] **D8. Ownership of the Propositions:** author review and acceptance (or reformulation, or rejection) of each Proposition and of each refinement drawn from the critique and review material. — **◻ open: author review of P1–P5 statuses proposed in `content_spec/00_global.md` §3**
- [x] **D9. AI-assistance disclosure:** whether, where (preface, methods note, acknowledgements) and how much the development process is disclosed, consistent with §6.1. — **✔ hybrid-process disclosure in the preface (§13.4)**
- [x] **D10. Epistemic-status labelling:** adopt a label scheme (definition / result under stated assumptions / conjecture / empirical claim) and assign one to each Proposition and major claim. — **✔ scheme (§13.3); statuses proposed, pending D8**
- [ ] **D11. Citation-verification pass:** when (before outline, before drafting, per chapter) and to what standard (primary source checked, page-level references). — **◐ two-file workflow in place (§23); verification pass pending**

### 9.3 Depth & Audience
- [x] **D12. Primary reader persona:** the one profile that sets default depth. — **✔ technically literate professional (§13.2)**
- [x] **D13. Depth of the formal track:** formal sketches vs. genuine models with stated assumptions; per Part if mixed. — **✔ mixed (§13.2)**
- [x] **D14. Pedagogical block typology:** final list and names of signaled blocks (e.g., Formal Core, Case Study, Quantitative Example, Nuance & Open Discussion, Self-Audit Question), capped to a small set. — **✔ six blocks (§13.5)**
- [x] **D15. Treatment of refinements:** woven into the main prose vs. dedicated *Nuance / Open Discussion* blocks (§6.1 implies no "amendment" framing; the block format is still open). — **✔ Nuance blocks for genuine tensions, corrections in the main prose (§13.5)**
- [ ] **D16. Register of the remedies:** prescriptive recommendations vs. hypotheses for practice. — **◻ open: interim instruction in `content_spec/part5.md` (working practices with rationale and limits)**
- [x] **D17. Handling of dated AI evidence:** dated case boxes, an "as of" convention, or a separate evidence appendix. — **✔ dated `.cas` blocks (authoring conventions §9)**

### 9.4 Quantitative Examples
- [x] **D18. Canonical parameter sets:** the fixed scenarios and numbers for each of the four quantitative examples (`seu`, `escape`, `chain`, `plausibility`), so text, figures and tables agree. — **✔ `commun/parametres.py` (§21)**
- [x] **D19. Figure types per example:** e.g., threshold plot for `seu`, escape-vs-error-rate curves for `escape`, risk-vs-N for `chain`, sample histograms for `plausibility`. — **✔ 8 figures built (§21)**
- [ ] **D20. Companion material:** whether the interactive labs ship as an online companion, and how the text refers to it. — **◻ open**

### 9.5 Production
- [x] **D21. Output format:** LaTeX, Markdown, Quarto, other. — **✔ Option 3, pandoc Markdown (§15)**
- [x] **D22. Figure toolchain:** matplotlib, TikZ/pgfplots, other. — **✔ Python/matplotlib (§15, §21)**
- [ ] **D23. Citation style and bibliography management.** — **◻ open: pandoc default style for now**
- [ ] **D24. Length target:** pages or words, overall and per chapter. — **◻ open: indicative chapter lengths in the content spec (≈ 300 pages)**
- [x] **D25. Language(s):** English only, French only, or bilingual (and in which order). — **✔ French (§13.6)**
- [x] **D26. Terminology and notation register:** create before drafting; Glossary generated from it. — **✔ `commun/registre_termes.md` (§23)**
- [ ] **D27. Exercises / problem sets / diagnostic checklists:** include or not, and in which chapters (deferred per §6.3; decide before chapter drafting). — **◻ open**

---

## 10. Archive: Author Prompt — Update 2

> I've iterated a bit with another model to build specs to build a proper academic monograph from the material that has been supplied into the artifact. You can read the specs at @course_specs_draft.md. Now I want you to have a re-read of these specs, maybe raising a warning on difficulties you feel have been omited, or what you percieve as risk or tension. And in particular, I want to have your take on possible option for a narrative flow (3 options so far). What do you think about them, do you favor one, do you feel another solution would be better ?

> yes, append it to the spec file, and list what has to be decided


---

## 11. Review Notes (Update 3): Assessment of Option D & Refinements

### 11.1 Verdict on Option D
Option D (§8.3) is the strongest narrative architecture so far—strictly preferable to Options A, B, and C:
- **Exact dependency alignment:** Splitting `two-axes-matrix` and `four-sources` out of the core check-theory Part and placing them as the **synthesis of Part III (The computing stack)** solves a real dependency violation in Option B, since both frameworks depend on the *stated vs. learned* component distinction. Meanwhile, Props. 1–5, severity/PPV, and `error × escape` depend on no AI concepts and unlock Parts III–V cleanly.
- **Pacing balance:** Opening Ch. 0 on the crisis contrast (*Mars Climate Orbiter* vs. *Mata v. Avianca* and the METR sign error) gives engineering and CS/AI practitioners immediate motivation without sacrificing scaffolding.
- **Pedagogical fit:** Distributed primers + spiral reuse of running examples embody the course's central theme (frame revision through new context).

### 11.2 Three Structural Refinements to Option D
1. **Unify the probability primer in Part I (avoid splitting it across Parts I and II).**
   - In §8.3, Part I lists *"logic & probability"* while Part II lists *"conditional probability, Bayes in odds form, variance"*. Yet Part I's `possible worlds` and `forecast vs. forecaster` (`neither-right-nor-wrong`) already rely on $\Pr(B \mid A)$, likelihood ratios ($0.05/0.001 = 50$), and logarithmic surprise ($-\ln \Pr$).
   - *Adjustment:* Place one unified **Logic, Conditioning & Bayes Primer** at the front of Part I (conditional rules `A ∩ (…) → B`, subjective vs. frequentist probability, $\Pr(B \mid A)$, Bayes in odds form, log score). Part II then needs only a compact **Variance & Reliability Primer** (law of total variance + series/parallel events) immediately before Prop. 3 and Prop. 5.
2. **Account for all Part II threads and guard against Part II feeling overly abstract.**
   - Including `within-frame-defenses`, `meta-nfl`, and `two-routes-in` makes Part II the heaviest block (~6 chapters) before reaching computing.
   - *Adjustment:* Ground every Part II chapter heavily in **non-AI physical, statistical, and engineering cases** (bracket corrosion, *Challenger*, medical screening PPV, *Knight & Leveson* 27-version programming, multiphysics chains) so Part II reads as general systems & quantitative reliability rather than delayed AI setup.
3. **Explicit spiral mapping for the four quantitative examples:**
   - **`seu`:** Baseline stakes & $p^*$ in **Part I** → revisited with hidden omitted factor $z$ and humility buffer $b$ in **Part V**.
   - **`escape`:** Fixed single checker, PPV, and probability matching in **Part II** → revisited with falling $P(\text{wrong})$ and rising common-mode sharing $c$ in **Part IV**.
   - **`chain`:** Idealised series vs. parallel reliability (Prop. 5) in **Part II** → revisited with laundering and multi-step agent trajectories in **Part IV**.
   - **`plausibility`:** Lives in **Part III** (Kalai–Vempala & semantic entropy).

### 11.3 Key Spec Tension to Resolve Explicitly (§6.1 vs. §8.4.1)
- §6.1 prohibits citing prior drafts/maps (`TK`, `WG`, `FD`, `CR`, `RV`), permitting only verifiable published literature plus the author's arXiv preprint.
- §8.4.1 warns that omitting AI-assistance provenance from the monograph would enact *provenance laundering* against the course's own principles.
- *Resolution path:* Keeping §6.1's ban on internal draft citations is compatible with adding a concise **Methodological / Acknowledgements Note** disclosing AI assistance during exploratory drafting and stress-testing, paired with explicit author review, ownership, and epistemic-status labelling of the five Propositions (**D8–D10**).

---

## 12. Archive: Author Prompts — Update 3

> read the critique that has been appended to the @course_specs_draft.md by another model. What do you think about the option D suggestion ?

> ok. append you critique and I will lead from the other model last read

---

## 13. Locked Decisions (Update 4)

### 13.1 Narrative Architecture (D1–D6: locked)
- **Sequence: Option D** (§8.3), with the §11.2 refinements:
  - a single **Logic, Conditioning & Bayes Primer** at the front of Part I (conditional rules, interpretations of probability, Pr(B | A), Bayes in odds form, likelihood ratio, log score);
  - **base rates and PPV** introduced in Part II, just before severity (not in the Part I primer);
  - a compact **Variance & Reliability Primer** in Part II (law of total variance, series/parallel events);
  - Part II grouped into five chapters:
    1. three uncertainties, error bars as disagreement, within-frame robustness tools;
    2. comparators and the five conditions;
    3. the frame as common cause: limits of data, the meta-level regress, how new relevance enters;
    4. independence and its cost, chains vs. cross-checks;
    5. severity, PPV, error × escape;
  - Part II grounded in non-AI cases (bracket corrosion, *Challenger*, medical screening, Knight & Leveson, multiphysics chains);
  - spiral map of the quantitative examples as in §11.2(3).
- **Five Parts** (D2); **per-Part primers plus a reference appendix** (D3); **SEU split** between Part I (baseline) and Part V (omitted factor, humility buffer) (D4); **two-axes matrix and four sources as the synthesis of Part III** (D5); **running examples reused deliberately**, tracked in a running-example register (D6).

### 13.2 Leitmotiv & Stance (L1, L2; D12, D13)
- **Primary reader:** a technically literate professional (engineer, analyst, ML practitioner) who once learned probability but never used it as an instrument of reasoning. Other profiles are served through reading paths.
- **Practical orientation first.** The goal is the *proper approach to acting on the world*: through a picture, and through the method of building that picture. Formality is a means (rigour, method, logical consistency, no leaks in the argument), not an end.
- **Working stance:** a best working assumption, held in the Bayesian sense (subjective, expected, *faute de mieux*), with its tensions and risks identified. Exposing unavoidable tensions is itself an objective.
- **Self-consistency:** the monograph applies its own principles to itself. It is explicit and self-critical about the robustness of its own scaffold.
- **Formal depth: mixed.**
  - Assumptions are displayed where they are made.
  - Real models with stated assumptions where they carry the argument (core of Part II: a probabilistic model of blind spots and escape; the decision model with an unrepresented variable).
  - Formal sketches elsewhere.
  - The practical substrate carries the message where it does so better than formalism.

### 13.3 Status of Claims & Propositions (L3; D8, D10)
- Every Proposition and major claim states its **epistemic status**: definition; result under stated assumptions; working hypothesis; or claim backed by empirical evidence. Working hypotheses are acknowledged as such, distinct from better-supported claims.
- Where possible, a **self-critical note on robustness** accompanies the scaffold (what would weaken it, where it is thin).
- The author reviews, reformulates or rejects each Proposition before drafting (D8).
- **Numbering:** Propositions are numbered in order of appearance in the monograph (no link to earlier numbering); naming ("Proposition", "Principle", "Hypothesis") follows from each one's status.

### 13.4 Provenance & Disclosure (L4; D9)
- **Hard constraint (unchanged from §6.1):** no internal document is cited or mentioned.
- The monograph **acknowledges a hybrid human–AI development process**, neither understating the AI contribution nor dismissing human curation as a significant element of it. Indicative wording: *the framework was developed in dialogue with AI models; the author reviewed, revised and takes responsibility for every proposition.*
- The author's arXiv article is the one self-reference: a seal of curation, explicitly not an absolute one.
- The monograph claims no validation from its design process. It presents itself as a **working approach, not a formal prescription**: an argumentative line laid bare and structured, to be judged primarily on what it says, as in any peer-reviewed endeavour.

### 13.5 Pedagogical Blocks (L5; D14, D15)
Six signaled block types (French names, as they will appear in the text):

| Block | Role |
| :--- | :--- |
| **Boîte à outils** | Recalls a foundational tool assumed to be known (logic, probability, decision theory, contracts, reliability) for consistency, ease of reading, and to refocus the theoretical apparatus |
| **Noyau formel** | Definitions, derivations, stated assumptions |
| **Exemple quantitatif** | The three-form quantitative example (prose, figure, numbers), flagged as illustrative |
| **Étude de cas** | Documented empirical or legal case (dated where time-sensitive) |
| **Nuance et discussion ouverte** | Genuine tensions, objections, limits; refinements that are corrections go into the main prose instead |
| **Question à se poser** | Diagnostic question for the reader's own practice |

Per-Part primers are sections, not blocks; *Boîte à outils* is for shorter recalls elsewhere in the text.

### 13.6 Language & Multi-Session Production Model (L6; D25)
- **The monograph is written directly in French.** It is not a translation: ideas are rephrased in clear, idiomatic French, and terminology is (re)introduced as in any academic monograph.
- **Production model:** Parts and chapters will be built in separate sessions, possibly with different LLM models, with iteration and cross-reads. Each builder must work from a clean, locked argumentative structure.
- **Required shared artefacts (to produce once the specs are locked):**
  1. **Content spec** (in English, for precision, brevity and continuity with the source material). A minimal per-Part and per-chapter spec giving:
     - the chapter's purpose and its place in the whole;
     - prerequisites ("keys in") and what it establishes ("keys out");
     - Propositions introduced, with status;
     - running examples and their state at that point;
     - quantitative examples with canonical parameters;
     - backward and forward links;
     - intended Key Takeaways.
  2. **Terminology & notation register**: bilingual EN → FR. Each concept gets a fixed French term, a definition, and its first-introduction point. The Glossary is generated from it.
  3. **French style guide**: register, sentence style (no calques of English syntax), typography (non-breaking spaces, « » quotation marks, decimal comma), block usage.
  4. **Canonical parameter sets** for the quantitative examples (D18), shared by all builders so text, figures and tables agree.
  5. **Single shared bibliography**, populated only with verified references (D11).

### 13.7 Still Open
- **D21 / D22 Output format and figure toolchain:** under discussion (author leans LaTeX for the final product, with a more textual first pass for iteration and sharing).
- D11 (timing of the citation pass), D16 (register of remedies), D17 (dated evidence), D19–D20 (figure types, companion labs), D23–D24 (citation style, length), D27 (exercises): to be settled while outlining or drafting.

---

## 14. Archive: Author Prompt — Update 4

> On L1, I agree on the technically literate professionnal. I'd add that my objective is to produce something that is practically oriented first (in the sense of "having the proper approach, whatever that might mean, to act on the world"), with enough formality to be logically consistant and sound, and avoid leaks (even if identifying /exposing inavoidable tensions is in itself one objective) in argumentative structure. So, the formal is in fine, a means (rigour, method) to an end (act on the world). The monograph should follow that leitmotive, while being consistant, and explicit and self-critical on the principle it preaches. So naturally, on L2, that means mixed, with assumption displayed where they are, and practical substrate where they carry the message. On the practical vision again, a best working assumption, with identified tensions and risks, is in the Bayesian sense, the proper way ("subjective expected", "faute de mieux"). On L3, yes, state, or rather display self-critical view on the robustness of our own scaffold when it is possible to do so, and honest to acknowledge a working hypothesis from a claim backed by more evidence. On numbering, I have no rigid rule to convey right now, whatever works best. On L4, I agree with your formulation, neither understating nor dismissing than human curation is a significant element of an hybrid process. The building of the monograph is clearly in itself a building process, as I do not expect it to have somehow the value of a "validation", it is also in itself an argumentative line laid bare and structured, as a "working approch (not a formal prescription)" to, in fine "help acting on the world, though a picture, and the method of elaborating said picture". No internal document cited is a hard constraint thought. I want the monography to be self consistent, even I the reference to the arXiv article, is somewhat a "seal" (albeit a non absolute one) on curation, in the hybrid process (acknowledged in the monograph). I'd say, in a empirical stance, the content of the end product (monograph) should also and maybe primilarily be judged by what it says, not by any higher authority in the design process it claims to have, in fact as in any peer reviewed scientific endeavour. On L5, ok on the block types you identified, maybe I'd add a distinctive one for "primers" or "tools" or "foundations" (that are supposed to be given, but recalled anyway for consistancy, ease of read, and also, refocus on the whole theoretical apparatus), whatever you feel best to call it. On L6 I'd push back, it'd be best to write it in French directly, so that has to be acknowledge by the specs, and the design process. Once the specs are "crystalized" or "locked-in" enough, it is my intention to have different session build the different parts / chapters, possibly with different LLM models, possibly with iteration and cross-reads on production. And I want them to work from a clean argumentative structure. So once the argumentative line is locked-in in the specs, a minimal "content-spec" should be produced, so that a builder of one part, has to have enough vision of how it's focus part clicks inside the whole monograph. This content spec can be in English for precision / breivity and continuity with the source material, but the monograph derived from it in different session has to rephrase the underlying ideas in clear idiomatic french, without ambiguity in terminology (which has to be reintroduced, as in any academic monograph). For the format, last decision to be made, maybe let us talk about it in what follows so that I can see alternatives : I'd lean latex, but for iteration and sharing, maybe a more textual first pass (in markdown) would be more comfortable.

---

## 15. Format Decision & Companion Documents (Update 5)

- **D21 locked: Option 3.** Structured pandoc Markdown is the single source, rendered to PDF through a project LaTeX template (LuaLaTeX, babel-french) and to HTML/DOCX for sharing. There is no later conversion pass. Quarto remains a possible mechanical migration path (same syntax family).
- **D22 locked:** figures and number tables are generated by Python/matplotlib scripts from shared canonical parameters.
- **Companion documents:**
  - `authoring_conventions.md`: toolchain, file layout, chapter structure, the six blocks and statement syntax (with mandatory `statut`), labels and cross-references, figures and tables, the four-step quantitative example, French language, terminology and typography rules, provenance rules, builder permissions, cross-read checklist.
  - `course_outline.md`: Option D outline (19 chapters + preface + conclusion + appendices A–D), statements renumbered P1–P5 in order of appearance with proposed statuses, per-chapter purpose, sections, threads, keys in/out and notable blocks, spiral map of the quantitative examples, running-example register, reading paths, coverage check of all 50 threads, and points for author review.
- **Next step:** author review of the outline (`course_outline.md` §7); then, on the author's go, the content spec.

---

## 16. Archive: Author Prompts — Update 5

> For the format, last decision to be made, maybe let us talk about it in what follows so that I can see alternatives : I'd lean latex, but for iteration and sharing, maybe a more textual first pass (in markdown) would be more comfortable.

> ok for option 3. Go for the authoring convention note and the chapter outline. I'll give you the go for the final content spec

---

## 17. Content Spec & Builder Entry Point (Update 6)

- **Content spec written** in `content_spec/` (English; the monograph is written in French):
  - `00_global.md`:
    - the argument line S1–S16, with the chapter that carries each step;
    - the stance;
    - the five statements P1–P5 (canonical wording, status, justification, robustness note);
    - formal models M1 (blind spots and escape), M2 (deciding with an unrepresented variable), M3 (the frame as common cause);
    - the terminology register EN → FR;
    - notation;
    - canonical parameters with computed values (checked against the interactive labs);
    - the references register (all "to verify" except the arXiv article);
    - global pitfalls.
  - `part0_front.md`, `part1.md` … `part5.md`, `part9_back.md`: per-chapter specs giving argument step, keys in and out, source threads, sections, blocks, figures, intended Key Takeaways, and indicative length.
  - `source_threads_en.md`: the full English text of all 50 map threads, extracted mechanically, as raw material. It carries a header warning that it is never cited or mentioned, and that `CR`/`RV` material enters only as nuance.
- **Builder entry point:** `BUILDER_START_HERE.md` gives:
  - the reading order and precedence of documents;
  - ten hard rules;
  - deliverables for builders (chapter plus `NOTES_NN.md` template) and cross-readers (`RELECTURE_NN.md`);
  - a project-state table;
  - a copy-paste session prompt.
- **Pending before chapter builds (maintainer):**
  1. `monographie/` tree, LaTeX template, Lua filter, Makefile;
  2. `commun/registre_termes.md` from `00_global.md` §5;
  3. `commun/parametres.py` and figure/table scripts from `00_global.md` §7;
  4. citation-verification pass populating `commun/biblio.bib` (D11);
  5. author review of statement statuses (D8) and of the register of remedies (D16).

---

## 18. Archive: Author Prompt — Update 6

> ok. Go for the content spec. When you are done our while you do it. Can you produce a simpler entry point, jump starter md, so that I can point any builder session to it (possibly with references to the authoring spec, the outline and/or the content spec)

---

## 19. Build Infrastructure (Update 7)

- `monographie/` built and tested (see `monographie/README.md`):
  - folder tree; `livre.yaml` (chapter order);
  - chapter stubs with fixed titles, labels and structural classes; Part pages; appendix stubs; placeholders for shared files;
  - **template:** pandoc's default LaTeX template plus `gabarit/preambule.tex` (scrbook, TeX Gyre Pagella, six coloured block boxes, Proposition/Définition environments with a status line, draft markers), plus `gabarit/{commun,pdf,html,docx}.yaml`;
  - **filter:** `filtres/monographie.lua` (blocks, statements with mandatory statut, cross-references `@id` / `[-@id]` with identical numbering in PDF and HTML, labelled equations, generated-table includes, missing-figure placeholders, `A-VERIFIER` markers, French spacing, book structure, non-floating figures and tables inside blocks);
  - **build script:** `Makefile` (pdf, html, docx, single-chapter preview, figures, verifier, self-test);
  - **checker:** `outils/verifier.py`.
- **Tests:**
  - `make essai` exercises every convention and catches the planted faults (undefined reference, missing figure, wrong number in a quantitative example);
  - the stubbed book builds in PDF, HTML and DOCX;
  - `make verifier` reports 0 errors and 25 stubs.
- **Small design choices made during the build:**
  - reference words are generated by the filter rather than cleveref, so PDF and HTML wording is identical;
  - chapter 0 numbering is forced so figures read "0.1" in both outputs;
  - "Points clés" sections are unnumbered and kept out of the tables of contents;
  - the HTML edition uses the `.svg` twin of each `.pdf` figure.
- **The book subtitle in `livre.yaml` is a placeholder** proposed during the build: « Cadre, contrôles et décision, de l'informatique classique à l'IA ».

---

## 20. Archive: Author Prompt — Update 7

> build the folder structure, latex template, filter and build script

---

## 21. Quantitative Examples Built (Update 8)

- **`commun/parametres.py`:** models M1 and M2 and the canonical parameter sets of every quantitative example. Its self-check reproduces the 49 canonical values of `content_spec/00_global.md` §7.
- **`scripts/`:** `_style.py` plus five scripts producing 8 figures (PDF + SVG) and 12 tables:
  - figures for ch. 3, 4, 8, 9, 12, 14, 16 and 17;
  - additional tables for the plain-arithmetic examples of ch. 9 (screening, disagreements, error × escape teaser).
- **Figure design** (following the dataviz method):
  - book font;
  - three-colour palette validated for colour-vision deficiency (all-pairs);
  - colour never the only cue;
  - two panels instead of dual axes;
  - emphasis rather than many colours;
  - every figure paired with a number table.
- **Tables** were redesigned during testing: escape tables transposed (one column per scenario), the decision table split into inputs and outcomes, column widths sized to content. Every table was tested inside and outside blocks in a LaTeX build.
- **Build fixes made along the way:**
  - figure font embedding (type 3, since Pagella is CFF);
  - `tabularx` with proportional widths for tables inside blocks;
  - a verifier false positive on figure attributes.

---

## 22. Archive: Author Prompt — Update 8

> do the parametres.py and figure scripts next

---

## 23. Register and Bibliography Set Up (Update 9)

- **Register:** `monographie/commun/registre_termes.md` is the French terminology register (64 terms: French term, English equivalent, French definition, chapter of introduction, definition label) plus the notation table (15 symbols). `outils/glossaire.py` (`make glossaire`) generates appendices B (Glossary, alphabetical, with live chapter references) and C (Notation).
- **Bibliography:** a two-file workflow.
  - `biblio.bib` holds verified references (the author's arXiv article, arXiv:2605.23614).
  - `biblio_a_verifier.bib` holds about 60 candidate references entered from memory, each with an `averifier` field (never printed) stating the claim it should support and what to check.
  - Candidates are citable by key and render with an orange « ? ». `make verifier` lists them and reports unknown keys as errors.
  - Verification consists of checking an entry and moving it to `biblio.bib`; no chapter edit is needed.
- `BUILDER_START_HERE.md`, `authoring_conventions.md` (§9) and `content_spec/00_global.md` (§5, §8) updated accordingly.
- **Builder entry point brought up to date** before the first builder session:
  - the register is added to the reading order;
  - rule 3 describes the two-file citation workflow, including « do not stretch a candidate reference to another claim »;
  - rule 4 points to the French register;
  - the project-state table is current;
  - the outdated fallback instructions are replaced by what is already available (figures, tables, register, bibliography keys).
- **Smaller additions in the same step:**
  - the notation-table column is widened;
  - apostrophes in the register are typographic;
  - the self-test now also exercises a verified citation, a candidate citation and an unknown key (all three behave as intended).

---

## 24. Archive: Author Prompts — Update 9

> do the terminology register and the bibliography set up, to be populated later (or you can plug in a few references, to be double checked later)

> when you are done, check that @BUILDER_START_HERE.md is up to date and then I'll launch a builder session

---

## 25. Current State and Next Steps

**Ready:**
- specs and decision log (this file);
- `authoring_conventions.md`, `course_outline.md`, `content_spec/` and `BUILDER_START_HERE.md`;
- `monographie/`:
  - template, filter, Makefile, verifier, self-test;
  - chapter stubs;
  - 8 figures and 12 tables with self-checked numbers;
  - terminology register with generated Glossary and Notation appendices;
  - bibliography: one verified reference and 60 candidates.
- **Last verified:** the self-test, the whole book in PDF, HTML and DOCX, and `make verifier` (0 errors) all pass.

**Next step:** first builder session, Part 0 (preface and chapter 0), using the example prompt in `BUILDER_START_HERE.md` §6. It is to be followed by a cross-read session (§4 of the same file).

**Open, none blocking the first builder:**
- D8, the author's review of the P1–P5 statuses;
- D11, the citation-verification pass (move entries from `biblio_a_verifier.bib` to `biblio.bib`);
- D16, the register of remedies (before Part V);
- Part-page introductions (`monographie/parties/`);
- the book subtitle (placeholder in `livre.yaml`);
- D20, D23, D24, D27.

