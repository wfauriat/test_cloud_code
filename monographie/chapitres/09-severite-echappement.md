# Sévérité, fausses alertes et probabilité d’échappement {#sec:ch09}

Le @sec:ch06 a établi qu’une erreur n’est détectée que lorsqu’une affirmation rencontre un comparateur qui existe, se trompe autrement qu’elle, lui est comparable, arrive à temps et fait l’objet d’une prise en compte effective (@sec:ch06-cinq-conditions) ; si l’une de ces conditions manque, l’erreur échappe. Le @sec:ch08 a montré qu’un contrôle croisé réduit l’angle mort (@def:angle-mort) aux seules causes que partagent le producteur et le contrôleur (@prop:chaines). À l’aide de la règle de Bayes sous forme de cotes rappelée au @sec:ch01, ce chapitre donne une mesure quantitative à la détection et à l’échappement. Il montre à quelle condition un contrôle réussi constitue un indice probant, pourquoi l’amélioration d’un producteur rend fausses la plupart des alertes d’un contrôleur fixe, pourquoi la réaction aux alertes relève du comportement plutôt que du seul calcul, et comment le risque résiduel se décompose en taux d’erreur multiplié par probabilité d’échappement — refermant ainsi la @sec:partie-2 avant d’aborder la @sec:partie-3.

## Taux de base et valeur prédictive positive {#sec:ch09-taux-base-vpp}

Un test très fiable peut néanmoins tromper presque à chaque fois qu’il sonne l’alerte, dès lors que ce qu’il cherche est rare. Pour le voir sans appareil formel, partons d’un exemple médical choisi pour l’illustration. On soumet une population à un dépistage systématique d’une affection qui touche 1 % des personnes examinées. Cette fréquence préalable, avant toute mesure, est le **taux de base** de l’affection dans la population (en médecine, on parle de prévalence).

Le test utilisé possède deux caractéristiques établies sur des cas connus. Lorsqu’une personne est réellement atteinte, le test donne un résultat positif dans 90 % des cas : c’est sa **sensibilité**, notée $s$, c’est-à-dire, de manière générale, la probabilité qu’un contrôle signale une erreur quand il y en a une. Lorsqu’une personne est saine, le test donne tout de même un résultat positif par erreur dans 5 % des cas : en médecine on appelle ce chiffre taux de faux positifs, et nous le nommerons plus généralement **taux de fausses alertes**, noté $f$, soit la probabilité qu’un contrôle signale une erreur quand il n’y en a pas.

Un patient reçoit un résultat positif. Quelle est la probabilité qu’il soit réellement atteint ? Au premier abord, avec une sensibilité de 90 % et seulement 5 % de fausses alertes, on s’attend à un chiffre élevé. Imaginons pourtant mille personnes soumises à ce dépistage :

- au taux de base de 1 %, dix personnes portent l’affection ; le test, sensible à 90 %, en repère neuf ;
- les neuf cent quatre-vingt-dix autres personnes sont saines ; avec 5 % de fausses alertes, le test produit en moyenne $49{,}5$ résultats positifs à tort ;
- au total, sur ces mille personnes, le test délivre $9 + 49{,}5 = 58{,}5$ résultats positifs, parmi lesquels neuf seulement correspondent à des personnes réellement atteintes.

La proportion de vrais cas parmi les résultats positifs vaut donc $9 / 58{,}5 = 2/13$, soit environ 15,4 %. On appelle **valeur prédictive positive (VPP)** la proportion des alertes qui correspondent à de vraies erreurs (ou, dans un dépistage, à de vrais cas). Ici, plus de cinq alertes sur six sont fausses, non parce que le test fonctionne mal, mais parce que la population saine est quatre-vingt-dix-neuf fois plus nombreuse que la population malade (@tbl:ch09-depistage).

::: {.inclure fichier="tableaux/ch09-depistage.md"}
:::

::: {.outils titre="Taux de base, vrais positifs et règle de Bayes"}
Notons $D$ l’état recherché (présence de l’affection ou erreur) et $T^+$ une alerte positive, avec taux de base $\Pr(D)$, sensibilité $s = \Pr(T^+ \mid D)$ et taux de fausses alertes $f = \Pr(T^+ \mid \bar{D})$. D’après la formule des probabilités totales (@eq:ch01-totale), la probabilité globale d’une alerte vaut $\Pr(T^+) = \Pr(D)\,s + \Pr(\bar{D})\,f$. La valeur prédictive positive est donc :

