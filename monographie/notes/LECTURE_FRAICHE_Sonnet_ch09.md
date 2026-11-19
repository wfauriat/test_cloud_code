# Lecture fraîche, chapitre 9 (Sévérité, fausses alertes et probabilité d'échappement)

Lecteur : Sonnet, première lecture, texte seul. Aucun fichier source modifié.

## 1. Ce que j'ai compris (test de lisibilité)

1. Un test fiable peut produire surtout de fausses alertes si ce qu'il cherche est rare (exemple du dépistage : sensibilité 90 %, fausses alertes 5 %, prévalence 1 % donnent une VPP de 15,4 %). Le même mécanisme vaut pour un contrôleur placé derrière un producteur très exact.
2. Un contrôle qui concorde ne prouve quelque chose que s'il aurait donné l'alerte au cas où l'affirmation aurait été fausse (sévérité). Chiffré : l'accord multiplie la cote de justesse par (1−f)/(1−s) ; ce facteur vaut 1 pour un contrôleur sans discernement ou aveugle.
3. Quand le producteur s'améliore et que le contrôleur reste le même, la VPP s'effondre. Chaque vraie erreur attrapée coûte alors 1/VPP examens, et les opérateurs ont tendance à régler leur vigilance sur la VPP (appariement des probabilités), ce qui est un fait de comportement et non un théorème de Bayes.
4. Le risque résiduel est le produit du taux d'erreur du producteur par la probabilité d'échappement, qui vaut 1 − s·u. Les évaluations qui ne notent que le producteur ne voient que le premier facteur. Un producteur dix fois plus exact peut former un système neuf fois plus risqué.
5. Le modèle M1 (c = causes partagées, m = oublis sur les autres causes, f, u) et l'exemple chiffré montrent trois leviers : précision du contrôleur, indépendance, prise en compte. Les causes partagées forment un plancher d'échappement. Le chapitre clôt la partie 2.

Les calculs que j'ai refaits (dépistage, désaccords 11/12, M1, deux configurations de l'exemple, rapport 9 des deux systèmes) sont tous exacts. Les constats portent uniquement sur la formulation, la cohérence interne et les dépendances.

## 2. Constats classés par gravité

### Gravité A

**A1. Section « Risque = taux d'erreur × probabilité d'échappement » (exemple, « Lecture », deuxième levier) et Points clés (dernière puce) : le levier « indépendance » est incohérent entre le texte et l'exemple.**
Passage : « *L'indépendance élargit ce que le contrôleur peut voir.* Garder les causes partagées à 10 % et ramener l'oubli sur les autres erreurs de 20 % à 10 % élève la sensibilité… ». Les Points clés disent : « son indépendance (faible $c$, pour abaisser le plancher d'échappement) ». Dans l'encadré, l'indépendance correspond à c.
Gêne : l'exemple illustre le levier « indépendance » en laissant c constant et en modifiant m (l'oubli), alors que les points clés et l'encadré l'associent à c. Un lecteur ne sait plus quel paramètre est « l'indépendance », ni comment un abaissement de m peut illustrer un levier qui porte sur c. Le plancher change aussi de définition (voir B9).
Reformulation minimale : deux lectures plausibles, que je ne tranche pas.
(a) Si « indépendance » désigne c, renommer le levier de l'exemple (« La qualité propre du contrôleur », avec m) et signaler qu'aucun levier de c n'est illustré ici.
(b) Si « indépendance » englobe c et m, le dire dans l'encadré et, dans les points clés, écrire « son indépendance et sa discrimination (faibles c et m) ».
Le sens change selon le choix.

### Gravité B

**B1. Section « Sévérité d'un contrôle » : « contrôle réussi » / « échec du contrôle ».**
Passage : « un contrôle réussi n'est probant que dans la mesure où il aurait échoué si l'affirmation avait été fausse » ; « si l'échec du contrôle était probable dans l'hypothèse où l'affirmation aurait été fausse ».
Gêne : « réussi » désigne l'accord (l'affirmation passe) et « échoué » désigne l'alerte. Or, pour un lecteur, un contrôle « réussit » aussi quand il détecte une erreur. La définition se lit de façon paradoxale tant que l'on n'a pas reconstitué ce sens à partir de la notation A de la page précédente. Le sens de « échec » est celui de l'événement Ā.
Reformulation : « un accord du contrôleur n'est probant que dans la mesure où le contrôleur aurait signalé une alerte si l'affirmation avait été fausse ». Même sens, sans changement de fond.

