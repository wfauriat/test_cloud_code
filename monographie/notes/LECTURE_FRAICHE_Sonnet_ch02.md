# Lecture fraîche du chapitre 2 (« Le cadre : ce qui compte et ce qu’on tait »)

Lecteur : première lecture, texte seul. Seul le fichier `chapitres/02-cadre.md` a été lu.

## 1. Ce que j’ai compris du chapitre (test de lisibilité)

1. On n’agit jamais sur le monde lui-même mais d’après une représentation construite (mesures, catégories, équations, probabilités). Le monde répond à l’action, pas à la représentation (exemples du navigateur à 5 % et du téléphone satellite à 20 %).
2. Toute règle utilisable repose sur des conditions tues, la « parenthèse » : l’exemple de l’ébullition de l’eau montre qu’on la précise sans jamais la clore, et qu’elle ne peut pas l’être sans rendre la règle inutilisable.
3. Un « cadre » est la spécification finie, choisie avant toute inférence : variables, catégories, classe de modèles, objectif. La formule des probabilités totales montre que ce qui est hors de la liste de variables reste anonyme. Énoncer plus rend la règle fragile, énoncer moins laisse des exceptions muettes.
4. La rigueur interne (déduction, induction, inférence causale, prédiction conforme) ne certifie pas le cadre. Un modèle clinique peut échouer sans aucune faute technique, et ajouter une méta-procédure de contrôle ne fait que reporter le choix d’un cran.
5. Le « problème du cadre » de l’IA (McCarthy, Hayes, Dennett) est pris ici au sens large : l’impossibilité de spécifier à l’avance tout ce qui est pertinent.

Les deux seuls points que je n’ai pas pu reconstituer sans effort sont l’apologue du robot (§5, contradiction interne) et le détail des deux « garanties » formelles du §4 (jargon).

## 2. Constats classés par gravité

### Gravité A (compréhension compromise)

**A1. §5 (« Un mot sur le problème du cadre »), apologue de Dennett.**
Passage : « sa batterie de rechange, posée sur un chariot à côté d’une bombe à retardement » puis « il savait la bombe posée dessus, mais n’avait pas compris qu’elle suivrait la batterie ».
Gêne : la bombe est d’abord « à côté » de la batterie, puis « dessus » (sur le chariot). La chute (la bombe suit la batterie) ne tient que si la bombe est sur le chariot. Le lecteur ne sait pas quelle version retenir.
Reformulation minimale : « posée sur un chariot, lequel portait aussi une bombe à retardement ».
Risque de glissement de sens : aucun si l’on retient la lecture « bombe sur le chariot », seule compatible avec la suite. Si le texte voulait « à côté », la suite est à revoir. Je ne tranche pas le contenu mais la phrase actuelle est contradictoire.

### Gravité B (gêne réelle)

**B1. §1, exemple du navigateur.**
Passage : « il estime à 5 % le risque de démâter s’il part sur un voilier léger plutôt que sur un voilier renforcé ».
Gêne : deux lectures plausibles. (i) 5 % est le risque propre au voilier léger, comparé implicitement au renforcé. (ii) 5 % est un écart de risque entre les deux bateaux. La suite (« une course à 5 % ») favorise (i) sans l’imposer.
Reformulation minimale (lecture i) : « il estime à 5 % le risque de démâter s’il part sur un voilier léger (plutôt que sur un voilier renforcé) ». Pour (ii) il faudrait « à 5 points de plus ». Je ne tranche pas.

**B2. §1, exemple du téléphone satellite.**
Passage : « Si sa barre casse au large ».
Gêne : la représentation listait « l’âge du moteur », jamais la barre. Le lecteur ne voit pas si la barre est un facteur omis (c’est probablement le but) ou un incident déjà prévu parmi les « avaries ». C’est aussi un cas où le chiffre de 20 % n’est pas comparé à une issue : le lien avec « l’omis » reste implicite.
Reformulation minimale : « Si sa barre casse au large (avarie que sa représentation n’avait pas distinguée), ». Le sens bouge si la barre est un incident prévu ; auquel cas il vaut mieux ne rien ajouter.

