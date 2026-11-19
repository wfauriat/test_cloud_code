# Lecture fraîche, chapitre 8 (Indépendance, chaînes et contrôles croisés)

Lecteur : Sonnet 5.5, lecture seule du fichier 08-independance-chaines.md. Aucun autre fichier consulté.

## 1. Ce que j'ai compris (test de lisibilité)

1. Un contrôle ne vaut que par ce que le comparateur ne partage pas avec l'affirmation. L'indépendance est donc toujours relative à une classe d'erreurs, et elle coûte en comparabilité (donc en travail de traduction et de prise en compte).
2. Chaque acteur (producteur ou contrôleur) a un angle mort. Une chaîne en série réunit les angles morts de tous les maillons, plus les erreurs d'interface. Un contrôle croisé en parallèle ne garde que l'intersection, éventuellement élargie par l'angle mort de la comparaison.
3. Une cause commune plafonne le bénéfice des contrôles : avec q = 3 %, la chaîne contrôlée passe de 1,43 % à 4,39 % d'échec, et ajouter des relectures de pairs qui partagent le cadre n'y change rien (cas Knight et Leveson : même spécification, mêmes pièges).
4. Le « blanchiment » est la perte des conditions d'un résultat (hypothèses, unités, incertitude, provenance) quand il passe d'un maillon à l'autre. Il détruit la comparabilité et fait retomber un contrôle croisé en chaîne aveugle (Mars Climate Orbiter).
5. Le chapitre ouvre sur la question du contrôle réel : qu'est-ce qui rend un contrôle probant, et que deviennent les alertes quand les erreurs sont rares (chapitre suivant).

Le fil général est tenable. La plupart des gênes sont locales (notation, vocabulaire flottant, un énoncé inversé).

## 2. Constats classés par gravité

### Gravité A (compréhension compromise)

**A1. Sec. « Chaînes contre contrôles croisés », modèle M1, point 2.**
Passage : « Un désaccord n'apparaît — et n'arrête une erreur, sous réserve de prise en compte (@def:prise-en-compte) — que si la cause échappe au producteur *et* si le contrôleur ou la comparaison échoue à la faire ressortir »
Gêne : l'énoncé est inversé. Un désaccord apparaît précisément quand le contrôleur et la comparaison réussissent. Ce que la formule $B_1 \cap (B_2 \cup B_{\text{cmp}})$ décrit, c'est l'erreur qui passe sans désaccord. Pris au pied de la lettre, c'est un contresens. Le « n'arrête une erreur » enchâssé aggrave la confusion.
Reformulation minimale : « Une erreur ne franchit le contrôle sans désaccord — ni ne peut donc être arrêtée, sous réserve de prise en compte — que si la cause échappe au producteur *et* si le contrôleur ou la comparaison échoue à la faire ressortir ». L'intention est probablement celle-ci. Si l'auteur voulait vraiment dire « l'erreur n'est arrêtée que si... », ce serait une autre erreur logique, donc à vérifier.

### Gravité B (gêne réelle)

