# Points laissés à l’auteur : partie 1 (page de partie et chapitres 1 à 4)

Ces constats des relectures « à froid » (Sonnet, Opus) n’ont pas été appliqués, pour l’une de ces raisons : deux lectures plausibles ; incohérence de fond ; changement de portée ou de force ; nombre ; terme ou définition du registre ; ajout d’une affirmation. Dans chaque fichier, les points sont classés par importance, les incohérences de fond d’abord. Viennent ensuite les constats rejetés, avec une raison courte. La dernière section regroupe ce qui concerne plusieurs fichiers ou le livre entier.

Les corrections appliquées sont consignées dans `notes/EDITS_partie1.md`. Les extraits ci-dessous citent le texte tel qu’il est après ces corrections.

## Décompte

| Fichier | Points à trancher | Constats rejetés |
| :-- | --: | --: |
| `parties/partie-1.md` | 4 | 4 |
| `chapitres/01-outils-logique-probabilite.md` | 13 | 23 |
| `chapitres/02-cadre.md` | 16 | 26 |
| `chapitres/03-mondes-possibles.md` | 18 | 22 |
| `chapitres/04-decider.md` | 9 | 23 |

(Un constat parfois en partie appliqué, en partie laissé ou rejeté, figure à chaque endroit concerné.)

---

## `parties/partie-1.md`

**T1. Deux lectures de « vaut » (logique).** Paragraphe consacré au chapitre 1.
- Extrait : « Une déduction ne vaut que si ses prémisses sont vraies, une généralisation que si les cas à venir ressemblent à ceux que l’on a observés. »
- Lectures : (a) la conclusion d’une déduction n’est garantie que si les prémisses sont vraies (intention probable) ; (b) une déduction n’est *valide* que si ses prémisses sont vraies, ce qui est faux pour un logicien, puisque la validité ne dépend que de la forme (le ch. 1 distingue d’ailleurs valide et solide).
- Proposition (Opus B1) : « Une déduction ne garantit sa conclusion que si ses prémisses sont vraies ».
- Non appliqué : le lecteur voit deux lectures. « Ne vaut que » est en outre la formulation du registre (« L’une et l’autre ne valent que « pourvu que »… ») et revient au ch. 2 (chapeau) et aux Points clés du ch. 1 ; à harmoniser globalement si l’auteur le souhaite.

**T2. Portée de « ne protège de rien ».** Paragraphe consacré au chapitre 4.
- Extrait : « Dans ce dernier cas, aucune série d’essais ne vient compenser une issue malheureuse, et avoir raison en moyenne ne protège de rien. »
- Question : « de rien » (portée générale) ou « de cette issue » (portée restreinte) ? « Avoir raison en moyenne » sonne aussi comme un calque (*being right on average*) et suppose la notion d’espérance, introduite au ch. 4.
- Propositions : Opus B3, « et une décision qui serait gagnante en moyenne sur de nombreux essais ne protège pas de cette issue » ; Sonnet C3, rien à changer si le ch. 4 reprend la notion.
- Non appliqué : changement de portée ; les lecteurs divergent.

**T3. Connecteur « Encore faut-il ».** Paragraphe consacré au chapitre 3.
- Extrait : « Encore faut-il savoir ce qu’exprime une probabilité. »
- Lectures : (a) simple transition (« il reste à comprendre ») ; (b) condition de validité des calculs faits dans le cadre.
- Propositions : Sonnet C2, « Reste à savoir ce qu’exprime une probabilité. » ; Opus C1, « Reste à savoir ce qu’exprime une probabilité, outil central de ces modèles. »
- Non appliqué : Sonnet voit deux lectures et ne tranche pas. « Reste à » supprimerait la nuance de condition, et l’ajout d’Opus introduit une affirmation.

**T4. « Probabilité », « confiance », « situations », « issues ».** Même paragraphe.
- Extrait : « la façon dont on répartit sa confiance entre les situations que l’on ne peut pas encore exclure […]. Comme une probabilité se partage ainsi entre plusieurs issues »
- Question : c’est la confiance, non la probabilité, qui « se partage » ; et l’on passe de « situations » à « issues » d’une phrase à l’autre.
- Proposition (Opus B2, seconde partie) : « Comme la confiance se répartit ainsi entre plusieurs issues ».
- Non appliqué : choix de termes qui touche la manière de présenter les mondes possibles (registre, ch. 3). Seul le pronom « la » a été corrigé (EDITS, E1).

### Constats rejetés
- Sonnet C1, « Le chapitre [-@sec:ch02] en tire la conséquence » : le « en » renvoie clairement au paragraphe précédent ; le lecteur lui-même ne voit pas de risque.
- Opus C2, « quels modèles compteront » : sens stable dans les deux lectures ; retouche de style.
- Opus C3, « dans ces conditions » : idiome courant au sens clair ; la proximité avec « conditions » (de validité) au paragraphe suivant est une gêne légère.
- Opus C4, espaces ordinaires avant « : ; ? » et dans « 100 °C » : les conventions (§8) demandent des espaces simples ; le filtre et babel-french les convertissent.

---

## `chapitres/01-outils-logique-probabilite.md`

### Incohérences de fond

**T1. Critère de la probabilité nulle : « réellement » ou « logiquement » impossible.** § Mesurer la qualité d’une prévision, texte et encadré `.formel` « Score logarithmique et rapport de vraisemblance », point 3.
- Extraits : texte, « D’où une règle de prudence élémentaire : ne donner une probabilité nulle qu’à ce qui est réellement impossible. » ; encadré, « la prudence commande de la réserver à ce qui est logiquement impossible. »
- Question : « réellement » (physiquement, en fait) est plus large que « logiquement » ; le lecteur ne sait pas quelle règle retenir, dans un chapitre qui oppose sans cesse ce que garantit la logique à ce que réalise le monde.
- Proposition (Sonnet B10, Opus A1) : harmoniser sur un seul adverbe, au choix de l’auteur.
- Non appliqué : harmonisation d’un critère entre texte et encadré, qui change le sens (règle stricte ou large). Voir aussi ch. 3 (« logiquement exclu », garde-fou) dans la liste transversale.

**T2. « L’exemple ne dit pas […] d’où viennent les chiffres de la sonde ».** Encadré `.exemple-quantitatif`, dernier paragraphe.
- Extrait : « L’exemple ne dit pas, en revanche, d’où viennent les chiffres de la sonde. Ils ont été mesurés sur des pièces d’étalonnage et ne valent pour les soudures réelles que pourvu que celles-ci leur ressemblent ; »
- Question : la mise en place dit déjà que les chiffres viennent de pièces d’étalonnage, et les déclare « purement illustratifs », alors qu’ici ils « ont été mesurés ». Faut-il dire que l’exemple ne discute pas la *portée* de ces chiffres (Opus), ou que la fiction est qu’ils ont été mesurés (Sonnet, lecture i) ?
- Propositions : Opus B8, « L’exemple ne discute pas, en revanche, la portée des chiffres de la sonde. » ; Sonnet B7 (lecture i), « Supposons que ces chiffres aient été mesurés sur des pièces d’étalonnage : ils ne valent alors pour les soudures réelles que pourvu que… ».
- Non appliqué : deux lectures plausibles (provenance ou validité) ; le sens bouge selon le choix.

**T3. « La seconde sonde ».** Même encadré, Lecture (et légende : « deux signaux anormaux indépendants »).
- Extrait : « Si la seconde sonde réagit à la même irrégularité de forme que la première, son signal n’apporte presque rien de neuf »
- Question : le second signal vient-il d’une seconde sonde ou d’un second passage de la même sonde ? La mise en place ne parle que de « la sonde ».
- Propositions : Opus B7, « Si le second examen réagit… » et annoncer le dispositif dans la mise en place ; Sonnet B4, « la seconde sonde (ou le second passage) ».
- Non appliqué : deux lectures plausibles ; c’est à l’auteur de fixer le dispositif, de préférence dès la mise en place.

