# Start Here — Builder Sessions

You are joining the build of a **French-language academic monograph** whose working title is *Agir d'après une représentation du monde*.
- **Subject:** how we act on the world through a finite picture of it, what can tell us in time that we are wrong, and what classical computing, machine learning and automation change about that.
- **Organization:** chapters are written by separate sessions, possibly by different models, and then cross-read. Your job is one well-defined piece that fits a locked structure.

---

## 1. What to Read, in This Order

| # | File | Why | Read |
| :-- | :-- | :-- | :-- |
| 1 | `BUILDER_START_HERE.md` (this file) | orientation and hard rules | all |
| 2 | `authoring_conventions.md` | **how** to write: syntax, blocks, labels, figures, French rules, provenance, what you may touch | all |
| 3 | `content_spec/00_global.md` | **what** the book says: argument line, the five statements, formal models, canonical numbers and generated artefacts, references, pitfalls | all |
| 3b | `monographie/commun/registre_termes.md` | the **French terminology and notation register**: one fixed term per concept, its definition, and the chapter that introduces it (source of truth; it supersedes the English table of `00_global.md` §5) | all |
| 4 | `content_spec/partN.md` | the detailed spec of your chapter(s) | your Part, plus the neighbouring chapters' "Keys out". **Chapter 0 and preface builders:** skim every Part file, since chapter 0 previews the whole book |
| 5 | `course_outline.md` | the whole map: overview (§0), quantitative-example spiral (§3), running examples (§4), reading paths (§5) | §0 and §3–§5 |
| 6 | `content_spec/source_threads_en.md` | raw English material, keyed by the thread ids listed in your chapter spec | only your threads |
| 7 | `source/frame_problem_article_WF.tex` | the author's arXiv article, the one citable self-reference | the sections your spec names |

Part files:
- `part0_front.md`: preface, ch. 0;
- `part1.md`: ch. 1–4;
- `part2.md`: ch. 5–9;
- `part3.md`: ch. 10–13;
- `part4.md`: ch. 14–16;
- `part5.md`: ch. 17–18;
- `part9_back.md`: conclusion and appendices.

The background design decisions are in `course_specs_draft.md` (§13 is the locked summary). You do not need it to build a chapter.

**Precedence when documents disagree:**
1. authoring conventions;
2. content spec;
3. outline;
4. source threads.

Report any conflict in your notes file.

---

## 2. Hard Rules (non-negotiable)

1. **Write in idiomatic French.** Rephrase the ideas; never translate the English sentences of the specs or sources. No English syntax calques.
2. **Never mention internal material:** maps, drafts, versions, reviews, source tags (TK, WG, FD, CR, RV), thread ids, "amendments". The only self-reference is the author's arXiv article.
3. **Cite by key, from the two bibliography files; never invent a reference.** Attach a citation to every empirical figure.
   - `monographie/commun/biblio.bib` holds **verified** references. Among them is the author's arXiv article: `[@fauriat2026frame]` (arXiv:2605.23614).
   - `monographie/commun/biblio_a_verifier.bib` holds about **60 candidate** references, not yet checked (e.g. `[@mco1999]`, `[@mata2023]`, `[@becker2025]`, `[@kalai2024]`). Cite them by key: they render with an orange « ? », and `make verifier` lists them. Each entry's `averifier` field says which claim it is meant to support; do not stretch it to another claim.
   - A reference in neither file: write `[@A-VERIFIER: description]` and propose the entry in your notes.
   - Never edit the bibliography files.
4. **Use the registered French terms** (`monographie/commun/registre_termes.md`).
   - Set a term in bold and define it **only in the chapter listed in the register's « Introduit » column**. Elsewhere, use it plainly, and refer back to that chapter if useful. The register's definitions are the reference wording, but phrase the in-text definition naturally.
   - The Glossary and Notation appendices are generated from the register: never write them by hand.
   - Use no synonyms for a term's technical sense.
   - If you need a new term, propose it in your notes; do not invent it.
5. **Every `.proposition` carries its `statut`** exactly as fixed in `00_global.md` §3. Never upgrade a working hypothesis into a result.
6. **Never type a number by hand in an `.exemple-quantitatif` block.** Its numbers come from the generated tables (`monographie/tableaux/`), copied with their displayed precision. Plain-arithmetic examples in running prose (e.g. the 1 % × 90 % teaser) must use exactly the values of `00_global.md` §7.
7. **Respect the dependency order.** Do not use a concept before the chapter that introduces it. Announce forward only where your spec lists a forward link.
   - **Exception: chapter 0** previews every concept informally, by design, with no formal definitions and no bold terms. Its spec governs.
   - **Refer to chapters and sections by label, never by typed number:** « le chapitre [-@sec:ch05] » or « le @sec:ch05 ». Numbers are generated, so renumbering stays safe. This matters for chapter 0's reading paths.
