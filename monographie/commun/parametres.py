"""Canonical parameters and models of the quantitative examples — single source of truth.

Every figure, every generated table and every number quoted in a quantitative example
comes from here. Values and formulas follow content_spec/00_global.md (§4 models, §7 values).
Builders never edit this file; they propose new scenarios in notes/NOTES_NN.md.

Running this module directly checks the computed values against the canonical ones
published in the content spec (python3 commun/parametres.py).
"""
import math

# ---------------------------------------------------------------------------
# log-score (ch. 3): a forecast vs a forecaster
# ---------------------------------------------------------------------------
LOGSCORE = {'M. X': 0.05, 'M. Y': 0.001}  # believed probability that the light boat breaks


def surprise(prob):
    """Logarithmic score of an outcome that had probability prob: -ln(prob)."""
    return -math.log(prob)


def logscore_table():
    """Surprise of each forecaster under both outcomes, and the likelihood ratios X vs Y."""
    px, py = LOGSCORE['M. X'], LOGSCORE['M. Y']
    rows = [{'prevision': name, 'p': p, 'casse': surprise(p), 'tient': surprise(1 - p)}
            for name, p in LOGSCORE.items()]
    return rows, px / py, (1 - px) / (1 - py)


# ---------------------------------------------------------------------------
# seu-a (ch. 4) and seu-b (ch. 17): deciding on belief, model M2
# ---------------------------------------------------------------------------
def seuil(rapport):
    """Decision threshold p* = dU/(dU+L) = 1/(1 + L/dU)."""
    return 1.0 / (1.0 + rapport)


def risque_monde(p, z):
    """The world's failure probability when an omitted factor z adds its own chance: 1-(1-p)(1-z)."""
    return 1.0 - (1.0 - p) * (1.0 - z)


SEU_SCENARIOS = [  # (key, label, L/dU, p, b, z) — seu-a uses the rows with b = z = 0
    ('y', 'M. Y', 25, 0.001, 0.0, 0.0),
    ('x', 'M. X', 25, 0.05, 0.0, 0.0),
    ('fissure', 'M. Y, fissure non repérée', 25, 0.001, 0.0, 0.08),
    ('marge', '… avec une marge', 25, 0.001, 0.04, 0.08),
    ('prudence', 'Prudence superflue', 25, 0.001, 0.04, 0.0),
    ('roulette', 'Roulette russe', 10_000, 0.00001, 0.0, 1 / 6),
]


def seu(rapport, p, b, z):
    ps = seuil(rapport)
    decide = p + b
    go = decide < ps
    pw = risque_monde(p, z)
    if go and pw < ps:
        issue = 'départ justifié'
    elif go:
        issue = 'piège silencieux'
    elif p >= ps:
        issue = 'renoncement justifié'
    elif pw >= ps:
        issue = 'sauvé par la marge'
    else:
        issue = 'prudence superflue'
    return {'seuil': ps, 'decide': decide, 'go': go, 'monde': pw, 'issue': issue}


# ---------------------------------------------------------------------------
# chain-a (ch. 8) and chain-b (ch. 14): chains vs cross-checks, model M1
# ---------------------------------------------------------------------------
CHAIN_P = 0.06            # per-step error rate; the peer misses with the same probability
CHAIN_Q = (0.0, 0.03)     # shared omitted factor: one cause for all steps
CHAIN_N_A, CHAIN_N_B = 4, 12


def chaine(n, p, q):
    """Failure probabilities of an n-step chain, unchecked vs every step cross-checked by a peer."""
    a1 = (1 - p) ** n           # no independent error at all
    a2 = (1 - p * p) ** n       # no independent error that both producer and peer miss
    non_controle = 1 - a1 * (1 - q)
    controle = 1 - a2 * (1 - q)
    return {
        'non_controle': non_controle, 'controle': controle,
        'part_indep_non_controle': 1 - a1, 'part_indep_controle': 1 - a2,
        'part_q': (q / controle) if controle > 0 else 0.0,
    }


