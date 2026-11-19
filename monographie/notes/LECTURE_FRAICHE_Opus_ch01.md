# Lecture fraîche — Chapitre 1 « Boîte à outils : logique, conditionnement, probabilité »

Lecteur : Opus (première lecture, seul le fichier du chapitre a été lu).

## 1. Résumé de ce que j'ai compris (test de lisibilité)

1. Déduction et induction sont deux modes de raisonnement rigoureux, mais chacun ne vaut que « pourvu que » quelque chose : la vérité des prémisses pour la première, la ressemblance des cas nouveaux avec les cas observés pour la seconde.
2. Toute règle portant sur le monde réel tait une partie de ses conditions ; le livre l'écrit $A \cap (\dots) \rightarrow B$, la parenthèse figurant cet arrière-plan ouvert (exemple de l'ébullition de l'eau).
3. Quand on ignore si l'arrière-plan est réuni, on passe aux probabilités : axiomes de Kolmogorov, deux lectures (fréquence, jugement) ; le livre adopte le jugement et le contrôle par les fréquences.
4. La probabilité conditionnelle est une « part de mondes » ; la formule des probabilités totales recompose une probabilité à partir de scénarios ; la règle de Bayes en cotes multiplie la cote de départ par le rapport de vraisemblance (exemple chiffré des soudures et des ultrasons).
5. Le score logarithmique (« surprise », $-\ln p$) note une prévision après coup ; l'écart des surprises de deux prévisions est le logarithme de leur rapport de vraisemblance ; ne jamais donner une probabilité nulle à ce qui peut arriver.

Le fil d'ensemble se suit bien ; les points ci-dessous sont des gênes locales.

## 2. Constats classés par gravité

### Gravité A (compréhension compromise ou contresens possible)

