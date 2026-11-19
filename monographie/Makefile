# Makefile — build of the monograph. Run from monographie/.
#   make pdf | html | docx | tout   whole book
#   make chapitre CH=05             one chapter (PDF + HTML preview, in build/apercu/);
#                                   CH is a file-name prefix: CH=00-a (preface), CH=00-c (chapter 0)
#   make figures                    run every scripts/fig_*.py (figures/ and tableaux/)
#   make verifier                   static checks (statuts, labels, leaks, A-VERIFIER, numbers)
#   make glossaire                  regenerate annexes B (glossary) and C (notation) from commun/registre_termes.md
#   make essai                      toolchain self-test on tests/essai.md
#   make clean
# Option, for every PDF target (pdf, tout, chapitre, essai):
#   ECRAN=1                         on-screen layout: one-sided, text block centred on every
#                                   page whatever its parity, no blank pages. Output gets an
#                                   "-ecran" suffix (build/livre-ecran.pdf, build/apercu/ch-05-ecran.pdf),
#                                   so the print version is kept alongside.
# Owned by the maintainer.

PANDOC  ?= pandoc
LATEXMK ?= latexmk
PY      ?= $(shell test -x /opt/venvs/pyDS/bin/python && echo /opt/venvs/pyDS/bin/python || echo python3)
BUILD   := build
COMMUN  := -d gabarit/commun.yaml
SOURCES := $(shell sed -n 's/^  - \(.*\.md\)$$/\1/p' livre.yaml)
DEPS    := $(SOURCES) livre.yaml gabarit/commun.yaml filtres/monographie.lua commun/biblio.bib commun/biblio_a_verifier.bib
LATEXMK_OPTS := -lualatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=$(BUILD)

# Print layout (default): twoside, as set in gabarit/pdf.yaml.
# ECRAN=1 appends "oneside" to the class options; KOMA reads them left to right, so it
# overrides "twoside" and typearea gives equal left and right margins.
ifeq ($(ECRAN),1)
  PDF_OPTS := -V classoption=oneside
  SUFFIXE  := -ecran
else
  PDF_OPTS :=
  SUFFIXE  :=
endif
PDF_LIVRE := $(BUILD)/livre$(SUFFIXE)

.PHONY: pdf html docx tout chapitre figures verifier glossaire essai clean

pdf: $(PDF_LIVRE).pdf
html: $(BUILD)/livre.html
docx: $(BUILD)/livre.docx
tout: pdf html docx

$(BUILD):
	mkdir -p $(BUILD) $(BUILD)/apercu

$(PDF_LIVRE).tex: $(DEPS) gabarit/pdf.yaml gabarit/preambule.tex | $(BUILD)
	$(PANDOC) $(COMMUN) -d gabarit/pdf.yaml $(PDF_OPTS) -d livre.yaml -o $@

$(PDF_LIVRE).pdf: $(PDF_LIVRE).tex
	$(LATEXMK) $(LATEXMK_OPTS) $<

$(BUILD)/livre.html: $(DEPS) gabarit/html.yaml gabarit/livre.css | $(BUILD)
	$(PANDOC) $(COMMUN) -d gabarit/html.yaml -d livre.yaml -o $@

$(BUILD)/livre.docx: $(DEPS) gabarit/docx.yaml | $(BUILD)
	$(PANDOC) $(COMMUN) -d gabarit/docx.yaml -d livre.yaml -o $@

# Single-chapter preview: references to other chapters show as ?? (expected).
chapitre: | $(BUILD)
	@test -n "$(CH)" || (echo "usage : make chapitre CH=05  (ou CH=00-a, CH=00-c)" && exit 2)
	@f=$$(ls chapitres/$(CH)*.md | head -1); test -n "$$f" || (echo "aucun chapitre $(CH)" && exit 2); \
	echo "aperçu de $$f"; mkdir -p $(BUILD)/apercu; \
	$(PANDOC) $(COMMUN) -d gabarit/html.yaml --metadata title="Aperçu — chapitre $(CH)" --metadata premier-chapitre=$(shell echo $(CH) | cut -c1-2) $$f -o $(BUILD)/apercu/ch-$(CH).html && \
	$(PANDOC) $(COMMUN) -d gabarit/pdf.yaml $(PDF_OPTS) --metadata title="Aperçu — chapitre $(CH)" --metadata premier-chapitre=$(shell echo $(CH) | cut -c1-2) $$f -o $(BUILD)/apercu/ch-$(CH)$(SUFFIXE).tex && \
	$(LATEXMK) -lualatex -interaction=nonstopmode -halt-on-error -outdir=$(BUILD)/apercu $(BUILD)/apercu/ch-$(CH)$(SUFFIXE).tex

figures:
	@for s in scripts/fig_*.py; do [ -e "$$s" ] || continue; echo "→ $$s"; $(PY) $$s || exit 1; done

verifier:
	@$(PY) outils/verifier.py

glossaire:
	@$(PY) outils/glossaire.py

essai: | $(BUILD)
	cd tests && $(PY) fig_essai.py
	$(PANDOC) $(COMMUN) -d gabarit/html.yaml tests/essai.md -o $(BUILD)/essai.html
	$(PANDOC) $(COMMUN) -d gabarit/pdf.yaml $(PDF_OPTS) tests/essai.md -o $(BUILD)/essai$(SUFFIXE).tex
	$(LATEXMK) $(LATEXMK_OPTS) $(BUILD)/essai$(SUFFIXE).tex
	@$(PY) outils/verifier.py tests/essai.md || true

clean:
	$(LATEXMK) -C -outdir=$(BUILD) 2>/dev/null || true
	rm -rf $(BUILD)
