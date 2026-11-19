# Décider d’après ce que l’on croit {#sec:ch04}

Le @sec:ch02 a établi que nous agissons d’après une représentation, et que c’est à l’action, non à la représentation, que le monde répond. Le @sec:ch03 a montré qu’une probabilité attribue un poids à des mondes possibles, et qu’une issue isolée ne suffit pas à juger celui qui l’avait annoncée. Il reste à passer du jugement à l’acte. Ce chapitre présente la règle de décision de Savage et en tire un seuil de probabilité d’échec qui ne dépend que du rapport entre ce que l’on risque de perdre et ce que l’on espère gagner. Il montre que ce seuil tend vers zéro lorsque la perte devient démesurée, distingue la décision prise une seule fois de la décision répétée, et pose une question qu’il laisse ouverte jusqu’au @sec:ch17.

## L’utilité espérée subjective de Savage {#sec:ch04-ues}

Une fois des poids accordés aux mondes possibles, comment choisir ce que l’on va faire ? On pourrait vouloir s’en remettre aux fréquences observées et retenir l’option qui a le mieux réussi par le passé. Mais une décision se prend toujours *avant* que le monde ait répondu, souvent dans une situation qui ne se répétera pas et pour laquelle il n’existe aucune série de cas comparables. Au moment de trancher, le décideur ne connaît ni l’issue ni sa fréquence. Il dispose seulement de ce qu’il juge plausible et de ce qu’il peut gagner ou perdre.

La théorie classique de la décision combine ces deux éléments dans une règle, l’**utilité espérée subjective (UES)**, formulée par Leonard Savage [-@savage1954] : on choisit l’acte dont l’utilité espérée est la plus élevée, l’espérance étant calculée avec ses propres probabilités. Une décision s’y décrit par quatre éléments :

- *les actes*, c’est-à-dire les options ouvertes au moment du choix : prendre le départ sur un voilier léger ou sur un voilier renforcé, lancer une mise en production ou la différer ;
- *les états du monde*, sur lesquels le décideur n’a plus de prise une fois son choix arrêté : le mât tient ou casse, la mise en production se passe bien ou provoque une panne. Ce sont les mondes possibles de la @sec:ch03-mondes-possibles ;
- *les conséquences*, qui résultent de la rencontre d’un acte et d’un état : une victoire, un démâtage suivi d’un remorquage coûteux, une course sans incident mais plus lente ;
- *les probabilités et les utilités* : le poids que le décideur, d’après sa représentation, accorde à chaque état, et la valeur, ou *utilité*, qu’il attache à chaque conséquence.

Deux mots demandent une précision. Le premier est *utilité*. L’utilité ne se confond pas avec une somme d’argent : la perte d’une somme qui ruinerait une entreprise pèse bien plus lourd que le gain de la même somme lorsqu’elle s’ajoute à un bénéfice déjà confortable, et la perte d’une vie n’a pas d’équivalent monétaire. L’utilité mesure l’importance qu’attache à chaque conséquence celui qui s’y expose. Le second est *subjective*. Comme à la @sec:ch03-raisonner-envers, le mot ne veut pas dire arbitraire : les probabilités sont celles du décideur, relatives à ce qu’il sait, aux hypothèses qu’il retient et au cadre dans lequel il raisonne.

Savage a donné à cette règle un fondement axiomatique [@savage1954]. Si les préférences d’un décideur entre des actes aux issues incertaines respectent quelques axiomes de cohérence, il se comporte *comme s’il* attribuait une probabilité à chaque état du monde et une utilité à chaque conséquence, puis choisissait l’acte d’utilité espérée maximale. La cohérence relie ainsi ce que l’on croit à ce que l’on fait. Elle ne dit rien, en revanche, de ce qui fonde la croyance.

::: {.outils titre="L’utilité espérée subjective : actes, états et conséquences"}
Notons $\mathcal{A}$ l’ensemble des actes envisagés et $\Omega$ l’ensemble des états du monde retenus, qui joue le rôle de l’ensemble des issues de la @sec:ch01-probabilite. Si l’état $\omega \in \Omega$ se réalise, l’acte $a \in \mathcal{A}$ produit la conséquence $c(a, \omega)$, dont l’utilité vaut $U\bigl(c(a, \omega)\bigr)$. Le décideur pondère les états par une probabilité personnelle $\Pr(\cdot)$, avec $\sum_{\omega \in \Omega} \Pr(\omega) = 1$ (une intégrale remplace la somme lorsque les états forment un continuum). L’utilité espérée de l’acte $a$ vaut alors :