**A1 — § Mesurer la qualité d'une prévision (paragraphe courant et encadré « Score logarithmique et rapport de vraisemblance », point 3)**
- Passages : « ne donner une probabilité nulle qu'à ce qui est réellement impossible » et, dans l'encadré, « la prudence commande de la réserver à ce qui est logiquement impossible ».
- Gêne : les deux critères ne coïncident pas (« réellement » peut s'entendre physiquement impossible, ce qui est plus large que « logiquement impossible ») ; le lecteur ne sait pas quelle règle retenir.
- Reformulation minimale : harmoniser les deux occurrences sur un seul adverbe. Attention : le choix change le sens (règle stricte « logiquement » ou règle plus large « réellement / physiquement ») ; c'est à l'auteur de trancher, je ne tranche pas.

### Gravité B (gêne réelle)

**B1 — § Règles conditionnelles et conditions tues**
- Passage : « ou $A_1 \cap A_2 \rightarrow B$ lorsque plusieurs conditions doivent être réunies ».
- Gêne : le symbole $\cap$ est employé ici sans explication ; il n'est défini (« note la conjonction (« et ») ») que huit lignes plus bas, et le non-spécialiste qui le connaît comme intersection d'ensembles est dérouté.
- Reformulation : « ou $A_1 \cap A_2 \rightarrow B$ (le symbole $\cap$ se lit « et ») lorsque plusieurs conditions doivent être réunies ».

**B2 — § Réviser un jugement : la règle de Bayes sous forme de cotes**
- Passage : « On peut écrire cette règle directement en probabilités, mais le dénominateur $\Pr(E)$ y masque le mécanisme de la révision. »
- Gêne : le lecteur n'a pas encore vu cette écriture (elle n'apparaît que dans l'encadré qui suit) ; « le dénominateur » renvoie à une formule absente.
- Reformulation : « On peut écrire cette règle directement en probabilités (voir l'encadré ci-dessous), mais la probabilité globale de l'observation, $\Pr(E)$, qui y figure au dénominateur, masque le mécanisme de la révision. »

**B3 — § Règle de Bayes**
- Passage : « Autrement dit, la cote *a posteriori* est la cote *a priori* multipliée par le rapport de vraisemblance. »
- Gêne : *a priori* / *a posteriori* ne sont pas définis ; un lecteur cultivé les entend au sens philosophique (indépendant de / issu de l'expérience), pas au sens « avant / après l'observation $E$ ». La notation $\text{cote}(H \mid E)$ n'a pas non plus été introduite.
- Reformulation : « Autrement dit, la cote *a posteriori* (après l'observation, $\text{cote}(H \mid E)$) est la cote *a priori* (avant l'observation) multipliée par le rapport de vraisemblance. »

**B4 — § Règle de Bayes**
- Passage : « si plusieurs observations $E_1, E_2, \dots$ sont indépendantes sous chacune des deux hypothèses ».
- Gêne : cette indépendance « sous chaque hypothèse » n'est pas celle définie dans la section précédente ; elle n'est expliquée qu'à la fin de l'encadré suivant. Le lecteur risque de la confondre avec l'indépendance simple.
- Reformulation : « si plusieurs observations $E_1, E_2, \dots$ sont indépendantes sous chacune des deux hypothèses (on dit *conditionnellement indépendantes* ; voir l'encadré ci-dessous) ».

**B5 — § Règle de Bayes, exemple, légende de la figure**
- Passage : « Le même signal anormal multiplie la cote par 5 dans les deux cas, mais seule la soudure de la zone suspecte franchit la barre d'une chance sur deux. »
- Gêne : la légende vient d'énumérer quatre situations ; « les deux cas » n'a pas de référent clair (il s'agit des deux situations à un seul signal anormal), et la cas des deux signaux, qui franchit aussi la barre, brouille « seule ».
- Reformulation : « Un même signal anormal multiplie la cote par 5 pour les deux soudures, mais, après ce seul signal, seule celle de la zone suspecte franchit la barre d'une chance sur deux. »

**B6 — § Règle de Bayes, exemple, « Lecture »**
- Passage : « multiplier la cote par 5 laisse la soudure du lot courant probablement saine (17,2 %) ».
- Gêne : le pourcentage entre parenthèses, accolé à « saine », se lit comme une probabilité d'être saine, alors que c'est la probabilité de défaut.
- Reformulation : « laisse la soudure du lot courant probablement saine (probabilité de défaut : 17,2 %) ».

**B7 — § Règle de Bayes, exemple, « Lecture »**
- Passage : « Si la seconde sonde réagit à la même irrégularité de forme que la première ».
- Gêne : il n'a jamais été question de deux sondes (seulement de « la sonde » et de « deux signaux anormaux indépendants ») ; le lecteur ne sait pas si le second signal vient d'un second passage de la même sonde ou d'un autre appareil.
- Reformulation : « Si le second examen réagit à la même irrégularité de forme que le premier ». Deux lectures plausibles (même sonde repassée / seconde sonde) ; je ne tranche pas, mais le texte devrait annoncer laquelle en mise en place.

**B8 — § Règle de Bayes, exemple, dernier paragraphe**
- Passage : « L'exemple ne dit pas, en revanche, d'où viennent les chiffres de la sonde. Ils ont été mesurés sur des pièces d'étalonnage »
- Gêne : contradiction apparente : la mise en place a dit d'où viennent les chiffres, et la phrase suivante le redit aussitôt. Le sens visé semble être « l'exemple ne discute pas ce que valent ces chiffres hors de leur cadre de mesure ».
- Reformulation : « L'exemple ne discute pas, en revanche, la portée des chiffres de la sonde. » (Le sens bouge légèrement selon que l'auteur visait la provenance ou la validité ; à vérifier.)

**B9 — § Mesurer la qualité d'une prévision : la surprise**
- Passage : « C'est ce que mesure le **score logarithmique**. La surprise d'une issue, sous une prévision qui lui attribuait la probabilité $p$ … vaut : $S(p) = -\ln p$ »
- Gêne : le terme défini en gras (« score logarithmique ») n'est jamais explicitement identifié à « la surprise », qui est le mot effectivement défini ; en outre, un « score » s'entend spontanément comme « plus il est élevé, mieux c'est », alors qu'ici c'est l'inverse (une pénalité).
- Reformulation : « C'est ce que mesure le **score logarithmique**, que nous appellerons aussi *surprise* : plus il est élevé, plus l'issue a pris la prévision au dépourvu. Pour une issue à laquelle la prévision attribuait la probabilité $p$, il vaut : »

**B10 — § Mesurer la qualité d'une prévision, exemple du verger**
- Passage : « il correspond à un rapport de vraisemblance de 10 en faveur du premier ».
- Gêne : le rapport de vraisemblance a été défini pour deux hypothèses $H$ et $\bar{H}$ ; son application à deux prévisionnistes n'est expliquée qu'après (paragraphe suivant et encadré). Le lecteur ne voit pas d'où sort ce « 10 en faveur du premier ».
- Reformulation : « il correspond à un rapport de vraisemblance de 10 en faveur du premier : si l'on traite chaque prévision comme une hypothèse, le gel était dix fois plus probable selon le premier que selon le second. »

### Gravité C (confort, style)

**C1 — § Déduction et induction** — « ou une prévision pour des cas qui ne l'ont pas encore été » : le « l' » renvoie à « vus », placé loin en amont ; reprise elliptique. → « pour des cas que l'on n'a pas encore observés ».

**C2 — § Déduction et induction** — « Lorsque les définitions, les mesures et les idéalisations de départ décrivent fidèlement la situation » : « idéalisations » arrive sans préparation (on ne parlait que de prémisses) ; le lien prémisses / idéalisations reste implicite. → « Lorsque les prémisses — définitions, mesures, idéalisations de départ — décrivent fidèlement la situation ».

**C3 — § Règles conditionnelles** — « faute d'aspérités où les bulles se forment » → « faute d'aspérités où les bulles puissent se former » (le présent de l'indicatif affirme un fait là où l'on énonce une condition).

**C4 — § Probabilité : règles et lectures, encadré Kolmogorov** — « stable par passage au complémentaire et par réunion dénombrable » : jargon (possible dépendance) acceptable dans un encadré formel, mais opaque pour le lecteur non spécialiste ; une glose d'une demi-ligne suffirait (« on peut prendre le contraire d'un événement, ou réunir une suite d'événements, et l'on obtient encore un événement »).

**C5 — § Probabilité : règles et lectures** — « Deux lectures principales leur en donnent un. » : « leur » (axiomes ou nombres ?) et « en … un » (un sens) font une phrase un peu chargée. → « Deux lectures principales leur donnent un sens. »

**C6 — § Probabilité : règles et lectures** — « Les fréquences ensuite, pour deux raisons. Lorsqu'on dispose … Surtout, … » : l'énumération annoncée n'est pas balisée pour la première raison. → « D'abord, lorsqu'on dispose … Surtout, … ».

**C7 — Encadré « Fréquence ou jugement »** — « La même opération chirurgicale n'affiche pas la même fréquence de succès » : « la même » peut renvoyer à l'opération « prévue demain » de la section précédente ou désigner un type d'opération. → « Une opération chirurgicale donnée n'affiche pas … » (deux lectures possibles ; le sens général ne change pas).

**C8 — § Probabilité conditionnelle** — « De l'@eq:ch01-cond découle la règle du produit … Elle donne aussi une définition précise de l'indépendance » : « Elle » peut être la règle du produit ou l'équation de la probabilité conditionnelle. → « La probabilité conditionnelle donne aussi … » ou « Cette règle donne aussi … » (selon l'intention ; je ne tranche pas).

**C9 — § Probabilité conditionnelle** — « deux situations météorologiques, exclusives l'une de l'autre » (calque de *mutually exclusive*) → « qui s'excluent l'une l'autre » ; et « la probabilité du retard est leur moyenne pondérée » : « leur » est flou → « la moyenne de ces deux probabilités, pondérée par le poids de chaque situation ».

**C10 — § Probabilité conditionnelle** — « Plus généralement, si des hypothèses $H_1, \dots, H_k$ … » : on passe de « situations / scénarios » à « hypothèses » sans le signaler. → « si des hypothèses (ou scénarios) $H_1, \dots, H_k$ … ».

**C11 — § Probabilité conditionnelle** — « Le @sec:ch02 s'appuiera sur cette formule. Les probabilités conditionnelles $\Pr(B \mid H_i)$ y résument … » : « y » = dans la formule ou dans le chapitre 2 ? → « Dans cette formule, les probabilités conditionnelles … résument … » (les deux lectures sont plausibles).

**C12 — § Règle de Bayes, exemple, « Calcul »** — « Pour la zone suspecte, la cote de départ vaut $0{,}25$ : un signal anormal la porte à … (…), un signal normal la ramène à … (…), et deux signaux anormaux … (…). » : phrase très dense, trois cas et trois parenthèses ; couper en trois phrases. Au passage, « vaut $0{,}25$ » gagnerait un rappel (« comme on l'a calculé plus haut pour 20 % »). Par ailleurs « zone suspecte » remplace sans transition « zone qui a subi des contraintes inhabituelles » ; un « (dite ci-après zone suspecte) » dans la mise en place suffirait.

**C13 — § Règle de Bayes, exemple, « Lecture »** — « ce qui revient à la diviser par moins de 5 » : formule vague ; « par 3,4 environ » serait plus parlant (simple explicitation d'un nombre déjà donné).

**C14 — § Mesurer la qualité d'une prévision** — « Sur une série de prévisions indépendantes, enfin, les surprises s'additionnent » : c'est l'indépendance des issues (cf. encadré : « issues … jugées indépendantes ») et non des prévisions. → « Sur une série d'issues jugées indépendantes ». Également « coûte une surprise infinie » : image un peu heurtée (« coûte » + « surprise ») → « entraîne une surprise infinie ».

**C15 — § Mesurer la qualité d'une prévision** — « comparer les estimations de deux navigateurs avant une même course » : renvoi allusif ; « navigateurs » peut s'entendre comme logiciels. → « deux navigateurs (marins) avant une même course au large ».

**C16 — Encadré « Score logarithmique et rapport de vraisemblance », point 3** — « aucune observation ne rendra plus cette éventualité plausible » : « plus » se lit « ne … plus » (plus jamais) ou « plus plausible » (davantage). → « aucune observation ne pourra jamais rendre cette éventualité plausible » (les deux lectures mènent au même constat, mais la première suggère qu'elle l'était auparavant).

## 3. Appréciation globale

Le chapitre est clair, bien charpenté (chaque section ouvre sur sa question, le fil du « pourvu que » est tenu jusqu'aux points clés) et la langue est dans l'ensemble idiomatique. Les sections les plus accessibles sont « Déduction et induction » et « Règles conditionnelles et conditions tues », dont les exemples (poutre, ébullition) portent bien l'idée. La section la moins accessible est celle sur la règle de Bayes, et surtout l'exemple des soudures : vocabulaire introduit après usage (*a priori*, indépendance conditionnelle), légende et « Lecture » aux référents flous, seconde sonde surgie sans annonce. La dernière section se lit bien mais gagnerait à poser d'emblée que « score » et « surprise » sont une même pénalité, et à harmoniser le critère « réellement / logiquement impossible ».
