# Lecture fraîche, chapitre 7 (Le cadre, cause commune de nos contrôles)

Lecteur : Sonnet, première lecture, texte seul.

## 1. Ce que j'ai compris (5 lignes)

Plusieurs protections qui dépendent d'une même cause amont tombent ensemble (défaillance de mode commun). De même, tous les contrôles calculés à l'intérieur d'un cadre ignorent ce que le cadre omet : leur accord ne dit rien de l'erreur due au facteur omis z. Des données du monde peuvent le révéler, mais seulement si z a varié pendant la collecte et s'il agit sur des grandeurs que le cadre enregistre ; sinon on a une dérive de distribution (cas Google Flu Trends). Une méta-procédure de contrôle du cadre adopte elle-même un cadre, d'où la régression à l'infini (no free lunch, Hume, Goodman). Un facteur nouveau n'entre donc que de l'extérieur, par l'avertissement d'un autre point de vue ou par l'épreuve du monde, et la seconde voie est limitée par son coût.

## 2. Constats

### Gravité A (2)

**A1. Sec. 3, « grandeurs que le cadre enregistre » : deux lectures possibles.**
Passage : « ses effets ne peuvent apparaître qu'à travers les grandeurs que le cadre enregistre. Et même lorsqu'ils déplacent une grandeur enregistrée, ils ne s'y montrent pas sous leur vrai nom […] Si $z$ varie sans toucher aux grandeurs mesurées, ou si le cadre n'a prévu aucune case… »
Problème : on ne sait pas si « grandeurs enregistrées » désigne les entrées $X$ ou aussi la sortie mesurée $Y$. Or $Y=g(x,z)$ dépend de $z$ par définition, donc « $z$ varie sans toucher aux grandeurs mesurées » semble impossible si $Y$ est incluse. Le bloc formel parle d'une dispersion de $Y$ sachant $x$, ce qui irait dans le sens de « $Y$ incluse ».
Reformulation minimale : préciser dans la phrase (« les variables d'entrée $X$ » ou « les sorties mesurées $Y$ »), et dire quel cas « sans toucher » vise (par exemple une autre sortie que celle mesurée). Le sens bouge selon la lecture : je ne tranche pas.

**A2. Sec. 3, exemple de l'automate et du fil rouge.**
Passage : « les capteurs n'enregistrent que la position de chaque fil et le résultat final […] à l'exclusion de la couleur. Si l'automate s'entraîne dans un simulateur où le fil dangereux occupe une place fixe ou dans lequel la couleur n'est pas modélisée, il peut couper le fil rouge au fil de mille essais simulés sans jamais rien apprendre de la couleur. »
Problème : le fil « rouge » surgit sans avoir été posé comme le fil dangereux. Comment couper « le rouge » si la couleur n'est pas enregistrée ? « au fil de » fait écho à « fil rouge » (jeu de mots involontaire). Le « ou » entre les deux simulateurs est elliptique (qui est « dans lequel » ?). L'exemple est le plus difficile du chapitre.
Reformulation minimale : « …il peut couper, par exemple, le fil situé en troisième position pendant mille essais simulés sans rien apprendre de la couleur » ; scinder en deux phrases (simulateur où la position du fil dangereux est fixe / simulateur où la couleur n'existe pas). Deux scénarios sont donc à distinguer et non à fusionner ; le sens ne change pas.

### Gravité B (15)

**B1. Sec. 1, dernier paragraphe.**
Passage : « un contrôle ne protège contre une classe d'erreurs que si le comparateur peut se tromper autrement que l'affirmation face à cette classe d'erreurs ».
Problème : lourd, avec répétition de « cette classe d'erreurs » ; « autrement » reste implicite (autrement que quoi, à quelles occasions).
Reformulation : « …que si, face à cette classe d'erreurs, le comparateur peut se tromper autrement que l'affirmation ». Sens inchangé.

**B2. Sec. 2, paragraphe du mécanisme.**
Passage : « l'accord ou le désaccord entre $f_1(x)$ et $f_2(x)$ est déjà arrêté — tout au plus à des tirages internes sans lien avec $z$ ».
Problème : la syntaxe est brisée. « arrêté à des tirages près » n'est pas français, et le lien logique entre « déjà arrêté » et « tirages aléatoires » (qui introduisent du hasard) n'est pas clair.
Reformulation : « est déterminé par $x$, aux tirages internes près, qui n'ont aucun lien avec $z$ ». Sens inchangé.

**B3. Sec. 2, même paragraphe.**
Passage : « Le rapport de vraisemblance de cet accord, conditionnellement à $x$, vaut exactement $1$ ».
Problème : annoncé avant que les deux hypothèses comparées soient nommées (elles ne le sont que dans le bloc formel) ; un lecteur non spécialiste ne sait pas « de quoi contre quoi ».
Reformulation : ajouter « pour une erreur grande contre une erreur petite ». Sens inchangé.

**B4. Sec. 2, bloc formel, deux sens de « hypothèses ».**
Passage : « *Hypothèses.* » (les trois numérotées), puis « deux hypothèses portant sur l'ampleur de l'erreur : $H_{\text{grand}}$… ».
Problème : le mot désigne tantôt les conditions du modèle, tantôt les deux cas statistiques comparés. L'hypothèse 3 (« Conditionnement sur $X=x$ ») n'est d'ailleurs pas une hypothèse mais un choix de lecture.
Reformulation : appeler les deux cas « scénarios » ou « cas » ($H_{\text{grand}}$ et $H_{\text{petit}}$ conservés comme noms), ou rebaptiser la liste « Conditions ». Sens inchangé.

**B5. Sec. 2, bloc formel, notation et vocabulaire.**
Passage : « Soit une grandeur réelle $Y=g(x,z)$ » ; « observations réelles où $Z$ aurait varié » ; « $g(X,Z)$ ».
Problème : (i) « réelle » peut se lire comme « à valeur réelle » ou comme « du monde réel » (le texte parle ailleurs d'« issue réelle ») ; (ii) $z$ minuscule (valeur) devient $Z$ majuscule (variable aléatoire) dans « Limite » sans annonce, et l'« indépendance conditionnelle de $z$ » traite $z$ comme aléatoire.
Reformulation : « une grandeur observée dans le monde $Y$ » ; une phrase indiquant que $Z$ désigne le facteur lorsqu'on le traite comme variable aléatoire. Pas de modification du contenu mathématique.

**B6. Sec. 2, hypothèse 2 du modèle.**
Passage : « aucune variable retenue dans $X$ ne varie avec $z$ au-delà de ce que $x$ fixe déjà ».
Problème : phrase dense et abstraite, difficile à saisir sans formalisme.
Reformulation : « aucune variable de $X$ ne porte de trace de $z$ en plus de ce que $x$ contient déjà ». La lecture exacte (corrélation résiduelle ?) est à confirmer par l'auteur ; je ne tranche pas.

**B7. Sec. 2, annonce avant la boîte « Nuance ».**
Passage : « Cet argument formel appelle trois précisions sur son champ d'application réel : conditionner nettement sur $x$ reste une idéalisation, et l'impuissance d'un contrôle interne face à $z$ ne retire rien à son utilité… ».
Problème : « trois précisions » annoncées, deux seulement énumérées après les deux-points ; la boîte en a trois, dont celle sur les grands modèles n'est pas annoncée. « conditionner nettement » est peu clair.
Reformulation : supprimer l'énumération et écrire « Trois nuances délimitent la portée de cet argument. » (la boîte suit). Sens inchangé.

**B8. Sec. 2, nuance 2.**
Passage : « Dans les grands modèles statistiques ajustés sur des masses d'exemples, un facteur pertinent peut même figurer dans les données ou le texte fournis en entrée… » ; « les mêmes paramètres ajustés et la même formulation de la question ».
Problème : « le texte », « la question », « la réponse produite » apparaissent sans transition : on devine qu'il s'agit de modèles de langage, mais rien ne le dit (possible dépendance : nature de ces modèles). L'« omission de saillance » est présentée en italique, non définie à fond.
Reformulation : remplacer « grands modèles statistiques » par « grands modèles de langage » si c'est bien ce que vise l'auteur, et expliciter « (le texte d'une question, par exemple) ». Sens susceptible de changer si l'auteur vise plus large (autres grands modèles) : je ne tranche pas.

**B9. Sec. 3, rééchantillonnage : contrôle interne ou observation du monde ?**
Passage : sec. 2 « rééchantillonner un jeu de données » est un contrôle interne ; sec. 3 « l'épreuve sur données tenues en réserve et le recoupement par partitions successives (souvent appelé *validation croisée*) » reposent sur les observations du monde ; le premier point clé reclasse « rééchantillonnage » comme contrôle interne.
Problème : un lecteur voit une contradiction apparente : la validation croisée est un rééchantillonnage, donc interne, mais elle est présentée comme un recours aux observations extérieures. La différence (relancer une simulation avec une nouvelle graine ≠ réutiliser les données réelles déjà recueillies) n'est pas dite.
Reformulation : une phrase sec. 3 : « Contrairement au simple tirage de graine, ces épreuves portent sur des mesures réelles, mais recueillies à une seule époque. » Deux lectures possibles de l'intention de l'auteur ; je ne tranche pas.

**B10. Sec. 3 : renvois à des chapitres antérieurs (possibles dépendances).**
Passages : « comme le relevait déjà l'analyse de l'@eq:ch02-cond-cadre » ; « le modèle clinique examiné à la @sec:ch02-rigueur-formelle » ; « la règle d'ébullition (@sec:ch02) » (sec. 5) ; « coefficient de sécurité de 1,8 qu'au @sec:ch05 » (sec. 2).
Problème : un lecteur qui n'a pas ce chapitre sous les yeux ne sait pas ce que contiennent l'équation, le modèle clinique, la règle d'ébullition. Le « 1,8 » est inutile à l'argument.
Reformulation : une demi-phrase de rappel pour le modèle clinique et la règle d'ébullition ; supprimer la parenthèse sur le coefficient 1,8. Sens inchangé.

**B11. Sec. 4, passage vers les théorèmes no free lunch.**
Passage : « donnent une expression mathématique précise à une partie de cette contrainte dans le domaine de l'optimisation ».
Problème : « cette contrainte » est floue (la régression ? l'impossibilité de certifier un cadre ?). Le lien entre l'optimisation et les méta-procédures n'est annoncé qu'à la fin du paragraphe.
Reformulation : « …à une idée voisine : aucune procédure n'est efficace sans hypothèse sur la classe de problèmes visée ». Sens inchangé.

**B12. Sec. 4, Hume : régression ou circularité ?**
Passage : « Sous sa forme philosophique, cette régression à l'infini est bien plus ancienne… » puis « revient à justifier l'induction par elle-même, de façon circulaire ».
Problème : la régression à l'infini (chaque étage a besoin d'un autre) et la circularité (l'induction se justifie par elle-même) sont deux figures différentes ; le texte passe de l'une à l'autre sous le même nom.
Reformulation : « Sous sa forme philosophique, ce problème est bien plus ancien… » ou nommer la circularité comme variante. Le sens risque de bouger si l'auteur tient les deux pour équivalentes ; je ne tranche pas.

**B13. Sec. 5 (titre et corps), « pertinence nouvelle ».**
Passage : « les deux seules voies par lesquelles une pertinence nouvelle entre de l'extérieur » ; « une pertinence nouvelle ne peut entrer dans un cadre que de l'extérieur ».
Problème : « pertinence » est ici un nom abstrait à sens de « facteur jugé désormais pertinent » (calque de *relevance*) ; « entre » avec « pertinence » sonne étrange. Terme non défini.
Reformulation : « un facteur jusque-là négligé qui devient pertinent entre… ». Sens inchangé.

**B14. Sec. 2, ferrure (premier exemple).**
Passage : « les mêmes cotes géométriques, les mêmes caractéristiques d'alliage et la même hypothèse d'air sec. Les deux calculs s'accordent jusqu'à la troisième décimale. Ce contrôle confirme utilement que le maillage n'a pas divergé… ».
Problème : le « maillage » (éléments finis) est du jargon ; l'exemple suppose que la ferrure vient du chapitre 5. Le propos est clair, mais l'accord « jusqu'à la troisième décimale » ne dit pas sur quelle grandeur.
Reformulation : « …(la discrétisation numérique du modèle) » ou retirer « maillage ». Gêne limitée.

**B15. Variation lexicale pour une même notion.**
Passages : « variables représentées $X$ », « variables retenues », « ce que le cadre enregistre », « grandeurs enregistrées », « contenu du cadre », « grandeurs mesurées ».
Problème : cinq à six expressions voisines sans équivalence posée ; elles alimentent l'ambiguïté signalée en A1 et font douter si la notion change.
Reformulation : fixer « variables représentées » pour $X$ et réserver « enregistrées » à ce que les capteurs ou bases mesurent, ou poser leur équivalence une fois.

### Gravité C (15)

**C1. Intro.** « laissant le reste dans un arrière-plan $(\dots)$ » : le « $(\dots)$ » ne se lit pas. Reformulation : « laissant le reste dans un arrière-plan non représenté ».
**C2. Sec. 1.** « ne forment qu'un double câblage sous une vulnérabilité unique » : image peu naturelle. Reformulation : « ne protègent pas davantage qu'une seule, puisqu'elles partagent la même vulnérabilité ».
**C3. Sec. 1, boîte.** « ajouter une troisième protection indépendante le réduit encore d'un ordre de grandeur » : vrai seulement si les probabilités valent environ 0,1. Reformulation : « le réduit encore (d'un ordre de grandeur si chaque panne a une probabilité de l'ordre de 1/10) ».
**C4. Sec. 1.** « Cette logique de fiabilité vaut exactement pour… » : « exactement » est surprenant (analogie, non identité). Reformulation : « s'applique tout aussi bien à ».
**C5. Sec. 2.** « — que nous notons désormais formellement $z$, reprenant la lettre esquissée au @sec:ch05 —, la situation bascule » : la virgule après le tiret fermant est lourde. Reformulation : fermer l'incise sans virgule ou la mettre entre parenthèses.
**C6. Proposition.** « partie (b) » dans l'énoncé, « volet (a) » dans le texte ; la dernière phrase répète le « statut » et mêle résultat et illustration (« la partie (b) est illustrée… »). Reformulation : choisir « volet », supprimer la phrase.
**C7. Sec. 2.** « le bloc formel suivant (modèle M3) » : la numérotation M3 renvoie à des modèles M1 et M2 non vus dans ce chapitre. Reformulation : retirer « M3 » ou rappeler d'où vient la série.
**C8. Sec. 3.** « deux limites rigoureuses qui empêchent souvent les données de jouer ce rôle de comparateur salvateur » : « rigoureuses » (calque de *rigorous*) et « salvateur » sonnent faux ; la proposition parle de « conditions », ici de « limites ». Reformulation : « deux limites précises qui empêchent souvent… de jouer ce rôle de comparateur ».
**C9. Sec. 3.** « épreuve sur données tenues en réserve » : calque de *hold-out*. Reformulation : « validation sur un jeu de test mis de côté ».
**C10. Après le cas.** « le modèle n'a cédé que face à des données indépendantes » : « cédé » est ambigu (il a fini par échouer, ou on l'a corrigé). Reformulation : « n'a été pris en défaut que par ».
**C11. Sec. 4.** « les tests de diagnostic… attrapent des défauts bien réels » : registre familier, calque de *catch*. Reformulation : « détectent ».
**C12. Sec. 4 (Goodman).** « ne peut jamais être tiré de rien » : « de rien » ambigu (de rien d'autre que les données ?). Reformulation : « ne peut jamais être déduit des seules données ».
**C13. Sec. 5.** « Sutton et Barto placent ainsi l'exploration au cœur de toute adaptation » : « ainsi » n'enchaîne pas avec la phrase précédente ; « toute adaptation » est un peu fort. Reformulation : « placent l'exploration au cœur de l'adaptation ».
**C14. Sec. 5, « règle de prudence ».** Une seule phrase de six lignes, avec deux « dès que / là où » parallèles. Reformulation : couper après « effacée » ou mettre en deux phrases.
**C15. Lexique informel.** « aucune case pour recueillir la trace » (sec. 3) ; « des essais de charge poussés » (ferrure : poussés jusqu'à la rupture ?). Reformulation : « aucune variable prévue pour » ; « des essais de charge répétés ».

## 3. Possibles dépendances (terme ou notion non définis ici)

Cadre (@def:cadre), comparateur (@def:comparateur), arrière-plan, règle de Bayes sous forme de cotes, modèle clinique et règle d'ébullition du chapitre 2, barres d'erreur du chapitre 5, décision unique du chapitre 4, éléments finis, apprentissage par renforcement (exploration/exploitation).
Les termes en gras définis dans le chapitre (défaillance de mode commun, dérive de distribution) sont bien définis avant usage et de façon accessible.

## 4. Appréciation globale

Les plus accessibles : la section 1 (analogie des pompes, très claire), la section 5 (deux voies, claire et bien argumentée), l'exemple Google Flu Trends, et la ferrure en air sec puis marin. La section 4 est lisible mais elle enchaîne trois références savantes (no free lunch, Hume, Goodman) avec des transitions un peu courtes ; le « vleu » est bien expliqué. Les moins accessibles : la section 2, qui superpose texte, proposition, bloc formel et nuances avec des notations qui glissent ($z$ / $Z$, « hypothèses » / « hypothèses »), et la section 3, dont la seconde condition (A1) et l'exemple de l'automate (A2) demandent à être précisés. Globalement, le fil d'ensemble est tenu et les connecteurs sont corrects ; les problèmes sont locaux.
