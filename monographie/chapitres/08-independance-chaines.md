# Indépendance, chaînes et contrôles croisés {#sec:ch08}

Le @sec:ch06 (@prop:comparateur) a établi qu’une erreur n’est détectée que si l’affirmation rencontre un comparateur qui existe, se trompe autrement qu’elle, lui est comparable, arrive à temps et fait l’objet d’une prise en compte effective (@sec:ch06-cinq-conditions). Le @sec:ch07 (@prop:cause-commune) a montré qu’un même cadre agit comme cause commune de tous les contrôles calculés en son sein, si bien qu’un facteur omis reste hors de leur portée tant qu’une observation ou un regard extérieur ne l’apporte pas du dehors (@sec:ch07-deux-voies). Lorsque l’on assemble plusieurs personnes, équipes, modèles ou programmes pour accomplir une tâche complexe ou pour se relire mutuellement, deux questions décisives se posent : que vaut au juste l’indépendance d’un comparateur, et comment les angles morts se composent-ils selon l’architecture de l’assemblage ? Ce chapitre répond à ces deux questions, formalise l’opposition entre chaînes en série et contrôles croisés en parallèle, et identifie le mécanisme — le blanchiment aux interfaces — qui transforme si souvent un contrôle croisé en simple chaîne.

## Boîte à outils : fiabilité en série et en parallèle {#sec:ch08-serie-parallele}

Avant de parler de raisonnements et d’erreurs de modèle, il est utile de rappeler un calcul élémentaire de sûreté de fonctionnement. Lorsqu’un système est formé de plusieurs composants élémentaires — des relais électriques, des pompes de secours, des étages de calcul —, la façon dont ils sont reliés gouverne directement la probabilité que l’ensemble échoue. Deux montages extrêmes fournissent les repères de base.

Dans un montage *en série*, chaque composant doit accomplir sa part pour que le système fonctionne : une seule défaillance interrompt toute la ligne, comme un maillon faible qui cède sous la charge. À mesure que le nombre $N$ d’étapes augmente, les occasions de faillir s’ajoutent ; même si chaque étape est individuellement fiable, une longue suite d’étapes accumule vite un risque global appréciable.

Dans un montage *en parallèle*, au contraire, plusieurs composants redondants assurent la même fonction : le système ne cède que s’ils défaillent tous ensemble. Lorsque leurs pannes surviennent indépendamment les unes des autres, mettre deux composants en parallèle réduit spectaculairement le risque d’échec global, parce qu’il faut une coïncidence de pannes pour abattre l’ensemble.

Tout change dès qu’apparaît une défaillance de mode commun (@sec:ch07-mode-commun), comme deux pompes de secours alimentées par le même tableau électrique. Si la panne de ce tableau survient avec une certaine probabilité, elle met hors service les deux pompes d’un coup. On peut alors empiler une troisième ou une quatrième pompe sur la même alimentation : la probabilité d’échec de l’ensemble ne descendra jamais au-dessous du risque porté par la cause partagée.

::: {.outils titre="Fiabilité en série, en parallèle et défaillances corrélées"}
Soient $N$ étapes dont les probabilités d’échec individuelles sont $p_1, \dots, p_N$, supposées indépendantes dans un premier temps.

- **Système en série.** L’ensemble fonctionne si et seulement si toutes les étapes fonctionnent. Sa fiabilité vaut $\prod_{i=1}^{N} (1 - p_i)$, et sa probabilité d’échec s’écrit :
  $$\Pr(\text{échec en série}) = 1 - \prod_{i=1}^{N} (1 - p_i).$$
  Lorsque toutes les étapes ont une même petite probabilité d’échec $p$, on a $1 - (1 - p)^N \approx Np$ au premier ordre : la probabilité d’échec croît d’abord à peu près proportionnellement à $N$.
- **Système en parallèle.** Si $K$ composants redondants ont des probabilités d’échec indépendantes $p_1, \dots, p_K$, le système n’échoue que si tous échouent simultanément :
  $$\Pr(\text{échec en parallèle}) = \prod_{j=1}^{K} p_j.$$
  Pour deux composants identiques de taux d’échec individuel $p = 5\,\%$, la probabilité d’échec simultané tombe à $p^2 = 0{,}25\,\%$.
