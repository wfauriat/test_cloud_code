# Lecture fraîche — chapitre 2 « Le cadre : ce qui compte et ce qu’on tait »

Lecteur : Opus (première lecture, seul le fichier `chapitres/02-cadre.md` a été lu).

## 1. Ce que j’ai compris (test de lisibilité)

On n’agit jamais sur le monde lui-même, mais d’après une représentation construite ; or le monde répond à l’action, pas à la représentation (navigateur à 5 %, téléphone satellite, carte et territoire).
Toute règle utilisable laisse un arrière-plan de conditions tues, $A \cap (\dots) \rightarrow B$ : l’exemple de l’eau bouillante montre que chaque surprise fait passer une condition dans $A$ sans jamais vider la parenthèse, et que cette ouverture est aussi ce qui rend la règle maniable.
Un cadre est le choix fini (variables, catégories, classe de modèles, objectif) qui précède l’inférence ; en probabilités, tout ce qui n’est pas dans $X$ n’a pas de nom dans le calcul. Énoncer plus rend fragile, énoncer moins laisse des exceptions muettes.
Ni la déduction (calcul causal sur graphe) ni l’induction (prédiction conforme) ne certifient leur propre cadre ; formaliser un étage plus haut ne fait que reporter le choix (cas du modèle clinique).
Le « problème du cadre » de l’IA (McCarthy et Hayes, robot de Dennett) n’est qu’un cas particulier de cette limite générale.

## 2. Constats

### Gravité A

**A1 — § « Le cadre comme spécification finie » (avec la définition de *représentation* au § 1 et les Points clés)**
Passage : « La représentation est ce que l’on construit à l’intérieur de ce cadre (valeurs mesurées, paramètres estimés, probabilités attribuées) », à rapprocher de la définition : « Une **représentation** est la construction (mesures, catégories, équations, probabilités) » et de « redéfinir une catégorie […] c’est changer de cadre ».
Gêne : les *catégories* (et les *équations*, qui relèvent de la « classe de modèles ») figurent dans la définition de la représentation, puis sont attribuées au cadre ; le lecteur ne sait plus si cadre et représentation sont emboîtés (le cadre est une partie de la représentation) ou disjoints (la représentation est ce qu’on met dans le cadre).
Reformulation minimale : « La représentation est la construction complète : le cadre, plus ce que l’on construit à l’intérieur de lui (valeurs mesurées, paramètres estimés, probabilités attribuées) ». Attention : cela tranche pour la lecture « emboîtée » ; si l’auteur vise la lecture « disjointe », c’est plutôt la parenthèse de la définition (et du premier point clé) qu’il faut retoucher. Deux lectures plausibles, je ne tranche pas.

### Gravité B

**B1 — § « Le monde répond à l’action »**
Passage : « il estime à 5 % le risque de démâter s’il part sur un voilier léger plutôt que sur un voilier renforcé ».
Gêne : deux lectures : (a) le risque de démâter *avec le voilier léger* est de 5 % ; (b) choisir le léger *ajoute* 5 % de risque par rapport au renforcé.
Reformulation (lecture a) : « il estime à 5 % le risque de démâter s’il choisit le voilier léger plutôt que le voilier renforcé ». Pour la lecture (b) : « il estime que partir sur le voilier léger augmente de 5 points le risque de démâter ». Le sens change selon la lecture retenue.

**B2 — titre du § 3 et définition du cadre**
Passage : « Un **cadre** est la spécification finie à l’intérieur de laquelle opère un raisonnement ».
Gêne : pour un lecteur non mathématicien, « finie » se lit d’abord « achevée, terminée », ce qui est presque le contraire de l’idée (une liste bornée, donc incomplète).
Reformulation : « la spécification, en nombre fini d’éléments, à l’intérieur de laquelle… » (ou « la liste finie… »). Sens inchangé.

**B3 — § 3, lecture de l’équation**
Passage : « L’@eq:ch02-cond-cadre se lit à deux niveaux [...]. Les lois conditionnelles [...]. Les poids [...]. Mais l’essentiel est décidé avant même d’écrire la somme ».
Gêne : on ne sait pas quels sont les « deux niveaux » : (a) lois conditionnelles / poids (ce sont alors deux *composantes*, pas des niveaux, et le choix de la liste fait un troisième temps) ; (b) contenu de la somme / choix préalable de la liste.
Reformulation pour (a) : « se compose de deux éléments » ; pour (b) : garder « deux niveaux » mais annoncer : « au niveau de la somme, puis en amont de celle-ci ». Je ne tranche pas.

**B4 — § 3, encadré « Énoncer plus ou taire plus »**
Passage : « les facteurs écartés (salinité, pression, habitudes de codage d’un dossier) ».
Gêne : les « habitudes de codage d’un dossier » renvoient au cas clinique, qui n’apparaît qu’au § 4 ; ici l’exemple est opaque.
Reformulation : remplacer par un facteur déjà rencontré, p. ex. « (salinité, pression, saturation des sols) », ou ajouter « (on en verra un exemple clinique plus loin) ». Sens inchangé.

