# Lecture fraîche, chapitre 14 « Des chaînes qui agissent » (Sonnet)

Lecture à froid, sans autre document que le chapitre. Gravités : A = compréhension compromise ou contresens possible ; B = gêne réelle ; C = confort/style.

## 1. Ce que j'ai compris (test de lisibilité)

1. Quand des composants d'IA s'enchaînent en *pipelines* orchestrés, il n'y a plus de contrat aux jonctions ni de temps de relecture entre les étapes : la chaîne cumule les angles morts.
2. Un agent (modèle en boucle qui appelle des outils) est une chaîne à N maillons dont les erreurs s'auto-entretiennent, et il produit des actions, non des réponses : une réponse fausse se lit puis s'écarte, une action fausse s'exécute (Knight Capital en illustration).
3. Exemple chiffré à 12 étapes (p = 6 %) : sans contrôle, échec d'environ 52 % ; avec contrôle croisé à chaque étape, environ 4 % ; un facteur omis partagé (q = 3 %) échappe à tout contrôle de même nature et pèse environ 42 % des échecs restants.
4. Entre les étapes, les résultats circulent en texte nu, sans hypothèses, provenance ni incertitude (« blanchiment ») ; les contrôleurs en aval n'ont donc plus de prise.
5. L'agent inverse la pyramide de la pile logicielle : la couche la moins garantie reçoit l'autorité d'agir. Principe : explorer librement là où le comparateur est rapide et sans conséquence, faire attendre un contrôle indépendant là où l'acte est irréversible.

Je n'ai pas eu de difficulté à suivre le fil. Les gênes sont locales : renvois à des notions sans glose, quelques formulations ambiguës, quelques flottements terminologiques.

## 2. Constats classés par gravité

### Gravité A

**A1. §Le blanchiment dans les chaînes d'IA, premier paragraphe.**
Passage : « des impulsions dépourvues de mention d'unité, effaçant l'écart entre livres-force-secondes et newton-secondes ».
Gêne : « effacer l'écart » peut se lire « supprimer la différence » (donc plutôt une bonne chose). Le sens voulu est « rendre la différence invisible ». Contresens possible pour un lecteur qui ne connaît pas l'épisode.
Proposition : « masquant l'écart entre livres-force-secondes et newton-secondes » (ou « rendant invisible l'écart… »). Une seule lecture plausible côté auteur ; le sens ne bouge pas.

### Gravité B

**B1. Introduction, phrase 3.**
Passage : « Pour le dire, ce chapitre reprend deux acquis du @sec:ch08 ».
Gêne : « le » n'a pas de référent net (dire quoi ? la réponse à la question qui précède ?).
Proposition : « Pour y répondre, ce chapitre reprend… ». Lecture alternative : « pour l'exposer » (la thèse du chapitre). Dans les deux cas le sens varie peu.

