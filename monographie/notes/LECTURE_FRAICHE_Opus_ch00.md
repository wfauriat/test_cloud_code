# Lecture fraîche — chapitre 0 « Cartographier le terrain »

Lecteur : cultivé, non spécialiste, n'ayant sous les yeux que `chapitres/00-cartographier.md`.

## 1. Ce que j'ai compris (test de lisibilité, 5 lignes)

1. Trois récits (sonde martienne perdue pour une erreur d'unités, avocats piégés par des jurisprudences inventées par une IA, développeurs plus lents avec l'IA qui se croient plus rapides) montrent des erreurs de plus en plus difficiles à localiser.
2. Nous décidons toujours d'après une représentation limitée (un « cadre ») ; les probabilités traduisent un jugement, et toute règle sous-entend un arrière-plan de conditions non dites que le monde, lui, n'ignore pas.
3. Une barre d'erreur ne voit pas ce que le cadre a omis ; seule la confrontation à un comparateur qui « se trompe autrement », comparable, disponible à temps et écouté, arrête une erreur — d'où la faiblesse de l'auto-vérification et des chaînes, et l'intérêt des contrôles croisés.
4. L'informatique classique tenait ses garanties de contrats écrits ; l'IA les sacrifie pour gagner en portée, et l'automatisation enchaîne les étapes, supprime les vérifications humaines spontanées et rend les contrôles dépendants des mêmes modèles : le risque global peut monter même si l'outil s'améliore.
5. Remèdes : marge d'humilité et verrous pour les décisions uniques, bacs à sable pour explorer, quatre questions à poser devant un chiffre, contrôles placés aux points de passage vers l'action ; suivent le plan en cinq parties et huit parcours de lecture.

Le fil général se suit bien ; les points ci-dessous sont des gênes locales.

## 2. Constats classés par gravité

### Gravité A — compréhension compromise ou contresens possible

**A1. § « Ce que nous pouvons encore faire », puce *L'attitude individuelle***
Passage : « notre expérience du monde déborde souvent le cadre du modèle que l'on consulte, à défaut de déborder le nôtre »
Gêne : « à défaut de déborder le nôtre » est opaque (le « nôtre » de quoi ? cadre ? et pourquoi « à défaut » ?) ; le lecteur ne reconstitue pas l'idée, et le passage de « notre » à « l'on » brouille encore le sujet.
Reformulation minimale : « notre expérience du monde déborde souvent le cadre du modèle que nous consultons, même si elle ne déborde pas le nôtre ». Le sens peut bouger : deux lectures plausibles — (a) notre expérience excède le cadre du modèle, même si elle reste prisonnière de notre propre cadre ; (b) elle excède le cadre du modèle plus souvent qu'elle n'excède le nôtre. Je ne tranche pas.

**A2. § « Ce que nous pouvons encore faire », puce *L'organisation collective***
Passage : « protéger la capacité d'évaluation indépendante comme une ressource budgétaire propre qui plafonne le volume de production »
Gêne : on ne sait pas si c'est la ressource qui, par nature, plafonne la production (constat), ou si l'on recommande de régler la production sur cette capacité (prescription), ni ce que « propre » qualifie.
Reformulation minimale : « traiter la capacité d'évaluation indépendante comme une ligne budgétaire à part, et ne pas produire plus que ce qu'elle permet de vérifier ». Le sens peut bouger selon la lecture retenue (constat ou prescription) ; je ne tranche pas.

### Gravité B — gêne réelle

**B1. § « Toute règle cache un arrière-plan ouvert »**
Passage : « l'eau pure, *à la pression atmosphérique ambiante*, bout à 100 °C. Mais si l'on transporte le même récipient ouvert au sommet du mont Blanc, l'eau pure y bout aux alentours de 85 °C. »
Gêne : au mont Blanc la pression est aussi « ambiante » ; beaucoup de lecteurs entendront « ambiante » comme « normale » et ne verront pas en quoi le contre-exemple réfute la règle précisée, ou croiront à une incohérence.
Deux lectures : (a) l'auteur veut que « ambiante » soit justement le mot trop vague que le mont Blanc met en défaut ; (b) il voulait dire « normale (au niveau de la mer) » et le mont Blanc illustre une condition que la règle n'avait pas encore. Reformulation selon (a) : ajouter « … ambiante — c'est-à-dire, pensions-nous, celle de notre laboratoire — » ; selon (b) : « à la pression atmosphérique normale ». Je ne tranche pas.

