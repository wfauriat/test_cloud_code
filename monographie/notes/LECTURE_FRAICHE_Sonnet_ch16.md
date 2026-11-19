# Lecture fraîche, chapitre 16 « Angles morts collectifs » (Sonnet)

Lecture du seul fichier `16-angles-morts-collectifs.md`, sans autre source. Aucune modification du texte source.

## 1. Ce que j'ai compris (test de lisibilité)

1. Quand toute une communauté s'appuie sur le même modèle, chacun fait moins de fautes personnelles (le taux d'erreur baisse), mais les erreurs propres au modèle deviennent communes au producteur et au relecteur, si bien que le contrôle croisé perd sa valeur et que la probabilité qu'une erreur passe tous les contrôles augmente.
2. Un exemple chiffré à quatre configurations montre que rendre le contrôleur plus précis répare le problème des fausses alertes, mais pas le plancher d'échappement fixé par les causes d'erreur partagées. Seul un comparateur réellement différent abaisse ce plancher. Le risque total peut tout de même baisser si la chute du taux d'erreur est assez forte.
3. Le modèle est un « prêteur » unique : il aide contre les erreurs de l'emprunteur, jamais contre les siennes. L'anecdote des vingt journalistes qui s'appuient sur la même dépêche illustre l'accord apparent entre sources.
4. Le « blanchiment de provenance » (les textes produits avec un modèle sont publiés sans mention d'origine) crée une illusion de corroboration. Il alimente aussi l'effondrement des modèles futurs entraînés sur ces textes et appauvrit les biens communs épistémiques.
5. Enfin, la production devient presque gratuite alors que l'évaluation coûte toujours autant. Les incitations favorisent le débit, donc la capacité d'évaluation stagne au moment où le volume à contrôler explose. Cela clôt la partie 4 et annonce la partie 5.

Le chapitre se lit globalement bien. Les difficultés se concentrent dans l'exemple quantitatif (notations non définies, une attribution causale incomplète) et dans quelques passages de jargon ou de syntaxe lourde.

## 2. Constats classés par gravité

### Gravité A

**A1. Section 1, encadré « Lecture », 3e puce, et paragraphe de calcul précédent.**
Passage : « ramener les causes partagées de 60 % à 10 % réduit encore nettement le risque final, aussi bien sous examen complet (de 1,36 % à 0,380 %) que sous appariement (de 1,64 % à 0,756 %) », avec « pour le même taux d'erreur de 2 % et le même taux de fausses alertes de 0,5 % ».
Gêne : la liste « mêmes » omet que le taux d'oubli m passe aussi de 20 % à 10 % dans le scénario *Indépendant et précis*. Le lecteur qui recalcule avec c = 0,10 et m = 0,20 (sensibilité 0,72) ne retrouve pas les chiffres, et l'effet est attribué à la seule corrélation. Le m = 10 % n'apparaît qu'entre parenthèses dans le paragraphe de calcul.
Reformulation minimale : « pour le même taux d'erreur de 2 % et le même taux de fausses alertes de 0,5 %, ramener les causes partagées de 60 % à 10 % (et l'oubli de 20 % à 10 %) réduit encore nettement… ».
Le sens ne bouge pas, mais la puce 3 dit ensuite que le « plancher » dépend de la corrélation. Si l'auteur veut isoler la corrélation, il faut changer le scénario ou nuancer le texte. Je ne tranche pas.

