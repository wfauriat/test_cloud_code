# Lecture fraîche du chapitre 99 (Conclusion), par Sonnet

Lecture du seul fichier `chapitres/99-conclusion.md`. Aucun fichier modifié hormis ce rapport.

## 1. Ce que j'ai compris (test de lisibilité)

1. La conclusion applique au livre sa propre méthode : un livre est une représentation à cadre fini qui ne peut pas certifier son cadre de l'intérieur. Elle ne contient aucune notion nouvelle.
2. Un grand tableau donne à chaque énoncé principal un statut (définition, résultat sous hypothèses, hypothèse de travail, constat empirique) et son « point le plus faible ». Trois enseignements en sortent : le poids pratique repose sur des hypothèses de travail, les constats empiriques sont rares et datés, les chiffres sont illustratifs.
3. Six tensions restent ouvertes (distance optimale du contrôleur, coût contre indépendance, omission de saillance, prise en compte comme comportement, signe du produit erreur × échappement, statut des remèdes). Une septième partie en liste d'autres.
4. Des observations répétées (pas un épisode isolé) affaibliraient l'argument : contrôles du même cadre qui attrapent pourtant les erreurs, modèles partagés sans hausse d'échappement, erreurs injectées qui ne confirment pas les échappements attendus. L'élaboration du livre avec des modèles de langage est déclarée. Les comparateurs utiles du livre sont la littérature, le domaine du lecteur et le monde, et sa validation ne se tranche pas de l'intérieur.
5. Posture finale : le livre se tient pour la meilleure hypothèse de travail disponible, retenue faute de mieux. Il demande d'agir d'après lui là où l'erreur coûte peu, de garder marge et verrou ailleurs, et d'entretenir des comparateurs capables de le contredire à temps.

## 2. Constats classés par gravité

### Gravité A (contresens possible)

**A1. Section « Le signe du produit… » (2e paragraphe).**
Passage : « Dans l'exemple illustratif de ce chapitre, le risque sous appariement des probabilités reste même plus bas avec le modèle partagé (1,93 %) qu'entre pairs (5,57 %). »
Gêne : dans une conclusion, « ce chapitre » peut désigner la conclusion elle-même (le chapitre 16 n'est pas nommé dans la phrase). « reste même plus bas » a un « même » mal placé et peut se lire comme un démenti de l'avertissement du livre (le modèle partagé augmenterait le risque). Le lecteur doit deviner que la phrase illustre l'absence de conclusion générale. « entre pairs » n'est pas défini ici.
Reformulation minimale : « Dans l'exemple illustratif du @sec:ch16, le risque sous appariement des probabilités est, au contraire, plus bas avec le modèle partagé (1,93 %) qu'entre pairs (5,57 %) ».
Deux lectures : (i) l'exemple montre que le produit peut baisser, donc que rien ne se déduit en général ; (ii) l'exemple tempère l'avertissement. Le contexte suggère (i), mais je ne tranche pas.

**A2. Fin de « Le livre devant ses propres questions ».**
Passage : « C'est pourquoi l'ouvrage demande, comme l'annonçait l'avant-propos, à être jugé sur ce qu'il énonce, et sur rien d'autre. »
Gêne : le connecteur « C'est pourquoi » enchaîne mal sur ce qui précède (la validation ne se tranche pas de l'intérieur et reste ouverte aux comparateurs). « sur rien d'autre » peut se lire comme « pas sur sa provenance ni sur sa prose » ou comme « pas sur sa cohérence interne », ce qui contredirait la phrase d'avant.
Reformulation minimale : expliciter l'exclu, par exemple « à être jugé sur ce qu'il énonce, non sur sa provenance, ni sur la netteté de sa prose, ni sur sa seule cohérence ». Le sens change selon ce qu'on exclut ; je ne tranche pas.

### Gravité B (gêne réelle)

