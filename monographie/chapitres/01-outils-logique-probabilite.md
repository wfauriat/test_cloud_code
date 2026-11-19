# Boîte à outils : logique, conditionnement, probabilité {#sec:ch01}

Ce chapitre ne suppose rien des autres. On peut le lire d’une traite, à l’entrée de la @sec:partie-1, ou n’y revenir qu’au besoin en suivant l’un des parcours proposés à la @sec:ch00-parcours. Il rappelle les outils de logique et de probabilité dont se sert tout le livre : déduction et induction, règles à conditions sous-entendues, probabilité et conditionnement, règle de Bayes, score logarithmique. Chacun est introduit par la question à laquelle il répond. Un même fil les relie : aucun ne livre de conclusion sans condition, et l’on apprendra à repérer, derrière chaque résultat, le « pourvu que » qui le fait tenir.

## Déduction et induction {#sec:ch01-modes-inference}

Que garantit au juste un raisonnement, et à quelles conditions ? Pour tirer une conclusion de ce que l’on sait, on dispose de deux grands modes d’inférence. La **déduction** est une inférence nécessaire à partir de prémisses : si les prémisses sont vraies, la conclusion ne peut pas être fausse. L’**induction** est une généralisation à partir de régularités observées : de cas déjà vus, elle tire une règle, ou une prévision pour des cas qui ne l’ont pas encore été. L’une et l’autre sont des formes authentiques de rigueur, et pourtant aucune ne livre ses conclusions sans condition.

Une déduction se juge de deux façons qu’il importe de ne pas confondre. Elle est *valide* lorsqu’il est impossible que ses prémisses soient vraies et sa conclusion fausse ; c’est une propriété de sa seule forme. Elle est *solide* lorsqu’elle est valide et que ses prémisses sont, de surcroît, vraies. La logique se prononce sur la validité. Elle n’a rien à dire de la vérité des prémisses, qui se décide ailleurs, en regardant le monde.

Le raisonnement « tout métal conduit le courant électrique ; ce barreau est métallique ; donc ce barreau conduit le courant » est valide, et comme ses prémisses sont vraies, il est solide. Voici maintenant celui d’un bureau d’études : « toute poutre en acier homogène dont la contrainte calculée reste sous la limite d’élasticité supporte sa charge ; cette poutre est en acier homogène, et sa contrainte calculée reste sous cette limite ; donc elle supportera sa charge ». La forme est tout aussi irréprochable. Mais si la poutre réelle porte une fissure que personne n’a relevée, ou si son acier n’a pas la composition prévue, la seconde prémisse est fausse. L’argument reste valide, il cesse d’être solide, et sa conclusion n’est plus garantie. La déduction ne crée aucune vérité : elle transporte celle des prémisses jusqu’à la conclusion. Lorsque les définitions, les mesures et les idéalisations de départ décrivent fidèlement la situation, elle transporte une vérité ; lorsqu’elles s’en écartent, elle transporte l’erreur avec la même rigueur.

L’induction répond à une autre question : comment passer d’un nombre fini de cas observés à une règle générale, ou à une prévision sur un cas que l’on n’a pas encore vu ? Un laboratoire mesure trois fois la température d’ébullition de l’eau et lit trois fois 100 °C ; un service hospitalier constate l’efficacité d’un traitement sur cinq cents patients ; un ingénieur relève mille heures de fonctionnement sans panne sur un banc d’essai. De ces séries, l’induction tire une régularité. Mais le passage au cas suivant n’est jamais logiquement nécessaire. Rien, dans la logique, n’interdit que la mille et unième heure diffère des mille précédentes si une circonstance nouvelle intervient.

David Hume a mis le doigt, au XVIII^e^ siècle, sur la difficulté de fond [@hume1748] : qu’est-ce qui autorise à étendre au futur, ou à ce que l’on n’a pas observé, les régularités constatées jusqu’ici ? Répondre que « cette façon de généraliser a toujours réussi » revient à justifier l’induction par une induction, c’est-à-dire à tourner en rond. Nous retrouverons ce problème et ses formes contemporaines au @sec:ch07. Pour l’instant, retenons ce que les deux modes d’inférence ont en commun :

