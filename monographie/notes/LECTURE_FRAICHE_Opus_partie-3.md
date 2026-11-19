# Lecture fraîche : partie 3 (introduction de partie)

Fichier lu : `monographie/parties/partie-3.md`, et lui seul.

## Résumé de ce que j’ai compris (test de lisibilité)

Le logiciel classique est digne de confiance parce que chaque couche obéit à un contrat écrit : on peut la contrôler une fois pour toutes, et quand elle défaille, on sait où chercher. Avec l’apprentissage automatique, les règles viennent des données. Il n’y a plus de contrat vérifiable d’avance, et une erreur d’un modèle de langage ressemble à une réponse juste et ne renvoie à aucun endroit à corriger. Il faut donc placer les contrôles autour des tâches vérifiables ou sur chaque sortie. Le chapitre 13 classe les erreurs selon deux questions (la cause est-elle dans le cadre ? un comparateur la signale-t-il ?) et distingue vérification et validation.

Le texte se lit bien dans l’ensemble. Les gênes se concentrent dans les §4 et §5 (chapitres 12 et 13), où plusieurs notions (« cadre », « comparateur ») arrivent sans définition et où deux phrases ont deux lectures possibles.

## Constats

### Gravité A (compréhension compromise ou contresens possible)

**A1. « Il montre qu’un modèle qui reproduit fidèlement la distribution de ses données d’entraînement est conduit à inventer des faits rares. »** (§4)
- Gêne : on peut comprendre « inventer des faits qui sont rares » (produire des faits insolites) ou « inventer quand on l’interroge sur des faits rares », c’est-à-dire peu présents dans les données. Le lien de cause (pourquoi la fidélité à la distribution pousse à inventer) n’est pas donné non plus.
- Proposition : « … est conduit à inventer lorsqu’on l’interroge sur des faits rares dans ses données ».
- Le sens bouge selon la lecture retenue. Je ne tranche pas : c’est à l’auteur de confirmer laquelle des deux lectures est la bonne.

**A2. « La cause de l’erreur se trouve-t-elle à l’intérieur du cadre ou au-dehors ? […] La réponse à la première question est fixée par le cadre et ne peut pas être examinée de l’intérieur »** (§5)
- Gêne : « cadre » n’a pas été défini dans cette partie (possible dépendance à la partie 2). Sans définition, la seconde phrase est obscure : un lecteur ne voit pas ce que veut dire une réponse « fixée par le cadre » qui « ne peut pas être examinée de l’intérieur ».
- Proposition : rappeler en une incise le sens du mot, par exemple « du cadre (l’ensemble des facteurs que le modèle ou la spécification prend en compte) ». La glose est à adapter à la définition de la partie 2. Ma glose n’est qu’une hypothèse, et le sens bouge si elle est fausse.

### Gravité B (gêne réelle)

**B1. « Les observations sur les modèles actuels, appelées à vieillir vite, sont datées »** (§1)
- Gêne : « datées » peut se lire « dépassées », ce qui contredit l’intention visible (« elles portent une date »).
- Proposition : « … sont accompagnées de leur date ». Le sens ne bouge pas si l’intention est bien « porter une date ».

**B2. « et pour peu qu’elle soit appliquée mécaniquement »** (§2)
- Gêne : on peut comprendre « vérifiée par une machine » ou « suivie à la lettre, sans discernement ».
- Proposition : « … pour peu que son respect soit vérifié mécaniquement ». Le sens bouge si l’auteur voulait dire « respectée strictement par le composant ».

**B3. « Il en va encore ainsi lorsqu’un logiciel produit des résultats faux pendant des mois sans qu’aucune alarme ne l’arrête, comme lors de la perte de la sonde *Mars Climate Orbiter*. »** (§2)
- Gêne : on ne voit pas tout de suite ce qui reste vrai (la défaillance a encore une adresse). « encore » peut se lire « de nouveau » ou « même dans ce cas ». L’exemple suppose aussi qu’on connaisse la cause de la perte de la sonde, une confusion d’unités (possible dépendance).
- Proposition : « La défaillance garde une adresse même lorsqu’un logiciel produit des résultats faux pendant des mois sans qu’aucune alarme ne l’arrête, comme lors de la perte de la sonde *Mars Climate Orbiter* (une confusion d’unités entre deux équipes). » Le sens ne bouge pas.

