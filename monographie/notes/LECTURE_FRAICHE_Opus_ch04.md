# Lecture fraîche : chapitre 4, « Décider d’après ce que l’on croit »

Lecteur : Opus, première lecture, sans autre fichier que `chapitres/04-decider.md`.

## 1. Ce que j’ai compris (test de lisibilité)

1. La règle de Savage (utilité espérée subjective) prescrit de choisir l’acte dont l’utilité espérée, calculée avec ses propres probabilités, est maximale ; on décide avant que le monde ait répondu, donc d’après ce que l’on croit.
2. Entre une option sûre et une option risquée, cette règle donne un seuil p* = 1/(1 + L/ΔU) : on prend le risque si la probabilité d’échec estimée p est inférieure à p*. Le seuil ne dépend que du rapport des enjeux.
3. M. X (5 %) et M. Y (0,1 %), avec le même rapport des enjeux (25, seuil 3,85 %), prennent rationnellement des décisions opposées : leur désaccord vient de leurs représentations.
4. Quand la perte devient démesurée (roulette russe, rapport 10 000), le seuil s’effondre vers zéro. La moyenne sur des décisions répétées protège et permet de recalibrer, ce que ne fait pas une décision unique.
5. Si p vient d’un cadre qui a omis un élément décisif, le calcul ne le signale pas ; comment décider dans ce cas est la question renvoyée au chapitre 17.

## 2. Constats classés par gravité

### Gravité A (compréhension compromise ou contresens possible)

Aucun.

### Gravité B (gêne réelle)

**B1. Section « La course à la voile », « ce qui en donne une lecture par les cotes (@sec:ch01-bayes) : l’option risquée l’emporte lorsque la cote du succès contre l’échec dépasse le rapport des enjeux ».**
En français courant, la « cote » d’un pari désigne le multiplicateur de gain du bookmaker et non le rapport de chances (1 − p)/p. Un lecteur qui n’a pas en tête la définition du chapitre 1 risque de comprendre l’inverse (faux ami possible de l’anglais *odds*). C’est une possible dépendance.
Reformulation minimale : « … lorsque la cote du succès contre l’échec, c’est-à-dire le rapport (1 − p)/p de leurs probabilités, dépasse le rapport des enjeux ». Le sens ne change pas.

**B2. Section « La course à la voile », « le seuil passe au-dessous de 50 %, et il baisse d’autant plus que l’écart entre les deux est grand ».**
« Écart » fait penser à une différence. Or la phrase suivante dit que seul compte le *rapport* L/ΔU, ce qui crée une petite contradiction interne.
Reformulation : « … d’autant plus que la perte dépasse largement le gain » ou « … que le rapport entre les deux est grand ». Le sens ne change pas.

**B3. Sections « La course à la voile » et « La question laissée ouverte », « pèsent différemment l’arrière-plan $(\dots)$ », « laissé tout le reste dans l’arrière-plan $(\dots)$ », « avec tout ce que le cadre avait laissé dans $(\dots)$ ».**
Le chapitre ne définit pas la notation « (…) ». Dans la dernière occurrence, elle sert même de nom à elle seule (« laissé dans (…) »), ce qui est opaque pour qui n’a pas lu le chapitre 2. C’est une possible dépendance.
Reformulation pour la dernière occurrence : « … avec tout ce que le cadre avait laissé dans l’arrière-plan $(\dots)$ ». Un rappel en incise à la première occurrence aiderait aussi, par exemple « l’arrière-plan $(\dots)$, tout ce que la représentation n’explicite pas ». Je ne connais pas la définition exacte : à vérifier.

**B4. Section « La roulette russe… », « À un tel rapport des enjeux, la règle de l’UES n’autorise à presser la détente que dans deux cas. Ou bien le gain en jeu est immense, […] et le rapport des enjeux cesse d’être démesuré. »**
La phrase pose un rapport des enjeux fixé (10 000), puis donne comme premier cas une situation où ce rapport change. La logique se contredit en surface.
Reformulation : « Face à une mort possible, la règle de l’UES n’autorise à presser la détente que dans deux cas. » On peut aussi écrire « Avec une chance sur six, … ». Les deux lectures sont plausibles (contrainte posée par l’enjeu, ou contrainte posée par la probabilité) ; je ne tranche pas.