$$\mathrm{VPP} = \Pr(D \mid T^+) = \frac{\Pr(D)\,s}{\Pr(D)\,s + \bigl(1 - \Pr(D)\bigr)\,f}.$$

L’écriture en cotes de l’@eq:ch01-bayes-cotes rend le mécanisme immédiat. La cote *a priori* vaut $\Pr(D)/\bigl(1 - \Pr(D)\bigr) = 1/99$. Le rapport de vraisemblance d’un résultat positif vaut $\Lambda(T^+) = s / f = 0{,}90 / 0{,}05 = 18$. La cote *a posteriori* vaut donc $(1/99) \times 18 = 2/11$, ce qui donne une probabilité de $2/(2 + 11) = 2/13 \approx 15{,}4\,\%$. Tant que le taux de base reste faible devant le rapport $f/s$ (ici $0{,}05/0{,}90 \approx 5{,}6\,\%$), les fausses alertes l’emportent en nombre sur les vraies détections, même lorsque $\Lambda(T^+)$ est élevé.
:::

Ce mécanisme arithmétique ne dépend en rien de la biologie. Remplaçons le patient par une affirmation issue d’un calcul, d’un modèle ou d’un collaborateur, et le test biologique par un contrôleur ou une procédure de contrôle : les mêmes nombres gouvernent la confiance que mérite un accord comme le crédit que mérite une alerte.

## Sévérité d’un contrôle {#sec:ch09-severite}

Commençons par le cas rassurant en apparence : le contrôleur ne signale rien, il concorde avec le producteur. À la @sec:ch06-accord-desaccord, nous avons remarqué qu’un tel accord ne prouve rien si le contrôleur n’avait pas réellement la possibilité de contredire une affirmation fausse. La règle de Bayes permet de préciser exactement combien pèse un contrôle réussi.

Notons $E$ l’événement « l’affirmation est fausse », $\bar{E}$ l’événement « l’affirmation est juste », et $A$ l’événement « le comparateur concorde avec l’affirmation » (aucune alerte n’est émise ; l’événement contraire, $\bar{A}$, est l’émission d’une alerte). D’après l’@eq:ch01-bayes-cotes, observer cet accord multiplie la cote de justesse de l’affirmation par le rapport de vraisemblance de l’accord :

