# Pourquoi l’on peut oublier les couches basses {#sec:ch10}

Ce chapitre s’appuie sur la théorie générale du contrôle exposée dans la @sec:partie-2, en particulier sur les cinq conditions nécessaires pour qu’un comparateur arrête une erreur (@sec:ch06, @prop:comparateur) et sur l’analyse des chaînes, des contrôles croisés et du blanchiment aux interfaces (@sec:ch08, @prop:chaines, @def:blanchiment). Avec la @sec:partie-3, nous appliquons cette grille à l’empilement des couches informatiques. Pourquoi pouvons-nous lancer un calcul scientifique, ouvrir un fichier ou consulter un compte en banque sans surveiller les milliards d’opérations élémentaires qu’exécute le matériel à chaque seconde ? Ce chapitre montre comment l’informatique classique a conquis ce droit de se faire oublier grâce aux contrats écrits, aux composants spécifiés, à la vérification en amont et au fait que chaque défaillance y conserve une adresse — tout en marquant la limite précise où s’arrête cette garantie lorsqu’une règle reste lettre morte.

## Boîte à outils : les contrats logiciels {#sec:ch10-boite-outils}

Dans la vie quotidienne comme en ingénierie, nous confions sans cesse des sous-tâches à des programmes : calculer une paie, trier une table, acheminer un paquet sur un réseau, intégrer une équation. Lorsque nous appelons l’un de ces programmes, nous ne voulons pas suivre chacune de ses instructions pas à pas ; nous voulons savoir ce qu’il exige au départ et ce qu’il garantit à l’arrivée.

En génie logiciel, cette répartition des responsabilités porte un nom précis. Un **contrat** est l’engagement écrit d’un composant : ce qu’il exige de l’appelant — sa *précondition* — et ce qu’il garantit en retour — sa *postcondition*. Formalisée par Bertrand Meyer sous le nom de *programmation par contrat* [@meyer1992], cette idée transpose à la frontière d’un module logiciel la logique d’un accord juridique clair. Si l’appelant veille à ce que la précondition soit satisfaite au moment de l’appel, le composant s’engage à ce que la postcondition soit vérifiée lorsqu’il rend la main (tout en préservant ses invariants internes d’un appel à l’autre). Réciproquement, si l’appelant enfreint la précondition — par exemple en demandant une recherche dichotomique sur un tableau qui n’a pas été trié, ou en passant une taille négative à un allocateur de mémoire —, le composant est délié de sa promesse.

L’informatique théorique exprime ce lien depuis les travaux de C. A. R. Hoare [@hoare1969] sous la forme devenue usuelle du *triplet de Hoare*, noté $\{P\}\; C \;\{Q\}$ : si l’assertion $P$ (la précondition) est vraie avant l’exécution de l’instruction ou du programme $C$, alors l’assertion $Q$ (la postcondition) est vraie une fois cette exécution achevée. Ce schéma simple suffit à décrire le contrat d’un composant : $P$ délimite les situations dans lesquelles il accepte d’opérer, $Q$ énonce ce que l’on peut tenir pour acquis en aval de son exécution.

::: {.outils titre="Triplets de Hoare et programmation par contrat"}
À la suite de l’axiomatique proposée par Hoare [@hoare1969], un énoncé de contrat pour un bloc d’instructions $C$ s’écrit sous la forme :

$$\{P\}\; C \;\{Q\}.$$

On distingue deux degrés de garantie :

- *Correction partielle* : si $P$ est vrai avant l’exécution de $C$ *et si $C$ se termine*, alors $Q$ est vrai à la sortie. (Une boucle infinie satisfait trivialement la correction partielle.)
- *Correction totale* : si $P$ est vrai avant l’exécution de $C$, alors $C$ se termine en un temps fini et $Q$ est vrai à la sortie.

La propriété décisive pour l’architecture des programmes est la *règle de composition séquentielle*. Si l’on dispose de deux composants $C_1$ et $C_2$ tels que :

$$\{P\}\; C_1 \;\{R\} \qquad \text{et} \qquad \{R\}\; C_2 \;\{Q\},$$

alors leur enchaînement vérifie :

