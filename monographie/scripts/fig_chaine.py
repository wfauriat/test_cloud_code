"""chain-a (ch. 8) and chain-b (ch. 14): chains vs cross-checks with a shared omitted factor (model M1).

Outputs: figures/ch08-chaine.{pdf,svg}, tableaux/ch08-chaine.md,
         figures/ch14-chaine-agent.{pdf,svg}, tableaux/ch14-chaine-agent.md
"""
import numpy as np
from _style import BLEU, ORANGE, ENCRE2, MUET, LARGEUR, PCT_AXE, debut, pct, pct_in, plt, sauver, tableau, parametres as P

debut(__file__)
p, (q0, q1) = P.CHAIN_P, P.CHAIN_Q


def figure(n_max, n_cle, nom):
    n = np.arange(1, n_max + 1)
    fig, ax = plt.subplots(figsize=(LARGEUR, 3.6))
    series = [('non_controle', ORANGE, 'chaîne sans contrôle'), ('controle', BLEU, 'chaque étape contrôlée par un pair')]
    for cle, col, lab in series:
        for q, ls in ((q0, '-'), (q1, (0, (4, 2.5)))):
            vals = [100 * P.chaine(k, p, q)[cle] for k in n]
            ax.plot(n, vals, color=col, ls=ls, label=f'{lab}, q = {pct_in(q)}')
            v = 100 * P.chaine(n_cle, p, q)[cle]
            ax.plot([n_cle], [v], 'o', color=col, mec='white', mew=1.2, ms=6, zorder=3)
    ax.axvline(n_cle, color=MUET, lw=0.6)
    r = P.chaine(n_cle, p, q1)
    ax.annotate(f'N = {n_cle} : facteur partagé\n= {pct(r["part_q"])} des défaillances restantes',
                (n_cle, 100 * r['controle']), xytext=(-14 if n_cle == n_max else 16, 30), textcoords='offset points',
                ha='right' if n_cle == n_max else 'left',
                fontsize=8, color=ENCRE2, arrowprops=dict(arrowstyle='-', color=MUET, lw=0.6))
    ax.set_xlabel('nombre d’étapes N')
    ax.set_ylabel('probabilité d’échec de la chaîne')
    ax.set_xticks(n)
    ax.set_xlim(0.6, n_max + 0.4)
    ax.set_ylim(0, None)
    ax.yaxis.set_major_formatter(PCT_AXE)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=2, title=f'erreur par étape p = {pct_in(p)}',
              title_fontsize=8.5)
    sauver(fig, nom)


def table(n_cle, nom, legende):
    rows = []
    for q in (q0, q1):
        r = P.chaine(n_cle, p, q)
        rows.append([str(n_cle), pct_in(q), pct(r['non_controle']), pct(r['controle']),
                     f"{pct(r['part_indep_non_controle'])} → {pct(r['part_indep_controle'])}",
                     pct(r['part_q']) if q > 0 else '—'])
    tableau(nom, ['N', 'Facteur partagé q', 'Chaîne sans contrôle', 'Contrôle croisé à chaque étape',
                  'Part indépendante (sans → avec contrôle)', 'Part des défaillances restantes due à q'],
            rows, legende)


figure(8, P.CHAIN_N_A, 'ch08-chaine')
table(P.CHAIN_N_A, 'ch08-chaine', 'Chaîne et contrôle croisé, avec et sans facteur omis partagé (N = 4).')
figure(P.CHAIN_N_B, P.CHAIN_N_B, 'ch14-chaine-agent')
table(P.CHAIN_N_B, 'ch14-chaine-agent', 'Trajectoire d’agent en douze étapes, avec et sans facteur omis partagé.')
