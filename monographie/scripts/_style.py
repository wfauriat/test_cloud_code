"""Shared figure style, French number formatting and table writer for scripts/fig_*.py.

Figures: print-first (PDF) with an SVG twin for HTML. Book font (TeX Gyre Pagella),
thin marks, hairline solid grid, at most three categorical colours (validated palette:
blue, orange, aqua, all-pairs safe), identity never carried by colour alone
(line style, position or direct labels back it up). Every figure ships with a number table.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'commun'))

import matplotlib  # noqa: E402
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

import parametres  # noqa: E402,F401  (re-exported for the scripts)

# Validated categorical slots (dataviz reference palette, slots 1-3) and neutral inks
BLEU, ORANGE, AQUA = '#2a78d6', '#eb6834', '#1baf7a'
ENCRE, ENCRE2, MUET, GRILLE = '#1d232b', '#52514e', '#8a8984', '#e4e3df'
NEUTRE = '#b9b8b2'  # de-emphasized marks

LARGEUR = 5.6  # inches: fits the text block of the book


def _polices():
    for f in ('texgyrepagella-regular.otf', 'texgyrepagella-italic.otf', 'texgyrepagella-bold.otf'):
        try:
            path = subprocess.run(['kpsewhich', f], capture_output=True, text=True).stdout.strip()
        except FileNotFoundError:
            path = ''
        if path:
            font_manager.fontManager.addfont(path)


_polices()
plt.rcParams.update({
    'font.family': ['TeX Gyre Pagella', 'DejaVu Serif'],
    'font.size': 9, 'axes.titlesize': 9.5, 'axes.labelsize': 9, 'legend.fontsize': 8.5,
    'xtick.labelsize': 8.5, 'ytick.labelsize': 8.5,
    'mathtext.fontset': 'stix',
    'axes.edgecolor': ENCRE2, 'axes.linewidth': 0.6, 'axes.labelcolor': ENCRE, 'text.color': ENCRE,
    'xtick.color': ENCRE2, 'ytick.color': ENCRE2, 'xtick.major.width': 0.6, 'ytick.major.width': 0.6,
    'axes.spines.top': False, 'axes.spines.right': False,
    'axes.grid': True, 'grid.color': GRILLE, 'grid.linewidth': 0.5, 'grid.linestyle': '-',
    'axes.axisbelow': True, 'lines.linewidth': 1.6, 'lines.markersize': 6,
    'legend.frameon': False, 'figure.dpi': 150,
    'savefig.bbox': 'tight', 'savefig.pad_inches': 0.04, 'savefig.facecolor': 'white',
    'pdf.fonttype': 3, 'svg.fonttype': 'path',  # Pagella is CFF-based: type 42 would mis-embed
})


# --------------------------------------------------------------------- numbers
def fr(x, nd=2):
    """Fixed decimals, decimal comma, space as thousands separator: 10 000 ; 3,85."""
    s = f'{x:,.{nd}f}'
    return s.replace(',', ' ').replace('.', ',')


def _strip(s):
    return s.rstrip('0').rstrip(',') if ',' in s else s


def sig(x, n=3):
    """n significant digits, trailing zeros kept (results): 3,85 ; 0,0100 ; 28,0."""
    s = f'{x:#.{n}g}'.rstrip('.')
    if 'e' in s:
        s = f'{x:.{n}f}'
    return s.replace('.', ',')


def pct(x, n=3):
    """A computed probability as a percentage with n significant digits: 3,85 %."""
    v = 100 * x
    if v > 99.95 and v < 100:
        return '> 99,9 %'
    return sig(v, n) + ' %'


def pct_in(x):
    """An input parameter as a percentage: 3 significant digits, no trailing zeros (0,1 % ; 5 % ; 16,7 %)."""
    return _strip(sig(100 * x, 3)) + ' %'


def format_pct_axe(v, _pos=None):
    if v <= 0:
        return '0 %'
    return (_strip(f'{v:.4f}'.replace('.', ',')) if v < 1 else fr(v, 0) if v >= 1 and v == int(v) else sig(v, 2)) + ' %'


PCT_AXE = FuncFormatter(format_pct_axe)
NOMBRE_AXE = FuncFormatter(lambda v, _p=None: fr(v, 0) if v >= 1 else _strip(f'{v:.4f}'.replace('.', ',')))


# --------------------------------------------------------------------- output
def sauver(fig, nom):
    """Write figures/<nom>.pdf (print) and figures/<nom>.svg (HTML)."""
    out = ROOT / 'figures'
    out.mkdir(exist_ok=True)
    for ext in ('pdf', 'svg'):
        fig.savefig(out / f'{nom}.{ext}')
    plt.close(fig)
    print(f'  figure  figures/{nom}.pdf (+ .svg)')


def tableau(nom, entetes, lignes, legende, alignements=None):
    """Write tableaux/<nom>.md: a pipe table with caption and label {#tbl:<nom>}."""
    alignements = alignements or ['l'] + ['r'] * (len(entetes) - 1)
    sep = {'l': ':--', 'r': '--:', 'c': ':-:'}
    md = '| ' + ' | '.join(entetes) + ' |\n'
    # dash counts set pandoc's relative column widths (content length; headers count half: they wrap)
    largeurs = [max([len(str(h)) // 2, max(len(w) for w in str(h).split()) + 1]
                    + [len(str(r[i])) for r in lignes] + [3]) for i, h in enumerate(entetes)]
    if sum(largeurs) < 90:  # pandoc wraps cells (relative widths) only when the source line exceeds 72 columns
        largeurs = [max(3, round(w * 90 / sum(largeurs))) for w in largeurs]
    md += '|' + '|'.join({'l': ':', 'r': '', 'c': ':'}[a] + '-' * w + {'l': '', 'r': ':', 'c': ':'}[a]
                         for a, w in zip(alignements, largeurs)) + '|\n'
    for row in lignes:
        md += '| ' + ' | '.join(str(c) for c in row) + ' |\n'
    md += f'\nTable: {legende} {{#tbl:{nom}}}\n'
    out = ROOT / 'tableaux'
    out.mkdir(exist_ok=True)
    (out / f'{nom}.md').write_text(md, encoding='utf-8')
    print(f'  tableau tableaux/{nom}.md')


def debut(script):
    """Common start of every figure script: check the canonical values first."""
    n = parametres.verifier_canon()
    print(f'{Path(script).name} — {n} valeurs canoniques vérifiées')