$$\{P\}\; C_1 \,;\, C_2 \;\{Q\}.$$

L’assertion intermédiaire $R$ joue le rôle de relais exact à la frontière : pour savoir si $C_2$ tiendra sa promesse $Q$, on n’a besoin de connaître que $R$, jamais la manière dont $C_1$ l’a établi.

Bertrand Meyer a donné à cette logique une traduction architecturale directe dans la programmation par contrat [@meyer1992]. Chaque clause partage symétriquement obligations et bénéfices : la précondition est une obligation pour l’appelant et un bénéfice pour le composant (qui n’a pas à traiter les cas exclus) ; la postcondition est une obligation pour le composant et un bénéfice pour l’appelant. S’y ajoutent les *invariants de structure*, propriétés internes (par exemple « le compteur de taille égale toujours le nombre d’éléments rangés ») que toute opération publique suppose vrais à l’entrée et rétablit à la sortie. Dès lors qu’un contrat assigne clairement la responsabilité de $P$ à l’appelant, les étages internes évitent la duplication défensive de contrôles redondants, tandis que les points d’entrée exposés à des données extérieures non fiables concentrent les contrôles nécessaires pour établir $P$.
:::

Cette notion de promesse placée à la frontière entre deux étages va expliquer comment l’informatique peut empiler des millions de lignes de code sans s’effondrer sous son propre poids.

## Des opérations élémentaires à la composition {#sec:ch10-composition}

Descendons tout en bas de la pile informatique. Au niveau physique, un *bit* n’est rien d’autre qu’un état matériel — un niveau de tension électrique, une charge piégée dans un condensateur, une orientation magnétique — associé à une convention de lecture qui lui attribue la valeur `0` ou `1`. En groupant ces bits, le matériel exécute des opérations élémentaires : additionner deux entiers, comparer deux mots, déplacer une valeur d’un registre à une case mémoire, sauter à une autre adresse d’instruction selon le résultat d’un test.

Prises une à une, ces opérations sont triviales. Elles possèdent toutefois deux traits précieux. D’abord, elles s’exécutent à une cadence vertigineuse, à l’échelle de la nanoseconde sur un processeur courant. Ensuite, hors panne matérielle ou perturbation physique accidentelle, elles sont *déterministes* : placée devant les mêmes entrées et le même état initial, la même suite d’instructions produit exactement les mêmes sorties, sur une autre machine, dix ans plus tard.

En remontant de la couche matérielle vers un compilateur, un système d’exploitation, un moteur de base de données, un logiciel de paie ou un calculateur de navigation spatiale, aucun ingrédient mystérieux n’apparaît en chemin. Tout ce qui existe au sommet d’un édifice informatique classique est *composition* de ces opérations élémentaires. Or nous avons établi au @sec:ch08 (@prop:chaines) qu’une longue suite d’étapes mises en série risque de cumuler les angles morts de chaque maillon et les malentendus nés aux interfaces. Comment un édifice logiciel d’une telle ampleur peut-il donc fonctionner sans exiger que quelqu’un surveille chaque étape intermédiaire ?

La réponse tient au fait que chaque couche dissimule sa mécanique interne derrière une promesse exacte. Celui qui écrit un logiciel de comptabilité n’a pas besoin de connaître la géométrie des transistors du processeur, l’algorithme d’ordonnancement des processus du noyau ni le placement physique des secteurs sur le disque. Il lui suffit de s’appuyer sur les contrats exposés par les couches inférieures. Tant que ces promesses tiennent, la complexité interne de ce qui se trouve au-dessous devient transparente pour l’étage supérieur.

Le transport maritime moderne offre une analogie exacte de cette économie de l’attention. Avant la normalisation du conteneur, charger un cargo exigeait de connaître la forme, l’emballage et la fragilité de chaque caisse ou de chaque sac ; chaque transbordement entre camion, train et navire imposait de manipuler le contenu pièce par pièce. Avec le conteneur normalisé, la grue du port et le navire porte-conteneurs n’ont plus besoin de savoir ce qui se trouve à l’intérieur de la boîte — chaussures, céréales, pièces usinées ou matériel électronique — pourvu que ses dimensions extérieures, la position de ses pièces de coin, sa résistance à l’empilement et sa masse brute maximale obéissent à un contrat rigoureux. Parce que l’interface est fixe et tenue, l’infrastructure de transport ignore le détail de la cargaison et passe à l’échelle mondiale sans ouvrir les boîtes à chaque transfert. Il en va exactement de même pour l’informatique classique : c’est la netteté de la frontière qui permet d’oublier ce qui s’exécute à l’intérieur.