# ---------------------------------------------------------------------------
# escape-a (ch. 9) and escape-b (ch. 16): the checker model of M1
# ---------------------------------------------------------------------------
ESCAPE_PRESETS = [  # (key, label, P(E), c, m, f)
    ('pairs', 'Contrôle entre pairs', 0.10, 0.10, 0.20, 0.05),
    ('partage', 'Un modèle pour tous', 0.02, 0.60, 0.20, 0.05),
    ('partage_precis', 'Modèle partagé, contrôleur précis', 0.02, 0.60, 0.20, 0.005),
    ('indep_precis', 'Indépendant et précis', 0.02, 0.10, 0.10, 0.005),
]


def echappement(pe, c, m, f, politique='vpp'):
    """Checker model: sensitivity, PPV, uptake, escape probability and risk.

    politique='vpp': flags are heeded at the PPV rate (probability matching);
    politique='toutes': every flag is investigated (uptake = 1).
    """
    s = (1 - c) * (1 - m)
    vp, fp = pe * s, (1 - pe) * f
    vpp = vp / (vp + fp) if vp + fp > 0 else 0.0
    u = 1.0 if politique == 'toutes' else vpp
    esc = 1 - s * u
    return {'sensibilite': s, 'vpp': vpp, 'prise_en_compte': u, 'echappement': esc,
            'risque': pe * esc, 'cout': (1 / vpp) if vpp > 0 else float('inf')}


# ---------------------------------------------------------------------------
# plausibility (ch. 12): what re-asking catches
# ---------------------------------------------------------------------------
PLAUSIBILITE_ECHANTILLONS = 5
PLAUSIBILITE = {  # mode -> (question, [(answer, probability in %, right?)])
    'connu': ('Dans quelle ville se trouve la tour Eiffel ?',
              [('Paris', 97, True), ('Lyon', 2, False), ('Marseille', 1, False)]),
    'arbitraire': ('Quand est née une personne obscure, mentionnée une seule fois dans le corpus ?',
                   [('14 mai', 22, False), ('3 août', 20, False), ('22 nov.', 18, True),
                    ('9 janv.', 16, False), ('17 oct.', 14, False), ('une autre date', 10, False)]),
    'idee_recue': ('Quelle planète est, en moyenne, la plus proche de la Terre ?',
                   [('Vénus', 88, False), ('Mercure', 9, True), ('Mars', 3, False)]),
}
PLAUSIBILITE_NOMS = {'connu': 'Fait bien connu', 'arbitraire': 'Fait rare et arbitraire',
                     'idee_recue': 'Idée reçue répandue'}


def plausibilite(items, k=PLAUSIBILITE_ECHANTILLONS):
    """P(one answer wrong); severity = P(k answers disagree | first wrong); P(flag | first right)."""
    faux = [pct / 100 for _, pct, ok in items if not ok]
    justes = [pct / 100 for _, pct, ok in items if ok]
    pf, pj = sum(faux), sum(justes)
    sev = 1 - sum(x ** k for x in faux) / pf if pf else 0.0
    fausse_alerte = 1 - sum(x ** k for x in justes) / pj if pj else 0.0
    return {'p_faux': pf, 'severite': sev, 'fausse_alerte': fausse_alerte}


# ---------------------------------------------------------------------------
# Plain-arithmetic examples (ch. 0, ch. 9)
# ---------------------------------------------------------------------------
TEASER = [(0.01, 0.90), (0.10, 0.01)]          # (error rate, escape probability)
DEPISTAGE = {'prevalence': 0.01, 'sensibilite': 0.90, 'faux_positifs': 0.05}
DESACCORD = {'producteur': 0.01, 'relecteur': 0.10}


def vpp_depistage(prevalence, sensibilite, faux_positifs):
    vp = prevalence * sensibilite
    return vp / (vp + (1 - prevalence) * faux_positifs)


