# Authoring Conventions — Monograph Build

**Status:** v0.1 (to be frozen before the first chapter is drafted)
**Applies to:** every session (human or model) that writes, revises or cross-reads a chapter.
**Companion documents:** `course_specs_draft.md` (decisions, §13), `course_outline.md` (chapter outline), content spec (to come).

---

## 1. Toolchain (Option 3: structured Markdown → pandoc → LaTeX/PDF, HTML)

- **Source:** pandoc Markdown, one file per chapter. This is the single source of truth: there is no later conversion pass.
- **PDF:** pandoc → LaTeX (LuaLaTeX, babel-french, csquotes, amsthm/thmtools, booktabs, siunitx) through a project template, built with `latexmk`.
- **HTML / DOCX:** generated from the same sources for sharing and commenting.
- **Citations:** pandoc's built-in `--citeproc` with a shared `biblio.bib` and a CSL style (style to be chosen, D23).
- **Cross-references, blocks and Propositions:** handled by the project's Lua filter `filtres/monographie.lua` (pandoc-crossref is not used).
- **Build:** `make` from `monographie/` (see `monographie/README.md`); `make verifier` for static checks.
- **Figures and number tables:** produced by Python scripts (matplotlib) reading `commun/parametres.py`; never drawn or typed by hand.
- **Owned by the maintainer only:** template, filters, Makefile, shared files. Builders write chapters only (§9).

## 2. File Layout

```
monographie/                    # see monographie/README.md for commands
├── livre.yaml                  # chapter order + title metadata (pandoc defaults file)
├── chapitres/                  # one file per chapter: NN-slug.md (stubs exist with fixed title and label)
│   ├── 00-avant-propos.md
│   ├── 00-cartographier.md     # Chapter 0
│   ├── 01-outils-logique-probabilite.md … 18-remede-trois-niveaux.md
│   └── 99-conclusion.md
├── parties/partie-N.md         # Part pages: title + short introduction
├── annexes/                    # A-outils.md, B-glossaire.md (generated), C-notation.md, D-parametres.md, Z-bibliographie.md
├── commun/
│   ├── registre_termes.md      # terminology & notation register (EN → FR), source of the Glossary
│   ├── biblio.bib              # verified references only
│   ├── parametres.py           # canonical parameter sets of the quantitative examples
│   └── exemples_courants.md    # running-example register (where each example appears, what it establishes)
├── scripts/                    # one script per quantitative example: fig_<id>.py
├── figures/                    # generated: .pdf (print) + .svg twin (HTML) — never edited by hand
├── tableaux/                   # generated Markdown number tables — never edited by hand
├── notes/                      # NOTES_NN.md (builders), RELECTURE_NN.md (cross-reads)
├── gabarit/                    # commun.yaml, pdf.yaml, html.yaml, docx.yaml, preambule.tex, livre.css
├── filtres/monographie.lua     # blocks, statements, references, equations, includes, French spacing
├── outils/verifier.py          # static checks (make verifier)
├── tests/                      # toolchain self-test (make essai)
└── Makefile
```

**Preview while writing:** `make chapitre CH=NN` (PDF and HTML in `build/apercu/`), then `make verifier`.

## 3. Structure of a Chapter File

```markdown
# Titre du chapitre {#sec:ch05}

Chapeau : 3 à 5 lignes situant le chapitre (d'où l'on vient, ce que l'on va établir).

## Première section {#sec:ch05-incertitudes}
…

## Points clés {.points-cles}

- 4 à 7 points, chacun une phrase complète.
```

- One `#` heading per file (the chapter). Sections `##`, subsections `###`; no deeper level.
- **Keep the chapter heading line exactly as in the stub** (title, label and classes). Classes such as `.corps`, `.unnumbered`, `.annexes` drive the book structure.
- Every heading carries an explicit label (§5).
- Every chapter ends with **Points clés** (Key Takeaways). The filter makes that section unnumbered and keeps it out of the tables of contents.
- Part pages (title and a short introduction) live in `parties/partie-N.md` and are written by the maintainer.

## 4. Blocks (fenced divs)

