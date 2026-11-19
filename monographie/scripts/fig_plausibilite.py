"""plausibility (ch. 12): what re-asking catches — guessing errors scatter, consistent errors repeat.

Outputs: figures/ch12-plausibilite.{pdf,svg}, tableaux/ch12-plausibilite.md
"""
from _style import BLEU, ENCRE2, NEUTRE, LARGEUR, debut, pct, pct_in, plt, sauver, tableau, parametres as P

debut(__file__)
modes = ['connu', 'arbitraire', 'idee_recue']
k = P.PLAUSIBILITE_ECHANTILLONS

fig, axes = plt.subplots(1, 3, figsize=(LARGEUR, 2.9), sharex=True)
for ax, mode in zip(axes, modes):
    _, items = P.PLAUSIBILITE[mode]
    st = P.plausibilite(items)
    noms = [a for a, _, _ in items][::-1]
    vals = [v for _, v, _ in items][::-1]
    cols = [BLEU if ok else NEUTRE for _, _, ok in items][::-1]
    ax.barh(range(len(items)), vals, color=cols, height=0.62)
    for i, (v, (_, _, ok)) in enumerate(zip(vals, items[::-1])):
        ax.text(v + 2, i, f'{v} %' + ('  ✓ juste' if ok else ''), va='center', fontsize=7.5, color=ENCRE2)
    ax.set_yticks(range(len(items)), noms, fontsize=7.5)
    ax.set_xlim(0, 135)
    ax.set_xticks([])
    ax.grid(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='y', length=0)
    ax.set_title(P.PLAUSIBILITE_NOMS[mode], loc='left', fontsize=8.5)
    ax.text(0, -0.06, f'sévérité : {pct(st["severite"])}\nalerte sur bonne réponse : {pct(st["fausse_alerte"])}',
            fontsize=7.5, color=ENCRE2, va='top', transform=ax.transAxes)
fig.tight_layout(w_pad=0.8)
sauver(fig, 'ch12-plausibilite')

rows = []
for mode in modes:
    _, items = P.PLAUSIBILITE[mode]
    st = P.plausibilite(items)
    dist = ', '.join(f'{a}{" ✓" if ok else ""} {v} %' for a, v, ok in items)
    rows.append([P.PLAUSIBILITE_NOMS[mode], dist, pct_in(st['p_faux']), pct(st['severite']), pct(st['fausse_alerte'])])
tableau('ch12-plausibilite',
        ['Question', 'Réponses (✓ = juste)', 'Réponse fausse', 'Sévérité', 'Alerte à tort'],
        rows, f'Reposer {k} fois la même question. Sévérité : probabilité que les {k} réponses divergent quand '
              'la première est fausse ; alerte à tort : qu’elles divergent alors qu’elle est juste.',
        ['l', 'l', 'r', 'r', 'r'])
