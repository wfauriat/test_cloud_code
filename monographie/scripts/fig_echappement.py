"""escape-a (ch. 9) and escape-b (ch. 16): the checker model (M1) — PPV, uptake, escape, risk.

Outputs: figures/ch09-echappement.{pdf,svg}, tableaux/ch09-echappement.md,
         figures/ch16-modele-partage.{pdf,svg}, tableaux/ch16-modele-partage.md,
         tableaux/ch09-depistage.md, tableaux/ch09-desaccords.md, tableaux/ch09-taux-echappement.md
"""
import numpy as np
from _style import (BLEU, ORANGE, ENCRE2, MUET, NEUTRE, LARGEUR, PCT_AXE, debut, fr, pct, pct_in,
                    plt, sauver, tableau, parametres as P)

debut(__file__)
PRE = {k: (lab, pe, c, m, f) for k, lab, pe, c, m, f in P.ESCAPE_PRESETS}
POL = [('vpp', ORANGE, 'alertes suivies à hauteur de la VPP'), ('toutes', BLEU, 'chaque alerte examinée')]


def tableau_transpose(nom, cles, legende):
    """One column per scenario, one row per quantity: narrow enough for the text block."""
    res = {k: (P.echappement(*PRE[k][1:], 'vpp'), P.echappement(*PRE[k][1:], 'toutes')) for k in cles}
    lignes = [
        ['Taux d’erreur du producteur P(faux)'] + [pct_in(PRE[k][1]) for k in cles],
        ['Causes d’erreur partagées c'] + [pct_in(PRE[k][2]) for k in cles],
        ['Oubli sur les autres erreurs m'] + [pct_in(PRE[k][3]) for k in cles],
        ['Taux de fausses alertes f'] + [pct_in(PRE[k][4]) for k in cles],
        ['Sensibilité (1 − c)(1 − m)'] + [pct_in(res[k][0]['sensibilite']) for k in cles],
        ['Alertes qui sont de vraies erreurs (VPP)'] + [pct(res[k][0]['vpp']) for k in cles],
        ['Alertes par vraie erreur attrapée (1/VPP)'] + [fr(res[k][0]['cout'], 1) for k in cles],
        ['Échappement, alertes suivies à hauteur de la VPP'] + [pct(res[k][0]['echappement']) for k in cles],
        ['Échappement, chaque alerte examinée'] + [pct(res[k][1]['echappement']) for k in cles],
        ['Risque, alertes suivies à hauteur de la VPP'] + [pct(res[k][0]['risque']) for k in cles],
        ['Risque, chaque alerte examinée'] + [pct(res[k][1]['risque']) for k in cles],
        ['Risque sans contrôleur'] + [pct_in(PRE[k][1]) for k in cles],
    ]
    tableau(nom, ['Grandeur'] + [PRE[k][0] for k in cles], lignes, legende)



# ---------------------------------------------------------------- escape-a: fixed checker, P(E) varies
lab, pe0, c, m, f = PRE['pairs']
pe = np.logspace(-3, np.log10(0.3), 200)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(LARGEUR, 2.9), sharex=True)
for pol, col, nom in POL:
    esc = [100 * P.echappement(x, c, m, f, pol)['echappement'] for x in pe]
    rk = [100 * P.echappement(x, c, m, f, pol)['risque'] for x in pe]
    a1.plot(100 * pe, esc, color=col, label=nom)
    a2.plot(100 * pe, rk, color=col)
    r0 = P.echappement(pe0, c, m, f, pol)
    a1.plot([100 * pe0], [100 * r0['echappement']], 'o', color=col, mec='white', mew=1.2, ms=6, zorder=3)
    a2.plot([100 * pe0], [100 * r0['risque']], 'o', color=col, mec='white', mew=1.2, ms=6, zorder=3)
a2.plot(100 * pe, 100 * pe, color=NEUTRE, lw=1.2, label='sans contrôleur')
a2.text(17, 100 * 0.17 * 1.15, 'sans contrôleur', color=MUET, fontsize=8, ha='right', va='bottom')
for ax, titre in ((a1, 'probabilité d’échappement'), (a2, 'risque : erreurs suivies d’effet')):
    ax.set_xscale('log')
    ax.set_title(titre, loc='left')
    ax.xaxis.set_major_formatter(PCT_AXE)
    ax.yaxis.set_major_formatter(PCT_AXE)
    ax.set_xlabel('taux d’erreur du producteur P(faux)')
