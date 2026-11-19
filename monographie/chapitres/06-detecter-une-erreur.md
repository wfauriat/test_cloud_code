# Détecter une erreur : comparateurs et cinq conditions {#sec:ch06}

Le @sec:ch05 a distingué trois sortes d’incertitudes — aléatoire, épistémique et ontologique — et montré qu’une barre d’erreur ne mesure jamais que l’ampleur du désaccord à l’intérieur d’un ensemble d’alternatives admises à l’avance (@prop:desaccord) : ce que le cadre omet, et sur quoi toutes les alternatives admises gardent donc le silence, ne laisse aucune trace chiffrée. Une estimation ou un calcul peut donc être faux sans qu’aucun intervalle d’incertitude l’indique. Ce chapitre cherche à établir ce qu’il faut pour repérer une erreur avant qu’elle ne guide l’action. Il définit les notions d’affirmation, de contrôle et de comparateur, énonce les cinq conditions qui décident si un contrôle peut arrêter une erreur, introduit la probabilité d’échappement de manière qualitative, relit le cas *Challenger* à cette lumière et précise ce que montrent un désaccord et un accord.

## Affirmation, contrôle et comparateur {#sec:ch06-affirmation-comparateur}

Dans la pratique technique comme dans la vie courante, nous n’agissons pas à partir de théories abstraites, mais à partir d’énoncés concrets produits pour une situation particulière : la charge admissible calculée pour une pièce, le taux de survie annoncé par un modèle clinique, la prévision de pluie du lendemain matin ou le compte rendu d’un essai en laboratoire. Ces énoncés préparent une décision qui, une fois engagée, recevra la réponse du monde réel (@sec:ch02).

