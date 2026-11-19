# Lecture fraîche — Chapitre 10 « Pourquoi l’on peut oublier les couches basses »

Lecteur : Opus (première lecture, seul le fichier `chapitres/10-couches-basses.md` a été lu).

## 1. Résumé de ce que j’ai compris (test de lisibilité)

L’informatique classique peut empiler des couches énormes sans qu’on surveille les étages inférieurs, parce que chaque couche cache son fonctionnement derrière un contrat (précondition/postcondition, triplets de Hoare, programmation par contrat de Meyer) qui sert de comparateur écrit à l’avance.
Un « composant spécifié » est un composant dont on a écrit les règles et qu’on peut doter d’un tel contrat. On peut donc le vérifier une fois, avant l’usage (types, tests, relecture, analyse statique, fuzzing, preuve), pour toutes ses exécutions futures.
Ces composants échouent pourtant, parfois en silence (Mars Climate Orbiter), mais leurs défaillances ont toujours une « adresse », c’est-à-dire un lieu précis où une règle écrite ou formulable a été violée.
Nuance : écrire un contrat n’est pas le faire appliquer. Il y a trois degrés (appliqué mécaniquement, écrit en prose, formulable mais non écrit), et seul le premier arrête l’erreur avant l’usage.
Les composants appris sur données (chapitre 11) n’ont aucun de ces trois degrés.

Le fil général est clair. Ce qui reste flou à la lecture, c’est surtout le statut exact de ce qui doit être « écrit » (voir A1).

## 2. Constats classés par gravité

### Gravité A : compréhension compromise ou contresens possible

**A1. Section « Chaque couche est une promesse écrite » (définition), puis « Les défaillances ont une adresse » et l’encadré « Écrire n’est pas encore vérifier » : le mot « écrit » et le mot « règle » changent de sens.**
Passages :
- « *une spécification est un énoncé écrit* » ; « elle est établie *à l’avance* » ;
- définition : « Un **composant spécifié** est un composant dont quelqu’un a écrit les règles et qu’on peut doter d’une spécification vérifiable, c’est-à-dire d’un contrat » ;
- « la règle existe *avant* l’exécution sous forme de texte : quelqu’un l’a formulée, quelqu’un peut la lire, quelqu’un peut la confronter au programme » ;
- « une spécification écrite, ou qu’on aurait pu écrire » ;
- « Même dans un code entièrement dépourvu de documentation, le caractère spécifié des instructions préserve l’adresse » ;
- « *Les contrats formulables mais non écrits* ».

Ce qui gêne : « les règles » désigne tantôt le code lui-même (les instructions qu’un auteur a écrites), tantôt une spécification distincte du code, à laquelle on « confronte le programme ». Dans le second cas, la règle est écrite à l’avance. Dans le premier, elle peut n’être formulée qu’après coup. Le lecteur ne sait donc pas si un programme non documenté est un composant spécifié au sens de la définition, alors que tout le contraste avec le chapitre 11 repose là-dessus. Il y a deux lectures plausibles : (a) « spécifié » signifie « dont les instructions ont été écrites par quelqu’un », et la spécification peut venir plus tard ; (b) « spécifié » signifie « doté d’un contrat écrit à l’avance ». Je ne tranche pas.
Reformulation minimale, à choisir selon la lecture retenue. Pour (a), ajouter après la définition : « Les règles dont il est question ici sont les instructions du programme elles-mêmes ; le contrat peut être écrit avant l’exécution ou seulement formulé après coup. » Pour (b), retirer « ou qu’on aurait pu écrire » et le troisième degré de l’encadré. Mais (b) change le contenu de l’argument et relève de l’auteur.

### Gravité B : gêne réelle

**B1. « Des opérations élémentaires à la composition » : « la complexité interne de ce qui se trouve au-dessous devient transparente pour l’étage supérieur ».**
« Transparent » est ici un faux ami venu du jargon informatique anglais, où il veut dire « invisible ». En français courant, ce qui est transparent est ce qu’on voit à travers, donc ce qu’on voit. On peut comprendre l’inverse du sens voulu.
Reformulation : « devient invisible pour l’étage supérieur ». Le sens ne bouge pas.

