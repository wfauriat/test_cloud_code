# Lecture fraîche — Chapitre 11 « Quand la règle est tirée des données »

Lecteur : Opus (première lecture, chapitre seul). Aucun fichier source modifié.

## 1. Résumé de ce que j'ai compris (test de lisibilité)

1. Quand personne ne sait écrire la règle (reconnaître un « 4 », résumer un texte), on la fait apprendre sur des exemples : c'est le composant appris, dont les règles n'existent que dans des paramètres.
2. On y gagne de la portée (des tâches jusque-là hors d'atteinte) et on y perd la garantie préalable et la lisibilité ; la spécification ne disparaît pas, elle passe dans le choix des données et de l'objectif.
3. Un modèle de langage est entraîné à prédire le *token* suivant ; grammaire, faits et raisonnements s'y déposent parce qu'ils améliorent cette prédiction, mais sa compétence n'a pas de frontière nette (étude BCG).
4. Il optimise la plausibilité, pas la vérité : une réponse fausse et fluide n'enfreint aucun contrat et rien ne la distingue en surface (*Mata v. Avianca* ; *Moffatt* ne prouve rien sur les modèles de langage, seulement la responsabilité de l'entreprise).
5. Consignes, RLHF, filtres et tests de référence *orientent* le modèle sans le *spécifier* ; optimiser ces mesures expose à la loi de Goodhart (chien dressé contre disjoncteur câblé).

Le fil général se suit bien ; mon résumé n'a buté que sur les points A ci-dessous.

## 2. Constats classés par gravité

### Gravité A — compréhension compromise ou contresens possible

**A1. § « Le moteur à prédire le fragment suivant » (2e paragraphe)**
« Personne ne saisit dans un tel système les règles de la grammaire, la table des capitales… »
Gêne : « saisir » a deux lectures plausibles, « entrer, taper » (personne n'écrit ces règles dans le système) ou « comprendre » (personne ne comprend ces règles à l'intérieur du système). La seconde contredit l'idée du paragraphe, mais elle vient spontanément.
Reformulation minimale : « Personne n'inscrit dans un tel système les règles de la grammaire… ». Le sens choisi est la lecture « entrer » ; si l'auteur voulait jouer sur les deux sens, la reformulation en efface un.

**A2. § « La spécification passe dans les données » (5e paragraphe)**
« l'ajustement numérique contraint les paramètres à s'accorder aux exemples d'entraînement — ainsi qu'aux échantillons d'essai tirés d'une source semblable — »
Gêne : on lit que les paramètres sont *ajustés* aussi sur les échantillons d'essai, ce qu'un lecteur averti prendra pour une erreur de méthode (on ne s'entraîne pas sur le jeu de test). Deux lectures : (a) les paramètres sont ajustés sur l'entraînement et *contrôlés* sur des essais de même provenance ; (b) le tout est réglé pour réussir sur ces deux ensembles, par exemple via le choix des hyperparamètres. Je ne tranche pas.
Reformulation minimale pour la lecture (a) : « …à s'accorder aux exemples d'entraînement — et on ne les contrôle que sur des échantillons d'essai tirés d'une source semblable — … ».

### Gravité B — gêne réelle

**B1. § « La spécification passe dans les données » (1er paragraphe)**
« l'arrière-plan ouvert d'exceptions étudié dès le @sec:ch02 »
Gêne : la notion n'est pas rappelée et le mot « arrière-plan » reste opaque sans le ch. 2. C'est une possible dépendance.
Reformulation : « l'arrière-plan ouvert d'exceptions étudié dès le @sec:ch02 — ces cas imprévus qu'aucune liste ne parvient à clore — envahissait… ».

**B2. § « La spécification passe dans les données » (5e paragraphe)**
« dès que le contexte se déplace hors de l'échantillon (@sec:ch07), rien dans les poids du modèle n'avertit ni ne borne l'écart »
Gêne : « poids » arrive sans annonce alors que le texte disait jusque-là « paramètres » (puis « coefficients ») ; le lecteur se demande s'il s'agit d'autre chose. « Hors de l'échantillon » sent le calque (*out of sample*). Ces deux mots sont aussi des dépendances possibles du ch. 7.
Reformulation : « …hors des situations couvertes par l'échantillon (@sec:ch07), rien dans les paramètres (ou « poids ») du modèle n'avertit… ».

**B3. § « Le moteur à prédire le fragment suivant » (3e paragraphe)**
« on peut observer cette structure interne se former étape par étape »
Gêne : aucune « structure interne » n'a été nommée avant ; le paragraphe précédent parlait de « régularités » qui « se déposent dans les paramètres ». Le référent du démonstratif est flou.
Reformulation : « on peut observer ces régularités s'organiser en une structure interne, étape par étape… ».

**B4. § « Fluide et faux sans enfreindre aucune règle » (3e paragraphe)**
« Mais dès que la donnée est rare, l'événement particulier ou la question ambiguë, composer un paragraphe bien charpenté, conforme aux usages du genre et assuré dans son ton demeure une suite hautement probable de la consigne. »
Gêne : il y a deux ellipses d'affilée (« l'événement [est] particulier ») et un sujet verbal (« composer ») qui ne peut pas être une « suite » ; on relit la phrase pour la comprendre.
Reformulation : « Mais dès que l'information est rare, l'événement trop particulier ou la question ambiguë, un paragraphe bien charpenté, conforme aux usages du genre et assuré dans son ton, demeure une suite hautement probable de la consigne. »