**B2. Même section : le lien entre « sévérité » et le multiplicateur est implicite.**
Passage : « L'@eq:ch09-accord-cotes relie directement la sévérité aux grandeurs introduites à la section précédente… L'accord multiplie donc la cote de justesse par $(1 - f)/(1 - s)$ ».
Gêne : la définition de la sévérité est qualitative. Le chapitre ne dit jamais si la sévérité est un nombre, ni lequel : Pr(Ā|E), c'est-à-dire s, le multiplicateur (1−f)/(1−s), ou autre chose. La phrase finale (« sa sévérité est nulle contre un mécanisme… ») traite la sévérité comme une grandeur à valeurs, mais « nulle » correspondrait à s = 0 (multiplicateur égal à 1).
Reformulation : ajouter une phrase du type « La sévérité d'un accord se mesure par $\Pr(\bar{A}\mid E)$, c'est-à-dire $s$ ; le multiplicateur $(1-f)/(1-s)$ en est la traduction en cotes ». Deux lectures plausibles : sévérité = s, ou sévérité = multiplicateur. Le choix est à faire par l'auteur.

**B3. Section « Le piège des fausses alertes » : « Ce renversement crée un piège contre-intuitif ».**
Gêne : le référent de « renversement » est flou. Rien n'est renversé dans le paragraphe précédent (on y a seulement constaté que les désaccords sont surtout de fausses alertes). Le « piège » n'est vraiment énoncé qu'à la phrase suivante.
Reformulation : « Ce constat conduit à un piège contre-intuitif à mesure que la qualité de la production augmente. »

**B4. Même section, dernière phrase : « il ne suffit donc pas qu'il soit indépendant (sensibilité $s$ élevée) ».**
Gêne : l'indépendance est assimilée à une sensibilité élevée. Plus loin, s = (1−c)(1−m) mélange indépendance (c) et discrimination (m). Le lecteur retient une équivalence que la suite contredit à moitié (voir A1).
Reformulation : « il ne suffit pas qu'il soit sensible (s élevée) ». La nuance indépendance / sensibilité est alors laissée à la suite du chapitre. Le sens ne bouge pas.

**B5. Section « Ce que l'on fait des alertes » : phrase sur la prise en compte syntaxiquement bancale.**
Passage : « La prise en compte (@def:prise-en-compte) — que nous noterons $u \in [0,1]$, la proportion des alertes effectivement examinées et suivies d'effet — relève d'une politique d'action… ».
Gêne : « que nous noterons u, la proportion… » accole deux appositions. De plus, « prise en compte » était au ch. 6 une condition de détection, et elle devient ici une proportion sans que le glissement soit signalé.
Reformulation : « La prise en compte (…) est ici mesurée par $u \in [0,1]$, la proportion des alertes effectivement examinées et suivies d'effet ; elle relève d'une politique d'action… ».