**T4. « Score logarithmique » et « surprise ».** § Mesurer la qualité d’une prévision, définition en gras.
- Extrait : « C’est ce que mesure le **score logarithmique**. La surprise d’une issue, sous une prévision qui lui attribuait la probabilité $p = \Pr(\text{issue})$, vaut : »
- Question : le terme en gras n’est jamais explicitement identifié à « la surprise », qui est le mot effectivement défini ; le sens de lecture (plus il est faible, meilleure est la prévision ; c’est une pénalité) n’est pas énoncé. Le registre définit le terme comme « Surprise d’une issue, −ln Pr(issue)… ».
- Propositions : Opus B9, « C’est ce que mesure le **score logarithmique**, que nous appellerons aussi *surprise* : plus il est élevé, plus l’issue a pris la prévision au dépourvu. » ; Sonnet B8, « Le score logarithmique d’une prévision est la surprise de l’issue observée […] ; plus il est faible, meilleure est la prévision. »
- Non appliqué : la correction touche la phrase de définition en gras d’un terme du registre et ferait de « surprise » un synonyme déclaré. Sonnet signale aussi que l’auteur distingue peut-être score et surprise.

**T5. Indépendance des issues ou des prévisions.** § Mesurer la qualité d’une prévision.
- Extrait : « Sur une série de prévisions indépendantes, enfin, les surprises s’additionnent »
- Question : l’encadré parle d’issues « jugées indépendantes » ; c’est cette condition, et non l’indépendance des prévisions, qui fonde l’additivité.
- Proposition (Opus C14) : « Sur une série d’issues jugées indépendantes ».
- Non appliqué : la correction modifie la condition d’un résultat (fond).

**T6. « L’arrière-plan tu $(\dots)$ laisse effectivement $B$ se produire ».** § Probabilité conditionnelle et probabilité totale.
- Extrait : « $\Pr(B \mid A)$ mesure, parmi les situations où les conditions énoncées $A$ sont remplies, la part de celles où l’arrière-plan tu $(\dots)$ laisse effectivement $B$ se produire. »
- Question : l’image est elliptique : $(\dots)$ désigne-t-il des circonstances réunies ou non dans chaque monde ?
- Proposition (Sonnet B11) : « …la part de celles où les circonstances non énoncées $(\dots)$ sont réunies de sorte que $B$ se produit ».
- Non appliqué : le lecteur précise lui-même « si l’auteur entend bien cela » ; la même image revient au ch. 3 (§ Mondes possibles, « où l’arrière-plan laisse effectivement $B$ se produire »), à traiter ensemble.

### Deux lectures, portée, terminologie

**T7. Prémisses et « idéalisations ».** § Déduction et induction.
- Extraits : « Lorsque les définitions, les mesures et les idéalisations de départ décrivent fidèlement la situation » ; puce « la déduction garantit sa conclusion *pourvu que* ses prémisses et ses idéalisations soient exactes ».
- Question : « idéalisations » surgit sans préparation ; sont-elles une sorte de prémisses (proposition d’Opus) ou une catégorie distincte (lecture de la puce, et du ch. 2 : « les axiomes, les définitions, les conditions aux limites et les idéalisations de départ ») ?
- Propositions : Opus C2, « Lorsque les prémisses — définitions, mesures, idéalisations de départ — décrivent fidèlement la situation » ; Sonnet C3, annoncer les idéalisations dans l’exemple de la poutre.
- Non appliqué : la proposition d’Opus fusionne deux notions que la puce distingue ; changement de sens possible.

**T8. « Elle donne aussi une définition précise de l’indépendance ».** § Probabilité conditionnelle et probabilité totale.
- Question : « Elle » renvoie-t-il à la règle du produit ou à l’@eq:ch01-cond ?
- Propositions : Sonnet C10, « Cette règle permet aussi de définir… » ; Opus C8, « La probabilité conditionnelle donne aussi… » ou « Cette règle donne aussi… », selon l’intention.
- Non appliqué : Opus voit deux lectures et ne tranche pas.

**T9. « Le @sec:ch02 s’appuiera sur cette formule. Les probabilités conditionnelles $\Pr(B \mid H_i)$ y résument… ».** Même section.
- Question : « y » désigne-t-il la formule ou le chapitre 2 ?
- Proposition (Sonnet C11, Opus C11) : « Dans cette formule, les probabilités conditionnelles… résument… ».
- Non appliqué : Opus juge les deux lectures plausibles. Si l’auteur visait « dans le ch. 2 », la reformulation déplace le propos.

**T10. Indépendance « sous chacune des deux hypothèses ».** § Réviser un jugement.
- Extrait : « si plusieurs observations $E_1, E_2, \dots$ sont indépendantes sous chacune des deux hypothèses »
- Question : cette indépendance conditionnelle n’est définie qu’à la fin de l’encadré suivant ; risque de confusion avec l’indépendance simple définie juste avant.
- Proposition (Opus B4) : ajouter « (on dit *conditionnellement indépendantes* ; voir l’encadré ci-dessous) ».
- Non appliqué : l’ajout ferait passer un terme technique de l’encadré au texte principal (nouveau terme dans le texte courant). « Sous chacune des deux hypothèses » marque déjà la différence.

**T11. « Aucune observation ne rendra plus cette éventualité plausible ».** Encadré `.formel`, point 3.
- Lectures : « ne… plus » (plus jamais) ou « plus plausible » (davantage).
- Proposition (Opus C16) : « aucune observation ne pourra jamais rendre cette éventualité plausible ».
- Non appliqué : deux lectures (même conclusion pratique, selon le lecteur) ; choix d’auteur.

**T12. « Deux lignes de calcul suffisent à suivre le mécanisme ».** Encadré `.exemple-quantitatif`, Calcul.
- Question : le paragraphe contient quatre calculs (deux points de départ) ; « deux lignes » peut sembler trompeur, et l’on mêle fractions et décimaux.
- Proposition (Sonnet B5) : « Deux cas suffisent… », et présenter les quatre issues en liste.
- Non appliqué : touche un nombre dans un bloc `.exemple-quantitatif` ; le paragraphe compte d’ailleurs bien deux phrases de calcul, une par point de départ.

**T13. « Conditions tues », « arrière-plan tu », « conditions sous-entendues », « arrière-plan non énoncé ».** Chapeau, § Règles conditionnelles et conditions tues (titre), § Probabilité conditionnelle.
- Question : plusieurs expressions désignent une même notion ; « tu » adjectif est rare. Le registre (notations) emploie « règle à conditions sous-entendues » et « arrière-plan non énoncé ».
- Proposition (Sonnet C5) : harmoniser sur « non énoncé » ou « sous-entendu ».
- Non appliqué : choix terminologique qui touche un titre de section et plusieurs chapitres (voir liste transversale).