$$\text{cote}(\bar{E} \mid A) = \text{cote}(\bar{E}) \times \frac{\Pr(A \mid \bar{E})}{\Pr(A \mid E)}$$ {#eq:ch09-accord-cotes}

Regardons le dénominateur $\Pr(A \mid E)$ : c’est la probabilité que le contrôleur ne signale rien et valide l’affirmation alors même qu’elle est fausse. Si le comparateur avait de toute façon donné son accord dans ce cas — parce qu’il est trop indulgent, parce qu’il répète les mêmes calculs ou parce qu’il partage l’angle mort du producteur (@sec:ch08) —, alors $\Pr(A \mid E)$ est proche de $\Pr(A \mid \bar{E})$, ou vaut $1$ comme lui. Le rapport de vraisemblance de l’@eq:ch09-accord-cotes est alors égal à $1$ : le contrôle ajoute une signature au dossier, et aucun indice en faveur de l’affirmation.

Inversement, un contrôle passé sans alerte ne déplace la confiance vers $\bar{E}$ que si $\Pr(A \mid E)$ est petit, c’est-à-dire si une alerte était probable dans l’hypothèse où l’affirmation aurait été fausse. La philosophe des sciences Deborah Mayo a formulé ce principe sous le nom de *critère de sévérité* [@mayo1996; @mayo2018].

::: {.definition #def:severite titre="Sévérité"}
La **sévérité** exprime la valeur probante d’un contrôle passé sans alerte : un tel contrôle n’est probant que dans la mesure où il aurait donné l’alerte si l’affirmation avait été fausse [@mayo1996; @mayo2018].
:::

On la mesure par $\Pr(\bar{A} \mid E)$, la probabilité que le contrôle donne l’alerte quand l’affirmation est fausse.

L’@eq:ch09-accord-cotes relie directement la sévérité aux grandeurs introduites à la section précédente. Pour un contrôleur de sensibilité $s = \Pr(\bar{A} \mid E)$ et de taux de fausses alertes $f = \Pr(\bar{A} \mid \bar{E})$, la probabilité de ne pas signaler d’erreur quand l’affirmation est juste vaut $1 - f$, et la probabilité de n’émettre aucune alerte quand elle est fausse vaut $1 - s$. L’accord multiplie donc la cote de justesse par $(1 - f)/(1 - s)$. Lorsque $s = 0$ et $f = 0$ — par exemple pour une auto-vérification face à une variable omise du cadre (@sec:ch07) ou une simple copie du calcul initial —, le multiplicateur vaut $1$ ; il vaut encore $1$ si le contrôleur répond sans discernement, en alertant aussi souvent sur une affirmation juste que sur une affirmation fausse ($s = f$). À l’opposé, lorsqu’un contrôle atteint une sensibilité de 90 % avec 5 % de fausses alertes, un accord multiplie la cote par $0{,}95 / 0{,}10 = 9{,}5$.

Comme l’indépendance au @sec:ch08 (@prop:independance), la sévérité est toujours relative à une classe d’erreurs donnée. Un second calcul mené par un collègue avec les mêmes hypothèses de la résistance des matériaux exerce un contrôle sévère contre les fautes d’algèbre ou d’unité, car il les aurait repérées ; sa sévérité est nulle contre un mécanisme de dégradation absent des deux cadres. Demander si un contrôle est sévère oblige toujours à préciser : *sévère contre quelles erreurs ?*

## Le piège des fausses alertes {#sec:ch09-fausses-alertes}

Passons maintenant du côté des désaccords, c’est-à-dire des cas où le contrôleur lève une alerte. Imaginons un producteur très fiable qui ne se trompe que dans 1 % des cas, et un relecteur humain ou logiciel qui commet une erreur d’appréciation dans 10 % des cas, indépendamment du producteur — c’est-à-dire qu’il se trompe dans 10 % des cas aussi bien lorsqu’il juge une affirmation juste (10 % de fausses alertes) que lorsqu’il examine une affirmation fausse (10 % d’oubli).

Supposons que les deux parties examinent un grand nombre de dossiers. Quand un désaccord éclate entre le producteur et le relecteur, qui a raison ? Calculons la fréquence des deux situations de désaccord :

- le producteur a tort et le relecteur a raison dans $0{,}01 \times (1 - 0{,}10) = 0{,}009$, soit 0,9 % de l’ensemble des dossiers ;
- le producteur a raison et le relecteur a tort dans $(1 - 0{,}01) \times 0{,}10 = 0{,}099$, soit 9,9 % des dossiers.

Ensemble, les désaccords couvrent $0{,}009 + 0{,}099 = 0{,}108$, soit 10,8 % des dossiers. Parmi eux, la proportion de cas où le producteur avait raison vaut $0{,}099 / 0{,}108 = 11/12$, soit 91,7 % (@tbl:ch09-desaccords). Plus de neuf fois sur dix, le désaccord vient d’une fausse alerte du relecteur, et non d’une faute du producteur.

::: {.inclure fichier="tableaux/ch09-desaccords.md"}
:::

Ce renversement (le désaccord accuse le plus souvent le relecteur, non le producteur) crée un piège contre-intuitif à mesure que la qualité de la production augmente. Supposons un contrôleur fixe, doté d’une sensibilité $s$ et d’un taux de fausses alertes $f$, placé en aval d’un producteur dont le taux d’erreur (introduit au @sec:ch06) vaut $P(E) = \Pr(E)$, noté $P(\text{faux})$ dans les tableaux et les graphiques. En reprenant la formule vue à la @sec:ch09-taux-base-vpp, la valeur prédictive positive du contrôleur s’écrit :

$$\mathrm{VPP} = \frac{P(E)\,s}{P(E)\,s + \bigl(1 - P(E)\bigr)\,f}$$ {#eq:ch09-vpp}

Quand le producteur progresse et que $P(E)$ diminue, le numérateur $P(E)\,s$ baisse au même rythme. Au dénominateur, en revanche, le terme des fausses alertes $\bigl(1 - P(E)\bigr)\,f$ reste voisin de $f$, car $1 - P(E)$ demeure proche de $1$. Si le taux d’erreur du producteur tombe nettement au-dessous de $f/s$, la $\mathrm{VPP}$ s’effondre : sans que le contrôleur se soit dégradé d’un pouce, la majorité des alertes qu’il émet deviennent fausses.

Le prix concret de cette chute se lit directement dans l’inverse de la $\mathrm{VPP}$. Si une fraction $\mathrm{VPP}$ des alertes correspond à de vraies erreurs, attraper une erreur réelle exige d’ouvrir en moyenne $1/\mathrm{VPP}$ alertes. Dans l’exemple du dépistage à 15,4 % de $\mathrm{VPP}$, chaque vrai cas détecté coûte environ six ou sept examens complémentaires ; dans celui du relecteur, où la $\mathrm{VPP}$ n’est que de $1 - 91{,}7\,\% = 8{,}3\,\%$, chaque vraie faute du producteur coûte douze examens. Pour qu’un contrôle reste crédible lorsque les producteurs deviennent plus exacts, il ne suffit donc pas qu’il soit indépendant (sensibilité $s$ élevée) : il doit aussi être *précis*, c’est-à-dire que son taux de fausses alertes $f$ doit baisser à peu près au même rythme que $P(E)$.

## Ce que l’on fait des alertes {#sec:ch09-comportement-alertes}

Devant une alerte dont on sait qu’elle est fausse neuf fois sur dix, deux réactions hâtives guettent l’organisation : rejeter le travail du producteur dès que le contrôleur proteste — ce qui gaspille neuf fois sur dix un travail juste —, ou finir par balayer ses remarques d’un revers de main — ce qui laisse passer la dixième, celle qui était fondée.

Les études expérimentales sur la réponse humaine aux systèmes d’alarme montrent ce qui se produit le plus souvent en pratique. James Bliss, Richard Gilson et John Deaton [@bliss1995] ont montré que, placés devant des alarmes dont la fiabilité varie, la plupart des opérateurs ajustent la fréquence à laquelle ils réagissent à la fiabilité perçue du signal : si une alarme ne correspond à un danger réel que dans une fraction modérée des cas, ils ne la vérifient qu’environ à cette fréquence. Ce comportement, dit d’**appariement des probabilités**, sous-tend l’effet bien connu du berger qui « crie au loup » : à force d’entendre sonner pour rien, on cesse de vérifier à chaque appel.

Il importe ici de ne pas confondre la probabilité conditionnelle et la décision. La règle de Bayes fixe la valeur prédictive positive : si le producteur se trompe dans 1 % des cas et le relecteur dans 10 %, un observateur bayésien conclut simplement que 8,3 % des désaccords trahissent une vraie erreur. La règle de Bayes ne lui dicte en aucune manière de ne vérifier que 8,3 % des alertes. La prise en compte (@def:prise-en-compte) — que nous noterons $u \in \left[0, 1\right]$ et qui désigne la proportion des alertes effectivement examinées et suivies d’effet — relève d’une politique d’action et d’un comportement humain, non d’un théorème de probabilités.

Quelle devrait être, en bonne méthode, la réponse à un désaccord ? Comme l’a établi la @sec:ch06-accord-desaccord, un désaccord indique qu’au moins l’une des deux voies s’est trompée, jamais laquelle. La réponse cohérente avec le cadre de ce livre n’est ni d’ignorer l’alerte, ni de s’y plier mécaniquement, mais de *résoudre le désaccord* à l’aide d’un troisième comparateur, au prix moyen de $1/\mathrm{VPP}$ enquêtes par erreur réelle interceptée.

Savoir s’il faut payer ce coût est une décision d’utilité espérée subjective au sens du @sec:ch04. Une fois l’alerte déclenchée, la probabilité que l’affirmation soit fausse n’est plus le taux de base $P(E)$, mais la $\mathrm{VPP}$ (@eq:ch09-vpp). On compare alors le gain attendu de l’enquête — éviter une perte $L$ pondérée par $\mathrm{VPP}$ — au coût de l’arbitrage par un tiers. Pour une décision unique aux enjeux élevés, où la perte en cas d’échec dépasse de plusieurs ordres de grandeur le prix d’une contre-expertise (situation où le seuil $p^\ast$ de l’@eq:ch04-seuil s’effondre vers zéro), même une $\mathrm{VPP}$ de quelques pour cent justifie amplement d’examiner chaque alerte ($u = 1$). En revanche, dans un flux répétitif où les enjeux unitaires sont modestes et le temps de relecture compté, un effondrement de la $\mathrm{VPP}$ expose à l’appariement des probabilités et à l’érosion de la prise en compte.

## Risque = taux d’erreur × probabilité d’échappement {#sec:ch09-risque-echappement}

Rassemblons maintenant les fils pour exprimer le risque réel d’un système composé d’un producteur et de ses contrôles. Parce que le monde répond à l’action et non à la représentation (@sec:ch02), une erreur commise dans un brouillon, une note ou un calcul ne cause aucun tort tant qu’elle reste sur le papier : elle ne devient dommageable que si elle franchit tous les contrôles et gouverne l’action.

Notons toujours $E$ l’événement « l’affirmation est fausse », et $C$ l’événement « un contrôle la contredit et l’arrête avant l’action » (au sens des cinq conditions du @sec:ch06). La probabilité qu’une affirmation soit à la fois fausse et suivie d’effet se factorise par la règle du produit (@sec:ch01-probabilite-conditionnelle) :

$$\Pr(E \cap \bar{C}) = \Pr(E) \times \Pr(\bar{C} \mid E)$$ {#eq:ch09-risque}

Le premier facteur, $\Pr(E) = P(E)$ (également noté $P(\text{faux})$ sur les graphiques et tableaux), est le taux d’erreur du producteur. Le second, $\Pr(\bar{C} \mid E)$, est la probabilité d’échappement (@def:echappement) : la probabilité qu’une affirmation fausse parvienne jusqu’à l’action sans qu’un désaccord ait été détecté et pris en compte à temps.

Cette décomposition en deux facteurs révèle une asymétrie profonde dans la manière dont on évalue d’ordinaire la fiabilité des méthodes et des outils. Les batteries d’évaluations comparatives, les classements de performance et les courbes d’amélioration notent, par construction, le producteur seul sur un jeu d’épreuves. Ils mesurent donc le premier facteur, $P(E)$ — à quelle fréquence le producteur donne-t-il une réponse fausse ? — et ne disent rien du second. Toute l’ingénierie de la sûreté et toute l’analyse de la @sec:partie-2 portent au contraire sur le second facteur, la probabilité d’échappement, qui détermine quelle part des erreurs survit jusqu’à l’acte.

Un jeu de chiffres illustratifs, déjà croisé au @sec:ch00, montre pourquoi le premier facteur ne suffit jamais (@tbl:ch09-taux-echappement). Imaginons deux systèmes :

- dans le premier, le producteur se trompe souvent (taux d’erreur de 10 %), mais ses affirmations passent devant un contrôleur qui se trompe autrement que lui et ne laisse échapper que 1 % des erreurs ; la part des affirmations fausses suivies d’effet vaut $10\,\% \times 1\,\% = 0{,}1\,\%$ ;
- dans le second, le producteur est dix fois plus exact (taux d’erreur de 1 %), mais le contrôle laisse passer 90 % des erreurs ; la part des affirmations fausses suivies d’effet atteint $1\,\% \times 90\,\% = 0{,}9\,\%$.

Le producteur dix fois plus fiable forme ici un système neuf fois plus risqué.

::: {.inclure fichier="tableaux/ch09-taux-echappement.md"}
:::

De plus, l’abaissement de $P(E)$ et l’échappement ne sont pas indépendants : comme l’ont montré les sections [-@sec:ch09-fausses-alertes] et [-@sec:ch09-comportement-alertes], lorsque $P(E)$ baisse avec un contrôleur inchangé, la $\mathrm{VPP}$ recule, ce qui peut abaisser la prise en compte $u$ et faire monter en retour la probabilité d’échappement $\Pr(\bar{C} \mid E)$.

Dans le prolongement du modèle d’angles morts introduit au @sec:ch08, on peut chiffrer cette dépendance à l’aide de deux paramètres de fiabilité du contrôleur. Notons $c \in \left[0, 1\right]$ la part des erreurs du producteur dont la cause est partagée avec le contrôleur — causes qui relèvent de leur angle mort commun et que le contrôleur manque toujours —, et $m \in \left[0, 1\right]$ la probabilité que le contrôleur oublie une erreur sur les autres causes (fraction $1 - c$). La sensibilité du contrôleur vaut alors $s = (1 - c)(1 - m)$. Comme seule une proportion $u$ des alertes est examinée et résolue, la probabilité qu’une erreur soit arrêtée vaut $s\,u$, et la probabilité d’échappement devient $1 - s\,u$, ce qui donne le risque résiduel $P(E)\,(1 - s\,u)$. L’encadré suivant regroupe le modèle complet et ses hypothèses.

::: {.formel titre="Modèle M1 : sensibilité, VPP, prise en compte et échappement"}
Poursuivons le modèle M1 du @sec:ch08 pour un producteur de taux d’erreur $P(E) \in \left[0, 1\right]$ et un contrôleur binaire qui émet ou non une alerte sur chaque affirmation, en supposant la comparaison fidèle ($B_{\text{cmp}} = \emptyset$ dans l’@eq:ch08-croise-angle-mort) :

- une fraction $c \in \left[0, 1\right]$ des causes d’erreur appartient à l’angle mort commun du producteur et du contrôleur : ces erreurs partagées sont toujours manquées par le contrôleur ;
- sur la fraction complémentaire $1 - c$ des causes d’erreur (non partagées), le contrôleur oublie tout de même une erreur avec la probabilité $m \in \left[0, 1\right]$ ;
- lorsque l’affirmation est juste ($\bar{E}$), le contrôleur émet une fausse alerte avec un taux $f \in \left[0, 1\right]$.

Une erreur n’est signalée par le contrôleur que si sa cause n’est pas partagée (probabilité $1 - c$) et s’il ne l’oublie pas par ailleurs (probabilité $1 - m$). La sensibilité du contrôleur vaut donc :

$$s = (1 - c)(1 - m).$$ {#eq:ch09-sensibilite}

La proportion d’alertes correspondant à de vraies erreurs est donnée par l’@eq:ch09-vpp :

$$\mathrm{VPP} = \frac{P(E)\,s}{P(E)\,s + \bigl(1 - P(E)\bigr)\,f},$$

et le nombre moyen d’alertes à examiner par vraie erreur interceptée vaut $1/\mathrm{VPP}$.

Lorsqu’une alerte se déclenche, elle est examinée et résolue avec la probabilité $u \in \left[0, 1\right]$ (prise en compte). Une affirmation fausse est donc arrêtée avec la probabilité $s\,u$, et sa probabilité d’échappement vaut :

$$P(\text{échappement}) = 1 - s\,u = 1 - (1 - c)(1 - m)\,u.$$ {#eq:ch09-echappement}

Même lorsque chaque alerte est résolue ($u = 1$), la probabilité d’échappement reste bornée inférieurement par $1 - s = c + (1 - c)m \ge c$ : les causes partagées $c$ forment un plancher qu’aucune diligence sur les alertes ne peut percer (@eq:ch08-echappement-commun). Enfin, d’après l’@eq:ch09-risque, le risque résiduel — probabilité qu’une affirmation fausse gouverne l’action — s’écrit :

$$R = P(E)\,(1 - s\,u).$$

Nous étudierons deux politiques de prise en compte : l’appariement des probabilités ($u = \mathrm{VPP}$) et l’examen systématique de chaque alerte ($u = 1$).

**Hypothèses explicites.** Ce modèle du contrôleur repose sur trois hypothèses qu’il faut garder visibles :

1. *Indépendance des oublis non partagés.* En dehors de la fraction $c$ des causes partagées, les erreurs du contrôleur surviennent indépendamment de celles du producteur ; le modèle suppose en outre que les désaccords sont comparables et qu’une alerte examinée ($u$) est tranchée exactement par un troisième comparateur.
2. *Taux d’erreur stationnaire.* Le taux $P(E)$ est supposé constant sur la série considérée, et la $\mathrm{VPP}$ à laquelle réagit l’opérateur correspond à ce taux stationnaire.
3. *Appariement des probabilités comme hypothèse comportementale.* L’égalité $u = \mathrm{VPP}$ ne découle pas de la règle de Bayes : elle résume un fait comportemental documenté [@bliss1995], à mettre en regard de la politique $u = 1$.
:::

L’exemple quantitatif qui suit met ce modèle en mouvement sur deux situations contrastées, et montre ce qui advient d’un contrôleur fixe lorsque le producteur devient plus fiable.

::: {.exemple-quantitatif titre="Contrôleur fixe, taux d’erreur décroissant et prise en compte (illustratif)"}
**Mise en place.** Les valeurs ci-dessous sont purement illustratives : elles sont choisies pour isoler les leviers du modèle M1, non pour chiffrer un dispositif réel. On examine deux configurations. Dans la première (*Contrôle entre pairs*), un producteur dont le taux d’erreur $P(\text{faux})$ vaut 10 % est relu par un contrôleur qui partage 10 % de ses causes d’erreur ($c = 0{,}10$), oublie 20 % des autres erreurs ($m = 0{,}20$) et déclenche 5 % de fausses alertes ($f = 0{,}05$). Dans la seconde (*Indépendant et précis*), le producteur ne se trompe plus que dans 2 % des cas, et le contrôleur — qui garde la même part de causes partagées ($c = 0{,}10$) — réduit à la fois son taux d’oubli sur les autres erreurs (10 %) et son taux de fausses alertes (0,5 %). Dans chaque configuration, on compare deux politiques de prise en compte : suivre les alertes à hauteur de la VPP ($u = \mathrm{VPP}$) ou examiner chaque alerte avec un troisième comparateur ($u = 1$). La @fig:ch09-echappement montre comment évoluent l’échappement et le risque résiduel du contrôleur fixe (*Contrôle entre pairs*) lorsque le taux d’erreur du producteur diminue sur plusieurs ordres de grandeur, comparés au cas sans contrôleur.

![Probabilité d’échappement (à gauche) et risque résiduel, c’est-à-dire part des affirmations fausses suivies d’effet (à droite), en fonction du taux d’erreur du producteur $P(\text{faux})$ sur axe horizontal logarithmique, pour un contrôleur fixe ($c = 10\,\%$, $m = 20\,\%$, $f = 5\,\%$). La courbe orange suppose les alertes suivies à hauteur de la VPP ($u = \mathrm{VPP}$), la courbe bleue suppose chaque alerte examinée ($u = 1$), et les points marquent le scénario « Contrôle entre pairs » à $P(\text{faux}) = 10\,\%$ (échappement de 55,7 % contre 28,0 % ; risque de 5,57 % contre 2,80 %, au lieu de 10 % sans contrôleur). À mesure que le producteur devient plus fiable (vers la gauche), la courbe orange se rapproche de la droite grise « sans contrôleur ».](figures/ch09-echappement.pdf){#fig:ch09-echappement width=90%}

**Calcul.** Le @tbl:ch09-echappement rassemble les valeurs exactes des deux configurations.

::: {.inclure fichier="tableaux/ch09-echappement.md"}
:::

Dans le scénario *Contrôle entre pairs*, la sensibilité vaut $s = (1 - 0{,}10)(1 - 0{,}20) = 0{,}72$, soit 72 %. Au taux d’erreur de 10 % et avec un taux de fausses alertes de 5 %, la VPP atteint $0{,}10 \times 0{,}72 / (0{,}10 \times 0{,}72 + 0{,}90 \times 0{,}05)$, soit 61,5 %, ce qui représente 1,6 alerte par vraie erreur attrapée. Si les alertes ne sont suivies qu’à hauteur de la VPP, la probabilité d’échappement vaut 55,7 % et le risque résiduel 5,57 % ; si chaque alerte est examinée, l’échappement tombe à $1 - 0{,}72 = 28{,}0\,\%$ et le risque à 2,80 %, contre 10 % sans contrôleur.

Dans le scénario *Indépendant et précis*, la sensibilité monte à $s = (1 - 0{,}10)(1 - 0{,}10) = 0{,}81$, soit 81 %. Bien que le producteur soit cinq fois plus fiable (taux d’erreur de 2 %), l’abaissement du taux de fausses alertes à 0,5 % porte la VPP à 76,8 %, soit 1,3 alerte par vraie erreur. L’échappement descend alors à 37,8 % sous appariement des probabilités (risque de 0,756 %) et à 19,0 % si chaque alerte est examinée (risque de 0,380 %), contre 2 % sans contrôleur.

**Lecture.** Le @tbl:ch09-echappement et la @fig:ch09-echappement font apparaître trois leviers distincts :

- *La précision garde les alertes lisibles.* Sur la @fig:ch09-echappement, à mesure que $P(\text{faux})$ baisse vers la gauche face au contrôleur fixe, la courbe bleue ($u = 1$) reste horizontale à 28,0 % sur le panneau de gauche, mais la courbe orange ($u = \mathrm{VPP}$) remonte vers l’échappement complet sur ce même panneau et rejoint visuellement, sur le panneau de droite, la ligne grise « sans contrôleur ». Dans le scénario *Indépendant et précis*, ramener le taux de fausses alertes de 5 % à 0,5 % empêche cet effondrement et maintient une VPP de 76,8 % malgré un taux d’erreur de 2 %.
- *L’indépendance élargit ce que le contrôleur peut voir.* Garder les causes partagées à 10 % et ramener l’oubli sur les autres erreurs de 20 % à 10 % élève la sensibilité de 72 % à 81 %, ce qui abaisse le plancher d’échappement lorsque chaque alerte est vérifiée (de 28,0 % à 19,0 %).
- *La prise en compte est le levier caché.* Dans chacune des deux colonnes, passer de l’appariement des probabilités à l’examen de chaque alerte divise presque par deux la probabilité d’échappement (de 55,7 % à 28,0 %, puis de 37,8 % à 19,0 %) et réduit le risque dans les mêmes proportions (de 5,57 % à 2,80 %, puis de 0,756 % à 0,380 %).

Cet exemple ne montre pas comment évolue le risque lorsque les causes partagées $c$ augmentent en même temps que $P(\text{faux})$ diminue, ni ce qui se passe lorsque la comparabilité ou le recours au troisième comparateur échouent. Il repose sur l’hypothèse d’un taux d’erreur stationnaire, de causes non partagées indépendantes, d’un arbitrage exact lorsqu’une alerte est examinée, et sur l’hypothèse comportementale d’appariement des probabilités pour la courbe orange.
:::

::: {.nuance titre="La baisse du taux d’erreur n’érode pas la prise en compte par la seule règle de Bayes"}
Il est tentant de résumer la courbe orange de la @fig:ch09-echappement en affirmant que, « par la règle de Bayes », la baisse du taux d’erreur détruit la prise en compte. Ce raccourci est inexact. La règle de Bayes fixe uniquement la VPP, c’est-à-dire la proportion d’alertes qui signalent une erreur véritable. Ce que l’on fait d’une alerte lorsque sa VPP baisse dépend d’un arbitrage humain ou organisationnel : un opérateur soumis à l’appariement des probabilités réagit moins souvent [@bliss1995], alors qu’un décideur qui applique la règle de l’utilité espérée subjective (@sec:ch04) devant une décision unique aux enjeux élevés examine chaque alerte ($u = 1$).

En outre, dans ce modèle simple à contrôleur fixe, la baisse de $P(E)$ suivie d’une baisse de $u$ rend le contrôleur peu à peu décoratif : le risque $P(E)(1 - s\,u)$ tend vers $P(E)$ par en dessous, sans devenir supérieur au risque sans contrôleur ni croître à lui seul quand $P(E)$ diminue. Le risque total ne peut remonter sous l’effet d’une amélioration apparente que si un autre paramètre change en même temps, en particulier lorsque la part des causes partagées $c$ grandit, comme nous le verrons au @sec:ch16.
:::

Avec ce chapitre s’achève la @sec:partie-2. Des trois incertitudes et de la mesure d’une barre d’erreur jusqu’aux cinq conditions de détection, à l’effet de cause commune du cadre, au compromis entre indépendance et comparabilité, puis à la sévérité, aux fausses alertes et au produit taux d’erreur par probabilité d’échappement, nous disposons désormais d’une théorie des contrôles des représentations finies, édifiée hors de l’informatique récente. La @sec:partie-3 appliquera cette grille à l’empilement des couches logicielles, de la programmation par contrat aux modèles appris — où le @sec:ch12 retrouvera le critère de sévérité face aux réponses répétées d’un modèle. Le @sec:ch16 reviendra ensuite directement sur le modèle du contrôleur pour séparer l’effet des causes partagées de celui des fausses alertes.

::: {.question}
Dans vos dispositifs de contrôle actuels, quelle part des alertes correspond à de vraies erreurs, et comment ces alertes sont-elles traitées en pratique ?
:::

## Points clés {.points-cles}

- Un contrôle passé sans alerte n’est probant que dans la mesure où il aurait donné l’alerte si l’affirmation avait été fausse (sévérité) ; si le comparateur concorde dans tous les cas, l’accord multiplie la cote par un et n’apporte aucune preuve.
- Lorsque les erreurs du producteur deviennent rares devant le taux de fausses alertes d’un contrôleur fixe, la valeur prédictive positive chute et la plupart des alertes deviennent fausses, portant le coût de détection à $1/\mathrm{VPP}$ examens par erreur réelle attrapée.
- La règle de Bayes fixe la valeur prédictive positive, non la prise en compte : l’appariement des probabilités pousse les opérateurs à négliger des alertes peu fiables, alors que résoudre un désaccord par un tiers est une décision d’utilité espérée qui paie lorsque les enjeux sont élevés (décision unique, perte très supérieure au coût de la contre-expertise).
- Le risque réel est le produit du taux d’erreur et de la probabilité d’échappement ; les évaluations comparatives, qui notent le producteur seul, ne mesurent que le premier facteur, alors qu’un producteur très exact dont les erreurs échappent peut former un système plus risqué qu’un producteur moins précis mais mieux contrôlé.
- Réduire durablement le risque exige d’agir sur les trois leviers du modèle : la précision du contrôleur (faible $f$, pour garder des alertes lisibles), son indépendance (faible $c$, pour abaisser le plancher d’échappement) et une prise en compte effective ($u$).