**B2. Introduction, densité.**
Passage : le premier paragraphe, deux phrases très longues, cinq renvois entre parenthèses, notions « angle mort », « contrôle croisé », « part commune », « blanchiment » condensées en une subordonnée (« une chaîne cumule les angles morts, quand un contrôle croisé n'en garde que la part commune »).
Gêne : l'opposition « cumule / ne garde que la part commune » est elliptique pour qui n'a pas le ch. 8 en tête (réunion contre intersection).
Proposition : couper après « s'enchaînent d'eux-mêmes ? » et reformuler : « une chaîne additionne les angles morts de ses étapes, alors qu'un contrôle croisé ne conserve que celui qu'ils ont en commun ». Possible dépendance : angle mort, contrôle croisé, blanchiment.

**B3. §Pipelines, avant-dernier paragraphe.**
Passage : « s'intercale un comparateur capable de se tromper autrement que le composant appris ».
Gêne : « comparateur » apparaît ici pour la première fois, sans définition dans le chapitre, avec un renvoi (@sec:ch13-quatre-sources) qui ne l'explique pas. Possible dépendance (ch. 6/13).
Proposition : glose brève à la première occurrence : « un comparateur (une instance indépendante qui confronte la sortie à autre chose qu'elle-même) ».

**B4. §Agents, danger opérationnel.**
Passage : « ce basculement frappe directement les deux dernières conditions : l'*arrivée à temps* et la *prise en compte* ».
Gêne : les cinq conditions ne sont pas énumérées ; « les deux dernières » n'a de sens que si l'on connaît leur ordre. Possible dépendance (ch. 6).
Proposition : « … les deux conditions d'*arrivée à temps* et de *prise en compte* (les deux dernières de la liste du @sec:ch06-cinq-conditions) », ou énumérer les cinq en une ligne.

**B5. §Agents (Knight Capital) et §Autorité.**
Passages : « où un écart conservait une adresse » ; « dont les erreurs fluides n'ont pas d'adresse de défaillance ».
Gêne : « adresse » est une métaphore technique (localisation de la cause de l'erreur) jamais glosée ; « erreurs fluides » aussi. Possible dépendance (ch. 11/12).
Proposition : à la première occurrence, « où un écart pouvait être localisé et imputé (conservait une « adresse » de défaillance) ».

**B6. §Chiffrer une trajectoire, Lecture, 3e puce.**
Passage : « *Le facteur partagé finit par dominer les défaillances restantes.* … intervient dans 42,2 % des échecs qui subsistent ».
Gêne : 42,2 % est inférieur à la moitié, et la part indépendante (4,24 %) dépasse q (3 %) ; « dominer » contredit les chiffres. « Finit par » suggère aussi une croissance avec N qui n'est pas montrée. Les points clés disent « une large part », autre formulation du même fait.
Proposition : « *Le facteur partagé pèse lourd dans les défaillances restantes* » ou « *pèse pour plus de 40 %…* ». Deux lectures possibles de l'intention (« premier facteur parmi d'autres » ou « devient un ordre de grandeur comparable ») : je ne tranche pas.

**B7. Terminologie « lisibilité / comparabilité / comparaison fidèle / B_cmp ».**
Passages : « comparaison fidèle ($B_{\text{cmp}} = \emptyset$) » (exemple) ; « sache lire ce que l'étape précédente lui transmet… cette lisibilité » (fin de section) ; « détruit la *comparabilité* » et « l'angle mort de la comparaison $B_{\text{cmp}}$ » (blanchiment).
Gêne : trois mots pour une même propriété, et B_cmp n'est jamais défini dans le chapitre. Le lecteur ne sait pas si lisibilité = comparabilité.
Proposition : retenir « comparabilité » partout et glosser une fois B_cmp : « l'angle mort de la comparaison, noté $B_{\text{cmp}}$ ». Possible dépendance (ch. 8).

**B8. §Blanchiment, premier paragraphe.**
Passage : « qui ne valait que sous des hypothèses explicites $A$ et dans les limites de $(\dots)$ ».
Gêne : le « $(\dots)$ » est un trou de notation illisible en texte courant, et $A$ ne sert plus ensuite.
Proposition : « qui ne valait que sous des hypothèses explicites et dans certaines limites de validité » (supprimer la notation), ou la définir.

**B9. §Blanchiment, avant les deux puces.**
Passage : « le blanchiment des hypothèses et les deux proches cousins que la @sec:ch08-blanchiment en avait distingués ».
Gêne : on annonce trois formes ; la liste en donne deux (hypothèses/unités/définitions/domaines, puis provenance). Le lecteur cherche le troisième.
Proposition : annoncer « les deux formes que… », ou scinder la première puce. Deux lectures : (i) le premier item rassemble le blanchiment des hypothèses et un cousin (unités/définitions) ; (ii) il manque un item. Je ne tranche pas.

**B10. §Autorité, début de la 3e liste.**
Passage : « il convient de croiser le diagnostic avec les quatre sources de comparateurs du @sec:ch13 ».
Gêne : les quatre sources ne sont ni nommées ni utilisées ; les deux puces suivantes opposent seulement deux régimes (environnement informatique / monde réel). La promesse n'est pas tenue dans le texte. Possible dépendance (ch. 13).
Proposition : « avec la distinction du @sec:ch13 entre environnement informatique déterministe et monde physique ou institutionnel », en laissant le renvoi aux quatre sources entre parenthèses.

**B11. §Autorité, 1er paragraphe.**
Passage : « l'absence de contrat au sommet demeurait contenue par les couches situées juste au-dessous ».
Gêne : le contenant est, dans la phrase précédente, l'humain lecteur ou le comparateur mécanique, pas « les couches situées au-dessous » (qui, selon le paragraphe suivant, exécutent sans valider). Deux lectures : (a) les couches basses bornaient l'effet ; (b) la phrase vise le comparateur placé entre le sommet et les couches basses.
Proposition (lecture b) : « demeurait contenue par le lecteur humain ou par le comparateur placé entre ce sommet et les couches situées au-dessous ». Le sens bouge selon la lecture retenue.

**B12. §Autorité, avant-dernier paragraphe.**
Passage : « Le @sec:ch17 formalisera ces deux dispositifs complémentaires ».
Gêne : la phrase précédente décrit un principe (dissocier deux espaces), pas deux dispositifs ; le référent de « ces deux dispositifs » est flou (l'exploration à faible coût et le contrôle à la frontière ?).
Proposition : « Le @sec:ch17 formalisera ces deux volets (exploration libre, autorisation indépendante) ».

**B13. §Pipelines et §Agents : notions de ch. 11/12 non glosées.**
Passages : « une omission de saillance (@sec:ch12) » ; « frontière en dents de scie » ; « un fait rare inventé au deuxième tour » ; « fait rare deviné ».
Gêne : un lecteur qui n'a pas lu les chapitres précédents ne les comprend pas ; elles sont employées comme des acquis. Possible dépendance.
Proposition : une glose de quelques mots à la première occurrence (« omission de saillance : détail présent dans l'énoncé que le modèle laisse échapper »).

### Gravité C

**C1. Introduction.** « ces composants ne répondent plus à un lecteur, mais s'enchaînent » : « ces composants » renvoie à une énumération de trois types (spécifiés, appris, sorties). Proposition : « ces composants appris ».

**C2. §Pipelines, 3e paragraphe.** « tandis que les résultats intermédiaires circulent toujours plus vite » : « tandis que » est temporel/oppositif alors que le lien est cumulatif. Proposition : « et que ».

**C3. §Agents, danger opérationnel.** « s'interpose au moins le temps de lecture et la décision de l'utilisateur » : sujet double, verbe au singulier. Proposition : « s'interposent au moins le temps de lecture et la décision ».

**C4. §Pipelines, analogie industrielle.** « les conditions réelles de la route qu'il va emprunter » : l'objet assemblé (un véhicule) n'est jamais nommé, la « route » surgit. Proposition : « répond aux conditions réelles de la route que le véhicule va emprunter ».

**C5. §Agents, danger opérationnel.** « un agent muni d'outils qui écrivent et déclenchent » : verbes sans complément. Proposition : « d'outils d'écriture et de déclenchement ».

**C6. §Chiffrer, Calcul.** « la probabilité qu'une erreur locale traverse une étape donnée est $p^2$ » : le raisonnement (erreur $p$ × oubli du pair $m$, avec $m = p$) n'est pas écrit. Proposition : « est $p \times m = p^2$ ». Pas de changement de contenu.

**C7. Flottements lexicaux dans l'exemple.** Le pair « manque » l'erreur, a une « probabilité d'oubli » et « laisse passer » l'erreur (légende) ; « part indépendante » (calcul, légende) / « composante indépendante » (puce 2) ; « étourderies locales » (puce 3) / « erreurs locales ». Proposition : fixer un terme par notion.

**C8. §Chiffrer, conclusion.** « ne suffit jamais à sécuriser une trajectoire longue » : « jamais » est fort pour un exemple déclaré illustratif. Proposition : « ne suffit pas ».

**C9. §Blanchiment, étape 3.** « cette chaîne de caractères ne porte aucune cicatrice : une phrase assurée y vaut autant qu'une donnée certifiée d'un grand livre » : deux métaphores empilées ; « y » (dans le texte reçu) et « grand livre » (comptabilité) demandent un effort. Proposition : « une phrase assurée y vaut autant qu'une donnée certifiée ».

**C10. §Autorité, incohérence de grandeur.** « des millions d'instructions élémentaires » (§Pipelines, puce 1) et « des milliards d'opérations enchaînées » (§Autorité). Contextes un peu différents, mais le lecteur peut y voir un écart. Proposition : aligner (« des millions », ou « des milliards » aux deux endroits).

**C11. §Autorité, première phrase.** « Rassemblons maintenant la vue d'ensemble de l'édifice… et ce que l'enchaînement des étapes dans un agent vient y déplacer » : le complément coordonné à « la vue d'ensemble » est bancal. Proposition : « Reprenons la vue d'ensemble de l'édifice… et voyons ce que l'enchaînement des étapes dans un agent y déplace ».

**C12. §Blanchiment, comparabilité.** « Un contrôleur… aurait beau pouvoir se tromper autrement — … —, il n'a plus de prise » : concession lourde (deux modalités, tiret ouvert sur trois exemples), et temps mêlés (conditionnel / présent). Proposition : « Un contrôleur capable de se tromper autrement… n'a plus de prise sur un texte qui… ».

**C13. §Autorité.** « ils ont acheté une portée inédite… en *dépensant* ces garanties » : métaphore financière assez calquée ; « ces garanties » renvoie aux contrats des couches basses, pas à ceux du sommet. Proposition : « ils ont gagné une portée inédite… au prix de ces garanties préalables ».

**C14. §Autorité.** « Rétablir une architecture cohérente… commande un principe » : « commander » au sens de « exiger » est inhabituel. Proposition : « appelle un principe ».

**C15. Jargon isolé.** « tableau de nombres nus » / « flottants » ; « chaîne d'ingénierie multiphysique » ; « routage d'ordres » ; « hiérarchie des finalités » ; notation de Hoare {P} C {R} (renvoi à ch. 10). Compréhensibles par le contexte pour la plupart ; une glose de quelques mots suffirait pour « flottants » et « routage d'ordres ».

**C16. Nommage des « cinq conditions ».** « cinq conditions nécessaires pour qu'un contrôle arrête une erreur » (agents) et « grille des cinq conditions de détection » (blanchiment). Proposition : un seul nom.

**C17. Emploi de « agent » avant sa définition.** Utilisé dès l'introduction (« des agents, dont les erreurs… ») et dans les titres, défini en gras au début de la section suivante. Sans gravité car la définition suit immédiatement ; envisager seulement « (définis plus bas) » à l'introduction.

## 3. Appréciation globale

Chapitre globalement très lisible, bien construit (question d'ouverture, quatre temps du blanchiment, questions de fin), avec des calculs vérifiables en texte (52,4 %, 4,24 %, 7,11 %, 42,2 % se recoupent entre légende, calcul, puces et points clés).

Les plus accessibles : §Agents (danger opérationnel, réponses/actions, Knight Capital) et §Blanchiment (parcours en quatre temps, très concret).

Les moins accessibles : l'introduction (densité, renvois), §Chiffrer une trajectoire (notations M1, $B_{\text{cmp}}$, vocabulaire flottant, « dominer » en désaccord avec 42,2 %) et §Autorité (renvois aux « quatre sources », aux « couches situées au-dessous », « ces deux dispositifs ») : c'est là que le lecteur doit le plus s'appuyer sur des chapitres antérieurs.

Total : 1 A, 13 B, 17 C.
