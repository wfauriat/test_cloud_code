# Lecture fraîche, chapitre 1 (Boîte à outils : logique, conditionnement, probabilité)

Lecteur : Sonnet, première lecture, seul le texte du chapitre sous les yeux. Aucun fichier modifié.

## 1. Ce que j'ai compris (test de lisibilité)

1. La déduction ne fait que transporter la vérité des prémisses ; l'induction généralise des régularités sans nécessité logique. Dans les deux cas, la conclusion tient « pourvu que » des conditions soient remplies.
2. Les règles portant sur le monde matériel ont des conditions non énoncées ; on les note A ∩ (…) → B. Comme la logique ne dit rien quand ces conditions sont incertaines, il faut les probabilités.
3. Une probabilité obéit aux axiomes de Kolmogorov ; le livre la lit comme un jugement (degré de croyance), tout en contrôlant les jugements par les fréquences. La probabilité conditionnelle est une « part de mondes », et la formule des probabilités totales recompose une probabilité à partir de scénarios.
4. La règle de Bayes en cotes : cote a posteriori = cote a priori × rapport de vraisemblance. L'exemple des soudures montre qu'un même signal conclut différemment selon le point de départ, que signal normal et anormal pèsent différemment, et que multiplier suppose l'indépendance.
5. Le score logarithmique −ln p mesure la surprise d'une issue ; la différence de surprises de deux prévisions est le logarithme de leur rapport de vraisemblance ; une probabilité nulle est à éviter (surprise infinie, cote nulle irrattrapable).

Aucune zone d'incompréhension majeure : le chapitre se lit bien. Les gênes sont locales.

## 2. Constats classés par gravité

### Gravité A (compréhension compromise)

Aucun.

### Gravité B (gêne réelle)

**B1. §5 (Bayes), « soit une chance contre quatre »**
Gêne : à côté d'une probabilité de 20 %, « une chance contre quatre » se confond aisément avec « une chance sur quatre » (25 %), alors que la cote vaut 0,25 et la probabilité 0,20.
Reformulation : « soit « un contre quatre » (un cas favorable pour quatre défavorables) ». Une seule lecture correcte ; le sens ne bouge pas.

**B2. §5 (Bayes), « On peut écrire cette règle directement en probabilités, mais le dénominateur $\Pr(E)$ y masque le mécanisme de la révision »**
Gêne : la forme en probabilités n'est donnée nulle part dans le corps du texte (elle n'apparaît que dans l'encadré de dérivation, plus bas). Le lecteur doit juger d'une forme qu'il n'a pas vue ; de plus, le paragraphe précédent annonce « la règle de Bayes » sans l'énoncer.
Reformulation : insérer l'énoncé en une ligne ($\Pr(H\mid E)=\Pr(E\mid H)\Pr(H)/\Pr(E)$) ou écrire « (forme donnée dans l'encadré ci-dessous) ». Aucun risque pour le sens.

**B3. §5, exemple, « Mise en place »**
Gêne : un seul paragraphe porte neuf nombres (75, 25, 15, 85, 5, 5/17, 0,294, 4 %, 20 %), les deux hypothèses, les deux signaux et les deux a priori. Il se lit difficilement d'une traite.
Reformulation : couper en deux paragraphes (comportement de la sonde et rapports de vraisemblance ; jugements a priori). Pas de changement de sens.

**B4. §5, exemple : « soudure d'une zone suspecte » (légende de figure, calcul) et « la seconde sonde » (Lecture)**
Gêne : la mise en place parle d'« une zone qui a subi des contraintes inhabituelles », puis la suite dit « zone suspecte » sans faire le lien. De même, « la seconde sonde » apparaît sans que l'on ait dit que les deux signaux venaient de deux sondes distinctes (« deux signaux indépendants » pouvait désigner deux passages de la même sonde).
Reformulation : nommer dès la mise en place (« une zone dite suspecte, qui a subi… ») et écrire « la seconde sonde (ou le second passage) ». Pas de risque sur le sens.

