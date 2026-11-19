# Lecture fraîche — chapitre 13 « Synthèse : deux axes et quatre sources de comparateurs »

Lecteur : Opus (première lecture, seul le fichier `chapitres/13-synthese-deux-axes.md` a été lu).

## 1. Résumé de ce que j'ai compris (test de lisibilité)

1. Le chapitre remplace le classement des incertitudes selon le cadre (dedans / dehors) par une matrice à deux axes : le lieu de la cause (dans le cadre ou hors du cadre) et la présence ou l'absence d'un comparateur qui contredit (erreur signalée / silencieuse).
2. On ne peut pas changer de ligne de l'intérieur du cadre, mais on peut changer de colonne en ajoutant des comparateurs qui se trompent autrement. Le formalisme agit sur la colonne, jamais sur la ligne.
3. Les composants appris remplissent la case « dans le cadre et silencieuse ». Un composant spécifié peut la vider à l'avance grâce à son contrat, ce qui ne veut pas dire qu'il la vide par nature.
4. Les comparateurs ont quatre sources : un énoncé fixé à l'avance, vos propres contrôles, un autre raisonneur et le monde. L'automatisation les transforme inégalement : un contrôle mécanique peut être reconstruit autour d'une tâche (Lean, Simplex), le repère personnel s'efface, les seconds avis sont corrélés, et l'épreuve physique reste lente.
5. La distinction vérification / validation recoupe la matrice : la génération abondante aide la vérification là où un contrôle mécanique indépendant existe, mais ne fait pas avancer la validation, qui exige un contact avec l'extérieur du cadre.

Le fil principal se suit bien. Les gênes viennent surtout du vocabulaire spatial (ligne, colonne, case), employé dans deux tableaux différents, et de quelques passages où l'on ne sait pas si un apport extérieur fait « monter » l'erreur ou la fait « passer à gauche ».

## 2. Constats classés par gravité

### Gravité A (compréhension compromise ou contresens possible)

