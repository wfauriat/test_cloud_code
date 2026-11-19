# monographie/ — build of the monograph

Sources in structured pandoc Markdown → PDF (LuaLaTeX), HTML, DOCX. Conventions: `../authoring_conventions.md`. Builders start at `../BUILDER_START_HERE.md`.

## Commands (run from this folder)

| Command | Result |
| :-- | :-- |
| `make pdf` / `make html` / `make docx` / `make tout` | the whole book in `build/` |
| `make chapitre CH=05` | preview of one chapter in `build/apercu/` (references to other chapters show `??`); `CH` is a file-name prefix: `CH=00-a` preface, `CH=00-c` chapter 0 |
| `make figures` | runs every `scripts/fig_*.py`: writes `figures/*.pdf` + `.svg` and `tableaux/*.md` |
| `make verifier` | static checks: statuts, labels, internal-document leaks, `A-VERIFIER` markers, stubs, numbers in quantitative examples (exit code 1 on errors) |
| `make essai` | toolchain self-test on `tests/essai.md` (exercises every convention) |
| `make clean` | removes `build/` |
| `… ECRAN=1` | option for every PDF target (`pdf`, `tout`, `chapitre`, `essai`): on-screen layout, one-sided, with the text block centred on every page whatever its parity and no blank pages. Written next to the print version with an `-ecran` suffix (`build/livre-ecran.pdf`, `build/apercu/ch-05-ecran.pdf`) |

Requirements: pandoc ≥ 3.1, LuaLaTeX with KOMA-Script, tcolorbox, thmtools, babel-french and TeX Gyre fonts, latexmk, and Python with matplotlib (`PY=` overrides the interpreter; default `/opt/venvs/pyDS/bin/python` if present).

## Layout

```
livre.yaml              chapter order + title metadata (pandoc defaults file)
chapitres/NN-slug.md    one file per chapter (builders)
parties/partie-N.md     Part pages: title + short introduction (maintainer)
annexes/                appendices A–D + Z-bibliographie.md (maintainer)
commun/                 biblio.bib · registre_termes.md · parametres.py · exemples_courants.md (maintainer)
scripts/fig_<id>.py     one script per quantitative example (maintainer)
figures/ tableaux/      generated — never edited by hand
notes/                  NOTES_NN.md and RELECTURE_NN.md from sessions
gabarit/                commun.yaml · pdf.yaml · html.yaml · docx.yaml · preambule.tex · livre.css
filtres/monographie.lua blocks, statements, cross-references, equations, includes, French spacing, book structure
outils/verifier.py      static checks
tests/                  essai.md + fig_essai.py (self-test)
build/                  outputs
```

## How the pieces fit

- `make pdf` runs `pandoc -d gabarit/commun.yaml -d gabarit/pdf.yaml -d livre.yaml`. This uses pandoc's default LaTeX template, plus `gabarit/preambule.tex` (scrbook class, Pagella fonts, block boxes, statement environments, draft markers), then `latexmk -lualatex`.
- The Lua filter runs **before** citeproc. It turns `@sec:…`, `@prop:…`, `@fig:…`, `@tbl:…`, `@eq:…`, `@def:…` into numbered references, with the same numbers in PDF and HTML. It turns `[@A-VERIFIER: …]` into a visible marker.
- Inside blocks, figures and tables are made non-floating; this is a LaTeX constraint, and their numbering is unchanged.
- Chapter heading classes have structural meaning:
  - `.avant-propos` → front matter;
  - `.corps` → main matter, numbering starts at chapter 0;
  - `.partie` → Part page;
  - `.annexes` → appendices (A, B, …);
  - `.fin` → back matter;
  - `.unnumbered` → no number.
- Citations: `commun/biblio.bib`, pandoc's default style until D23 is decided (then set `csl:` in `gabarit/commun.yaml`).

## Still to do (maintainer)

1. Citation-verification pass: check each entry of `commun/biblio_a_verifier.bib` (fields and the claim in `averifier`), then move it to `commun/biblio.bib`.
2. Part-page introductions in `parties/`.

## Register and bibliography

- `commun/registre_termes.md` is the French terminology and notation register. `make glossaire` regenerates appendices B and C from it.
- `commun/biblio.bib` holds verified references; `commun/biblio_a_verifier.bib` holds candidates. Citations of candidates render with an orange « ? » and are listed by `make verifier`. Unknown keys are verifier errors.

## Quantitative examples

- `commun/parametres.py` holds every parameter and model. `python3 commun/parametres.py` checks the 49 canonical values of the content spec; every figure script runs this check first and stops on drift.
- `scripts/_style.py` provides the shared style:
  - book font (TeX Gyre Pagella);
  - three validated colours (blue, orange, aqua), never alone (line style, position or labels back them up);
  - French number formatting;
  - the table writer, whose column widths are sized to content.
- `scripts/fig_*.py` write `figures/chNN-*.pdf` + `.svg` and `tableaux/chNN-*.md`. The mapping to chapters is in `content_spec/00_global.md` §7, "Generated artefacts".