**B3. §2, avant-dernier paragraphe de la section.**
Passage : « Cette ouverture n’est pas un défaut de méthode ».
Gêne : « ouverture » n’a pas été posé ; on a parlé de parenthèse et de liste « non close ». Le lecteur doit deviner que c’est le caractère ouvert de la parenthèse.
Reformulation minimale : « Le caractère ouvert de la parenthèse n’est pas un défaut de méthode… C’est lui, au contraire, qui rend… ».

**B4. §3, énumération des quatre choix, point 1.**
Passage : « les variables, c’est-à-dire les grandeurs que l’on mesure […], et, par omission, toutes celles que l’on néglige ou que l’on suppose constantes ».
Gêne : la définition de « variables » inclut ce qu’on retient et, « par omission », ce qu’on néglige. Un lecteur peut y voir une contradiction ou ne pas comprendre en quel sens les omises sont des « variables » du cadre.
Reformulation minimale : « les variables retenues […] ; le choix écarte, en creux, toutes celles que l’on néglige ou suppose constantes (…) ». Sens inchangé.

**B5. §3, juste après l’exemple de la crue.**
Passage : « L’écriture probabiliste rend cette dépendance explicite ». Puis : « L’@eq:ch02-cond-cadre se lit à deux niveaux […] Mais l’essentiel est décidé avant même d’écrire la somme ».
Gêne : (a) « cette dépendance » n’a pas de référent net (dépendance de la prévision au cadre ?). (b) « deux niveaux » désigne en fait deux facteurs (lois conditionnelles et poids ; la boîte dit « deux éléments distincts »), puis le « Mais » en ajoute un troisième, la liste, qui n’est pas un niveau de lecture de la même nature. Le lecteur attend deux niveaux et en reçoit trois.
Reformulation minimale : « …rend explicite la dépendance de toute prévision à l’égard du cadre » ; « se lit en deux temps » ou « comporte deux facteurs », puis « Mais l’essentiel est décidé en amont : la somme suppose arrêtée la liste… ». Le contenu ne change pas.

**B6. §3, boîte « Conditionnement sur les variables du cadre ».**
Passage : « Les lois Pr(Y | X = x) moyennent tacitement son effet sur les valeurs qu’il prenait là où elles ont été établies ».
Gêne : calque de « average over » ; « son effet sur les valeurs » se lit « l’effet exercé sur les valeurs », ce qui n’est pas l’idée (moyenne de l’effet prise sur l’ensemble des valeurs que le facteur prenait). « il » (le facteur) et « elles » (les lois) sont éloignés du verbe.
Reformulation minimale : « Les lois Pr(Y | X = x) incorporent tacitement une moyenne de son effet sur l’ensemble des valeurs que ce facteur prenait là où elles ont été établies ». Sens inchangé.

**B7. §3, après la boîte.**
Passage : « Le compromis est plus serré qu’il n’y paraît. »
Gêne : (a) « le compromis » n’a pas été annoncé : la question précédente propose d’allonger la liste, pas de composer ; le lecteur découvre ensuite qu’il s’agit du compromis entre énoncer plus et énoncer moins. (b) « plus serré » sent le calque de « tighter trade-off ».
Reformulation minimale : « L’arbitrage est plus contraignant qu’il n’y paraît : il faut choisir entre énoncer plus et énoncer moins. » Sens inchangé.

**B8. §4, paragraphe sur la déduction (poutre).**
Passage : « Considérons à nouveau la poutre de la @sec:ch01-modes-inference. Si elle porte une fissure […] « cette poutre est en acier homogène » est fausse. Si la charge varie de façon cyclique, c’est la prémisse générale qui devient fausse ».
Gêne : possible dépendance. La poutre n’est pas rappelée et la « prémisse générale » n’a jamais été nommée dans ce chapitre. Un lecteur qui ne retrouve pas le §1 de l’autre chapitre ne sait pas de quelle prémisse il s’agit ni quelle est la conclusion.
Reformulation minimale : rappeler l’argument en une demi-phrase : « (… tout acier homogène porte telle charge ; cette poutre est en acier homogène ; donc elle porte cette charge) ». À vérifier avec l’auteur : le syllogisme exact du chapitre 1.