**A1. § Deux axes (puces après le tableau) : qu'est-ce qui fait « remonter » une erreur ?**
- Passage 1 : « Aucune méthode interne […] ne fait remonter une erreur de la ligne du bas vers la ligne du haut. Une pertinence nouvelle ne peut entrer que du dehors, par l'avertissement d'un tiers ou par l'épreuve du réel ».
- Passage 2 : « le regard d'une autre discipline ou une mesure de terrain indépendante rend visible une omission du cadre » (présenté comme un mouvement de droite à gauche).
- La gêne : le premier passage laisse entendre qu'un apport extérieur fait monter l'erreur (la cause entre dans le cadre). Le second présente le même apport comme un passage vers la gauche, sur la ligne du bas (l'erreur devient signalée sans que la cause change de ligne). La légende de la figure, qui ne montre « aucune flèche montante », renforce le doute.
- Deux lectures plausibles : (a) l'apport extérieur fait d'abord passer l'erreur à gauche ; le cadre ne s'élargit (montée) que si cet apport est pris en compte ensuite. (b) L'apport extérieur fait monter l'erreur directement. Je ne tranche pas.
- Reformulation minimale, selon (a) : « Une pertinence nouvelle ne peut entrer que du dehors […] : elle rend d'abord l'omission signalée, et c'est seulement en révisant le cadre qu'on la fait remonter. » Selon (b), il faudrait préciser dans la seconde puce que le regard extérieur fait aussi changer de ligne. Le sens change selon la lecture retenue.

**A2. § Vérification et validation, avant-dernier paragraphe**
- Passage : « Là où le goulot d'étranglement principal tient à la *vérification* face à un comparateur mécanique rapide et peu coûteux ».
- La gêne : un contrôle rapide et peu coûteux n'est pas un goulot d'étranglement. La phrase semble se contredire.
- Lecture probable : là où l'essentiel de la difficulté relève de la vérification, et où un comparateur mécanique rapide existe.
- Reformulation : « Là où l'essentiel de l'exigence relève de la *vérification* et où l'on dispose d'un comparateur mécanique rapide et peu coûteux — […] — ». Le sens ne devrait pas bouger.

### Gravité B (gêne réelle)

**B1. § Quatre sources, phrase d'annonce avant les sous-sections**
- Passage : « Examinons chacune de ces quatre lignes ».
- La gêne : dans ce chapitre, « ligne » désigne partout une ligne de la matrice (lieu de la cause). Il s'agit ici des lignes du second tableau, ce qui crée une collision de sens.
- Reformulation : « Examinons chacune de ces quatre sources ».

**B2. § Deux axes, seconde puce**
- Passage : « *La colonne dépend de ce qui entoure l'affirmation, et peut se concevoir.* »
- La gêne : « se concevoir » se lit d'abord comme « est imaginable ». Le sens voulu, confirmé par les points clés (« peut être conçue »), est « peut être aménagée délibérément ».
- Reformulation : « et peut être conçue délibérément. »

**B3. § Deux axes, tableau, cellules de la ferrure**
- Passages : la cellule « Cause hors du cadre / signalée » donne « le chimiste de la corrosion interrogeant l'atmosphère de service de la ferrure ». La cellule « Cause hors du cadre / silencieuse » donne « corrosion marine de la ferrure avant rupture ».
- La gêne : le même cas apparaît dans deux colonnes, sans que le texte dise que la différence tient à la présence ou à l'absence du chimiste. Le lecteur peut croire à une contradiction.
- Reformulation : ajouter dans la cellule de droite « (faute de spécialiste consulté) », ou bien, dans le paragraphe qui suit le tableau, une phrase indiquant qu'un même cas peut changer de colonne. Le contenu reste le même.

**B4. § Le monde, premier paragraphe, comparé au § Deux axes et au § Vérification et validation**
- Passage : « C'est la seule source capable, sous les conditions de la @prop:cause-commune, de démentir un cadre tout entier ».
- La gêne : ailleurs, « l'avertissement d'un tiers » et « le regard d'une autre discipline » sont présentés comme l'autre voie d'entrée d'une pertinence nouvelle. Le mot « seule » semble contredire ces passages.
- Deux lectures plausibles : (a) un tiers peut signaler une omission mais seul le monde la *dément* ; (b) imprécision, l'autre raisonneur extérieur compte aussi. Je ne tranche pas.
- Reformulation selon (a) : « C'est la seule source capable de *démentir* un cadre tout entier — un tiers peut le mettre en doute, seul le monde le réfute — ». Selon (b) : « C'est, avec le regard extérieur d'un autre raisonneur, la source capable de… ». Le sens change selon la lecture retenue.

**B5. Points clés, troisième puce**
- Passage : « dans les deux cas, le formalisme déplace la colonne, jamais la ligne ».
- La gêne : « les deux cas » renvoie aux composants appris et aux composants spécifiés, alors que le corps du texte dit qu'un composant appris n'a pas de spécification formelle. Par ailleurs, le corps ne dit pas que le formalisme déplace la colonne partout, mais « sur la ligne du haut », en facilitant seulement *indirectement* les objections sur la ligne du bas.
- Reformulation : « ; de manière générale, le formalisme déplace la colonne (sur la ligne du haut), jamais la ligne. »

**B6. Points clés, cinquième puce, comparée au § Vérification et validation**
- Passage : « la validation […] ne s'automatise pas et reste liée au contact avec le monde ».
- La gêne : le corps du texte dit que la validation exige « le regard d'une autre discipline ou la confrontation avec le monde réel ». Le point clé omet la première voie.
- Reformulation : « reste liée à un apport extérieur au cadre — autre discipline ou contact avec le monde. »

**B7. § Quatre sources : à qui renvoie « vos » ?**
- Passages : dans le tableau, pour les composants spécifiés : « Préservés : quelqu'un a dû écrire les règles ». Dans la sous-section : « celui qui rédige les règles […] dépose en lui un comparateur personnel ». Puis : « L'utilisateur qui n'a pas encore arrêté sa propre estimation ».
- La gêne : le « vous » de « vos propres contrôles » désigne tantôt l'auteur des règles, tantôt l'utilisateur de la sortie. Le lecteur ne sait pas si la comparaison porte sur la même personne.
- Reformulation : préciser une fois, dans la définition de la source 2, « vos propres contrôles (ceux de la personne qui produit ou utilise le résultat) ». Si l'auteur visait seulement l'auteur des règles d'un côté et l'utilisateur de l'autre, il faut le dire. Le sens bouge légèrement selon le choix.

**B8. § Quatre sources : frontière entre la source 1 et la source 4**
- Passages : la source 1 inclut « un test automatisé » et un « noyau de preuve formelle ». Dans « Le monde », on trouve : « exécuter du code généré sur des cas d'essai, […] résoudre un système formel dans un noyau logique ».
- La gêne : les mêmes dispositifs sont rangés tantôt dans « énoncé fixé à l'avance », tantôt dans « le monde ». Le lecteur ne voit plus où passe la frontière.
- Reformulation : dans « Le monde », préciser « exécuter réellement du code généré (et observer ce qu'il fait, au-delà des tests écrits) ». Pour le noyau logique, si c'est bien lui qui est visé, préciser en quoi il relève ici du « monde ». Je ne tranche pas sur l'intention.

**B9. § Énoncé fixé à l'avance, puce Simplex**
- Passage : « associe à un contrôleur complexe ou non certifié un petit module de sûreté spécifié et contrôlé à l'avance ».
- La gêne : dans tout l'ouvrage, « contrôle » veut dire « vérification ». Ici, « contrôleur » veut dire « organe de commande » (calque de *controller*). Les deux sens se télescopent dans la même phrase.
- Reformulation : « associe à une loi de commande complexe ou non certifiée un petit module de sûreté spécifié et vérifié à l'avance ». Faire de même pour « le contrôleur principal » et « contrôleur appris » plus loin.

**B10. § Énoncé fixé à l'avance, encadré Lean, deuxième paragraphe**
- Passage : « déplace radicalement ce point d'appui ».
- La gêne : aucun « point d'appui » n'a été nommé dans le paragraphe précédent. Le démonstratif n'a pas de référent.
- Reformulation : « déplace radicalement le point où doit s'exercer la confiance ».

**B11. § Deux axes, deuxième paragraphe**
- Passage : « Au sommet de la pile, un modèle de langage qui invente une décision de justice — comme dans l'affaire *Mata v. Avianca* (@sec:ch11) [@mata2023] —, échoue sur une variante voisine de sa frontière en dents de scie ou répète une idée reçue (@sec:ch12) ne bute pas nécessairement sur… ».
- La gêne : le sujet est très long, contient trois relatives et une incise, et le verbe principal arrive tard. À la lecture, on prend « échoue » pour le verbe principal.
- Reformulation : « Au sommet de la pile, qu'un modèle de langage invente une décision de justice […], échoue sur une variante voisine […] ou répète une idée reçue, il ne bute pas nécessairement sur… »

**B12. § Énoncé fixé à l'avance, « Deuxièmement »**
- Passage : « vingt-sept programmeurs […] échouaient déjà ensemble sur les entrées difficiles ».
- La gêne : « ensemble » peut se lire « en équipe », ce qui serait un contresens puisqu'ils travaillaient séparément.
- Reformulation : « échouaient déjà sur les mêmes entrées difficiles ».

**B13. Introduction du chapitre**
- Passage : « …et l'écart irréductible entre résoudre correctement le problème posé et poser un problème fidèle au réel avant d'aborder la @sec:partie-4. »
- La gêne : le paragraphe est très long et dense en renvois. La fin est ambiguë : « avant d'aborder » semble porter sur « poser un problème ».
- Reformulation : couper avant « Nous détaillons ensuite… », puis finir par « …fidèle au réel. La @sec:partie-4 viendra ensuite. »

### Gravité C (confort, style)

**C1. § Deux axes, tableau, ligne « Cause hors du cadre », colonne signalée**
- Passage : « — le chimiste […] de la ferrure (@sec:ch08) — ; ».
- La gêne : la suite tiret plus point-virgule est maladroite.
- Reformulation : remplacer l'incise par des parenthèses.

**C2. § Deux axes, troisième paragraphe**
- Passage : « un comparateur contredit l'affirmation ».
- La gêne : « l'affirmation » apparaît sans avoir été introduite, alors que la phrase parle d'« erreur ».
- Reformulation : « contredit l'affirmation erronée ».

**C3. Ensemble du chapitre : désignations de la case critique**
- Désignations relevées : « case supérieure droite », « case « dans le cadre et silencieuse » », « ligne du haut », « ligne supérieure », « première ligne ».
- La gêne : cinq désignations pour deux objets. Elles se comprennent, mais elles obligent à revenir au tableau.
- Reformulation : s'en tenir à une forme, par exemple « case « dans le cadre et silencieuse » ».

**C4. § Deux axes, paragraphe sur le logiciel classique et encadré « Vider la case par avance »**
- La gêne : l'encadré répète presque mot pour mot le paragraphe qui le précède (« caricature symétrique » puis « opposer terme à terme… L'affirmation est trop forte »).
- Suggestion : alléger l'un des deux. En outre, « caricature symétrique » est obscur (symétrique de quoi ?) ; on pourrait écrire « une caricature inverse, qui idéaliserait le logiciel classique ».

**C5. § Deux axes, encadré formel, point 1**
- Passage : « sa rigueur opère conditionnellement au cadre retenu ».
- La gêne : c'est un calque de *conditionally on*.
- Reformulation : « sa rigueur ne vaut que relativement au cadre retenu ».

**C6. § Deux axes, encadré formel, point 2**
- Passage : « toute divergence par rapport à cet énoncé sur la ligne du haut ».
- La gêne : le rattachement de « sur la ligne du haut » est ambigu (la divergence ou l'énoncé ?).
- Reformulation : « sur la ligne du haut, toute divergence par rapport à cet énoncé peut être… ».

**C7. § Deux axes, phrase après l'encadré formel**
- Passage : « Dans la lecture courante du tableau, on dit donc avec prudence que… ».
- La gêne : « lecture courante » est vague et la formule est flottante.
- Reformulation : « En résumé, le formalisme déplace la colonne… ».

**C8. § Quatre sources, premier paragraphe**
- Passage : « vos propres contrôles personnels ».
- La gêne : pléonasme. Le passage soudain au « vous » surprend aussi, alors que le chapitre disait « nous » ou « on ».
- Reformulation : « vos propres contrôles ».

**C9. § Quatre sources, premier paragraphe**
- Passage : « une autre affirmation, un texte fixé à l'avance ou une observation du monde ».
- La gêne : la liste dit « texte fixé à l'avance », alors que la source 1 s'appelle « énoncé fixé à l'avance ».
- Reformulation : harmoniser, sauf s'il s'agit d'une citation exacte de la définition du ch. 6.

**C10. § Autre raisonneur, deuxième paragraphe**
- Passages : « trois freins sévères à cette abondance » et « attrape les erreurs ».
- La gêne : les freins ne limitent pas l'abondance, mais sa valeur. « Attrape » est familier.
- Reformulation : « trois limites à la valeur de cette abondance » ; « décèle les erreurs ».

**C11. § Énoncé fixé à l'avance, encadré Lean**
- Passage : « n'a plus à juger — outre l'intégrité du noyau lui-même, réduite à une base logicielle restreinte — que d'un point précis en amont ».
- La gêne : l'incise est longue et la structure « n'a plus à juger que d'un point » se perd. « Réduite à une base restreinte » est redondant.
- Reformulation : « n'a plus à juger que d'un point précis en amont (outre l'intégrité du noyau, qui tient en une petite base logicielle) ».

**C12. § Énoncé fixé à l'avance**
- Passage : « nul ne sait écrire le contrat d'un réseau de neurones qui résume un contrat d'assurance ».
- La gêne : « contrat » apparaît deux fois dans deux sens différents dans la même phrase.
- Reformulation : « …qui résume une police d'assurance ».

**C13. § Deux axes, paragraphe après le tableau**
- Passage : « une erreur silencieuse passe dans les faits ».
- La gêne : l'expression figée « passer dans les faits » signifie « se concrétiser ».
- Reformulation : « passe jusqu'à l'action ».

**C14. Possibles dépendances (termes non définis dans le chapitre)**
- Liste : « frontière en dents de scie », « erreurs de devinette » / « erreurs constantes », « tirage », « omission de saillance », « blanchiment », « nombres nus », « modèle M3 », « méta-procédure formelle », « valeur prédictive positive », « loi de bascule », « le basculement du calendrier pour la dinde », « l'eau qui bout vers 85 °C au sommet du mont Blanc » (dont on ne voit pas, sans le ch. 2, en quoi c'est une erreur signalée hors du cadre), « facteur de 1,8 de la ferrure ».
- Ces termes sont attendus dans une synthèse. Un rappel en trois mots aiderait pour « M3 » et « erreurs de devinette / constantes », qui portent une partie de l'argument.

**C15. § Deux axes, deuxième paragraphe**
- Passage : « La question porte souvent sur des faits courants ».
- La gêne : on ne sait pas de quelle question il s'agit (la requête posée au modèle ?).
- Reformulation : « La requête porte souvent sur… ».

## 3. Appréciation globale

Le chapitre remplit bien son rôle de synthèse. La matrice à deux axes est claire, et la section « Vérification et validation », avec ses exemples (ferrure, *Mars Climate Orbiter*, encadré Simplex), est la plus accessible et la plus convaincante.

Les passages les moins accessibles sont les suivants :
- l'introduction, qui est un mur de renvois ;
- la discussion des puces « ligne / colonne », où le mouvement « vers le haut » et « vers la gauche » se brouille (A1) ;
- la frontière entre les quatre sources, notamment entre énoncé fixé et monde, et l'affirmation que le monde est la « seule » source (B4, B8) ;
- deux des points clés, qui ne reprennent pas exactement le corps du texte (B5, B6).

La sous-section « Vos propres contrôles » se lit très bien, si l'on met de côté l'ambiguïté du « vous » (B7).