**B5. §5, « Deux lignes de calcul suffisent à suivre le mécanisme »**
Gêne : le paragraphe contient en fait quatre calculs enchaînés, mêlant fractions (5/24, 5/29, 5/68, 25/29) et décimaux (1,25 ; 6,25 ; 55,6 %). « Deux lignes » renvoie sans doute aux deux a priori (deux cas de départ), mais l'expression est trompeuse.
Reformulation : « Deux cas suffisent… » et présenter les quatre issues en liste, ou reprendre la même notation partout. Le calcul n'est pas touché.

**B6. §5, Lecture : « Il rassure donc moins que le signal anormal n'inquiète, parce que la sonde manque un défaut plus souvent qu'elle ne signale à tort une soudure saine »**
Gêne : le « parce que » est elliptique ; le lien entre 25 % de défauts manqués contre 15 % de fausses alertes et l'asymétrie des facteurs (×5 contre ×0,294) n'est pas explicité. Le lecteur doit le deviner.
Reformulation : ajouter les chiffres entre parenthèses (« 25 % de défauts manqués contre 15 % de fausses alertes »). Si l'on voulait donner la raison exacte, cela relèverait d'un ajout de contenu, que je ne propose pas.

**B7. §5, dernier paragraphe de l'exemple : « L'exemple ne dit pas, en revanche, d'où viennent les chiffres de la sonde. Ils ont été mesurés sur des pièces d'étalonnage… »**
Gêne : trois tensions. (a) La mise en place a déjà dit « sur des pièces d'étalonnage », donc l'exemple dit bien d'où viennent les chiffres. (b) Ils sont déclarés « purement illustratifs » puis « ont été mesurés ». (c) La phrase suivante porte en réalité sur la validité des chiffres pour les soudures réelles.
Deux lectures plausibles : (i) la fiction est que les chiffres ont été mesurés ; (ii) le paragraphe vise à dire ce que l'exemple ne justifie pas. Je ne tranche pas.
Reformulation minimale compatible avec (i) : « Supposons que ces chiffres aient été mesurés sur des pièces d'étalonnage : ils ne valent alors pour les soudures réelles que pourvu que… ».

**B8. §6, « C'est ce que mesure le score logarithmique. La surprise d'une issue… vaut $S(p)=-\ln p$ »**
Gêne : le terme en gras est « score logarithmique », mais le texte définit la « surprise » ; le lien (même quantité ? le score est-il la somme des surprises ?) n'est dit qu'implicitement, et la boîte écrit « score logarithmique $S(p)=-\ln p$ ». Le sens de lecture (plus petit = meilleur) n'est jamais énoncé.
Reformulation : « Le score logarithmique d'une prévision est la surprise de l'issue observée, … ; plus il est faible, meilleure est la prévision. » Si l'auteur distingue score et surprise, la phrase doit être ajustée.

**B9. §6, « il correspond à un rapport de vraisemblance de 10 en faveur du premier »**
Gêne : le rapport de vraisemblance a été défini en §5 pour deux hypothèses H et H̄ et une observation. Ici, les « hypothèses » sont deux prévisions et l'observation est l'issue. L'extension n'est pas annoncée avant d'être utilisée (elle n'est formulée qu'à la phrase suivante et dans la boîte).
Reformulation : placer en tête « Les deux prévisions jouent ici le rôle des deux hypothèses de la §5, l'issue observée celui de l'observation. » Pas de changement de sens.

**B10. §6, « ne donner une probabilité nulle qu'à ce qui est réellement impossible » (corps) contre « logiquement impossible » (boîte, point 3)**
Gêne : « réellement » (physiquement ? en pratique ?) et « logiquement » ne sont pas synonymes, et tout le chapitre insiste sur la différence entre ce que la logique garantit et ce que le monde réalise.
Deux lectures : (i) impossible par pure logique ; (ii) impossible en fait. Ne tranche pas. Reformulation : harmoniser les deux passages avec le même adverbe, au choix de l'auteur.