a1.set_ylim(0, 100)
a2.set_yscale('log')
a2.yaxis.set_major_formatter(PCT_AXE)
a1.legend(loc='lower left', fontsize=8)
fig.tight_layout(w_pad=2.5)
sauver(fig, 'ch09-echappement')
tableau_transpose('ch09-echappement', ['pairs', 'indep_precis'],
        f'Contrôleur fixe (c = {pct_in(c)}, m = {pct_in(m)}, f = {pct_in(f)}) : contrôle entre pairs, '
        'et un contrôleur indépendant et précis pour comparaison.')

# ---------------------------------------------------------------- escape-b: shared model
cles = ['pairs', 'partage', 'partage_precis', 'indep_precis']
noms = ['Contrôle entre pairs', 'Un modèle pour tous', 'Modèle partagé,\ncontrôleur précis', 'Indépendant et précis']
y = np.arange(len(cles))[::-1]
h = 0.36
fig, (a1, a2) = plt.subplots(1, 2, figsize=(LARGEUR, 3.3), sharey=True, gridspec_kw={'width_ratios': [1.15, 1]})
for k, (pol, col, nom) in enumerate(POL):
    esc = [100 * P.echappement(*PRE[c_][1:], pol)['echappement'] for c_ in cles]
    rk = [100 * P.echappement(*PRE[c_][1:], pol)['risque'] for c_ in cles]
    dy = (0.5 - k) * (h + 0.04)
    a1.barh(y + dy, esc, h, color=col, label=nom)
    a2.barh(y + dy, rk, h, color=col)
for yi, c_ in zip(y, cles):  # risk without any checker = P(wrong): a neutral tick per group
    a2.vlines(100 * PRE[c_][1], yi - 0.45, yi + 0.45, color=ENCRE2, lw=1.0)
for ax, titre in ((a1, 'probabilité d’échappement'), (a2, 'risque : erreurs suivies d’effet')):
    ax.set_title(titre, loc='left')
    ax.xaxis.set_major_formatter(PCT_AXE)
    ax.grid(axis='y', visible=False)
    ax.tick_params(axis='y', length=0)
a1.set_yticks(y, noms, fontsize=8)
a1.set_xlim(0, 100)
a2.set_xlim(0, 11.5)
from matplotlib.lines import Line2D
poignees, etiquettes = a1.get_legend_handles_labels()
poignees.append(Line2D([], [], color=ENCRE2, lw=0, marker='|', markersize=11, markeredgewidth=1.2))
etiquettes.append('sans contrôleur (= P(faux))')
a1.legend(poignees, etiquettes, loc='upper center', bbox_to_anchor=(1.0, -0.12), ncol=3, fontsize=8)
fig.tight_layout(w_pad=1.5)
sauver(fig, 'ch16-modele-partage')
tableau_transpose('ch16-modele-partage', cles,
        'Quand producteur et contrôleur partagent un même modèle : corrélation et fausses alertes.')

# ---------------------------------------------------------------- plain-arithmetic tables (ch. 9)
d = P.DEPISTAGE
tableau('ch09-depistage', ['Prévalence', 'Sensibilité', 'Taux de faux positifs', 'Valeur prédictive positive'],
        [[pct_in(d['prevalence']), pct_in(d['sensibilite']), pct_in(d['faux_positifs']), pct(P.vpp_depistage(**d))]],
        'Un dépistage d’une affection rare : la plupart des résultats positifs sont faux.')
dd = P.DESACCORD
tableau('ch09-desaccords', ['Producteur dans l’erreur', 'Relecteur dans l’erreur', 'Désaccords où le producteur avait raison'],
        [[pct_in(dd['producteur']), pct_in(dd['relecteur']), pct(P.desaccords_producteur_juste(**dd))]],
        'Deux erreurs indépendantes : la plupart des désaccords donnent tort au relecteur.')
tableau('ch09-taux-echappement', ['Taux d’erreur', 'Probabilité d’échappement', 'Affirmations fausses suivies d’effet'],
        [[pct_in(e), pct_in(s), pct_in(e * s)] for e, s in P.TEASER],
        'Le producteur le plus fiable peut former le système le plus risqué.')
