#!/usr/bin/env python3
"""verifier.py — static checks on the monograph sources (run: make verifier).

Errors (exit code 1):
  - proposition without a valid statut
  - cross-reference to an undefined label; duplicate label
  - internal-document leakage (source tags, map ids, working-file names)
  - chapter file without exactly one level-1 heading, or without "Points clés"
Warnings:
  - [@A-VERIFIER: ...] markers still present (listed)
  - unwritten chapters (stubs)
  - numbers quoted in a quantitative example that do not appear in its included table(s)
  - the word "amendement" (allowed in French, but check it is not review vocabulary)

Usage: python3 outils/verifier.py [files...]   (default: input-files of livre.yaml)
Run from the monographie/ directory.
"""
import re
import sys
from pathlib import Path

STATUTS = {'définition', 'résultat sous hypothèses', 'hypothèse de travail', 'constat empirique'}
PREFIXES = ('sec', 'prop', 'def', 'fig', 'tbl', 'eq')
FORBIDDEN = [
    (re.compile(r'\b(TK|WG|FD|CR|RV)\b'), 'étiquette de source interne'),
    (re.compile(r'source_threads|content_spec|course_outline|course_specs|BUILDER_START_HERE', re.I), 'fichier de travail interne'),
    (re.compile(r'\b(carte|map)\s*v[12]\b', re.I), 'version de la carte'),
]
ROOT = Path(__file__).resolve().parent.parent
THREADS_FILE = ROOT.parent / 'content_spec' / 'source_threads_en.md'


def input_files():
    files, on = [], False
    for line in (ROOT / 'livre.yaml').read_text(encoding='utf-8').splitlines():
        if line.startswith('input-files:'):
            on = True
            continue
        if on:
            m = re.match(r'\s+-\s+(\S+)', line)
            if m:
                files.append(m.group(1))
            elif line.strip() and not line.startswith(' '):
                on = False
    return files


def bib_keys(name):
    p = ROOT / 'commun' / name
    return set(re.findall(r'@\w+\s*\{\s*([^,\s]+)\s*,', p.read_text(encoding='utf-8'))) if p.exists() else set()


def thread_ids():
    if not THREADS_FILE.exists():
        return []
    return re.findall(r'^#### `([\w-]+)`', THREADS_FILE.read_text(encoding='utf-8'), re.M)


def fenced_divs(lines, cls):
    """Yield (start line number, body text) for every fenced div of class cls, nesting-aware."""
    stack = []  # (class list, start index)
    for i, line in enumerate(lines):
        if re.match(r'^:{3,}\s*$', line):
            if stack:
                classes, start = stack.pop()
                if cls in classes:
                    yield start + 1, '\n'.join(lines[start + 1:i])
        else:
            m = re.match(r'^:{3,}\s*(\{([^}]*)\}|([\w-]+))', line)
            if m:
                attrs = m.group(2) or ('.' + m.group(3))
                stack.append((re.findall(r'\.([\w-]+)', attrs), i))


def strip_code(text):
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    return re.sub(r'`[^`\n]*`', '', text)