**B6. Même section, avant-dernier paragraphe : notations et renvois non expliqués.**
Passage : « éviter une perte $L$ pondérée par VPP » ; « le seuil $p^\ast$ de l'@eq:ch04-seuil s'effondre vers zéro ».
Gêne : L et p* ne sont pas introduits ici. Le lecteur qui n'a pas le ch. 4 sous les yeux ne peut pas suivre la comparaison gain / coût. Dépendance au ch. 4 (utilité espérée subjective, seuil).
Reformulation : ajouter une demi-phrase : « (la décision est utile dès que la probabilité de faute dépasse le seuil $p^\ast$ = coût de l'enquête / perte évitée…) ». Je ne peux pas vérifier la définition exacte de p* ; à ajuster d'après le ch. 4.

**B7. Section « Risque = … » : « on peut chiffrer cette dépendance à l'aide de deux paramètres de fiabilité du contrôleur ».**
Gêne : la dépendance annoncée est celle entre P(E), la VPP, u et l'échappement. Or c et m ne la portent pas : ils ne sont pas des paramètres de cette dépendance, ils définissent s. La dépendance passe par u = VPP, ce qui n'apparaît qu'implicitement dans l'encadré. De plus, c y est présenté comme un « paramètre de fiabilité du contrôleur », alors qu'il mesure ce que le producteur et le contrôleur ont en commun.
Reformulation minimale : « on peut chiffrer l'échappement à l'aide de deux paramètres du contrôleur… ; la dépendance à P(E) passe alors par u (cas u = VPP) ». Le sens risque de bouger si l'auteur veut vraiment dire que c et m chiffrent la dépendance.

**B8. Encadré M1 : « $B_{\text{cmp}} = \emptyset$ dans l'@eq:ch08-croise-angle-mort ».**
Gêne : notation du ch. 8 non expliquée, aucune glose de « comparaison fidèle ».
Reformulation : « en supposant la comparaison fidèle (aucune cause d'erreur propre au comparateur, $B_{\text{cmp}} = \emptyset$ dans l'@eq:ch08-croise-angle-mort) ». À vérifier d'après le ch. 8.

**B9. Encadré M1 puis exemple : le mot « plancher » est employé pour deux grandeurs différentes.**
Passage encadré : « les causes partagées $c$ forment un plancher qu'aucune diligence… », alors que la borne inférieure écrite est 1 − s = c + (1−c)m. Passage exemple : « abaisse le plancher d'échappement… (de 28,0 % à 19,0 %) ».
Gêne : plancher = c dans l'encadré, plancher = 1 − s (28 %, 19 %) dans l'exemple. Le lecteur ne sait plus ce qui est « le plancher ». Lié à A1.
Reformulation : encadré « …bornée inférieurement par $1 - s$ ; dans cette borne, les causes partagées $c$ forment une part incompressible… ». Dans l'exemple, conserver « plancher » pour 1 − s.

**B10. Terminologie flottante : comparateur, contrôleur, relecteur, contrôle.**
Passages : « le comparateur concorde avec l'affirmation » et « le contrôleur ne signale rien » (même section), « le relecteur » (section suivante), « un troisième comparateur » (arbitre).
Gêne : on ne sait pas si « comparateur » (terme du ch. 6) et « contrôleur » désignent la même entité, ni si le « troisième comparateur » est un autre contrôleur. Même chose pour « contrôle » (processus) et « contrôleur » (agent).
Reformulation : unifier (« le contrôleur » partout, « comparateur » seulement en lien explicite avec les cinq conditions) ou poser une équivalence en une phrase. Un simple choix de vocabulaire, sans effet sur le fond.

**B11. Encadré « nuance », deuxième paragraphe : phrase dense, double négation.**
Passage : « le risque $P(E)(1 - s\,u)$ tend vers $P(E)$ par en dessous, sans devenir supérieur au risque sans contrôleur ni croître à lui seul quand $P(E)$ diminue. Le risque total ne peut remonter… que si un autre paramètre change ».
Gêne : trois idées entassées (convergence vers P(E), risque jamais supérieur à P(E), monotonie). « à lui seul » est ambigu (la baisse de P(E) seule ? ce paramètre seul ?). Par contraste avec la section précédente, « faire monter en retour la probabilité d'échappement », le lecteur peut croire que le risque remonte. Il faut distinguer échappement et risque.
Reformulation : couper en deux phrases et rappeler : « Le risque reste inférieur ou égal à P(E) et décroît avec P(E) ; seule la probabilité d'échappement se rapproche de 1. Il ne remonterait que si… ». Le contenu mathématique n'est pas touché ; je n'ai pas vérifié la monotonie au-delà de ce que dit l'auteur.

**B12. Dernier paragraphe : jargon et phrase énumérative.**
Passage : « Des trois incertitudes et de la mesure d'une barre d'erreur jusqu'aux cinq conditions de détection, à l'effet de cause commune du cadre, au compromis entre indépendance et comparabilité, puis à la sévérité… une théorie générale du contrôle des représentations finies, édifiée hors de l'informatique récente. »
Gêne : récapitulation de six idées en une phrase de plus de 60 mots. « Trois incertitudes », « représentations finies » et « édifiée hors de l'informatique récente » sont opaques sans les chapitres antérieurs (dépendances).
Reformulation : scinder en deux phrases, ou en liste brève de quatre éléments ; remplacer « édifiée hors de l'informatique récente » par un énoncé direct (ex. « qui ne suppose aucun outil informatique récent »), si c'est bien le sens visé.

**B13. Points clés, 3e puce : écart avec le corps du texte.**
Passage : « résoudre un désaccord par un tiers est une décision d'utilité espérée qui paie presque toujours devant des enjeux élevés et irréversibles ».
Gêne : le corps dit « décision unique aux enjeux élevés… justifie amplement », avec explicitement un flux répétitif où cela ne vaut plus ; « irréversibles » n'apparaît pas dans le corps ; « presque toujours » généralise.
Reformulation : « …qui paie lorsque les enjeux sont élevés (décision unique, perte très supérieure au coût de la contre-expertise) ».

### Gravité C

**C1. Introduction.** « pourquoi l'amélioration d'un producteur rend fausses la plupart des alertes d'un contrôleur fixe » : le corps conditionne à P(E) « nettement au-dessous de f/s ». L'introduction n'annonce pas non plus la section 1 (taux de base, dépistage), ni son ordre : elle présente la sévérité avant les fausses alertes, alors que la section 1 est un détour médical. Reformulation : « …rend fausses la plupart des alertes d'un contrôleur fixe lorsque les erreurs deviennent rares » ; ajouter « un exemple de dépistage médical introduit d'abord le raisonnement ».

**C2. Fin de la section « Taux de base ».** « les mêmes nombres gouvernent la confiance que mérite un accord comme le crédit que mérite une alerte » : seul le crédit d'une alerte (VPP) a été calculé. La confiance dans l'accord vient à la section suivante. Reformulation : « …gouvernent le crédit que mérite une alerte ; la section suivante traite celui que mérite un accord ».

**C3. Section « Sévérité » : « ou vaut $1$ comme lui » et « est alors égal à $1$ ».** « proche de… ou vaut 1 comme lui » est difficile à lire (qui vaut 1 ?). Puis « proche » devient « égal à 1 ». Reformulation : « est proche de $\Pr(A \mid \bar{E})$ (ou égal à lui, par exemple tous deux égaux à 1) » ; « Le rapport est alors proche de (ou égal à) $1$ ».

**C4. Même section.** « $s = \Pr(\bar{A} \mid E)$ » : Ā n'est jamais défini ; il faut deviner « Ā = alerte ». Reformulation : « notons $\bar{A}$ l'événement complémentaire (le comparateur signale une alerte) ».

**C5. Début de section.** « tant que le contrôleur n'avait pas réellement la possibilité » : temps incohérent. Reformulation : « tant que le contrôleur n'a pas réellement la possibilité ».

**C6. Fin de section « Sévérité ».** « Comme l'indépendance au @sec:ch08 (@prop:independance), la sévérité est toujours relative à une classe d'erreurs » : elliptique (l'indépendance est relative… ?). Reformulation : « Comme l'indépendance (@prop:independance, @sec:ch08), la sévérité est toujours relative… ».

**C7. « contrôleur fixe ».** Terme utilisé dès la section 3 (et l'encadré) sans glose. Reformulation : « un contrôleur dont $s$ et $f$ restent constants (contrôleur fixe) ».

**C8. Début de la section « Ce que l'on fait des alertes ».** « une alerte dont on sait que neuf fois sur dix elle est fausse » : tournure maladroite. Reformulation : « une alerte dont on sait qu'elle est fausse neuf fois sur dix ».

**C9. Notation.** P(E) est employé dès l'@eq:ch09-vpp, alors que l'équivalence Pr(E) = P(E) n'est donnée qu'à la section 5 ; Pr(D) est utilisé dans l'encadré de la section 1. Reformulation : poser l'équivalence à la première apparition de P(E).

**C10. Section 5.** « déjà croisé au @sec:ch00 » : « croisé » est un peu étrange (« rencontré », « vu »). Reformulation : « déjà présenté au @sec:ch00 ».

**C11. Section 5.** « De plus, l'abaissement de $P(E)$ et l'échappement ne sont pas indépendants » : le connecteur introduit une réserve plutôt qu'un ajout. Reformulation : « Par ailleurs » ou « Toutefois ».

**C12. Exemple, « Lecture ».** « Dans chacune des deux colonnes » (le tableau est supposé en colonnes ; le texte parle de configurations) ; « la courbe bleue reste horizontale à 28,0 % » vaut pour le panneau de gauche uniquement. Reformulation : « Dans chacune des deux configurations » ; « sur le panneau de gauche, la courbe bleue… ».

**C13. Section 3.** « Supposons que les deux parties examinent un grand nombre de dossiers » : « parties » connote un litige. Reformulation : « le producteur et le relecteur ».

**C14. Section 5.** Le paragraphe « Dans le prolongement… » et l'encadré M1 donnent deux fois les mêmes définitions de c, m, s, u (redondance de lecture). Reformulation : alléger l'un des deux, au choix de l'auteur.

**C15. Section 5.** « Les batteries d'évaluations comparatives… jeu d'épreuves » : « batteries d'évaluations » est un calque probable de « benchmarks » ; compréhensible. Reformulation : « Les évaluations comparatives (benchmarks)… ».

## 3. Appréciation globale

Sections les plus accessibles : la section 1 (taux de base et VPP). L'exemple des mille personnes, le tableau et les trois puces sont clairs, et l'encadré en cotes se lit bien. La section 3 (désaccords 11/12) est aussi très lisible et s'appuie sur des fractions simples. Les calculs de l'exemple quantitatif sont exacts et faciles à suivre ligne par ligne.

Sections les moins accessibles : la section 2 sur la sévérité, par la définition qui joue sur « réussi / échoué » et par l'absence de quantification explicite de la sévérité (B1, B2, C3, C4). La section 4, pour les notions importées du ch. 4 (L, p*, utilité espérée). Surtout, la fin de la section 5 : le modèle M1 et l'exemple utilisent « indépendance » et « plancher » pour des paramètres différents selon l'endroit (A1, B9), ce qui peut faire croire à un contresens sur ce que mesure c. Le récapitulatif final et l'encadré « nuance » sont denses (B11, B12).

Le chapitre a une bonne ossature (taux de base, sévérité, VPP, comportement, produit). Un lecteur cultivé le suit jusqu'au modèle M1, puis se perd sur l'attribution des trois leviers.
