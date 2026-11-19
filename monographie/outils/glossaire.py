#!/usr/bin/env python3
"""glossaire.py — generate annexes/B-glossaire.md and annexes/C-notation.md from commun/registre_termes.md.

Run from monographie/: make glossaire. The appendices are generated: never edit them by hand.
Each entry points to the chapter where the term is introduced (cross-reference [-@sec:chNN]).
"""
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRE = ROOT / 'commun' / 'registre_termes.md'
AVERT = '<!-- Fichier généré par outils/glossaire.py à partir de commun/registre_termes.md : ne pas modifier à la main. -->'


def tables(text):
    """Return {section title: [row cells]} for every pipe table under a '## ' heading."""
    out, section = {}, None
    for line in text.splitlines():
        if line.startswith('## '):
            section = line[3:].strip()
            out[section] = []
        elif section and line.startswith('|') and not re.match(r'^\|\s*:?-', line):
            cells = [c.strip().replace('\\|', '|') for c in re.split(r'(?<!\\)\|', line.strip())[1:-1]]
            out[section].append(cells)
    return {k: v[1:] for k, v in out.items() if v}  # drop header rows


def cle_tri(s):
    s = unicodedata.normalize('NFKD', s.lower())
    return ''.join(c for c in s if not unicodedata.combining(c))


def renvoi(label):
    return f'chapitre [-@{label}]' if label.startswith('sec:ch') else f'[-@{label}]'


def main():
    t = tables(REGISTRE.read_text(encoding='utf-8'))
    termes, notations = t.get('Termes', []), t.get('Notations', [])
    erreurs = [r for r in termes if len(r) != 5] + [r for r in notations if len(r) != 3]
    if erreurs:
        sys.exit(f'registre mal formé (nombre de colonnes) : {erreurs[:3]}')

    b = ['# Glossaire {#sec:annexe-b}', '', AVERT, '',
         'Termes définis dans l’ouvrage, avec leur équivalent anglais usuel et le chapitre où ils sont introduits.', '']
    for terme, anglais, definition, intro, _etiq in sorted(termes, key=lambda r: cle_tri(r[0])):
        b += [f'**{terme}** (angl. *{anglais}*)', f':   {definition} Voir le {renvoi(intro)}.', '']
    (ROOT / 'annexes' / 'B-glossaire.md').write_text('\n'.join(b), encoding='utf-8')

    c = ['# Notation {#sec:annexe-c}', '', AVERT, '',
         '| Symbole | Signification | Introduit |', '|:--------------------|:------------------------------------------------|:------------|']
    for sym, sens, intro in notations:
        c.append(f'| {sym.replace("|", chr(92) + "|")} | {sens} | {renvoi(intro)} |')
    c += ['', 'Table: Notations employées dans l’ouvrage. {#tbl:annexe-c-notation}', '']
    (ROOT / 'annexes' / 'C-notation.md').write_text('\n'.join(c), encoding='utf-8')
    print(f'glossaire : {len(termes)} termes ; notation : {len(notations)} symboles')


if __name__ == '__main__':
    main()