def main(argv):
    files = argv[1:] or input_files()
    errors, warnings, averif, stubs = [], [], [], []
    defined, used = {}, []
    verifiees, candidates = bib_keys('biblio.bib'), bib_keys('biblio_a_verifier.bib')
    ref_candidates = []
    tids = [t for t in thread_ids() if len(t) > 6]
    for f in files:
        p = ROOT / f
        if not p.exists():
            errors.append(f'{f}: fichier absent')
            continue
        text = p.read_text(encoding='utf-8')
        lines = text.splitlines()
        is_chapter = f.startswith('chapitres/')
        h1 = [l for l in lines if re.match(r'^# ', l)]
        if is_chapter and len(h1) != 1:
            errors.append(f'{f}: {len(h1)} titres de niveau 1 (attendu : 1)')
        if is_chapter and re.search(r'\{#sec:ch\d\d', text) and '{.points-cles}' not in text:
            errors.append(f'{f}: section « Points clés {{.points-cles}} » absente')
        if re.search(r'\*(Chapitre|Annexe) à rédiger\.\*', text):
            stubs.append(f)
        # labels defined (in attribute blocks of the file and of the generated files it includes)
        included = re.findall(r'\.inclure[^}]*fichier="([^"]+)"', text)
        sources = [(f, text)] + [(inc, (ROOT / inc).read_text(encoding='utf-8'))
                                 for inc in included if (ROOT / inc).exists()]
        for src, txt in sources:
            for lab in re.findall(r'\{[^}\n]*#((?:sec|prop|def|fig|tbl|eq):[\w-]+)', txt):
                if lab in defined and defined[lab] != src:
                    errors.append(f'{src}: étiquette en double {lab} (déjà dans {defined[lab]})')
                defined[lab] = src
        # statements
        for m in re.finditer(r'^:::+\s*\{([^}]*\.proposition[^}]*)\}', text, re.M):
            attrs = m.group(1)
            st = re.search(r'statut="([^"]*)"', attrs)
            lab = re.search(r'#(prop:[\w-]+)', attrs)
            where = f'{f}:{text[:m.start()].count(chr(10)) + 1}'
            if not lab:
                errors.append(f'{where}: proposition sans étiquette #prop:…')
            if not st or st.group(1) not in STATUTS:
                errors.append(f'{where}: proposition {lab.group(1) if lab else ""} sans statut valide')
        # per-line checks
        for i, line in enumerate(lines, 1):
            plain = strip_code(line)
            for ref in re.findall(r'-?@((?:%s):[\w-]+)' % '|'.join(PREFIXES), plain):
                used.append((ref, f'{f}:{i}'))
            for key in re.findall(r'(?<![\w.])-?@([A-Za-z][\w:-]*[\w])', plain):
                if key == 'A-VERIFIER' or key.split(':')[0] in PREFIXES:
                    continue
                if key in candidates and key not in verifiees:
                    ref_candidates.append(f'{f}:{i}: {key}')
                elif key not in verifiees:
                    errors.append(f'{f}:{i}: clé bibliographique inconnue « {key} » (ni vérifiée ni candidate)')
            for m in re.finditer(r'\[@A-VERIFIER:\s*([^\]]*)\]', line):
                averif.append(f'{f}:{i}: {m.group(1).strip()}')
            for rx, what in FORBIDDEN:
                if rx.search(plain):
                    errors.append(f'{f}:{i}: {what} : « {rx.search(plain).group(0)} »')
            for t in tids:
                if t in plain:
                    errors.append(f'{f}:{i}: identifiant de fil interne « {t} »')
            if re.search(r'\bamendement', plain, re.I):
                warnings.append(f'{f}:{i}: « amendement » — vérifier qu’il ne s’agit pas de vocabulaire de relecture')
        # quantitative examples: prose numbers vs included tables
        for start, body in fenced_divs(lines, 'exemple-quantitatif'):
            tables = re.findall(r'fichier="([^"]+)"', body)
            prose = re.sub(r'^:::+.*$', '', body, flags=re.M)
            prose = re.sub(r'\$[^$]*\$', '', prose)
            prose = re.sub(r'^!\[.*$', '', prose, flags=re.M)      # figure lines
            prose = re.sub(r'\{[^}\n]*\}', '', prose)             # attribute blocks
            nums = set(re.findall(r'(?<![\w.,])\d+(?:,\d+)?(?=\s?%|\b)', prose))
            nums = {n for n in nums if not re.fullmatch(r'\d', n)}  # ignore single digits (counts, steps)
            where = f'{f}:{start}'
            if not tables:
                warnings.append(f'{where}: exemple quantitatif sans tableau inclus (.inclure)')
                continue
            content = ''
            for t in tables:
                tp = ROOT / t
                if tp.exists():
                    content += tp.read_text(encoding='utf-8')
                else:
                    warnings.append(f'{where}: tableau généré absent : {t}')
            if content:
                missing = sorted(n for n in nums if n not in content)
                if missing:
                    warnings.append(f'{where}: nombres cités absents du tableau généré : {", ".join(missing)}')
    for ref, where in used:
        if ref not in defined:
            errors.append(f'{where}: référence à une étiquette non définie {ref}')

    out = []
    out.append(f'== Vérification : {len(files)} fichiers ==')
    out.append(f'Erreurs : {len(errors)}')
    out += ['  ✘ ' + e for e in errors]
    out.append(f'Avertissements : {len(warnings)}')
    out += ['  ! ' + w for w in warnings]
    out.append(f'Références à vérifier (texte libre [@A-VERIFIER: …]) : {len(averif)}')
    out += ['  ? ' + a for a in averif]
    out.append(f'Citations de références candidates (biblio_a_verifier.bib) : {len(ref_candidates)}')
    out += ['  ? ' + a for a in ref_candidates]
    out.append(f'Chapitres/annexes non rédigés : {len(stubs)}')
    out += ['  · ' + s for s in stubs]
    print('\n'.join(out))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
