# Lecture fraîche — chapitre 8 « Indépendance, chaînes et contrôles croisés »

Lecteur : Opus (première lecture, seul le fichier `chapitres/08-independance-chaines.md` a été lu).

## 1. Ce que j'ai compris (test de lisibilité, 5 lignes)

1. Un contrôle n'est « indépendant » que par rapport à une classe d'erreurs donnée. Plus un comparateur est éloigné de l'affirmation, plus il voit d'erreurs, mais plus il coûte cher à rendre comparable (traduction, écoute). Cette règle est une tendance, pas une loi.
2. Les étapes enchaînées en série (chaîne) cumulent leurs angles morts et ceux des interfaces. Deux composants qui jugent la même question en parallèle (contrôle croisé) ne laissent passer que leur angle mort commun, plus ce que la comparaison ne sait pas exprimer.
3. Le modèle M1 formalise cela ; l'exemple chiffré montre qu'un contrôle par un pair écrase les erreurs locales (21,9 % → 1,43 %), mais qu'un facteur omis partagé de 3 % fixe un plancher que les relectures entre pairs n'abaissent pas.
4. L'expérience de Knight et Leveson (27 programmes, une seule spécification) et la critique de la formule de Levins montrent que la séparation ne suffit pas quand le point de départ est commun.
5. Le blanchiment, c'est-à-dire la perte des conditions d'un résultat quand il change de mains (exemple : Mars Climate Orbiter), détruit la comparabilité et ramène un contrôle croisé à une simple chaîne.

## 2. Constats

Note sur la typographie : le source met une espace ordinaire devant « : », « ; », « ? ». Je suppose que la composition (babel/polyglossia ou filtre pandoc) la remplace par une espace insécable. Je ne la compte donc pas comme une faute. À vérifier seulement si le rendu n'applique pas cette règle.

### Gravité A (compréhension compromise ou contresens possible)

**A1 — Modèle M1, item 2 (§ Chaînes contre contrôles croisés).**
« Un désaccord n'apparaît — et n'arrête une erreur, sous réserve de prise en compte (@def:prise-en-compte) — que si la cause échappe au producteur *et* si le contrôleur ou la comparaison échoue à la faire ressortir »
Problème : la phrase décrit les conditions d'**échappement** (c'est ce que dit la formule $B_1 \cap (B_2 \cup B_{\text{cmp}})$), mais elle les présente comme les conditions d'**apparition d'un désaccord**. Prise à la lettre, elle dit qu'un désaccord n'apparaît que si le contrôleur échoue, ce qui est contradictoire.
Reformulation minimale : « Une erreur passe au travers du contrôle croisé lorsque sa cause échappe au producteur *et* que le contrôleur ou la comparaison échoue à la faire ressortir (même un désaccord exprimé ne l'arrête que sous réserve de prise en compte, @def:prise-en-compte) : ». Le sens mathématique ne bouge pas.

**A2 — § Boîte à outils, paragraphe sur le mode commun.**
« la fiabilité de l'ensemble ne descendra jamais au-dessous du risque porté par la cause partagée »
Problème : on compare une fiabilité à un risque, et le sens s'inverse. L'idée est que la *probabilité d'échec* ne descend pas sous $q$ (ce que dit l'encadré). La fiabilité, elle, ne *monte* pas au-dessus de $1-q$.
Reformulation : « la probabilité d'échec de l'ensemble ne descendra jamais au-dessous du risque porté par la cause partagée ».

### Gravité B (gêne réelle)

**B1 — § Le blanchiment aux interfaces, « Deux cousins proches » et Points clés (incohérence de définition).**
La @def:blanchiment ne parle que de la « perte des conditions d'un résultat ». Mars Climate Orbiter est présenté comme une illustration « de ce que provoque le blanchiment ». Pourtant, la liste suivante range « l'effacement des unités », avec MCO comme exemple, parmi les « cousins » du blanchiment, donc comme un phénomène distinct. Enfin, le dernier point clé définit le blanchiment comme « la perte des conditions, des unités ou de la provenance ». Le lecteur ne sait plus si les unités et la provenance font partie du blanchiment ou s'en distinguent.
Deux lectures sont plausibles et je ne tranche pas :
- (a) le blanchiment au sens large inclut unités et provenance. Il faut alors élargir la définition ou annoncer que les « cousins » sont des formes du blanchiment ;
- (b) le blanchiment se limite aux conditions. Il faut alors présenter MCO comme un « cousin » et retirer unités et provenance du point clé.