**B9. §4, même paragraphe.**
Passage : « Dans les deux cas, le raisonnement reste valide, mais il cesse d’être solide ».
Gêne : la distinction valide/solide (angl. valid/sound) n’est pas présentée ici. Un lecteur cultivé non logicien peut croire que « valide » et « solide » sont synonymes ou comprendre « solide » au sens de robustesse. Possible dépendance du chapitre 1.
Reformulation minimale : « le raisonnement reste valide (sa forme est correcte), mais ses prémisses ne sont plus vraies : sa conclusion n’est plus garantie ». Sens inchangé.

**B10. §4, paragraphe sur l’induction.**
Passage : « les variables sur lesquelles on conditionne et la série de référence qui définissent cette ressemblance ».
Gêne : « la série de référence » surgit sans introduction (la suite parle de jeu d’étalonnage). Le « qui » pluriel s’accorde mal avec le groupe de trois termes dont le dernier est au singulier.
Reformulation minimale : « les grandeurs mesurées, les variables sur lesquelles on conditionne et l’ensemble de cas pris pour référence, qui définissent cette ressemblance ». Si « série de référence » désigne autre chose que le jeu d’étalonnage, le dire.

**B11. §4, paragraphe Pearl / prédiction conforme et boîte.**
Passages : « l’ensemble prédit contiendra la vraie valeur », « le critère de d-séparation et les règles du do-calcul », « un score de non-conformité ».
Gêne : possibles dépendances. Le corps du texte explique « identifiable » et « échangeables », mais « d-séparation », « do-calcul » et « score de non-conformité » ne sont jamais glosés. Leur position dans la boîte « formel » les rend digestes pour un lecteur spécialiste, pas pour un lecteur cultivé. « Ensemble prédit » est aussi obscur (ensemble de valeurs plausibles ?).
Reformulation minimale : une incise suffit, par exemple « (d-séparation et do-calcul, deux outils de lecture du graphe) », « score de non-conformité (mesure de l’écart entre prévision et réalité) », « ensemble de valeurs prédit ». Aucun changement mathématique.

**B12. §4, boîte, point 2.**
Passage : « Ils servent à ajuster un modèle, puis à étalonner un score de non-conformité (c’est le jeu d’étalonnage). »
Gêne : « c’est » est flou (les cas ? le score ? la seconde étape ?). Deux lectures : « les cas servant à l’étalonnage forment le jeu d’étalonnage », ou « étalonner le score = jeu d’étalonnage ». Le corps du texte emploie « jeu d’étalonnage » comme les cas eux-mêmes, ce qui oriente vers la première.
Reformulation minimale : « (les cas utilisés pour cette seconde étape forment le jeu d’étalonnage) ». Le sens risque de bouger si l’auteur entend autre chose ; je ne tranche pas.

**B13. §4, fin de section.**
Passage : « Le @sec:ch07 reviendra sur cette régression à l’infini ».
Gêne : le texte dit seulement que la méta-procédure « adopte à son tour un cadre » et reporte « d’un étage ». Le caractère infini du report (étage après étage) n’est jamais dit : le lecteur doit le déduire.
Reformulation minimale : ajouter avant : « …exposé aux mêmes omissions un étage plus haut, et ainsi de suite sans terme. » Contenu inchangé.