**B2. « Des opérations élémentaires à la composition » contre « Les défaillances ont une adresse » : « sauter à une autre adresse d’instruction » / « la défaillance possède une **adresse** ».**
« Adresse » sert d’abord au sens technique d’adresse mémoire, puis devient le terme défini en gras au sens de « lieu de la défaillance ». L’introduction l’emploie déjà (« chaque défaillance y conserve une adresse ») avant toute définition. La collision de sens trouble le lecteur.
Reformulation : dans la section sur la composition, « sauter à une autre instruction du programme selon le résultat d’un test ». Le sens ne bouge pas.

**B3. « Les défaillances ont une adresse » : « l’endroit précis où une spécification écrite, ou qu’on aurait pu écrire, a été enfreinte ».**
L’adresse est-elle une clause de la spécification ou un endroit du code ? Plus loin, on lit « un écart parfaitement localisé entre un module de code et un document de spécification », puis, dans l’encadré final, « instruction locale à incriminer ligne par ligne ». Les deux lectures sont plausibles. Je ne tranche pas.
Reformulation, si c’est le code qui est visé : « l’endroit précis du programme où une spécification écrite, ou qu’on aurait pu écrire, a été enfreinte ».

**B4. « Chaque couche est une promesse écrite » : « 5. elle est *violable* : on peut constater de manière nette si une implémentation la respecte ou l’enfreint ».**
« Violable » veut dire « qui peut être violé ». Le sens visé est plutôt « dont la violation est constatable ». De plus, les points clés résument cette liste en quatre traits seulement (« écrit à l’avance, lisible par autrui, discutable et opposable »). « Versionnable » y a disparu et « opposable » remplace « violable ».
Reformulation : « elle est *vérifiable* : on peut constater nettement si une implémentation la respecte ou l’enfreint ». Il faudrait aussi aligner le point clé sur les cinq traits, ou dire dans le corps du texte que « violable » équivaut à « opposable ».

**B5. Fin de « Chaque couche est une promesse écrite » : « un contrat ne protège que ce qu’il énonce, et seulement là où quelque chose l’impose ».**
« Quelque chose » est trop vague. Le lecteur ne comprend qu’au tout dernier tiers du chapitre qu’il s’agit d’un contrôle mécanique.
Reformulation : « et seulement là où un mécanisme de contrôle le fait respecter ». Le sens ne bouge pas, si c’est bien l’idée de l’encadré final.

**B6. « Vérifier une fois, avant l’usage » : « En reprenant la grille des cinq conditions du chapitre 6, ce geste résout d’avance la condition d’arrivée à temps pour toute faute qu’il sait saisir ».**
« Condition d’arrivée à temps » est une possible dépendance (chapitre 6) que rien n’éclaire ici. La phrase a en outre un gérondif mal rattaché : ce n’est pas « ce geste » qui reprend la grille.
Reformulation : « Si l’on reprend la grille des cinq conditions du chapitre 6, ce geste satisfait d’avance celle qui exige que le contrôle intervienne à temps, avant que l’erreur ait produit ses effets, pour toute faute qu’il sait saisir. » Le sens risque de bouger si la condition du chapitre 6 dit autre chose qu’« à temps ».

**B7. « Vérifier une fois, avant l’usage » : la phrase « Une batterie de tests unitaires, même étendue, n’explore qu’un sous-ensemble fini … que forme la spécification retenue ».**
La phrase est trop dense. Elle juxtapose les tests, la preuve, le modèle de machine, un renvoi au chapitre 2 et la notion de « cadre », qui est une possible dépendance.
Reformulation : couper avant le tiret. « … vis-à-vis d’un modèle donné de la machine. Encore cette preuve n’est-elle rigoureuse que relativement au cadre que forme la spécification retenue (chapitre 2). »

**B8. Encadré « Le rapport d’enquête » : « les facteurs organisationnels qui l’avaient laissée se prolonger ».**
« L’ » renvoie grammaticalement à « la cause technique », mais on ne « laisse » pas « se prolonger » une cause. On comprend plutôt l’erreur ou l’écart.
Reformulation : « qui avaient laissé l’erreur persister ». Le sens ne bouge pas.