Six signaled block types (spec §13.5). Syntax: a fenced div with a class and an optional title.

```markdown
::: {.formel titre="Décomposition de la variance"}
…
:::
```

| Class | Rendered title | Use |
| :--- | :--- | :--- |
| `.outils` | Boîte à outils | short recall of a foundational tool (logic, probability, decision, contracts, reliability) |
| `.formel` | Noyau formel | definitions, derivations, explicit assumptions |
| `.exemple-quantitatif` | Exemple quantitatif | three-form quantitative example (§7), flagged illustrative |
| `.cas` | Étude de cas | documented empirical or legal case; add `date="AAAA"` if time-sensitive |
| `.nuance` | Nuance et discussion ouverte | genuine tension, objection, limit (corrections go in the main text) |
| `.question` | Question à se poser | diagnostic question for the reader's practice |

**Statements** (numbered, cross-referenceable, rendered as theorem-style environments):

```markdown
::: {.proposition #prop:desaccord titre="L'incertitude n'est qu'un désaccord mesuré" statut="résultat sous hypothèses"}
Énoncé.
:::

::: {.definition #def:comparateur titre="Comparateur"}
…
:::
```

- `statut` is mandatory on every `.proposition`. Allowed values: `définition`, `résultat sous hypothèses`, `hypothèse de travail`, `constat empirique`.
- The statement is followed in the main text by its justification. Where possible, it is also followed by a `.nuance` block on its robustness (spec §13.3).
- Propositions are numbered automatically, in order of appearance. Never type a number.

Main-text rule: a reader who skips every block except `.exemple-quantitatif` and `.cas` must still follow the argument. Blocks deepen; they never carry a step the argument needs.

## 5. Labels and Cross-References

| Object | Label pattern | Example | Reference in text |
| :--- | :--- | :--- | :--- |
| Chapter | `sec:chNN` | `sec:ch09` | `@sec:ch09` → « chapitre 9 » |
| Section | `sec:chNN-slug` | `sec:ch09-ppv` | `@sec:ch09-ppv` |
| Proposition | `prop:slug` | `prop:cause-commune` | `@prop:cause-commune` |
| Definition | `def:slug` | `def:comparateur` | `@def:comparateur` |
| Equation | `eq:chNN-slug` | `eq:ch04-seuil` | `@eq:ch04-seuil` |
| Figure | `fig:chNN-slug` | `fig:ch09-echappement` | `@fig:ch09-echappement` |
| Table | `tbl:chNN-slug` | `tbl:ch08-comparateurs` | `@tbl:ch08-comparateurs` |

- **Two reference forms:**
  - `@id` gives the word and the number, as a link: « figure 9.1 », « proposition 3 », « équation (4.1) ». Write « la @prop:desaccord ».
  - `[-@id]` gives the number only. Use it to start a sentence or to build your own phrase: « Figure [-@fig:ch09-echappement] », « l'annexe [-@sec:annexe-d] ».
  - Several references: `@fig:a et @fig:b`.
- Slugs: lowercase ASCII, hyphens, no accents.
- Proposition and definition slugs are fixed in the content spec and **must not be renamed** (other chapters reference them).
- Forward references are allowed only where the outline lists them as forward links. A concept must never be *used* before its chapter introduces it; a forward reference may only *announce* it.
- Equations: `$$ … $$ {#eq:ch04-seuil}`. Inline math: `$…$`.

## 6. Figures and Number Tables

- Figures come only from `scripts/fig_<id>.py`, which writes a `.pdf` (print) and a `.svg` twin (used automatically in HTML). A figure not yet generated shows as a placeholder box; the build does not fail. Include figures with:
  `![Légende complète, compréhensible sans le texte.](figures/ch09-echappement.pdf){#fig:ch09-echappement width=90%}`
- Number tables come only from scripts, and are included with
  `::: {.inclure fichier="tableaux/ch09-echappement.md"}` `:::` (expanded by the filter).
- **Numbers quoted in prose must appear in the generated table of the same example.** The build checks this for every `.exemple-quantitatif` block.
- Canonical parameters live in `commun/parametres.py`. A builder who needs a new scenario proposes it in `notes/NOTES_NN.md`; the maintainer adds it.

