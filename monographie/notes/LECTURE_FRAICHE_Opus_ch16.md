# Lecture fraîche — chapitre 16 « Angles morts collectifs »

Lecteur : Opus (première lecture, seul le fichier `chapitres/16-angles-morts-collectifs.md` a été lu).

## 1. Ce que j'ai compris (test de lisibilité, 5 lignes)

1. Le risque se décompose en taux d'erreur du producteur × probabilité qu'une erreur échappe aux contrôles. Un modèle partagé fait baisser le premier facteur mais peut faire monter le second, parce que producteur et relecteur partagent alors les mêmes angles morts.
2. Un exemple chiffré (modèle M1) le montre : avec un modèle partagé, un contrôleur plus précis (moins de fausses alertes) ne descend pas sous un plancher d'échappement. Seul un contrôleur qui se trompe autrement fait baisser ce plancher.
3. Un modèle de langage est un « prêteur » unique de savoir. Il corrige les erreurs de l'emprunteur, jamais les siennes, et tout le monde emprunte aujourd'hui aux mêmes prêteurs (comme vingt journalistes qui reprennent la même dépêche).
4. Le blanchiment de provenance fait passer des copies pour des témoins indépendants. L'accord entre ces copies ne prouve presque rien (sévérité nulle), et il contamine aussi les modèles futurs (effondrement de modèle).
5. Produire ne coûte plus presque rien, alors qu'évaluer coûte toujours autant. Les incitations au débit vident pourtant la capacité d'évaluation au moment où on en a le plus besoin. Cela clôt la partie 4 et ouvre la partie 5.

Le fil est clair et le chapitre se lit bien. Les difficultés se concentrent dans l'encadré quantitatif et l'encadré « nuance ».

## 2. Constats classés par gravité

### Gravité A (compréhension compromise ou contresens possible)

**A1 — Encadré « nuance » (et légende de figure, et Lecture, 2e puce) : attribution du plancher de 68 %.**
Passages :
- « il met ainsi à nu un plancher d'échappement de 68,0 %, que fixe la seule corrélation, à 60 %, des causes d'erreur » ;
- légende : « sans pouvoir percer le plancher de 68,0 % imposé par les 60 % de causes partagées » ;
- Lecture : « la précision du contrôleur ne peut rien contre les 60 % de causes partagées ».

Ce qui gêne : selon la formule du chapitre lui-même, $s = (1-c)(1-m)$, le plancher vaut $1 - 0{,}40 \times 0{,}80 = 68\,\%$. Il dépend donc de $c$ et aussi de l'oubli $m = 20\,\%$. Avec $c$ seul, il serait de 60 %. « La seule corrélation » contredit le calcul affiché un peu plus haut. Un lecteur attentif bute sur cet écart, un lecteur rapide retient un chiffre mal attribué.

Reformulation minimale (encadré) : « un plancher d'échappement de 68,0 %, que fixent la part de causes partagées (60 %) et l'oubli résiduel (20 %) sur les autres causes, et qu'aucune baisse des fausses alertes ne peut entamer ». Dans la légende, remplacer « imposé par les 60 % de causes partagées » par « imposé par les causes partagées et l'oubli résiduel ».

Le sens peut bouger selon l'interprétation. Si l'auteur veut dire « ce que la précision ne peut pas réparer », la formule actuelle se défend en substance (ni $c$ ni $m$ ne dépendent de $f$). S'il veut dire « ce qui vient de la corrélation seule », le chiffre est faux. Je ne tranche pas.

**A2 — Encadré quantitatif, Lecture, 3e puce : « Seul un comparateur qui se trompe autrement abaisse le plancher ».**
Passage : « pour le même taux d'erreur de 2 % et le même taux de fausses alertes de 0,5 %, ramener les causes partagées de 60 % à 10 % réduit encore nettement le risque final, aussi bien sous examen complet (de 1,36 % à 0,380 %) que sous appariement (de 1,64 % à 0,756 %) ».

Ce qui gêne : la mise en place du scénario *Indépendant et précis* change deux paramètres. Le contrôleur « redevient indépendant sur la plupart des causes ($c = 10\,\%$) et n'oublie que 10 % des erreurs non partagées » : $m$ passe donc de 20 % à 10 %, ce que confirme $s = 81\,\%$. La puce attribue toute la baisse à $c$. Le lecteur qui vérifie trouve une comparaison confondue, et le lecteur qui ne vérifie pas retient une attribution inexacte des chiffres.

