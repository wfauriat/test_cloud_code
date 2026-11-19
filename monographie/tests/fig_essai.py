"""Toolchain self-test: one generated figure (pdf + svg) and one generated number table.

Run from monographie/tests/ (make essai does it). Writes tests/figures/ and tests/tableaux/.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

here = Path(__file__).parent
(here / 'figures').mkdir(exist_ok=True)
(here / 'tableaux').mkdir(exist_ok=True)

ratios = np.logspace(0, 5, 200)
seuil = 1 / (1 + ratios)
fig, ax = plt.subplots(figsize=(6, 3.4))
ax.loglog(ratios, seuil * 100, color='#3A4BC8')
for nom, p in [('M. Y', 0.1), ('M. X', 5.0)]:
    ax.axhline(p, ls='--', lw=0.8, color='#888')
    ax.text(1.2, p * 1.15, nom, fontsize=8)
ax.axvline(25, ls=':', lw=0.8, color='#A35F00')
ax.set_xlabel('rapport des enjeux L/ΔU')
ax.set_ylabel('seuil p∗ (%)')
fig.tight_layout()
for ext in ('pdf', 'svg'):
    fig.savefig(here / 'figures' / f'essai-seuil.{ext}')

def fr(x, nd=2):
    return f'{x:.{nd}f}'.replace('.', ',')

rows = [('25', fr(100 / 26)), ('100', fr(100 / 101)), ('10 000', fr(100 / 10001, 4))]
table = '| L/ΔU | p∗ (%) |\n|---:|---:|\n' + ''.join(f'| {a} | {b} |\n' for a, b in rows)
table += '\nTable: Seuil p∗ pour trois rapports des enjeux. {#tbl:ch00-seuils}\n'
(here / 'tableaux' / 'essai-seuil.md').write_text(table, encoding='utf-8')
print('essai : figure et tableau générés')