**A2. Section 1, dernier paragraphe de l'exemple, contre l'encadré « Séparer la corrélation… ».**
Passage 1 : « à corrélation égale, une baisse plus modeste du taux d'erreur suffirait à faire monter le risque total ».
Passage 2 (encadré) : « Pour qu'une amélioration du producteur s'accompagne d'une hausse du risque total, il faut qu'un autre paramètre bouge en même temps, au premier chef la part des causes partagées c ».
Gêne : deux lectures plausibles de « à corrélation égale ».
- (a) Même c = 0,60 que dans l'exemple : le passage 1 est alors cohérent avec l'encadré, car c a déjà bougé par rapport au scénario de départ.
- (b) Même c que dans la situation de départ : le passage 1 contredit l'encadré. Avec c et m, f fixes et P(E) qui baisse, l'encadré affirme que le risque ne peut pas monter.
« Faire monter » n'indique pas non plus par rapport à quoi (le scénario entre pairs ?).
Reformulation : « au même niveau de corrélation (c = 0,60), une baisse moins forte du taux d'erreur que celle supposée (de 10 % à plus de 5,8 %, par exemple) suffirait à faire monter le risque par rapport au contrôle entre pairs ». Cela fixe la lecture (a). Je ne tranche pas si l'auteur visait (b).

### Gravité B

**B1. Section 1 (§ 2, 4e et 5e paragraphes, avant l'exemple). Notations non définies à leur premier emploi.**
Passages : « la fraction $c$ … la sensibilité $s = (1 - c)(1 - m)$ », « prise en compte $u$ lorsque les fausses alertes dominent », « modèle M1 », « $\Pr(\bar{C} \mid E)$ ».
Gêne : m, u, M1 et la VPP (jamais développée avant les Points clés) sont utilisés avant toute explication. Le lecteur ne peut pas lire l'équation de la sensibilité, car m manque. C'est une possible dépendance du chapitre 9, mais le texte fait d'abord du contenu avec ces symboles.
Reformulation minimale : une demi-phrase à la première occurrence, par exemple « …(la part $m$ des autres erreurs que le contrôleur oublie) », « (valeur prédictive positive, VPP : part des alertes qui signalent une vraie erreur) », « la probabilité $u$ que l'on donne suite à une alerte ». Le sens ne bouge pas.

**B2. Section 1, début de l'exemple. Jargon technique non introduit.**
Passage : « comparaison fidèle ($B_{\text{cmp}} = \emptyset$), taux d'erreur stationnaire … appariement des probabilités ($u = \mathrm{VPP}$) … résolution exacte des alertes examinées, comparabilité intacte ».
Gêne : plusieurs termes techniques (comparaison fidèle, stationnaire, comparabilité, appariement des probabilités) apparaissent en une seule phrase sans explication. La définition de l'appariement n'arrive que dans l'encadré, via la citation de Bliss. Le paragraphe « Mise en place » est une seule phrase très longue (plus de 80 mots).
Reformulation : couper en deux phrases et glisser une glose, par exemple « l'appariement des probabilités (on examine une alerte avec une probabilité égale à la VPP) ». Le sens ne bouge pas.

**B3. Section 1, exemple, puce « Contrôle entre pairs ».**
Passage : « déclenche 5 % de fausses alertes ($f = 0{,}05$) ».
Gêne : deux lectures possibles. Soit 5 % des affirmations correctes déclenchent une alerte (c'est ce qu'utilise le calcul : 0,98 × 0,05), soit 5 % des alertes sont fausses. La seconde est contredite par la VPP de 61,5 %, mais le lecteur ne le sait qu'après coup.
Reformulation : « déclenche une fausse alerte sur 5 % des affirmations correctes ». Cela fixe la première lecture, qui est la seule compatible avec les chiffres.

**B4. Section 1, paragraphes « Calcul ». Le calcul de l'échappement n'est jamais montré.**
Passage : « Sous appariement des probabilités, la probabilité d'échappement grimpe à 96,3 % ».
Gêne : seul le calcul de la VPP est détaillé. Le passage de VPP et s à l'échappement (ici 1 − VPP × s) n'est pas écrit, et la correspondance « 11,6 % (8,7 alertes à examiner par vraie erreur attrapée) » (inverse de la VPP) n'est pas expliquée. Le lecteur doit renvoyer à des équations de la partie 3 qu'il n'a pas sous les yeux.
Reformulation : une ligne d'appui, par exemple « (échappement = 1 − VPP × s, soit 1 − 0,116 × 0,32 ; le nombre d'alertes par vraie erreur est l'inverse de la VPP) ». Aucun changement de contenu mathématique.

**B5. Section 1, « Lecture », puce 1.**
Passage : « Avec un risque de 1,93 % contre 2 % sans contrôleur, le contrôle croisé n'arrête presque plus rien. »
Gêne : cela n'est vrai que sous appariement. Sous examen complet (que la même puce vient d'évoquer), le contrôleur arrête encore 32 % des erreurs (risque de 1,36 %). La phrase suivie de « reste à 68,0 % même sous examen complet » laisse croire que le constat est général.
Reformulation : « Sous appariement, avec un risque de 1,93 % contre 2 % sans contrôleur, le contrôle croisé n'arrête presque plus rien. »