$$\mathrm{UE}(a) = \sum_{\omega \in \Omega} \Pr(\omega)\,U\bigl(c(a, \omega)\bigr),$$

et la règle de Savage prescrit de choisir un acte qui rend $\mathrm{UE}(a)$ maximale. Elle s’appuie sur des probabilités personnelles plutôt que sur des fréquences pour une raison simple : la décision se prend avant que le monde ait répondu, et ne peut donc reposer que sur ce que l’on croit à ce moment-là.

Deux propriétés serviront dans la suite. D’abord, remplacer $U$ par $\alpha\,U + \beta$, avec $\alpha > 0$, ne change pas l’ordre des actes : l’origine et l’unité de l’échelle d’utilité sont libres, et seuls comptent les rapports entre écarts d’utilité. Ensuite, la somme ne porte que sur les états qui figurent dans $\Omega$, pondérés par les probabilités que le décideur leur accorde dans son cadre. Un état qu’il n’a pas envisagé n’y figure pas, et n’y pèse donc rien.
:::

Appliquée au choix entre une option sûre et une option risquée, cette règle conduit à un résultat simple : un seuil de probabilité d’échec au-delà duquel l’option risquée cesse d’être préférable.

## La course à la voile {#sec:ch04-course-voile}

Retrouvons M. X et M. Y, que nous avons laissés sur le quai à la @sec:ch03-prevision-previsionniste. Avant le départ d’une course au large, chacun doit choisir entre deux bateaux : un *voilier léger*, rapide mais sollicité près de ses limites, et un *voilier renforcé*, plus lent mais à peu près incassable. Le voilier léger offre une meilleure chance de victoire. S’il casse en mer, en revanche, il faudra le faire remorquer, et le remorquage coûtera beaucoup plus cher que le prix promis au vainqueur.

Prenons le voilier renforcé comme option sûre : il procure une utilité $U_{\text{sûr}}$, tenue pour certaine. Le voilier léger conduit à deux issues. S’il tient jusqu’à l’arrivée, c’est le *succès*, d’utilité $U_{\text{succès}}$ supérieure à $U_{\text{sûr}}$ ; s’il casse, c’est l’*échec*, d’utilité $U_{\text{échec}}$ inférieure à $U_{\text{sûr}}$. Mesurons les deux enjeux à partir de l’option sûre : le gain en cas de succès vaut $\Delta U = U_{\text{succès}} - U_{\text{sûr}}$, et la perte en cas d’échec $L = U_{\text{sûr}} - U_{\text{échec}}$ ; ce sont deux quantités positives. On appelle **rapport des enjeux** le quotient $L/\Delta U$ de la perte en cas d’échec par le gain en cas de succès, tous deux mesurés par rapport à l’option sûre.

Notons enfin $p$ la probabilité d’échec du voilier léger telle que l’estime le décideur, qui attribue donc la probabilité $1 - p$ au succès. D’après la règle de l’UES, prendre le départ sur le voilier léger procure l’utilité espérée $(1 - p)\,U_{\text{succès}} + p\,U_{\text{échec}}$. Celle-ci dépasse $U_{\text{sûr}}$ si et seulement si le gain espéré $(1 - p)\,\Delta U$ l’emporte sur la perte espérée $p\,L$, c’est-à-dire si $p$ reste au-dessous du **seuil $p^\ast$**, probabilité d’échec au-delà de laquelle l’option risquée cesse d’être préférable :