**B9. Encadré « Le rapport d’enquête » : « introduisant un écart d’un facteur voisin de 4,45 dans l’estimation de trajectoire ».**
Le corps du texte dit que l’effet de chaque poussée était sous-estimé d’un facteur 4,45. L’encadré, lui, laisse croire que la trajectoire estimée était fausse d’un facteur 4,45. Les deux énoncés ne sont pas équivalents.
Reformulation : « introduisant un écart d’un facteur voisin de 4,45 dans les impulsions prises en compte pour l’estimation de trajectoire ».

**B10. « Les défaillances ont une adresse », avant-dernier paragraphe : « la protection en cours de route change du tout au tout ».**
« En cours de route » fait penser à une protection pendant l’exécution. Or la phrase suivante oppose justement le blocage « en amont » et l’absence de « barrière avant l’usage ». Deux lectures sont possibles : pendant la chaîne de traitement, ou avant l’usage.
Reformulation : « la protection avant l’usage change du tout au tout ». C’est cohérent avec l’encadré qui suit, mais le sens bouge si l’auteur pensait aussi aux contrôles d’exécution, comme les assertions à la frontière.

**B11. Encadré « Écrire n’est pas encore vérifier », degré 1 : « le désaccord aurait été bloqué avant le lancement ».**
Il y a deux lectures. (a) Avant le lancement de la sonde : or l’erreur concernait des fichiers produits pendant le transit. (b) Avant la mise en service du programme ou l’exploitation des fichiers. Je ne tranche pas.
Reformulation, pour la lecture (b) : « aurait été bloqué dès la production du premier fichier ». Pour la lecture (a) : « aurait été détecté dès les essais au sol, avant le lancement de la sonde ».

**B12. Points clés, troisième puce, contre l’encadré final : « la vérification en amont (…) contrôle le composant une fois pour toutes avant sa mise en service ».**
L’affirmation est sans réserve, alors que le chapitre insiste ensuite : « écrire une règle n’est pas encore la faire vérifier ». Le résumé contredit donc la nuance principale du corps du texte.
Reformulation : « …la vérification en amont (…) *peut* contrôler le composant une fois pour toutes avant sa mise en service… ».

### Gravité C : confort et style

**C1. Introduction : « grâce aux contrats écrits, aux composants spécifiés, à la vérification en amont et au fait que chaque défaillance y conserve une adresse ».** La phrase d’annonce, très longue, empile quatre notions encore inconnues. « Adresse » y est opaque. On peut accepter cela dans une annonce, mais il vaudrait mieux couper après « à chaque seconde ? ». « L’informatique classique » n’est pas non plus défini à cet endroit : on ne comprend l’opposition avec l’apprentissage automatique qu’à la fin.

**C2. « Boîte à outils » : « (tout en préservant ses invariants internes d’un appel à l’autre) ».** Le mot « invariants » est employé avant sa définition, qui vient dans l’encadré. Proposition : « (tout en préservant d’un appel à l’autre certaines propriétés internes, ses *invariants*, voir l’encadré) ».

**C3. « Boîte à outils » : double exposé.** Le texte courant présente Meyer, puis Hoare et le triplet. L’encadré refait ensuite tout l’exposé (« À la suite de l’axiomatique proposée par Hoare… », « Bertrand Meyer a donné… »). Le lecteur a une impression de redite. On pourrait alléger le second paragraphe du texte courant (« L’informatique théorique exprime ce lien… ») et renvoyer simplement à l’encadré.

**C4. Encadré « Triplets de Hoare » : « les étages internes évitent la duplication défensive de contrôles redondants ».** Le jargon de la « programmation défensive » arrive sans explication. Proposition : « les étages internes n’ont pas à refaire, par précaution, des contrôles déjà assurés ailleurs ».

**C5. Fin de « Boîte à outils » : « Cette notion de promesse (…) va expliquer comment l’informatique peut empiler des millions de lignes de code ».** Le futur proche a une tournure anglaise (*will explain*) et l’image « empiler des lignes » est boiteuse. Proposition : « C’est cette notion (…) qui permet de comprendre comment l’informatique peut superposer des millions de lignes de code ».

**C6. « Des opérations élémentaires à la composition » : « comparer deux mots ».** Au sens machine (*word*), « mot » sera lu par un non-spécialiste comme un mot de la langue. Proposition : « comparer deux valeurs ».