**B6. Section 1, dernier paragraphe de l'exemple.**
Passage : « Le risque ne pouvant jamais dépasser $P(\text{faux})$, c'est l'ampleur de cette baisse, face à la hausse de l'échappement, qui décide du sens de la variation ».
Gêne : le lien causal (« ne pouvant jamais dépasser… donc c'est l'ampleur… qui décide ») est implicite. Le plafond P(faux) n'explique pas à lui seul pourquoi la comparaison tourne sur l'ampleur de la baisse.
Reformulation : « Le risque est le produit de P(faux) par l'échappement : c'est donc l'ampleur de la baisse de P(faux), face à la hausse de l'échappement, qui décide du sens de la variation. » Le sens est conservé si l'auteur voulait seulement rappeler la décomposition.

**B7. Section 2, 2e paragraphe.**
Passage : « un grand modèle de langage entraîné sur l'immense archive écrite industrialise la voie qui consiste à *être averti* en un réservoir unique ».
Gêne : syntaxe lourde, calque probable (« industrialise … en un réservoir »). « En » ne se rattache à aucun verbe attendu (transformer en ?). « L'immense archive écrite » est aussi allusive.
Reformulation : « …industrialise la voie qui consiste à *être averti* : il la concentre en un réservoir unique, un seul jeu de paramètres qui condense ce que… ». Le sens est maintenu.

**B8. Section 2, début du 4e paragraphe (« Mais un comparateur emprunté a une limite de principe »).**
Passage : « Ce que les données d'entraînement laissent dans l'ombre, ce que la calibration générative a fixé sous la forme d'une erreur constante ou d'une idée reçue fréquente (…), ce que la consigne ou l'ajustement par préférences pousse à taire (…) appartient tout entier à l'angle mort du prêteur lui-même. »
Gêne : trois sujets longs séparés du verbe, et jargon opaque pour un lecteur cultivé non spécialiste (« calibration générative », « erreur constante », « ajustement par préférences »). Possible dépendance aux chapitres 11 et 12.
Reformulation : scinder en trois propositions (« Ce que les données … laissent dans l'ombre, ce que … a fixé…, ce que … pousse à taire : tout cela appartient… ») et expliciter « erreur constante » (une erreur que le modèle répète à l'identique ?). Je ne tranche pas sur le sens exact de « erreur constante » ni de « calibration générative ».

**B9. Section 2, 5e paragraphe.**
Passage : « la règle du @sec:ch15 — arrêter d'abord leur propre jugement avant de consulter l'outil ».
Gêne : « arrêter son jugement » (au sens de le fixer) est vieilli et ambigu. Un lecteur peut comprendre « cesser de juger » et inverser le sens. L'introduction du chapitre dit « se forge un avis », ce qui est plus clair.
Reformulation : « formuler d'abord leur propre jugement avant de consulter l'outil ». Cela aligne le texte sur l'introduction.