**B5. Même section, « Ou bien le joueur est à peu près certain que la chambre placée face au percuteur est vide, au point d’estimer la probabilité d’échec […] à 0,001 % ».**
La phrase précédente vient de fixer la probabilité à une chance sur six. Le lecteur se demande sur quoi peut reposer une telle certitude, et la réponse n’arrive que deux sections plus loin (le « cadre » du joueur).
Reformulation minimale : « Ou bien le joueur est, à tort ou à raison, à peu près certain que… ». Le sens ne bouge pas, mais l’incise oriente vers la suite. Si l’auteur veut un cas *légitime* (le joueur a vérifié le barillet), l’incise « à tort ou à raison » change la nuance ; à arbitrer.

**B6. Section « Décider une seule fois ou à répétition », début : « Un lecteur familier des usages statistiques de la théorie de la décision pourrait trouver ici une consolation. »**
On ne voit pas ce qui appelle une consolation. L’encadré précédent se termine sur une réserve technique (l’estimation ne couvre peut-être pas toutes les façons de casser), mais la phrase ne nomme pas l’inquiétude qu’elle prétend apaiser. Le fil se perd.
Reformulation : « Face au risque que l’estimation soit fausse, un lecteur familier des usages statistiques […] pourrait trouver une consolation. » Le sens risque de bouger si la « consolation » visait autre chose, par exemple le désaccord entre X et Y.

**B7. Même section, « une décision prise une seule fois, sans série d’essais comparables, et dont la réponse du monde n’arrive qu’après l’acte ».**
Le troisième critère ne distingue rien : la première section a posé que *toute* décision se prend avant que le monde ait répondu. Le lecteur cherche ce qui est propre à la décision unique.
Reformulation possible : « … et dont la réponse du monde n’arrive qu’après l’acte, trop tard pour être corrigée. » Une autre lecture est possible (critère redondant, gardé pour rappel). Je ne tranche pas.

**B8. Même section, « M. Y ne saura pas s’il le doit à un gréement sans défaut ou à la chance, dans un monde où M. X avait vu juste ».**
Le complément final est elliptique et mal rattaché : on comprend après coup qu’il signifie « ou à la chance, si le vrai risque était de 5 % comme le pensait M. X ».
Reformulation : « … ou à la chance, au cas où M. X aurait vu juste. » Le sens ne change pas.

**B9. Encadré « Le monde ne consulte pas nos probabilités », « un risque ignoré de moins de quatre points de pourcentage suffirait, s’il était connu, à changer sa décision ; pour le joueur […], moins d’un centième de point suffirait ».**
Lu littéralement, « un risque de moins de quatre points suffirait » laisse croire que *n’importe quel* risque inférieur à quatre points renverse la décision, alors qu’il faut un risque d’environ 3,75 points au moins. L’écart réel est 3,85 − 0,1 pour M. Y et 0,0100 − 0,001 ≈ 0,009 pour le joueur.
Reformulation : « un risque ignoré d’à peine quatre points de pourcentage (3,75) suffirait […] ; pour le joueur […], un peu moins d’un centième de point suffirait ». Le sens ne change pas : seule la formulation de la borne est en cause.

### Gravité C (confort, style)

**C1. Section « L’utilité espérée subjective », « La théorie classique de la décision combine ces deux éléments […]. Une décision s’y décrit par quatre éléments ».**
On passe de « deux éléments » à « quatre éléments » à une ligne d’intervalle, et le référent de « s’y » est flou (la théorie, ou la règle ?).
Reformulation : « Dans cette théorie, une décision se décrit par quatre composantes ».

**C2. Même section et encadré, « subjective », « ses propres probabilités », « probabilité personnelle ».**
Trois expressions désignent la même notion. C’est compréhensible, mais le lecteur peut se demander si « personnelle » ajoute une nuance.
Si c’est voulu, une incise suffit : « une probabilité personnelle (subjective, au sens précisé plus haut) ».

**C3. Encadré « actes, états et conséquences », « seuls comptent les rapports entre écarts d’utilité ».**
L’expression est dense pour un non-spécialiste. Elle s’éclaire plus tard par L/ΔU, mais pas à cet endroit.
Reformulation : « seuls comptent les rapports entre différences d’utilité (par exemple entre ce que l’on perd et ce que l’on gagne) ».

