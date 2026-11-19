# Lecture fraîche du chapitre 0 (« Cartographier le terrain ») — Sonnet

Lecteur : cultivé, non spécialiste, qui n'a que ce texte sous les yeux. Aucun fichier modifié. Vérification complémentaire sur le fichier lui-même : aucune espace insécable n'y figure (voir C3).

## 1. Ce que j'ai compris (test de lisibilité)

1. Trois histoires (sonde Mars Climate Orbiter, avocats trompés par un modèle de langage, développeurs qui se croient plus rapides alors qu'ils sont plus lents) posent une question : qu'est-ce qui peut encore nous avertir qu'on se trompe ?
2. Nous décidons toujours d'après une représentation (un « cadre ») qui laisse dans l'ombre un arrière-plan de conditions ; le monde, lui, répond à ce qui est, pas à nos probabilités. Pour une décision unique à enjeux asymétriques, il existe un seuil de risque au-delà duquel il vaut mieux renoncer.
3. Une barre d'erreur ne mesure que le désaccord entre alternatives déjà admises. Une erreur n'est arrêtée que par un comparateur qui peut se tromper autrement, comparable, disponible à temps et réellement écouté. Les chaînes en série cumulent les angles morts ; les contrôles croisés en parallèle ne laissent passer que les erreurs communes.
4. L'informatique classique tirait sa fiabilité de contrats écrits vérifiables d'avance, avec une « adresse » pour chaque faute ; les modèles appris ont dépensé cette garantie contre de la portée. L'automatisation met les étapes en chaîne, supprime des vérifications humaines implicites et corrèle les angles morts. Le risque est le taux d'erreur multiplié par la probabilité d'échappement (exemple chiffré : un producteur dix fois plus fiable peut donner un système neuf fois plus risqué).
5. Remèdes : distinguer décisions répétées (calibrer) et décisions uniques (marge d'humilité, verrou) ; explorer en bac à sable ; poser quatre questions à tout chiffre assuré ; agir sur trois niveaux (attitude, placement, organisation). Suivent le plan en cinq parties et huit parcours de lecture.

Bilan : le fil général est compréhensible. Les points flous se concentrent sur quelques phrases elliptiques, sur du jargon d'ingénierie ou d'informatique non glosé, et sur les sections de plan (architecture) très denses.

## 2. Constats classés par gravité

### Gravité A (compréhension compromise ou contresens possible)

**A1. § « Ce que nous pouvons encore faire », 3e niveau (attitude individuelle)**
Passage : « notre expérience du monde déborde souvent le cadre du modèle que l'on consulte, à défaut de déborder le nôtre ».
Gêne : « à défaut de » est employé au sens de « sans pour autant ». Deux lectures plausibles : (a) concessive, notre expérience dépasse le cadre du modèle sans nécessairement dépasser le nôtre ; (b) « à défaut » au sens de pis-aller. La suite (« l'humilité épistémique consiste alors à… ») ne tranche pas.
Proposition (lecture a, sans trancher définitivement) : « notre expérience du monde déborde souvent le cadre du modèle que l'on consulte, même si elle ne déborde pas forcément le nôtre ». Le sens bouge si l'auteur visait (b) ; à confirmer.

### Gravité B (gêne réelle)

**B1. § « Nous agissons d'après une représentation », première phrase**
Passage : « Pour répondre à cette question, il faut repartir de la situation élémentaire… ». Il y a deux questions juste avant (« Que s'est-il passé entre… ? » et « qu'est-ce qui peut encore nous avertir… ? »). « cette question » est flou, et le retour à la situation de l'agent n'est pas annoncé comme un détour. La question « Que s'est-il passé… » ne reçoit de réponse que beaucoup plus loin.
Proposition : « Pour répondre à la seconde question, il faut repartir… ». Deux lectures possibles si l'auteur visait les deux questions ensemble ; alors « Pour répondre à ces questions ».

**B2. § « La mer ne consulte pas nos probabilités »**
Passage : « Qui, de M. X ou de M. Y, avait raison avant le départ ? Ni l'un ni l'autre : chacun a traduit honnêtement… ».
Gêne : « Ni l'un ni l'autre » peut se lire « tous deux avaient tort », alors que le sens est « la question n'a pas de réponse ».
Proposition : « On ne peut pas le dire : chacun a traduit honnêtement… ». Lecture unique ensuite ; le sens ne bouge pas.

**B3. § « Toute règle cache un arrière-plan ouvert », première phrase**
Passage : « Pourquoi deux raisonneurs attentifs peuvent-ils ainsi diverger… ? Parce qu'aucune règle utilisable ne peut énoncer la totalité des conditions nécessaires à sa vérité. »
Gêne : le lien entre la divergence de M. X et M. Y (hypothèses différentes sur la fatigue des matériaux) et l'impossibilité d'énumérer les conditions n'est pas explicité. Le lecteur doit le reconstruire.
Proposition : ajouter un chaînon, par exemple « …peuvent-ils ainsi diverger, chacun retenant d'autres hypothèses de fond ? Parce qu'… ». Sans changement d'argument ; deux reconstructions possibles du chaînon, d'où ma prudence.

**B4. § « Décider une seule fois face à des enjeux asymétriques »**
Passage : « à la roulette russe, où la perte est sans commune mesure avec la mise ».
Gêne : la formule utilise « gain » et « perte » ; « mise » introduit un troisième terme. Le lecteur ne sait pas si « mise » désigne le gain.
Proposition : « sans commune mesure avec le gain espéré ». Le sens risque de bouger si « mise » était voulu comme enjeu ; à confirmer.

**B5. § « Ce que mesure — et ce que tait — une barre d'erreur »; § « Chaînes… »**
Passages : « en tirant des échantillons par rééchantillonnage » ; « ses balayages paramétriques explorent… ». Jargon statistique et d'ingénierie sans équivalent courant. Possible dépendance.
Proposition : « en simulant de nombreux échantillons à partir des données » ; « en faisant varier systématiquement ses paramètres ». Sens inchangé.

**B6. § « Les cinq conditions d'un contrôle », début**
Passage : « Cette évidence apparente tire toute sa force pratique des cinq conditions qu'elle exige simultanément. »
Gêne : les cinq conditions sont des exigences, qui rendent le contrôle difficile ; elles ne lui donnent pas de « force ». Deux lectures : la force vient de ce que ces conditions sont à la fois nécessaires (portée) ou de ce qu'elles sont contraignantes (limite).
Proposition : « Cette évidence apparente ne devient utile en pratique que si cinq conditions sont réunies simultanément. » Lecture « exigence » privilégiée ; l'autre lecture est écartée.

**B7. § « Les cinq conditions d'un contrôle », phrase suivante**
Passage : phrase de près de 200 mots, cinq « il faut… » séparés par des points-virgules, close par « et ce contrôle les laisse toutes passer : pour lui, leur probabilité d'échappement… est de 100 % ». « pour lui » est obscur ; « les » renvoie à une « famille d'erreurs » à peine nommée.
Proposition : couper en liste numérotée (1 à 5) ; fin : « et ce contrôle laisse alors passer toutes les erreurs de cette famille : leur probabilité d'échappement… est de 100 % ». Sens inchangé.

**B8. § « Pourquoi l'auto-vérification bute sur le cadre », 1er paragraphe**
Passage : « refaire tourner une simulation avec une autre graine aléatoire ou vérifier un calcul par éléments finis à l'aide d'une formule analytique bâtie sur les mêmes idéalisations géométriques ». Phrase très longue, jargon enchaîné (graine aléatoire, éléments finis, formule analytique, idéalisations géométriques). Possible dépendance forte.
Proposition : couper après « bogue de programmation » et alléger : « refaire tourner une simulation avec un autre tirage aléatoire, ou recouper un calcul numérique par une formule simplifiée qui repose sur les mêmes hypothèses de forme ». Sens inchangé.

**B9. § « Pourquoi l'auto-vérification… », 2e paragraphe**
Passage : « Les observations tirées du monde réel échappent en principe à cette clôture ». Le mot « clôture » n'a pas d'antécédent (calque probable de closure) ; le paragraphe précédent parle de « copies », de « même source ».
Proposition : « échappent en principe à ce cercle fermé » ou « à cette circularité ». Sens inchangé.

**B10. § même paragraphe**
Passages : « On parlera alors de dérive de distribution » ; « il se heurte à une régression sans fin ». Jargon (distribution shift) ; « régression » peut évoquer la régression statistique. Possible dépendance.
Proposition : « dérive des données (changement de la distribution des données) » ; « régression à l'infini ». Sens inchangé.

**B11. § « L'informatique classique a gagné ses garanties… »**
Passage : « typage, tests, analyse statique ou preuve formelle » ; « le protocole TCP promet que les octets arriveront dans l'ordre ». Jargon informatique non glosé (typage, analyse statique, TCP, octets). Possible dépendance.
Proposition : glose brève, par exemple « (vérifications automatiques de la nature des données, tests, analyse du code sans l'exécuter, preuve mathématique) » ; « un protocole d'Internet (TCP) promet que les données arriveront dans l'ordre ». Sens inchangé.

**B12. § même section, avant-dernier bloc**
Passages : « la certitude préalable n'a pas été perdue par négligence » ; « le choix des données d'entraînement, de la fonction de coût et des préférences d'évaluation ». « la certitude préalable » n'a pas d'antécédent exact (le texte parlait de « garanties », de « vérification en amont ») ; « fonction de coût », « préférences d'évaluation » sont opaques. Possible dépendance.
Proposition : « la garantie obtenue d'avance » ; « du critère que l'on cherche à minimiser pendant l'entraînement, des jugements humains utilisés pour évaluer ». Sens proche mais « préférences d'évaluation » peut viser autre chose ; à vérifier.

**B13. § « Elle érode les vérifications humaines », 2e paragraphe**
Passage : paragraphe de plus de dix lignes, avec une incise sur METR (« L'étude de METR évoquée plus haut montre d'ailleurs… ») qui interrompt le fil « le doute s'efface / la forme ne signale plus la qualité ». La liaison « d'ailleurs » est faible : l'étude porte sur la perception de l'efficacité, pas sur la détection de l'erreur.
Proposition : couper avant « Plus largement » ; retirer ou déplacer la phrase METR (en fin de paragraphe, introduite par « Rappelons que… »). Pas de changement d'argument.

**B14. § même sous-section**
Passage : « deux pièges referment le contrôle sur lui-même : la consigne soumise par l'utilisateur transmet déjà son propre cadre à la machine, et l'entraînement des modèles à plaire à leur interlocuteur les pousse à la complaisance plutôt qu'à la contradiction ». Le premier piège est elliptique : pourquoi est-ce un piège ? « son propre cadre » : celui de l'utilisateur (probable) ou de la machine ? Deux lectures.
Proposition : « la consigne soumise par l'utilisateur impose déjà son cadre à la réponse du modèle, qui répond donc dans ce cadre ». Lecture « cadre de l'utilisateur » retenue ; à confirmer.

**B15. § « Elle corrèle les angles morts à l'échelle collective »**
Passage : « lorsque les textes et les codes engendrés par les modèles retournent alimenter le Web, les dépôts logiciels et la littérature sans mention de leur origine : par ce blanchiment de provenance, dix copies… ». Le lecteur ne voit pas qui consulte ces sources ensuite ni pourquoi cela produit de « faux témoins indépendants ».
Proposition : ajouter « …, de sorte que celui qui cherche ensuite une confirmation y trouve ce qui provient du même modèle : par ce blanchiment… ». Pas de changement d'argument.

**B16. § « L'énigme arithmétique… », seconde puce**
Passage : « mais ses erreurs ont l'aisance de ses réussites, n'ont pas d'adresse, et ceux qui le relisent consultent le même outil que lui ». Trois propositions de statut différent coordonnées ; « ont l'aisance » est elliptique.
Proposition : « mais ses erreurs se présentent avec autant d'aisance que ses réussites et n'ont pas d'adresse, et ceux qui le relisent consultent le même outil que lui ». Sens inchangé.

**B17. § même section, fin**
Passage : « à mesure que le taux d'erreur d'un producteur baisse, une part croissante des alertes d'un contrôleur imparfait sont de fausses alertes ». Affirmation donnée sans le chaînon (les vraies erreurs se raréfient, les fausses alertes demeurent) ; un lecteur non spécialiste peine à l'accepter.
Proposition : « …, puisque les vraies erreurs se raréfient alors que le contrôleur continue de se tromper, une part croissante… ». Sans changement d'argument.

**B18. § « Ce que nous pouvons encore faire », 3e paragraphe**
Passage : « Cette distinction éclaire aussi le rôle de l'exploration. Puisque toute action sur le monde est en même temps une question posée au monde, il est fécond de laisser… explorer librement ». « Cette distinction » (répété/unique) est lointaine ; le « Puisque » donne une prémisse non reliée à la conclusion.
Proposition : « Elle éclaire aussi le rôle de l'exploration : puisque toute action… ». Le lien logique reste à la charge du lecteur ; deux lectures (l'exploration est utile parce qu'elle apprend ; ou parce qu'elle est réversible). Je ne tranche pas.

**B19. § même section, paragraphe « Quant au décideur… »**
Passage : « Quant au décideur, au citoyen ou au responsable à qui l'on remet un chiffre assuré sans ses conditions d'obtention — ce qui revient à lui transférer une responsabilité déguisée en information —, il dispose de quatre questions… ». Sujet « il » rejeté très loin, double incise.
Proposition : couper : « …remet un chiffre assuré sans ses conditions d'obtention. C'est lui transférer une responsabilité déguisée en information. Il dispose pourtant de quatre questions… ». Sens inchangé.

**B20. § même section, 2e puce du remède**
Passage : « des relecteurs qui comprennent une couche en dessous de l'interface qu'ils contrôlent ». Obscur hors du jargon des couches logicielles.
Proposition : « des relecteurs qui comprennent le fonctionnement de l'étape située juste en amont de ce qu'ils contrôlent ». Le sens risque de bouger : « une couche en dessous » peut viser l'amont (producteur) ou un niveau d'abstraction plus bas ; à confirmer.

**B21. § même section, 3e puce du remède**
Passage : puce d'environ dix lignes, quatre mesures, dont « une ressource budgétaire propre qui plafonne le volume de production » et « affiche son statut et ses hypothèses ». « qui plafonne » (sujet ? la ressource ou le budget ?) et « statut » (nouveau ici, redéfini à la fin du chapitre autrement) sont flous.
Proposition : transformer en quatre sous-puces ; « une ressource budgétaire propre, dont la limite plafonne le volume de production ». Sens inchangé ; « statut » à préciser par l'auteur.

**B22. § « Architecture de l'ouvrage », première phrase**
Passage : « Pour établir chacune de ces propositions sans pétition de principe ». Les « propositions » ne sont pas encore numérotées dans le chapitre (elles le seront plus bas, partie 2 : « première proposition », etc.). Le lecteur ne sait pas ce que désigne « ces propositions » : les remèdes ? le diagnostic ?
Proposition : « Pour établir l'ensemble de ces affirmations sans pétition de principe ». Deux lectures possibles (remèdes seuls / diagnostic et remèdes) ; je ne tranche pas.

**B23. § « Architecture », Partie 1**
Passages : « règle de Bayes sous forme de cotes, rapport de vraisemblance, score logarithmique de surprise » ; « l'habitude de raisonner à l'envers » ; « dérive le seuil de décision $p^\ast$ ». Jargon de plan acceptable, mais « raisonner à l'envers » est obscur et $p^\ast$ n'a jamais été introduit (le texte appelait ce seuil « seuil »).
Proposition : « l'habitude de raisonner à partir de l'issue observée pour remonter aux causes » (lecture à vérifier) ; « dérive le seuil de décision (noté $p^\ast$) ». Le sens de « à l'envers » peut bouger ; à confirmer.

**B24. § « Architecture », Partie 3**
Passage : « le lien mathématique entre la calibration générative d'un modèle et l'invention de faits rares ». « calibration générative » est opaque, y compris après l'emploi de « calibration » dans la section sur la mer (qui portait sur des prévisions).
Proposition : « le lien mathématique entre la qualité probabiliste d'un modèle qui engendre du texte et sa tendance à inventer des faits rares ». Le sens risque de bouger ; à confirmer par l'auteur.

**B25. § « Architecture », dernier paragraphe**
Passage : phrase unique d'environ vingt lignes énumérant huit exemples, chacun suivi de trois ou quatre renvois en parenthèse. Illisible à l'oreille.
Proposition : transformer en liste à puces (un exemple par ligne, renvois entre parenthèses). Sens inchangé. Note : « l'accident de la navette *Challenger* » est cité ici alors qu'il n'a pas été mentionné dans ce chapitre (voir C9).

### Gravité C (confort, style)

**C1. Emploi répété de « vis-à-vis » (calque probable de « with respect to »).** « vis-à-vis de la cause d'erreur considérée » ; « Mais vis-à-vis de tout facteur omis » ; « Vis-à-vis des étourderies propres à chaque individu » ; « vis-à-vis de son propre angle mort ». Proposition : varier avec « à l'égard de », « face à », « pour ». Sens inchangé.

**C2. Calques ou tournures anglicisantes isolées.** « le lieu où atterrit l'enquête après coup » (lands) ; « une frontière en dents de scie » (jagged frontier) ; « c'est la figure de l'agent autonome » ; « une trajectoire de douze étapes » ; « un signal coûteux, donc crédible » (costly signal) ; « Opérationnellement » ; « dérive le seuil » (derives). Propositions : « où aboutit l'enquête » ; « une frontière irrégulière » ; « c'est le schéma de l'agent autonome » ; « un enchaînement de douze étapes » ; « un signal onéreux, donc crédible » ; « Concrètement » ; « établit le seuil ». Les sens sont stables.

**C3. Typographie.** Le fichier ne contient aucune espace insécable (0 occurrence) : « 5 % », « 100 °C », « : », « ; », « ? », « ! », « « … » » sont suivis ou précédés d'espaces ordinaires. À vérifier que la chaîne de compilation les rend insécables ; sinon, risques de coupures de ligne entre un nombre et « % » ou avant « : ».

**C4. Jargon mineur (possible dépendance).** « démâter », « barillet », « coulée » (propriétés de l'alliage d'une coulée à l'autre), « sûreté de fonctionnement », « un champ de températures », « utilité espérée subjective », « sous les rapports retenus », « pile logicielle », « ajustement sur des préférences humaines », « instruits » (désaccords instruits). Chacun se devine à peu près par le contexte ; une glose brève ou un synonyme suffirait ponctuellement.

**C5. § « La mer ne consulte pas nos probabilités », fin.** « Pour savoir si une prévision de “70 % de chances de pluie” mesure bien l'incertitude… Seule la répétition permet de juger ainsi celui qui prévoit : on parlera alors de calibration ». « mesure bien l'incertitude » (traduit bien ?) ; « ainsi » et « alors » laissent flou ce que désigne « calibration ». Proposition : « traduit bien l'incertitude » ; « on appellera calibration cette qualité de la prévision ». Sens inchangé.

**C6. Intertitres commençant par « Elle ».** « Elle met les étapes en chaîne et exécute les erreurs », « Elle érode les vérifications humaines », « Elle corrèle les angles morts… » : le pronom perd son référent dans la table des matières. Proposition : « L'automatisation met… ». Sens inchangé.

**C7. § « L'informatique classique… ».** « on vérifie d'avance, une fois pour toutes les exécutions » : « une fois pour toutes » suivi de « les exécutions » est lourd, et la phrase précédente vient de dire que les tests ne prouvent rien. Proposition : « on vérifie d'avance, sans attendre chaque exécution ». Sens inchangé.

**C8. § « Elle érode… ».** « Personne n'avait jamais inscrit cette boucle de rétroaction sur les organigrammes » : « cette boucle » désigne la friction/comparateurs, jamais nommée ainsi. Proposition : « ce mécanisme de rétroaction ». Sens inchangé.

**C9. § « Architecture », dernier paragraphe.** « forger les clés avant d'aborder les serrures » : métaphore dont la signification (théorie générale d'abord, cas de l'IA ensuite) n'arrive qu'à la phrase suivante ; passable. Et *Challenger*, cité en exemple récurrent, n'est évoqué nulle part dans ce chapitre. Proposition (facultative) : une demi-phrase de rappel, ou retirer l'item de la liste.

**C10. § « Trois récits… », Mata v. Avianca, fin.** « Le programme avait fonctionné comme il avait été construit : il avait prolongé le texte soumis par une suite de mots plausible. » « Le programme » (au lieu de « le modèle ») ; « le texte soumis » (par qui ? l'avocat). Proposition : « Le modèle avait fonctionné comme prévu : à partir de la question posée, il avait produit une suite de mots plausible. » Sens inchangé.

**C11. § « Ce que nous pouvons encore faire », 3e niveau.** « Du côté de l'organisation des contrôles, enfin, la défense s'articule sur trois niveaux » alors que le premier niveau est l'attitude individuelle, non l'organisation. Proposition : « Du côté de la défense, enfin, elle s'articule… » Sens inchangé.

**C12. § « Ce que mesure… une barre d'erreur ».** « Tout au plus un facteur omis qui aurait varié pendant la collecte des données s'y glisse-t-il… » : la collecte des données surgit sans préparation. Proposition : « pendant la collecte des données qui alimentent le calcul ». Sens inchangé.

**C13. § « Toute règle cache un arrière-plan ouvert ».** Le symbole ∩ (intersection) pour la conjonction de conditions peut étonner ; pas bloquant puisque la phrase en clair précède. Aucune proposition.

## 3. Appréciation globale

Sections les plus accessibles : « Trois récits pour poser le problème » (récit net, chiffres concrets), « La mer ne consulte pas nos probabilités » et l'exemple de l'eau qui bout (progression pédagogique excellente), les passages sur les deux pompes de secours, sur la dinde et sur les deux organisations imaginaires (calcul expliqué). Les quatre questions et la liste des trois propriétés qui basculent se lisent aussi très bien.

Sections les moins accessibles : « Les cinq conditions d'un contrôle » (phrase fleuve), « Pourquoi l'auto-vérification bute sur le cadre » (jargon d'ingénierie, concepts empilés), « Elle érode les vérifications humaines » (paragraphe trop long, incise METR) et surtout « Architecture de l'ouvrage » (plan très dense, jargon de spécialiste, énumération finale), dont la lecture continue est lourde pour un lecteur grand public. La section « Ce que nous pouvons encore faire » est riche mais comprime plusieurs idées en puces longues (B18 à B21). Le tableau des parcours est clair ; la liste à puces qui le précède fait double emploi avec lui.