### Constats rejetés
- Sonnet B6, ajouter « (25 % de défauts manqués contre 15 % de fausses alertes) » à « parce que la sonde manque un défaut… » : ajout de nombres dans un bloc `.exemple-quantitatif` ; le raisonnement actuel est exact.
- Sonnet B12, seconde partie (gloser $\cup$ et $\emptyset$) : encadré formel ; « incompatibles » explicite déjà $A \cap B = \emptyset$, et le texte courant dit « que l’un ou l’autre se produise ».
- Opus B1 (∩ employé avant sa glose) : la glose arrive quelques lignes plus bas et « lorsque plusieurs conditions doivent être réunies » donne déjà le sens ; une seconde glose ferait doublon.
- Sonnet C1 (« Ce chapitre ne suppose rien des autres ») : « supposer » au sens de « présupposer » est correct ; sens clair.
- Sonnet C2, première partie (« formes authentiques de rigueur ») : français correct.
- Sonnet C4 (« l’eau y bout bien avant ») : une seule lecture plausible.
- Sonnet C6 (« Un besoin se fait sentir dès maintenant ») : style.
- Sonnet C7 (deux sens de « monde ») : le ch. 1 annonce lui-même « des situations, ou des mondes » ; le ch. 3 fixe le terme.
- Sonnet C8 (« calibration » et « étalonnage ») : deux notions distinctes (étalonnage d’un instrument ; calibration d’un prévisionniste, terme du registre) ; la distinction est voulue.
- Sonnet C9 (titre de la nuance « un débat que ce livre ne tranche pas ») : attribut de bloc ; « ne tranche pas » est cohérent avec « position de travail ».
- Sonnet C12 (« son contraire » plutôt que « sa négation ») : usage courant ; la notation $\bar{H}$ précise.
- Sonnet C13 (syntaxe « en appliquant… à $H_1$ et à $H_2$ sachant $E$ ») : encadré formel, compréhensible.
- Sonnet C14 (chiffrer l’écart des surprises) : ajouterait un nombre.
- Sonnet C16 (« sous la première prévision contre la seconde », « Du côté de la règle de Bayes ») : « sous la prévision » est la formulation du registre (score logarithmique) ; le reste relève du style.
- Sonnet C17 et Opus C14, seconde partie (« coûte cher », « coûte une surprise infinie », « enfin ») : style.
- Sonnet C18 (règles énoncées deux fois) : choix pédagogique (intuitif, puis formel dans l’encadré), conforme à la règle du texte principal.
- Opus C3 (« où les bulles se forment » au subjonctif) : l’indicatif énonce un fait général exact.
- Opus C6 (ajouter « D’abord » à la première raison) : « Le jugement d’abord » vient d’être employé ; énumération lisible.
- Opus C7 (« La même opération chirurgicale ») : les deux lectures donnent le même sens.
- Opus C9 (« exclusives l’une de l’autre », « leur moyenne pondérée ») : tournure française correcte ; la formule suit immédiatement.
- Opus C10 (« hypothèses » et « scénarios ») : la définition de la partition, donnée dans la phrase, lève le doute.
- Opus C12, deuxième partie (couper en trois la phrase de calcul de la zone suspecte) : énumération lisible après les deux-points, dans un bloc `.exemple-quantitatif`. (La troisième partie, « zone suspecte », est appliquée : EDITS, E8.)
- Opus C13 (« diviser par 3,4 environ ») : ajouterait un nombre dans un bloc `.exemple-quantitatif`.

---

## `chapitres/02-cadre.md`

### Incohérences de fond

**T1. Cadre et représentation : emboîtés ou disjoints ?** Définition de la représentation (§ Le monde répond à l’action), § Le cadre comme spécification finie, premier point clé.
- Extraits : « Une **représentation** est la construction (mesures, catégories, équations, probabilités) d’après laquelle on décide et l’on agit. » ; « La représentation est ce que l’on construit à l’intérieur de ce cadre (valeurs mesurées, paramètres estimés, probabilités attribuées), et d’après quoi l’on agit. » ; « redéfinir une catégorie ou changer d’objectif, ce n’est plus ajuster une représentation à l’intérieur du cadre : c’est changer de cadre. »
- Question : les catégories (et les équations, qui relèvent de la classe de modèles) appartiennent à la représentation selon la définition, puis au cadre selon le § 3. Le cadre fait-il partie de la représentation (lecture emboîtée), ou la représentation est-elle ce que l’on met dans le cadre (lecture disjointe) ?
- Proposition (Opus A1) : « La représentation est la construction complète : le cadre, plus ce que l’on construit à l’intérieur de lui (…) » (lecture emboîtée) ; sinon, retoucher la parenthèse de la définition et du premier point clé (lecture disjointe).
- Non appliqué : incohérence de fond entre deux définitions du registre ; deux lectures.

**T2. Apologue de Dennett : place de la bombe ; « modèle ».** § Un mot sur le « problème du cadre ».
- Extrait : « Un robot devait sortir d’une pièce sa batterie de rechange, posée sur un chariot à côté d’une bombe à retardement. Le premier modèle a tiré le chariot dehors : il savait la bombe posée dessus, mais n’avait pas compris qu’elle suivrait la batterie. »
- Question : la bombe est « à côté » puis « dessus » ; la chute n’a de sens que si elle est sur le chariot. Par ailleurs, on passe d’« un robot » à trois « modèles » sans l’annoncer, et « modèle » entre en collision avec le sens statistique qu’il a dans tout le chapitre.
- Propositions : Sonnet A1, « posée sur un chariot, lequel portait aussi une bombe à retardement » ; Opus B11, « posée sur un chariot où se trouvait aussi une bombe à retardement » ; Sonnet B14, « Dennett imagine trois versions successives d’un robot… Le premier robot… ».
- Non appliqué : contenu de l’apologue (point réservé à l’auteur) ; mieux vaut le reprendre d’un seul geste avec la question du « modèle ».

**T3. « Problème du cadre » : sens étroit ou large dans les Points clés.** Dernier point clé et § Un mot sur le « problème du cadre ».
- Extraits : Points clés, « Le problème du cadre, né en intelligence artificielle, est un cas particulier d’une limite épistémologique générale » ; § 5, « le **problème du cadre** est pris dans un sens épistémologique général, dont la difficulté logique initiale n’est qu’un cas particulier ».
- Question : au § 5, l’expression désigne la limite générale ; dans le point clé, elle désigne la difficulté initiale, qui en est un cas particulier.
- Proposition (Opus B12) : « Le problème du cadre, au sens étroit où l’intelligence artificielle l’a posé, est un cas particulier… ».
- Non appliqué : choix terminologique sur un terme du registre (sens étroit ou large), réservé à l’auteur.

**T4. Le 5 % du navigateur : risque propre ou supplément de risque ?** § Le monde répond à l’action.
- Extrait : « il estime à 5 % le risque de démâter s’il part sur un voilier léger plutôt que sur un voilier renforcé. »
- Lectures : (a) 5 % est le risque de démâter avec le voilier léger ; (b) choisir le léger ajoute 5 points de risque par rapport au renforcé.
- Propositions : Sonnet B1 (lecture a), « s’il part sur un voilier léger (plutôt que sur un voilier renforcé) » ; Opus B1, (a) « s’il choisit le voilier léger plutôt que le voilier renforcé », (b) « il estime que partir sur le voilier léger augmente de 5 points le risque de démâter ».
- Non appliqué : les deux lecteurs voient deux lectures. Le ch. 4 (§ La course à la voile) fixe la lecture (a) : $p$ y est « la probabilité d’échec du voilier léger », et M. X l’estime à 5 % ; le ch. 3 parle aussi de « la probabilité que le bateau casse ». La correction (a) paraît donc sûre sur le fond, mais elle reste à confirmer par l’auteur.

**T5. « Ce choix […] est circulaire ».** § Le cadre comme spécification finie.
- Extrait : « Ce choix précède toute inférence, et il est circulaire [@fauriat2026frame]. »
- Question : un choix n’est pas circulaire ; c’est sa *justification* qui l’est.
- Proposition (Opus C11) : « et sa justification est circulaire ».
- Non appliqué : change l’objet de l’affirmation (fond).

### Deux lectures, portée, terminologie

**T6. « Cette dépendance » ; « se lit à deux niveaux ».** § Le cadre comme spécification finie.
- Extraits : « L’écriture probabiliste rend cette dépendance explicite. » ; « L’@eq:ch02-cond-cadre se lit à deux niveaux [@fauriat2026frame]. […] Mais l’essentiel est décidé avant même d’écrire la somme »
- Question : « cette dépendance » n’a pas de référent net. Les « deux niveaux » sont-ils (a) les lois conditionnelles et les poids (deux composantes, plus un troisième temps, la liste), ou (b) le contenu de la somme et le choix préalable de la liste ?
- Propositions : Sonnet B5, « rend explicite la dépendance de toute prévision à l’égard du cadre » et « comporte deux facteurs » ; Opus B3, (a) « se compose de deux éléments », (b) garder « deux niveaux » et annoncer « au niveau de la somme, puis en amont de celle-ci ».
- Non appliqué : Opus voit deux lectures et ne tranche pas.