**B5 — § 3, articulation cadre/représentation**
Passage : « Deux analystes qui partagent le même cadre peuvent aboutir à des représentations différentes s’ils pèsent différemment les hypothèses disponibles. »
Gêne : « les hypothèses disponibles » est flou : hypothèses de modélisation, configurations possibles, données ?
Reformulation : « s’ils estiment différemment les paramètres ou attribuent des probabilités différentes aux mêmes configurations ». À valider : cela fixe une interprétation.

**B6 — § 3, encadré formel « Conditionnement sur les variables du cadre »**
Passage : « Les lois $\Pr(Y \mid X = x)$ moyennent tacitement son effet sur les valeurs qu’il prenait là où elles ont été établies ».
Gêne : trois pronoms (« son », « il », « elles ») à référents différents dans une seule proposition ; « là où » est vague (lieu ? conditions ?).
Reformulation : « Les lois $\Pr(Y \mid X = x)$ moyennent tacitement l’effet de ce facteur sur les valeurs que celui-ci prenait dans les conditions où ces lois ont été établies ». Sens inchangé.

**B7 — § « La rigueur formelle ne lève pas cette limite » (possible dépendance)**
Passages : « Considérons à nouveau la poutre de la @sec:ch01-modes-inference », « c’est la prémisse générale qui devient fausse », « le raisonnement reste valide, mais il cesse d’être solide ».
Gêne : le lecteur qui n’a pas le syllogisme du ch. 1 en tête ignore quelle est « la prémisse générale » ; la distinction *valide*/*solide* (calque de *valid*/*sound*) n’est pas rappelée.
Reformulation : rappeler en une incise la prémisse (« la prémisse générale, selon laquelle [...] ») et gloser : « valide (la conclusion suit des prémisses), mais plus solide (ses prémisses ne sont plus toutes vraies) ». Sens inchangé si conforme au ch. 1.

**B8 — § 4, induction (possible dépendance)**
Passage : « choisir les grandeurs mesurées, les variables sur lesquelles on conditionne et la série de référence qui définissent cette ressemblance ».
Gêne : « conditionner sur » et « série de référence » sont du jargon non rappelé ici.
Reformulation : « les variables dont on tient compte pour comparer les cas et l’ensemble de cas jugés comparables (la série de référence) ». Sens inchangé si conforme au ch. 1.

**B9 — § 4, prédiction conforme**
Passage : « elle garantit que l’ensemble prédit contiendra la vraie valeur avec au moins la fréquence choisie ».
Gêne : rien n’a dit que la méthode prédit un *ensemble* de valeurs plutôt qu’une valeur ; « l’ensemble prédit » tombe du ciel.
Reformulation : « elle fournit, au lieu d’une valeur unique, un ensemble de valeurs plausibles, et garantit que cet ensemble contiendra la vraie valeur… ». Sens inchangé.

**B10 — § 4, encadré formel, item 2**
Passage : « Ils servent à ajuster un modèle, puis à étalonner un score de non-conformité (c’est le jeu d’étalonnage). »
Gêne : « c’est » peut désigner les $n$ cas entiers ou seulement ceux qui servent à l’étalonnage ; le score de non-conformité n’est pas défini.
Reformulation : « Ces $n$ cas, qui forment le jeu d’étalonnage, servent à… » ou « Une partie d’entre eux sert à ajuster un modèle, l’autre (le jeu d’étalonnage) à étalonner… ». Les deux reformulations n’ont pas le même sens ; je ne tranche pas.

**B11 — § « Un mot sur le problème du cadre »**
Passage : « sa batterie de rechange, posée sur un chariot à côté d’une bombe à retardement » puis « il savait la bombe posée dessus ».
Gêne : la première phrase se lit « le chariot est à côté de la bombe », la seconde place la bombe sur le chariot ; le ressort de l’apologue en souffre.
Reformulation : « sa batterie de rechange, posée sur un chariot où se trouvait aussi une bombe à retardement ». Sens inchangé.

**B12 — Points clés, dernier point**
Passage : « Le problème du cadre, né en intelligence artificielle, est un cas particulier d’une limite épistémologique générale ».
Gêne : dans le § 5, « problème du cadre » désigne précisément la limite générale, et c’est la difficulté logique initiale qui en est un cas particulier ; ici l’expression change de référent.
Reformulation : « Le problème du cadre, au sens étroit où l’intelligence artificielle l’a posé, est un cas particulier… ». Sens inchangé.

### Gravité C

**C1 — Introduction** : « ne valent que « pourvu que » leurs conditions soient remplies » : la locution citée rend la phrase bancale. Proposition : « ne valent que sous condition, « pourvu que » leurs conditions soient remplies ».

**C2 — § 1** : « ce que nous appellerons plus loin un cadre : ce que le navigateur retient de la mer… » : deux « ce que » en apposition ; on hésite sur ce que les deux-points expliquent (« cadre » ou « façon de découper »). Proposition : « …un cadre, c’est-à-dire ce que le navigateur retient… ».

**C3 — § 1** : « Ce livre s’intéresse à son prolongement pratique » : « son » = la formule ou le constat ? Proposition : « au prolongement pratique de cette formule ».

