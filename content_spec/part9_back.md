# Content Spec — Conclusion and Appendices

Read `00_global.md` first.

---

## Conclusion — La méthode appliquée à elle-même (file `99-conclusion.md`, ~8–12 pages)

**Argument step:** S16. **Keys in:** the whole book.

**Purpose:** apply the book's principles to the book, as promised in the preface. No new concepts.

**Sections:**
1. **The scaffold and its statuses.** A table of P1–P5 and the main claims (S1–S15), each with its status (definition, result under assumptions, working hypothesis, empirical finding) and its weakest point.
2. **Open tensions.** An inventory of the *Nuance* blocks that remain open:
   - the optimal reviewer distance (not derived);
   - the cost–independence tendency;
   - salience omission and P3a;
   - behavioural uptake vs Bayes;
   - the empirical sign of the rate–escape product;
   - the register of remedies.
3. **What would weaken the argument.** Observations that would count against it, for example:
   - checks that share a frame nevertheless catching frame errors routinely;
   - shared-model communities showing lower escape;
   - seeded-error measurements not supporting the claimed escape rates.
4. **The book's own comparators.**
   - Its provenance: a hybrid human–AI process, curated by the author, with one self-reference (the arXiv article).
   - Where its claims could fail differently: published literature, the reader's own field.
   - It asks to be judged on what it says.
5. **Closing.** The working stance: a best working assumption, held *faute de mieux*, with its risks named. Acting through a picture, and building pictures that can be told they are wrong in time.

**Points clés:** 4–5 bullets.

**Must not:** mention internal documents or design history beyond the preface's disclosure; claim the scaffold is validated.

---

## Appendices

| File | Content | Source |
| :-- | :-- | :-- |
| `A-outils.md`: Outils de référence | consolidated primers: logic, probability (axioms, conditioning, Bayes in odds form, log score), variance decomposition, base rates and PPV, series/parallel reliability, SEU and p∗, contracts and Hoare triples, signalling | condensed from the chapters' *Boîte à outils*; no new material |
| `B-glossaire.md`: Glossaire | generated from `commun/registre_termes.md` (French term, definition, chapter of introduction) | register |
| `C-notation.md`: Notation | `00_global.md` §6 | global spec |
| `D-parametres.md`: Paramètres des exemples quantitatifs | every canonical parameter set and the resulting tables | generated from `commun/parametres.py` |

Plus the bibliography (generated from `biblio.bib`) and an index (terms from the register and the main cases).