**B10. Section 3, début.**
Passage : « À la @sec:ch08-blanchiment (@def:blanchiment), le blanchiment a été défini comme la perte des conditions d'un résultat lorsqu'il change de mains, et deux proches cousins lui ont été reconnus : l'effacement des unités et des définitions, et l'effacement de la provenance, que la @sec:ch14-blanchiment a retrouvés entre les étapes d'un *pipeline*. »
Gêne : (a) « lorsqu'il change de mains » : « il » peut être le résultat ou le blanchiment, vraisemblablement le résultat ; (b) « deux proches cousins » (cousins de quoi : le blanchiment ?) ; (c) « que … a retrouvés » : « que » renvoie-t-il au second cousin ou aux deux ? ; (d) la définition en gras qui suit (« blanchiment de provenance ») redéfinit le terme alors que la phrase d'avant vient de le définir au chapitre 8 : on ne sait pas si c'est le cousin ou le concept général. La dernière phrase « le second prend une ampleur nouvelle » est alors floue.
Reformulation : « …la perte des conditions d'un résultat lorsque celui-ci change de mains. Deux variantes en ont été distinguées : l'effacement des unités et des définitions, et l'effacement de la provenance, que la … a retrouvé entre les étapes d'un *pipeline*. » Si l'auteur considère la variante « provenance » comme le blanchiment de provenance, le sens est préservé.

**B11. Section 3, définition en gras.**
Passage : « On appelle **blanchiment de provenance** la perte de l'origine d'une information, si bien que des copies d'une même source passent pour des témoignages indépendants. »
Gêne : « si bien que » mélange définition et conséquence. La phrase laisse croire que toute perte d'origine produit cet effet. Le lien avec le contenu généré par les modèles (la phrase d'avant) est implicite.
Reformulation : « …la perte de l'origine d'une information ; des copies d'une même source peuvent alors passer pour des témoignages indépendants. » Le sens de la définition n'est pas modifié.

**B12. Section 3, « Du côté des lecteurs humains… ».**
Passage : « Un ingénieur, un médecin, un chercheur ou un moteur de recherche documentaire interroge la littérature … et trouve … il interprète cette convergence ».
Gêne : sujet multiple (dont un moteur de recherche) repris par un « il » unique : un moteur de recherche n'« interprète » pas.
Reformulation : retirer le moteur de recherche du sujet (« …ou, via un moteur de recherche documentaire, trouve dix pages… ») ou écrire « elle/il » : « Un ingénieur, un médecin ou un chercheur interroge, éventuellement via un moteur de recherche documentaire, la littérature… ».

**B13. Section 3, « La notion de sévérité… ».**
Passage : « Dans l'@eq:ch09-accord-cotes, dès lors que la première copie reproduit une erreur $E$ …, les neuf autres copies … ont une probabilité $\Pr(A \mid E)$ voisine de $1$ de concorder avec elle ».
Gêne : A (l'événement d'accord) n'est pas défini ; « sévérité » n'est pas rappelée (« tranche aussitôt ce que vaut un tel accord » reste abstrait). Le lecteur sans le chapitre 9 comprend l'idée mais pas la notation. Le terme « sévérité » est un possible renvoi au chapitre 9. Le mélange P(E) / Pr(…) est aussi inhabituel.
Reformulation : « …une probabilité $\Pr(A \mid E)$ voisine de 1 (A : les copies concordent) ». Pas de changement de contenu.

**B14. Section 3, fin (« Ainsi se dégradent les biens communs épistémiques »).**
Gêne : « Ainsi » annonce une conséquence du paragraphe précédent (effondrement des modèles), alors que le paragraphe traite des biens communs destinés aussi aux humains ; saut d'objet non annoncé. L'expression « biens communs épistémiques » arrive sans définition préalable et n'est pas mise en gras.
Reformulation : « Plus largement, se dégradent les biens communs épistémiques — … ». Le sens est maintenu.

**B15. Section 4, début.**
Passage : « une dynamique proprement organisationnelle qui explique pourquoi nos institutions tendent à aggraver le déséquilibre au lieu de le corriger ».
Gêne : « le déséquilibre » n'a pas de référent précis à cet endroit (entre production et évaluation ? entre erreurs et contrôles ?), car la notion n'est posée qu'au paragraphe suivant.
Reformulation : « …tendent à aggraver ce déséquilibre entre production et évaluation, que nous décrivons ci-dessous ». Je ne tranche pas sur le sens exact visé.