**C4 — § 1, encadré question** : « à l’intérieur du modèle qu’elle a retenu » : « modèle » alors que le chapitre va parler de « cadre » ; « degré de croyance » n’a pas été introduit (le texte parlait de « jugement »). Proposition : garder, ou « à l’intérieur de la façon dont elle a découpé la situation ».

**C5 — § 2, paragraphe du mont Blanc** : paragraphe long et dense (règle non démentie à la lettre, croyance dérivée fausse, cuisson, sens caché de « pression atmosphérique », nouvelle règle). Proposition : couper avant « Ce qui cède ici ».

**C6 — § 2, tableau, ligne 3** : la règle du tableau (« Eau pure portée à 100 °C à l’air libre → ébullition ») omet « sous la pression atmosphérique » que le texte ajoute à la même étape ; petit décalage texte/tableau.

**C7 — § 2 (possible dépendance)** : la notation $A \cap (\dots) \rightarrow B$ : un lecteur cultivé lit « ∩ » comme une intersection d’ensembles ; si le ch. 1 ne le glose pas, ajouter « (A *et* l’arrière-plan) ».

**C8 — § 3** : « Le partage entre ce qui entre dans $A$ » : répétition « entre… entre ». Proposition : « Le partage entre ce qui figure dans $A$ ».

**C9 — § 3, liste des quatre choix, item 1** : les exemples « (la pression pour la règle d’ébullition ; pour le navigateur, une fissure cachée dans le mât) » peuvent se lire comme des variables retenues. Proposition : « (par exemple, la pression…) » placé juste après « que l’on néglige ».

**C10 — § 3 (possible dépendance)** : « une grandeur ou un événement $Y$ » suivi de « $\Pr(Y)$ » ; « partition » ; « loi » (au sens de loi de probabilité, homonyme de « loi » au sens courant) : notions non rappelées pour le non-spécialiste.

**C11 — § 3** : « Ce choix précède toute inférence, et il est circulaire » : un *choix* n’est pas circulaire, c’est la *justification* du choix qui l’est. Proposition : « et sa justification est circulaire ».

**C12 — § 3** : « Le compromis est plus serré qu’il n’y paraît » : calque de « the trade-off is tighter ». Proposition : « L’arbitrage est plus délicat qu’il n’y paraît ».

**C13 — § 3** : « les rend maniables et générales en apparence » : « en apparence » porte sur les deux adjectifs ou sur le seul second ? Les deux lectures sont possibles ; je ne tranche pas.

**C14 — § 3** : le paragraphe « Ne suffirait-il pas… » et l’encadré « Énoncer plus ou taire plus » disent deux fois la même chose avec la même chute (« Aucun réglage… »). Alléger l’un des deux.

**C15 — § 4** : « cette dépendance envers le cadre » : « envers » est inhabituel ici. Proposition : « à l’égard du cadre ».

**C16 — § 4, paragraphe sur la déduction** : très long ; et dans « la déduction transporte la fidélité au réel lorsqu’elle est présente au départ », « elle » peut renvoyer à la déduction. Proposition : couper avant « Considérons à nouveau la poutre » ; « lorsque cette fidélité est présente au départ ».

**C17 — § 4, encadré formel (possible dépendance)** : « *d*-séparation », « *do*-calcul », « quantité interventionnelle », « score de non-conformité » ne sont pas glosés ; acceptable dans un encadré technique, mais une incise par terme aiderait.

**C18 — § 4, cas clinique** : « Déployé dans une autre région, ou quelques années plus tard […]. Entre-temps, l’organisation des urgences a changé » : « Entre-temps » ne convient qu’au second scénario (le déploiement plus tardif). Proposition : « Entre-temps ou d’un lieu à l’autre, … ».

**C19 — § 4, cas clinique** : « car toutes avaient été obtenues » : « toutes » = les mesures ou les cohortes ? Le sens bouge peu. Proposition : « car toutes ces mesures avaient été obtenues ».

**C20 — § 5** : « [@A-VERIFIER: Shanahan, « The Frame Problem », SEP] » : marqueur éditorial qui s’affichera tel quel ou mal ; à résoudre avant publication.

## 3. Appréciation globale

Le chapitre se lit bien et sa progression est nette. Les sections les plus accessibles sont le § 1 (exemples maritimes concrets, image de la carte et de la coque) et le § 2 (l’eau bouillante, très pédagogique, avec un tableau utile ; seul le paragraphe du mont Blanc est un peu chargé). Le § 3 est solide, mais c’est là que se trouve la principale difficulté conceptuelle : la frontière entre *cadre* et *représentation* n’est pas tracée de façon cohérente (A1). Les sections les moins accessibles sont la fin du § 3 (lecture de l’équation, encadré formel aux pronoms serrés) et le § 4, qui s’appuie sur des notions du ch. 1 (poutre, valide/solide, série de référence) et introduit vite la prédiction conforme et le calcul causal. Le cas clinique, lui, éclaire bien l’ensemble. Le § 5 est clair, si l’on règle la position de la bombe et la cohérence avec le dernier point clé.