**B5. § « Fluide et faux… » (4e paragraphe)**
« aucune clause vérifiable en amont n'interdit la fabrication sur la requête suivante »
Gêne : « la fabrication » employé seul est un faux ami (*fabrication* signifie « invention mensongère » en anglais) ; en français on lit d'abord « production industrielle ». Par ailleurs, « requête » vient s'ajouter à « consigne » pour désigner la même chose.
Reformulation : « …n'interdit l'invention de toutes pièces sur la consigne suivante ».

**B6. § « Fluide et faux… » (2e paragraphe) et paragraphe après l'encadré *Mata***
« un programme de navigation comme celui de *Mars Climate Orbiter* » ; « l'équivalent du programme `SM_FORCES` écrivant des livres-force-secondes au lieu de newton-secondes »
Gêne : sans les ch. 8 et 10, la comparaison tombe à plat : on ne sait ni ce que fut l'incident ni ce qu'est `SM_FORCES`. C'est une possible dépendance.
Reformulation : ajouter une incise, « …`SM_FORCES` — le module qui, dans l'affaire *Mars Climate Orbiter*, livrait ses valeurs dans la mauvaise unité — écrivant… ».

**B7. § « Fluide et faux… » (transition avant l'encadré *Moffatt*)**
« Dans les commentaires qui entourent ces affaires, un autre litige survenu peu après… »
Gêne : « ces affaires » est au pluriel alors qu'une seule affaire a été présentée ; le lecteur cherche la seconde.
Reformulation : « Dans les commentaires qui entourent cette affaire, un autre litige… ». Si l'auteur pense aux affaires d'hallucination en général, il faut le dire : « ce type d'affaires ».

**B8. § « Orienter n'est pas spécifier » (3e paragraphe)**
« Même lorsque cet ajustement améliore nettement l'utilité et la prudence apparente d'un système, il procède en entraînant un modèle auxiliaire… puis en déplaçant les poids… »
Gêne : la concession « Même lorsque… » attend une conclusion (« il ne pose aucun contrat ») ; elle débouche sur une simple description du procédé, et le lien logique est à reconstituer.
Reformulation : « …il ne fait qu'entraîner un modèle auxiliaire sur des jugements humains comparatifs, puis déplacer les poids du modèle principal pour obtenir des notes plus élevées. »

**B9. § « Orienter n'est pas spécifier » (paragraphe après l'encadré Goodhart)**
« optimiser des systèmes pour progresser sur une batterie publique finit par mesurer l'adaptation à la forme particulière de cette batterie »
Gêne : le sujet (« optimiser ») ne peut pas « mesurer » ; c'est la batterie, ou son score, qui finit par mesurer autre chose.
Reformulation : « à force d'optimiser des systèmes pour progresser sur une batterie publique, celle-ci finit par mesurer l'adaptation à sa forme particulière… ».

**B10. Même paragraphe**
« — parfois jusqu'à l'imprégnation de variantes voisines — »
Gêne : l'expression est obscure. Deux lectures : (a) des épreuves du test ou leurs variantes proches se sont retrouvées dans les données d'entraînement (contamination) ; (b) le modèle s'imprègne de variantes voisines des épreuves à force d'y être ajusté. Je ne tranche pas.
Reformulation pour la lecture (a) : « — parfois jusqu'à ce que des variantes voisines des épreuves se retrouvent dans les données d'entraînement — ».