Reformulation minimale : « ramener les causes partagées de 60 % à 10 % (et l'oubli de 20 % à 10 %) réduit encore nettement… ».

### Gravité B (gêne réelle)

**B1 — § « Le taux d'erreur baisse… », 5e paragraphe : $m$ et $u$ utilisés avant d'être présentés.**
- « la sensibilité $s = (1 - c)(1 - m)$ s'effondre » : $m$ n'est nommé (« taux d'oubli ») que dans l'encadré quantitatif, plus loin.
- « une éventuelle baisse de la prise en compte $u$ lorsque les fausses alertes dominent » : $u$ n'est rattaché à sa définition (@def:prise-en-compte) qu'à la toute fin du chapitre (section « étranglement »). Par ailleurs, la raison pour laquelle les fausses alertes « domineraient » (la rareté des erreurs) n'est pas dite à cet endroit.

Reformulation minimale :
- « la sensibilité $s = (1 - c)(1 - m)$, où $m$ est le taux d'oubli du contrôleur sur les causes non partagées, s'effondre » ;
- « une éventuelle baisse de la prise en compte $u$ des alertes (@def:prise-en-compte) lorsque, les erreurs devenant rares, les fausses alertes dominent ».

Il s'agit d'une possible dépendance au chapitre 9.

**B2 — Encadré quantitatif, mise en place : sigle VPP et notations non expliqués.**
Passage : « comparaison fidèle ($B_{\text{cmp}} = \emptyset$) […] l'appariement des probabilités ($u = \mathrm{VPP}$) ».

Ce qui gêne : « VPP » n'est développé (« valeur prédictive positive ») que dans les Points clés, à la fin du chapitre. $B_{\text{cmp}}$ n'est jamais glosé. « Appariement des probabilités » est un calque (*probability matching*) opaque sans le chapitre 9.

Reformulation minimale : « l'appariement des probabilités ($u = \mathrm{VPP}$, valeur prédictive positive : l'opérateur ne donne suite aux alertes qu'au prorata de leur fiabilité) ». Pour $B_{\text{cmp}}$, ajouter « (aucun biais de comparaison) » ou une formule équivalente.

Possible dépendance.

**B3 — Polysémie de « modèle » (§ 1 et encadré).**
Passages : « Dans les paramètres du modèle M1 […] » ; « On reprend […] le modèle M1 » au voisinage de « Un modèle pour tous », « Modèle partagé, contrôleur précis ».

Ce qui gêne : « modèle » désigne tour à tour l'outil de langage partagé et le schéma probabiliste M1 du contrôleur. Dans l'encadré, les deux sens se côtoient dans la même phrase. Un lecteur peut croire que « M1 » est le modèle de langage partagé.

Reformulation minimale : à la première occurrence, écrire « le modèle probabiliste du contrôleur (M1) du @sec:ch09 ».

**B4 — Encadré quantitatif, mise en place, 3e puce : « dix fois plus précis ».**
Passage : « le contrôleur devient dix fois plus précis en abaissant son taux de fausses alertes de 5 % à 0,5 % ».

Ce qui gêne : la VPP, qui mesure la précision au sens usuel, passe de 11,6 % à 56,6 %, soit environ cinq fois plus. « Dix fois plus précis » entre donc en conflit avec les chiffres donnés juste après.

Reformulation minimale : « le contrôleur émet dix fois moins de fausses alertes (de 5 % à 0,5 %) ».

**B5 — Encadré quantitatif, dernier paragraphe : lien logique elliptique.**
Passage : « Le risque ne pouvant jamais dépasser $P(\text{faux})$, c'est l'ampleur de cette baisse, face à la hausse de l'échappement, qui décide du sens de la variation ».

Ce qui gêne : le lecteur ne voit pas en quoi la borne « risque ≤ P(faux) » entraîne la conclusion. Le maillon manquant est que la chute de 10 % à 2 % suffit à elle seule à garantir un risque inférieur aux 5,57 % initiaux.

Reformulation minimale : « Comme le risque ne peut jamais dépasser $P(\text{faux})$, la chute de 10 % à 2 % garantit ici à elle seule un risque inférieur aux 5,57 % initiaux. C'est donc l'ampleur de cette baisse, face à la hausse de l'échappement, qui décide du sens de la variation : … ».

**B6 — Phrase d'annonce de l'encadré « nuance » et sa 1re phrase.**
Passages : « afin d'éviter une confusion fréquente sur l'effet de la seule règle de Bayes » ; « Lorsque les erreurs d'un producteur deviennent rares, deux mécanismes distincts dégradent le contrôle » ; « La règle de Bayes fixe la VPP, non la décision d'examiner une alerte. »

Ce qui gêne :
- La « confusion fréquente » n'est jamais énoncée.
- La phrase d'ouverture laisse croire que les deux mécanismes naissent de la rareté des erreurs, alors que le second (la corrélation) vient du partage du modèle, comme le paragraphe suivant le dit.
- La phrase sur Bayes tombe sans lien avec ce qui précède.

Reformulations minimales :
- annonce : « afin d'éviter de croire que la seule règle de Bayes (la chute de la VPP) suffit à faire monter le risque » ;
- ouverture : « Lorsqu'un producteur devient plus fiable grâce à un modèle partagé, deux mécanismes distincts… » ;
- phrase sur Bayes : « Encore faut-il distinguer : la règle de Bayes fixe la VPP, non la décision d'examiner une alerte. »

Le sens peut bouger : si l'auteur visait précisément la seule rareté, l'ouverture actuelle est voulue pour le premier mécanisme. Il faudrait alors simplement ne pas y rattacher le second.

**B7 — § « Blanchiment de provenance… », 1er et 2e paragraphes : définition en gras d'une notion présentée comme déjà connue.**
Passages : « deux proches cousins lui ont été reconnus : […] l'effacement de la provenance » puis « On appelle **blanchiment de provenance** la perte de l'origine d'une information, si bien que des copies d'une même source passent pour des témoignages indépendants. »

Ce qui gêne : le premier paragraphe dit que la notion a été établie au chapitre 8 et retrouvée au chapitre 14, puis le gras la définit comme nouvelle. Le lecteur ne sait pas s'il s'agit de la même notion ou d'une extension collective. De plus, la définition inclut sa conséquence (« si bien que… »).

Reformulation minimale : « On appellera **blanchiment de provenance** cette forme collective de l'effacement de la provenance : la perte de l'origine d'une information, qui fait passer des copies d'une même source pour des témoignages indépendants. »

**B8 — § « Blanchiment de provenance… », paragraphe sur la sévérité : notation $E$ et $A$.**
Passage : « dès lors que la première copie reproduit une erreur $E$ du modèle source, les neuf autres copies […] ont une probabilité $\Pr(A \mid E)$ voisine de $1$ ».

Ce qui gêne : plus haut, $E$ est l'événement générique « l'affirmation est fausse » (le taux d'erreur s'écrit $P(E)$). Ici, il devient « une erreur » particulière. $A$ n'est pas défini. Le lecteur sans le chapitre 9 ne lit pas la formule.

Reformulation minimale : « dès lors que l'affirmation est fausse ($E$) parce que le modèle source se trompe, les neuf autres copies […] ont une probabilité $\Pr(A \mid E)$ de concorder (événement $A$) voisine de 1 ».

Possible dépendance : @eq:ch09-accord-cotes, sévérité.

**B9 — § « Un même prêteur… », 1er paragraphe : jargon du chapitre 7.**
Passage : « les deux voies par lesquelles une pertinence nouvelle peut entrer dans un cadre ».

Ce qui gêne : « pertinence nouvelle » et « cadre » au sens technique ne sont pas compréhensibles sans le chapitre 7. La suite (« découvrir par l'épreuve », « être averti ») éclaire en partie.

Reformulation minimale : « les deux voies par lesquelles un facteur jusque-là ignoré peut entrer dans notre représentation (notre « cadre ») ».

Possible dépendance. Le sens peut bouger si « pertinence » a une acception technique précise.

**B10 — § « Un même prêteur… », 2e paragraphe : syntaxe.**
Passage : « industrialise la voie qui consiste à *être averti* en un réservoir unique ».

Ce qui gêne : « industrialiser X en un réservoir » ne se construit pas. On comprend après coup « en la concentrant dans un réservoir unique ».

Reformulation minimale : « industrialise la voie qui consiste à *être averti* en la concentrant dans un réservoir unique ».

**B11 — § 1, 4e paragraphe : jargon non glosé.**
Passages : « une omission de saillance déclenchée par une formulation standard », « un biais induit par l'orientation sur préférences humaines », « la même lignée de corpus et d'alignement ».

Ce qui gêne : ce sont trois notions techniques en une phrase, sans glose. « Orientation sur préférences humaines » est de plus un calque peu idiomatique, et le § 2 dit autrement « ajustement par préférences » : deux noms pour une même chose.

Reformulation minimale : unifier sur « ajustement par préférences humaines » aux deux endroits. Pour « omission de saillance », c'est une possible dépendance (renvoi utile).

**B12 — § « L'étranglement… », 3e paragraphe : « équilibre mélangeant ».**
Passage : « deviennent indiscernables au premier coup d'œil dans un équilibre mélangeant ».

Ce qui gêne : il s'agit d'un terme de théorie des jeux (*pooling equilibrium*), opaque pour un lecteur cultivé non spécialiste.

Reformulation minimale : « deviennent indiscernables au premier coup d'œil, si bien que l'apparence ne permet plus de les trier (ce que la théorie des jeux appelle un équilibre mélangeant) ».

Possible dépendance.

**B13 — § « L'étranglement… », 4e paragraphe : phrase longue et « ce qui » flou.**
Passage : « Les évaluateurs restants, submergés par le flux, n'ont plus le temps de remonter […] ni d'enquêter sur des alertes dont la VPP baisse — ce qui referme sur eux le piège de l'appariement des probabilités et les ramène à une vigilance purement formelle, tandis que la prise en compte (@def:prise-en-compte) cède sous la pression des délais. »

Ce qui gêne : « ce qui » peut renvoyer au manque de temps ou à la baisse de VPP. La phrase enchaîne aussi trois propositions.

Reformulation minimale : couper après « dont la VPP baisse. » puis écrire : « Ce manque de temps referme sur eux le piège de l'appariement des probabilités : leur vigilance devient purement formelle et la prise en compte des alertes (@def:prise-en-compte) cède sous la pression des délais. »

Le sens peut bouger si l'auteur visait la baisse de VPP comme cause. Les deux lectures sont plausibles et je ne tranche pas.

**B14 — § « L'étranglement… », avant-dernier paragraphe : « Elle les *enchaîne* ».**
Passage : « Ce constat referme l'enquête de la @sec:partie-4 sur ce que l'automatisation fait à nos contrôles. Elle les *enchaîne* d'abord… ».

Ce qui gêne : grammaticalement, « Elle » renvoie d'abord à « l'enquête » (ou à la partie), alors que le sens est « l'automatisation ».

Reformulation minimale : « L'automatisation les *enchaîne* d'abord… ».

**B15 — Vocabulaire du contrôle (ensemble du chapitre).**
Passages : « comparateur » (§ 1, 3e paragraphe ; § 2), « contrôleur » (encadré), « relecteur » (§ 1), « filtre » (« évaluer directement le filtre », § 1, 6e paragraphe).

Ce qui gêne : sans le chapitre 8, le lecteur ne sait pas si « comparateur » et « contrôleur » sont synonymes ou distincts. Au § 1, le modèle est d'abord comparateur du producteur, puis source d'angles morts communs au producteur et au contrôleur. « Filtre » ajoute un quatrième nom.

Reformulation minimale : remplacer « évaluer directement le filtre » par « évaluer directement le contrôle ». Le rapport entre comparateur et contrôleur relève d'une possible dépendance (un renvoi d'une demi-phrase suffirait).

### Gravité C (confort, style)

**C1 — Introduction : « prêteur » employé avant l'image.**
Passage : « qu'un comparateur emprunté ne contrôle jamais son prêteur ». L'image n'est introduite qu'au § 2.
Reformulation minimale : « qu'un comparateur emprunté à un modèle ne contrôle jamais les erreurs de ce modèle ».

**C2 — Notation $P(E)$, $\Pr(\bar{C} \mid E)$ et $P(\text{faux})$.**
Passage (§ 1) : « du taux d'erreur $P(E)$ (noté $P(\text{faux})$ dans les tableaux et les figures) ». Le chapitre emploie à la fois $P$ et $\Pr$, et alterne $P(E)$ et $P(\text{faux})$ jusque dans le texte courant (encadré « nuance » : $P(E)$ ; encadré quantitatif : $P(\text{faux})$). La mise en garde est faite, mais l'alternance reste dans la prose.
Pas de reformulation imposée : s'en tenir à $P(\text{faux})$ dans les encadrés et à $P(E)$ dans le corps, ou l'inverse.

**C3 — Encadré quantitatif : $c$ noté tantôt en décimal, tantôt en pourcentage.**
Passages : « $c = 0{,}10$ » et « $c = 10\,\%$ ».
Reformulation minimale : unifier, par exemple sur « $c = 0{,}10$ ».

**C4 — Encadré quantitatif, Calcul : comment l'échappement sous appariement est obtenu.**
Passage : « l'échappement s'établit à 55,7 % sous appariement des probabilités ». La formule ($1 - \mathrm{VPP} \times s$) n'est pas rappelée, alors que la VPP l'est au paragraphe suivant. De même, « 1,6 alerte par vraie erreur attrapée » est $1/\mathrm{VPP}$, sans que ce soit dit.
Reformulation minimale : « l'échappement s'établit à $1 - 0{,}615 \times 0{,}72 = 55{,}7\,\%$ ».

**C5 — § 1, 3e paragraphe : « le même modèle appris ».**
Passage : « le même modèle appris ». C'est un calque de *learned model*.
Reformulation minimale : « le même modèle de langage ».

**C6 — § « Un même prêteur… », 3e paragraphe : pronoms « il ».**
Passage : « il intercepte les fautes propres à l'emprunteur — […] une piste classique de la littérature qu'il ignorait ». Le premier « il » renvoie à l'emprunt, le second à l'emprunteur.
Reformulation minimale : « que celui-ci ignorait ».

**C7 — § « Un même prêteur… », scène journalistique.**
- « Une scène familière […] : imaginons » : la scène est donnée pour familière puis pour imaginée.
- « le même bilan » : le mot arrive sans antécédent, puisqu'on parlait de « chiffres et citations ».

Reformulation minimale : « Une scène, transposée du journalisme, résume… » ; « lui ont confirmé les mêmes chiffres ».

**C8 — § « Blanchiment de provenance… », 2e paragraphe : accord.**
Passage : « des quantités massives de synthèses, d'articles explicatifs, de bouts de code […] produits […] sans aucune mention de la façon dont elles ont été obtenues ». « Produits » est au masculin, « elles » au féminin.
Reformulation minimale : « dont ils ont été obtenus ».

**C9 — § « Blanchiment de provenance… », illusion de corroboration.**
Passage : « Un ingénieur, un médecin, un chercheur ou un moteur de recherche documentaire […] il interprète cette convergence ». Un moteur de recherche n'« interprète » pas au sens humain.
Reformulation minimale : retirer « ou un moteur de recherche documentaire », ou écrire « (ou s'en remet à un moteur de recherche documentaire) ».

**C10 — § « Blanchiment de provenance… », boucle des modèles.**
Passage : « ferme la boucle sur les générations suivantes ». C'est un léger calque (*closes the loop*).
Reformulation minimale : « se répercute sur les générations suivantes ».

**C11 — § « L'étranglement… », 3e paragraphe.**
Passages : « produire des réponses […] coûte presque zéro » ; « les directions et les arbitrages budgétaires sont fortement incités ». Des arbitrages ne sont pas « incités ».
Reformulations minimales : « ne coûte presque rien » ; « les directions sont fortement incitées, dans leurs arbitrages budgétaires, à réallouer… ».

**C12 — Dernier paragraphe : récapitulatif et transition.**
- « agir d'après un cadre fini (partie-1), ce qui peut nous détromper à temps (partie-2), la spécification passée dans les données (partie-3) » : l'énumération est hétérogène (un infinitif, une relative, un groupe nominal).
- « Aucune couche d'outils ne peut garantir, de l'intérieur, qu'elle n'a rien omis » : la phrase arrive sans lien.
- « trancher une décision unique » : la collocation est impropre.

Reformulation minimale : « comment prendre une décision unique à fort enjeu » ; ajouter « Une leçon s'en dégage : aucune couche d'outils… ».

**C13 — Points clés, 3e puce : « l'écoute des alertes ».**
Passage : « restaure la valeur prédictive positive et l'écoute des alertes ». Le corps dit « prise en compte » ($u$), alors qu'ici apparaît un troisième nom.
Reformulation minimale : « et la prise en compte des alertes ».

## 3. Appréciation globale

**Sections les plus accessibles.**
- La section « Un même prêteur pour tous les emprunteurs » : l'image du prêteur et la scène des vingt journalistes portent l'argument sans formule.
- La section « L'étranglement institutionnel de l'évaluation » : la thèse (la production ne coûte plus presque rien, l'évaluation coûte toujours autant) est limpide, hors le jargon « équilibre mélangeant ».

**Sections les moins accessibles.**
- L'encadré quantitatif et l'encadré « nuance ». Les calculs sont justes et vérifiables. Mais les notations ($m$, $u$, VPP, $B_{\text{cmp}}$) arrivent avant d'être expliquées, ou ne le sont jamais.
- Le plancher de 68 % est attribué à la seule corrélation alors qu'il intègre l'oubli $m$ (A1).
- Le dernier scénario change deux paramètres, mais la conclusion n'en cite qu'un (A2).
- La section sur le blanchiment de provenance est fluide. Le statut de la définition en gras (nouvelle ou reprise) reste ambigu, et la notation de sévérité $\Pr(A \mid E)$ suppose le chapitre 9.