**C7. « Des opérations élémentaires à la composition » : « En remontant de la couche matérielle vers un compilateur, (…) aucun ingrédient mystérieux n’apparaît en chemin ».** Le gérondif n’a pas le même sujet que le verbe principal. Proposition : « Si l’on remonte de la couche matérielle vers… ».

**C8. Analogie du conteneur : « passe à l’échelle mondiale ».** C’est un calque de *scale up*, et « passer à l’échelle » se lit mal avec « mondiale ». Proposition : « peut s’étendre à l’échelle mondiale ».

**C9. Section « Chaque couche est une promesse écrite », fin : « commande tout ce qui change au sommet de la pile informatique ».** L’image du « sommet de la pile » pour l’apprentissage automatique n’est pas préparée. Plus haut, le sommet désignait la comptabilité ou la paie. Proposition : « commande tout ce qui change avec ces nouveaux composants ».

**C10. « Vérifier une fois, avant l’usage » : « à des niveaux croissants d’exigence et de coût ».** L’ordre de la liste (relecture humaine, puis analyse statique, puis fuzzing) ne paraît pas strictement croissant. Proposition : « à des niveaux variés d’exigence et de coût, jusqu’à la preuve formelle ».

**C11. Même liste, item 1 : « passer un type `LivreForceSeconde` là où la signature attend un `NewtonSeconde` ».** On passe une valeur d’un type, pas un type. « Signature » est un terme de jargon. Proposition : « passer une valeur de type `LivreForceSeconde` là où la fonction attend un `NewtonSeconde` ».

**C12. Même liste, item 2 : « des jeux d’épreuves écrits à l’avance confrontent le composant sur des cas nominaux et des cas limites aux postconditions attendues ».** Le complément « aux postconditions » est trop éloigné de « confrontent ». Proposition : « …vérifient, sur des cas courants et des cas limites, que le composant respecte les postconditions attendues ».

**C13. Même liste, item 4 : « le déréférencement d’un pointeur nul, le débordement de tableau ».** Le jargon est opaque pour un lecteur non informaticien. On pourrait ajouter une glose brève, par exemple « (accès à une zone de mémoire inexistante ou hors limites) ».

**C14. Même liste, item 5 : « *Le fuzzing* — l’envoi automatisé… — éprouve… ».** La typographie diffère des autres items, qui suivent tous le modèle « *Intitulé* : explication ». Proposition : « *Le fuzzing* : l’envoi automatisé (…) de données malformées éprouve… ».

**C15. « Les défaillances ont une adresse » : « même si le code laisse encore désigner après coup ce qu’il aurait dû faire ».** La tournure est lourde. Proposition : « même si le code permet encore de désigner après coup ce qu’il aurait dû faire ».

**C16. « Les défaillances ont une adresse » : « sous cette couche institutionnelle demeurait un écart ».** Le mot « couche » est employé au sens figuré dans un chapitre où il a un sens technique précis. Cela ne gêne que légèrement. Proposition : « sous ces défaillances institutionnelles demeurait… ».

**C17. Conclusion : « Au terme de ce chapitre, … ».** La conclusion est rattachée à la section « Les défaillances ont une adresse » et n’a pas de titre propre. Le saut vers le chapitre 11 (« une réponse fluide et fausse ») évoque des modèles de langage qui n’ont pas encore été mentionnés. On peut l’accepter comme accroche, mais un intertitre ou une ligne de séparation aiderait.

## 3. Appréciation globale

Le chapitre se lit bien. La progression est nette : contrat, composition, promesse écrite, vérification en amont, adresse, nuance. Les analogies (conteneur, pont) sont efficaces.

- **Sections les plus accessibles.** « Des opérations élémentaires à la composition », avec l’analogie du conteneur, et « Vérifier une fois, avant l’usage », avec l’image du pont. Le récit de Mars Climate Orbiter est également clair.
- **Sections les moins accessibles.** La « Boîte à outils » est redondante entre le texte courant et l’encadré, et elle emploie des termes avant de les définir. Surtout, l’articulation entre la définition du composant spécifié, le principe « une spécification est un énoncé écrit » et le troisième degré « formulable mais non écrit » reste instable (A1). C’est le point qui mérite l’arbitrage de l’auteur, car il conditionne le contraste avec le chapitre 11. Les points clés gagneraient aussi à reprendre exactement les nuances du corps du texte (B4, B12).