**B11. Points clés (dernier point) et corps du § « Orienter n'est pas spécifier »**
« Les consignes, l'ajustement sur des préférences humaines et les tests de référence orientent les distributions du modèle »
Gêne : dans le corps, les tests de référence *mesurent* des taux moyens et servent à piloter ; ce ne sont pas eux qui orientent. Les filtres, eux, ont disparu de la liste. Le point clé ne correspond donc pas au corps du texte.
Reformulation : « Les consignes, l'ajustement sur des préférences humaines et les filtres orientent les distributions du modèle, et les tests de référence n'en mesurent que des moyennes : aucun n'établit d'invariant vérifiable en amont. »

### Gravité C — confort et style

**C1. Introduction**
« pour obtenir un composant appris (@def:composant-appris) » ; « orienter un modèle ne revient jamais à le spécifier »
Gêne : le terme est employé avant sa définition en gras (§ 1) ; il en va de même pour « orienter » (défini au § 4). Le renvoi atténue la gêne, sans plus.
Reformulation : aucune nécessaire si l'usage du livre l'admet ; sinon, « un composant *appris* (défini plus bas) ».

**C2. § « La spécification passe dans les données » (2e paragraphe)**
« on choisit une fonction objectif et une famille de fonctions paramétrées »
Gêne : ce jargon n'est pas glosé pour un lecteur non spécialiste.
Reformulation : « une fonction objectif (la mesure de l'erreur à réduire) et une famille de fonctions paramétrées (un modèle à réglages ajustables) ».

**C3. § « La spécification passe dans les données » (après la définition)**
« le dispositif décrit par la @def:composant-appris repose sur un échange : on achète de la *portée* »
Gêne : la périphrase est lourde, et la « portée » n'est glosée qu'au paragraphe suivant.
Reformulation : « le composant appris repose sur un échange : on achète de la *portée* — l'accès à des tâches jusque-là hors d'atteinte — … ».

**C4. § « La spécification passe dans les données » (6e paragraphe)**
« La question que pose la relecture technique » ; « la règle métier »
Gêne : ces mots sentent le calque (*code review*, *business rule*) et restent du jargon de métier.
Reformulation : « La question que pose la relecture du code » ; « n'énonce pas la règle à appliquer ».

**C5. Même paragraphe (typographie)**
« …la postcondition du contrat ? ». » ; « …hors des données ? ». »
Gêne : quand la citation se termine par un point d'interrogation, on ne met pas de point après le guillemet fermant.
Reformulation : supprimer le point final après « ».

**C6. § « La spécification passe dans les données » (dernier paragraphe)**
« lui demander de cesser d'être ce que l'on a acheté »
Gêne : on ne sait pas trop si « ce que l'on a acheté » désigne le composant lui-même ou la portée.
Reformulation : « lui demander de renoncer à ce pour quoi on l'a choisi ».

**C7. § « Le moteur… » (1er paragraphe)**
« le sommet de la pile logicielle » ; la longue phrase « On découpe… et recommencer. »
Gêne : « pile logicielle » est une possible dépendance (ch. 10). La phrase enchaîne cinq étapes et deux incises, ce qui fait beaucoup.
Reformulation : couper après la définition des *tokens* : « …selon le découpage statistique retenu. Puis on répète la même épreuve… ».

**C8. § « Le moteur… » (2e paragraphe)**
« qu'un modèle qui les capture »
Gêne : calque de *captures*.
Reformulation : « qu'un modèle qui les a intégrées ».

**C9. § « Le moteur… » (3e paragraphe)**
« En projetant les états intermédiaires sur le vocabulaire de sortie » ; « couches du réseau »
Gêne : « états intermédiaires », « couches » et « réseau » sont du jargon sans glose ; on comprend l'idée grâce à l'exemple qui suit.
Reformulation : « En traduisant en mots ce que le réseau calcule à mi-parcours… ».

**C10. Encadré BCG ; § « Le moteur… » (dernier paragraphe) ; § « Fluide et faux… » (5e paragraphe)**
« domaine de compétence du modèle » / « domaine de maîtrise du modèle » ; « tâches » / « mission »
Gêne : le même critère reçoit deux noms différents.
Reformulation : unifier, par exemple « domaine de maîtrise » et « tâche ».

**C11. Encadré BCG**
« remis des productions évaluées environ 40 % plus haut en qualité »
Gêne : la tournure est peu idiomatique.
Reformulation : « remis des productions dont la qualité a été jugée supérieure d'environ 40 % ».

**C12. § « Le moteur… » (dernier paragraphe)**
« Mais cette genèse imprime aussitôt une limite » ; « sans que rien en lui n'avertisse d'avoir franchi une limite »
Gêne : le référent de « cette genèse » est éloigné, puisqu'un encadré s'intercale. Le sujet implicite d'« avoir franchi » est « rien » grammaticalement, alors que le sens vise le modèle.
Reformulation : « Mais cette manière de former le modèle… » ; « sans que rien en lui ne signale qu'il a franchi une limite ».

**C13. § « Fluide et faux… » (1er paragraphe) et § « Orienter… » (1er et 2e paragraphes)**
« consigne (*prompt*) » puis « consignes générales placées en tête d'interaction », « consigne générale »
Gêne : le même mot sert à la requête de l'utilisateur et aux instructions système ; on suit, mais la distinction n'est pas posée. « Table de vérités » évoque par ailleurs la table de vérité des logiciens.
Reformulation : « …de consignes générales (dites *consignes système*) placées en tête… » ; « une table de faits certifiés ».

**C14. § « Fluide et faux… » (2e paragraphe)**
« délivre un résultat erroné »
Gêne : calque (*deliver*).
Reformulation : « fournit un résultat erroné ».

**C15. § « Fluide et faux… » (5e paragraphe)**
« la fluidité de la prose est uniforme entre les réponses justes et les réponses fabriquées »
Gêne : calque (*uniform across*).
Reformulation : « la prose est aussi fluide dans les réponses fabriquées que dans les réponses justes ».

**C16. Transition avant l'encadré *Moffatt***
« invoqué dans le même souffle »
Gêne : en français, on dit plutôt « d'un même souffle ».
Reformulation : « est souvent invoqué d'un même souffle ».

**C17. § « Orienter… » (1er paragraphe)**
« sortent du préentraînement » ; « la tenue des modèles à l'usage »
Gêne : « préentraînement » n'a pas été nommé dans le § 2 et « tenue » est vague.
Reformulation : « tels qu'ils sortent de leur entraînement initial (le *préentraînement*) » ; « le comportement des modèles à l'usage ».

**C18. § « Orienter… » (2e paragraphe)**
« ni précondition ni postcondition opposable au programme »
Gêne : « opposable » est un terme juridique, et « opposable au programme » est étrange.
Reformulation : « ni précondition ni postcondition que l'on puisse vérifier sur le programme ».

**C19. § « Orienter… » (paragraphe après l'encadré RLHF)**
« qu'ils reposent sur des listes de motifs ou sur d'autres classifieurs appris »
Gêne : « d'autres » suppose que les listes de motifs sont des classifieurs, et « classifieurs » n'est pas glosé.
Reformulation : « …ou sur des classifieurs eux-mêmes appris ».

**C20. Paragraphe et encadré Goodhart**
« lorsqu'une mesure devient un objectif à atteindre, elle cesse d'être une bonne mesure » (corps), répété mot pour mot dans l'encadré
Gêne : la redite est immédiate.
Reformulation : dans le corps, « …on se heurte à un mécanisme identifié bien avant l'apprentissage automatique : la loi de Goodhart. »

**C21. § « Orienter… » (avant-dernier paragraphe)**
« celle qui sépare *dresser un chien* et *câbler un disjoncteur* » ; « éprouver ce déclenchement d'avance contre une tolérance écrite »
Gêne : on dit « sépare X de Y », et « contre » est un calque (*against*).
Reformulation : « …sépare *dresser un chien* de *câbler un disjoncteur* » ; « au regard d'une tolérance écrite ».

**C22. Points clés (3e point)**
« ne porte en surface aucune marque d'erreur »
Gêne : le corps précise « prise isolément » et renvoie au ch. 12 pour la comparaison de plusieurs tirages ; le point clé, plus absolu, perd cette nuance.
Reformulation : « …et, prise isolément, ne porte en surface aucune marque d'erreur ».

## 3. Appréciation globale

Le chapitre est bien construit et se lit avec plaisir : la thèse (orienter n'est pas spécifier) est annoncée, illustrée, puis reprise par l'image du chien et du disjoncteur, qui fonctionne très bien.
- **Sections les plus accessibles :** « Fluide et faux sans enfreindre aucune règle » (l'affaire *Mata* est limpide, la nuance *Moffatt* est exemplaire) et la fin de « Orienter n'est pas spécifier » (l'analogie).
- **Sections les moins accessibles :**
  - « Le moteur à prédire le fragment suivant » : ambiguïté de « saisit », jargon du *logit lens*, référent de « cette structure interne ».
  - Le paragraphe sur les deux dérives de Goodhart : syntaxe de « optimiser… finit par mesurer » et « imprégnation de variantes voisines ».
  - Les passages qui supposent les ch. 2, 8 et 10 : arrière-plan d'exceptions, *Mars Climate Orbiter*, `SM_FORCES`.