**B2. § « Toute règle cache un arrière-plan ouvert »**
Passage : « Un second essai échoue à 104 °C avec de l'eau distillée »
Gêne : « échoue » est elliptique ; il faut deviner que l'eau ne bout toujours pas.
Reformulation : « Un second essai, avec de l'eau distillée, ne bout toujours pas à 104 °C ». Sens inchangé.

**B3. § « Décider une seule fois face à des enjeux asymétriques »**
Passage : « à la roulette russe, où la perte est sans commune mesure avec la mise »
Gêne : la formule qui précède oppose perte et *gain* ; « mise » (ce que l'on engage) brouille le parallèle, la mise étant ici précisément la vie.
Reformulation : « où la perte est sans commune mesure avec ce que l'on peut gagner ». Sens inchangé si « mise » voulait dire « enjeu à gagner ».

**B4. § « Décider une seule fois face à des enjeux asymétriques », dernier paragraphe**
Passage : « tandis que le monde ne consulte pas ce chiffre. Il répond selon ce qui est »
Gêne : « Il » a pour antécédent grammatical le plus proche « ce chiffre » (voire « le décideur ») ; le lecteur doit rectifier.
Reformulation : « Le monde, lui, répond selon ce qui est ». Sens inchangé. (Même paragraphe, C : « dont la réponse ne vient qu'après l'acte » — « réponse » de qui ? on ne le comprend qu'à la phrase suivante ; « dont le monde ne donne la réponse qu'après l'acte ».)

**B5. § « Ce que mesure — et ce que tait — une barre d'erreur »**
Passage : « Ce sur quoi toutes les variantes admises s'accordent par construction — parce qu'aucune d'elles ne contient la variable correspondante — ne produit aucun désaccord »
Gêne : tournure abstraite ; « la variable correspondante » renvoie à un facteur omis qui n'a pas encore été nommé.
Reformulation : « Un facteur qu'aucune des variantes admises ne contient ne les fait jamais diverger : il ne produit aucun désaccord… ». Sens inchangé.

**B6. § « Les cinq conditions d'un contrôle », 1er paragraphe**
Passage : « en confrontant l'affirmation produite à un comparateur censé concorder avec elle »
Gêne : « censé concorder » peut se lire comme « dont on attend qu'il soit d'accord » (donc complaisant), alors que l'idée est « qui devrait concorder si l'affirmation est juste ».
Reformulation : « à un comparateur qui devrait concorder avec elle si elle est juste ». Le sens peut bouger légèrement si l'auteur visait autre chose ; à vérifier.

**B7. § « Les cinq conditions d'un contrôle », 2e paragraphe**
Passage : la phrase « Pour qu'un contrôle arrête une erreur, il faut d'abord qu'un comparateur *existe* (…) ; il faut enfin une *prise en compte* effective (…) »
Gêne : une seule phrase d'environ 130 mots porte les cinq conditions, qui sont le cœur du chapitre ; le lecteur perd le compte.
Reformulation : couper en cinq phrases ou en liste numérotée (comme les « trois propriétés » plus loin), sans changer les mots. Sens inchangé.

**B8. § « Pourquoi l'auto-vérification bute sur le cadre »**
Passages : « refaire tourner une simulation avec une autre graine aléatoire » ; « vérifier un calcul par éléments finis à l'aide d'une formule analytique bâtie sur les mêmes idéalisations géométriques »
Gêne : possible dépendance — « graine aléatoire », « éléments finis », « formule analytique », « idéalisations géométriques » ne disent rien au non-spécialiste, qui ne voit plus en quoi ces contrôles sont des copies.
Reformulation : « relancer une simulation en changeant seulement le tirage au hasard » ; « recouper un calcul numérique par une formule simplifiée qui repose sur les mêmes approximations ». Sens inchangé.

**B9. § « Ce que mesure — et ce que tait — une barre d'erreur », 2e paragraphe**
Passage : « ses balayages paramétriques explorent l'incertitude aléatoire »
Gêne : possible dépendance (« balayages paramétriques »).
Reformulation : « en faisant varier ses paramètres, il explore… ». Sens inchangé.

**B10. § « L'informatique classique a gagné ses garanties… », 2e paragraphe**
Passage : « typage, tests, analyse statique ou preuve formelle confrontent le composant à son énoncé »
Gêne : possible dépendance — liste de termes techniques non glosés ; seul « tests » est transparent.
Reformulation : ajouter une glose : « …ou preuve formelle — autant de façons de vérifier le code contre son énoncé — confrontent… ». Sens inchangé.

**B11. § « L'informatique classique a gagné ses garanties… », paragraphe « Dans cette opération… »**
Passage : « elle a migré dans le choix des données d'entraînement, de la fonction de coût et des préférences d'évaluation »
Gêne : possible dépendance (« fonction de coût », « préférences d'évaluation »).
Reformulation : « …de la fonction de coût (ce que l'optimisation cherche à réduire) et des préférences d'évaluation (ce que l'on juge être une bonne réponse) ». Sens inchangé si ces gloses sont justes.

**B12. § « L'informatique classique a gagné ses garanties… », paragraphe « Au sommet de la pile logicielle »**
Passage : « Au sommet de la pile logicielle, avec les grands modèles de langage »
Gêne : possible dépendance ; l'image d'une « pile » de couches, dont les modèles de langage seraient le sommet, n'a pas été posée (elle est implicite dans le paragraphe sur processeur, fichiers, réseau), et « couches basses » arrive ensuite sans préparation.
Reformulation : « Au sommet de cet empilement de couches logicielles, là où se trouvent les grands modèles de langage, … ». Sens inchangé.

**B13. § « L'informatique classique… », dernier paragraphe**
Passage : « Orienter le modèle par des consignes soignées ou par un ajustement sur des préférences humaines »
Gêne : calque (« fine-tuning on human preferences ») et possible dépendance.
Reformulation : « …ou en le réentraînant pour qu'il produise les réponses que des humains préfèrent ». Sens inchangé.

**B14. § « Elle met les étapes en chaîne et exécute les erreurs » (titre)**
Passage : « exécute les erreurs »
Gêne : « exécuter » a aussi le sens de « mettre à mort » ; le titre peut se lire « élimine les erreurs », à contresens. Le corps de la section lève l'ambiguïté, mais tard.
Reformulation : « …et passe à l'acte sur ses erreurs » ou « …et transforme les erreurs en actes ». Sens inchangé.

**B15. § « Elle érode les vérifications humaines », 2e paragraphe**
Passage : tout le paragraphe « En même temps disparaît un indice précieux… … plutôt qu'à la contradiction. »
Gêne : un seul paragraphe enchaîne quatre idées (le signe du doute, l'étude METR, le signal coûteux de la forme, les pièges de la consigne et de la complaisance) ; le rappel de METR, introduit par « d'ailleurs », s'y rattache mal (il porte sur l'impression d'efficacité, non sur le doute d'autrui).
Reformulation : couper avant « Plus largement » et avant « Et même lorsqu'un humain relit ». Sens inchangé.

**B16. § « Elle érode les vérifications humaines », même paragraphe**
Passage : « la qualité de la forme constituait un signal coûteux, donc crédible, de la solidité du fond »
Gêne : « coûteux, donc crédible » suppose connue l'idée de signal coûteux ; le lien logique reste implicite pour le non-spécialiste.
Reformulation : « un signal coûteux à produire — on ne pouvait guère l'obtenir sans avoir compris —, donc crédible ». Sens inchangé.

**B17. § « Elle érode les vérifications humaines », fin du même paragraphe**
Passage : « Et même lorsqu'un humain relit le brouillon du modèle, deux pièges referment le contrôle sur lui-même : la consigne soumise par l'utilisateur transmet déjà son propre cadre à la machine, et l'entraînement des modèles à plaire… »
Gêne : on ne voit pas comment ces deux pièges, qui portent sur la machine, neutralisent la relecture humaine ; « son propre cadre » est ambigu (celui de l'utilisateur ou celui de la consigne).
Reformulation (lecture la plus probable) : « …deux pièges referment le contrôle sur lui-même : la machine part du cadre que l'utilisateur lui a transmis dans sa consigne, et, entraînée à plaire, elle tend à confirmer ce cadre plutôt qu'à le contredire ; le relecteur ne fait donc que retrouver ses propres hypothèses ». Le sens peut bouger : c'est une interprétation à faire valider par l'auteur.

**B18. § « Elle corrèle les angles morts à l'échelle collective »**
Passage : « adopte les mêmes quelques modèles de fondation »
Gêne : calque (« foundation models ») et possible dépendance ; « les mêmes quelques » est aussi peu idiomatique.
Reformulation : « adopte le même petit nombre de grands modèles d'IA ». Sens inchangé (perte du terme technique).

**B19. § « L'énigme arithmétique… », 2e puce**
Passage : « mais ses erreurs ont l'aisance de ses réussites, n'ont pas d'adresse, et ceux qui le relisent consultent le même outil que lui »
Gêne : le « producteur » est-il l'outil d'IA lui-même (« ses erreurs ont l'aisance… ») ou un humain qui s'en sert (« le même outil que lui ») ? Deux lectures plausibles.
Reformulation (si producteur = humain équipé) : « le producteur, désormais assisté d'un modèle, … et ceux qui le relisent consultent le même modèle » ; (si producteur = l'outil) : « …et ses relecteurs s'appuient sur ce même outil ». Je ne tranche pas.

**B20. § « L'énigme arithmétique… », dernier paragraphe**
Passage : « à mesure que le taux d'erreur d'un producteur baisse, une part croissante des alertes d'un contrôleur imparfait sont de fausses alertes »
Gêne : le raisonnement (moins de vraies erreurs à signaler, donc proportion plus forte de fausses alertes) est laissé implicite ; le lecteur non statisticien ne le reconstitue pas.
Reformulation : ajouter « : comme il reste moins de vraies erreurs à signaler, une part croissante… ». Sens inchangé.

**B21. § « Ce que nous pouvons encore faire », 2e paragraphe**
Passage : « engager une architecture critique »
Gêne : formule opaque (architecture de quoi ? s'engager sur un choix de conception ?).
Reformulation : « arrêter la conception d'un système critique ». Le sens peut bouger si l'auteur visait autre chose (architecture logicielle, d'organisation).

**B22. § « Ce que nous pouvons encore faire », puce *Le placement des contrôles***
Passage : « les confier à des relecteurs qui comprennent une couche en dessous de l'interface qu'ils contrôlent »
Gêne : elliptique et dépendant de l'image de la « pile » ; on comprend mal ce que veut dire « comprendre une couche en dessous ».
Reformulation : « …à des relecteurs capables de comprendre aussi ce qui se passe au niveau inférieur à celui qu'ils contrôlent ». Sens inchangé si telle est l'intention.

**B23. § « Architecture de l'ouvrage », dernier paragraphe**
Passage : « un petit nombre d'exemples courants qui s'enrichissent »
Gêne : calque de « running examples » ; en français « courants » se lit « ordinaires, banals », contresens possible.
Reformulation : « un petit nombre d'exemples récurrents » (ou « exemples fils rouges »). Sens inchangé.

**B24. § « Trois récits pour poser le problème », 3e paragraphe**
Passage : « qui travaillaient sur leurs propres dépôts de code »
Gêne : possible dépendance (« dépôt de code ») ; la glose qui suit (« des projets complexes… ») aide mais ne dit pas ce qu'est un dépôt.
Reformulation : « …sur leurs propres projets logiciels : des bases de code complexes qu'ils connaissaient intimement… ». Sens inchangé. (Même terme dans « remanier un dépôt de code », § automatisation.)

### Gravité C — confort / style

**C1. Introduction, dernière phrase** — « Il se referme sur l'architecture des cinq parties » : après « dans le chapitre qui l'introduit », « Il » peut un instant renvoyer à ce dernier chapitre. Reformulation : « Ce chapitre se referme sur… ». Sens inchangé.

**C2. § « Trois récits… », 1er paragraphe** — « avait calculé l'effet de petites poussées de correction » puis « ces impulsions » : le glissement poussée → impulsion n'est pas expliqué. Reformulation : « …l'effet (l'« impulsion ») de petites poussées… ». Sens inchangé.

**C3. § « Trois récits… », 2e paragraphe** — « le tribunal prononça en juin 2023 une amende et d'autres sanctions » : contre qui ? Reformulation : « …une amende et d'autres sanctions contre les avocats ». À vérifier (sanctions éventuellement contre le cabinet).

**C4. § « Trois récits… », encadré** — « l'inversion de signe entre la mesure et l'impression » : tournure mathématique. Reformulation : « au fait que la mesure et l'impression d'experts… vont en sens contraires ». Sens inchangé. (Idem, plus bas, « se trompent sur le signe même de l'effet » — acceptable car expliqué aussitôt.)

**C5. § « Trois récits… », 3e paragraphe** — « essai contrôlé randomisé » : possible dépendance légère ; « Chaque tâche … était tirée au sort pour être accomplie soit avec … » est un peu calqué (« randomly assigned to »). Reformulation : « Pour chaque tâche…, un tirage au sort décidait si elle serait accomplie avec… ou sans eux ». Sens inchangé.

**C6. § « Nous agissons d'après une représentation »** — « Pour répondre à cette question » : deux questions viennent d'être posées. Reformulation : « Pour répondre à cette seconde question ». Sens inchangé.

**C7. § « La mer ne consulte pas nos probabilités »** — « une traversée isolée renseigne sur une prévision, guère sur le prévisionniste » : distinction subtile, puis passage abrupt du voilier à la pluie. Reformulation : « …renseigne sur cette prévision-là, guère sur la fiabilité de celui qui l'a faite. Pour juger celui-ci, il faut… ». Sens inchangé.

**C8. § « Toute règle cache un arrière-plan ouvert »** — « C'est le premier des deux seuls repères symboliques » : « C' » renvoie au schéma sous-entendu, puis la formule utilise « ∩ » (intersection d'ensembles) pour « et », signe qu'un non-spécialiste ne lit pas. Reformulation : « Ce schéma est le premier… » ; et, si possible, préciser « (où ∩ se lit « et ») ». Sens inchangé.

**C9. § « Toute règle cache… », dernier paragraphe** — « pourvu que le contexte futur ressemble au contexte passé sous les rapports retenus » : « sous les rapports retenus » est obscur. Reformulation : « …sur les points que l'on a retenus ». Sens inchangé.

**C10. § « Ce que mesure… une barre d'erreur »** — « en tirant des échantillons par rééchantillonnage » : redondant et technique. Reformulation : « en rééchantillonnant les données ». Sens inchangé. Même section : « ferrure » peut être inconnu (« pièce de fixation métallique, ou ferrure »).

**C11. § « Pourquoi l'auto-vérification bute sur le cadre »** — « Les observations tirées du monde réel échappent en principe à cette clôture » : « clôture » n'a pas été nommée ainsi auparavant. Reformulation : « échappent en principe à ce cercle fermé ». Le même paragraphe enchaîne sans transition la dérive de distribution et la « méta-procédure » : couper avant « Quant à l'espoir… ». « auditer » est un léger anglicisme (« contrôler »).

**C12. § « Chaînes en série et contrôles croisés »** — « que les désaccords soient instruits » : sens juridique rare. Reformulation : « examinés ». Dernière phrase : « Un modèle à qui l'on demande de relire sa propre sortie » — « modèle » a servi jusqu'ici pour des modèles mathématiques ; ici il s'agit visiblement d'un modèle d'IA, que le lecteur n'a pas encore rencontré comme tel dans cette partie. Reformulation : « Un modèle d'IA… ». Sens inchangé si telle est l'intention.

**C13. § « L'informatique classique… »** — « Les tests ne prouvent jamais l'absence d'erreur, mais le geste reste le même : on vérifie d'avance, une fois pour toutes les exécutions » : redit la phrase précédente, et « une fois pour toutes les exécutions » télescope l'expression figée « une fois pour toutes ». Reformulation : « …on vérifie d'avance, une seule fois, pour toutes les exécutions ». Sens inchangé.

**C14. § « L'informatique classique… »** — « on ne répare pas une distribution de probabilité » : pourquoi le modèle « est » une distribution n'a pas été dit ; possible dépendance légère. Reformulation : « on ne répare pas un comportement statistique par une rustine… ». Sens inchangé.

**C15. § « Ce que l'automatisation fait aux contrôles », chapeau** — « L'automatisation agit simultanément sur trois leviers » : un levier est ce qu'on actionne, pas ce sur quoi on agit. De plus « elle corrèle les contrôles restants » devient « corrèle les angles morts » dans le titre de sous-section. Reformulation : « L'automatisation agit de trois façons à la fois ». Sens inchangé.

**C16. § « Elle met les étapes en chaîne… »** — « une trajectoire de douze étapes » ; « Structurellement, … Opérationnellement, … » : calques. Reformulation : « une suite de douze étapes » ; « Dans sa structure… Dans son fonctionnement… ». Sens inchangé.

**C17. § « Architecture de l'ouvrage »** — densité de termes techniques (« règle de Bayes sous forme de cotes », « score logarithmique de surprise », « programmation multiversion », « calibration générative… invention de faits rares », « effondrement du signal par la forme ») : acceptable dans un plan, mais ce sont les passages les moins lisibles pour le public visé. « dérive le seuil de décision $p^\ast$ » : « dériver » est un calque (en français mathématique, « calculer la dérivée ») et $p^\ast$ est un symbole nouveau alors que le chapitre annonçait deux repères seulement. Reformulation : « établit le seuil de décision ». « l'habitude de raisonner à l'envers » reste vague.

**C18. § « Architecture de l'ouvrage »** — « pipelines » : anglicisme non signalé (italique ou « chaînes de traitement », expression déjà employée plus haut).

**C19. § « Architecture de l'ouvrage »** — « cinq questions de contrôle avant l'action » (ch. 18) peut se confondre avec les « quatre questions » vues plus haut ; et « l'accident de la navette *Challenger* » figure parmi les exemples que le lecteur « retrouvera » alors qu'il n'apparaît nulle part dans ce chapitre. Reformulation : « …retrouvera ou découvrira… ». « examen de ses limites de robustesse » : préférer « examen de sa robustesse et de ses limites ».

**C20. Typographie** — « au dehors » (§ « Les cinq conditions ») : la graphie « au-dehors » est plus courante. Le reste (espaces devant « % », « ; », « : », guillemets « »), les italiques des titres d'affaires et de sondes est correct à la lecture du source.

## 3. Appréciation globale

Le chapitre se lit bien dans l'ensemble : la voix est nette, les récits d'ouverture (Mars Climate Orbiter, Mata v. Avianca), les voiliers, l'eau bouillante, la dinde et l'exemple chiffré des deux organisations sont très accessibles et portent réellement l'argument. Les sections les plus accessibles sont « Trois récits », « La mer ne consulte pas nos probabilités », « Décider une seule fois » et « L'énigme arithmétique ».

Les moins accessibles : « Pourquoi l'auto-vérification bute sur le cadre » et « L'informatique classique a gagné ses garanties… », où s'accumule un vocabulaire technique non glosé (graine aléatoire, éléments finis, typage, analyse statique, fonction de coût, pile logicielle) ; la fin de « Elle érode les vérifications humaines » (paragraphe surchargé, pièges de la consigne peu clairs) ; et les puces de « Ce que nous pouvons encore faire », où deux formules (A1, A2) restent indéchiffrables sans l'avis de l'auteur. La section « Architecture de l'ouvrage » est, par nature, une table des matières dense et jargonneuse ; elle reste acceptable si le lecteur accepte de la survoler. La phrase des cinq conditions (B7), centrale, gagnerait beaucoup à être mise en liste.