::: {.definition #def:affirmation titre="Affirmation"}
Une **affirmation** est un énoncé portant sur un fait : la réponse d’un modèle, une prévision ou un rapport de mesure.
:::

Prise isolément, aucune affirmation ne porte sur le front la marque de sa justesse ou de sa fausseté. Qu’elle provienne d’un calcul rigoureux à l’intérieur d’un cadre (@def:cadre), d’une estimation statistique ou d’une mesure instrumentale, elle ne se contredit pas elle-même. Une faute de frappe dans une feuille de calcul, une approximation abusive, un capteur mal étalonné ou un phénomène laissé hors du cadre peuvent la rendre fausse sans altérer son apparence. Pour déceler une erreur avant que le monde ne se charge de nous détromper, il faut confronter l’affirmation à un autre élément qui, si elle est juste, devrait aller dans le même sens.

::: {.definition #def:controle titre="Contrôle"}
Un **contrôle** est la confrontation d’une affirmation à un comparateur censé concorder avec elle.
:::

::: {.definition #def:comparateur titre="Comparateur"}
Un **comparateur** est ce à quoi l’on confronte une affirmation : une autre affirmation, un texte fixé à l’avance ou une observation du monde.
:::

Cette définition regroupe trois familles de comparateurs, familières dans l’expérience quotidienne comme dans l’ingénierie.

1. *Une autre affirmation.* On recoupe un énoncé par un second calcul, une seconde estimation ou un autre jugement censé décrire le même fait. Dans la vie courante, on recompte une addition de bas en haut, ou l’on demande à un collègue de refaire le total de tête. En ingénierie, on confronte le calcul par éléments finis d’une ferrure métallique (@sec:ch05) à un calcul analytique approché mené à la main par un collègue, ou l’on compare deux modèles météorologiques indépendants avant de choisir une route maritime (@sec:ch03).
2. *Un texte fixé à l’avance.* On confronte l’affirmation à une règle, à une norme ou à une spécification arrêtée avant le calcul ou l’opération. À l’échelle ordinaire, c’est vérifier l’heure annoncée d’un départ sur l’horaire officiel ou comparer une dose préparée à l’ordonnance écrite. À l’échelle technique, c’est confronter les résultats d’un modèle thermique à une loi de conservation de l’énergie, contrôler la conformité d’un dimensionnement aux exigences d’un code de calcul réglementaire, ou s’assurer qu’un fichier de résultats respecte le format et les unités prescrits par une notice d’interface écrite à l’avance.
3. *Une observation du monde.* On met l’affirmation en présence des faits mesurés ou observés. On regarde par la fenêtre après avoir lu la prévision météo, ou l’on plonge un thermomètre dans la casserole au lieu de se fier au réglage de la plaque. En pratique technique, on soumet un prototype de la ferrure à un essai de charge sur banc, on pèse une pièce usinée, on inspecte une soudure par ultrasons (@sec:ch01) ou l’on confronte une prévision consignée dans un historique (@sec:ch03-calibration-historique) à l’issue effectivement observée.

Cette tripartition — une autre affirmation, un texte fixé à l’avance, une observation du monde — indique d’où un contrôle peut tirer son point d’appui. Elle annonce une question plus générale sur l’origine des références auxquelles nous confrontons nos calculs et nos programmes : le @sec:ch13 reprendra cette classification et la détaillera en quatre sources distinctes de comparateurs.

## Cinq conditions pour qu’un contrôle arrête une erreur {#sec:ch06-cinq-conditions}

Munis de ces trois termes, nous pouvons énoncer le principe général de la détection d’erreur.

::: {.proposition #prop:comparateur titre="Pas de détection sans comparateur" statut="définition"}
Une erreur n’est détectée que lorsqu’une affirmation est confrontée à un comparateur censé concorder avec elle, que cette comparaison fait apparaître un désaccord et que quelqu’un en prend acte.
:::

Disons-le sans détour : prise isolément, la @prop:comparateur est presque définitionnelle. Si l’on entend par « détecter une erreur » le fait d’en repérer la trace et d’en tenir compte avant d’agir, énoncer qu’il faut pour cela un terme de comparaison, un écart constaté et une prise en compte revient presque à déplier le sens des mots. Son intérêt ne tient donc pas à une thèse audacieuse, mais à la grille d’examen qu’elle impose. Dès qu’on déroule ce qu’elle exige en pratique, elle fait apparaître cinq conditions distinctes, qui doivent toutes être réunies en même temps pour qu’un contrôle arrête une erreur. Or chacune de ces cinq conditions obéit à des mécanismes qui lui sont propres, et elles peuvent céder séparément.

1. *Existence.* Il faut d’abord qu’un comparateur portant sur le même objet existe et soit disponible au moment du contrôle. Sans terme de comparaison, aucune erreur ne se révèle d’elle-même. Une estimation unique de durée de projet établie sans référence à des chantiers passés, une prévision produite pour une situation sans précédent ni modèle concurrent, ou une grandeur calculée qu’aucun capteur ne mesure laissent l’affirmation seule face à elle-même.
2. *Différence.* Il faut ensuite que le comparateur puisse **se tromper autrement** que l’affirmation : pour une cause d’erreur donnée, un comparateur se trompe autrement qu’une affirmation si cette cause ne les fausse pas tous deux de la même manière. Recalculer la même formule dans le même tableur débusque une erreur de saisie manuelle, mais non une faute dans la formule elle-même. De même, si un calcul numérique et un calcul à la main reposent sur le même formulaire de résistance des matériaux qui ignore l’effet d’un milieu corrosif, les deux calculs peuvent se tromper autrement sur une faute d’arithmétique, mais ils ne se trompent pas autrement vis-à-vis de la corrosion : sur ce point, ils s’accordent dans l’erreur.
3. *Comparabilité.* Il faut en troisième lieu que l’affirmation et le comparateur puissent être ramenés à un point de comparaison commun : qu’ils portent sur la même grandeur, dans les mêmes unités, selon les mêmes définitions et avec leurs conditions de validité explicites. Comparer une poussée calculée en livres-force à une limite exprimée en newtons, confronter une probabilité de défaillance calculée sur un mois à un seuil annuel, ou rapprocher un calcul établi pour une atmosphère sèche d’un essai conduit en enceinte humide sans en préciser les conditions interdit toute lecture fiable d’un accord comme d’un écart. Lorsque des résultats circulent entre équipes ou entre outils en perdant leurs hypothèses, leurs définitions ou leurs unités — un appauvrissement de l’information transmise que le @sec:ch08 étudiera de près —, la comparabilité disparaît avant même qu’une confrontation puisse avoir lieu.
4. *Arrivée à temps.* Il faut encore que le désaccord apparaisse *avant* que les conséquences ne soient figées par l’action. Vérifier la tenue d’une passerelle une fois le public engagé, confronter une prévision météo à la réalité une fois le voilier pris dans la tempête en pleine mer, ou conduire une enquête après l’accident fournit des enseignements précieux pour l’avenir, non un contrôle capable d’arrêter l’acte en cours. Cette contrainte de délai pèse particulièrement sur toute décision unique (@sec:ch04-decision-unique), dont la réponse réelle du monde n’arrive qu’après l’engagement irréversible.
5. *Prise en compte.* Il faut enfin que quelqu’un reçoive le désaccord, le reconnaisse pour tel et puisse agir en conséquence.

::: {.definition #def:prise-en-compte titre="Prise en compte"}
La **prise en compte** est le fait que quelqu’un prenne acte d’un désaccord et ait l’autorité pour agir en conséquence.
:::

Les deux volets de cette définition comptent également. D’une part, il faut que quelqu’un *prenne acte* du désaccord : un avertissement noyé dans des centaines de messages journaliers, relégué dans une annexe non lue ou écarté par habitude ne produit aucun effet. D’autre part, il faut que cette personne *ait l’autorité pour agir* : suspendre une mise en service, reporter un essai, demander un nouveau calcul ou modifier un choix. Si un technicien découvre une contradiction réelle, mais ne dispose ni du pouvoir de bloquer l’opération ni de l’écoute de celui qui décide, le contrôle remplit les quatre premières conditions et échoue néanmoins à la cinquième.

![Les cinq conditions d’un contrôle représentées comme cinq barrages successifs entre l’affirmation et l’action : existence d’un comparateur, capacité à se tromper autrement, comparabilité des grandeurs et des conditions, arrivée à temps et prise en compte effective. Qu’un seul barrage cède pour une famille d’erreurs, et celles-ci traversent le contrôle sans être arrêtées.](figures/ch06-cinq-conditions.pdf){#fig:ch06-cinq-conditions width=92%}

La @fig:ch06-cinq-conditions résume cette architecture : les cinq conditions agissent comme cinq barrages placés l’un derrière l’autre. Il ne suffit pas que le dispositif soit solide en moyenne ou satisfasse quatre exigences sur cinq ; si un seul barrage manque ou cède devant un type d’erreur donné, toute erreur de ce type traverse le contrôle sans obstacle.

::: {.nuance titre="Une proposition presque définitionnelle dont la portée tient aux cinq conditions"}
La @prop:comparateur porte le statut de *définition* parce qu’elle énonce presque ce que signifie le mot même de détection. Aucune expérience empirique ne saurait la démentir : si l’on découvrait une erreur sans comparateur apparent, l’examen montrerait que l’esprit s’appuyait tacitement sur un souvenir, une règle de vraisemblance ou une attente physique, qui jouait précisément ce rôle.

Sa fécondité pratique ne vient donc pas d’un résultat surprenant, mais de la grille d’examen qu’elle déploie. Parce que les cinq conditions renvoient à des défaillances distinctes — absence de référence, hypothèses partagées, perte des unités ou des conditions, retard d’exécution, défaut d’écoute ou d’autorité —, elles empêchent de confondre l’existence nominale d’un contrôle avec sa capacité réelle d’arrêter une erreur. Un organisme peut multiplier les relectures entre pairs formés à la même école (échec de la deuxième condition), exiger des comptes rendus si tardifs qu’ils arrivent après la décision (échec de la quatrième) ou marginaliser les avis dissidents (échec de la cinquième) tout en affichant un processus de contrôle formellement irréprochable.
:::

## Taux d’erreur et probabilité d’échappement {#sec:ch06-echappement}

Distinguer ce qui produit une erreur de ce qui l’empêche d’atteindre l’action demande deux grandeurs distinctes. La première mesure la fréquence ou la plausibilité de l’erreur à la source. On appelle **taux d’erreur**, noté $P(E)$, la probabilité qu’une affirmation soit fausse. Selon les contextes examinés au @sec:ch03, $P(E)$ représente soit une fréquence observée sur une longue série d’affirmations comparables, soit un poids de jugement accordé aux mondes possibles où l’affirmation considérée ne correspond pas aux faits.

Mais connaître le taux d’erreur ne dit pas encore à quel point il est dangereux d’agir d’après l’affirmation. Une équipe ou un système dont le taux d’erreur est modeste peut néanmoins causer de graves dommages si ses erreurs franchissent tous les contrôles sans être arrêtées ; à l’inverse, un outil sujet à des erreurs fréquentes, mais aussitôt interceptées avant la décision, expose moins qu’un outil plus exact dont les fautes passent sans contradiction. Il faut donc nommer la seconde grandeur.

::: {.definition #def:echappement titre="Probabilité d’échappement"}
La **probabilité d’échappement** est la probabilité qu’une affirmation fausse débouche sur une action sans avoir été contredite à temps.
:::

Dans ce chapitre, la probabilité d’échappement reste caractérisée de façon qualitative, à la limite extrême où l’une des cinq conditions manque entièrement. Considérons une famille particulière d’erreurs — par exemple les erreurs dues à une incompatibilité d’unités ou celles qu’engendre un facteur physique omis par le modèle — et un contrôle donné. Si l’une quelconque des cinq conditions fait défaut pour cette famille d’erreurs, le contrôle n’a aucune chance d’arrêter les erreurs de cette famille avant qu’elles ne se traduisent en acte : devant lui, leur probabilité d’échappement est égale à $1$, soit 100 %. Peu importe alors que le taux d’erreur $P(E)$ soit de 10 %, de 1 % ou d’un pour mille : chaque erreur de cette famille qui vient à se produire passe au travers sans contradiction utile.

Dans bien des situations réelles, les cinq conditions ne sont ni parfaitement remplies ni totalement absentes : un comparateur ne décèle qu’une fraction des fautes, produit parfois des désaccords injustifiés sur des affirmations exactes, ou n’est suivi d’effet qu’une partie du temps. La probabilité d’échappement prend alors des valeurs intermédiaires entre $0$ et $1$. Le @sec:ch09 la quantifiera et montrera comment elle se combine avec le taux d’erreur $P(E)$ pour déterminer le risque effectif d’une décision.

::: {.formel titre="Condition nécessaire de détection et échappement total"}
Soit une affirmation susceptible d’être fausse, et notons $E$ l’événement « l’affirmation est fausse », de probabilité $P(E) = \Pr(E) > 0$. Considérons une sous-classe particulière d’erreurs $E_k \subseteq E$, telle que $\Pr(E_k) > 0$, et un contrôle particulier chargé de l’examiner avant qu’une action soit engagée.

Notons $D$ l’événement « l’erreur est détectée et prise en compte avant l’action », et associons aux cinq conditions les événements suivants pour l’épisode considéré :

- $C_1$ : un comparateur portant sur l’affirmation existe et est mobilisé ;
- $C_2$ : le comparateur ne subit pas la même erreur que l’affirmation ;
- $C_3$ : l’affirmation et le comparateur sont comparés dans des grandeurs et des conditions compatibles ;
- $C_4$ : le résultat de la confrontation parvient avant que l’action fixe les conséquences ;
- $C_5$ : quelqu’un prend acte d’un éventuel désaccord et exerce l’autorité nécessaire pour suspendre ou corriger l’action.

D’après la @prop:comparateur, une détection suivie d’effet exige la réunion simultanée des cinq conditions :

$$D \subseteq C_1 \cap C_2 \cap C_3 \cap C_4 \cap C_5.$$ {#eq:ch06-inclusion}

Supposons que, pour les erreurs de la sous-classe $E_k$, l’une au moins des conditions fasse systématiquement défaut : il existe un indice $j \in \{1, 2, 3, 4, 5\}$ tel que $\Pr(C_j \mid E_k) = 0$. (Par exemple, pour $j = 2$, la cause qui engendre $E_k$ fausse systématiquement le comparateur dans le même sens ; pour $j = 5$, les avis contraires relatifs à $E_k$ ne sont jamais suivis d’effet.) Par inclusion et monotonie des probabilités (@sec:ch01-probabilite), la probabilité conditionnelle de détection vérifie :

$$\Pr(D \mid E_k) \le \Pr(C_j \mid E_k) = 0, \qquad \text{d’où} \qquad \Pr(D \mid E_k) = 0.$$ {#eq:ch06-detection-nulle}

La probabilité conditionnelle qu’une erreur de la sous-classe $E_k$ échappe à ce contrôle — c’est-à-dire l’événement contraire $\overline{D}$, atteindre l’action sans avoir été contredite à temps — vaut donc :

$$\Pr(\overline{D} \mid E_k) = 1 - \Pr(D \mid E_k) = 1.$$ {#eq:ch06-echappement-un}

Ce raisonnement repose sur deux hypothèses explicites : il vaut pour un contrôle donné (ou pour un ensemble de contrôles partageant tous la même lacune sur $E_k$), et il suppose l’absence totale de la condition $C_j$ sur cette sous-classe. L’inclusion (@eq:ch06-inclusion) ne donne qu’une borne supérieure : lorsque aucune condition ne fait systématiquement défaut, elle ne force plus la détection à zéro, et la probabilité d’échappement peut descendre au-dessous de $1$, ce que modélisera le @sec:ch09.
:::

## Le cas Challenger à la lumière des cinq conditions {#sec:ch06-challenger}

Il est tentant de lire les grands accidents industriels à travers une cause unique : tantôt un défaut de modèle qui omet une variable décisive, tantôt une faute humaine d’organisation. L’accident de la navette spatiale *Challenger*, survenu le 28 janvier 1986 [@rogers1986], illustre au contraire comment plusieurs des cinq conditions peuvent céder en même temps — les unes dans la mise en forme des données, une autre dans la salle de décision.

L’affirmation soumise au contrôle, la veille du vol, était que les joints toriques assurant l’étanchéité des propulseurs d’appoint à poudre tiendraient malgré les températures très basses annoncées pour le matin du lancement [@rogers1986]. L’enquête officielle et l’examen des documents préparés pour la réunion montrent que ce contrôle n’a pas échoué faute d’indices disponibles, mais par la rupture conjointe de la différence, de la comparabilité et de la prise en compte.

::: {.cas titre="La téléconférence précédant le lancement de Challenger (1986)"}
La veille du lancement, une téléconférence réunit les responsables de la NASA et les ingénieurs de l’entreprise Morton Thiokol, conceptrice des propulseurs à poudre, pour statuer sur l’effet du froid sur les joints toriques [@rogers1986]. Plusieurs ingénieurs recommandaient de reporter le tir, estimant que les joints risquaient de perdre leur souplesse et leur étanchéité à une température inférieure à toutes celles des lancements précédents.

Edward Tufte a examiné les tableaux et graphiques présentés lors de cette discussion [@tufte1997]. Le graphique principal montrait exclusivement les vols antérieurs sur lesquels des dommages aux joints avaient été relevés, en laissant de côté tous les vols antérieurs qui s’étaient déroulés sans incident, à des températures plus élevées. Privées de ce groupe de comparaison et présentées sans aligner l’ensemble des vols le long d’un axe de température commun, les données retenues ne faisaient pas apparaître la tendance nette de dégradation par temps froid, que révèle au contraire l’ensemble des 23 vols antérieurs documentés lorsqu’on les porte tous sur un même axe de température [@tufte1997]. Au cours des échanges qui suivirent, la direction demanda aux ingénieurs de prouver que le lancement serait dangereux plutôt que d’exiger la démonstration de sa sûreté ; leur recommandation de report fut écartée et le lancement fut maintenu [@rogers1986].
:::

Passons méthodiquement ce cas en revue selon les cinq conditions du contrôle.

- *Existence.* La première condition était remplie. Deux comparateurs existaient bel et bien avant le tir : d’une part, l’ensemble des relevés des vols passés, avec leurs températures de lancement et l’état constaté des joints [@tufte1997] ; d’autre part, l’expérience technique des ingénieurs ayant conçu les propulseurs [@rogers1986].
- *Différence.* Dans la présentation des données, la capacité à se tromper autrement a cédé. En n’affichant que les vols affectés de dommages, le graphique a sélectionné un sous-ensemble qui ne pouvait plus contredire clairement la confiance affichée dans le tir par temps froid : répartis sur une plage restreinte de cas déjà endommagés, les incidents semblaient dispersés sans ordre net et tendaient à conforter l’idée que la température n’expliquait rien [@tufte1997].
- *Comparabilité.* Dans les données également, la comparabilité a été perdue. L’absence des vols sans dommage — survenus à des températures plus clémentes — et l’absence de mise en regard de tous les vols sur une même échelle de température ôtaient le contraste indispensable entre temps doux et temps froid [@tufte1997]. Les graphiques ne rapprochaient pas dans une forme lisible ce que les vols antérieurs montraient de la température prévue pour le lendemain.
- *Arrivée à temps.* La quatrième condition était satisfaite. La réunion se tenait la veille du décollage, alors que la navette se trouvait encore sur le pas de tir et que le report demeurait possible [@rogers1986].
- *Prise en compte.* La cinquième condition a rompu dans la salle de décision. Le désaccord formulé par les ingénieurs a bien été prononcé, mais il n’a pas été retenu comme motif d’arrêt, et ceux qui le portaient ne détenaient pas l’autorité finale pour suspendre le lancement [@rogers1986].

Cette lecture évite un contresens répandu, qui ferait de *Challenger* un simple oubli de variable dans un cadre de calcul. La température figurait bien dans les préoccupations et dans les dossiers. Ce qui a manqué, c’est d’une part une mise en forme des données capable de rendre visible le contraste avec les vols sans dommage — défaillance de différence et de comparabilité —, et d’autre part l’autorité et la disposition à retenir une objection formulée à temps — défaillance de prise en compte. Réduire l’épisode à un seul de ces deux versants laisserait croire qu’un meilleur graphique aurait suffi devant une hiérarchie décidée à lancer, ou qu’une organisation plus attentive aurait tranché aisément sur la foi d’un dossier mutilé.

## Ce que montrent un désaccord et un accord {#sec:ch06-accord-desaccord}

Revenons à la structure générale d’un contrôle pour éviter une dernière confusion, fréquente lorsque l’on interprète le résultat d’une confrontation entre une affirmation et un comparateur.

Supposons d’abord que la comparaison fasse apparaître un *désaccord* : le calcul analytique à la main donne une contrainte deux fois plus élevée que le modèle par éléments finis, l’essai sur banc rompt avant la charge annoncée, ou un collègue relève une incohérence dans un bilan thermique. En supposant la comparabilité assurée — les deux côtés parlent bien de la même grandeur dans les mêmes unités et les mêmes conditions —, que prouve ce désaccord ? Il prouve qu’*au moins l’un des deux termes est faux*. Il ne dit pas encore lequel. Le premier calcul peut comporter une erreur de modélisation ou de codage ; mais le comparateur peut lui aussi être fautif, parce que le calcul à la main néglige un effet tridimensionnel réel, parce que le capteur du banc d’essai était déréglé, ou parce que le relecteur a mal lu une hypothèse. Un désaccord ne condamne pas automatiquement l’affirmation initiale : il ouvre une enquête visant à départager les deux termes, souvent en recourant à un troisième comparateur.

Considérons maintenant la situation inverse : l’affirmation et le comparateur *concordent*. Que prouve cet accord ? Pris tel quel, *il ne prouve rien*, à moins que le comparateur n’ait eu une véritable possibilité de contredire l’affirmation si celle-ci avait été fausse.

Relisons cette asymétrie à travers les cinq conditions. Si les deux calculs de la ferrure métallique s’accordent étroitement parce qu’ils partagent les mêmes idéalisations géométriques et passent tous deux sous silence l’atmosphère corrosive dans laquelle la pièce doit servir, leur accord ne dit rien sur la tenue future de la pièce en milieu marin : le comparateur ne pouvait pas se tromper autrement sur la corrosion. De même, si un contrôle compare des nombres privés de leurs conditions de validité et accepte à peu près n’importe quel ordre de grandeur, la conformité apparente ne renseigne pas sur l’exactitude du résultat. En somme, un contrôle dont le comparateur aurait acquiescé même devant une erreur grave délivre une signature, non une preuve.

L’asymétrie est nette. Un désaccord établi entre grandeurs comparables oblige à chercher l’erreur, puisqu’il démontre qu’un des deux côtés au moins fait défaut ; un accord, lui, n’apporte un véritable appui à l’affirmation que dans la mesure où le contrôle courait réellement le risque d’échouer si l’affirmation avait été fausse. Cette exigence — ce qui distingue une mise à l’épreuve véritable d’une confirmation de pure forme — constituera l’un des critères centraux du @sec:ch09.

::: {.question}
Avant d’agir sur votre prochaine affirmation décisive, quel est son comparateur, et laquelle des cinq conditions — existence, capacité à se tromper autrement, comparabilité, arrivée à temps ou prise en compte — est la plus fragile ?
:::

## Points clés {.points-cles}

- Une erreur n’est détectée avant l’action que lorsqu’une affirmation est confrontée à un comparateur censé concorder avec elle, que cette comparaison fait apparaître un désaccord et que quelqu’un en prend acte (@prop:comparateur).
- Un contrôle efficace exige cinq conditions simultanées : l’existence d’un comparateur, sa capacité à se tromper autrement pour la cause d’erreur visée, la comparabilité des grandeurs et de leurs conditions, l’arrivée à temps du désaccord et sa prise en compte par une personne ayant l’autorité d’agir.
- Qu’une seule de ces cinq conditions manque pour une classe d’erreurs, et la probabilité d’échappement de ces erreurs devant ce contrôle vaut $1$, quel que soit le taux d’erreur $P(E)$.
- Le cas *Challenger* montre la combinaison de plusieurs défaillances : l’omission des vols sans dommage sur le graphique examiné la veille a privé l’analyse de différence et de comparabilité, tandis que le rejet des objections techniques en séance a rompu la prise en compte.
- Un désaccord établit qu’au moins un des deux termes est faux, sans dire lequel ; un accord n’apporte aucune preuve si le comparateur n’avait aucune possibilité de contredire une affirmation fausse.