**B11. §4, « $\Pr(B\mid A)$ mesure… la part de celles où l'arrière-plan tu $(\dots)$ laisse effectivement $B$ se produire »**
Gêne : l'image est elliptique ; on ne voit pas si $(\dots)$ désigne des circonstances qui sont réunies ou non dans chaque monde, ni pourquoi « laisser B se produire » équivaut à la réalisation de $B$.
Reformulation : « …la part de celles où les circonstances non énoncées $(\dots)$ sont réunies de sorte que $B$ se produit ». Le sens est préservé si l'auteur entend bien cela ; sinon à vérifier.

**B12. §3, encadré « Axiomes » : « famille de parties de Ω… stable par passage au complémentaire et par réunion dénombrable », « $A\cap B=\emptyset$ », « $\Pr(A\cup B)$ »**
Gêne : possible dépendance (tribu, réunion dénombrable) ; $\cup$ et $\emptyset$ ne sont pas introduits (seul $\cap$ l'a été, au §2).
Reformulation : « (famille de parties de Ω qui contient Ω et reste stable quand on prend un complémentaire ou une réunion finie ou dénombrable) » et « $\cup$ (« ou »), $\emptyset$ (ensemble vide) ». Pas de risque.

**B13. §3, « Ces axiomes fixent les règles du calcul, non le sens des nombres. Deux lectures principales leur en donnent un. »**
Gêne : pronoms en cascade (« leur » = les nombres ou les axiomes ? « en » ? « un » = sens). La phrase se décode après deux relectures.
Reformulation : « Deux lectures principales donnent un sens à ces nombres. » Le sens ne bouge pas.

### Gravité C (confort, style)

**C1. Introduction : « Ce chapitre ne suppose rien des autres »**
Tournure un peu calquée ; « ne suppose la connaissance d'aucun autre » serait plus idiomatique.

**C2. §1 : « formes authentiques de rigueur » ; « des cas qui ne l'ont pas encore été »**
« authentiques » sent l'anglais (genuine) ; « de véritables formes de rigueur ». La seconde est lourde : « des cas pas encore observés ».

**C3. §1, puces et fin du paragraphe sur la déduction : « ses prémisses et ses idéalisations »**
« Idéalisations » surgit à la fin du paragraphe et se retrouve dans la puce sans avoir été illustré (la poutre l'illustre en partie). Lecture facile, mais on gagnerait à l'annoncer dans l'exemple de la poutre.

**C4. §2 : « l'eau y bout bien avant »**
« avant » peut se lire comme temporel ; « bout à une température nettement inférieure » est plus sûr.

**C5. §2 : « conditions tues », « arrière-plan tu », « conditions sous-entendues » (intro), « non énoncé »**
Plusieurs expressions pour une même notion. « Tu » comme adjectif est rare. Harmoniser sur « non énoncé » ou « sous-entendu ». Aucun risque pour le sens.

**C6. §2 : « Un besoin se fait sentir dès maintenant. »**
Le saut est abrupt entre la remarque sur la parenthèse et le besoin de probabilités ; « Un besoin apparaît pourtant dès maintenant : » ou fusion avec la phrase suivante.

**C7. §3-§4 : « le monde a répondu » / « en regardant le monde » et « mondes » (situations possibles)**
Deux sens de « monde » (réel / possible) dans le même chapitre ; le lecteur doit s'habituer. Une incise suffit (« mondes possibles »). De même, Ω est tour à tour « issues élémentaires », « situations », « mondes ».

**C8. §3 : « vérifier… c'est ce que le @sec:ch03 appellera la calibration »**
Dépendance annoncée, ce qui est correct. Notons seulement que « calibration » côtoie « étalonnage » (pièces d'étalonnage, §5) : deux mots pour le même mot anglais, sens proches ; risque de confusion légère.

**C9. §3, encadré Nuance : titre « un débat que ce livre ne tranche pas »**
Le texte adopte pourtant la lecture comme jugement comme « position de travail ». « Ne tranche pas » est à comprendre comme « ne prétend pas le clore ». Reformulation : « un débat que ce livre ne prétend pas clore ».

**C10. §4 : « Elle donne aussi une définition précise de l'indépendance »**
« Elle » : la règle du produit ou l'équation de conditionnement ? Lecture naturelle : la règle du produit. « Cette règle permet aussi de définir… ».

**C11. §4 : « Le @sec:ch02 s'appuiera sur cette formule. Les probabilités conditionnelles… y résument »**
« y » renvoie à la formule, mais peut être pris pour le @sec:ch02. « Dans cette formule, les $\Pr(B\mid H_i)$ résument… ».

**C12. §5 : « son contraire »**
Au sens strict de la logique, le contraire n'est pas la négation. Le texte emploie $\bar H$ (négation) ; « sa négation » éviterait toute hésitation, mais « contraire » reste intelligible.

**C13. §5, encadré : « en appliquant… la règle du produit, à $H_1$ et à $H_2$ sachant $E$ »**
Syntaxe peu claire. « …en l'appliquant aux probabilités de $H_1$ et de $H_2$ sachant $E$ ».

**C14. §6, exemple des prévisionnistes : « L'écart est faible, et le rapport de vraisemblance… ne les départage guère »**
« L'écart » n'est pas chiffré (≈ 0,20) et le sens du rapport (0,816 < 1, en faveur du second) n'est pas dit. Chiffrer l'écart suffit.

**C15. §6 : « comparer les estimations de deux navigateurs… et examiner ce qu'une issue unique permet de conclure à leur sujet »**
« Navigateurs » n'a pas été introduit et peut évoquer un navigateur web (« course » lève ensuite le doute) ; « leur » est ambigu (estimations ou navigateurs). « ce couple » est compréhensible. Ajouter « (des skippers) » ou « navigateurs en mer ».

**C16. §6, encadré : « sous la première prévision contre la seconde » ; « Du côté de la règle de Bayes »**
Expressions lourdes ou familières. Reformulation : « ... de l'issue observée selon la première prévision par rapport à la seconde » ; « En termes de règle de Bayes ». Le lien entre surprise infinie et cote nulle est dit mais pas explicité (un seul parallèle, qui paraît clair au lecteur attentif).

**C17. §6 : « coûte cher » ; « Sur une série… enfin, les surprises s'additionnent »**
Le champ lexical glisse de « surprise » à « coût » sans annonce ; « enfin » ne ferme pas une énumération clairement ouverte. Rien d'indispensable.

**C18. §3 : paragraphe d'ouverture et encadré « Axiomes »**
Les règles (0 à 1, certain = 1, additivité, négation) sont énoncées deux fois à quelques lignes de distance. Le choix pédagogique se comprend (intuitif puis formel), mais le rythme s'en ressent.

Typographie : rien de manifestement fautif (guillemets, espaces avant « : » et « % », exposant du siècle corrects).

Dépendances possibles (non définies dans le chapitre) : tribu / réunion dénombrable (B12) ; renvois à la calibration et au cas des navigateurs (ch. 3) ; limite d'élasticité (poutre), bien suffisamment expliquée par le contexte.

## 3. Appréciation globale

Chapitre clair et bien construit : chaque section s'ouvre par une question, et le fil « pourvu que » est tenu jusqu'au bout. Les sections les plus accessibles sont §1 (déduction et induction, avec l'exemple de la poutre), §2 (l'eau qui bout) et §4 (conditionnement, avec le calcul du retard de livraison, très lisible). Les moins accessibles : §5, par la densité de l'exemple des soudures (paragraphes de calcul, nombres nombreux, quelques flottements sur l'origine des chiffres), et §6, où l'extension du rapport de vraisemblance aux prévisions et la relation score/surprise demandent un effort. La boîte d'axiomes (§3) est la seule vraie marche d'escalier pour un lecteur non mathématicien.

Décompte : A = 0 ; B = 13 ; C = 18.
