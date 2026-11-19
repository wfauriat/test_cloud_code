# Lecture fraîche, chapitre 10 « Pourquoi l'on peut oublier les couches basses »

Lecteur : Sonnet (première lecture, texte seul).

## 1. Ce que j'ai compris (5 lignes)

1. En informatique classique, chaque couche cache son fonctionnement derrière un contrat écrit (précondition de l'appelant, postcondition du composant), d'où l'on peut empiler des opérations élémentaires déterministes sans surveiller les étages inférieurs.
2. Un « composant spécifié » est un composant dont les règles sont écrites ; l'écrit joue le rôle de comparateur fixé à l'avance.
3. On peut donc vérifier le composant une fois, avant l'usage (types, tests, relecture, analyse statique, fuzzing, preuve), avec un degré de certitude variable (Dijkstra).
4. Quand ça échoue, la défaillance a une « adresse » (l'écart à une règle écrite ou formulable), même si l'erreur est silencieuse : cas Mars Climate Orbiter (newton-secondes contre livres-force-secondes).
5. Écrire une règle ne suffit pas à la faire appliquer (trois degrés : appliqué mécaniquement, écrit, formulable seulement) ; l'apprentissage automatique (chap. 11) n'a aucun de ces trois degrés.

## 2. Constats

### Gravité A

**A1. Frontière floue de « composant spécifié » (déf., sections « Chaque couche… », « Les défaillances ont une adresse », encadré « Écrire n'est pas encore vérifier »).**
- Passages : « Un composant spécifié est un composant dont quelqu'un a écrit les règles et qu'on peut doter d'une spécification vérifiable » ; « une spécification écrite, ou qu'on aurait pu écrire » ; « Même dans un code entièrement dépourvu de documentation, le caractère spécifié des instructions préserve l'adresse de la défaillance » ; degré 3 : « contrats formulables mais non écrits ».
- Gêne : la définition exige des règles *écrites*, puis le texte parle de composants à contrat seulement « formulable » ou de code sans documentation qui resterait « spécifié ». On ne sait plus si un code non documenté est un composant spécifié. « a écrit » et « qu'on peut doter » sont aussi en tension (fait accompli ou possibilité ?). Le sens de « spécifié » glisse de « règles rédigées » à « instructions déterministes lisibles ».
- Deux lectures plausibles, je ne tranche pas.
  - Lecture restrictive (spécifié = règles effectivement écrites) : remplacer « le caractère spécifié des instructions préserve » par « le caractère déterministe et lisible du code préserve », et dire que le degré 3 concerne des composants non spécifiés qui gardent pourtant une adresse.
  - Lecture large (spécifié = règles écrites ou écrivables) : définition « … dont les règles sont écrites, ou pourraient l'être, de sorte qu'on peut le doter d'une spécification vérifiable ».
- Le sens bouge selon le choix.

### Gravité B

**B1. « Vérification en amont » (déf. en gras) contre le contenu de la liste.**
- Passage : « le contrôle d'un composant fait une fois, par rapport à sa spécification, et valable pour toutes ses exécutions futures ».
- Gêne : la liste inclut tests et relecture, dont le texte dit ensuite qu'ils n'explorent qu'un sous-ensemble ; « valable pour toutes » ne vaut que pour la preuve. Le point clé 3 (« une fois pour toutes ») reprend cette formule.
- Proposition : « … et dont la confiance acquise couvre, à un degré variable selon la méthode, les exécutions futures ». Sens inchangé si « toutes » visait la preuve seule ; sinon il y a une vraie nuance à assumer.

**B2. Encadré « trois degrés », degré 1.**
- Passage : « (… assertions vérifiées à la frontière, suites de tests automatisés) : ils sont contrôlés en amont et automatiquement ».
- Gêne : une assertion vérifiée à la frontière s'exécute à l'usage, pas « en amont » ; des tests ne couvrent pas toutes les exécutions. Cela contredit la définition de la vérification en amont.
- Proposition : « contrôlés automatiquement, en amont (types, schémas, tests) ou à la frontière (assertions) ». Deux lectures possibles (l'auteur peut vouloir « avant l'usage » au sens large) ; ne pas trancher.

**B3. Renvoi non rappelé à une condition du comparateur (section « Vérifier une fois »).**
- Passage : « ce geste résout d'avance la condition d'arrivée à temps pour toute faute qu'il sait saisir ».
- Gêne : la « condition d'arrivée à temps » vient du chap. 6 et n'est pas rappelée ; « saisir » est un calque (« catch ») flou. La phrase est elliptique : on ne voit pas quelle faute le geste « sait saisir ».
- Proposition : « ce geste satisfait d'avance la condition d'arrivée à temps (le contrôle précède l'action sur le monde) pour toute faute que le contrôle détecte ».

**B4. Termes utilisés avant leur définition en gras.**
- Passage : introduction (« composants spécifiés », « vérification en amont » non nommée mais annoncée, « chaque défaillance y conserve une adresse »), et titre de section « Les défaillances ont une adresse ».
- Gêne : « adresse » et « composants spécifiés » sont employés comme acquis dès l'introduction, alors qu'ils ne sont définis qu'aux sections 3 et 5. « adresse » est une métaphore opaque au premier emploi.
- Proposition : glose brève à l'introduction, par exemple « une défaillance localisable (nous dirons : qui a une adresse) ». Sens inchangé.

**B5. Phrase elliptique sur la portée du contrat (fin de la section 3).**
- Passage : « un contrat ne protège que ce qu'il énonce, et seulement là où quelque chose l'impose ».
- Gêne : « quelque chose » est vague, et la condition (un mécanisme de contrôle) n'est expliquée que beaucoup plus loin.
- Proposition : « … et seulement là où un mécanisme (type, test, contrôle) l'impose ».

**B6. Jargon informatique dense, sans glose.**
- Passage : « déréférencement d'un pointeur nul », « signature », « ordre total cohérent », « micro-noyaux critiques », « décodeurs », « cas nominaux », « régression », « tampons », « allocateur de mémoire ».
- Gêne : un lecteur cultivé non informaticien bute sur plusieurs termes à la suite, surtout dans les listes de la section 4.
- Proposition : gloses entre parenthèses pour « pointeur nul » (« référence vers une case mémoire inexistante »), « signature » (« type attendu des données »), « ordre total » (« qui permet de comparer deux éléments quelconques »). Ou alléger la liste.

**B7. « Correction partielle / totale » (encadré Hoare).**
- Passage : « *Correction partielle* … *Correction totale* ».
- Gêne : en français courant « correction » évoque le fait de corriger ; le sens « correct, conforme à la spécification » n'est pas posé.
- Proposition : « *Exactitude partielle* / *totale* (au sens de « conforme à la spécification »)». Ces termes existent aussi en français pour « correctness » ; le sens ne change pas.

**B8. Redondance du récit Mars Climate Orbiter et de l'encadré « Le rapport d'enquête ».**
- Passage : date du 23 septembre 1999, `SM_FORCES`, N·s contre lbf·s, facteur 4,45 : tout figure dans le corps du texte puis presque mot pour mot dans l'encadré.
- Gêne : lecture lourde, et l'encadré coupe le fil entre le récit et « Que se passe-t-il dans des situations beaucoup plus ordinaires ».
- Proposition : réduire l'encadré à la partie organisationnelle (deuxième et troisième paragraphes), ou ne conserver le technique que dans le corps du texte. Aucun changement d'argument.

**B9. Possibles dépendances non rappelées.**
- Passage : « blanchiment » (« le blanchiment à l'interface détruisait la comparabilité »), « comparateur », « cadre (@def:cadre) », « comparabilité », « trois grandes familles de comparateurs ».
- Gêne : le chapitre renvoie aux chap. 2, 6, 8 sans redonner le sens minimal. Le blanchiment est partiellement glosé (« les unités disparaissent au passage d'une frontière »), mais « cadre » et « comparabilité » ne le sont pas.
- Proposition : une demi-phrase de rappel pour chacun, par exemple « (la possibilité de confronter le résultat à une référence) » après « comparabilité ».

**B10. Saut logique en tête de la section « Vérifier une fois, avant l'usage ».**
- Passage : « Pourquoi personne ne se tient-il à côté d'un logiciel de paie pour refaire à la main chaque addition … ? Parce que la promesse … est un énoncé écrit, la confrontation … n'a pas à attendre l'exploitation ».
- Gêne : la question porte sur l'absence de contrôle humain à l'usage ; la réponse annonce seulement que le contrôle peut se faire avant. Le lien (« avant » donc « pas besoin de refaire après ») est implicite. Phrase longue.
- Proposition : ajouter « et, une fois faite, elle dispense de refaire le contrôle à chaque usage » après « sur le composant lui-même ».

**B11. Conclusion : « y » flou et formulation plus forte que le corps du texte.**
- Passages : « pourquoi une réponse fluide et fausse n'y brise aucun contrat » ; « des contrats écrits autorisent une vérification en amont ».
- Gêne : « y » renvoie à « ce renversement » (sens probable), mais la phrase est lourde. « Autorisent » laisse croire que l'écrit suffit, alors que l'encadré dit que le contrat seulement écrit ne relève de la vérification en amont que s'il est converti en contrôle.
- Proposition : « n'y brise aucun contrat » devient « dans ce cadre ne brise aucun contrat ». « autorisent » devient « rendent possible » (nuance à garder explicite).

**B12. Point clé 4, enchaînement elliptique.**
- Passage : « seul le premier arrête automatiquement les écarts avant l'usage, faute de quoi des données nues subissent encore un blanchiment aux interfaces ».
- Gêne : « faute de quoi » a un référent incertain (« faute d'application mécanique » ?). La phrase accumule trois idées.
- Proposition : couper en deux : « … seul le premier arrête automatiquement les écarts avant l'usage. Sans lui, des données nues continuent de subir le blanchiment aux interfaces. »

### Gravité C

1. Section « Chaque couche… » : « elle possède cinq caractères décisifs » est un calque de « characteristics ». Proposition : « cinq propriétés ».
2. Même liste : « elle est *violable* » (présenté comme une qualité) surprend. Proposition : « *vérifiable* : on peut constater nettement si une implémentation la respecte ou l'enfreint ».
3. Encadré Hoare/Meyer : « partage symétriquement obligations et bénéfices », « bénéfice » (calque de « benefit », à rendre par « avantage »), « données extérieures non fiables » (calque de « untrusted » ; « non maîtrisées »).
4. Même encadré : « duplication défensive de contrôles redondants » est un pléonasme. Proposition : « contrôles défensifs redondants ».
5. Répétition de « exact » : « promesse exacte », « analogie exacte », « relais exact », « exactement de même », « On reconnaît exactement ». Effet d'insistance qui affaiblit. À varier.
6. Section 2, conteneur : « passe à l'échelle mondiale » (calque de « scales ») ; « pièces de coin » (calque de « corner castings », « pièces d'angle » ou « coins de fixation »).
7. Section 2 : « sauter à une autre adresse d'instruction » entre en collision avec le sens ultérieur d'« adresse » de défaillance. Proposition : « sauter à une autre instruction du programme ».
8. Section 5 : « Les programmes spécifiés échouent sans relâche » est hyperbolique. Proposition : « échouent régulièrement ».
9. « rassemble en un seul épisode les deux faces de cette réalité » : « cette réalité » est floue (silence de l'erreur / localisation de la cause). Nommer les deux faces.
10. « sans déclencher d'alarme décisive » : « décisive » est obscur ; en outre l'encadré dit que des anomalies de trajectoire avaient été observées mais non remontées. Petite tension avec « Durant des mois … sans alarme ». Proposition : « sans alarme suffisante pour être traitée ».
11. Encadré MCO : « des newton-secondes (…) prescrites » : accord à revoir (« prescrits »).
12. Typographie : « unités du Système international » ; en français courant : « système international d'unités ».
13. Section 4, pont : « Ils ne pèsent pas chaque véhicule après qu'il a traversé le fleuve pour savoir si le tablier va tenir » : temporalité illogique (après la traversée, il est trop tard). Proposition : « Ils ne pèsent pas chaque véhicule pour savoir, au fur et à mesure, si le tablier va tenir ».
14. « l'écart est arrêté sur la table de travail » : image peu naturelle (« sur la planche à dessin », « avant la mise en service »).
15. Section 3, fin : « commande tout ce qui change au sommet de la pile » (calque de « drives »). Proposition : « conditionne ».
16. Le triplet de Hoare est présenté deux fois (corps et encadré) presque à l'identique ; allègement possible.
17. Phrases très longues : introduction (phrase « Ce chapitre montre comment… lettre morte »), dernier paragraphe (« Au terme de ce chapitre… »), paragraphe « Avant même d'y venir ». À couper.
18. Encadré « Le rapport d'enquête » placé au milieu du récit : coupure de rythme (voir B8).
19. Section 1 : « (tout en préservant ses invariants internes d'un appel à l'autre) » : notion non expliquée avant l'encadré, qui la définit.
20. Registre : passé simple isolé (« survint », « ne se perdit », « pénétra », « fut perdue ») au milieu d'un texte au présent et au passé composé. À harmoniser si voulu.

## 3. Appréciation globale

- **Les plus accessibles** : sections 2 (« Des opérations élémentaires à la composition », avec l'image du conteneur) et 4 (le pont) ; la narration de Mars Climate Orbiter est claire et bien menée ; la question finale et les points clés se comprennent bien.
- **Les moins accessibles** : l'encadré Hoare/Meyer (dense, jargonnant, redondant avec le corps du texte) ; la section 3 (« composant spécifié ») et l'encadré des trois degrés, où la définition de « spécifié » n'est pas stable (A1) ; la liste des méthodes de vérification (jargon et définition de la « vérification en amont » trop forte, B1, B2, B6) ; la fin du chapitre, longue et elliptique.
- Le fil général est bon, les renvois sont nombreux mais bien annoncés ; le principal risque de contresens est la définition de « composant spécifié ».