- la déduction garantit sa conclusion *pourvu que* ses prémisses et ses idéalisations soient exactes ;
- l’induction prolonge à bon droit les régularités observées *pourvu que* les cas nouveaux ressemblent aux cas observés sur les points qui gouvernent le phénomène.

Dans un cas comme dans l’autre, la rigueur du raisonnement ne garantit pas, à elle seule, que la clause « pourvu que » est remplie.

## Règles conditionnelles et conditions tues {#sec:ch01-regles-conditionnelles}

Comment écrire une règle utile lorsque la liste des conditions qui la font tenir ne peut pas être close ? En logique, une règle conditionnelle s’énonce « si $A$, alors $B$ », ce que l’on note $A \rightarrow B$, ou $A_1 \cap A_2 \rightarrow B$ lorsque plusieurs conditions doivent être réunies. Dans un domaine fermé, comme l’arithmétique, le jeu d’échecs ou un circuit logique idéal, on peut faire figurer dans $A$ toutes les conditions nécessaires sans rien laisser dans l’ombre.

Il en va autrement dès que la règle porte sur le monde matériel. Prenons un exemple que le @sec:ch02 développera en détail, l’ébullition de l’eau. Chacun connaît la règle courte « si l’on porte de l’eau à 100 °C, alors elle bout », et trois mesures en laboratoire suffisent à la confirmer. Il suffit pourtant que l’eau soit fortement salée, ou que le récipient soit clos et que la pression y monte, pour qu’elle reste calme à 100 °C ; en altitude, c’est la valeur même de 100 °C qui cesse de convenir, car l’eau y bout bien avant. On peut allonger la règle en précisant que l’eau est pure et la pression normale. Même ainsi complétée, elle tait encore d’autres conditions. Dans un récipient très lisse, l’eau peut dépasser 100 °C sans bouillir, faute d’aspérités où les bulles se forment : c’est le retard à l’ébullition. Le relevé suppose en outre un thermomètre juste, plongé dans un liquide de température homogène.

Pour rendre visible ce caractère ouvert des règles empiriques, techniques ou pratiques, nous les écrirons dans ce livre sous la forme :