**B2 — même passage.** « produisent des effets symétriques aux interfaces »
Problème : rien n'est symétrique ici. Les deux phénomènes sont *analogues* ou *parallèles*, et le texte précise ensuite que le second atteint une autre propriété (le jugement d'indépendance).
Reformulation : « produisent aux interfaces des effets analogues ».

**B3 — § Le blanchiment, notation $A \cap (\dots) \rightarrow B$ (possible dépendance + collision de notation).**
« Reprenons la notation $A \cap (\dots) \rightarrow B$ introduite au @sec:ch01 et au @sec:ch02. »
Problème 1 : le chapitre n'explique pas ce que représente $(\dots)$ (l'arrière-plan implicite ?). Le texte ne commente ensuite que $A$ et $B$. Même problème plus haut, au § Les angles morts : « ce que le cadre (@def:cadre) a laissé dans l'arrière-plan $(\dots)$ », où le symbole est posé sans glose.
Problème 2 : dans ce chapitre, $B$ (avec indice) désigne partout un angle mort ($B_1$, $B_2$, $B_{\text{cmp}}$…). Le même $B$, sans indice, devient soudain « le résultat », ce qui prête à confusion.
Reformulation minimale : ajouter une glose courte, par exemple « (où $(\dots)$ désigne l'arrière-plan resté implicite) », et signaler « ici, $B$ désigne le résultat, et non un angle mort ». Le sens ne bouge pas.

**B4 — § L'indépendance est relative, @prop:independance, 1re phrase.**
« Un comparateur aide contre une classe d'erreurs dans la mesure où leur cause l'affecte autrement que l'affirmation contrôlée. »
Problème : « aider contre » est un calque (*helps against*). De plus, « leur » (les erreurs) et « l' » (le comparateur) s'enchaînent, ce qui oblige à relire.
Reformulation : « Un comparateur protège contre une classe d'erreurs dans la mesure où la cause de ces erreurs l'affecte autrement qu'elle n'affecte l'affirmation contrôlée. »

**B5 — § L'indépendance est relative, 1er paragraphe.**
« une tension apparaît avec une autre des cinq conditions du @sec:ch06 […] : la comparabilité »
Problème : « une autre » suppose que l'indépendance est l'une des cinq conditions. Or la liste rappelée en introduction ne contient pas le mot « indépendance », seulement « se trompe autrement ». Le lecteur doit deviner que les deux notions sont la même.
Reformulation : « une tension apparaît entre cette condition — se tromper autrement — et une autre des cinq conditions […] : la comparabilité ».

**B6 — § L'indépendance est relative, après la liste sur la ferrure.**
« Ce dernier point illustre d'ailleurs une subtilité capitale de la @prop:independance : la relation entre indépendance et coût est une tendance forte, non une loi sans exception. »
Problème : le dernier point de la liste (essai en brouillard salin, question du chimiste) ne dit nulle part que l'un de ces comparateurs serait bon marché. Le lecteur ne voit donc pas en quoi il illustre une *exception*. Le lien n'apparaît qu'en lisant l'encadré suivant (la « question naïve »).
Reformulation minimale : « Ce dernier point appelle une précision : la question du chimiste, contrairement à l'essai de vieillissement, ne coûte presque rien à poser ; la relation entre indépendance et coût est donc une tendance forte […] ». *Attention, cela ajoute une affirmation.* Si l'auteur ne la fait pas sienne, il suffit de remplacer « illustre » par « invite à préciser ».

**B7 — § L'indépendance est relative, paragraphe Levins (fait à vérifier).**
« Mais Elliott Orzack et Steven Sober [@orzack1993] »
Problème : les prénoms semblent intervertis. L'article de 1993 est, à ma connaissance, de Steven H. Orzack et Elliott Sober. Un lecteur qui les connaît trébuchera.
Reformulation : « Steven Orzack et Elliott Sober ».

**B8 — même paragraphe.** « le génie logiciel critique »
Problème : calque de *safety-critical software engineering*. En français, on peut comprendre « le génie logiciel qui exerce une critique ».
Reformulation : « le génie des logiciels critiques (ceux dont une défaillance met en jeu la sécurité) ».

**B9 — § L'indépendance est relative, copie exacte.**
« et ne contrôlent rien l'une chez l'autre (à peine une panne matérielle fugitive) »
Problème : « à peine » se lit comme « presque pas », alors que le sens voulu semble être « tout au plus ».
Reformulation : « (tout au plus une panne matérielle fugitive) ».

**B10 — § Composer des étapes spécialisées, 3e paragraphe.**
« tandis que les résultats intermédiaires circulent toujours plus vite d'un maillon au suivant »
Problème : l'idée de vitesse croissante arrive sans préparation, et « tandis que » n'indique pas le lien logique avec le morcellement. Deux lectures sont plausibles : « de plus en plus vite avec le temps » (tendance historique) ou « vite, sans être réexaminés ». Je ne tranche pas.
Reformulation (lecture 2) : « et les résultats intermédiaires passent d'un maillon au suivant sans y être réexaminés ». Le sens change selon la lecture retenue.

**B11 — § Le blanchiment, encadré Mars Climate Orbiter.**
Problème : la chaîne causale entre l'erreur d'unité et la trajectoire trop basse n'est jamais énoncée. Le lecteur doit inférer que la navigation a sous-estimé, d'un facteur 4,45, l'effet des poussées, d'où une orbite mal prédite.
Reformulation (une phrase à ajouter en fin de 2e paragraphe, si l'auteur l'accepte) : « Les navigateurs ont donc sous-estimé l'effet cumulé de ces poussées, et la trajectoire réelle s'est écartée de celle qu'ils prédisaient. » *Cela ajoute du contenu factuel : à valider.*

**B12 — § Chaînes contre contrôles croisés, exemple quantitatif (vocabulaire flottant).**
Pour la même notion, on lit : « erreur propre », « erreur indépendante », « erreur locale », « part indépendante », « composante indépendante ». Pour le contrôleur, on lit « oubli », « défauts d'attention » (@prop:chaines), « laisse échapper » (M1). « Erreur indépendante » est ambigu : indépendante de quoi ?
Reformulation : fixer un terme, par exemple « erreur locale » pour $p$ et « probabilité d'oubli $m$ » pour le contrôleur, puis s'y tenir. Le sens ne bouge pas.

**B13 — § Deux précisions (encadré nuance), 1er paragraphe.**
« ne nuit qu'aux erreurs que le producteur n'a pas su éviter ni retenir lui-même »
Problème : « retenir » peut se lire « garder, mémoriser » au lieu de « intercepter ».
Reformulation : « ni intercepter lui-même ».

### Gravité C (confort, style)

- **C1 — § Boîte à outils.** « À mesure que le nombre $N$ d'étapes s'allonge » : un nombre ne s'allonge pas. Proposition : « À mesure que la suite de $N$ étapes s'allonge » ou « que le nombre $N$ d'étapes augmente ».
- **C2 — Encadré outils.** « supposées indépendantes » porte sur les probabilités $p_1, \dots, p_N$ : ce sont les *défaillances* qui sont indépendantes. Proposition : « les défaillances étant supposées indépendantes dans un premier temps ».
- **C3 — Encadré outils.** « soit $1 - (1 - p)^N \approx Np$ » : « soit » est elliptique. Proposition : « la probabilité d'échec vaut $1 - (1-p)^N \approx Np$ au premier ordre ». Dans le même encadré, « taux d'échec individuel $p$ » alterne avec « probabilité d'échec » : garder « probabilité ».
- **C4 — § Les angles morts, dernier paragraphe.** « Deux conséquences suivent immédiatement de la @def:angle-mort » : la seconde (l'angle mort de la comparaison) ne découle pas de la définition, c'est un ajout. Proposition : « Deux remarques suivent ». Autre point : « $B_{\text{cmp}}$ […] (introduit dans le modèle formel de la @sec:ch08-chaines-controles) » alors que la notation est posée ici même. Proposition : « (repris dans le modèle formel…) ».
- **C5 — § L'indépendance est relative.** Passage soudain au « vous » (« votre cadre », « vos chiffres ») dans un texte jusque-là impersonnel ou au « nous ». Le passage est acceptable, mais il surprend.
- **C6 — même §.** « risquent d'être écartées faute de terrain commun ou de prise en compte » : écartées faute de prise en compte, la formule est circulaire. Proposition : « faute de terrain commun ou faute d'être réellement prises en compte ».
- **C7 — Tableau des comparateurs.** « Erreurs de forme du modèle, dans les variables partagées » reste obscur pour un non-spécialiste. Proposition : « Erreurs dans la forme des équations, limitées aux variables communes aux deux modèles ».
- **C8 — § Ferrure.** « Plaçons la ferrure […] sur le @tbl:ch08-comparateurs » : ce sont les comparateurs qu'on place, pas la ferrure. Proposition : « Situons sur le @tbl:ch08-comparateurs les comparateurs possibles de la ferrure ». Toujours dans la 1re puce, « demeure, lui aussi, bloqué au niveau des méthodes partageant le même modèle » : l'image n'est pas claire. Proposition : « reste, lui aussi, aveugle à la corrosion, puisqu'il partage le même modèle ».
- **C9 — Paragraphe Levins.** « formulait l'espoir de la multiplicité des modèles » → « formulait l'espoir placé dans la multiplicité des modèles ». « ne se corrigent mutuellement *que pourvu qu'ils* ne partagent pas » → « ne se corrigent mutuellement *qu'à condition de ne pas partager* ».
- **C10 — § Chaînes contre contrôles croisés.** « les angles morts s'additionnent » alors que la proposition et M1 parlent de réunion ($\cup$). Proposition : « les angles morts se cumulent ».
- **C11 — même §.** « On croit souvent dresser un contrôle croisé » → « mettre en place un contrôle croisé ».
- **C12 — M1, item 3.** « (prise en compte égale à $1$) » suppose une prise en compte chiffrée qui n'a pas été définie dans ce chapitre (possible dépendance, @def:prise-en-compte). Proposition : « (chaque désaccord étant toujours pris en compte) ».
- **C13 — Légende de @fig:ch08-chaine.** « la probabilité d'échec reste à $4{,}39\,\%$ » : « reste » suggère que la valeur n'a pas bougé, alors qu'elle remonte depuis 1,43 %. Proposition : « remonte à $4{,}39\,\%$ ».
- **C14 — Lecture de l'exemple quantitatif.** « une différence modeste au regard du bruit des erreurs locales » : « bruit » est impropre (il s'agit du poids des erreurs locales). Proposition : « au regard du poids des erreurs locales ». Plus loin, dans « ne permet pas d'abaisser ce plancher », le référent de « ce plancher » est flou : est-ce $q = 3\,\%$ ou 4,39 % ? Proposition : « ce plancher fixé par $q$ ».
- **C15 — Encadré « Deux précisions », 2e paragraphe.** « l'angle mort de la comparaison $B_1 \cap B_{\text{cmp}}$ » : ailleurs, « angle mort de la comparaison » désigne $B_{\text{cmp}}$ seul. Proposition : « la part de l'angle mort due à la comparaison, $B_1 \cap B_{\text{cmp}}$ ».
- **C16 — § Le blanchiment.** « ces conditions restent sur la rive : seul $B$ passe la frontière » : la métaphore est mêlée (rive / frontière). Proposition : « seul $B$ traverse ».
- **C17 — Encadré MCO.** « l'incompatibilité des grandeurs » : la grandeur (l'impulsion) est la même, ce sont les *unités* qui diffèrent. Proposition : « l'incompatibilité des unités ». Au paragraphe suivant, « une poussée exprimée en unités anglo-saxonnes contredit le Système international » → « contredit la spécification, qui imposait le Système international ».
- **C18 — Points clés, 3e puce.** « compte tenu des écarts que la comparaison ne sait pas exprimer » est vague. Proposition : « augmentée des écarts que la comparaison ne sait pas exprimer ».

## 3. Appréciation globale

Le chapitre est bien construit. La progression (outillage de fiabilité, angles morts, indépendance relative, chaîne contre croisé, blanchiment) est annoncée puis tenue, et les exemples (ferrure, multiphysique, Knight-Leveson, MCO) sont bien choisis.

**Sections les plus accessibles :**
- la boîte à outils série/parallèle (sauf la confusion fiabilité/risque, A2) ;
- l'encadré Knight-Leveson ;
- le récit multiphysique du blanchiment.

**Sections les moins accessibles :**
- l'encadré formel M1, à cause de la phrase de l'item 2 qui contredit sa formule (A1) ;
- l'exemple quantitatif, où le vocabulaire flotte (« erreur propre/locale/indépendante », B12) ;
- la fin du § Le blanchiment, où le statut des unités et de la provenance (blanchiment ou « cousins » ?) est incohérent avec la définition et les points clés (B1).

Le passage du tableau des comparateurs à la nuance « tendance, pas loi » demande aussi au lecteur un raccord qu'il doit faire seul (B6).