**B1. Tableau, ligne de la proposition « comparateur ».**
Passage : « pas de détection sans comparateur, désaccord et prise en compte » ... « sa portée tient aux cinq conditions et à l'idée qu'elles cèdent séparément ».
Gêne : l'énoncé en cite trois, la cellule voisine en annonce cinq. Les cinq ne sont énumérées qu'à la dernière page (« existe, se trompe autrement, reste comparable, arrive à temps, trouve quelqu'un pour l'entendre »), avec d'autres mots. Le lecteur ne sait pas si « désaccord » = « se trompe autrement ».
Reformulation minimale : citer les cinq conditions une fois dans le tableau, avec les mêmes mots qu'à la fin, ou écrire « les cinq conditions (dont comparateur, désaccord et prise en compte) ».

**B2. Tableau, « Enseignement 1 », section « La tension entre coût et indépendance… », Points clés.**
Passages : « La tension entre coût et indépendance » (titre, enseignement 1, points clés) ; « l'indépendance tend à se payer en comparabilité » (tableau, proposition) ; « Leur prix se reporte alors sur la comparabilité ».
Gêne : la tension est formulée comme coût contre indépendance, puis comme indépendance contre comparabilité. Le lecteur ne voit pas si le « coût » est la comparabilité, un coût monétaire ou un coût de traduction. La phrase « Traduire un taux d'attaque chimique… coûte moins en calcul qu'en traduction et en autorité » suggère que le coût est déplacé, mais la formule du titre ne le dit pas.
Reformulation minimale : un seul libellé, par exemple « La tension entre indépendance et comparabilité (le coût s'y déplace) ». Si le livre tient réellement deux tensions distinctes, cela devrait être dit ; je ne tranche pas.

**B3. Tableau, notations non glosées.**
Passages : « $p^\ast = \Delta U / (\Delta U + L)$ » ; « $B_1 \cap (B_2 \cup B_{\text{cmp}})$ » ; « la VPP chute ».
Gêne : ΔU, L, B₁, B₂, B_cmp et l'acronyme VPP ne sont pas rappelés. La VPP n'est développée qu'à la section « La prise en compte… » (« valeur prédictive positive »), bien plus bas. « ne se justifie qu'au-dessous du seuil » ne dit pas de quelle grandeur (probabilité de perte ?).
Reformulation minimale : « valeur prédictive positive (VPP) » à la première occurrence ; une demi-phrase de glose pour p* (« seuil de probabilité de perte p* ») et pour les angles morts (« B₁ : angle mort du producteur ; B₂ : celui du contrôleur ; B_cmp : celui de la comparaison »).

**B4. Tableau, ligne « Au sommet de la pile… ».**
Passage : « trois propriétés basculent ensemble ; la compétence dessine une frontière en dents de scie ; la calibration générative impose d'inventer des faits rares ; reposer la question n'attrape pas les erreurs constantes ».
Gêne : quatre affirmations accolées par des points-virgules dans une cellule. « la pile » et « trois propriétés » ne sont pas identifiées. « calibration générative » et « inventer des faits rares » sont opaques pour qui n'a pas lu le chapitre. « erreurs constantes » surgit sans lien avec « reposer la question ».
Reformulation minimale : éclater en deux ou trois lignes, ou ajouter « (la pile : empilement de composants appris ; les trois propriétés : …) ». Le fond ne change pas.

**B5. Tableau, ligne « Les composants appris peuplent la case… » et dernier paragraphe de 4.3.**
Passages : « la formalité déplace la colonne, non la ligne » ; « puisque la formalité déplace la colonne et non la ligne ».
Gêne : la matrice à deux axes n'est jamais décrite dans la conclusion (seul le « premier axe » est évoqué en 2.3). Le lecteur ne sait pas quel axe est la ligne et lequel est la colonne. La formule est reprise telle quelle à la fin comme argument.
Reformulation minimale : « la formalité déplace le classement selon la manière de vérifier (colonne), non selon l'origine de l'erreur (ligne) », à ajuster selon la matrice réelle du @sec:ch13.

**B6. Tableau, jargon non gloséé.**
Passages : « l'orienter ne revient pas à le spécifier » ; « remède à trois niveaux » ; « leurs défaillances ont une adresse ».
Gêne : « orienter » (guider par la consigne ? entraîner ?) est vague. Le « remède à trois niveaux » n'est repris nulle part dans la conclusion (la liste de 2.6 ne le mentionne pas). « ont une adresse » est une métaphore non expliquée.
Reformulation minimale : « l'orienter par la consigne ne revient pas à le spécifier » ; « un remède à trois niveaux (@sec:…) » ; « ont une adresse, c'est-à-dire un endroit identifiable où les chercher ». Le sens risque de bouger sur « orienter » si le chapitre vise autre chose que la consigne.

**B7. « Enseignement 1 » contre section « Ce qui affaiblirait l'argument ».**
Passages : « ne peut être prise en défaut que dans l'usage de la grille qu'elle déplie » ; « La @prop:comparateur ne peut être démentie par aucune observation » ; plus loin « des défaillances de détection qui ne se laisseraient ranger sous aucune des cinq conditions ».
Gêne : « grille » et « déplie » ne sont pas définis (la grille = les cinq conditions ?). Surtout, l'observation finale de la liste semble démentir la proposition que la section 3 dit non démentable. L'écart « démentie / affaiblie dans son usage » demande une phrase de liaison.
Reformulation minimale : dans la liste, « des défaillances de détection qui ne se laisseraient ranger sous aucune des cinq conditions (ce qui ôterait à la grille son utilité sans réfuter la définition) ». Cette glose présuppose la lecture « utilité » ; si l'auteur entend autre chose, je ne tranche pas.

**B8. « Enseignement 2 » contre le tableau.**
Passages : « L'argument a été construit pour ne dépendre d'aucun d'eux ; ils illustrent un mécanisme sans l'établir » ; tableau : « *constat empirique* daté pour le gain de portée », « *constat empirique* daté pour la frontière », « la frontière s'appuie sur une seule expérience de terrain ».
Gêne : le statut « constat empirique » attribué à des affirmations du tableau paraît dire le contraire de « sans l'établir » et d'« aucun ne soutient l'argument ». Deux lectures : (i) l'argument central ne dépend d'aucun constat, mais certaines affirmations subsidiaires si ; (ii) les constats servent seulement d'illustration, et alors l'étiquette du tableau est trompeuse. Je ne tranche pas.
Reformulation minimale : préciser « l'argument central » ou « le noyau de l'argument ».

**B9. Section 2.1, « La distance optimale du contrôleur ».**
Passages : « qui confie le contrôle à qui partage l'interface tout en comprenant au moins une couche au-dessous » ; « celui de la comparaison tend à s'élargir ».
Gêne : « interface » et « une couche au-dessous » ne se comprennent pas sans le chapitre 18 (une couche de quoi ? de la chaîne de production ?). « celui de la comparaison » désigne un angle mort sans le nommer (« l'angle mort de la comparaison »).
Reformulation minimale : « celui que la comparaison imparfaite ajoute » ; « à qui partage l'interface (la jonction entre deux étapes) tout en comprenant au moins l'étape située en dessous ».

**B10. Sections 2.2 et 2.3, exemples allusifs.**
Passages : « Traduire un taux d'attaque chimique en perte d'épaisseur, puis convaincre une équipe de rouvrir un plan bouclé » ; « l'ingénieur qui relit le calcul de la ferrure en consultant l'implantation côtière de l'ouvrage ».
Gêne : ces exemples renvoient à un cas de corrosion jamais nommé ici. Pris seuls, ils ne s'interprètent pas (quel plan ? quelle ferrure ? pourquoi la côte ?). « omission structurelle » (2.3) est opposée à « omission de saillance » sans définition.
Reformulation minimale : une mention du cas (« dans le cas de corrosion du @sec:ch07 »). Pour « structurelle », « un facteur absent du cadre, par opposition à un facteur présent mais non mobilisé ».

**B11. Section 2.4, « La prise en compte relève du comportement… ».**
Passages : « l'appariement des probabilités » ; « Le modèle M1 a donc mis côte à côte deux politiques » ; « la baisse du taux d'erreur suivie d'une baisse de la prise en compte rend le contrôleur décoratif ».
Gêne : « appariement des probabilités » n'est pas expliqué (le relecteur examine les alertes à une fréquence égale à leur probabilité d'être vraies ?). Le « donc » ne se justifie pas par la phrase qui précède. Le 2e paragraphe empile plusieurs conditionnelles sur un contrôleur fixe, ce qui le rend dense.
Reformulation minimale : « (examiner chaque type d'alerte dans la proportion où il est fondé) » ; remplacer « donc » par « ainsi » ou le supprimer.

**B12. Section 2.5, titre et corps.**
Passages : « Le signe du produit entre taux d'erreur et échappement reste à mesurer » ; « Savoir si leur produit monte ou baisse ».
Gêne : le produit est positif ; ce qui est incertain est le sens de sa variation. « Signe » est un abus qui peut dérouter. Le même mot se retrouve dans les Points clés.
Reformulation minimale : « Le sens de variation du produit entre taux d'erreur et échappement… ».

**B13. Section 3 (« Ce qui affaiblirait l'argument »).**
Passage : « Une course sans incident ne juge guère un prévisionniste ».
Gêne : « course » est opaque (course de chevaux ? trajet ? exemple du chapitre 3 ?). Le lecteur ne sait pas ce qu'est un « incident » dans ce contexte.
Reformulation minimale : « Une prévision qui n'est pas contredite une seule fois ne juge guère un prévisionniste », ou nommer l'exemple.

**B14. Section 3, paragraphe « D'autres observations… ».**
Passage : phrase unique de six items séparés par des points-virgules, dont « des essais répétés où l'estimation que les praticiens font de leur efficacité avec un outil concorderait avec la mesure, faisant de l'étude de 2025 un cas isolé » et « l'attente écrite, le pré-mortem ».
Gêne : phrase trop longue pour être lisible ; la logique du cas « 2025 » (pourquoi la concordance ferait-elle de l'étude un cas isolé ?) est implicite ; « l'attente écrite » n'est expliquée nulle part dans la conclusion (« pré-mortem » est, lui, courant).
Reformulation minimale : une liste à puces de six lignes ; « l'étude de 2025, où les développeurs surestimaient leur gain, » ou équivalent si cela reflète le fond. Je ne précise pas le contenu de l'étude.

**B15. Section 3, 3e puce.**
Passage : « Et si l'échappement ainsi mesuré ne prévoyait pas les erreurs qui atteignent réellement l'action ».
Gêne : « prévoyait » est maladroit ; il s'agit de « prédire la fréquence » ou « rendre compte ».
Reformulation minimale : « ne permettait pas de prédire la part des erreurs qui atteignent réellement l'action ».

**B16. Titre 4.2.**
Passage : « Où ses affirmations peuvent se tromper autrement ».
Gêne : ce sont les comparateurs qui se trompent autrement, pas les affirmations ; le titre est un calque approximatif.
Reformulation minimale : « D'où peuvent venir des comparateurs qui se trompent autrement ».

**B17. Section 4.3, questions et réponses.**
Passages : « comme à tout chiffre assuré » ; « les valeurs réelles des paramètres $c$, $m$, $f$ et $u$ ».
Gêne : « chiffre assuré » est ambigu (assuré = affirmé avec assurance ?). Seul c est glosé plus haut ; m, f, u ne sont pas rappelés (renvoi à l'annexe D uniquement).
Reformulation minimale : « à toute affirmation chiffrée présentée comme assurée » ; « (part des causes partagées c, …) ».

**B18. Section 5, 2e paragraphe.**
Passage : « garder une marge et un verrou là où il engage une décision unique ».
Gêne : « il » peut désigner l'argument, le livre ou le lecteur ; le sujet est difficile à retrouver après la longue incise.
Reformulation minimale : « là où l'argument engage une décision unique » ou « là où l'on engage une décision unique ». Les deux lectures sont possibles ; je ne tranche pas.

**B19. Section 4.1, « Une provenance déclarée ».**
Passages : « il n'y a rien à ajouter à cette déclaration » ; « il ne témoigne pas qu'elle soit juste, puisqu'il en partage le cadre ».
Gêne : le paragraphe suivant reprend longuement la déclaration, ce qui contredit « rien à ajouter ». « témoigner que… soit » est un calque (« ne prouve pas qu'elle est juste »). Les pronoms « il » (l'article), « elle » (la thèse) et « en » (de la thèse) se suivent sans repère.
Reformulation minimale : « Voici, pour mémoire, cette déclaration » ; « Il ne prouve pas qu'elle est juste, puisque l'article et la thèse partagent le même cadre ».

### Gravité C (confort, style)

**C1. Tableau, ligne 1.** « ce qui reste dans l'arrière-plan $(\dots)$ ; cette frontière… » : points de suspension entre parenthèses apparemment résiduels. Supprimer ou compléter.

**C2. Section 2, introduction.** « la décision *Moffatt v. Air Canada* ne témoigne pas sur les modèles de langage » : « ne dit rien des modèles de langage » serait plus idiomatique.

**C3. Section 2.7.** « que le @sec:ch17 résout en articulant bacs à sable et verrous, mais avec un reste » contre l'introduction « qu'ils ne réduisent jamais tout à fait » : « résout » et « jamais tout à fait » se heurtent. « atténue » conviendrait.

**C4. Section 2.5, 3e paragraphe.** « reste selon les termes mêmes du livre rarement pratiquée » : incise mal placée. De plus, « Tant qu'elle fait défaut » glisse de « rarement pratiquée » à « fait défaut ».

**C5. Section 3, 2e puce.** « trouvaient… un échappement qui n'est pas plus élevé » : après un imparfait conditionnel, « qui ne serait pas plus élevé » est plus naturel.

**C6. Section 4.3.** « À notre jugement » : le texte parle ailleurs de « l'auteur » et du « livre » à la 3e personne ; seul le « nous » final est inclusif. Remplacer par « Selon l'auteur » ou « À mon sens » si l'on veut garder l'unité.

**C7. Section 2.1 et 2.4.** Le « modèle M1 » sert à deux usages (distance du contrôleur, politiques de prise en compte). Cela peut être exact, mais un lecteur n'a pas de repère pour le vérifier ; ajouter « le même modèle M1 » aiderait.

**C8. Titre 2.6.** « Le registre des remèdes » : « registre » désigne ici le mode d'énonciation (règle ou hypothèse) mais se lit d'abord comme « catalogue ». Titre plus clair : « Le statut des remèdes : règles ou hypothèses ».

**C9. Points clés, 4e puce.** « le livre n'en tire aucune autorité » est plus tranché que le corps (« un gage réel de ce travail, non une garantie absolue » pour l'article). Il s'agit sans doute de deux objets différents (outils / article) ; une précision aiderait.

**C10. Tableau, ligne 3 et section 3.** La faiblesse notée (« l'issue rare… peut peser lourd, rapport de vraisemblance de 50 ») cohabite avec « un contre-exemple unique ne juge guère mieux un argument ». Le lecteur peut y voir une tension. Un « en règle générale » suffirait.

**C11. Fin de 4.3.** « Elle reste ouverte aux comparateurs » : « Elle » (la validation) est séparé de son antécédent par une longue phrase. « Cette section » désigne ambigument 4.3 ou toute la partie 4.

## 3. Appréciation globale

Sections les plus accessibles : l'introduction, la section 5 (posture), la section 3 pour ses deux grands principes (l'épisode isolé ne départage pas ; la liste des observations tient en trois puces) et la section 4.1 sur la provenance. La voix est claire et la rhétorique (« faute de mieux », « a pu passer dans le texte sans rencontrer d'objection ») fonctionne bien. Les Points clés sont une bonne synthèse.

Sections les moins accessibles : le grand tableau, dense, avec des cellules à plusieurs affirmations, des notations et des acronymes non rappelés et une terminologie métaphorique (pile, colonne/ligne, adresse, grille) ; les sous-sections 2.3 et 2.4 qui s'appuient sur des exemples et un vocabulaire (omission de saillance, appariement des probabilités, interface, couche) que la conclusion ne rappelle pas ; la phrase-liste de la section 3 (« D'autres observations… »). Trois incohérences de formulation demandent un arbitrage de l'auteur : cinq conditions contre trois citées (B1), coût/indépendance contre indépendance/comparabilité (B2), constats « qui n'établissent pas » contre statut « constat empirique » (B8).