**T7. « (c’est le jeu d’étalonnage) ».** Encadré `.formel` « Relativité au cadre… », point 2.
- Extrait : « Ils servent à ajuster un modèle, puis à étalonner un score de non-conformité (c’est le jeu d’étalonnage). »
- Question : le jeu d’étalonnage est-il l’ensemble des $n$ cas, ou seulement ceux qui servent à la seconde étape ?
- Propositions : Sonnet B12, « (les cas utilisés pour cette seconde étape forment le jeu d’étalonnage) » ; Opus B10, « Ces $n$ cas, qui forment le jeu d’étalonnage, servent à… » ou « Une partie d’entre eux sert à ajuster un modèle, l’autre (le jeu d’étalonnage) à étalonner… ».
- Non appliqué : deux lectures aux sens différents (les deux lecteurs ne tranchent pas).

**T8. « Les hypothèses disponibles ».** § Le cadre comme spécification finie.
- Extrait : « Deux analystes qui partagent le même cadre peuvent aboutir à des représentations différentes s’ils pèsent différemment les hypothèses disponibles. »
- Question : hypothèses de modélisation, configurations possibles, données ?
- Proposition (Opus B5) : « s’ils estiment différemment les paramètres ou attribuent des probabilités différentes aux mêmes configurations ».
- Non appliqué : la reformulation fixe une interprétation (le lecteur le signale).

**T9. « Spécification finie » (et « cadre fini » au ch. 4).** Définition du cadre ; titre du § 3.
- Extrait : « Un **cadre** est la spécification finie à l’intérieur de laquelle opère un raisonnement »
- Question : pour un non-mathématicien, « finie » se lit d’abord « achevée », presque le contraire de l’idée (une liste bornée, donc incomplète).
- Proposition (Opus B2) : « la spécification, en nombre fini d’éléments, à l’intérieur de laquelle… » ou « la liste finie… ».
- Non appliqué : définition en gras reprise du registre (« Spécification finie… ») ; le titre de section et le ch. 4 (« un cadre fini ») sont concernés. Voir la liste transversale.

**T10. Jargon de l’encadré formel.** Encadré « Relativité au cadre des garanties déductives et inductives ».
- Extraits : « le critère de *d*-séparation et les règles du *do*-calcul », « une quantité interventionnelle », « un score de non-conformité ».
- Propositions : Sonnet B11, « (d-séparation et do-calcul, deux outils de lecture du graphe) », « score de non-conformité (mesure de l’écart entre prévision et réalité) » ; Opus C17, une incise par terme.
- Non appliqué : une glose de ces termes risquerait d’introduire une affirmation inexacte (un score de non-conformité ne mesure pas toujours un écart entre prévision et réalité). À rédiger par l’auteur si elle est souhaitée. (« Ensemble prédit » a été glosé : EDITS, E5.)

**T11. « Habitudes de codage d’un dossier » avant le cas clinique.** Encadré `.nuance` « Énoncer plus ou taire plus ».
- Extrait : « les facteurs écartés (salinité, pression, habitudes de codage d’un dossier) »
- Question : l’exemple renvoie au cas clinique du § 4, pas encore lu ; il est opaque ici.
- Proposition (Opus B4) : « (salinité, pression, saturation des sols) », ou « (on en verra un exemple clinique plus loin) ».
- Non appliqué : changer l’exemple modifie le contenu ; un renvoi vers l’avant est à décider par l’auteur.

**T12. « Si sa barre casse au large ».** § Le monde répond à l’action, exemple du téléphone satellite.
- Question : la barre est-elle un facteur omis par la représentation (elle listait « l’âge du moteur », non la barre) ou l’une des « avaries » prévues ?
- Proposition (Sonnet B2) : « Si sa barre casse au large (avarie que sa représentation n’avait pas distinguée), ».
- Non appliqué : le sens bouge si la barre est un incident prévu (le lecteur le note lui-même).

**T13. Variables « par omission » ; exemples entre parenthèses.** § Le cadre comme spécification finie, liste des quatre choix, point 1.
- Extrait : « et, par omission, toutes celles que l’on néglige ou que l’on suppose constantes (la pression pour la règle d’ébullition ; pour le navigateur, une fissure cachée dans le mât) »
- Question : la définition de « variables » inclut ce que l’on retient et, « par omission », ce que l’on néglige ; les exemples peuvent se lire comme des variables retenues.
- Propositions : Sonnet B4, « les variables retenues […] ; le choix écarte, en creux, toutes celles que l’on néglige ou suppose constantes (…) » ; Opus C9, « (par exemple, la pression…) » placé juste après « que l’on néglige ».
- Non appliqué : réécriture de structure, au-delà d’une correction locale ; propositions divergentes.

**T14. « Maniables et générales en apparence ».** § Le cadre comme spécification finie.
- Question : « en apparence » porte-t-il sur les deux adjectifs ou sur le seul second ?
- Constat : Opus C13, qui ne tranche pas.
- Non appliqué : deux lectures.

**T15. Tableau, ligne 3, et texte.** @tbl:ch02-eau-bouillante.
- Extraits : tableau, « Eau pure portée à 100 °C à l’air libre $\rightarrow$ ébullition » ; texte, « « si l’on porte de l’eau pure à 100 °C *à l’air libre, sous la pression atmosphérique*, alors elle bout » ».
- Question : le tableau omet « sous la pression atmosphérique », que le texte ajoute à la même étape (il range « valeur de la pression atmosphérique » parmi les conditions encore tues).
- Constat : Opus C6.
- Non appliqué : contenu du tableau ; l’écart est peut-être voulu (la valeur de la pression reste tue à l’étape 3).

**T16. Marqueur `[@A-VERIFIER: Shanahan, « The Frame Problem », SEP]`.** § Un mot sur le « problème du cadre ».
- Question : référence à vérifier (et « SEP » à développer : Stanford Encyclopedia of Philosophy) avant publication.
- Constats : Sonnet B15 ; Opus C20.
- Non appliqué : les marqueurs `A-VERIFIER` sont intouchables pour l’éditeur ; relève de la passe bibliographique.

