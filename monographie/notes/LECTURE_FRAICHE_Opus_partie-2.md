# Lecture fraîche : partie 2 (« Ce qui peut nous détromper »)

Lecteur : Opus, première lecture, sans accès aux autres fichiers.

## Résumé (test de lisibilité)

1. La partie cherche ce qui peut signaler, à temps, qu'une représentation finie a omis l'essentiel. Elle prend ses exemples hors de l'IA pour dégager des mécanismes généraux.
2. Une barre d'erreur ne voit pas les facteurs omis. Un contrôle ne détecte une erreur que si cinq conditions sont réunies (comparateur, erreurs différentes, comparabilité, timing, autorité). Refaire un calcul dans le même cadre ne révèle jamais un facteur omis : seul un apport extérieur le peut.
3. L'indépendance est relative à une classe d'erreurs. Les chaînes additionnent les angles morts, les contrôles croisés n'en laissent que les communs, et le « blanchiment » ramène les seconds aux premières. Le risque réel est le produit de deux probabilités : que l'affirmation soit fausse, et que l'erreur échappe aux contrôles. Or la plupart des évaluations ne mesurent que la première.

Dans l'ensemble, le texte se lit bien. La plupart des constats relèvent du confort. Les deux points qui comptent sont un pronom ambigu (§ ch07) et une formule sur la barre d'erreur qui peut se lire de deux façons (§ ch05).

## Constats

### Gravité A

Aucun.

### Gravité B

**B1.** § ch07 : « Aucune procédure de contrôle de niveau supérieur ne lève cette limite, car elle reposerait à son tour sur un cadre fini qu'il faudrait contrôler. »
- Gêne : grammaticalement, « elle » renvoie d'abord à « cette limite », le féminin le plus proche, alors que le sens demande « la procédure ». Le lecteur doit revenir en arrière.
- Reformulation : « …ne lève cette limite, car une telle procédure reposerait à son tour sur un cadre fini qu'il faudrait contrôler. »
- Sens : ne bouge pas.

**B2.** § ch05 : « Une barre d'erreur ne mesure jamais que le désaccord entre des hypothèses admises au départ, et une hypothèse que personne n'a envisagée n'y contribue en rien. »
- Gêne : « le désaccord entre des hypothèses » se comprend mal, et il admet deux lectures.
  - (a) La barre mesure l'écart entre plusieurs hypothèses concurrentes que l'on a envisagées (par exemple plusieurs modèles).
  - (b) La barre mesure la dispersion permise à l'intérieur des hypothèses admises.
- Autre gêne : le lien avec la distinction en trois incertitudes qui précède n'est pas dit. On devine que la barre couvre l'aléatoire et l'épistémique, mais pas l'ontologique.
- Reformulation minimale, selon la lecture (a) : « Une barre d'erreur ne reflète jamais que les écarts entre les hypothèses que l'on a admises au départ… ». Selon la lecture (b), il faudrait plutôt : « …que la variation permise par les hypothèses admises au départ… ».
- Sens : il bouge selon la lecture retenue. Je ne tranche pas, l'auteur doit choisir.

**B3.** § ch07 : « …soit d'une confrontation directe avec le monde, là où l'essai coûte peu et peut être défait. »
- Gêne : la portée de « là où » est double.
  - (a) Restriction normative : on ne doit se confronter directement au monde que là où l'essai coûte peu et se défait.
  - (b) Constat : c'est là seulement qu'une telle confrontation est praticable.
- Reformulation : « …soit d'une confrontation directe avec le monde, menée là où l'essai coûte peu et peut être défait. » Cette formulation penche vers (a). Pour (b), on écrirait : « …confrontation qui n'est possible que là où… ».
- Sens : il peut bouger. Je ne tranche pas.

**B4.** § ch08 : « Ce blanchiment rend les résultats impossibles à comparer… »
- Gêne : le terme est introduit directement par un démonstratif, comme s'il avait déjà été défini. La métaphore se devine, mais le mot tombe sans être nommé.
- Reformulation : « Ce phénomène, que le chapitre appelle *blanchiment*, rend les résultats… ».
- Sens : ne bouge pas.