**B14. §5, apologue de Dennett.**
Passage : « Un robot devait sortir… Le premier modèle a tiré… Le deuxième… Le troisième ».
Gêne : (a) on passe d’« un robot » à trois « modèles » sans l’annoncer. (b) « modèle » entre en collision avec le sens statistique de tout le chapitre, ce qui fait lire « modèle » comme « représentation » plutôt que « version du robot ».
Reformulation minimale : « Dennett imagine trois versions successives d’un robot, chargé de sortir d’une pièce… Le premier robot… Le deuxième… Le troisième ». Sens inchangé.

**B15. §5, citation de la source.**
Passage : « [@A-VERIFIER: Shanahan, « The Frame Problem », SEP] ».
Gêne : marqueur éditorial qui s’affichera tel quel ou comme une clé brisée. « SEP » n’est pas développé. Ce n’est pas un problème de lecture mais le lecteur verra un défaut non résolu.
Reformulation minimale : remplacer par une clé de citation valide (ou retirer l’appel) et développer « Stanford Encyclopedia of Philosophy » si la source reste dans le texte.

### Gravité C (confort / style)

**C1. §1, paragraphe du navigateur.**
Passage : « porté à l’intérieur d’une certaine façon de découper la situation, ce que nous appellerons plus loin un cadre : ce que le navigateur retient de la mer… ».
Gêne : deux « ce que » à quelques mots d’intervalle, l’un annonçant le terme, l’autre le développant ; la phrase est longue et l’antécédent de « ce que nous appellerons » est flou.
Reformulation minimale : couper en deux : « …porté à l’intérieur d’une certaine façon de découper la situation. Nous appellerons cela plus loin un cadre : il comprend ce que le navigateur retient de la mer… ».

**C2. §1, paragraphe de la dissymétrie.**
Passage : « Cette dissymétrie entre la représentation et la réponse du monde ».
Gêne : « dissymétrie » n’a pas été nommée comme telle jusque-là (on parlait de « seconde phrase de la définition »). Ce n’est pas grave, mais c’est un terme d’apparition soudaine.
Reformulation minimale : « Cet écart entre la représentation et la réponse du monde ».

**C3. §2, exemple de la voiture.**
Passage : « une voiture roulant à 50 km/h sur route sèche […] une chaussée sans gravillons ni plaque de verglas ».
Gêne : « route sèche » est déjà énoncé, puis le verglas est cité comme condition tue ; l’exemple se contredit un peu (sur route sèche, il n’y a pas de verglas).
Reformulation minimale : supprimer « sur route sèche » de la règle énoncée, ou remplacer « plaque de verglas » par « huile ou feuilles mortes ».

**C4. §2, mont Blanc.**
Passage : « ce que chacun en retient, à savoir que l’eau bout à 100 °C ».
Gêne : « en » renvoie à la règle (ou à l’expérience ?) sans être net.
Reformulation minimale : « ce que chacun retient de cette règle ».

**C5. §2, paragraphe « Même ainsi, l’inventaire n’est pas clos ».**
Passage : « petites bulles bien avant l’ébullition, qu’un observateur pressé peut prendre pour elle ».
Gêne : relative et pronom (« qu’ », « elle ») qui se renvoient dans une même phrase.
Reformulation minimale : « qu’un observateur pressé peut confondre avec l’ébullition ».

**C6. §2, structure A, B.**
Passage : « La lettre $A$ y rassemble les conditions énoncées » ; la lettre B n’est jamais glosée dans ce chapitre.
Gêne : possible dépendance légère. La conséquence « B » reste implicite.
Reformulation minimale : « …et B ce que la règle annonce (ici l’ébullition) ».

**C7. §3, définition du cadre.**
Passage : « les variables, les catégories, la classe de modèles et l’objectif qu’il retient ».
Gêne : « il » peut renvoyer au raisonnement ou au cadre. Les deux lectures donnent le même sens pratique.
Reformulation minimale : « l’objectif que celui-ci retient » ou « l’objectif retenu ».

**C8. §3, articulation cadre/représentation.**
Passage : « ce qui a droit de cité dans l’analyse et la forme des liens envisagés ».
Gêne : la coordination est ambiguë (« dans l’analyse et dans la forme » ?).
Reformulation minimale : « ce qui a droit de cité dans l’analyse, ainsi que la forme des liens envisagés ».