$$p^\ast = \frac{\Delta U}{\Delta U + L} = \frac{1}{1 + L/\Delta U}$$ {#eq:ch04-seuil}

Au sens de Savage, il est donc rationnel de prendre le départ sur le voilier léger si $p < p^\ast$, et de choisir le voilier renforcé si $p > p^\ast$ ; lorsque $p = p^\ast$, les deux options se valent.

L’inégalité $(1 - p)\,\Delta U > p\,L$ s’écrit aussi $(1 - p)/p > L/\Delta U$, ce qui en donne une lecture par les cotes (@sec:ch01-bayes) : l’option risquée l’emporte lorsque la cote du succès contre l’échec, c’est-à-dire le rapport de leurs probabilités, dépasse le rapport des enjeux. Si la casse coûte vingt-cinq fois ce que rapporte le succès, il faut juger le succès plus de vingt-cinq fois plus probable que la casse. Lorsque la perte égale le gain ($L/\Delta U = 1$), le seuil vaut $1/2$ : on prend le risque dès que le succès paraît plus probable que l’échec. Dès que la perte dépasse le gain, le seuil passe au-dessous de 50 %, et il baisse d’autant plus que le rapport entre les deux est grand. La seconde forme de l’@eq:ch04-seuil montre en outre que le seuil ne dépend ni de la valeur absolue des enjeux ni de l’échelle choisie pour l’utilité : seul compte le rapport sans dimension $L/\Delta U$.

::: {.formel titre="Dérivation du seuil de décision"}
Le modèle repose sur quatre hypothèses.

1. *Issue binaire de l’option risquée.* Le voilier léger tient, avec la probabilité $1 - p$ (utilité $U_{\text{succès}}$), ou casse, avec la probabilité $p \in [0, 1]$ (utilité $U_{\text{échec}}$).
2. *Option sûre.* Le voilier renforcé procure une utilité certaine $U_{\text{sûr}}$. S’il lui reste un risque infime, on le suppose déjà compté dans $U_{\text{sûr}}$, qui est alors elle-même une utilité espérée.
3. *Enjeux de part et d’autre.* $U_{\text{échec}} < U_{\text{sûr}} < U_{\text{succès}}$, si bien que $\Delta U = U_{\text{succès}} - U_{\text{sûr}} > 0$ et $L = U_{\text{sûr}} - U_{\text{échec}} > 0$.
4. *Décision sur la croyance.* La seule probabilité qui intervient est $p$, celle que le décideur forme dans sa représentation. La dérivation ne suppose rien sur l’accord entre $p$ et ce que le monde réserve.

L’option risquée est strictement préférée si et seulement si :

$$(1 - p)\,U_{\text{succès}} + p\,U_{\text{échec}} > U_{\text{sûr}}.$$

Écrivons $U_{\text{sûr}} = (1 - p)\,U_{\text{sûr}} + p\,U_{\text{sûr}}$ et retranchons ce terme des deux membres :

$$(1 - p)\,(U_{\text{succès}} - U_{\text{sûr}}) - p\,(U_{\text{sûr}} - U_{\text{échec}}) > 0,$$

soit $(1 - p)\,\Delta U - p\,L > 0$, ou encore $\Delta U > p\,(\Delta U + L)$. Comme $\Delta U + L > 0$, la division conserve le sens de l’inégalité :

$$p < \frac{\Delta U}{\Delta U + L} = \frac{1}{1 + L/\Delta U} = p^\ast,$$

ce qui établit l’@eq:ch04-seuil. Le seuil décroît quand le rapport des enjeux croît. Il tend vers $1$ quand $L/\Delta U \to 0$ (perte négligeable devant le gain) et vers $0$ quand $L/\Delta U \to +\infty$ (perte écrasante devant le gain). Lorsque $L/\Delta U$ est grand devant $1$, $p^\ast \approx \Delta U / L$ : le seuil est à peu près l’inverse du rapport des enjeux. Enfin, remplacer $U$ par $\alpha\,U + \beta$, avec $\alpha > 0$, multiplie $\Delta U$ et $L$ par $\alpha$, et laisse donc $L/\Delta U$ et $p^\ast$ inchangés.
:::

Revenons sur le quai. M. X et M. Y préparent la même course, lisent le même bulletin météorologique et examinent le même voilier léger. Supposons qu’ils fassent aussi le même bilan des enjeux : pour l’un comme pour l’autre, la perte en cas de casse vaut vingt-cinq fois le gain en cas de succès, soit $L/\Delta U = 25$. Le seuil vaut alors $p^\ast = 1/(1 + 25) = 1/26$, soit environ 3,85 %.

Nous avons vu à la @sec:ch03-prevision-previsionniste que, devant les mêmes faits, les deux navigateurs pèsent différemment l’arrière-plan tacite $\mathcal{T}$ : M. X estime le risque de casse à 5 %, M. Y à 0,1 %, et rien, avant la course, ne permet de dire lequel a raison. L’@eq:ch04-seuil leur dicte pourtant des décisions opposées :

- M. Y compare 0,1 % à 3,85 % : il se trouve nettement au-dessous du seuil et prend, rationnellement, le départ sur le voilier léger ;
- M. X compare 5 % à 3,85 % : il se trouve au-dessus du seuil et choisit, tout aussi rationnellement, le voilier renforcé.

Deux décideurs qui poursuivent le même but, font le même bilan des enjeux et appliquent la même règle peuvent donc agir en sens contraires, dès lors que leurs estimations de $p$ se situent de part et d’autre du seuil. Leur désaccord ne vient ni d’une faute de calcul ni d’intérêts divergents : il vient de leurs représentations. La décision peut d’ailleurs basculer par l’un ou l’autre des deux termes de la comparaison. Si une information nouvelle porte l’estimation de M. Y au-dessus de 3,85 % (la règle de Bayes, sous la forme de l’@eq:ch01-bayes-cotes, dit de combien cette information doit déplacer l’estimation), il choisira le voilier renforcé. Si une baisse du prix du remorquage ou une hausse de la récompense abaisse assez le rapport des enjeux pour que le seuil dépasse 5 %, M. X prendra le départ sur le voilier léger sans avoir changé d’avis sur le bateau. La règle ne se substitue ni à la représentation ni aux valeurs du décideur : elle traduit leur rencontre en un acte.

## La roulette russe et l’effondrement du seuil {#sec:ch04-roulette-russe}

Que devient le seuil lorsque l’asymétrie des enjeux grandit de plusieurs ordres de grandeur ? Dès que la perte dépasse largement le gain, l’@eq:ch04-seuil donne $p^\ast \approx \Delta U / L$ : le seuil est à peu près l’inverse du rapport des enjeux. Multiplier ce rapport par dix divise donc à peu près par dix la probabilité d’échec que l’on peut accepter, et le seuil tend vers zéro lorsque le rapport des enjeux tend vers l’infini.

La *roulette russe* pousse cette logique jusqu’à sa limite. On propose à un joueur une somme d’argent pour presser une fois la détente d’un revolver appuyé contre sa tempe. L’échec, c’est la mort ; le succès, un gain d’argent ordinaire. Le rapport des enjeux est démesuré ; fixons-le, pour l’illustration, à $L/\Delta U = 10\,000$. L’@eq:ch04-seuil donne alors $p^\ast = 1/10\,001$, soit environ 0,0100 %, un peu moins d’une chance sur dix mille.

Avec un barillet de six chambres dont une seule est chargée, la probabilité d’échec, une chance sur six, dépasse ce seuil de très loin, et personne de sensé ne joue. À un tel rapport des enjeux, la règle de l’UES n’autorise à presser la détente que dans deux cas. Ou bien le gain en jeu est immense, comme celui de sauver une vie, et le rapport des enjeux cesse d’être démesuré. Ou bien le joueur est à peu près certain que la chambre placée face au percuteur est vide, au point d’estimer la probabilité d’échec très au-dessous du seuil, par exemple à 0,001 %, soit une chance sur cent mille.

L’exemple quantitatif qui suit place la course à la voile et la roulette russe sur une même courbe, pour montrer comment le seuil s’effondre quand le rapport des enjeux grandit.

::: {.exemple-quantitatif titre="Seuil de décision et rapport des enjeux : course à la voile et roulette russe"}
**Mise en place.** Les valeurs sont illustratives : elles sont choisies pour faire voir le comportement du seuil $p^\ast$ de l’@eq:ch04-seuil, non pour décrire une course ou un jeu réels. Les deux navigateurs font face au même rapport des enjeux, égal à 25, avec le voilier renforcé pour option sûre ; M. Y estime la probabilité d’échec du voilier léger à 0,1 %, M. X à 5 %. Le joueur de roulette russe fait face à un rapport des enjeux de 10 000 ; persuadé que la chambre est vide, il estime la probabilité d’échec à 0,001 %. Dans les trois situations, l’issue est binaire (le bateau tient ou casse, le coup part ou non), l’option sûre est bien définie, et la décision ne dépend que de l’estimation $p$ du décideur.

![Seuil de décision $p^\ast$ en fonction du rapport des enjeux $L/\Delta U$, sur deux axes logarithmiques. Le décideur choisit l’option risquée lorsque son estimation $p$ se trouve au-dessous de la courbe. Les droites en tirets marquent les estimations de M. X (5 %) et de M. Y (0,1 %). Pour un rapport des enjeux de 25, le seuil vaut 3,85 % : M. Y, au-dessous, part ; M. X, au-dessus, renonce. Pour la roulette russe (rapport de 10 000), le seuil tombe à 0,0100 %.](figures/ch04-seuil.pdf){#fig:ch04-seuil width=90%}

**Calcul.**

::: {.inclure fichier="tableaux/ch04-seuil.md"}
:::

Pour un rapport des enjeux de 25, l’@eq:ch04-seuil donne $p^\ast = 1/(1 + 25) = 1/26$, soit 3,85 % : M. Y, à 0,1 %, se trouve au-dessous du seuil et part ; M. X, à 5 %, se trouve au-dessus et renonce. Pour un rapport de 10 000, $p^\ast = 1/(1 + 10\,000)$, soit 0,0100 % : le joueur, qui estime le risque à 0,001 %, reste au-dessous et presse la détente.

**Lecture.** Le @tbl:ch04-seuil et la @fig:ch04-seuil font voir deux choses. D’abord, à rapport des enjeux égal, la même règle place M. X et M. Y de part et d’autre du seuil sans que ni l’un ni l’autre raisonne mal : leur désaccord tient tout entier à leurs estimations. Ensuite, dès que le rapport des enjeux dépasse quelques dizaines, la courbe se confond presque, sur les axes logarithmiques, avec une droite de pente $-1$ : chaque fois que le rapport des enjeux est multiplié par dix, la probabilité d’échec acceptable est divisée par dix. L’exemple ne montre pas, en revanche, que les estimations de 0,1 % ou de 0,001 % tiennent compte de toutes les façons dont le bateau peut casser ou le coup partir. Il compare le seuil à l’estimation du décideur, et à elle seule ; il suppose en outre une issue binaire et une option sûre bien définie.
:::

## Décider une seule fois ou à répétition {#sec:ch04-decision-unique}

Un lecteur familier des usages statistiques de la théorie de la décision pourrait trouver ici une consolation. Si M. Y choisit le voilier léger chaque fois que $p < p^\ast$, et si ses estimations sont bien calibrées, ses gains l’emporteront à la longue sur ceux de l’option sûre. Cette consolation suppose pourtant que la décision se répète.

Prenons des décisions répétées dans des conditions stables : celle du citadin qui consulte chaque matin la prévision de pluie pour savoir s’il emporte son parapluie (@sec:ch03-calibration-historique), celle d’un organisme de crédit qui instruit chaque mois des milliers de dossiers comparables, celle d’un service qui trie un flux quotidien de demandes. L’utilité espérée s’y retrouve, à la longue, dans la moyenne des résultats, car la répétition fournit une population d’épreuves semblables. Une erreur sur un cas isolé se fond dans le bilan, pourvu qu’aucune perte ne soit ruineuse à elle seule. Et si les probabilités annoncées sont trop optimistes, ou si le seuil est mal réglé, l’écart entre les prévisions consignées et les fréquences observées finit par apparaître dans l’historique : on peut alors recalibrer la règle pour les cas suivants.

Il en va autrement d’une **décision unique**, c’est-à-dire d’une décision prise sans série d’essais comparables, si bien qu’une issue malheureuse ne peut être compensée par d’autres cas : la réponse du monde n’arrive qu’après l’acte, trop tard pour le corriger. Prendre le départ d’une course au large sur un voilier léger, pratiquer une opération chirurgicale exceptionnelle, arrêter l’architecture d’un grand système d’information, engager une action irréversible : aucune de ces décisions n’appartient à une série dont la loi des grands nombres compenserait les mauvais tirages. Le bateau casse ou franchit la ligne, une seule fois, et la perte $L$ tombe tout entière sur cette traversée. Que l’estimation de M. Y, 0,1 %, soit inférieure au seuil de 3,85 % signifie seulement que, compte tenu de sa représentation, le départ l’emporte en utilité espérée. Ce n’est en rien une promesse que *cette* traversée se passera bien.

La réponse du monde n’arrive d’ailleurs pas seulement trop tard : elle renseigne mal. Nous avons vu à la @sec:ch03-prevision-previsionniste qu’une issue isolée départage à peine deux estimations. Si le bateau arrive intact, M. Y ne saura pas s’il le doit à un gréement sans défaut ou à la chance, dans un monde où M. X avait vu juste. S’il casse, le remorquage est dû avant toute révision du jugement. La calibration aide là où les décisions se répètent et où les cas passés éclairent les suivants. Une décision unique demande autre chose, que le @sec:ch17 examinera.

## La question laissée ouverte {#sec:ch04-question-ouverte}

Rapprochons la thèse du @sec:ch02 et la règle établie dans ce chapitre. L’UES dit comment décider de façon cohérente *à l’intérieur* d’une représentation : le rapport des enjeux fixe le seuil $p^\ast$, et l’option retenue est la meilleure compte tenu des probabilités que le décideur accorde aux mondes possibles qu’il envisage.

Mais d’où vient $p$ ? D’une représentation (@def:representation) construite dans un cadre fini (@def:cadre), qui n’a retenu que certaines grandeurs, certaines catégories et certains scénarios d’échec, et qui a laissé tout le reste dans l’arrière-plan tacite. Tant que les risques en jeu sont ceux que la représentation envisage, comme un coup de vent annoncé par le bulletin ou la fatigue ordinaire des matériaux, l’@eq:ch04-seuil arbitre correctement entre prudence et gain.

Supposons maintenant que la conviction du joueur de roulette russe, qui estime la probabilité d’échec à 0,001 %, vienne d’un cadre où une chambre chargée n’avait pas sa place : aucun des éléments qu’il a retenus ne lui permettait de l’envisager. Ou que l’estimation de M. Y, 0,1 %, repose sur des fiches techniques qui ne disent rien d’un défaut caché dans le mât. Rien, dans le calcul de l’utilité espérée, ne signale le danger : la règle compare au seuil le nombre $p$ que fournit la représentation, constate que $p < p^\ast$ et conclut au départ.

Or le monde, une fois l’acte engagé, ne consulte pas nos probabilités (@sec:ch02-monde-action). Le percuteur frappe ce qui se trouve réellement dans la chambre, et la houle éprouve le mât tel qu’il est, avec tout ce que le cadre avait laissé dans l’arrière-plan tacite. Telle est la question que ce chapitre laisse ouverte : *comment décider, lorsque l’enjeu est sans appel, alors que notre propre calcul ne peut rien dire de ce que notre cadre a manqué ?* Il faudra d’abord comprendre ce que mesurent au juste nos chiffres d’incertitude, et ce qui peut nous détromper avant qu’il soit trop tard ; le @sec:ch17 reviendra ensuite aux décisions uniques pour y répondre.

::: {.nuance titre="Le monde ne consulte pas nos probabilités"}
La règle de l’UES est rationnelle au regard de ce que croit le décideur, non de ce qui arrivera. Une décision bien prise peut mal tourner, et une décision imprudente bien finir : une issue isolée ne juge pas mieux une décision qu’elle ne jugeait une prévision au @sec:ch03. On pourrait vouloir corriger la règle en exigeant de ne partir que si le risque *véritable* est inférieur à $p^\ast$. Mais une règle de décision ne peut s’appliquer qu’à ce que contient la représentation : ce que le cadre a omis, le décideur n’a, par définition, aucun moyen de le lire pour le comparer au seuil. Le @sec:ch17 cherchera comment tenir compte de cette part inconnue sans prétendre la mesurer.

L’habitude de raisonner à l’envers (@sec:ch03-raisonner-envers) offre déjà une prise. Elle invite à se demander quelle variation cachée, si on la connaissait, renverserait la décision, et donc à regarder l’écart entre $p$ et $p^\ast$. Pour M. Y, avec un rapport des enjeux de 25, il suffirait d’un risque ignoré d’à peine quatre points de pourcentage, s’il était connu, pour changer sa décision ; pour le joueur de roulette russe, avec un rapport de 10 000, d’un peu moins d’un centième de point. Savoir que la décision tient à si peu ne fait pas apparaître pour autant la chambre chargée.
:::

::: {.question}
Pour votre prochain déploiement irréversible, quel est le rapport des enjeux $L/\Delta U$, et quel seuil $p^\ast$ en découle ?
:::

## Points clés {.points-cles}

- Nous décidons d’après ce que nous croyons : l’utilité espérée subjective (UES) pondère l’utilité des conséquences par nos propres probabilités, parce que la décision se prend avant que le monde ait répondu.
- Face à une option sûre, une option risquée n’est préférable que si la probabilité d’échec estimée $p$ reste au-dessous du seuil $p^\ast = 1/(1 + L/\Delta U)$, qui baisse quand le rapport des enjeux $L/\Delta U$ augmente et tend vers zéro quand la perte devient démesurée.
- Deux décideurs également rationnels, devant les mêmes enjeux, peuvent prendre des décisions opposées si leurs estimations de $p$ se situent de part et d’autre du seuil.
- Une décision unique ne bénéficie d’aucune moyenne protectrice : le monde ne livre qu’une issue, après l’acte, sans consulter nos estimations, et la calibration n’aide que lorsque les décisions se répètent.
- Si la conviction qui place $p$ au-dessous de $p^\ast$ vient d’un cadre qui a laissé de côté un élément décisif, rien dans le calcul ne le signale : cette question, laissée ouverte ici, sera reprise au @sec:ch17.
