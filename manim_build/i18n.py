"""French translation of every visible text (labels, captions, titles).

Equations and notations are not translated (D_mes, D_void, A_object, A_cand, ...).
Keys are the exact English strings used in scenes.py / theme.py; templates use {name} placeholders.
French typography: a space before ':' and ';'.
"""

FR = {
    # ------------------------------------------------------------------ titles
    "Uniaxial X-ray tomography": "Tomographie X uniaxiale",
    "Phase 1: accounting - separate the object's contribution from the rest":
        "Phase 1 : bilan - séparer la contribution de l'objet du reste",
    "Phase 2: inverting - what each pixel row sees": "Phase 2 : inversion - ce que voit chaque ligne de pixels",
    "Phase 2: inverting - optimization: stack bricks until the screens match":
        "Phase 2 : inversion - optimisation par empilement de briques",
    "Phase 2: inverting –": "Phase 2 : inversion –",
    "why gradients help the optimization": "pourquoi les gradients aident l'optimisation",
    "Going further 1 - noise in the measurement": "Pour aller plus loin 1 - bruit de mesure",
    "Going further 2 - two possible materials": "Pour aller plus loin 2 - deux matériaux possibles",
    "Going further 3 - a biased blank": "Pour aller plus loin 3 - un tir à vide biaisé",

    # ------------------------------------------------------------------ shared labels (theme)
    "Source (X-rays)": "Source (rayons X)",
    "Confinement casing": "Enceinte de confinement",
    "Screen (1 slice)": "Écran (1 coupe)",
    "high\nabsorption": "forte\nabsorption",
    "low\nabsorption": "faible\nabsorption",
    "density": "densité",
    "dashed: true density": "pointillés : densité vraie",
    "observed": "observé",
    "candidate": "candidat",

    # ------------------------------------------------------------------ S1
    "Object: concentric shells": "Objet : couches concentriques",
    "The object is circular and symmetric: one half-slice describes it.":
        "L'objet est circulaire et symétrique : une demi-coupe suffit à le décrire.",
    "The screen has one pixel per row i, and one row per shell.":
        "L'écran a un pixel par ligne i, et une ligne par couche.",
    "X-rays are absorbed by the casing walls and by every shell they cross.":
        "Les rayons X sont absorbés par les parois de l'enceinte et par chaque couche traversée.",
    "D: dose.   A: fraction of the dose let through (between 0 and 1).":
        "D : dose.   A : fraction de la dose transmise (entre 0 et 1).",
    r"\text{ unknown}": r"\text{ inconnues}",
    r"\qquad D_0,\ A_{\text{casing}},\ L_{ik} \text{ known}": r"\qquad D_0,\ A_{\text{casing}},\ L_{ik} \text{ connus}",

    # ------------------------------------------------------------------ S2
    "Calibration shot, or simulation without the object (a blank virtual shot).":
        "Tir d'étalonnage, ou simulation sans l'objet (un tir à vide virtuel).",
    "Measurement shot: the object is in place.": "Tir de mesure : l'objet est en place.",
    "dose": "dose",
    "Pixel by pixel, dividing by the blank shot cancels the source and the casing.":
        "Pixel par pixel, diviser par le tir à vide élimine la source et l'enceinte.",
    "In log scale the division is a plain difference: p is due to the object only.":
        "En échelle log, la division devient une simple différence : p ne dépend que de l'objet.",

    # ------------------------------------------------------------------ S3
    "fraction of\nabsorption": "fraction\nd'absorption",
    "traversed length": "longueur traversée",
    "Row i crosses shells 1 to i, over path lengths fixed by the geometry.":
        "La ligne i traverse les couches 1 à i, sur des longueurs fixées par la géométrie.",
    "One equation per pixel row: A = exp(-L ρ).": "Une équation par ligne de pixels : A = exp(-L ρ).",
    "Triangular structure: row i only depends on shells 1 to i.":
        "Structure triangulaire : la ligne i ne dépend que des couches 1 à i.",

    # ------------------------------------------------------------------ S4
    "candidate object": "objet candidat",
    "move": "coup",
    r"\text{mismatch}": r"\text{\'ecart}",
    "Start empty: the candidate screen lets everything through, far from the observation.":
        "Départ à vide : l'écran candidat laisse tout passer, loin de l'observation.",
    "Each move adds the brick that lowers the mismatch most: one step downhill.":
        "Chaque coup ajoute la brique qui réduit le plus l'écart : un pas vers le bas.",
    "Outer shells come first: the top rows only see them.":
        "Les couches externes d'abord : les lignes du haut ne voient qu'elles.",
    "exact match": "accord exact",
    "Screens match pixel by pixel: densities recovered (true: 0.4, 1.0, 1.4, 0.8, 0.6).":
        "Les écrans coïncident pixel par pixel : densités retrouvées (vraies : 0.4, 1.0, 1.4, 0.8, 0.6).",

    # ------------------------------------------------------------------ S5
    "Step walk:": "Marche pas à pas :",
    "knows the mismatch only where it tries;": "ne connaît l'écart que là où elle essaie ;",
    "probes the neighbours, one brick at a time.": "sonde les voisins, une brique à la fois.",
    "Gradient:": "Gradient :",
    "slope known everywhere, all shells at once.": "pente connue partout, pour toutes les couches à la fois.",
    "Step walk": "Pas à pas",
    "Gradient walk": "Par gradient",
    "fixed": "fixe",
    "steps:": "pas :",
    "Mismatch for every (ρ1, ρ2), shells 3 to 5 fixed: a landscape with one valley (light = small).":
        "Écart pour chaque (ρ1, ρ2), couches 3 à 5 fixées : un paysage à une seule vallée (clair = faible).",
    "Step walk: try each neighbouring brick, keep the best, repeat.":
        "Marche pas à pas : essayer chaque brique voisine, garder la meilleure, recommencer.",
    "The gradient gives the downhill direction at every point, without trying anything.":
        "Le gradient donne la direction de descente en tout point, sans rien essayer.",
    "Gradient walk: follow the slope, all densities together, with steps of any size.":
        "Marche par gradient : suivre la pente, toutes les densités ensemble, avec des pas de toute taille.",
    "Same answer: {a} single-brick steps (step walk) vs {b} gradient steps. "
    "With N shells, a brick step means 2N trials.":
        "Même résultat : {a} pas d'une brique contre {b} pas de gradient. "
        "Avec N couches, un pas de brique coûte 2N essais.",

    # ------------------------------------------------------------------ S6
    "noisy": "bruité",
    "exact": "exact",
    "measured absorption A\n({noise} noise)": "absorption mesurée A\n(bruit de {noise})",
    "invert\n(no regularization)": "inverser\n(sans régularisation)",
    "outer": "externe",
    "inner": "interne",
    "red: spread over many noise draws": "rouge : dispersion sur de nombreux tirages de bruit",
    "{noise} noise on the measured screen (10 shells): hardly visible on the screen.":
        "Bruit de {noise} sur l'écran mesuré (10 couches) : à peine visible à l'écran.",
    "But the reconstructed densities jump, and most at the centre (inner shells).":
        "Mais les densités reconstruites sautent, surtout au centre (couches internes).",
    "Spread over many draws: thin inner shells, short paths, strong amplification.":
        "Dispersion sur de nombreux tirages : couches internes fines, trajets courts, forte amplification.",
    "Without regularization, the centre of the object is unreliable.":
        "Sans régularisation, le centre de l'objet n'est pas fiable.",

    # ------------------------------------------------------------------ S7
    "material 1": "matériau 1",
    "material 2": "matériau 2",
    "the screen only sees  μ × ρ": "l'écran ne voit que  μ × ρ",
    "shells 1-3: material 1 (known)\nshells 4-5: material 1 or 2":
        "couches 1-3 : matériau 1 (connu)\ncouches 4-5 : matériau 1 ou 2",
    "candidates": "candidats",
    "Shells 1 to 3 are known to be material 1: their densities are fixed.":
        "Les couches 1 à 3 sont en matériau 1 (connu) : leurs densités sont fixées.",
    "Shells 4 and 5 may be material 1, or material 2 which absorbs half as much.":
        "Les couches 4 et 5 peuvent être en matériau 1, ou en matériau 2 qui absorbe deux fois moins.",
    "Material 2 needs twice the density for the same absorption: the screen does not change.":
        "Le matériau 2 demande une densité double pour la même absorption : l'écran ne change pas.",
    "all identical to the observed screen": "tous identiques à l'écran observé",
    "{n} objects, one screen: the measurement alone cannot tell them apart.":
        "{n} objets, un seul écran : la mesure seule ne permet pas de les distinguer.",
    "Extra information is needed: prior knowledge, or another measurement (e.g. a second X-ray energy).":
        "Il faut une information supplémentaire : connaissance a priori, ou une autre mesure "
        "(p. ex. une seconde énergie X).",

    # ------------------------------------------------------------------ S8
    "blank error (%)": "erreur sur le tir à vide (%)",
    "too dark": "trop sombre",
    "too bright": "trop clair",
    "With the right blank, the stacks match the true densities.":
        "Avec le bon tir à vide, les piles correspondent aux densités vraies.",
    "Blank too dark (source underestimated, or casing absorption overestimated):":
        "Tir à vide trop sombre (source sous-estimée, ou absorption de l'enceinte surestimée) :",
    "the object looks more transparent, so it comes out too light.":
        "l'objet paraît plus transparent : il ressort trop léger.",
    "Blank too bright (source overestimated, or casing absorption underestimated):":
        "Tir à vide trop clair (source surestimée, ou absorption de l'enceinte sous-estimée) :",
    "the object looks more absorbing, so it comes out too dense.":
        "l'objet paraît plus absorbant : il ressort trop dense.",
    "The error is the same on every row: the outer shell, seen by all rows, takes most of it.":
        "L'erreur est la même sur chaque ligne : la couche externe, vue par toutes les lignes, en prend l'essentiel.",
}