## 7. Quantitative Examples (spec §6.2)

Each `.exemple-quantitatif` block follows the same four steps:

1. **Mise en place:** the scenario, the parameters and the assumptions, in prose.
2. **Figure:** the generated plot showing the regimes, thresholds or curves.
3. **Calcul:** the generated number table, plus at most a few worked lines of arithmetic.
4. **Lecture:** what the example shows, what it does not show, and which assumption it rests on.

It is labelled as illustrative: the numbers are chosen to expose a mechanism, not to estimate a real quantity.

## 8. Language, Terminology and Typography

**Language.** The monograph is written in French: idiomatic, not translated. The content spec is in English. Builders rephrase the ideas; they do not translate sentences.
- No English syntax calques. Avoid colon-chained aphorisms and nominal shorthand; prefer full sentences with French connectives.
- A technical English term is kept only when it is the usage in French practice (*token*, *fuzzing*, *bootstrap*). It is italicized and glossed at first use.

**Terminology.**
- Every technical term comes from `commun/registre_termes.md`, which fixes one French term per concept.
- At its first introduction (the chapter listed in the register), the term is set in **bold** and defined in the text.
- No synonyms for a registered term used in its technical sense (e.g. always *comparateur*, never *référence de contrôle*). Plain-language paraphrase is allowed when it is clearly not the term.
- A builder who needs a term not in the register proposes it in `notes/NOTES_NN.md`; they do not invent it in the chapter.

**Typography.** Write plain spaces; the filter and babel-french produce the correct spacing.
- « guillemets » with plain inner spaces; “ ” for quotes inside quotes;
- decimal comma in prose (`0,1 %`), and `{,}` in math (`$0{,}05$`);
- a space before `%`;
- `M. X`; `et al.` not italicized;
- dates as « 23 septembre 1999 ».

## 9. Provenance and Citation Rules (hard constraints)

- **Never mention** prior drafts, maps, internal documents, their codes (TK, WG, FD, CR, RV), versions or review history.
- **Cite by key only.** References come from two files:
  - `commun/biblio.bib`: verified references (published literature, documented cases, the author's arXiv article);
  - `commun/biblio_a_verifier.bib`: candidate references, citable by key but rendered with an orange « ? » and listed by `make verifier`. Verification moves an entry to `biblio.bib` with no change to the chapters.
- A reference in neither file is written as `[@A-VERIFIER: description]`, and the entry is proposed in the notes.
- An unknown key is a verifier error.
- At release, no `A-VERIFIER` marker and no citation of a candidate may remain.
- Every empirical figure (percentages, amounts, dates) is attached to a citation.
- Dated AI evidence goes in a `.cas` block with `date="…"`. The argument must never depend on a particular model or tool generation.

## 10. What Builders May and May Not Touch

| May | May not |
| :--- | :--- |
| Write and revise their chapter file(s) | Edit shared files (`commun/`, `filtres/`, `gabarit/`, `livre.yaml`, Makefile) |
| Write `notes/NOTES_NN.md` (questions, proposed terms, parameters, references, inconsistencies spotted elsewhere) | Rename labels defined in the content spec |
| Propose figure scripts in their notes | Edit generated `figures/` or `tableaux/` |
| | Introduce a concept that another chapter introduces (reference it instead) |

## 11. Cross-Read Checklist (for reviewing sessions)

1. Keys: is every concept used in the chapter introduced here or earlier (per the content spec)?
2. Terminology: registered terms only, bold at first introduction, no drift?
3. Statements: does every `.proposition` have a `statut`, a justification and, where possible, a robustness `.nuance`?
4. Quantitative examples: four steps; prose numbers match the generated table?
5. Provenance: no internal-document leakage; every empirical figure cited; no `A-VERIFIER` left without a note?
6. French: idiomatic, no calques, typography per §8?
7. Main-text rule: does the argument survive skipping the optional blocks?
8. Points clés present, and consistent with the chapter's "keys out" in the content spec?