## Chaque couche est une promesse écrite {#sec:ch10-promesse-ecrite}

Regardons concrètement comment s’énoncent ces promesses à différents étages de la pile logicielle, bien au-dessus des portes logiques.

- *Le protocole réseau TCP.* Un programme qui ouvre une connexion réseau ne veut pas reconstituer lui-même les paquets découpés sur la route, réordonner ceux qui arrivent dans le désordre, éliminer les doublons ni gérer les retransmissions après perte sur une ligne encombrée. Le protocole TCP lui fait une promesse précise : les octets envoyés arriveront au destinataire dans l’ordre d’émission et intacts, ou bien — si le réseau cède durablement — la connexion signalera explicitement une rupture plutôt que de livrer sans avertissement un flux tronqué ou mélangé.
- *Une routine de tri.* Une fonction de tri de bibliothèque promet de renvoyer une permutation exacte du tableau qu’on lui confie — ni élément ajouté, ni élément perdu, avec les mêmes multiplicités — rangée par ordre croissant selon la relation fournie, à la condition préalable que cette relation définisse bien un ordre total cohérent.
- *Un système de fichiers.* Lorsqu’un programme écrit des données dans un fichier puis demande explicitement leur synchronisation sur le support matériel (par une opération de vidage des tampons sur disque telle que `flush` ou `fsync`), le système de fichiers promet que ces octets ont été inscrits de manière durable et qu’une lecture ultérieure les restituera fidèlement, hors destruction physique du support.

À travers ces trois exemples apparaît la propriété qui soutient toute l’architecture classique : *une spécification est un énoncé écrit*. Parce qu’elle est rédigée explicitement dans un langage formel ou technique, elle possède cinq caractères décisifs :

1. elle est établie *à l’avance*, indépendamment d’une exécution particulière ;
2. elle est *lisible* par quelqu’un d’autre que l’auteur du programme ;
3. elle est *discutable* : un juriste, un ingénieur ou un utilisateur peut contester que ce qui est promis corresponde au besoin réel ;
4. elle est *versionnable* : toute modification de la promesse laisse une trace datée ;
5. elle est *violable* : on peut constater de manière nette si une implémentation la respecte ou l’enfreint.

On retrouve ici directement l’une des trois grandes familles de comparateurs identifiées au @sec:ch06 (@sec:ch06-affirmation-comparateur, @def:comparateur) : un *texte fixé à l’avance*. Dans l’informatique classique, le contrat écrit joue précisément ce rôle de comparateur permanent, extérieur au code qui s’exécute et opposable à ses résultats. Nous pouvons maintenant nommer ce type de brique logicielle.