$$A \cap (\dots) \rightarrow B$$ {#eq:ch01-regle}

$A$ rassemble les conditions énoncées, le symbole $\cap$ note la conjonction (« et ») et $B$ la conséquence attendue. La parenthèse $(\dots)$ désigne l’arrière-plan non énoncé, c’est-à-dire l’ensemble indéfini des circonstances ordinaires que l’on tient tacitement pour acquises en appliquant la règle.

Cette parenthèse ne trahit pas une négligence que des auteurs plus scrupuleux sauraient réparer. Une règle qui voudrait tout énoncer dans $A$ deviendrait interminable, donc inutilisable ; le @sec:ch02 examinera ce partage entre ce que l’on énonce et ce que l’on tait. Un besoin se fait sentir dès maintenant. Lorsqu’on ignore si toutes les circonstances cachées dans $(\dots)$ sont réunies, la logique, qui ne connaît que le vrai et le faux, ne dit plus à quoi s’attendre. Il faut un instrument qui pèse les issues possibles, et c’est le calcul des probabilités.

## Probabilité : règles et lectures {#sec:ch01-probabilite}

Comment attribuer des poids cohérents à des issues incertaines, et que veulent dire ces nombres ? Notons $\Pr(A)$ la probabilité d’un événement, ou d’une proposition, $A$. Quel que soit le sens qu’on lui donne, ce nombre obéit à quelques règles de cohérence. Une probabilité est comprise entre $0$ et $1$ ; l’événement certain, qui réunit toutes les issues envisagées, reçoit $1$, et l’événement impossible $0$. Lorsque deux événements s’excluent, la probabilité que l’un ou l’autre se produise est la somme de leurs probabilités. En particulier, un événement $A$ et sa négation $\bar{A}$ s’excluent et couvrent à eux deux toutes les issues, si bien que $\Pr(\bar{A}) = 1 - \Pr(A)$.

::: {.formel titre="Axiomes du calcul des probabilités"}
On considère un ensemble $\Omega$ qui regroupe toutes les issues élémentaires retenues pour décrire le problème, et une famille de parties de $\Omega$ appelées événements (elle contient $\Omega$ et elle est stable par passage au complémentaire et par réunion dénombrable). Une mesure de probabilité $\Pr(\cdot)$ associe à chaque événement un nombre réel et vérifie les trois axiomes de Kolmogorov :

1. **Positivité :** pour tout événement $A$, $\Pr(A) \ge 0$.
2. **Normalisation :** $\Pr(\Omega) = 1$.
3. **Additivité :** pour deux événements incompatibles ($A \cap B = \emptyset$), $\Pr(A \cup B) = \Pr(A) + \Pr(B)$ ; plus généralement, pour une suite dénombrable d’événements deux à deux incompatibles $A_1, A_2, \dots$, $\Pr\bigl(\bigcup_{i \ge 1} A_i\bigr) = \sum_{i \ge 1} \Pr(A_i)$.

Les propriétés usuelles en découlent aussitôt : $\Pr(\emptyset) = 0$, $0 \le \Pr(A) \le 1$, $\Pr(\bar{A}) = 1 - \Pr(A)$, et, pour deux événements quelconques, $\Pr(A \cup B) = \Pr(A) + \Pr(B) - \Pr(A \cap B)$.
:::

Ces axiomes fixent les règles du calcul, non le sens des nombres. Deux lectures principales leur en donnent un.

- *La lecture fréquentiste.* $\Pr(A)$ est la fréquence limite avec laquelle $A$ se produit lorsqu’on répète une même expérience un grand nombre de fois, dans des conditions jugées identiques. Cette lecture va de soi pour des tirages au sort, des pièces produites en série sur une ligne stable ou des lancers de dé. Elle devient muette, ou artificielle, devant un événement qui ne se produira qu’une fois : le succès d’une opération chirurgicale prévue demain, la tenue d’un barrage lors d’une crue exceptionnelle, le lancement d’une sonde interplanétaire.
- *La lecture comme jugement.* $\Pr(A)$ mesure le degré de croyance que l’on accorde à $A$, compte tenu de ce que l’on sait et des hypothèses que l’on retient [@definetti1974; @jaynes2003; @lindley2006]. Le nombre ne décrit plus une propriété de l’objet, mais un état de connaissance. Une soudure n’est pas « défectueuse à 4 % » : elle a un défaut ou elle n’en a pas, et les 4 % disent seulement ce que l’on en sait. Deux personnes qui disposent d’informations différentes, ou qui retiennent des hypothèses différentes, peuvent donc annoncer des probabilités différentes sans que l’une ou l’autre viole les axiomes.

Ce livre raisonne et décide avec la lecture comme jugement, sans renoncer aux fréquences. Le jugement d’abord, parce qu’il faut presque toujours évaluer un risque ou trancher *avant* que le monde ait répondu, et souvent dans des situations qui ne se répètent pas. Les fréquences ensuite, pour deux raisons. Lorsqu’on dispose de fréquences stables sur des cas comparables, elles nourrissent directement le jugement. Surtout, sur une série de prévisions, ce sont les fréquences observées après coup qui mettent les jugements à l’épreuve : vérifier que les événements annoncés à 70 % se produisent bien environ sept fois sur dix, c’est ce que le @sec:ch03 appellera la calibration.

::: {.nuance titre="Fréquence ou jugement : un débat que ce livre ne tranche pas"}
Le choix entre les deux lectures nourrit un débat ancien, que ce livre ne prétend pas clore. Il adopte la lecture comme jugement à titre de position de travail, parce qu’elle s’applique aussi aux décisions qui ne se répètent pas, et il en accepte le prix : deux jugements également cohérents peuvent diverger, et il faudra dire comment les départager (@sec:ch03). La lecture fréquentiste, de son côté, n’échappe pas tout à fait au jugement. Parler de répétitions « dans des conditions jugées identiques », c’est décider quels cas l’on tient pour semblables. La même opération chirurgicale n’affiche pas la même fréquence de succès selon qu’on la range parmi toutes les opérations de ce type, parmi celles du même chirurgien ou parmi celles des patients du même âge. Choisir la série de référence est déjà un jugement.
:::

## Probabilité conditionnelle et probabilité totale {#sec:ch01-probabilite-conditionnelle}

Comment réviser le poids d’un événement $B$ lorsqu’on suppose, ou qu’on apprend, qu’une condition $A$ est remplie ? Et comment recomposer la probabilité d’un événement à partir de plusieurs scénarios ? La probabilité conditionnelle de $B$ sachant $A$, définie lorsque $\Pr(A) > 0$, vaut :

$$\Pr(B \mid A) = \frac{\Pr(A \cap B)}{\Pr(A)}$$ {#eq:ch01-cond}

Cette formule se lit de façon très concrète, et cette lecture servira tout au long du livre. Représentons-nous $\Omega$ comme l’ensemble des situations, ou des mondes, compatibles avec ce que l’on envisage, chacun muni de son poids. Conditionner par $A$, c’est ne garder que les mondes où $A$ est vrai, puis mesurer, parmi eux, la part de ceux où $B$ l’est aussi. Diviser par $\Pr(A)$ ne fait que renormaliser : les mondes retenus forment un nouvel univers, de poids total $1$.

Cette lecture rejoint les règles à conditions tues de l’@eq:ch01-regle. Si une règle s’écrit $A \cap (\dots) \rightarrow B$, $\Pr(B \mid A)$ mesure, parmi les situations où les conditions énoncées $A$ sont remplies, la part de celles où l’arrière-plan tu $(\dots)$ laisse effectivement $B$ se produire. Le @sec:ch03 fera de cette image des mondes le fondement du jugement probabiliste.

De l’@eq:ch01-cond découle la règle du produit, $\Pr(A \cap B) = \Pr(A)\,\Pr(B \mid A)$. Elle donne aussi une définition précise de l’indépendance au sens du calcul des probabilités. Deux événements $A$ et $B$ sont indépendants lorsque savoir $A$ ne change pas la part des mondes où $B$ est vrai, soit $\Pr(B \mid A) = \Pr(B)$, ou de façon équivalente $\Pr(A \cap B) = \Pr(A)\,\Pr(B)$. Dans tous les autres cas, apprendre $A$ déplace la probabilité de $B$.

Il arrive souvent que l’on sache mieux décrire un événement à l’intérieur de chaque scénario que globalement. Supposons que l’on cherche la probabilité d’un retard de livraison $B$, et que deux situations météorologiques, exclusives l’une de l’autre, couvrent toutes les possibilités : brouillard dense ($H$) ou temps dégagé ($\bar{H}$). Si l’on connaît la probabilité du retard dans chaque situation, $\Pr(B \mid H)$ et $\Pr(B \mid \bar{H})$, ainsi que le poids de chacune, $\Pr(H)$ et $\Pr(\bar{H})$, la probabilité du retard est leur moyenne pondérée :

$$\Pr(B) = \Pr(B \mid H)\,\Pr(H) + \Pr(B \mid \bar{H})\,\Pr(\bar{H}).$$

Si le brouillard survient un matin sur quatre et provoque alors un retard dans 40 % des cas, tandis que par temps dégagé le retard ne survient que dans 4 % des cas, on obtient $\Pr(B) = 0{,}40 \times 0{,}25 + 0{,}04 \times 0{,}75 = 0{,}10 + 0{,}03 = 0{,}13$, soit 13 %. Plus généralement, si des hypothèses $H_1, \dots, H_k$ forment une *partition* de $\Omega$, c’est-à-dire qu’elles s’excluent deux à deux et que leur réunion est $\Omega$ tout entier, la *formule des probabilités totales* s’écrit :

$$\Pr(B) = \sum_{i=1}^{k} \Pr(B \mid H_i)\,\Pr(H_i)$$ {#eq:ch01-totale}

Le @sec:ch02 s’appuiera sur cette formule. Les probabilités conditionnelles $\Pr(B \mid H_i)$ y résument ce que l’on sait décrire à l’intérieur de chaque scénario, et les poids $\Pr(H_i)$ portent le jugement sur l’importance relative des scénarios retenus.

## Réviser un jugement : la règle de Bayes sous forme de cotes {#sec:ch01-bayes}

Lorsqu’on observe un fait nouveau $E$, de combien doit-il déplacer la confiance accordée à une hypothèse $H$ plutôt qu’à son contraire $\bar{H}$ ? Les modèles scientifiques et techniques raisonnent d’ordinaire dans le sens direct : si le système se trouve dans l’état $H$ (un défaut mécanique, une panne de capteur), quelle est la probabilité d’observer l’indice $E$ ? C’est $\Pr(E \mid H)$. Celui qui reçoit les données se pose la question inverse : l’indice $E$ vient d’être observé, quelle confiance accorder désormais à $H$ ? C’est $\Pr(H \mid E)$. Prendre l’une pour l’autre est une erreur de raisonnement classique. La règle de Bayes permet de passer correctement de la première à la seconde.

On peut écrire cette règle directement en probabilités, mais le dénominateur $\Pr(E)$ y masque le mécanisme de la révision. Elle devient bien plus parlante en *cotes*. La cote d’une hypothèse $H$ est le rapport de sa probabilité à celle de son contraire (on suppose $\Pr(H) < 1$) :

$$\text{cote}(H) = \frac{\Pr(H)}{\Pr(\bar{H})} = \frac{\Pr(H)}{1 - \Pr(H)}, \qquad \text{et inversement} \quad \Pr(H) = \frac{\text{cote}(H)}{1 + \text{cote}(H)}.$$

Une probabilité de 20 % correspond ainsi à une cote de $0{,}20 / 0{,}80 = 0{,}25$, soit une chance contre quatre, et une probabilité de 50 % à une cote de $1$.

Reste à mesurer ce que l’observation $E$ apporte pour départager les deux hypothèses. On appelle **rapport de vraisemblance** de $E$, pour $H$ contre $\bar{H}$, le rapport des probabilités de cette observation sous chacune des deux hypothèses :

$$\Lambda(E) = \frac{\Pr(E \mid H)}{\Pr(E \mid \bar{H})}.$$

Il indique combien de fois $E$ est plus probable si $H$ est vraie que si $\bar{H}$ l’est. Un rapport supérieur à $1$ plaide pour $H$, un rapport inférieur à $1$ pour $\bar{H}$. Un rapport égal à $1$ signifie que $E$ est aussi probable sous l’une que sous l’autre : l’observation ne permet pas de les départager.

La règle de Bayes prend alors une forme multiplicative :

$$\text{cote}(H \mid E) = \text{cote}(H) \times \frac{\Pr(E \mid H)}{\Pr(E \mid \bar{H})}$$ {#eq:ch01-bayes-cotes}

Autrement dit, la cote *a posteriori* est la cote *a priori* multipliée par le rapport de vraisemblance. Deux conséquences en découlent. D’abord, une observation ne fixe jamais seule la probabilité finale ; elle multiplie la cote dont on partait, si bien que deux personnes parties de cotes différentes aboutissent, après la même observation, à des conclusions différentes. Ensuite, si plusieurs observations $E_1, E_2, \dots$ sont indépendantes sous chacune des deux hypothèses, il suffit de multiplier la cote par $\Lambda(E_1)$, puis par $\Lambda(E_2)$, et ainsi de suite.

::: {.formel titre="Dérivation de la règle de Bayes sous forme de cotes"}
Soient deux hypothèses incompatibles $H_1$ et $H_2$, et une observation $E$ telle que $\Pr(E) > 0$, $\Pr(H_2) > 0$ et $\Pr(E \mid H_2) > 0$. En appliquant l’@eq:ch01-cond, puis la règle du produit, à $H_1$ et à $H_2$ sachant $E$, on obtient :

$$\Pr(H_1 \mid E) = \frac{\Pr(H_1 \cap E)}{\Pr(E)} = \frac{\Pr(E \mid H_1)\,\Pr(H_1)}{\Pr(E)},$$

$$\Pr(H_2 \mid E) = \frac{\Pr(H_2 \cap E)}{\Pr(E)} = \frac{\Pr(E \mid H_2)\,\Pr(H_2)}{\Pr(E)}.$$

En divisant la première égalité par la seconde, le facteur commun $\Pr(E)$ disparaît :

$$\frac{\Pr(H_1 \mid E)}{\Pr(H_2 \mid E)} = \frac{\Pr(H_1)}{\Pr(H_2)} \times \frac{\Pr(E \mid H_1)}{\Pr(E \mid H_2)}.$$

Avec $H_1 = H$ et $H_2 = \bar{H}$, on retrouve l’@eq:ch01-bayes-cotes. Pour obtenir directement la probabilité *a posteriori* $\Pr(H \mid E)$, on calcule le dénominateur $\Pr(E) = \Pr(E \mid H)\,\Pr(H) + \Pr(E \mid \bar{H})\,\Pr(\bar{H})$ par la formule des probabilités totales (@eq:ch01-totale), d’où :

$$\Pr(H \mid E) = \frac{\Pr(E \mid H)\,\Pr(H)}{\Pr(E \mid H)\,\Pr(H) + \Pr(E \mid \bar{H})\,\Pr(\bar{H})}.$$

Enfin, pour deux observations $E_1$ et $E_2$ *conditionnellement indépendantes* sous chacune des hypothèses, c’est-à-dire telles que $\Pr(E_1 \cap E_2 \mid H) = \Pr(E_1 \mid H)\,\Pr(E_2 \mid H)$ et de même sous $\bar{H}$, le rapport de vraisemblance conjoint se factorise : $\Lambda(E_1 \cap E_2) = \Lambda(E_1)\,\Lambda(E_2)$.
:::

Voyons comment, sur un exemple chiffré, le jugement de départ et la force de l’observation se combinent.

::: {.exemple-quantitatif titre="Réviser la probabilité d’un défaut après un examen par ultrasons"}
**Mise en place.** On examine par ultrasons les soudures d’une canalisation, en se demandant si chacune présente un défaut interne (hypothèse $D$) ou si elle est saine ($\bar{D}$). Les chiffres sont purement illustratifs. Sur des pièces d’étalonnage, la sonde se comporte ainsi : en présence d’un défaut, elle émet un signal anormal ($T^+$) dans 75 % des cas, et son signal reste normal ($T^-$) dans 25 % des cas ; sur une soudure saine, une irrégularité de forme sans gravité déclenche tout de même un signal anormal dans 15 % des cas, et le signal reste normal dans 85 % des cas. Le rapport de vraisemblance d’un signal anormal vaut donc $\Lambda(T^+) = 0{,}75 / 0{,}15 = 5$, et celui d’un signal normal $\Lambda(T^-) = 0{,}25 / 0{,}85 = 5/17 \approx 0{,}294$. On part de deux jugements *a priori* : la probabilité de défaut est estimée à 4 % pour une soudure d’un lot courant, et à 20 % pour une soudure d’une zone qui a subi des contraintes inhabituelles.

![Probabilité qu’une soudure soit défectueuse, avant et après l’examen par ultrasons, dans quatre situations : soudure d’un lot courant suivie d’un signal anormal ; soudure d’une zone suspecte suivie d’un signal anormal, d’un signal normal, ou de deux signaux anormaux indépendants. Le même signal anormal multiplie la cote par 5 dans les deux cas, mais seule la soudure de la zone suspecte franchit la barre d’une chance sur deux.](figures/ch01-bayes-cotes.pdf){#fig:ch01-bayes-cotes width=88%}

**Calcul.** Le tableau ci-dessous donne, pour chaque situation, la cote *a priori*, le rapport de vraisemblance, la cote *a posteriori* et la probabilité *a posteriori*.

::: {.inclure fichier="tableaux/ch01-bayes-cotes.md"}
:::

Deux lignes de calcul suffisent à suivre le mécanisme. Pour la soudure du lot courant, la cote *a priori* vaut $0{,}04 / 0{,}96 = 1/24$ ; un signal anormal la porte à $5/24$, ce qui correspond à une probabilité de $5/29$, soit environ 17,2 %. Pour la zone suspecte, la cote de départ vaut $0{,}25$ : un signal anormal la porte à $1{,}25$ (probabilité $5/9$, environ 55,6 %), un signal normal la ramène à $0{,}25 \times 5/17 = 5/68$ (probabilité $5/73$, environ 6,85 %), et deux signaux anormaux indépendants la multiplient par $5 \times 5 = 25$, jusqu’à $6{,}25$ (probabilité $25/29$, environ 86,2 %).

**Lecture.** L’exemple montre trois choses. D’abord, un même signal ne conduit pas à la même conclusion selon le point de départ : multiplier la cote par 5 laisse la soudure du lot courant probablement saine (17,2 %), mais fait passer celle de la zone suspecte au-delà d’une chance sur deux (55,6 %). Ensuite, les deux signaux ne pèsent pas symétriquement. Un signal anormal multiplie la cote par 5 ; un signal normal la multiplie par 0,294, ce qui revient à la diviser par moins de 5. Il rassure donc moins que le signal anormal n’inquiète, parce que la sonde manque un défaut plus souvent qu’elle ne signale à tort une soudure saine. Le poids d’un résultat se calcule toujours à partir de ses propres probabilités sous les deux hypothèses. Enfin, la ligne des deux signaux repose entièrement sur leur indépendance sous chaque hypothèse. Si la seconde sonde réagit à la même irrégularité de forme que la première, son signal n’apporte presque rien de neuf, et multiplier une seconde fois par 5 compterait deux fois la même information.

L’exemple ne dit pas, en revanche, d’où viennent les chiffres de la sonde. Ils ont été mesurés sur des pièces d’étalonnage et ne valent pour les soudures réelles que pourvu que celles-ci leur ressemblent ; les probabilités *a priori*, elles, sont des jugements. La révision la plus rigoureuse hérite des « pourvu que » des nombres qu’elle combine.
:::

## Mesurer la qualité d’une prévision : la surprise {#sec:ch01-score-logarithmique}

Comment juger après coup une prévision probabiliste, lorsque le monde a tranché en faveur d’une seule issue ? Si un météorologue annonce « il pleuvra demain » et qu’il fait grand soleil, son énoncé est faux, tout simplement. S’il annonce « 20 % de risque de gel cette nuit », une nuit de gel ne prouve pas qu’il s’est trompé, pas plus qu’une nuit douce ne prouve qu’il avait raison. Pour confronter des prévisions probabilistes à l’issue observée, il faut une mesure graduée, qui dise à quel point cette issue a pris chaque prévision au dépourvu.

C’est ce que mesure le **score logarithmique**. La surprise d’une issue, sous une prévision qui lui attribuait la probabilité $p = \Pr(\text{issue})$, vaut :

$$S(p) = -\ln p$$ {#eq:ch01-score-log}

Plus la probabilité accordée à l’issue survenue était faible, plus la surprise est grande. Une issue annoncée comme certaine ($p = 1$) ne surprend pas du tout. Une issue jugée très improbable qui se produit malgré tout coûte cher, et une issue à laquelle on avait accordé une probabilité nulle coûte une surprise infinie. D’où une règle de prudence élémentaire : ne donner une probabilité nulle qu’à ce qui est réellement impossible. Sur une série de prévisions indépendantes, enfin, les surprises s’additionnent, ce qui permet de noter un prévisionniste sur la durée plutôt que sur un seul cas.

Deux prévisionnistes évaluent le risque de gel sur un verger : le premier l’estime à 20 %, le second à 2 %. Si le gel survient, la surprise du premier vaut $-\ln 0{,}20 \approx 1{,}61$, celle du second $-\ln 0{,}02 \approx 3{,}91$. L’écart entre les deux vaut $\ln(0{,}20 / 0{,}02) = \ln 10 \approx 2{,}30$ : il correspond à un rapport de vraisemblance de 10 en faveur du premier. Si la nuit reste douce, le premier avait accordé 80 % à cette issue (surprise $-\ln 0{,}80 \approx 0{,}223$) et le second 98 % (surprise $-\ln 0{,}98 \approx 0{,}020$). L’écart est faible, et le rapport de vraisemblance, $0{,}80 / 0{,}98 \approx 0{,}816$, ne les départage guère.

On voit ainsi le lien entre les deux outils : la différence des surprises de deux prévisions est le logarithme de leur rapport de vraisemblance sur l’issue observée, et le rapport de vraisemblance est l’exponentielle de cette différence. Le @sec:ch03 se servira de ce couple pour comparer les estimations de deux navigateurs avant une même course, et pour examiner ce qu’une issue unique permet, ou non, de conclure à leur sujet.

::: {.formel titre="Score logarithmique et rapport de vraisemblance"}
Pour toute issue ayant reçu une probabilité $p \in \left]0, 1\right]$, le score logarithmique $S(p) = -\ln p$ est positif ou nul ($S(1) = 0$) et strictement décroissant en $p$.

1. **Additivité sur des épreuves indépendantes.** Si deux issues successives $E_1$ et $E_2$ sont jugées indépendantes et reçoivent les probabilités $p_1$ et $p_2$, leur probabilité conjointe vaut $p_1 p_2$, et la surprise totale est la somme des surprises :
   $$S(p_1 p_2) = -\ln(p_1 p_2) = -\ln p_1 - \ln p_2 = S(p_1) + S(p_2).$$

2. **Lien avec le rapport de vraisemblance.** Soient deux prévisions qui attribuent à l’issue observée les probabilités strictement positives $p_1 = \Pr_1(\text{issue})$ et $p_2 = \Pr_2(\text{issue})$. La différence de leurs surprises vaut :
   $$S(p_2) - S(p_1) = -\ln p_2 - (-\ln p_1) = \ln\left(\frac{p_1}{p_2}\right) = \ln \Lambda,$$ {#eq:ch01-surprise-vraisemblance}
   où $\Lambda = p_1 / p_2$ est le rapport de vraisemblance de l’issue observée sous la première prévision contre la seconde ; réciproquement, $\Lambda = \exp\bigl(S(p_2) - S(p_1)\bigr)$.

3. **Effet d’une probabilité nulle.** Poser $p = 0$ pour une issue qui se produit donne $S(0) = +\infty$. Du côté de la règle de Bayes (@eq:ch01-bayes-cotes), une probabilité *a priori* nulle donne une cote nulle, qu’aucun rapport de vraisemblance fini ne peut relever : aucune observation ne rendra plus cette éventualité plausible. Les axiomes n’interdisent pas d’attribuer une probabilité nulle ; la prudence commande de la réserver à ce qui est logiquement impossible.
:::

## Points clés {.points-cles}

- La déduction transporte la vérité de ses prémisses et l’induction généralise des régularités observées ; l’une et l’autre ne livrent leurs conclusions que « pourvu que » leurs conditions soient remplies, et la rigueur du raisonnement ne garantit pas, à elle seule, qu’elles le sont.
- Toute règle portant sur le monde cache un arrière-plan ouvert de conditions sous-entendues, que l’on note $A \cap (\dots) \rightarrow B$.
- Une probabilité peut se lire comme une fréquence ou comme un jugement ; ce livre raisonne avec le jugement et le met à l’épreuve des fréquences.
- La probabilité conditionnelle $\Pr(B \mid A)$ est une part de mondes : parmi ceux où $A$ est vrai, la part de ceux où $B$ l’est aussi.
- Réviser un jugement, c’est multiplier sa cote par le rapport de vraisemblance de l’observation, si bien qu’une observation déplace un jugement sans jamais le fixer à elle seule.
- La surprise $-\ln \Pr(\text{issue})$ mesure à quel point une issue prend une prévision au dépourvu ; l’écart des surprises de deux prévisions est le logarithme de leur rapport de vraisemblance.