**C9. §3, exemple de la crue.**
Observation : le texte annonce « relève du premier choix… du quatrième » alors que les quatre choix sont énumérés une dizaine de lignes plus haut. Le lecteur doit remonter.
Reformulation minimale : rappeler la nature de chaque choix entre parenthèses : « (premier choix : les variables) ».

**C10. §3 (boîte « Énoncer plus ou taire plus »).**
Passage : la première puce mêle trois arguments (pratique, statistique, illusion) en une seule puce longue.
Reformulation minimale : couper en trois phrases courtes ou trois sous-puces. Aucun changement de contenu.

**C11. §3, boîte « formel » (Conditionnement…).**
Observation : la boîte reprend l’équation et presque mot pour mot l’explication du texte précédent. La répétition est pesante pour un lecteur non spécialiste. Elle apporte surtout la mention de l’intégrale.
Reformulation minimale : aucune réécriture ; envisager de signaler dans le texte que la boîte est facultative pour le lecteur non formaliste.

**C12. §4, titre et vocabulaire.**
Passage : le titre « La rigueur formelle ne lève pas cette limite ».
Gêne : « cette limite » n’a pas de référent dans la section précédente (on y parlait de parenthèse, d’exceptions, de « dépendance »). Le texte alterne ensuite « dépendance envers le cadre », « relativité au cadre », « limite ».
Reformulation minimale : « La rigueur formelle ne lève pas la dépendance envers le cadre ».

**C13. §4, cas clinique.**
Passage : « Entre-temps, l’organisation des urgences a changé les critères d’admission ».
Gêne : « entre-temps » ne convient qu’à l’alternative « quelques années plus tard », pas à « une autre région ».
Reformulation minimale : « Dans l’intervalle, ou ailleurs, l’organisation des urgences a pu changer les critères d’admission ».

**C14. §5, apologue de Dennett.**
Passage : « Un robot devait sortir d’une pièce sa batterie de rechange ».
Gêne : ordre des compléments peu naturel, probablement calque de « retrieve … from a room ».
Reformulation minimale : « devait récupérer, dans une pièce, sa batterie de rechange ».

**C15. §4, §3 (rythme).**
Observation : le paragraphe sur la déduction (§4) dépasse deux cents mots et mêle principe, explication, exemple de la poutre et deux variantes. À couper après « elle ne la crée pas et ne la certifie pas » pour ouvrir un paragraphe avec la poutre.

## Comptage

- Gravité A : 1 (A1)
- Gravité B : 15 (B1 à B15)
- Gravité C : 15 (C1 à C15)

## 3. Appréciation globale

Sections les plus accessibles : §1 (le monde répond à l’action) et §2 (pertinence et exceptions). Ce sont des exemples concrets (navigateur, téléphone satellite, ébullition avec tableau), une progression claire et un fil continu. Le tableau et la parenthèse A ∩ (…) → B sont bien amenés. La citation de Pearl sur le champ de mines est limpide.

Sections moyennement accessibles : §3. La définition du cadre et les quatre choix passent bien, surtout avec l’exemple de la crue. La difficulté vient du glissement vers la formule des probabilités totales (références à l’équation et expressions « deux niveaux », « compromis »), plus la boîte formelle redondante.

Sections les moins accessibles : §4 et la fin de §5. §4 enchaîne deux outils très techniques (inférence causale, prédiction conforme) avec un jargon non glosé et des renvois au chapitre 1 non rappelés (poutre, valide/solide). Le cas clinique, lui, est clair. §5 est brève mais l’apologue du robot est confus (bombe « à côté » / « dessus », « modèle » ambigu), et un marqueur « A-VERIFIER » reste dans le texte.

Le chapitre est globalement bien écrit, sans calque lourd. Les points A et B se concentrent sur §4 et §5, les deux dernières sections.