::: {.definition #def:composant-specifie titre="Composant spécifié"}
Un **composant spécifié** est un composant dont quelqu’un a écrit les règles et qu’on peut doter d’une spécification vérifiable, c’est-à-dire d’un contrat.
:::

La @def:composant-specifie trace une frontière nette qui structurera toute la @sec:partie-3. Dans un composant spécifié, la règle existe *avant* l’exécution sous forme de texte : quelqu’un l’a formulée, quelqu’un peut la lire, quelqu’un peut la confronter au programme. Par contraste, le @sec:ch11 étudiera des composants d’une tout autre nature, dont personne n’a rédigé les règles d’exécution sous forme d’instructions et de contrats, parce que ces règles ont été ajustées statistiquement sur de vastes ensembles d’exemples. Ce déplacement — quitter l’énoncé écrit pour ajuster des paramètres sur des données — commande tout ce qui change au sommet de la pile informatique.

Avant même d’y venir, une réserve essentielle s’impose sur les composants spécifiés eux-mêmes : *un contrat ne protège que ce qu’il énonce, et seulement là où quelque chose l’impose*. Si la routine de tri promet de conserver les éléments et de les ranger, elle ne dit rien de l’usage métier qu’on fera de la liste triée. Si une interface entre deux modules de calcul numérique précise en commentaire que les températures sont attendues en kelvins ou que les efforts sont exprimés en newtons, mais ne transporte que des nombres nus dépourvus d’étiquette d’unité dans le fichier ou dans le type de donnée transmis, le contrat écrit en prose n’empêche pas les grandeurs incompatibles de se mêler. On reconnaît exactement le mécanisme de blanchiment analysé à la @sec:ch08-blanchiment (@def:blanchiment), par lequel les conditions ou les unités d’un résultat disparaissent au passage d’une frontière : ce que l’interface laisse tomber ou relègue hors du périmètre contrôlé peut traverser les maillons sans alerte, même au cœur d’un logiciel parfaitement déterministe.

## Vérifier une fois, avant l’usage {#sec:ch10-verification-amont}

Pourquoi personne ne se tient-il à côté d’un logiciel de paie pour refaire à la main chaque addition au moment où tombent les bulletins de salaire ? Parce que la promesse d’un composant spécifié est un énoncé écrit, la confrontation avec ce comparateur n’a pas à attendre l’exploitation : elle peut se faire *avant* la mise en service, sur le composant lui-même.

On appelle **vérification en amont** le contrôle d’un composant fait une fois, par rapport à sa spécification, et valable pour toutes ses exécutions futures. Au lieu d’inspecter chaque réponse produite une à une en cours d’exploitation, on met le composant à l’épreuve de son contrat avant qu’il ne serve, et la confiance ainsi acquise couvre l’ensemble des appels ultérieurs qui respectent ses préconditions.

L’informatique classique a développé tout un arsenal pour accomplir ce mouvement en amont, à des niveaux croissants d’exigence et de coût :

- *Les systèmes de types statiques* : le compilateur vérifie avant toute exécution que les données passées aux fonctions appartiennent aux catégories attendues ; un programme qui tente d’additionner une date et une vitesse, ou de passer un type `LivreForceSeconde` là où la signature attend un `NewtonSeconde`, est rejeté avant même de pouvoir être exécuté.
- *Les tests unitaires et d’intégration* : des jeux d’épreuves écrits à l’avance confrontent le composant sur des cas nominaux et des cas limites aux postconditions attendues, et restent attachés au dépôt de code pour bloquer toute régression future.
- *La relecture de code* : un second développeur lit les instructions écrites et vérifie qu’elles traduisent fidèlement le contrat annoncé, mobilisant une compréhension humaine des intentions et des cas rares.
- *L’analyse statique* : des outils inspectent l’ensemble des chemins du programme sans le lancer, afin d’écarter automatiquement des familles entières de défauts comme le déréférencement d’un pointeur nul, le débordement de tableau ou la division par zéro.
- *Le fuzzing* — l’envoi automatisé d’un flot massif d’entrées aléatoires ou délibérément malformées — éprouve la robustesse des décodeurs et des frontières de modules avant la mise en production, pour vérifier qu’aucune entrée imprévue ne brise le contrat ni ne provoque d’arrêt brutal.
- *La preuve formelle* : là où les enjeux justifient le coût (signalisation ferroviaire, commandes de vol aéronautiques, micro-noyaux critiques), on démontre mathématiquement que, pour toute entrée vérifiant $P$, l’exécution du programme $C$ satisfait nécessairement $Q$.

Ce panorama appelle immédiatement une mise en garde classique, formulée avec netteté par Edsger Dijkstra : les essais peuvent montrer la présence de défauts, jamais prouver leur absence [@dijkstra1972]. Une batterie de tests unitaires, même étendue, n’explore qu’un sous-ensemble fini des entrées possibles ; seule une démonstration formelle couvre l’ensemble des exécutions vis-à-vis d’un modèle donné de la machine — et comme l’a établi la @sec:ch02-rigueur-formelle, la rigueur d’une preuve reste elle-même relative au cadre (@def:cadre) que forme la spécification retenue. Si la spécification oublie un cas du monde réel, le code prouvé conforme à cette spécification reproduira fidèlement cet oubli.

Pourtant, la limite rappelée par Dijkstra borne *le degré de certitude* acheté par les tests ; elle ne change pas la *nature de l’opération*. Dans tous ces cas — du typage statique à la preuve formelle —, l’effort de contrôle porte sur le composant lui-même, en regard de son énoncé écrit, et s’effectue *avant* le déploiement. En reprenant la grille des cinq conditions du @sec:ch06 (@sec:ch06-cinq-conditions), ce geste résout d’avance la condition d’arrivée à temps pour toute faute qu’il sait saisir : l’écart est arrêté sur la table de travail, non lorsque le système agit sur le monde.

Une image tirée du génie civil résume ce déplacement : celle de *l’épreuve et du calcul de charge d’un pont*. Les ingénieurs calculent la capacité portante de l’ouvrage sur plans, contrôlent ses assemblages et chargent le tablier avec des camions-étalons *avant* d’ouvrir le pont à la circulation, puis posent à l’entrée un panneau indiquant la charge maximale autorisée. Ils ne pèsent pas chaque véhicule après qu’il a traversé le fleuve pour savoir si le tablier va tenir. Tant que la structure a été contrôlée en amont et que les usagers respectent la précondition affichée sur le panneau, chacun peut franchir le pont sans refaire à chaque passage le calcul de résistance des matériaux.

## Les défaillances ont une adresse {#sec:ch10-adresse-defaillance}

Insister sur la vérification en amont ne doit pas conduire à idéaliser l’informatique classique. Les programmes spécifiés échouent sans relâche : erreurs d’arrondi, conditions limites négligées, blocages entre tâches concurrentes, débordements de mémoire, incompatibilités de format. Plus encore — et il faut écarter ici un contresens fréquent —, les erreurs des couches basses ne sont *pas* toujours bruyantes ni faciles à voir en cours d’exécution. Un logiciel classique peut parfaitement tourner sans planter, sans afficher le moindre message d’erreur et tout en produisant des nombres d’apparence plausible pendant des semaines ou des mois.

Ce qui distingue un composant spécifié ne tient donc ni à l’infaillibilité ni au vacarme des pannes ; cela tient au fait que ses écarts sont *définissables* par rapport à une règle écrite ou formulable. Lorsqu’un composant spécifié produit un mauvais résultat, la défaillance possède une **adresse** : l’endroit précis où une spécification écrite, ou qu’on aurait pu écrire, a été enfreinte.

L’histoire de la sonde *Mars Climate Orbiter*, déjà croisée au @sec:ch00 et examinée sous l’angle du blanchiment à la @sec:ch08-blanchiment, rassemble en un seul épisode les deux faces de cette réalité : comment une erreur classique peut passer longtemps inaperçue lorsque le contrat reste hors des contrôles automatiques, et pourquoi l’enquête après coup converge néanmoins vers un lieu exact.

Le 23 septembre 1999, la sonde *Mars Climate Orbiter* devait s’insérer en orbite autour de Mars ; elle pénétra bien trop bas dans l’atmosphère martienne et fut perdue [@mco1999]. Tout au long du transit vers la planète, un programme au sol baptisé `SM_FORCES` calculait l’effet des petites poussées de correction des propulseurs et inscrivait ces impulsions dans un fichier de données transmis à l’équipe de navigation [@mco1999]. Or la spécification d’interface écrite exigeait que ces grandeurs soient exprimées en unités du Système international, les newton-secondes ($\text{N}\cdot\text{s}$), alors que le programme `SM_FORCES` les écrivait en unités anglo-saxonnes, les livres-force-secondes ($\text{lbf}\cdot\text{s}$). Parce que l’équipe et les logiciels de navigation lisaient ces valeurs comme des newton-secondes, l’effet de chaque petite poussée était sous-estimé d’un facteur proche de 4,45 [@mco1999].

À la @sec:ch08-blanchiment, nous avons vu pourquoi l’erreur n’a pas été interceptée en vol : dans le fichier de transfert, les nombres voyageaient nus, dépourvus de toute indication d’unité, si bien que le blanchiment à l’interface détruisait la comparabilité. Durant des mois, le logiciel de navigation a poursuivi ses calculs sans déclencher d’alarme décisive ni interrompre les opérations. L’erreur était tout sauf bruyante.

Et pourtant, dès que la perte survint, l’enquête ne se perdit ni dans le flou ni dans l’indécision. Bien que le rapport de la commission d’enquête ait mis au jour de lourdes défaillances humaines et organisationnelles [@mco1999], sous cette couche institutionnelle demeurait un écart parfaitement localisé entre un module de code et un document de spécification.

::: {.cas titre="Le rapport d’enquête sur Mars Climate Orbiter (1999)"}
Dans son premier rapport publié après la perte de *Mars Climate Orbiter* le 23 septembre 1999, la commission d’enquête nommée par la NASA a reconstitué à la fois la cause technique immédiate de l’accident et les facteurs organisationnels qui l’avaient laissée se prolonger [@mco1999].

Sur le plan technique, la cause immédiate résidait dans le programme au sol `SM_FORCES` : celui-ci calculait et écrivait dans un fichier d’interface les impulsions des propulseurs en livres-force-secondes ($\text{lbf}\cdot\text{s}$) au lieu des newton-secondes ($\text{N}\cdot\text{s}$) prescrites par le document de spécification d’interface, introduisant un écart d’un facteur voisin de 4,45 dans l’estimation de trajectoire [@mco1999].

Sur le plan organisationnel, la commission a relevé plusieurs failles convergentes : des effectifs trop restreints et surchargés, une communication insuffisante entre équipes, l’absence de recalcul indépendant de bout en bout, et le fait que les doutes et anomalies de trajectoire observés pendant le transit n’aient pas été remontés ni instruits formellement à temps [@mco1999]. Ce sont ces failles humaines et de processus qui ont empêché la prise en compte des indices faibles en cours de vol ; mais elles n’ont pas effacé l’existence d’une règle écrite précise ni celle du programme et du fichier d’interface qui la contredisaient.
:::

Que se passe-t-il dans des situations beaucoup plus ordinaires, loin des dossiers spatiaux, lorsqu’un programme a été écrit à la hâte sans aucun cahier des charges ni document d’interface préalable ? Même dans un code entièrement dépourvu de documentation, le caractère spécifié des instructions préserve l’adresse de la défaillance. Face à un résultat aberrant, un développeur ouvre le code source, suit pas à pas la trace d’exécution sur l’entrée fautive et finit par pointer du doigt un énoncé du type : « à cette ligne, il aurait fallu tester le cas nul avant de diviser », ou « la boucle s’arrête un indice trop tôt et omet le dernier enregistrement ». Autrement dit, même lorsqu’une spécification n’a pas été rédigée *avant* la panne, on peut la formuler *après coup* en regard d’une instruction précise et localiser exactement l’endroit de la divergence. Les analyses après incident convergent vers une adresse, où un correctif local peut être écrit, relu et transformé en test de non-régression pour les exécutions futures.

Toutefois, *Mars Climate Orbiter* met également en lumière une distinction capitale que l’expression même de « contrat écrit » risque de masquer : *écrire une règle n’est pas encore la faire vérifier*. Entre un type statique qui interdit dès la compilation de confondre des newtons et des livres-force, un document d’interface rédigé en prose dans un classeur séparé, et une attente implicite que personne n’a pris la peine de noter avant la panne, la protection en cours de route change du tout au tout. Dans le premier cas, l’écart est bloqué automatiquement en amont ; dans le deuxième, le document écrit fournit bien une adresse après l’accident, mais n’arrête rien par lui-même tant qu’un test ou un schéma de données ne le traduit pas en contrôle ; dans le troisième, aucune barrière n’existe avant l’usage, même si le code laisse encore désigner après coup ce qu’il aurait dû faire.

::: {.nuance titre="Écrire n’est pas encore vérifier : les trois degrés du contrat"}
Dire qu’un composant spécifié repose sur un contrat ne signifie pas que toute violation sera interceptée avant le service. Il faut distinguer trois degrés d’existence d’un contrat dans l’informatique classique :

1. *Les contrats appliqués mécaniquement* (systèmes de types statiques, schémas de données contraignants, assertions vérifiées à la frontière, suites de tests automatisés) : ils sont contrôlés en amont et automatiquement. Si le fichier d’interface produit par le programme `SM_FORCES` avait imposé un format typé distinguant explicitement $\text{N}\cdot\text{s}$ et $\text{lbf}\cdot\text{s}$, le désaccord aurait été bloqué avant le lancement.
2. *Les contrats écrits* (documents d’interface en prose, spécifications fonctionnelles, commentaires) : ils fournissent avec certitude une adresse lors de l’enquête après coup, mais ne relèvent de la vérification en amont que si quelqu’un transforme le texte en un contrôle automatique effectif. La spécification d’interface de *Mars Climate Orbiter* appartenait à ce deuxième degré.
3. *Les contrats formulables mais non écrits* (attentes implicites dans un logiciel non documenté) : ils n’offrent aucune protection préalable, mais continuent d’offrir une adresse une fois l’incident survenu, puisqu’on peut toujours écrire après coup ce que le programme aurait dû calculer à tel endroit précis.

Gardons cette échelle en mémoire pour la suite : lorsqu’un composant n’est plus fait de règles rédigées par un auteur mais de paramètres ajustés statistiquement sur des exemples — comme nous l’examinerons au @sec:ch11 —, il ne dispose d’*aucun* de ces trois degrés pour le composant lui-même. Il n’existe ni type qui borne la justesse de ce qu’il répond, ni cahier écrit qui fixe la sortie exacte de chaque requête, ni même d’instruction locale à incriminer ligne par ligne après l’échec.
:::

Au terme de ce chapitre, la raison pour laquelle nous pouvons légitimement oublier les couches basses de l’informatique est claire : des opérations élémentaires jusqu’aux protocoles réseau et aux systèmes de fichiers, l’édifice est composé de composants spécifiés dont les contrats écrits autorisent une vérification en amont, une fois pour toutes les exécutions futures, et garantissent qu’en cas d’échec, l’enquête retrouve une adresse. Mais cette architecture rassurante s’est longtemps arrêtée devant un mur : toutes les tâches pour lesquelles aucun humain ne sait écrire de règle explicite — reconnaître une écriture manuscrite, évaluer si un dossier correspond à un poste, résumer fidèlement un ensemble de pièces hétérogènes. Pour franchir ce mur, l’apprentissage automatique renverse la démarche et tire la règle des données. Le @sec:ch11 examine ce que l’on gagne dans ce renversement, ce que l’on dépense en échange, et pourquoi une réponse fluide et fausse n’y brise aucun contrat.

::: {.question}
Lorsque l’un des composants de votre chaîne de traitement produit un résultat erroné, pouvez-vous désigner la règle précise qu’il a enfreinte — et cette règle était-elle imposée par un contrôle automatique ou seulement écrite dans un document ?
:::

## Points clés {.points-cles}

- Chaque couche de l’informatique classique dissimule sa mécanique interne derrière un contrat écrit précisant les préconditions attendues de l’appelant et les postconditions garanties en retour, ce qui permet d’empiler des opérations élémentaires déterministes jusqu’à des systèmes vastes sans inspecter les étages inférieurs.
- Un composant spécifié repose sur un énoncé écrit à l’avance, lisible par autrui, discutable et opposable à son exécution, qui joue le rôle d’un comparateur permanent.
- Parce que la promesse est écrite, la vérification en amont (typage, tests, relecture, analyse statique, *fuzzing*, preuve formelle) contrôle le composant une fois pour toutes avant sa mise en service, même si les essais montrent la présence de défauts sans jamais prouver leur absence.
- Écrire un contrat ne suffit pas à le faire appliquer : entre contrat appliqué mécaniquement, contrat seulement écrit en prose et attente formulable sans écrit préalable, seul le premier arrête automatiquement les écarts avant l’usage, faute de quoi des données nues subissent encore un blanchiment aux interfaces.
- Même lorsqu’un logiciel classique fonctionne pendant des mois en produisant des résultats faux sans alarme décisive, comme dans la perte de *Mars Climate Orbiter*, ses défaillances conservent une adresse précise où une règle écrite ou formulable après coup a été enfreinte.