def desaccords_producteur_juste(producteur, relecteur):
    """Share of disagreements in which the producer was right (independent errors)."""
    prod_faux = producteur * (1 - relecteur)
    prod_juste = (1 - producteur) * relecteur
    return prod_juste / (prod_faux + prod_juste)


# ---------------------------------------------------------------------------
# Self-check against the canonical values of content_spec/00_global.md §7
# ---------------------------------------------------------------------------
def _canon():
    """(description, computed, expected, tolerance) — tolerances match the published rounding."""
    out = []
    rows, lr_casse, lr_tient = logscore_table()
    out += [('surprise X casse', rows[0]['casse'], 3.00, 0.005), ('surprise Y casse', rows[1]['casse'], 6.91, 0.005),
            ('surprise X tient', rows[0]['tient'], 0.051, 0.0005), ('LR casse', lr_casse, 50, 1e-9),
            ('LR tient', lr_tient, 0.951, 0.0005), ('p* (25)', seuil(25), 0.0385, 0.00005),
            ('p* (10 000)', seuil(10_000), 0.000100, 5e-7)]
    out += [('monde, fissure', seu(25, 0.001, 0, 0.08)['monde'], 0.0809, 0.00005)]
    for n, q, nc, cc, part in [(4, 0, .219, .0143, None), (4, .03, .243, .0439, .683),
                               (12, 0, .524, .0424, None), (12, .03, .538, .0711, .422)]:
        r = chaine(n, CHAIN_P, q)
        out += [(f'chaîne N={n} q={q} non contrôlée', r['non_controle'], nc, .0005),
                (f'chaîne N={n} q={q} contrôlée', r['controle'], cc, .00005)]
        if part is not None:
            out.append((f'chaîne N={n} part de q', r['part_q'], part, .0005))
    expected = {'pairs': (.72, .615, .557, .280, 1.6), 'partage': (.32, .116, .963, .680, 8.7),
                'partage_precis': (.32, .566, .819, .680, 1.8), 'indep_precis': (.81, .768, .378, .190, 1.3)}
    for key, _, pe, c, m, f in ESCAPE_PRESETS:
        a, t = echappement(pe, c, m, f, 'vpp'), echappement(pe, c, m, f, 'toutes')
        s, vpp, e1, e2, cout = expected[key]
        out += [(f'{key} s', a['sensibilite'], s, .0005), (f'{key} VPP', a['vpp'], vpp, .0005),
                (f'{key} échappement VPP', a['echappement'], e1, .0005),
                (f'{key} échappement toutes', t['echappement'], e2, .0005), (f'{key} 1/VPP', a['cout'], cout, .05)]
    for mode, (pf, sev, fa) in {'connu': (.03, 1.0, .115), 'arbitraire': (.82, .999, .999),
                                'idee_recue': (.91, .420, 1.0)}.items():
        r = plausibilite(PLAUSIBILITE[mode][1])
        out += [(f'{mode} P(faux)', r['p_faux'], pf, .0005), (f'{mode} sévérité', r['severite'], sev, .0015),
                (f'{mode} fausse alerte', r['fausse_alerte'], fa, .0015)]
    out += [('VPP dépistage', vpp_depistage(**DEPISTAGE), .154, .0005),
            ('désaccords producteur juste', desaccords_producteur_juste(**DESACCORD), .917, .0005)]
    return out


def verifier_canon():
    """Raise if any computed value drifts from the canonical values published in the content spec."""
    bad = [(d, v, e) for d, v, e, tol in _canon() if abs(v - e) > tol]
    if bad:
        raise AssertionError('valeurs canoniques non reproduites : ' + '; '.join(f'{d}: {v:.5g} ≠ {e}' for d, v, e in bad))
    return len(_canon())


if __name__ == '__main__':
    print(f'{verifier_canon()} valeurs canoniques reproduites.')