**C4. Section « La course à la voile », notation « ΔU » pour le gain et « L » pour la perte.**
L’asymétrie de la notation (un Δ d’un côté, une lettre seule de l’autre) n’est pas motivée en français : L est vraisemblablement l’initiale de *loss*.
Gloss possible : « la perte en cas d’échec, notée $L$ (de l’anglais *loss*), … ». Cela ne touche pas les mathématiques.

**C5. Même section, « un voilier léger, rapide mais sollicité près de ses limites ».**
La tournure est un peu technique ou calquée.
Reformulation : « rapide mais exploité à la limite de sa résistance ».

**C6. Encadré « Dérivation du seuil », hypothèse 4, « ce que le monde réserve ».**
Le verbe « réserver » manque de complément.
Reformulation : « ce que le monde lui réserve ».

**C7. Section « La course à la voile », « L’@eq:ch04-seuil leur dicte pourtant des décisions opposées ».**
Le « pourtant » surprend, car des estimations différentes *conduisent* naturellement à des décisions différentes. Deux lectures sont possibles : contraste avec « rien ne permet de dire lequel a raison », ou contraste avec « devant les mêmes faits ». Je ne tranche pas.
Si la seconde lecture est la bonne : « Bien qu’ils partent des mêmes faits, l’équation leur dicte… ».

**C8. Même section, « (la règle de Bayes, sous la forme de l’@eq:ch01-bayes-cotes, dit de combien elle doit la déplacer) ».**
L’enchaînement « elle… la » (l’information, l’estimation) oblige à relire.
Reformulation : « … dit de combien cette information doit déplacer l’estimation ».

**C9. Section « La roulette russe » et encadré, « soit environ 0,0100 % ».**
Les zéros finaux surprennent dans un texte courant, et « environ » cohabite mal avec une précision affichée de quatre décimales.
Reformulation : « soit environ 0,01 % ». Dans l’encadré, garder 0,0100 % si c’est pour l’alignement avec le tableau.

**C10. Légende de la @fig:ch04-seuil, « Le décideur part lorsque son estimation $p$ se trouve au-dessous de la courbe ».**
« Part » ne convient pas au joueur de roulette, qui figure aussi sur la courbe.
Reformulation : « Le décideur choisit l’option risquée lorsque… ».

**C11. Section « La question laissée ouverte », « construite dans un cadre fini (@def:cadre) ».**
« Fini » peut se lire « achevé » au lieu de « limité ». C’est une possible dépendance.
Reformulation : « un cadre fini, c’est-à-dire limité (@def:cadre) ». Le sens est à vérifier selon la définition du chapitre 2.

**C12. Encadré « Le monde ne consulte pas nos probabilités », « le décideur n’a, par définition, aucun moyen de le lire pour le comparer au seuil ».**
« Lire » est inattendu à cet endroit.
Reformulation : « aucun moyen de le connaître pour le comparer au seuil ».

**C13. Encadré « question », « Pour votre prochain déploiement irréversible ».**
L’exemple informatique (mise en production) n’apparaît qu’une fois, dans la liste de la première section, puis disparaît ; « déploiement » arrive sans préparation.
Reformulation minimale : « Pour votre prochaine mise en production irréversible », ce qui reprend le terme du début du chapitre.

## 3. Appréciation globale

Le chapitre est clair et bien construit. Le fil va de la règle au seuil, puis au désaccord entre X et Y, à l’effondrement du seuil, à la décision unique et enfin à la question ouverte, et chaque transition est annoncée. Les calculs en texte sont justes et faciles à suivre ; le résumé ci-dessus a pu se faire sans relecture.

- **Sections les plus accessibles :** « La course à la voile », en particulier l’application à M. X et M. Y et la bascule par l’un ou l’autre terme, ainsi que « La question laissée ouverte ».
- **Sections les moins accessibles :**
  - « La roulette russe », à cause de la logique des « deux cas » (B4) et de la certitude du joueur non motivée à cet endroit (B5).
  - Le début de « Décider une seule fois ou à répétition », avec la consolation sans objet (B6) et un critère de définition qui ne distingue rien (B7).
  - L’encadré « Le monde ne consulte pas nos probabilités », à cause de la formulation des bornes en points de pourcentage (B9).
- **Dépendances :** la notation « (…) » pour l’arrière-plan est la principale dépendance non rappelée ; « cote » et « cadre fini » le sont dans une moindre mesure.