**B1. Introduction du chapitre.**
Passage : « identifie le mécanisme — le blanchiment aux interfaces — qui transforme si souvent un contrôle croisé en simple chaîne »
Gêne : « blanchiment », « chaîne » et « contrôle croisé » sont employés avant d'être définis (les définitions en gras viennent aux sections 4 et 6). Le terme « blanchiment » n'est pas éclairé avant la section qui le définit. L'image (blanchir, effacer l'origine) n'est jamais explicitée.
Reformulation : ajouter après le tiret une glose brève, par exemple « le blanchiment aux interfaces (la perte, au passage d'un maillon à l'autre, des conditions de validité d'un résultat) ». Sens inchangé.

**B2. Boîte à outils, dernier paragraphe de prose.**
Passage : « la fiabilité de l'ensemble ne descendra jamais au-dessous du risque porté par la cause partagée »
Gêne : on compare une fiabilité à un risque. C'est la probabilité d'échec qui ne descend pas sous celle de la cause commune (la boîte dit bien « ne descend jamais au-dessous de $q$ » pour l'échec).
Reformulation : « le risque d'échec de l'ensemble ne descendra jamais au-dessous de la probabilité de la cause partagée ».

**B3. Sec. « Les angles morts d'un composant » et sec. « Le blanchiment aux interfaces » : notation.**
Passages : « Ce que le cadre (@def:cadre) a laissé dans l'arrière-plan $(\dots)$ » ; « Reprenons la notation $A \cap (\dots) \rightarrow B$ introduite au @sec:ch01 et au @sec:ch02 »
Gêne : le lecteur qui n'a que ce chapitre ne sait pas ce que représentent $A$, $(\dots)$ et $B$. De plus le « $(\dots)$ » apparaît dès la section 2 sans explication. La seconde occurrence identifie ensuite « les conditions explicites $A$ » à « hypothèses de validité, réserves, marge d'incertitude », ce qui laisse flou ce que recouvre $(\dots)$ (non dit, arrière-plan ?). Possible dépendance aux chapitres 1 et 2.
Reformulation : à la première occurrence, « ce que le cadre a laissé dans l'arrière-plan, noté $(\dots)$ dans l'écriture $A \cap (\dots) \rightarrow B$ » et, en section blanchiment, dire une fois ce que désigne chaque symbole. Pas de changement de sens.

**B4. Sec. « L'indépendance est relative... », proposition.**
Passage : « tend à se payer en comparabilité — donc en coût de mise en correspondance »
Gêne : deux lectures plausibles. (a) Plus on gagne en indépendance, moins le comparateur est comparable (perte de comparabilité). (b) Plus on gagne en indépendance, plus il faut dépenser pour rétablir la comparabilité (coût). Le « donc » les fait glisser l'une dans l'autre. La section et les points clés semblent pencher vers (b) (« travail de mise en correspondance »), mais le titre « se paie en comparabilité » suggère (a).
Reformulation, sans trancher : choisir un seul verbe. Pour (b) : « tend à exiger un effort de comparabilité (mise en correspondance) croissant ». Pour (a) : « tend à diminuer la comparabilité, et donc à renchérir la mise en correspondance ». Le sens change selon l'option.

**B5. Sec. « L'indépendance est relative... », après la liste de la ferrure.**
Passage : « Ce dernier point illustre d'ailleurs une subtilité capitale de la @prop:independance : la relation entre indépendance et coût est une tendance forte, non une loi sans exception. »
Gêne : « ce dernier point » désigne la puce précédente (essai de charge, chimiste), qui illustre la tendance (indépendant, donc coûteux), pas l'exception. L'exception (comparateurs peu coûteux et décalés) n'arrive que dans l'encadré qui suit. Le lien est trompeur.
Reformulation : « Il faut d'ailleurs nuancer la @prop:independance : la relation entre indépendance et coût est une tendance forte, non une loi sans exception. »

**B6. Sec. « L'indépendance est relative... », paragraphe Levins.**
Passage : « Elliott Orzack et Steven Sober »
Gêne : les prénoms semblent permutés (Steven Orzack, Elliott Sober). Un lecteur averti y verra une erreur. À vérifier dans la bibliographie.
Reformulation : « Steven Orzack et Elliott Sober ».

**B7. Sec. « Chaînes contre contrôles croisés », encadré de nuance, 2e précision.**
Passage : « mais le modèle ne *dérive* aucun optimum »
Gêne : calque de l'anglais *derive* ; « dériver » en français évoque la dérive. Le sens voulu est « ne démontre pas ».
Reformulation : « mais le modèle n'établit aucun optimum » (ou « ne permet de déduire »).

**B8. Passage de la sec. « L'indépendance... » (cas Knight et Leveson) à la sec. « Composer des étapes spécialisées ».**
Passages : « Les systèmes techniques réels ne se réduisent presque jamais à un modèle unique contrôlé par un autre modèle. » ; « tandis que les résultats intermédiaires circulent toujours plus vite d'un maillon au suivant »
Gêne : (i) saut non annoncé : on quitte le parallèle (versions indépendantes) pour les étapes en série sans connecteur. (ii) « toujours plus vite » est une affirmation sans lien avec la phrase et sans justification : plus vite que quoi ? Le lecteur ne voit pas ce qu'elle apporte.
Reformulation : (i) ouvrir la section par « Jusqu'ici, nous avons comparé des réponses obtenues en parallèle. Or les systèmes réels... ». (ii) supprimer « toujours plus vite » ou écrire « tandis que les résultats intermédiaires passent d'un maillon au suivant sans être rediscutés ». Le sens de (ii) bouge selon que l'auteur tient à la notion de vitesse.

**B9. Vocabulaire flottant sur l'erreur de contrôle.**
Passages : proposition M1 « si les défauts d'attention sont indépendants, la probabilité d'échappement est le produit des probabilités d'oubli individuelles » ; modèle M1 « taux d'oubli vaut $1$ », « laisse néanmoins échapper », « manquent l'erreur », « $m_i$ »
Gêne : « défaut d'attention », « oubli », « taux d'oubli », « manquer », « laisser échapper » désignent apparemment la même chose (probabilité $m_i$), mais le lecteur peut croire à des notions différentes. « Taux d'oubli vaut 1 » pour un angle mort confond de plus l'ignorance structurelle avec l'oubli. Même glissement ailleurs : « taux d'échec » et « probabilité d'échec » dans la boîte à outils.
Reformulation : retenir un terme (par exemple « probabilité de non-détection $m_i$ ») et le reprendre partout.

**B10. M1 point 3 et exemple quantitatif : ce que multiplie le produit.**
Passages : M1 « $\Pr(\text{échappement}) = \prod_{i} m_i$ » (produit sur les contrôleurs) ; exemple « la probabilité qu'une erreur locale échappe à une étape vaut $p^2 = 0{,}06^2$ »
Gêne : dans M1, l'échappement est conditionnel à une affirmation déjà fausse et ne contient que les $m_i$ des contrôleurs. Dans l'exemple, on obtient $p \times m$, où le premier $p$ est la probabilité que le producteur se trompe. Le lecteur ne voit pas que les deux grandeurs diffèrent (conditionnelle contre inconditionnelle). Les indices posent aussi un problème : $i$ numérote les composants dans $B_i$ (le producteur est 1) et les contrôleurs dans $m_i$.
Reformulation : dans l'exemple, écrire « une erreur locale se produit (probabilité $p$) puis échappe au pair (probabilité $m$), soit $p \times m = p^2$ ». Sans toucher au contenu mathématique.

**B11. « Contrôle croisé » : définition contre exemple.**
Passages : définition « le deuxième composant ne reprend pas la sortie du premier comme une donnée d'entrée indiscutée : il produit une estimation ou un avis sur la même question » ; exemple et lecture « contrôle croisé ... par un pair », « Multiplier les relectures de pairs »
Gêne : deux lectures plausibles. Le pair produit-il sa propre estimation indépendamment (contrôle parallèle), ou relit-il le résultat du producteur (relecture) ? Le mot « relecture » est précisément ce que le paragraphe sur l'« illusion courante » traite comme pseudo-contrôle quand c'est la même source qui relit.
Reformulation : dans l'exemple, remplacer « relectures de pairs » par « contrôles par des pairs » ou préciser que le pair traite la même question en aval de sa propre analyse. Le sens bouge selon que l'on garde la relecture ou la production parallèle.

**B12. Encadré de nuance, 1re précision, contre l'exemple quantitatif.**
Passage : « Si une erreur n'appartient pas à $B_1$, le producteur la voit et ne l'émet pas »
Gêne : dans l'exemple, le producteur commet pourtant des erreurs propres avec $p = 6\,\%$ (étourderies hors angle mort), que le pair rattrape. Le chapitre ne dit pas que la nuance traite des causes structurelles (angle mort) et l'exemple des fautes ponctuelles. Un lecteur attentif voit deux modèles du producteur qui se contredisent.
Reformulation : « Si une cause n'appartient pas à $B_1$, le producteur est en principe capable de la voir (des étourderies ponctuelles mises à part) et ne l'émet pas ».

**B13. Encadré de nuance, 2e précision.**
Passage : « l'angle mort partagé $B_1 \cap B_2$ tend à se rétrécir, tandis que l'angle mort de la comparaison $B_1 \cap B_{\text{cmp}}$ tend à s'élargir »
Gêne : l'équation donnée est $B_1 \cap (B_2 \cup B_{\text{cmp}})$. La distribution en $(B_1 \cap B_2) \cup (B_1 \cap B_{\text{cmp}})$ n'est jamais écrite ; le lecteur doit la faire seul.
Reformulation : ajouter « puisque $B_1 \cap (B_2 \cup B_{\text{cmp}}) = (B_1 \cap B_2) \cup (B_1 \cap B_{\text{cmp}})$ ».

**B14. Sec. « Chaînes contre contrôles croisés », paragraphe « Une illusion courante ».**
Passage : « il ajoute une signature, non une protection »
Gêne : métaphore obscure (une signature de qui ? pour quoi ?). On devine « une apparence de validation ».
Reformulation : « il ajoute une apparence de validation, non une protection ». Sens inchangé.

**B15. Sec. « Le blanchiment aux interfaces » : statut du cas Mars Climate Orbiter.**
Passages : « illustre de façon dramatique ce que provoque le blanchiment à une interface » ; puis « Deux cousins proches du blanchiment des hypothèses produisent des effets symétriques aux interfaces » ; « Comme le montre *Mars Climate Orbiter*, laisser tomber l'unité ... »
Gêne : le cas est d'abord présenté comme illustration du blanchiment, puis l'effacement des unités est rangé parmi les « cousins ». Le lecteur ne sait pas si l'unité perdue est du blanchiment au sens de la définition (« perte des conditions ») ou autre chose. « Effets symétriques » est lui aussi opaque : symétriques de quoi ? Le premier cousin a le même effet (perte de comparabilité), le second un effet différent (indépendance).
Reformulation : « Deux variantes proches du blanchiment des hypothèses méritent d'être distinguées : ... » et, pour le cas, « illustre l'effacement des unités, variante du blanchiment ». Deux lectures sont possibles (unité comprise dans les « conditions » ou variante à part). Les deux sont cohérentes avec le texte ; à l'auteur de choisir.

**B16. Définition de « blanchiment » contre la fin du chapitre.**
Passages : « perte des conditions d'un résultat au moment où il change de mains » ; points clés : « la perte des conditions, des unités ou de la provenance »
Gêne : la définition n'inclut pas explicitement unités et provenance, que le texte range plus haut comme « cousins ». Le point clé élargit donc le terme sans le dire.
Reformulation : soit élargir la définition (« conditions, unités, définitions ou provenance »), soit retirer « des unités ou de la provenance » des points clés. Le sens change selon l'option retenue.

**B17. Sec. « Le blanchiment aux interfaces », fin du diagnostic.**
Passage : « le blanchiment fait enfler $B_{\text{cmp}}$ jusqu'à neutraliser l'indépendance potentielle du maillon suivant »
Gêne : en section M1, les erreurs « qui naissent aux jonctions » forment $B_{\text{interfaces}}$ (chaîne). Ici, le blanchiment gonfle plutôt $B_{\text{cmp}}$ (contrôle croisé). Le lecteur ne voit pas si le blanchiment relève de l'un, de l'autre ou des deux selon l'architecture.
Reformulation : une phrase de raccord, par exemple « dans une chaîne il nourrit $B_{\text{interfaces}}$, dans un contrôle croisé il gonfle $B_{\text{cmp}}$ ». Cela demande confirmation de l'intention de l'auteur.

**B18. Sec. « Composer des étapes spécialisées ».**
Passage : « plus l'objectif visé se situe haut dans la hiérarchie des finalités »
Gêne : « hiérarchie des finalités » est un terme qui renvoie sans doute à un chapitre antérieur ; non défini ici (possible dépendance). Le lien causal avec le morcellement est aussi un peu rapide.
Reformulation : « plus l'objectif visé est général (...) ».

**B19. Légende du tableau des comparateurs.**
Passage : « Plus on descend dans le tableau, plus la classe d'erreurs atteignable s'élargit, et plus le coût tend à croître »
Gêne : le coût n'est pas monotone dans le tableau (« Expérience » : très élevé et lent ; « Autre discipline » : élevé, plus traduction). Le « tend » atténue mais le lecteur voit une exception sans commentaire. Même remarque pour la ferrure : le « contrôle analytique rapide » est placé « tout en haut » alors qu'il correspond à la ligne « Autre méthode, même modèle » (3e ligne).
Reformulation : « (avec des exceptions : voir l'encadré ci-après) » et « en haut ou près du haut du tableau » pour le contrôle analytique.

**B20. Exemple quantitatif, lecture.**
Passage : « Multiplier les relectures de pairs qui partagent le même cadre ne permet pas d'abaisser ce plancher : comme le résume l'@eq:ch08-echappement-commun, pour toute cause commune aux contrôleurs, la probabilité d'échappement reste égale à $1$. »
Gêne : « ce plancher » n'est pas nommé. Ce n'est ni $q = 3\,\%$ ni 4,39 % ni 1 ; c'est un plancher d'échec lié à $q$, alors que l'équation citée donne un échappement égal à 1 pour une cause donnée. Le lecteur peut confondre les deux niveaux (échappement conditionnel égal à 1 et échec global plafonné par $q$).
Reformulation : « n'abaisse pas le plancher fixé par $q$ (l'échec global ne descend pas sous $q$) : conformément à l'@eq:..., une cause commune aux contrôleurs leur échappe avec une probabilité $1$ ». Pas de changement mathématique.

### Gravité C (confort, style)

**C1. Introduction.** Première phrase très longue (plus de soixante mots, deux renvois, deux parenthèses). Couper après « regard extérieur ne l'apporte pas du dehors ».

**C2. Boîte à outils, système en série.** Passage : « Lorsque toutes les étapes ont une même petite probabilité d'échec $p$, soit $1 - (1 - p)^N \approx Np$ au premier ordre » : phrase sans verbe principal (« soit » elliptique). Proposer : « ..., on a $1 - (1-p)^N \approx Np$ au premier ordre ».

**C3. Sec. « Les angles morts ».** « Deux conséquences suivent immédiatement de la @def:angle-mort » : ce sont des observations, pas des conséquences de la définition. Et « ce qui sépare $B_2$ de $B_1$, et ce qu'il en coûte de les éloigner » est vague. Proposer « Deux remarques complètent cette définition ».

**C4. Calques et tournures.** « lorsque l'on câble plusieurs composants » (calque de *wire*) ; « se tient exactement à la jonction » (calque ; « réside ») ; « le dialogue casse » (« se rompt ») ; « l'espoir de la multiplicité des modèles » (peu clair ; « l'idée qu'on gagne à multiplier les modèles »).

**C5. Table : « nouvelle graine ».** Terme technique non glosé pour un lecteur non spécialiste ; proposer « nouvelle graine du générateur aléatoire ».

**C6. Sec. « Chaînes contre contrôles croisés », ouverture.** « des effets rigoureusement inverses » : surcharge ; le texte montre union contre intersection, pas une stricte symétrie. Proposer « des effets opposés ». De même, « les angles morts s'additionnent » alors que l'union n'est pas une somme (« se cumulent » comme dans le titre de la proposition).

**C7. Proposition « chaînes » contre point clé 3.** La proposition suppose « une comparaison fidèle » pour ramener l'angle mort à l'intersection ; le point clé ajoute « compte tenu des écarts que la comparaison ne sait pas exprimer ». Pas contradictoire mais formulé différemment ; harmoniser.

**C8. M1 point 1.** « L'inclusion peut être stricte » : indiquer « $B_{\text{chaîne}}$ peut être strictement plus grand que la réunion ».

**C9. Encadré de nuance, 1re précision.** « que le producteur n'a pas su éviter ni retenir lui-même » : « retenir » est peu clair (retenir quoi ?) ; « éviter ni repérer ».

**C10. Hypothèses de M1.** « si celle-ci fait défaut, la probabilité d'échappement remonte à $1$ » est dit à propos d'une équation ensembliste (l'@eq:ch08-croise-angle-mort). Préciser « pour les causes de $B_1$ ».

Typographie : rien de manifestement fautif relevé (espaces insécables, guillemets français, majuscules corrects à l'affichage supposé).

## 3. Appréciation globale

Sections les plus accessibles : « Boîte à outils » (pédagogique, calculs simples), « Composer des étapes spécialisées » (images concrètes), le cas Knight et Leveson, et le cas Mars Climate Orbiter (très clair), ainsi que l'exemple de la ferrure sur le tableau des comparateurs.

Sections les moins accessibles : le modèle M1 (énoncé inversé du point 2, vocabulaire flottant pour les oublis, indices ambigus), l'encadré de nuance sur l'angle mort du contrôle croisé (décomposition non écrite, tension avec l'exemple chiffré) et la fin de la section blanchiment (statut des « cousins », rapport entre blanchiment, $B_{\text{interfaces}}$ et $B_{\text{cmp}}$). L'introduction souffre d'une phrase d'ouverture trop dense et de termes employés avant définition.

Les calculs de l'exemple quantitatif sont vérifiables et corrects en lecture (21,9 %, 1,43 %, 24,3 %, 4,39 %, 68,3 %).