**B4. « Trois choses y basculent ensemble »** (§4)
- Gêne : « basculer » ne dit pas vers quoi. Les trois éléments sont énumérés, mais leur nouvel état n’est donné qu’en partie dans la phrase suivante.
- Proposition : « Trois choses y changent de nature en même temps : … ». Le sens ne bouge pas.

**B5. « Il faut donc reconstruire les contrôles autour des tâches qui admettent un comparateur mécanique, ou bien les placer sur chaque sortie, une à une. »** (§4)
- Gêne : « comparateur mécanique » apparaît ici pour la première fois (possible dépendance). La phrase a aussi deux lectures : (a) limiter l’usage du modèle aux tâches dotées d’un comparateur ; (b) pour ces tâches, reconstruire les contrôles autour d’elles, et pour les autres, vérifier chaque sortie.
- Proposition : « … autour des tâches dont le résultat peut être confronté mécaniquement à une référence (un comparateur), ou bien, à défaut, contrôler chaque sortie une à une ». Le sens bouge légèrement : « à défaut » impose la lecture (b), à confirmer.

**B6. « Les composants appris produisent des erreurs du type le plus délicat : leur cause est interne au cadre, et rien ne les signale. »** (§5)
- Gêne : la phrase suivante (« Aucun contrat […] ne fait entrer dans le cadre un facteur que ce cadre a omis ») laisse penser que les causes extérieures au cadre sont encore plus difficiles à traiter. Le lecteur ne comprend donc pas pourquoi le cas « interne et non signalé » est « le plus délicat ».
- Proposition : préciser le critère, par exemple « du type le plus délicat parmi ceux qu’un contrat pourrait exclure ». Le sens bouge selon ce que l’auteur entend par « délicat ». Je ne tranche pas.

**B7. « quatre sources de comparateurs (un texte fixé à l’avance, ses propres contrôles, un autre raisonneur, le monde) »** (§5)
- Gêne : le référent de « ses » est flou : le composant, le texte, ou celui qui contrôle ?
- Proposition : « les propres contrôles du composant ». Le sens bouge si « ses » renvoie à autre chose, par exemple aux contrôles du raisonneur lui-même.

**B8. « la vérification, qui consiste à résoudre correctement le problème posé […] et la validation, qui consiste à poser un problème assez fidèle à la réalité »** (§5)
- Gêne : la phrase est elliptique. Vérifier, ce n’est pas résoudre mais s’assurer qu’on a bien résolu, et de même pour valider. Lue à la lettre, la vérification devient la tâche du composant lui-même.
- Proposition : « la vérification, qui consiste à s’assurer que le problème posé a été correctement résolu […], et la validation, qui consiste à s’assurer que le problème posé est assez fidèle à la réalité ». Le sens ne bouge pas, sauf si l’auteur désignait bien les tâches elles-mêmes.

### Gravité C (confort, style)

**C1. « Que devient la théorie des contrôles »** (§1) : possible dépendance. On peut confondre avec la « théorie du contrôle » au sens de l’automatique (*control theory*). Une incise renvoyant à la partie 2 lèverait le doute. Pas de reformulation proposée sans connaître le sens voulu.

**C2. « les porte sur l’empilement des couches logicielles »** (§1) : « porter sur » est peu idiomatique au sens de « transposer ». Proposition : « les applique à l’empilement… ». Le sens ne bouge pas.

**C3. « Les consignes, l’ajustement sur des préférences humaines et les tests de référence »** (§3) : possible dépendance. Ce sont des termes de métier (instructions données au modèle, réglage par retours humains, *benchmarks*), compréhensibles à peu près sans définition. Les tests de référence mesurent plus qu’ils n’« orientent » le modèle, ce qui peut surprendre. Pas de reformulation indispensable.

**C4. « suit une frontière irrégulière »** (§4) : l’image (*jagged frontier*) est expliquée par la suite de la phrase. Elle fonctionne.

**C5. « un autre raisonneur »** (§5) : le terme sent le calque (*reasoner*). Proposition : « un autre système (ou une autre personne) qui raisonne ». Le sens bouge un peu si l’auteur vise seulement des machines.

**C6. « lorsque les vérifications humaines s’effacent devant eux »** (§6) : « eux » peut renvoyer aux composants ou aux processus automatisés. Proposition : « devant ces processus ». La différence de sens est faible.

### Typographie

Rien de manifeste : apostrophes typographiques, italique pour le nom de la sonde, ponctuation double correcte.
