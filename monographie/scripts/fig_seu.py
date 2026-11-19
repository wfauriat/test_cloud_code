"""seu-a (ch. 4) and seu-b (ch. 17): deciding on belief while the world holds its own odds (model M2).

Outputs: figures/ch04-seuil.{pdf,svg}, tableaux/ch04-seuil.md,
         figures/ch17-decisions.{pdf,svg}, tableaux/ch17-decisions.md
"""
import numpy as np
from _style import (BLEU, ORANGE, ENCRE2, MUET, LARGEUR, NOMBRE_AXE, PCT_AXE, debut, fr, pct, pct_in,
                    plt, sauver, tableau, parametres as P)

debut(__file__)
SC = {k: (lab, r, p, b, z) for k, lab, r, p, b, z in P.SEU_SCENARIOS}

# ---------------------------------------------------------------- seu-a: threshold curve
fig, ax = plt.subplots(figsize=(LARGEUR, 3.3))
r = np.logspace(0, 5, 400)
ax.loglog(r, 100 * P.seuil(r), color=BLEU)
for k, dy in (('x', 1.25), ('y', 1.25)):
    lab, _, p, _, _ = SC[k]
    ax.axhline(100 * p, color=MUET, lw=0.8, ls=(0, (4, 3)))
    ax.text(1.15, 100 * p * dy, f'{lab} : p = {pct_in(p)}', fontsize=8, color=ENCRE2, va='bottom')
for k, txt, off in (('y', None, (10, -16)), ('roulette', 'roulette russe', (14, 34))):
    lab, rr, *_ = SC[k]
    ps = P.seuil(rr)
    ax.plot([rr], [100 * ps], 'o', color=BLEU, mec='white', mew=1.2, ms=7, zorder=3)
    label = f'L/ΔU = {fr(rr, 0)} : p∗ = {pct(ps)}' + (f'\n({txt})' if txt else '')
    ax.annotate(label, (rr, 100 * ps), xytext=off, textcoords='offset points', fontsize=8,
                ha='left' if off[0] > 0 else 'right', va='top', color=ENCRE2,
                bbox=dict(boxstyle='square,pad=0.15', fc='white', ec='none'))
ax.set_xlabel('rapport des enjeux L/ΔU (perte en cas d’échec / gain en cas de succès)')
ax.set_ylabel('seuil p∗ (probabilité d’échec)')
ax.xaxis.set_major_formatter(NOMBRE_AXE)
ax.yaxis.set_major_formatter(PCT_AXE)
ax.set_ylim(1e-3, 100)
ax.text(2e4, 25, 'on part si p < p∗', fontsize=8, color=ENCRE2, ha='right')
sauver(fig, 'ch04-seuil')

rows = []
for k in ('y', 'x', 'roulette'):
    lab, rr, p, b, z = SC[k]
    s = P.seu(rr, p, 0.0, 0.0)
    rows.append([lab, fr(rr, 0), pct_in(p), pct(s['seuil']), 'on part' if s['go'] else 'on renonce'])
tableau('ch04-seuil', ['Situation', 'L/ΔU', 'p estimé', 'Seuil p∗', 'Décision'], rows,
        'Seuil de décision et choix de chaque décideur (sans facteur omis).', ['l', 'r', 'r', 'r', 'l'])

# ---------------------------------------------------------------- seu-b: four outcomes
fig, ax = plt.subplots(figsize=(LARGEUR, 4.4))
ax.set_xscale('log')
ax.set_yscale('log')
lo, hi = 0.005, 5e3
ax.axvline(1, color=ENCRE2, lw=0.8)
ax.axhline(1, color=ENCRE2, lw=0.8)
quadrants = [((0.0065, 0.0065), 'départ justifié'), ((0.0065, 3.8e3), 'piège silencieux'),
             ((3.8e3, 3.8e3), 'renoncement justifié'), ((3.8e3, 0.0065), 'prudence superflue')]
for (qx, qy), t in quadrants:
    ax.text(qx, qy, t, fontsize=8.5, color=MUET, style='italic',
            ha='left' if qx < 1 else 'right', va='bottom' if qy < 1 else 'top')
pts = {}
for k, (lab, rr, p, b, z) in SC.items():
    s = P.seu(rr, p, b, z)
    pts[k] = (s['decide'] / s['seuil'], s['monde'] / s['seuil'], s)
offsets = {'y': (8, 4), 'x': (9, -12), 'fissure': (-4, 9), 'marge': (9, 6), 'prudence': (9, 4), 'roulette': (9, -3)}
for k, (xv, yv, s) in pts.items():
    col = ORANGE if s['issue'] == 'piège silencieux' else BLEU
    ax.plot([xv], [yv], 'o', color=col, mec='white', mew=1.2, ms=7, zorder=3)
    ax.annotate(SC[k][0], (xv, yv), xytext=offsets[k], textcoords='offset points', fontsize=8, color=ENCRE2)
x0, y0, _ = pts['fissure']
x1, y1, _ = pts['marge']
ax.annotate('', xy=(x1 * 0.93, y1), xytext=(x0 * 1.12, y0),
            arrowprops=dict(arrowstyle='->', color=ENCRE2, lw=0.8))
ax.text((x0 * x1) ** 0.5, y0 / 1.45, 'marge d’humilité b', fontsize=8, color=ENCRE2, ha='center', va='top')
from matplotlib.lines import Line2D
ax.legend(handles=[Line2D([], [], marker='o', ls='', color=ORANGE, mec='white', label='piège silencieux'),
                   Line2D([], [], marker='o', ls='', color=BLEU, mec='white', label='autres situations')],
          loc='upper center', bbox_to_anchor=(0.5, -0.13), ncol=2)
ax.set_xlim(lo, hi)
ax.set_ylim(lo, hi)
ax.xaxis.set_major_formatter(NOMBRE_AXE)
ax.yaxis.set_major_formatter(NOMBRE_AXE)
ax.set_xlabel('(p + b) / p∗ : ce sur quoi l’on décide, rapporté au seuil')
ax.set_ylabel('risque réel / p∗ : ce que le monde réserve')
sauver(fig, 'ch17-decisions')

ordre = ('y', 'x', 'fissure', 'marge', 'prudence', 'roulette')
rows = []
for k in ordre:
    lab, rr, p, b, z = SC[k]
    rows.append([lab, fr(rr, 0), pct_in(p), pct_in(b), pct_in(z)])
tableau('ch17-scenarios', ['Situation', 'Rapport des enjeux L/ΔU', 'Ce que l’on pense p', 'Marge b',
                           'Facteur omis z (invisible)'],
        rows, 'Les six situations : ce que croit le décideur, et ce que le monde ajoute.')
rows = []
for k in ordre:
    lab, rr, p, b, z = SC[k]
    s = P.seu(rr, p, b, z)
    rows.append([lab, pct_in(s['decide']), pct(s['seuil']), 'on part' if s['go'] else 'on renonce',
                 pct(s['monde']), s['issue']])
tableau('ch17-decisions', ['Situation', 'On décide sur p + b', 'Seuil p∗', 'Décision', 'Risque réel', 'Issue'],
        rows, 'Décider sur ce que l’on croit quand le monde ajoute un risque omis.',
        ['l', 'r', 'r', 'l', 'r', 'l'])