- **Effet d’une défaillance corrélée.** Supposons qu’une cause commune survienne avec la probabilité $q$ et entraîne à coup sûr l’échec de tous les composants, indépendamment de leurs pannes propres (de probabilités $p'_j$, supposées indépendantes entre elles). La probabilité d’échec du montage en parallèle devient alors :
  $$\Pr(\text{échec}) = 1 - (1 - q)\left(1 - \prod_{j=1}^{K} p'_j\right) \ge q.$$
  Quel que soit le nombre $K$ de composants ajoutés, la probabilité d’échec ne descend jamais au-dessous de $q$.
:::

Ce contraste entre montage en série et montage en parallèle va maintenant se transposer directement des pièces matérielles aux raisonnements et aux contrôles. Pour opérer cette transposition, il faut d’abord nommer ce qu’un composant ne sait pas voir.

## Les angles morts d’un composant {#sec:ch08-angles-morts}

Dans tout processus d’analyse, de calcul ou de décision, deux rôles se répondent (@sec:ch06). Nous appellerons **producteur** celui — personne, équipe, programme ou modèle — qui émet une affirmation, et **contrôleur** celui qui confronte cette affirmation à un comparateur. Un même ingénieur peut être producteur le matin et contrôleur l’après-midi sur le dossier d’un collègue ; un code de simulation peut produire une affirmation qu’un banc d’essai ou un second modèle vient contrôler.

Quel que soit son degré de soin, aucun de ces acteurs — humains ou logiciels — ne perçoit toutes les façons dont une affirmation peut être fausse. Ce que le cadre (@def:cadre) a laissé dans son arrière-plan tacite $\mathcal{T}$, ce que les instruments de mesure n’enregistrent pas, ce que la position dans l’organisation empêche de savoir, tout cela dessine autour de chaque composant une zone d’invisibilité.

::: {.definition #def:angle-mort titre="Angle mort"}
L’**angle mort** d’un composant (personne, équipe, programme ou modèle), noté $B_i$ pour le composant $i$, est l’ensemble des causes d’erreur qu’il est incapable de percevoir.
:::

Un angle mort n’est ni une faute morale ni une incompétence générale : c’est l’envers inévitable d’une spécialisation et d’un cadre fini. Un calcul par éléments finis sur une ferrure métallique (@sec:ch05, @sec:ch07) saisit avec une grande finesse les concentrations de contraintes dues à la géométrie, mais la corrosion électrochimique en atmosphère saline appartient à son angle mort dès lors qu’aucune variable chimique ne figure dans ses équations. Une analyse de syntaxe repère les fautes de grammaire d’un programme, non les erreurs de formule physique. Un examen comptable relève une facture mal imputée, non la fragilité réelle d’un matériau sur le terrain.

Deux remarques complètent la @def:angle-mort. D’abord, un producteur $1$ et un contrôleur $2$ arrivent chacun devant le problème avec leur propre angle mort, $B_1$ et $B_2$. Ensuite, le contrôle lui-même — l’acte de comparer leurs deux réponses — peut être trop grossier, ambigu ou mal raccordé pour enregistrer certains écarts : nous noterons $B_{\text{cmp}}$ l’angle mort propre à la comparaison (repris dans le modèle formel de la @sec:ch08-chaines-controles). Pour concevoir des contrôles qui arrêtent vraiment les erreurs, il faut donc comprendre ce qui sépare $B_2$ de $B_1$, et ce qu’il en coûte de les éloigner l’un de l’autre.

## L’indépendance est relative, et se paie en comparabilité {#sec:ch08-independance}

On parle souvent d’un « contrôle indépendant » comme s’il s’agissait d’une qualité absolue, à la manière d’une étiquette apposée sur un service d’audit ou sur une deuxième équipe. En réalité, l’indépendance entre une affirmation et son comparateur n’existe jamais dans l’absolu : elle se définit toujours par rapport à une classe d’erreurs précise. Et dès qu’on cherche à l’accroître, une tension apparaît avec une autre des cinq conditions du @sec:ch06 (@sec:ch06-cinq-conditions) : la comparabilité.

::: {.proposition #prop:independance titre="L’indépendance est relative, et se paie en comparabilité" statut="hypothèse de travail"}
Un comparateur aide contre une classe d’erreurs dans la mesure où leur cause l’affecte autrement que l’affirmation contrôlée. Ce qu’une affirmation et son comparateur ont en commun, aucun des deux ne peut le contrôler chez l’autre ; il leur faut pourtant partager quelque chose pour être comparés. L’indépendance d’un contrôle est donc toujours relative à une classe d’erreurs, et tend à se payer en comparabilité — donc en coût de mise en correspondance. *(Statut composite : la première phrase relève de la définition ; la tension générale entre indépendance et coût de comparabilité constitue une hypothèse de travail.)*
:::

Les deux pôles de cette tension éclairent le compromis auquel fait face toute vérification. À une extrémité se trouve la copie exacte : deux exécutions identiques du même programme sur les mêmes données. La comparabilité est parfaite — les résultats se superposent bit à bit —, mais la capacité à se tromper autrement est nulle : les deux exécutions partagent tout, jusqu’à la moindre omission de cadre, et ne contrôlent rien l’une chez l’autre (tout au plus une panne matérielle fugitive).

À l’autre extrémité se trouve le regard venu d’un tout autre horizon : un spécialiste d’une autre discipline, un opérateur de terrain qui n’utilise ni les mêmes équations ni les mêmes catégories. Cet interlocuteur peut apercevoir d’emblée ce que votre cadre a laissé dans l’ombre. Mais précisément parce qu’il partage très peu avec votre représentation, ses objections peinent à mordre sur vos chiffres : elles ne parlent pas des mêmes grandeurs, ne se traduisent pas sans effort dans votre modèle et risquent d’être écartées faute de terrain commun ou de prise en compte (@def:prise-en-compte). Entre la copie stérile et l’objection incommensurable, chaque type de comparateur occupe une place intermédiaire, selon ce qu’il partage avec l’affirmation et ce qu’il laisse au-dehors (@tbl:ch08-comparateurs).

| Comparateur | Partage avec l’affirmation | Peut déceler | Coût indicatif |
| :--- | :--- | :--- | :--- |
| Même calcul, nouvelle graine ou nouvel échantillon | Tout, sauf le tirage aléatoire | Bruit d’échantillonnage et bruit numérique | Négligeable |
| Même méthode, autre implémentation | Équations, données, hypothèses | Erreurs de programmation ou d’implémentation | Faible |
| Autre méthode, même modèle | Variables, hypothèses, données | Erreurs propres à la méthode | Modéré |
| Autre modèle du problème | La grandeur visée, une partie des données | Erreurs de forme du modèle, dans les variables partagées | Élevé |
| Expérience, retour d’exploitation | La grandeur mesurée en situation réelle | Tout ce qui fait bouger cette grandeur sur le terrain | Très élevé et lent |
| Autre discipline | Parfois pas même la grandeur | La classe d’erreurs la plus large, en principe | Élevé, plus un travail de traduction |

Table: Échelle des comparateurs, ordonnée selon ce qu’ils partagent avec l’affirmation contrôlée. Plus on descend dans le tableau, plus la classe d’erreurs atteignable s’élargit, et plus le coût tend à croître — sous forme d’effort de production ou de travail de traduction pour rendre les conclusions comparables. {#tbl:ch08-comparateurs}

Plaçons la ferrure métallique des chapitres [-@sec:ch05] et [-@sec:ch07] sur le @tbl:ch08-comparateurs. Rappelons la situation : le bureau d’études a calculé par éléments finis que la pièce supporte sa charge nominale avec un coefficient de sécurité de 1,8, mais le modèle ignore la corrosion en atmosphère marine.

- Tout en haut du tableau se tient une seconde exécution du même calcul par éléments finis : la comparaison est immédiate, gratuite, et parfaitement aveugle à la corrosion ; un contrôle analytique rapide reposant sur les mêmes idéalisations géométriques (@sec:ch07) demeure, lui aussi, bloqué au niveau des méthodes partageant le même modèle.
- Au milieu du tableau figure le modèle d’un collègue appartenant à une autre équipe de mécanique, bâti avec d’autres approximations de géométrie ou d’encastrement : ce comparateur peut repérer une mauvaise hypothèse mécanique dans les variables partagées, mais tant que le cadre demeure purement mécanique, la corrosion lui échappe encore.
- Tout en bas du tableau arrivent deux comparateurs d’une autre nature : un essai de charge pratiqué sur une ferrure vieillie plusieurs années en brouillard salin, et la question d’un chimiste spécialiste de la corrosion. Seuls ces deux derniers atteignent le facteur omis.

Ce dernier point appelle d’ailleurs une précision capitale sur la @prop:independance : la relation entre indépendance et coût est une tendance forte, non une loi sans exception.

::: {.nuance titre="Une tendance forte, pas une loi d’airain"}
Dire que le coût d’un comparateur augmente avec son indépendance exprime une tendance générale, non une nécessité mécanique. Certains comparateurs sont à la fois peu coûteux et très décalés par rapport au cadre du producteur : la question naïve d’un observateur extérieur (« dans quelle atmosphère cette ferrure va-t-elle servir ? »), une évaluation rapide d’ordre de grandeur, l’appel à une loi de conservation (masse, énergie, bilan comptable), ou encore un modèle grossier issu d’une autre famille de méthodes.

Leur véritable prix ne tient pas au temps de calcul ni au coût d’un banc d’essai ; il tient à la *comparabilité* et à la *prise en compte*. Pour que l’objection du spécialiste de la corrosion morde sur le dossier du bureau d’études, il faut traduire un taux d’attaque chimique en perte d’épaisseur, puis en contrainte mécanique, et convaincre l’équipe de réviser un plan déjà bouclé. Repérer ces comparateurs à la fois bon marché et décalés — et accepter de payer le travail de traduction qui leur donne prise — est une part essentielle de l’art de placer les contrôles.
:::

Deux traditions très éloignées, le génie des logiciels critiques et l’écologie théorique, convergent sur la leçon de la @prop:independance. En biologie des populations, Richard Levins formulait l’espoir placé dans la multiplicité des modèles par une phrase restée célèbre : « notre vérité est à l’intersection de mensonges indépendants » [@levins1966]. Mais Steven Orzack et Elliott Sober [@orzack1993], comme William Wimsatt [@wimsatt1981], ont rappelé la condition qui fait tenir cette formule : des modèles faux sur des points différents ne se corrigent mutuellement *que pourvu qu’ils ne partagent pas la même hypothèse simplificatrice* sur le phénomène décisif. Lorsque tous les modèles écartent tacitement le même mécanisme, leur intersection ne révèle aucune vérité robuste ; elle ne fait que répéter le mensonge commun avec l’autorité trompeuse du nombre.

C’est exactement ce qu’a montré, de manière expérimentale, une étude devenue classique en sûreté logicielle : même lorsque l’on paie le prix fort pour faire écrire plusieurs programmes séparément, l’indépendance ne se décrète pas tant que tous les auteurs partagent un même énoncé de départ.

::: {.cas titre="Vingt-sept versions issues d’une même spécification : l’expérience de Knight et Leveson"}
Pour tester l’hypothèse selon laquelle des équipes indépendantes produisent des logiciels dont les erreurs sont statistiquement indépendantes, John Knight et Nancy Leveson ont conduit en 1986 une expérience devenue une référence en sûreté de fonctionnement [@knightleveson1986]. Vingt-sept versions distinctes d’un même programme ont été développées séparément par des programmeurs différents à partir d’une seule et même spécification écrite.

Si les défauts de programmation étaient survenus indépendamment d’une version à l’autre, deux ou trois versions choisies au hasard auraient dû n’échouer ensemble sur une même entrée qu’avec une probabilité infime, conformément au calcul en parallèle de la boîte à outils. Lorsqu’on a soumis les vingt-sept programmes à un grand jeu de cas d’essai, le résultat a nettement démenti cette hypothèse : plusieurs versions ont échoué simultanément sur certaines entrées difficiles bien plus souvent que ne le prévoyait l’indépendance [@knightleveson1986].

Pourquoi cette convergence ? Parce que les vingt-sept développeurs partageaient l’énoncé du problème, les zones ambiguës ou pièges subtils cachés dans sa formulation, les cas limites peu intuitifs et les réflexes courants de leur formation. Produire séparément à partir d’une spécification commune garantit une certaine diversité de détail, mais ne rend pas les angles morts indépendants vis-à-vis de ce que la spécification elle-même suggère, complique ou laisse dans l’ombre.
:::

## Composer des étapes spécialisées {#sec:ch08-composer}

Les systèmes techniques réels ne se réduisent presque jamais à un modèle unique contrôlé par un autre modèle. Pour atteindre des objectifs qui dépassent les capacités d’un seul outil ou d’une seule discipline, les ingénieurs décomposent le problème et assemblent des modules spécialisés en séquence.

L’ingénierie multiphysique en fournit l’image la plus nette. Pour dimensionner une pièce de turbine, un échangeur thermique ou un bouclier aéronautique, un premier modèle résout les transferts thermiques et calcule un champ de températures ; un deuxième modèle importe ce champ pour calculer les déformations et les contraintes mécaniques ; un troisième évalue, à partir de ces contraintes, l’endommagement ou la durée de vie des matériaux. Chacune de ces étapes mobilise ses propres équations, ses propres hypothèses simplificatrices et ses propres spécialistes : aucune ne pourrait absorber facilement l’ensemble des trois physiques en un seul bloc.

Cette division du travail répond à une contrainte de fond : plus l’objectif visé se situe haut dans la hiérarchie des finalités — « garantir la sûreté de l’installation », « dimensionner cet ouvrage pour trente ans de service », « qualifier le vol d’une sonde spatiale » —, moins cet objectif se laisse enfermer dans une formulation formelle unique et exhaustive. On le morcelle donc en sous-problèmes locaux plus nets, confiés à des maillons successifs, tandis que les résultats intermédiaires circulent toujours plus vite d’un maillon au suivant.

Une chaîne de montage automobile éclaire à la fois la force et le péril de cette organisation. À chaque poste, un opérateur ou un automate exécute avec précision une tâche locale bien définie : serrer au couple, souder un élément, contrôler une cote géométrique. Pourtant, aucun poste pris isolément ne voit si l’ensemble ainsi assemblé convient à la route réelle sur laquelle le véhicule devra rouler. Dès que les résultats circulent d’un module à l’autre sans confrontation extérieure, l’architecture même de l’assemblage détermine comment les angles morts se combinent.

## Chaînes contre contrôles croisés {#sec:ch08-chaines-controles}

Deux architectures élémentaires s’opposent lorsque l’on câble plusieurs composants entre eux, et elles produisent sur les angles morts des effets rigoureusement inverses.

Dans une **chaîne**, les composants sont disposés en série : chaque composant tient pour acquis le résultat du précédent afin de produire le sien, et les angles morts se cumulent. Une erreur commise à la première étape traverse les suivantes si aucune ne s’avise de la remettre en cause, et chaque interface entre deux étapes ajoute sa propre occasion d’erreur.

Dans un **contrôle croisé**, à l’inverse, les composants sont disposés en parallèle : deux composants se prononcent sur la même affirmation et l’on relève leurs désaccords ; seul l’angle mort commun subsiste. Ici, le deuxième composant ne reprend pas la sortie du premier comme une donnée d’entrée indiscutée : il produit une estimation ou un avis sur la même question, de sorte qu’un désaccord signale une erreur probable d’au moins l’un des deux.

::: {.proposition #prop:chaines titre="Une chaîne cumule les angles morts ; un contrôle croisé ne garde que ceux qui sont communs" statut="résultat sous hypothèses"}
Dans une chaîne, l’angle mort global contient la réunion des angles morts de tous les composants, augmentée des erreurs nées aux interfaces. Dans un contrôle croisé, sous l’hypothèse d’une comparaison fidèle et d’une prise en compte effective des désaccords, l’angle mort se réduit à ce que les deux composants partagent ; si les défauts d’attention sont indépendants, la probabilité d’échappement est le produit des probabilités d’oubli individuelles, alors qu’elle vaut $1$ pour toute cause d’erreur commune à tous les contrôleurs.
:::

Le mécanisme se comprend sans calcul. Dans une chaîne à quatre étapes — par exemple mesure, lissage, calcul thermique, calcul mécanique —, chaque maillon se fie à ce qu’il reçoit pour se concentrer sur sa propre tâche : il suffit qu’un seul maillon laisse passer une cause d’erreur qu’il ne sait pas voir, ou que le passage d’un maillon au suivant introduise une erreur de raccordement, pour que le résultat final soit faussé. À l’opposé, lorsque deux composants examinent la même question en parallèle et que leurs désaccords sont instruits, une cause d’erreur qui n’échappe qu’à l’un des deux déclenche un signal. Seules traversent sans contradiction les causes auxquelles *tous deux* sont aveugles — ainsi que celles dont le protocole de comparaison ne sait pas faire apparaître l’écart.

Une illusion courante mérite ici d’être dissipée avant toute formalisation. On croit souvent dresser un contrôle croisé en demandant à un même modèle, à un même programme ou à la même équipe de « relire » ou de « revérifier » son propre résultat. Sur un organigramme, le second passage dessine une boucle parallèle qui ressemble à un contrôle croisé. Vis-à-vis de son propre angle mort, c’est en réalité une copie : le contrôleur partage le même cadre, les mêmes variables et les mêmes omissions que le producteur, de sorte que l’intersection de leurs angles morts redonne l’angle mort initial tout entier (@sec:ch07). Ce geste reste utile pour rattraper une étourderie passagère ; contre un défaut inscrit dans le cadre ou dans l’architecture du composant, il ajoute une signature, non une protection.

Le modèle M1, le premier des modèles formels du livre (@sec:ch00-architecture), rassemble sous forme algébrique la composition des angles morts et les probabilités d’échappement dans les deux architectures, en explicitant ses hypothèses.

::: {.formel titre="Modèle M1 : angles morts et échappement dans les chaînes et les contrôles croisés"}
Soit un ensemble de causes d’erreur possibles. Chaque composant $i$ possède un angle mort $B_i$ (ensemble des causes qu’il ne peut pas enregistrer, sur lesquelles son taux d’oubli vaut $1$) ; sur les causes qui n’appartiennent pas à son angle mort, un contrôleur $i$ laisse néanmoins échapper une erreur donnée avec une probabilité $m_i$ (notation locale à ce modèle). On note $B_{\text{interfaces}}$ l’ensemble des erreurs qui naissent aux jonctions entre composants sans appartenir à aucun maillon isolé, et $B_{\text{cmp}}$ l’angle mort de la comparaison, c’est-à-dire les causes pour lesquelles le protocole de confrontation ne parvient pas à exprimer un désaccord.

1. **Chaîne de $N$ composants en série.** Chaque composant tient le résultat précédent pour acquis. Une erreur échappe à la chaîne dès qu’elle appartient à l’angle mort d’un maillon quelconque ou naît à une interface :
   $$B_{\text{chaîne}} \supseteq \bigcup_{i=1}^{N} B_i \cup B_{\text{interfaces}}.$$ {#eq:ch08-chaine-angle-mort}
   L’inclusion peut être stricte lorsque l’enchaînement de plusieurs maillons crée des défauts d’interaction absents de chaque étape prise séparément.
2. **Contrôle croisé d’un producteur $1$ par un contrôleur $2$.** Une erreur passe au travers du contrôle croisé lorsque sa cause échappe au producteur *et* que le contrôleur ou la comparaison échoue à la faire ressortir (même un désaccord exprimé ne l’arrête que sous réserve de prise en compte, @def:prise-en-compte) :
   $$B_{\text{croisé}} = B_1 \cap (B_2 \cup B_{\text{cmp}}).$$ {#eq:ch08-croise-angle-mort}
   Lorsque la comparaison est parfaite ($B_{\text{cmp}} = \emptyset$), l’angle mort du contrôle croisé se ramène à l’intersection $B_1 \cap B_2$.
3. **Probabilité d’échappement sur une erreur donnée.** Considérons une affirmation fausse soumise à un ensemble de contrôleurs, en supposant la comparaison fidèle et chaque désaccord suivi d’effet :
   - si les contrôleurs manquent l’erreur de manière conditionnellement indépendante, chacun avec une probabilité $m_i$, la probabilité qu’elle franchisse tous les contrôles vaut :
     $$\Pr(\text{échappement}) = \prod_{i} m_i ;$$ {#eq:ch08-echappement-indep}
   - si l’erreur relève d’une cause commune appartenant à l’angle mort de tous les contrôleurs ($m_i = 1$ pour chacun), alors :
     $$\Pr(\text{échappement}) = 1,$$ {#eq:ch08-echappement-commun}
     quel que soit le nombre de contrôleurs ajoutés.

**Hypothèses explicites.** L’@eq:ch08-croise-angle-mort suppose que tout désaccord effectivement exprimé par la comparaison entraîne une prise en compte (@def:prise-en-compte) ; si celle-ci fait défaut, la probabilité d’échappement remonte à $1$. L’@eq:ch08-echappement-indep suppose l’indépendance conditionnelle des oublis des différents contrôleurs sachant que l’affirmation est fausse ; dès qu’une cause est partagée, cette indépendance cède et ramène vers l’@eq:ch08-echappement-commun. Le modèle du contrôleur au @sec:ch09 enrichira cette construction en y ajoutant la force probante d’un contrôle réussi, l’effet des fausses alertes et une prise en compte imparfaite.
:::

L’exemple quantitatif suivant chiffre l’écart entre chaîne sans contrôle et contrôle croisé à chaque étape, puis montre comment un modeste facteur omis partagé suffit à plafonner le bénéfice d’un contrôle entre pairs.

::: {.exemple-quantitatif titre="Chaînes sans contrôle et contrôles croisés face à un facteur omis partagé"}
**Mise en place.** Les chiffres retenus sont illustratifs : ils visent à rendre lisible le comportement du modèle M1, non à estimer la fiabilité d’un procédé réel. Considérons une séquence de $N$ étapes successives. À chaque étape, le producteur commet une erreur propre avec une probabilité $p = 6\,\%$, indépendamment des autres étapes. On compare deux organisations : dans la première, les étapes s’enchaînent sans contrôle ; dans la seconde, chaque étape fait l’objet d’un contrôle croisé en parallèle par un pair qui présente la même compétence que le producteur et laisse échapper chaque erreur indépendante avec la probabilité $m = p = 6\,\%$, indépendamment de lui. On suppose la comparaison fidèle ($B_{\text{cmp}} = \emptyset$) et la prise en compte assurée. On introduit enfin $q$, probabilité d’un facteur omis partagé qui frappe simultanément toutes les étapes et appartient à l’angle mort commun du producteur et du pair contrôleur : on examine les deux cas $q = 0\,\%$ et $q = 3\,\%$.

![Probabilité d’échec d’une chaîne en fonction du nombre d’étapes $N$ (de $1$ à $8$), pour une erreur indépendante par étape $p = 6\,\%$ et un pair qui laisse passer chaque erreur indépendante avec la même probabilité. En orange, la chaîne sans contrôle ($q = 0\,\%$ en trait plein, $q = 3\,\%$ en tirets) ; en bleu, chaque étape contrôlée en parallèle par un pair ($q = 0\,\%$ en trait plein, $q = 3\,\%$ en tirets). À $N = 4$, le contrôle croisé abaisse la part indépendante de $21{,}9\,\%$ à $1{,}43\,\%$, mais lorsque $q = 3\,\%$, la probabilité d’échec reste à $4{,}39\,\%$ et le facteur partagé intervient dans $68{,}3\,\%$ des défaillances restantes.](figures/ch08-chaine.pdf){#fig:ch08-chaine width=90%}

**Calcul.**

::: {.inclure fichier="tableaux/ch08-chaine.md"}
:::

Dans le modèle M1, lorsque l’erreur par étape est $p$ et le facteur omis partagé $q$ (indépendant des erreurs locales), une chaîne sans contrôle de $N$ étapes échoue avec la probabilité $1 - (1 - q)(1 - p)^N$. Lorsque chaque étape est contrôlée par un pair dont les oublis indépendants ont pour probabilité $p$, la probabilité qu’une erreur locale échappe à une étape vaut $p^2 = 0{,}06^2 = 0{,}0036$, et la chaîne contrôlée échoue avec la probabilité $1 - (1 - q)(1 - p^2)^N$. Pour $N = 4$ étapes et $q = 0\,\%$, on obtient $1 - 0{,}94^4 \approx 21{,}9\,\%$ sans contrôle et $1 - (1 - 0{,}0036)^4 \approx 1{,}43\,\%$ avec contrôle croisé. Pour $N = 4$ et $q = 3\,\%$, ces probabilités passent respectivement à $1 - 0{,}97 \times 0{,}94^4 \approx 24{,}3\,\%$ et $1 - 0{,}97 \times (1 - 0{,}0036)^4 \approx 4{,}39\,\%$. La fraction des défaillances résiduelles dans lesquelles intervient le facteur partagé vaut alors $q / 0{,}0439\dots \approx 68{,}3\,\%$.

**Lecture.** Le @tbl:ch08-chaine et la @fig:ch08-chaine font apparaître deux leçons complémentaires. D’abord, sur les erreurs indépendantes, le contrôle croisé par un pair est remarquablement efficace : pour $N = 4$ étapes, il fait chuter la composante indépendante de l’échec de 21,9 % à 1,43 %. Ensuite, dès qu’un facteur omis partagé $q$ de 3 % entre en jeu, la chaîne sans contrôle monte de 21,9 % à 24,3 % — une différence modeste au regard du bruit des erreurs locales —, alors que la chaîne contrôlée fait plus que tripler son risque résiduel, passant de 1,43 % à 4,39 %. Dans ces conditions, 68,3 % des défaillances qui subsistent malgré les contrôles croisés impliquent le facteur partagé $q$. Multiplier les relectures de pairs qui partagent le même cadre ne permet pas d’abaisser ce plancher : comme le résume l’@eq:ch08-echappement-commun, pour toute cause commune aux contrôleurs, la probabilité d’échappement reste égale à $1$. L’exemple repose sur des hypothèses fortes — indépendance des oublis locaux, comparabilité parfaite, prise en compte systématique de chaque désaccord — et ne dit pas ce qu’il advient lorsque la rareté des erreurs détériore l’écoute des alertes ou lorsque la comparaison elle-même est altérée : ces deux effets occupent la suite de ce chapitre et le @sec:ch09.
:::

Deux précisions s’imposent pour éviter de surinterpréter l’@eq:ch08-croise-angle-mort et la tension entre indépendance et comparabilité.

::: {.nuance titre="Deux précisions sur l’angle mort du contrôle croisé"}
La première précision touche à la forme même de l’@eq:ch08-croise-angle-mort : on écrit $B_{\text{croisé}} = B_1 \cap (B_2 \cup B_{\text{cmp}})$, et non $(B_1 \cap B_2) \cup B_{\text{cmp}}$. Pourquoi cette parenthèse importe-t-elle ? Parce que l’imperfection de la comparaison ($B_{\text{cmp}}$) ne nuit qu’aux erreurs que le producteur n’a pas su éviter ni repérer lui-même, c’est-à-dire celles qui appartiennent à $B_1$. Si une erreur n’appartient pas à $B_1$, le producteur la voit et ne l’émet pas : elle n’apparaît pas du seul fait que le protocole de comparaison n’aurait pas su l’exprimer. À l’inverse, dès qu’une cause appartient à $B_1$, il suffit soit que le contrôleur ne la voie pas non plus ($B_2$), soit que la comparaison échoue à la traduire ($B_{\text{cmp}}$), pour qu’elle passe au travers.

La seconde précision concerne le choix d’un bon contrôleur. En combinant la @prop:independance et l’@eq:ch08-croise-angle-mort, on voit deux forces tirer en sens contraires à mesure que le contrôleur s’éloigne du cadre du producteur : l’angle mort partagé $B_1 \cap B_2$ tend à se rétrécir, tandis que l’angle mort de la comparaison $B_1 \cap B_{\text{cmp}}$ tend à s’élargir. Ce double mouvement *suggère* qu’il existe une distance optimale — ni un jumeau qui ne voit rien de neuf, ni un étranger si éloigné que le dialogue casse —, mais le modèle n’*établit* aucun optimum. Calculer un tel point d’équilibre exigerait de connaître les formes quantitatives exactes des deux courbes en fonction de la distance entre cadres, ce qui varie d’un domaine à l’autre et ne se déduit pas d’un schéma général.
:::

## Le blanchiment aux interfaces {#sec:ch08-blanchiment}

Si les contrôles croisés réduisent si nettement la part des erreurs indépendantes, pourquoi tant de systèmes techniques et organisationnels qui réunissent pourtant des équipes différentes finissent-ils par se comporter comme de simples chaînes, accumulant les angles morts jusqu’à l’accident ? L’une des raisons principales se tient exactement à la jonction entre les composants : c’est le blanchiment.

::: {.definition #def:blanchiment titre="Blanchiment"}
Le **blanchiment** est la perte des conditions d’un résultat au moment où il change de mains : une conclusion conditionnelle arrive au maillon suivant comme un fait établi.
:::

Reprenons la notation $A \cap (\dots) \rightarrow B$ introduite au @sec:ch01 et au @sec:ch02. Au bureau ou dans le code du producteur, le résultat $B$ est encore accompagné des conditions explicites $A$ qui le soutiennent, de ses hypothèses de validité, de ses réserves et de sa marge d’incertitude. Mais lorsque ce résultat franchit une interface pour servir d’entrée au composant suivant, ces conditions restent sur la rive : seul $B$ passe la frontière.

L’ingénierie multiphysique en offre un exemple quotidien. Un modèle thermique calcule le champ de températures d’une pièce sous une série d’hypothèses explicites — fonctionnement permanent, convection naturelle, contact parfait entre deux surfaces — et avec une large incertitude sur les coefficients d’échange. Ce champ est ensuite exporté vers le modèle de mécanique des structures sous la forme d’un simple tableau de nombres nus, sans mention des hypothèses de calcul ni des bornes d’erreur. L’équipe de mécanique qui reçoit ce fichier n’a plus rien à quoi comparer ces températures : elle ne sait pas qu’elles supposent un fonctionnement permanent alors que la pièce subit un choc thermique transitoire, ni qu’une autre hypothèse de contact déplacerait fortement la carte des températures. Elle ne peut que prendre le tableau comme un fait acquis.

Le phénomène s’accentue le long des chaînes longues. Au bout d’une séquence de cinq étapes — mesure, filtrage, interpolation, modèle intermédiaire, calcul final —, la valeur de sortie s’affiche avec huit chiffres significatifs dans un tableur, ou sous la forme d’une phrase nette et sans réserve dans une note de synthèse. Sous cette apparence lisse et précise dort tout un empilement d’hypothèses non propagées que personne en aval ne peut plus relire.

La perte de la sonde spatiale *Mars Climate Orbiter*, évoquée au @sec:ch00, illustre de façon dramatique ce que provoque le blanchiment à une interface.

::: {.cas titre="Les nombres nus de Mars Climate Orbiter"}
Le 23 septembre 1999, la sonde *Mars Climate Orbiter* disparut lors de sa manœuvre d’insertion en orbite autour de Mars, après avoir suivi une trajectoire trop basse dans la haute atmosphère martienne [@mco1999]. Tout au long du transit, un programme au sol, `SM_FORCES`, avait calculé l’effet de petites poussées de correction des propulseurs et transmis ces valeurs par un fichier de sortie à l’équipe chargée de la navigation.

Alors que la spécification d’interface exigeait des impulsions exprimées en newton-secondes ($\text{N}\cdot\text{s}$), conformément au Système international, le programme `SM_FORCES` les écrivait en livres-force-secondes ($\text{lbf}\cdot\text{s}$), soit un écart d’un facteur proche de 4,45 [@mco1999]. Or les nombres franchissaient l’interface nus, dépourvus de toute mention d’unité à l’intérieur même du fichier transmis. L’indication de l’unité ne figurait que dans un document d’interface rédigé à part, si bien que ni le logiciel récepteur ni les étapes suivantes n’avaient les moyens de repérer automatiquement l’incompatibilité des unités. Le @sec:ch10 reviendra sur cet épisode pour examiner le rôle qu’y jouait la spécification écrite.
:::

Au regard des cinq conditions de détection établies au @sec:ch06 (@sec:ch06-cinq-conditions), le diagnostic du blanchiment est sans ambiguïté : le blanchiment détruit la *comparabilité* à chaque interface. Même lorsqu’un maillon situé en aval aurait la compétence voulue pour se tromper autrement — pour détecter qu’un champ thermique suppose un état permanent inadéquat, ou qu’une poussée exprimée en unités anglo-saxonnes contredit le Système international —, la disparition des conditions dans les données transmises l’empêche d’opérer le rapprochement. Dans les termes du modèle M1 (@eq:ch08-croise-angle-mort), le blanchiment fait enfler $B_{\text{cmp}}$ jusqu’à neutraliser l’indépendance potentielle du maillon suivant et rabattre le système tout entier sur une chaîne aveugle.

Deux cousins proches du blanchiment des hypothèses produisent aux interfaces des effets analogues et méritent d’être distingués avec netteté :

- *L’effacement des unités et des définitions.* Comme le montre *Mars Climate Orbiter*, laisser tomber l’unité d’une grandeur, la convention de signe d’un repère ou la définition d’une catégorie (par exemple ce que recouvre exactement un code clinique d’un hôpital à l’autre, @sec:ch02) ruine la comparabilité exactement au même titre que l’oubli des hypothèses du modèle.
- *L’effacement de la provenance.* Laisser tomber l’origine d’une affirmation — d’où vient ce chiffre, quelle observation ou quel modèle l’a produit, par quelles mains il est passé — compromet une autre propriété : le jugement d’indépendance. Faute de connaître la provenance des résultats qui arrivent sur son bureau, personne ne peut plus savoir si deux avis concordants émanent de comparateurs qui se trompent autrement, ou s’il s’agit de deux reprises déguisées d’une seule et même source. Cet effet collectif, qui dépasse la simple interface entre deux composants, sera analysé au @sec:ch16.

À ce point de la @sec:partie-2, nous disposons de la géométrie des contrôles : nous savons que les chaînes cumulent les angles morts, que les contrôles croisés n’en gardent que la part commune lorsque la comparabilité et la prise en compte tiennent, et que le blanchiment détruit la première aux interfaces. Il reste à examiner ce qui donne à un contrôle sa force probante, et ce qui arrive aux alertes — et à ceux qui les reçoivent — lorsque les erreurs deviennent rares : ce sera l’objet du @sec:ch09.

::: {.question}
Aux interfaces de votre chaîne de travail, les résultats voyagent-ils accompagnés de leurs hypothèses, de leurs unités, de leur incertitude et de leur origine, ou comme des nombres et des textes nus ?
:::

## Points clés {.points-cles}

- L’indépendance d’un contrôle est toujours relative à une classe d’erreurs : ce qu’une affirmation et son comparateur ont en commun, aucun des deux ne peut le contrôler chez l’autre.
- Cette indépendance tend à se payer en comparabilité — donc en travail de mise en correspondance pour que l’objection porte —, même s’il existe des comparateurs à la fois peu coûteux et décalés dont le coût réside surtout dans la traduction et l’écoute.
- Une chaîne en série cumule les angles morts de tous ses composants et les erreurs nées aux interfaces ; un contrôle croisé en parallèle réduit l’angle mort à l’intersection des angles morts du producteur et du contrôleur, augmentée des écarts que la comparaison ne sait pas exprimer.
- Même lorsque des contrôles croisés indépendants écrasent la part des erreurs locales, un facteur omis commun à tous les contrôleurs demeure hors de leur portée, avec une probabilité d’échappement égale à $1$.
- Le blanchiment — la perte des conditions, des unités ou de la provenance au moment où un résultat change de mains — détruit la comparabilité aux interfaces et transforme en chaîne fragile un ensemble que l’on croyait contrôlé.