8. **Touch only your chapter file(s) and your notes file.** Shared files, labels fixed by the spec, and generated figures and tables are off limits.
9. **The main-text rule:** a reader who skips the optional blocks must still follow the argument.
10. **End every chapter with `## Points clés`.**

---

## 3. What a Builder Session Delivers

Paths below are relative to `monographie/`.

1. **`chapitres/NN-slug.md`:** the chapter (the preface is `chapitres/00-avant-propos.md`, chapter 0 is `chapitres/00-cartographier.md`), following `authoring_conventions.md` §3–§8 and the chapter spec (sections, blocks, keys out, intended *Points clés*).
2. **`notes/NOTES_NN.md`** (preface and chapter 0 share `NOTES_00.md`), using this template:

```markdown
# Notes — Chapitre NN

## Références à ajouter ou à vérifier
- [@A-VERIFIER: …] ou clé candidate — affirmation concernée, section — entrée BibTeX proposée si la référence manque

## Termes proposés (absents du registre)
- terme FR — concept EN — définition — justification

## Paramètres / figures demandés
- id d'exemple — scénario — figure souhaitée

## Écarts par rapport à la spec
- ce qui a été changé et pourquoi

## Incohérences repérées ailleurs
- fichier — problème
```

---

## 4. What a Cross-Read Session Delivers

Use the checklist in `authoring_conventions.md` §11. Deliver `notes/RELECTURE_NN.md` with findings ranked by severity:
1. argument leaks and dependency violations;
2. provenance leaks;
3. status errors;
4. terminology drift;
5. French quality;
6. typography.

Quote the passage concerned in each finding. Do not rewrite the chapter unless asked.

---

## 5. Project State (update as artefacts are created)

| Artefact | Status |
| :-- | :-- |
| Specs (`course_specs_draft.md`), conventions, outline, content spec | ✔ written |
| `monographie/` tree, LaTeX template, Lua filter, Makefile, verifier, chapter stubs | ✔ built and tested (`make essai`; whole book builds in PDF, HTML and DOCX). See `monographie/README.md` |
| `commun/registre_termes.md`, generated Glossary and Notation appendices | ✔ 64 terms, 15 symbols (`make glossaire`, maintainer) |
| `commun/parametres.py`, figure scripts, generated figures and tables | ✔ built (`make figures`; values self-checked against `00_global.md` §7). Which file goes with which example: `00_global.md` §7, "Generated artefacts" |
| Bibliography | `biblio.bib` (verified): the author's arXiv article only. `biblio_a_verifier.bib`: about 60 candidates, citable by key, marked « ? » until the verification pass moves them to `biblio.bib` |
| Part-page introductions (`parties/`) | ✘ placeholders (maintainer) |

**Already available to builders:**
- the generated figures and tables for every quantitative example (mapping in `00_global.md` §7, "Generated artefacts");
- the register;
- the bibliography keys.

A figure or table you need that does not exist yet: reference it by its planned path (`figures/chNN-slug.pdf`, `tableaux/chNN-slug.md`). It renders as a placeholder; request it in your notes.

**Workflow for a builder:**
1. Write in `monographie/chapitres/NN-slug.md`, keeping the stub's heading line unchanged.
2. From `monographie/`, run `make chapitre CH=NN` to preview (`CH` is a file-name prefix: `CH=00-a` for the preface, `CH=00-c` for chapter 0). Add `ECRAN=1` for a screen layout with centred pages (`ch-NN-ecran.pdf`).
3. Run `make verifier` and fix every error in your chapter.

---

## 6. Prompt Template to Start a Session

Copy, fill in the brackets, and paste into a new session:

> You are a builder for a French-language academic monograph. Your working directory is `[path to project]`.
> Read `BUILDER_START_HERE.md` and follow its reading order (§1) and hard rules (§2).
> Your task: **[write | revise | cross-read] chapter [NN] — « [titre] »**, specified in `content_spec/[partN].md`.
> [Optional: specific instructions, e.g. "focus on section 3", "first draft only, no polishing".]
> Deliver the files listed in §3 (or §4 for a cross-read). When done, summarize in a few lines:
> - what you wrote;
> - which spec points you could not satisfy;
> - which references remain to verify.

**Example (first batch, Part 0):**

> You are a builder for a French-language academic monograph. Your working directory is `/home/ai-user/Documents/Sandbox/review_epist_ag`.
> Read `BUILDER_START_HERE.md` and follow its reading order (§1) and hard rules (§2).
> Your task: **write the preface (« Avant-propos ») and chapter 0 (« Cartographier le terrain »)**, specified in `content_spec/part0_front.md`.
> This is a first draft that will be cross-read and iterated. Favour a complete, coherent argument over polish, and flag every doubt in `notes/NOTES_00.md`.
> Preview with `make chapitre CH=00-a` and `make chapitre CH=00-c`, then run `make verifier` from `monographie/`.
> Deliver the files listed in §3. When done, summarize in a few lines:
> - what you wrote;
> - which spec points you could not satisfy;
> - which references remain to verify.