### Constats rejetés
- Sonnet B3 (« Cette ouverture n’est pas un défaut de méthode ») : le référent est donné par « la liste close » juste avant ; Opus reprend lui-même l’expression sans gêne ; « ouverture de la parenthèse » prêterait à confusion avec le signe « ( ».
- Sonnet B8, B9 et Opus B7 (poutre, « prémisse générale », valide et solide non rappelés) : dépendance légitime ; le ch. 1 donne le syllogisme et la distinction, et le paragraphe y renvoie (@sec:ch01-modes-inference). Un rappel d’une demi-phrase reste possible si l’auteur le souhaite.
- Sonnet B13 (« régression à l’infini » non préparée) : l’expression dit elle-même le report sans terme ; l’ajout n’apporterait rien.
- Sonnet C1 et Opus C2 (deux « ce que » autour de « un cadre ») : les deux lecteurs ont compris ; « façon de découper » et « cadre » sont en apposition, et les propositions divergent sans lever de véritable ambiguïté.
- Sonnet C2 (« dissymétrie ») : terme courant, sens clair.
- Sonnet C3 (« route sèche » et « verglas ») : pas de contradiction ; la plaque de verglas sur route sèche est précisément l’exception tue.
- Sonnet C4 (« ce que chacun en retient ») : une seule lecture.
- Sonnet C5 (« prendre pour elle ») : une seule lecture.
- Sonnet C6 ($B$ non glosé) : glosé au ch. 1.
- Sonnet C7 (« l’objectif qu’il retient » dans la définition) : définition encadrée ; les deux lectures ont le même sens.
- Sonnet C8 (« dans l’analyse et la forme des liens ») : la seconde analyse syntaxique n’est pas plausible.
- Sonnet C9 (rappeler la nature des quatre choix dans l’exemple de la crue) : style.
- Sonnet C10 (puce longue dans la nuance) : style.
- Sonnet C11 et Opus C14 (redites entre le texte et les encadrés) : la redite est voulue par la règle du texte principal.
- Sonnet C12 (titre « La rigueur formelle ne lève pas cette limite ») : titre de section ; aucun contresens signalé par les deux lecteurs.
- Sonnet C14 (« sortir d’une pièce sa batterie ») : construction correcte (complément long rejeté en fin) ; l’apologue est de toute façon à reprendre (T2).
- Opus C1 (« ne valent que « pourvu que » ») : formulation du registre (voir liste transversale).
- Opus C3 (« son prolongement pratique ») : les deux référents donnent le même sens.
- Opus C4 (encadré question : « modèle », « degré de croyance ») : « degré de croyance » est introduit au ch. 1 ; « modèle » est pris au sens courant.
- Opus C5 (couper le paragraphe du mont Blanc) : un seul lecteur ; paragraphe lisible.
- Opus C7 (∩ non glosé) : glosé au ch. 1.
- Opus C8 (« entre… entre ») : répétition mineure.
- Opus C10 (« loi », « partition ») : notions du ch. 1.
- Opus C15 (« dépendance envers ») : tournure admise.
- Opus C16, seconde partie (« lorsqu’elle est présente ») : une seule lecture plausible (la fidélité). (La coupure de paragraphe est appliquée : EDITS, E3.)
- Opus C19 (« toutes » : mesures ou cohortes) : sens identique.

---

## `chapitres/03-mondes-possibles.md`

### Incohérences de fond

**T1. « Lorsque l’estimation est juste ».** Encadré `.exemple-quantitatif` « Ce qu’une seule course dit de deux prévisions », Lecture.
- Extrait : « Une issue à laquelle on donnait 0,1 % se produit en moyenne une fois sur mille lorsque l’estimation est juste »
- Question : « juste » réintroduit l’idée d’une valeur vraie, que le chapitre écarte (« aucune règle de logique ni de probabilité ne permet de déclarer l’un juste et l’autre faux »). Lectures : (a) bien calibrée (fréquence à long terme sur les cas annoncés à 0,1 %) ; (b) égale à une chance objective, ou vraie fréquence de ce type d’avarie.
- Propositions : Sonnet A1 (a), « lorsque l’estimation est bien calibrée » ; Opus A2 (a), « chez un prévisionniste bien calibré ».
- Non appliqué : deux lectures ; incohérence possible avec la thèse. La même expression revient au ch. 4 (« si ses estimations sont justes ») : voir la liste transversale.

**T2. Points clés : « impossible à écarter » et texte : « ne permettent pas raisonnablement d’écarter ».** Deuxième point clé et § Raisonner à l’envers.
- Extraits : Points clés, « chercher quelle variation plausible, ou impossible à écarter, de cet arrière-plan renverserait la conclusion » ; corps, « ou que les éléments disponibles ne permettent pas raisonnablement d’écarter », puis le garde-fou « au motif que rien n’est logiquement impossible ».
- Question : sans « raisonnablement », « impossible à écarter » peut se lire « non exclu logiquement », c’est-à-dire ce que le garde-fou interdit.
- Propositions : Opus A1, « quelle variation plausible, ou que l’on ne peut raisonnablement écarter, de cet arrière-plan… » ; Sonnet C6, « difficile à écarter ».
- Non appliqué : harmonisation d’un critère entre texte et points clés ; la force de l’affirmation du point clé change. La correction d’Opus, alignée sur le corps du texte, paraît être l’intention.

**T3. « Quel bateau il fallait choisir ».** Même encadré, Lecture, fin.
- Extrait : « L’exemple ne dit pas, enfin, quel bateau il fallait choisir : la réponse dépend aussi de ce que coûte une casse et de ce que rapporte une victoire. »
- Question : les deux navigateurs examinent le même voilier ; aucun choix de bateau n’est posé dans le chapitre. Lectures : (a) le choix entre voilier léger et voilier renforcé (posé au ch. 2 et développé au ch. 4) ; (b) le choix de prendre ou non le départ.
- Propositions : Sonnet A2 (b), « s’il fallait prendre le départ […] ce que rapporte l’arrivée » ; Opus B8, (a) « quel bateau il fallait choisir pour la course (voilier léger ou autre) », (b) « s’il fallait prendre le départ avec ce voilier ».
- Non appliqué : deux lectures. Le ch. 4 (« chacun doit choisir entre deux bateaux ») appuie la lecture (a) ; un renvoi au @sec:ch04 lèverait le doute.

**T4. Garde-fou et règle de la probabilité nulle.** § Raisonner à l’envers.
- Extraits : « Raisonner à l’envers ne consiste pas à inventer des scénarios extravagants, comme une météorite qui frapperait la quille, au motif que rien n’est logiquement impossible. » ; « La prudence demande en outre de ne donner une probabilité nulle qu’à ce qui est logiquement exclu ».
- Question : la météorite doit-elle être écartée de l’examen tout en gardant un poids non nul (a), ou recevoir zéro faute d’examen (b) ?
- Proposition (Sonnet B7, lecture a) : ajouter à la règle de prudence « , même si l’on décide de ne pas examiner ces mondes ».
- Non appliqué : fond (deux lectures) ; lié au critère « réellement » ou « logiquement » du ch. 1 (T1 de ce chapitre-là).

**T5. « Une faiblesse constante du raisonnement ordinaire ».** § Prévision et prévisionniste, après l’encadré.
- Extrait : « Elle explique une faiblesse constante du raisonnement ordinaire : une issue sans histoire n’apporte presque aucune information. »
- Question : ce qui suit les deux-points est un fait, non une faiblesse ; la faiblesse (tenir une issue sans histoire pour une confirmation) n’est pas dite.
- Propositions : Sonnet B11, « …du raisonnement ordinaire, qui prend une issue sans histoire pour une confirmation alors qu’elle n’apporte presque aucune information sur le point en litige » ; Opus B9, « …qui tient pour une preuve de sûreté une issue sans histoire, alors qu’une telle issue n’apporte presque aucune information ».
- Non appliqué : ajout d’une affirmation ; Sonnet restreint en outre la portée (« sur le point en litige »).

**T6. Connecteur « donc » avant les règles de score.** § Calibration et historique des prévisions.
- Extrait : « Pour évaluer des prévisions probabilistes dans la durée, il faut donc une manière de les noter qui n’incite le prévisionniste ni à ramener ses chiffres vers la moyenne… »
- Question : le paragraphe précédent montre que la calibration ne suffit pas (absence de discrimination), alors que ce paragraphe-ci porte d’abord sur l’honnêteté des chiffres. Le score répond-il au problème de l’inutilité (a), ou s’agit-il d’un autre point (b) ?
- Propositions : Sonnet B14, « il faut aussi une manière de les noter » ; Opus B11, « il faut une manière de les noter qui récompense cette capacité à distinguer les jours, sans inciter… ».
- Non appliqué : Sonnet voit deux lectures de l’intention ; la proposition d’Opus réordonne le propos.

### Deux lectures, portée, terminologie

**T7. « Ni l’un ni l’autre ».** § Prévision et prévisionniste.
- Extrait : « Avant le départ, lequel des deux a raison ? Ni l’un ni l’autre, et ce n’est pas faute de rigueur »
- Question : la réponse se lit d’abord « tous deux ont tort », alors que la suite dit que la question n’a pas de réponse.
- Propositions : Sonnet B8, « Aucun des deux ne peut être déclaré avoir raison, et ce n’est pas faute de rigueur » ; Opus B7, « La question n’a pas de réponse, et ce n’est pas faute de rigueur ».
- Non appliqué : la réplique est peut-être un effet voulu ; les reformulations en changent la force rhétorique. Correction recommandée par les deux lecteurs.

**T8. « Donner ce rôle au jugement ».** § Raisonner à l’envers.
- Question : « ce rôle » renvoie-t-il au paragraphe précédent (juger quelles variations sont plausibles) ou à la thèse de la section 1 (la probabilité comme poids accordé par une personne) ?
- Propositions : Sonnet B6, « Lire ainsi la probabilité comme un jugement appelle une objection classique » ; Opus B5, « Faire ainsi reposer la probabilité sur un jugement appelle une objection classique ».
- Non appliqué : Opus voit deux lectures.

**T9. « Cette seconde limite. Retenons ici la première ».** § Prévision et prévisionniste, paragraphe de la dinde.
- Question : les deux limites ne sont pas annoncées. Les lecteurs reconstruisent la seconde (le danger absent du cadre) mais divergent sur la première (lenteur de l’accumulation, ou faible pouvoir de départage d’un matin ; le texte qui suit les deux-points dit plutôt la seconde chose).
- Propositions : Sonnet B13, annoncer « deux limites : la lenteur…, puis la condition… » ; Opus B10, « cette seconde limite, un danger absent du cadre. Retenons ici la première, la lenteur avec laquelle les cas s’accumulent : … ».
- Non appliqué : les lecteurs n’identifient pas la première limite de la même façon ; nommer les limites, c’est trancher.

**T10. « Ce qu’il faut protéger autrement ».** § Calibration et historique des prévisions, dernier paragraphe.
- Extrait : « Quant à la manière de séparer, en pratique, ce que l’on peut calibrer de ce qu’il faut protéger autrement, le @sec:ch17 y reviendra. »
- Question : protéger quoi, contre quoi ?
- Proposition (Sonnet B17, Opus C16) : « ce dont il faut se prémunir par d’autres moyens ».
- Non appliqué : les deux lecteurs signalent que le sens peut bouger selon ce que le ch. 17 entend par « protéger ».

**T11. « La lecture comme jugement rend visible… ».** § Raisonner à l’envers, fin.
- Extrait : « la lecture comme jugement rend visible ce qu’un chiffre présenté comme objectif, et qui n’appartiendrait à personne, laisserait dans l’ombre »
- Question : ellipse jugée peu idiomatique par les deux lecteurs ; l’objet de « rend visible » (hypothèses, information, cadre, mondes jugés plausibles ?) reste implicite.
- Propositions : Opus B6, « lire la probabilité comme un jugement rend visibles les hypothèses et l’information qu’un chiffre présenté comme objectif […] laisserait dans l’ombre » ; Sonnet C13, « la lecture en termes de jugement ».
- Non appliqué : « la lecture comme jugement » est l’expression constante du livre (ch. 1) ; préciser l’objet ajoute une affirmation (Opus le note).

**T12. « Une quatrième fois ».** § Raisonner à l’envers.
- Extrait : « raisonner à l’envers ne consiste pas à chauffer une quatrième fois de l’eau pure au niveau de la mer »
- Question : l’ordinal suppose qu’on se souvienne des trois essais du ch. 2.
- Proposition (Sonnet B5, Opus B4) : « à chauffer une fois de plus de l’eau pure… ».
- Non appliqué : touche un nombre. La dépendance est légitime (le renvoi @tbl:ch02-eau-bouillante est dans la phrase) ; correction sans risque de fond si l’auteur l’accepte.

**T13. « Les deux issues n’ont pas le même poids ».** Encadré `.exemple-quantitatif`, Lecture.
- Question : dans tout le chapitre, « poids » désigne la probabilité répartie sur les mondes ; ici, c’est le pouvoir de discrimination d’une issue.
- Proposition (Sonnet B10) : « n’ont pas la même force probante » ; couper la Lecture en trois paragraphes.
- Non appliqué : le lecteur demande de vérifier l’intention ; bloc `.exemple-quantitatif`.

**T14. Les deux navigateurs racontés deux fois.** § Mondes possibles (dernier paragraphe) et § Prévision et prévisionniste.
- Extraits : « Supposons que deux navigateurs inspectent le même voilier léger et lisent le même bulletin. » ; « Deux navigateurs expérimentés, M. X et M. Y, examinent avant le départ le même voilier léger ».
- Question : s’agit-il des mêmes personnes ? Les causes citées diffèrent légèrement.
- Propositions : Opus C4, « Reprenons les deux navigateurs, que nous appellerons M. X et M. Y : … » ; Sonnet C2, unifier les termes ou alléger le § 1.
- Non appliqué : choix de construction.

**T15. Rappel de $X$ et $Y$.** § Mondes possibles, paragraphe « L’@eq:ch02-cond-cadre prolonge la même image ».
- Propositions : Opus B3, « Les variables $X$ retenues dans le cadre (ce que l’on observe) découpent… ; $\Pr(Y \mid X = x)$, la probabilité de l’issue $Y$, pèse… » ; Sonnet B3, rappeler en quelques mots ce que sont $X$ et $Y$.
- Non appliqué : Opus demande de vérifier que « ce que l’on observe » et « l’issue » correspondent aux définitions du ch. 2 (au ch. 2, $X$ désigne les « variables représentées » et $Y$ « une grandeur ou un événement » à prévoir). (La coupure de paragraphe est appliquée : EDITS, E3.)

**T16. « Les mêmes écarts ».** § Calibration et historique des prévisions, paragraphe sur l’historique.
- Extrait : « distinguer deux situations qui produisent les mêmes écarts »
- Question : écarts entre prévisions et fréquences, ou entre prévisions et issues ?
- Proposition (Sonnet B16) : « le même écart entre prévisions et fréquences ».
- Non appliqué : deux précisions possibles.

**T17. « S’y reporter ».** Chapeau.
- Extrait : « Le lecteur qui arrive ici par l’un des parcours de la @sec:ch00-parcours pourra s’y reporter au besoin. »
- Proposition (Sonnet B1) : « pourra, au besoin, se reporter à ces deux chapitres ».
- Non appliqué : le lecteur voit deux lectures (les deux chapitres, ou les définitions citées).

**T18. « Autant que l’aveuglement ».** § Raisonner à l’envers.
- Extrait : « Une liste encombrée d’éventualités gratuites noie l’attention et paralyse l’action autant que l’aveuglement. »
- Lectures : l’aveuglement paralyse aussi l’action, ou la liste nuit autant que l’aveuglement.
- Proposition (Opus C6) : « …noie l’attention et paralyse l’action : elle nuit autant que l’aveuglement. »
- Non appliqué : deux lectures.

### Constats rejetés
- Sonnet B2 et Opus C1 (« mondes possibles » employé dans le chapeau avant sa définition ; granularité des mondes) : le chapeau annonce le chapitre, la définition en gras vient à la section suivante ; la granularité relève de la définition du registre.
- Sonnet B4 et Opus B2 (« une course à 5 % ») : rappel délibéré de l’expression du ch. 2, que la phrase suivante explique (« Le mât tiendra jusqu’à l’arrivée, ou il cassera »).
- Sonnet B3, seconde partie (« pèse des mondes ») : vocabulaire constant du chapitre (« ils pèsent différemment un même arrière-plan »).
- Sonnet B9 (la « cote » d’une prévision contre une autre) : dépendance légitime au ch. 1 (encadré « Score logarithmique et rapport de vraisemblance », et incise ajoutée au ch. 1, EDITS E11).
- Sonnet B12 (« et que le @sec:ch05 étudiera » ; dinde non résumée) : « et que », coordonné à « déjà rencontrée », ne renvoie qu’à la dinde ; l’histoire est au ch. 0.
- Sonnet B15 (« les jours où il pleuvra ») : futur correct dans la relative.
- Sonnet C3 et Opus C5 (« parti retenu », « sollicitation ») : termes français exacts (parti de conception, sollicitation mécanique) ; propositions divergentes.
- Sonnet C4 (« justifier la troisième décimale ») : nombre ; 0,1 % = 0,001, la troisième décimale existe.
- Sonnet C5 (« l’écart n’est donc pas un caprice ») : deux lectures, que le lecteur ne tranche pas ; « donc » conclut correctement le paragraphe sur la cohérence.
- Sonnet C7 (« prompt ») : sens français exact (« prompt à juger »).
- Sonnet C9 (« vers la moyenne » et « à 50 % ») : deux manœuvres distinctes, données en exemples.
- Sonnet C10 et Opus C13 (« strictement propres » ; « pénalité moyenne attendue » et « pénalité espérée ») : « règle de score propre » est le terme français établi ; « moyenne attendue » est la glose courante de « espérée » dans le texte principal.
- Sonnet C11 (redite sur la calibration) : la phrase annonce le second sens (calibration générative, registre, ch. 12) ; utile.
- Sonnet C12 (« calibrer […] une traversée ») : métonymie claire.
- Sonnet C14 (« notamment » dans le premier point clé) : sens clair.
- Opus C3 (« le 5 % du navigateur ») : renvoi explicite au ch. 2 dans la même phrase.
- Opus C7 (sujet de « casser » : le mât ou le bateau) : variation sans ambiguïté sur l’événement défini.
- Opus C8 (« sous la prévision de M. X ») : formulation du registre (score logarithmique) et usage des statisticiens.
- Opus C9 (« qui » rattaché au logarithme ou au rapport) : le calcul lève le doute ; bloc `.exemple-quantitatif`.
- Opus C10 (« il ne fait baisser que d’environ 5 % la cote ») : ajouterait un nombre.
- Opus C12 (couper le paragraphe de la dinde) : un seul lecteur ; voir T9.
- Opus C14 (« gonfler un 75 % en 95 % ») : compréhensible ; style.

---

## `chapitres/04-decider.md`

### Incohérences de fond

**T1. « Moins de quatre points » et « moins d’un centième de point ».** Encadré `.nuance` « Le monde ne consulte pas nos probabilités », 2e paragraphe.
- Extrait : « Pour M. Y, avec un rapport des enjeux de 25, un risque ignoré de moins de quatre points de pourcentage suffirait, s’il était connu, à changer sa décision ; pour le joueur de roulette russe, avec un rapport de 10 000, moins d’un centième de point suffirait. »
- Question : lue littéralement, la phrase dit que *tout* risque ignoré inférieur à quatre points suffirait, ce qui est faux (0,5 point ne changerait rien). Le sens voulu : il suffirait d’un risque ignoré d’à peine quatre points (l’écart entre $p$ et $p^\ast$, soit 3,75 points), et d’un peu moins d’un centième de point pour le joueur.
- Propositions : Sonnet A1, « un risque ignoré de l’ordre de quatre points de pourcentage (l’écart entre 0,1 % et 3,85 %) suffirait […] ; pour le joueur […], un centième de point environ suffirait » ; Opus B9, « un risque ignoré d’à peine quatre points de pourcentage (3,75) suffirait […] ; pour le joueur […], un peu moins d’un centième de point suffirait ».
- Non appliqué : touche des valeurs calculées (et ajouterait 3,75) ; les deux lecteurs relèvent la même erreur logique. Correction prioritaire.

**T2. Le joueur de roulette russe : certitude ou cadre aveugle ?** § La roulette russe… et § La question laissée ouverte.
- Extraits : « Ou bien le joueur est à peu près certain que la chambre placée face au percuteur est vide, au point d’estimer la probabilité d’échec très au-dessous du seuil » ; « Supposons maintenant que la conviction du joueur de roulette russe, qui estime la probabilité d’échec à 0,001 %, vienne d’un cadre où une chambre chargée n’avait pas sa place : aucun des éléments qu’il a retenus ne lui permettait de l’envisager. »
- Question : au § 3, le joueur sait qu’une chambre est chargée et estime qu’elle n’est pas face au percuteur ; au § 5, son cadre n’envisage pas de chambre chargée. Les deux scénarios semblent incompatibles. La certitude du § 3 n’est en outre pas motivée à cet endroit.
- Propositions : Sonnet B7, « Supposons maintenant une variante : le joueur ignore qu’une chambre est chargée » ; Opus B5, « Ou bien le joueur est, à tort ou à raison, à peu près certain que… ».
- Non appliqué : incohérence de fond. L’incise d’Opus change la nuance si l’auteur veut un cas légitime (barillet vérifié).

**T3. « À un tel rapport des enjeux […] deux cas ».** § La roulette russe…, 3e paragraphe.
- Extrait : « À un tel rapport des enjeux, la règle de l’UES n’autorise à presser la détente que dans deux cas. Ou bien le gain en jeu est immense, comme celui de sauver une vie, et le rapport des enjeux cesse d’être démesuré. »
- Question : le premier cas supprime la condition posée (le rapport démesuré) ; la logique se contredit en surface. Contrainte posée par l’enjeu (a) ou par la probabilité (b) ?
- Propositions : Sonnet B3, « Elle n’autorise à presser la détente que dans deux situations : ou bien le gain en jeu est en réalité immense (sauver une vie, par exemple), ce qui change le rapport des enjeux ; ou bien… » ; Opus B4, « Face à une mort possible, la règle de l’UES n’autorise… » ou « Avec une chance sur six, … ».
- Non appliqué : Opus voit deux lectures et ne tranche pas.

**T4. Définition de la décision unique.** § Décider une seule fois ou à répétition, définition en gras.
- Extrait : « Il en va autrement d’une **décision unique**, c’est-à-dire d’une décision prise une seule fois, sans série d’essais comparables, et dont la réponse du monde n’arrive qu’après l’acte. »
- Question : le dernier critère vaut pour toute décision (la section 1 dit qu’une décision se prend « toujours *avant* que le monde ait répondu ») ; il ne discrimine pas. « Prise une seule fois » est circulaire.
- Propositions : Sonnet B5, « …sans série d’essais comparables, et dont la perte éventuelle ne peut être compensée par d’autres cas » ; Opus B7, « …n’arrive qu’après l’acte, trop tard pour être corrigée » (ou garder le critère, redondant, pour rappel).
- Non appliqué : définition en gras qui suit la définition du registre (« Décision prise une seule fois, sans série d’essais, et dont la réponse du monde n’arrive qu’après l’acte ») ; à modifier dans le registre et le chapitre à la fois.

**T5. « Une consolation » : de quoi ?** § Décider une seule fois ou à répétition, ouverture.
- Extrait : « Un lecteur familier des usages statistiques de la théorie de la décision pourrait trouver ici une consolation. »
- Question : l’inquiétude que la consolation apaiserait n’est pas nommée (le risque que l’estimation soit fausse ? la perte $L$ ? le désaccord entre X et Y ?).
- Propositions : Sonnet B4, « pourrait penser qu’une règle fondée sur des probabilités personnelles se justifie malgré tout à la longue » ; Opus B6, « Face au risque que l’estimation soit fausse, un lecteur familier […] pourrait trouver une consolation. ».
- Non appliqué : le référent de l’inquiétude est à fixer ; le sens bouge selon le choix (Opus le note).

### Deux lectures, portée, terminologie

**T6. « Si ses estimations sont justes ».** Même section.
- Extrait : « Si M. Y choisit le voilier léger chaque fois que $p < p^\ast$, et si ses estimations sont justes, ses gains l’emporteront à la longue »
- Question : « justes » = vraies, ou bien calibrées ? (Même problème qu’au ch. 3, T1.)
- Constat : Sonnet C14, qui ne tranche pas.
- Non appliqué : deux lectures ; à harmoniser avec le ch. 3.

**T7. « Dans un monde où M. X avait vu juste ».** § Décider une seule fois ou à répétition, dernier paragraphe.
- Extrait : « Si le bateau arrive intact, M. Y ne saura pas s’il le doit à un gréement sans défaut ou à la chance, dans un monde où M. X avait vu juste. »
- Question : le complément final est elliptique et mal rattaché.
- Propositions : Sonnet B6 (lecture a), « ou à la chance, si M. X avait en réalité raison de craindre la casse » ; Opus B8, « … ou à la chance, au cas où M. X aurait vu juste. ».
- Non appliqué : Sonnet voit deux lectures. La proposition d’Opus, la plus proche du texte, paraît sûre si l’auteur confirme la lecture (a).

**T8. « Pourtant ».** § La course à la voile, avant la liste M. Y / M. X.
- Extrait : « L’@eq:ch04-seuil leur dicte pourtant des décisions opposées : »
- Question : le contraste porte-t-il sur « rien ne permet de dire lequel a raison », ou sur « devant les mêmes faits » ?
- Propositions : Sonnet C1, « La même équation leur dicte pourtant… » ou « Elle leur dicte donc… » ; Opus C7, « Bien qu’ils partent des mêmes faits, l’équation leur dicte… » (seconde lecture).
- Non appliqué : Opus voit deux lectures.

**T9. « Un cadre fini ».** § La question laissée ouverte.
- Extrait : « D’une représentation (@def:representation) construite dans un cadre fini (@def:cadre) »
- Question : « fini » peut se lire « achevé » au lieu de « limité ».
- Proposition (Opus C11) : « un cadre fini, c’est-à-dire limité (@def:cadre) ».
- Non appliqué : lié à la définition du registre (« spécification finie ») ; à traiter avec le ch. 2 (T9).

### Constats rejetés
- Sonnet B1, B8 et Opus B3 (M. X et M. Y, la notation $(\dots)$, « cadre », « calibration », « raisonner à l’envers » non rappelés) : dépendances légitimes aux ch. 1 à 3, avec renvois explicites. L’emploi de $(\dots)$ seul comme nom (« laissé dans $(\dots)$ ») est aussi celui du ch. 3 : voir la liste transversale.
- Sonnet B9, seconde partie (couper le paragraphe des cotes) : un seul lecteur ; la glose de « cote » est appliquée (EDITS, E1).
- Sonnet B10 (« variation cachée » et « risque ignoré ») : « variation cachée » est la formulation du registre (« raisonner à l’envers ») ; les deux expressions ne désignent pas la même chose (la variation produit le risque).
- Sonnet B11 (« on… ses propres probabilités ») : tournure régulière, et formulation du registre (UES).
- Sonnet C2 (« basculer par l’un ou l’autre des deux termes ») : style.
- Sonnet C3 et Opus C3 (« l’origine et l’unité de l’échelle d’utilité sont libres », « rapports entre écarts d’utilité ») : encadré `.outils` ; éclairés par $L/\Delta U$ dans la suite.
- Sonnet C4 (« droite de pente $-1$ ») : la proposition suivante l’explique déjà (« chaque fois que le rapport des enjeux est multiplié par dix… »).
- Sonnet C5 (redite de $p^\ast \approx \Delta U / L$) : redite voulue entre l’encadré et le texte principal.
- Sonnet C6 (UE et UES) : UE est l’utilité espérée d’un acte, UES la règle ; cohérent.
- Sonnet C7 (« victoire », « succès », « navigateurs ») : sens clair.
- Sonnet C9 (imparfait « qu’elle ne jugeait une prévision ») : renvoi au ch. 3, correct.
- Sonnet C10 (« arrêter l’architecture », « le remorquage est dû ») : une seule lecture plausible.
- Sonnet C11 et Opus C13 (« déploiement irréversible ») : vocabulaire du praticien visé ; propositions divergentes.
- Sonnet C12 (« pour y répondre », « nos chiffres d’incertitude ») : une seule lecture ; annonce du ch. 5.
- Sonnet C13 (« la thèse du @sec:ch02 ») : rappelée dans le chapeau et au paragraphe suivant.
- Sonnet C15 (« tenue pour certaine ») : compatible avec l’hypothèse 2 de l’encadré de dérivation.
- Opus C1 (« deux éléments » puis « quatre éléments », « s’y ») : style.
- Opus C2 (« subjective », « propres probabilités », « probabilité personnelle ») : variantes non techniques, sens clair.
- Opus C4 ($L$ de *loss*) : notation fixée par le registre ; ajout d’information.
- Opus C5 (« sollicité près de ses limites ») : terme technique correct.
- Opus C6 (« ce que le monde réserve ») : emploi absolu admis (« ce que l’avenir réserve »).
- Opus C9 (« 0,0100 % ») : valeur affichée du tableau généré.
- Opus C12 (« aucun moyen de le lire ») : métaphore cohérente (lire une valeur dans la représentation).

---

## Points qui concernent plusieurs fichiers ou le livre entier

1. **Critère de la probabilité nulle.** Ch. 1 : « réellement impossible » (texte) et « logiquement impossible » (encadré) ; ch. 3 : « logiquement exclu » (règle de prudence), le garde-fou « au motif que rien n’est logiquement impossible », et le point clé « impossible à écarter ». Il faut un critère unique, et sa compatibilité avec le garde-fou du raisonnement à l’envers (ch. 1 T1 ; ch. 3 T2, T4).
2. **« Estimation juste ».** Ch. 3, encadré : « lorsque l’estimation est juste » ; ch. 4 : « si ses estimations sont justes ». Le ch. 3 refuse par ailleurs de déclarer une estimation « juste ». « Bien calibrée » ou « vraie fréquence » ? (ch. 3 T1 ; ch. 4 T6).
3. **Le choix du bateau et le 5 %.** Ch. 2 : 5 % « s’il part sur un voilier léger plutôt que sur un voilier renforcé » ; ch. 3 : « quel bateau il fallait choisir » ; le ch. 4 fixe la lecture (choix entre voilier léger et voilier renforcé, $p$ = probabilité d’échec du voilier léger). Une décision de l’auteur règle les deux points (ch. 2 T4 ; ch. 3 T3).
4. **« Fini » / « finie ».** Ch. 2 : « spécification finie » (définition en gras, registre, titre du § 3) ; ch. 4 : « cadre fini ». Risque de lecture « achevé » (ch. 2 T9 ; ch. 4 T9).
5. **« Ne vaut que » / « ne valent que « pourvu que » ».** Partie 1 (« Une déduction ne vaut que si ses prémisses sont vraies »), Points clés du ch. 1, chapeau du ch. 2, définition du registre (déduction, induction). Une lecture « validité » serait fausse en logique (partie 1 T1 ; ch. 2, Opus C1 rejeté).
6. **« Problème du cadre » au sens étroit ou large.** Ch. 2 (§ 5 et Points clés), et toute occurrence ultérieure du terme dans le livre (ch. 2 T3).
7. **Cadre et représentation.** Les définitions du registre (représentation : « mesures, catégories, équations, probabilités » ; cadre : « variables, catégories, classe de modèles et objectif ») se recouvrent (catégories, équations) ; à clarifier pour tout le livre (ch. 2 T1).
8. **« L’arrière-plan […] laisse effectivement $B$ se produire ».** Même image au ch. 1 (§ Probabilité conditionnelle) et au ch. 3 (§ Mondes possibles), jugée elliptique (ch. 1 T6).
9. **Notation $(\dots)$ employée seule comme nom** (« reste cachée dans $(\dots)$ », « laissé dans $(\dots)$ ») aux ch. 3 et 4, alors que les ch. 1 et 2 écrivent « l’arrière-plan $(\dots)$ ». Dépendance légitime, mais opaque pour un lecteur qui arrive par un parcours de lecture.
10. **« Conditions tues », « arrière-plan tu », « conditions sous-entendues », « arrière-plan non énoncé »** (ch. 1 à 3, registre des notations) : plusieurs expressions pour une même notion (ch. 1 T13).
11. **« La lecture comme jugement »** (ch. 1, ch. 3) : expression jugée elliptique par les deux lecteurs du ch. 3 ; elle est constante dans le livre, donc à garder ou à changer partout (ch. 3 T11).
12. **« Sous la prévision qui lui attribuait la probabilité… »** (registre, score logarithmique ; ch. 1 et 3) : jugé calqué de *under* par un lecteur de chaque chapitre ; formulation du registre, à revoir là si l’auteur le souhaite.
13. **« Une course à 5 % »** (ch. 2, ch. 3) : expression elliptique relevée au ch. 3, introduite au ch. 2, où la phrase suivante l’explique ; aucune correction au ch. 3, pour garder l’écho.
14. **Correction appliquée de la même façon dans plusieurs fichiers :** « course au large » (ch. 1, E12 ; ch. 3, E4), alignée sur les ch. 2 et 4.
