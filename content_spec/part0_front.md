# Content Spec — Front Matter and Chapter 0

Read `00_global.md` first. Indicative lengths are guides, not quotas (D24 open).

---

## Avant-propos (file `00-avant-propos.md`, ~4–6 pages)

**Purpose:** tell the reader what the book is for, how it stands, how it was made, and how to read it.

**Must say:**
1. **Aim:** helping to act on the world through a picture, and through the method of building that picture. Practical first. Formality is a means (rigour, consistency), not an end.
2. **Stance:** a working approach, not a prescription. Claims are best working assumptions in the Bayesian sense (*faute de mieux*). Tensions are exposed on purpose. The book applies its principles to itself (statement statuses, a concluding self-examination).
3. **Who it is for:** technically literate professionals (engineers, analysts, ML practitioners, research managers) who once learned probability but have rarely used it as an instrument of reasoning. Other readers can use the reading paths (ch. 0).
4. **How it was made (disclosure, spec §13.4; cite the article as `[@fauriat2026frame]`):** the framework was developed in dialogue with AI models; the author reviewed, revised and takes responsibility for every proposition. Neither understate the AI contribution nor dismiss human curation. Cite the author's arXiv article as the one self-reference, and present it as a seal of curation that is not absolute. The book asks to be judged on what it says, as in any peer-reviewed endeavour; its design process confers no validation.
5. **How to read it:**
   - the legend of the six blocks;
   - the main-text rule: blocks deepen, never carry a step;
   - statement statuses;
   - quantitative examples are illustrative;
   - dated case studies;
   - reading paths are in ch. 0.

**Must not:** mention any internal document, map, version or review history; claim validation.

---

## Chapter 0 — Cartographier le terrain (file `00-cartographier.md`, ~15–20 pages)

**Argument step:** previews S1–S16 informally.

**Purpose:** chart the whole territory in plain language before walking it. Formal apparatus is pruned to two light displays at most.

**Keys in:** none.

**Keys out:** informal acquaintance with picture, frame, comparator, failing differently, blind spot, escape probability, specified vs learned component, one-shot decision, gate. *No formal definitions*; the defining chapters re-introduce every term in bold.

**Sections:**
1. **Three stories (opening puzzle).**
   - *Mars Climate Orbiter (1999):* a unit mismatch at an interface. The failure had an address: a file, a specification it violated.
   - *Mata v. Avianca (2023):* lawyers filed invented case law produced by a chatbot. It was fluent and wrong, and it broke no written contract, because there was none.
   - *METR (2025):* developers measured about 19 % slower with AI tools, while estimating afterwards that they had been about 20 % faster.

   Pose the question: what changed between the first story and the other two, and what can still tell us in time that we are wrong?
2. **We act on a picture.**
   - The sailor's 5 % is a judgment, not a property of the sea.
   - Boiling water: every rule hides conditions (one light display of the pattern `A ∩ (…) → B`, in words first).
   - Deciding once with high stakes: a go/no-go threshold idea, no formula needed, or one in words.
3. **Errors are caught only by something that can fail differently.**
   - Comparators, the five conditions in one paragraph.
   - Why a self-check is blind to what one's own frame omits.
   - Chains vs cross-checks, with one image (series vs parallel).
4. **Classical computing earned guarantees; learned models give them up.** Contracts written in advance versus rules fitted to examples. The address is gone; fluency is uniform.
5. **What automation does to checks.** It chains them (agents act), removes them (the lost friction, the lost hesitation) and correlates them (everyone consults the same model).
   - The teaser in plain arithmetic: 1 % error with 90 % escape lets 0.9 % through; 10 % error with 1 % escape lets 0.1 % through. The more accurate producer can be the riskier system.
6. **What we can still do.** Attitude, placement, organization; gates for one-shot acts; four questions for anyone handed a confident number.
7. **How this book is built.** The five Parts and why they come in this order: keys before locks. The statement statuses. The running examples (sailboat, boiling water, bracket, Orbiter) that will return.
8. **Reading paths.** The table from `course_outline.md` §5, with one sentence per profile. Remind readers that each chapter opens with its prerequisites. Write chapter numbers as label references (`[-@sec:ch05]`, labels `sec:ch00` … `sec:ch18`, `sec:conclusion`), never typed.

**Blocks:**
- *Étude de cas* (dated): METR, short.
- No *Noyau formel*.
- At most one *Question à se poser* at the end: "In your work, which number did you last act on, and what was its comparator?"

**Figures (suggested):**
- A one-page map of the five Parts and the argument steps.
- A series-vs-parallel pictogram.

**Points clés:** 5–6 bullets mirroring sections 2–6.

**Pitfalls:**
- Do not define terms formally here.
- Do not cite figures without references.
- Do not explain the AI cases in depth; that is Part III's job.
