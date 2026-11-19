"""log-score (ch. 3): one outcome barely grades a forecaster.

Outputs: figures/ch03-score-log.{pdf,svg}, tableaux/ch03-score-log.md
"""
import numpy as np
from _style import BLEU, ORANGE, ENCRE2, LARGEUR, debut, fr, pct_in, plt, sauver, tableau, parametres as P

debut(__file__)
rows, lr_casse, lr_tient = P.logscore_table()

fig, ax = plt.subplots(figsize=(LARGEUR, 2.9))
groupes = ['Le bateau casse', 'Le bateau tient']
x = np.arange(2)
w = 0.34
for k, (r, col) in enumerate(zip(rows, (BLEU, ORANGE))):
    vals = [r['casse'], r['tient']]
    bars = ax.bar(x + (k - 0.5) * (w + 0.02), vals, w, color=col, label=f"{r['prevision']} ({pct_in(r['p'])})")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.12, fr(v, 2 if v >= 1 else 3), ha='center', va='bottom',
                fontsize=8, color=ENCRE2)
ax.set_xticks(x, groupes)
ax.set_ylabel(r'surprise $-\ln \Pr(\mathrm{issue})$')
ax.set_ylim(0, 8.6)
ax.grid(axis='x', visible=False)
ax.legend(loc='upper right', title='Probabilité de casse annoncée', title_fontsize=8.5)
ax.text(0, 8.05, f'rapport de vraisemblance : {fr(lr_casse, 0)}', ha='center', fontsize=8, color=ENCRE2)
ax.text(1, 1.0, f'rapport de vraisemblance : {fr(lr_tient, 3)}', ha='center', fontsize=8, color=ENCRE2)
sauver(fig, 'ch03-score-log')

tableau('ch03-score-log',
        ['Prévision', 'Probabilité de casse', 'Surprise si le bateau casse', 'Surprise s’il tient'],
        [[r['prevision'], pct_in(r['p']), fr(r['casse'], 2), fr(r['tient'], 3)] for r in rows] +
        [['Rapport de vraisemblance (X contre Y)', '', fr(lr_casse, 0), fr(lr_tient, 3)]],
        'Surprise (score logarithmique) de deux prévisions selon l’issue de la course.')