**B16. Section 4, 3e paragraphe.**
Passage : « De plus, comme l'a montré la @sec:ch15-effondrement-signal, lorsque la tenue extérieure cesse d'être un signal coûteux, le travail contrôlé et le brouillon lisse deviennent indiscernables au premier coup d'œil dans un équilibre mélangeant. »
Gêne : « signal coûteux » et « équilibre mélangeant » (calque de l'anglais *pooling equilibrium*) sont du jargon d'économie des signaux, non expliqué ici. Le lien avec ce qui suit (incitations des directions) est implicite. La phrase finale du paragraphe (plus de 70 mots) est dense.
Reformulation : remplacer « dans un équilibre mélangeant » par « (les deux produits se confondent) » ou gloser en une proposition ; couper avant « Face à des équipes… ». Le sens reste inchangé.

**B17. Section 4, avant-dernier paragraphe.**
Passage : « enquêter sur des alertes dont la VPP baisse ».
Gêne : le chapitre n'a expliqué la baisse de la VPP que par la raréfaction des erreurs du producteur (section 1). Ici, la raison de la baisse n'est pas donnée : le volume augmente, rien n'indique que le taux d'erreur diminue. Le lecteur peut croire à une incohérence.
Reformulation : « dont la VPP baisse (les erreurs étant devenues plus rares) » ou « dont les alertes deviennent plus nombreuses et moins sûres ». Le sens change selon que l'auteur pense à une baisse du taux d'erreur ou à une dilution par le volume ; je ne tranche pas.

**B18. Section 4, conclusion de partie (« Ce constat referme l'enquête… »).**
Passage : « Ce constat referme l'enquête de la @sec:partie-4 …. Elle les *enchaîne* d'abord dans des suites d'étapes … ; elle *retire* ensuite … ; elle *corrèle* enfin ».
Gêne : le « elle » de la phrase suivante se lit d'abord comme « l'enquête » (sujet féminin le plus proche), alors qu'il s'agit de l'automatisation. De plus, « Ce constat » ne désigne pas clairement ce qui est « refermé » (la section ? le chapitre ?).
Reformulation : « L'automatisation les *enchaîne* d'abord… ; elle les *retire* ensuite… ; elle *corrèle* enfin… ».

**B19. Section 4, avant-dernier paragraphe de conclusion.**
Passage : « Le diagnostic est désormais complet : agir d'après un cadre fini (@sec:partie-1), ce qui peut nous détromper à temps (@sec:partie-2), la spécification passée dans les données (@sec:partie-3), puis ce que l'automatisation fait de nos contrôles. »
Gêne : énumération elliptique sans verbe ni sujet ; on ne sait pas que ce sont les quatre questions traitées par les parties. Puis « Aucune couche d'outils ne peut garantir, de l'intérieur, qu'elle n'a rien omis » est une thèse jetée sans transition.
Reformulation : « Le diagnostic est désormais complet. Il a porté sur l'action fondée sur un cadre fini (partie 1), sur ce qui peut nous détromper à temps (partie 2), sur la spécification passée dans les données (partie 3), puis sur ce que l'automatisation fait de nos contrôles. »

**B20. Section 1, « Mise en place », liste de configurations (variation de m non signalée).**
Passage : dans les puces 1 à 3, « oublie 20 % des autres » ; dans la puce 4, « n'oublie que 10 % des erreurs non partagées ».
Gêne : la puce 4 change aussi m, mais cela n'est pas annoncé comme une modification (voir A1 pour l'effet sur l'interprétation). Même constat pour les « Mise en place » initiales : m est « 20 % » dans la formule et « 10 % » dans la puce 4.
Reformulation : dans la puce 4, ajouter « (et améliore en outre son taux d'oubli, de 20 % à 10 %) ». Le sens est préservé.

### Gravité C

**C1. Section 1, ouverture de l'exemple et tout le chapitre.** Mélange de notations : $P(E)$, $P(\text{faux})$, $\Pr(\bar{C}\mid E)$, $\Pr(A\mid E)$. Les formes « 10\,% » (mathématique) et « 10 % » (texte) coexistent. Reformulation : uniformiser dans la mesure du possible.

**C2. Section 1, § 5 (« Plaçons… »).** « le même modèle appris » : « appris » est un calque probable (*learned model*). Proposition : « le même modèle entraîné ».

**C3. Section 1, « Une difficulté pratique aggrave ce constat ».** Phrase avec tirets longs imbriqués (« La méthode existe pourtant — elle consiste à … —, mais elle demeure rarement mise en œuvre ») : à alléger en deux phrases.

**C4. Section 1, paragraphe « Calcul », 1er scénario.** Phrase unique de près de 70 mots avec cinq chiffres ; à scinder en deux ou trois phrases. « attrapée » est familier (« détectée »).

**C5. Section 1, scénario 4 (« Seul le scénario *Indépendant et précis*… »).** « Seul » est étrange : les scénarios précédents ont été traités juste avant ; « Enfin » serait plus naturel.

**C6. Section 1, encadré « Séparer… », 1er paragraphe.** « afin d'éviter une confusion fréquente sur l'effet de la seule règle de Bayes » : la confusion n'est pas énoncée. Phrases nominales « Et tant que… » à reformuler. Dans le 2e paragraphe, « que fixe la seule corrélation, à 60 % » : « à 60 % » flotte (« la seule corrélation, de 60 %,… »).

**C7. Section 2, 5e paragraphe.** « aboutissent devant le même prêteur » : image inhabituelle (« aboutissent au même prêteur »). Et « prêteur / emprunteur » : la métaphore financière s'introduit abruptement (« L'image financière éclaire immédiatement… ») alors que « emprunter le regard » apparaissait à peine auparavant.

**C8. Section 3, « Ce blanchiment attaque simultanément les deux versants… ».** « versants » mélange image et sens : proposer « deux plans » ou « deux volets ».

**C9. Section 4, 2e paragraphe.** « le goulet d'étranglement s'est brusquement retourné » : un goulet ne se retourne pas (les Points clés disent « déplacé »). « coûte presque zéro » : tour oral, probable calque de *costs almost nothing*. Propositions : « s'est brusquement déplacé » ; « ne coûte presque rien ».

**C10. Section 4, 3e paragraphe.** « les directions et les arbitrages budgétaires sont fortement incités » : zeugme, « arbitrages » ne peut pas être incité. Proposition : « les directions, dans leurs arbitrages budgétaires, sont fortement incitées ».

**C11. Points clés, puce 3.** « restaure la valeur prédictive positive et l'écoute des alertes » : « écoute » n'est jamais employé dans le corps du texte, où l'on parle de « prise en compte » (u). Uniformiser.

**C12. Dernier paragraphe, fin.** « trois niveaux : l'attitude personnelle, le placement des comparateurs, et des règles collectives » : parallélisme rompu (les deux premiers termes sont définis, le dernier est indéfini).

**C13. Section 3, 1er paragraphe.** « l'effacement des unités et des définitions » : « deux proches cousins » est un peu familier. Le mot « *pipeline* » en italique est acceptable mais gagnerait à une glose.

## 3. Appréciation globale

Les sections les plus accessibles sont la 2 (« Un même prêteur pour tous les emprunteurs »), grâce à la métaphore du prêteur et à la scène des vingt journalistes, très claire, et la 3, dont l'argument central (dix pages = une seule source) est bien porté par l'exemple du médecin ou de l'ingénieur. Les Points clés sont également nets.

Les moins accessibles sont l'exemple quantitatif de la section 1 : notations introduites tardivement (m, u, VPP, M1), calculs partiels, trois paragraphes de chiffres denses, une attribution causale incomplète (A1) et une ambiguïté sur la « corrélation égale » (A2). Viennent ensuite la section 4 pour son vocabulaire d'économie (« équilibre mélangeant », « signal coûteux ») et la conclusion de partie pour son enchaînement elliptique.

Dans l'ensemble, le fil du chapitre est cohérent et les chiffres que j'ai recalculés (sensibilité, VPP, échappement, risque) sont exacts.