**B5.** § ch06 : « …une autre affirmation, un texte fixé à l'avance ou une observation. »
- Gêne : on ne voit pas ce qu'est « un texte fixé à l'avance » (une spécification ? une norme ? un cahier des charges ?). L'expression ressemble à une périphrase de *specification*.
- Reformulation : « …une spécification fixée à l'avance… », si c'est bien le sens visé.
- Sens : il peut bouger. Si l'auteur visait plus largement une norme ou une réglementation, « spécification » serait trop étroit.

### Gravité C

**C1.** § intro : « Si la représentation a omis l'essentiel… »
- Gêne : l'article défini renvoie à une représentation déjà discutée, sans doute dans la partie 1. C'est une possible dépendance, de même que « représentation finie » plus loin.
- Reformulation : « Si une représentation a omis l'essentiel… ».
- Sens : ne bouge pas.

**C2.** § intro : « chacune des propositions qui y sont énoncées indique son statut et les hypothèses dont elle dépend. »
- Gêne : « statut » reste vague à ce stade. On ne sait pas s'il s'agit de démontrée, conjecturale, empirique, etc. C'est une possible dépendance.
- Reformulation : « …indique son statut (démontrée, conjecturée, empirique…) et les hypothèses… ». Cette proposition ne vaut que si la typologie est bien celle-là.

**C3.** § intro : « Les mécanismes mis au jour ici ne tiennent donc pas aux particularités des machines qui apprennent »
- Gêne : « donc » présente comme une déduction ce qui découle du simple choix des exemples. Le lien est un peu forcé.
- Reformulation : « Les mécanismes mis au jour ici ne tiennent ainsi pas… ». On peut aussi supprimer « donc ».
- Sens : ne bouge pas.

**C4.** § ch06 : « Qu'une seule de ces conditions manque pour une classe d'erreurs, et toutes les erreurs de cette classe franchissent le contrôle, qu'elles soient fréquentes ou rares. »
- Gêne : la notion de « classe d'erreurs » arrive sans définition (possible dépendance).
- Gêne : « qu'elles soient fréquentes ou rares » admet deux lectures. Il peut porter sur les erreurs, c'est-à-dire sur la fréquence de la classe. Il peut aussi signifier « quelle que soit leur fréquence ».
- Sens : l'écart entre les deux lectures est faible. Aucune reformulation n'est nécessaire.

**C5.** § ch06 : « Dans le cas de *Challenger*, plusieurs d'entre elles ont fait défaut en même temps. »
- Gêne : le passage est elliptique. Le lecteur aimerait savoir lesquelles, au moins une. C'est acceptable pour une présentation de chapitre.

**C6.** § ch07 : « …rééchantillonner les mêmes données… »
- Gêne : c'est un terme technique (le *bootstrap*), donc une possible dépendance. Il reste compréhensible au sens courant.

**C7.** § ch09 : « Le chapitre décompose surtout le risque réel… »
- Gêne : « surtout » peut se lire « principalement » ou « avant tout, c'est sa contribution majeure ». Cette lecture est un peu flottante.
- Reformulation : « Surtout, le chapitre décompose le risque réel… ».
- Sens : ne bouge guère.

**C8.** § ch09 : « …et des alertes trop souvent fausses finissent par être négligées. »
- Gêne : ce n'est pas une alerte qui est « souvent fausse », c'est le contrôleur ou le flux d'alertes.
- Reformulation : « …et quand les alertes sont trop souvent fausses, on finit par les négliger. »
- Sens : ne bouge pas.

**C9.** § ch09 : « Un système très exact dont les rares erreurs… »
- Gêne : « exact » appliqué à un système sonne comme un calque de *accurate*.
- Reformulation : « Un système qui se trompe très rarement, mais dont les erreurs échappent aux contrôles… ».
- Sens : ne bouge pas.

## Typographie

Je n'ai rien relevé de manifeste. Les apostrophes et l'italique des noms propres sont cohérents.
