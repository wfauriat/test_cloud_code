# Lecture fraîche — chapitre 12 « Au sommet de la pile, un autre régime »

Lecteur : Opus, première lecture, seul le fichier `chapitres/12-autre-regime.md` a été lu.

## 1. Résumé (test de lisibilité)

1. Quand on passe des couches logicielles spécifiées à un grand modèle de langage, trois choses basculent ensemble (« changement de régime ») : ce qui est promis (une tendance statistique et non plus un contrat), la forme de l'échec (une erreur aussi fluide qu'une réussite) et l'issue de l'enquête (aucune ligne fautive à corriger).
2. Ce n'est pas une question de fréquence d'erreurs. Ce qui compte, c'est qu'on ne peut plus vérifier une fois pour toutes en amont. Le contrôle doit donc soit être reconstruit autour de tâches qui admettent un comparateur mécanique, soit porter sur chaque sortie.
3. La compétence des modèles forme une « frontière en dents de scie » : irrégulière, changeante d'une version à l'autre, invisible à l'usage (expérience BCG). Elle tient en partie aux « omissions de saillance » : l'information est présente mais n'est pas mobilisée.
4. La « calibration générative » oblige un modèle à inventer des faits rares, à peu près au taux de faits vus une seule fois (borne de Kalai et Vempala). Les barèmes d'évaluation, qui ne récompensent pas l'abstention, aggravent le problème.
5. Reposer plusieurs fois la question repère bien les erreurs dispersées, mais pas les erreurs constantes (idées reçues). Elle produit aussi beaucoup de fausses alertes. Un exemple chiffré à trois cas le montre.

Le fil général se suit bien. Les passages les moins clairs sont ceux qui renvoient à des notions des chapitres 7 et 9 sans les rappeler, et quelques formulations calquées.

## 2. Constats classés par gravité

### Gravité A — compréhension compromise ou contresens possible

**A1. § Trois propriétés basculent ensemble, 1er paragraphe**
« Passer d'un appel à une base de données relationnelle […] à l'appel d'un grand modèle de langage ne modifie pas un seul aspect de l'édifice technique. »
- **Problème** : en français, « ne modifie pas un seul aspect » se comprend d'abord comme « ne modifie aucun aspect », ce qui contredit la phrase suivante. Le sens voulu est sans doute celui de l'anglais *not just one aspect*.
- **Reformulation** : « … ne modifie pas seulement un aspect de l'édifice technique. »
- **Sens** : il ne bouge pas si le sens voulu est bien « plusieurs aspects à la fois », ce que la suite confirme.

### Gravité B — gêne réelle

**B1. Introduction (paragraphe unique)**
« trois propriétés basculent ensemble, déplaçant le contrôle vers chaque sortie individuelle, révélant une compétence en dents de scie et obligeant — à la lumière de la calibration (…), du cadre comme cause commune (…) et du critère de sévérité (…) — à distinguer… »
- **Problème** : la phrase finale est très longue et contient une incise de trois renvois. Les participes semblent avoir pour sujet « trois propriétés », alors que c'est leur basculement qui agit. Enfin, les trois propriétés ne sont pas nommées.
- **Reformulation** : couper la phrase. « … généralistes appelés dans des contextes ouverts. Trois propriétés y basculent ensemble : ce qui est promis, la forme de l'échec, le lieu où aboutit l'enquête. Ce basculement déplace le contrôle vers chaque sortie, révèle une compétence en dents de scie et oblige à distinguer… (en s'appuyant sur la calibration, le cadre comme cause commune et le critère de sévérité). »
- **Sens** : inchangé.

**B2. § Trois propriétés basculent ensemble, point 1**
« sans qu'aucune statistique de série ne garantisse la réponse particulière qui vient d'être émise »
- **Problème** : « statistique de série » n'est pas une expression courante. Le lecteur ne sait pas s'il s'agit d'une moyenne sur une série de tests ou d'autre chose.
- **Reformulation** : « sans qu'aucune statistique calculée sur l'ensemble des essais ne garantisse la réponse particulière… »
- **Sens** : inchangé si c'est bien le sens voulu, à confirmer par l'auteur.

**B3. § Vérifier la couche ou contrôler les sorties, 2e paragraphe**
« La nouveauté propre au sommet de la pile tient à la nature *compositionnelle* d'un grand modèle de langage généraliste. »
- **Problème** : en français, « compositionnel » évoque surtout la sémantique (le sens d'un tout composé à partir de celui de ses parties). Ce que la suite décrit, c'est qu'on peut appeler le modèle depuis n'importe quel logiciel, sur n'importe quelle tâche, et l'enchaîner à d'autres composants. C'est plutôt « composable » ou « polyvalent ».
- **Reformulation** : « … tient à ce qu'un grand modèle de langage généraliste se laisse *brancher* sur n'importe quelle chaîne de traitement. »
- **Sens** : deux lectures possibles. Si l'auteur vise un sens technique précis de « compositionnel », la reformulation le perd. À trancher.

**B4. § Vérifier la couche ou contrôler les sorties, 3e paragraphe**
« Dans l'architecture classique (@sec:ch10), cette réutilisation universelle était rendue sûre par la vérification en amont »
- **Problème** : « cette » renvoie au paragraphe précédent, qui oppose justement le modèle « universel » aux couches classiques « étroitement délimitées ». Le lecteur bute sur une réutilisation universelle attribuée à l'architecture classique.
- **Reformulation** : « Dans l'architecture classique (@sec:ch10), la réutilisation d'un même composant par de nombreux programmes était rendue sûre par la vérification en amont… »
- **Sens** : inchangé.

**B5. § Vérifier la couche ou contrôler les sorties, 1er tiret**
« l'incertitude de la génération reste enfermée dans la proposition de candidat »
- **Problème** : c'est un calque de *candidate proposal*, et l'expression est obscure.
- **Reformulation** : « … reste confinée à l'étape où le modèle propose une solution candidate ».
- **Sens** : inchangé.

**B6. § La frontière en dents de scie, 3e tiret, et Points clés, 3e puce**
« *L'indiscernabilité depuis l'intérieur.* Vue de l'interface conversationnelle… » / « indiscernable de l'intérieur de la conversation »
- **Problème** : « l'intérieur » a deux lectures : l'intérieur du modèle (« aucune alarme interne ») ou la position de l'utilisateur dans la conversation (« vue de l'interface »). Le titre du tiret et la suite tirent dans des directions opposées.
- **Reformulation** : selon le sens voulu, « *L'indiscernabilité à l'usage* » ou « *L'absence de signal interne* ». Aligner ensuite la puce des points clés sur le même terme.
- **Sens** : il bouge selon l'option retenue. Je ne tranche pas.

**B7. § La frontière en dents de scie, encadré « Omission structurelle… »**
« le champ d'application du volet (a) de la @prop:cause-commune » ; « la fermeture établie au @sec:ch07 tient strictement »
- **Problème** : l'encadré repose entièrement sur le contenu du volet (a) de la proposition et sur la notion de « fermeture ». Ni l'un ni l'autre n'est rappelé, si bien qu'un lecteur qui n'a pas le chapitre 7 en tête ne peut pas suivre la distinction (possible dépendance).
- **Reformulation** : ajouter une incise de rappel d'une ligne, par exemple « le volet (a) — selon lequel [énoncé bref] — ».
- **Sens** : inchangé. L'énoncé est à fournir par l'auteur.

**B8. § Calibration générative…, 3e paragraphe**
« Par un raisonnement statistique apparenté à l'estimation de Good-Turing, si le modèle reproduit fidèlement la distribution statistique des énoncés du corpus, il ne peut distinguer un fait vrai aperçu une seule fois d'une multitude d'énoncés plausibles mais faux… »
- **Problème** : « Good-Turing » est du jargon non expliqué. Surtout, le lien logique est elliptique : on ne voit pas pourquoi reproduire la distribution empêche de distinguer le vrai du faux. Le chaînon manquant semble être qu'un fait vu une seule fois ne pèse pas plus, statistiquement, qu'un fait jamais vu mais plausible.
- **Reformulation** : « … si le modèle reproduit fidèlement la distribution du corpus, un fait vrai vu une seule fois n'y pèse guère plus qu'une multitude d'énoncés plausibles jamais vus ; le modèle ne peut donc pas les distinguer. » Ajouter une glose d'une demi-ligne sur Good-Turing (« méthode classique pour estimer la part des cas jamais observés à partir de ceux vus une fois »).
- **Sens** : à vérifier par l'auteur, car je reconstruis le chaînon manquant.

**B9. § Calibration générative… (3e paragraphe et encadré formel) et Points clés, 4e puce**
« engendrer des énoncés faux à un taux voisin de la proportion de singletons » / borne « taux d'hallucination ≳ taux de singletons − … » / « à une fréquence comparable au taux de singletons »
- **Problème** : le texte présente le même résultat de trois façons. « Voisin » et « comparable » suggèrent une égalité approchée, alors que l'encadré donne une borne inférieure (« au moins ») corrigée de deux termes. Le lecteur ne sait pas lequel retenir.
- **Reformulation** : « … à un taux au moins voisin de la proportion de singletons » dans le corps du texte, et « à une fréquence au moins de l'ordre du taux de singletons » dans les points clés.
- **Sens** : inchangé si la borne inférieure est bien le résultat visé.

**B10. Ensemble du chapitre, à partir du § Calibration générative**
« invention », « hallucinations », « confabulation », « fabrication de faits rares », « inventer »
- **Problème** : cinq termes pour un même phénomène (ou pour des sous-espèces ?). « Hallucination » n'apparaît qu'entre parenthèses dans l'encadré, et « confabulation » arrive avec Farquhar sans être reliée aux autres. Le lecteur se demande si ce sont des synonymes.
- **Reformulation** : à la première occurrence, une incise du type « (on parle aussi d'hallucination ou de confabulation) », puis s'en tenir à « invention ».
- **Sens** : si l'auteur entend une distinction (chez Farquhar, la confabulation est un sous-type), il faut la dire. À trancher.

**B11. § Calibration générative…, à partir du paragraphe sur Kalai et al. 2025 ; repris dans les Points clés**
« une devinette tombée juste par hasard », « Les erreurs de devinette », « la devinette assurée »
- **Problème** : en français courant, une « devinette » est une énigme posée à quelqu'un. Le mot ne désigne pas une réponse donnée au hasard (*guess*). Comme le terme sert d'étiquette à tout un régime d'erreur, la gêne revient à chaque occurrence.
- **Reformulation** : « réponse devinée », « réponse au jugé » ou « conjecture » (« les erreurs de conjecture », « la réponse devinée avec assurance »).
- **Sens** : inchangé.

**B12. § Calibration générative…, 4e paragraphe**
« Il en résulte un contraste décisif entre deux régimes d'erreur… »
- **Problème** : « en » renvoie au paragraphe précédent (les barèmes qui récompensent la réponse devinée). Or le contraste entre erreurs dispersées et erreurs constantes ne découle pas de ces barèmes. Le connecteur est trompeur.
- **Reformulation** : « Ces inventions n'ont cependant pas toutes la même allure dès que l'on tente de contrôler un modèle… »
- **Sens** : inchangé, sauf si l'auteur voulait réellement établir un lien causal, auquel cas il faudrait l'expliciter.

**B13. § Calibration générative…, exemple quantitatif, « Calcul », 2e cas**
« les quatre autres tirages s'en écartent presque toujours ($1 - 0{,}18^4 \approx 99{,}9\,\%$) »
- **Problème** : la formule donne la probabilité qu'*au moins un* tirage s'écarte, mais la phrase dit que les quatre s'écartent. Le premier cas, lui, est formulé correctement (« au moins un des quatre autres tirages »). Le troisième cas dit de même, de façon imprécise, que « les tirages suivants rejoignent Vénus ».
- **Reformulation** : « au moins un des quatre autres tirages s'en écarte presque toujours ». Pour le troisième cas : « au moins un des tirages suivants s'écarte de Mercure ».
- **Sens** : inchangé, car le calcul ne change pas.

**B14. § Calibration générative…, encadré « Deux sens de calibration… », 3e paragraphe**
« conclure de façon trop absolue que « rien dans le modèle ne calcule de signal lorsqu'il quitte sa zone de compétence » »
- **Problème** : la phrase est présentée comme une citation, mais elle ne figure pas dans le chapitre. Le plus proche est « Aucune alarme interne n'informe l'utilisateur… ». Le lecteur cherche d'où elle vient, et se demande si le texte se corrige lui-même ou s'il cite un autre chapitre.
- **Reformulation** : « … conclure de ce qui précède (aucune alarme interne, § dents de scie) que rien dans le modèle ne calcule de signal… », sans guillemets, ou avec un renvoi explicite.
- **Sens** : inchangé.

**B15. Ensemble du chapitre**
« test de référence », « test de référence passé sur un jeu d'épreuves public », « classement général », « bancs d'épreuve », « protocoles d'évaluation », « barème »
- **Problème** : le même objet (*benchmark*) reçoit plusieurs noms. « Bancs d'épreuve » arrive tard et sans lien avec les autres termes.
- **Reformulation** : s'en tenir à « test de référence » et à « classement » pour le palmarès public, et remplacer « dans les bancs d'épreuve » par « dans les tests de référence ».
- **Sens** : inchangé.

**B16. § Calibration générative…, 1er tiret, et dernier paragraphe de l'exemple**
« (avec une température d'échantillonnage non nulle) » ; « un décodage déterministe (ou une température très basse) écrase toute dispersion »
- **Problème** : tout l'exemple repose sur cette notion, et elle n'est pas expliquée. Un lecteur cultivé ne sait pas ce qu'est une « température » de modèle (possible dépendance au chapitre 11).
- **Reformulation** : à la première occurrence, « (avec une température d'échantillonnage non nulle, c'est-à-dire en laissant une part de hasard dans le choix des mots) ».
- **Sens** : inchangé.

### Gravité C — confort ou style

**C1. § Trois propriétés basculent ensemble**
« l'endroit où aboutit l'enquête » / « ce que trouve l'enquête » / « Le lieu où atterrit l'enquête »
- **Problème** : la troisième propriété reçoit trois formulations dans la même page, et « atterrit » est un calque de *lands*.
- **Reformulation** : « Le lieu où aboutit l'enquête » partout.

**C2. § Trois propriétés…, point 3**
« on ne fusionne pas un correctif local dans une distribution de probabilité »
- **Problème** : « fusionner un correctif » est du jargon de développeur, calqué de *merge a patch*.
- **Reformulation** : « on n'applique pas un correctif local à une distribution de probabilité ».

**C3. § Trois propriétés…, paragraphe « Il importe… »**
« un producteur dont le taux d'erreur diminue »
- **Problème** : « producteur » est employé dans un sens technique sans être rappelé (possible dépendance au chapitre 9).

**C4. § Trois propriétés…, paragraphe d'une phrase avant l'encadré**
« De plus, opposer une « divergence définissable »… »
- **Problème** : ce paragraphe d'une seule phrase annonce exactement ce que l'encadré redit aussitôt. De plus, « De plus » n'ajoute rien à l'argument précédent : c'est une réserve.
- **Reformulation** : « Encore faut-il ne pas idéaliser les logiciels traditionnels : … », ou fondre la phrase dans l'encadré.

**C5. Ensemble du chapitre**
« comparateur », « comparateur mécanique »
- **Problème** : c'est une notion centrale, jamais définie ici (possible dépendance). Le sens se devine.

**C6. § Vérifier la couche…, dernier paragraphe**
« comme une chaîne de caractères fiable […], la chaîne entière (@sec:ch08) » ; « l'interface demeure aussi lisse »
- **Problème** : le mot « chaîne » apparaît deux fois à quelques mots d'écart, dans deux sens différents. Et « aussi lisse » appelle un « que » implicite.
- **Reformulation** : « l'ensemble de la chaîne de traitement » ; « l'interface reste aussi lisse qu'avant ».

**C7. § La frontière en dents de scie, 2e tiret**
« chaque changement d'alignement ou d'outillage », « la consigne système »
- **Problème** : ce jargon n'est pas glosé (possible dépendance au chapitre 11).

**C8. § La frontière…, encadré BCG**
« ont eu 19 points de pourcentage de moins de chances de parvenir à une solution correcte »
- **Problème** : la phrase est lourde.
- **Reformulation** : « ont trouvé la solution correcte 19 points de pourcentage moins souvent que… ». Le sens ne bouge pas.

**C9. § La frontière…, paragraphe « Cette sensibilité déroutante… »**
- **Problème** : « cette sensibilité aux détails du contexte » ne reprend qu'un seul des trois traits qui précèdent (l'irrégularité face à la reformulation). Le lecteur cherche brièvement le référent.
- **Reformulation** : « Cette sensibilité à la formulation, notée plus haut, éclaire… ».

**C10. § La frontière…, encadré « Omission structurelle… »**
« au sens où un modèle mécanique omet la corrosion saline » ; « les données du dossier » ; « le premier robot »
- **Problème** : ces exemples renvoient à des chapitres antérieurs (possibles dépendances). Pour Dennett, « le premier robot » suppose que l'on connaisse l'apologue et ses trois robots.
- **Reformulation** : une demi-phrase de contexte, par exemple « dans l'apologue de Dennett, où des robots successifs doivent sortir une batterie d'une pièce piégée… ».

**C11. § La frontière…, encadré, dernier tiret**
« interroger un autre cheminement »
- **Problème** : on n'interroge pas un cheminement.
- **Reformulation** : « emprunter un autre cheminement ».

**C12. § Calibration générative…, 1er paragraphe**
« Une deuxième famille d'échecs »
- **Problème** : la première famille n'a pas été nommée comme telle. On comprend après coup qu'il s'agit des omissions de saillance.
- **Reformulation** : « Une deuxième famille d'échecs, distincte des omissions de saillance, … ».

**C13. § Calibration générative…, 3e paragraphe**
« ce sont des *singletons* (ou *monofacts*) »
- **Problème** : « monofacts » est un anglicisme qui n'apporte rien au lecteur français. L'auteur peut le garder s'il le présente comme le terme anglais : « (en anglais *monofacts*) ».

**C14. § Exemple quantitatif, « Mise en place »**
« tire 5 réponses indépendantes (la réponse initiale suivie de quatre répétitions) » ; « sachant que la première réponse est fausse » / « sachant que la première réponse était juste »
- **Problème** : le nombre est écrit tantôt en chiffres, tantôt en lettres, et le temps change d'une définition à l'autre alors qu'elles sont parallèles.
- **Reformulation** : « cinq réponses » ; « est juste ».

**C15. § Exemple quantitatif, cas 3**
« seulement 9 % à Mercure (la bonne réponse en moyenne sur l'orbite) »
- **Problème** : la parenthèse est obscure.
- **Reformulation** : « (la bonne réponse, si l'on fait la moyenne sur les orbites) ».

**C16. § Exemple quantitatif, « Lecture », 1re puce**
« *La répétition attrape efficacement la devinette.* »
- **Problème** : le lecteur peut sentir une tension avec la 3e puce : sur ce même cas, le contrôle alerte aussi dans 99,9 % des bonnes réponses, donc il alerte presque toujours. « Efficacement » peut alors sembler contredit. Ce n'est pas un problème d'argument, mais de présentation.
- **Reformulation** : une incise de renvoi (« … au prix d'alertes quasi systématiques, voir plus bas ») ou rien. À la discrétion de l'auteur.

**C17. Encadré « Deux sens de calibration », Introduction, 3e paragraphe du § Trois propriétés**
« les décisions uniques (@sec:ch04) » ; « l'orientation remplace la spécification » ; « la nuance annoncée au @sec:ch07 »
- **Problème** : ces notions reprises de chapitres antérieurs ne sont pas glosées (possibles dépendances). Le sens se devine à peu près.

**C18. § final (transition), dernière phrase**
« Le @sec:ch13 va maintenant synthétiser l'appareil épistémologique de la @sec:partie-2 et cette analyse informatique en deux axes de classement des erreurs et quatre sources de comparateurs. »
- **Problème** : la phrase est dense. « synthétiser A et B en C et D » se lit mal.
- **Reformulation** : « Le @sec:ch13 réunira l'appareil épistémologique de la @sec:partie-2 et cette analyse informatique : il en tirera deux axes de classement des erreurs et quatre sources de comparateurs. »

## 3. Appréciation globale

Le chapitre est solidement construit et son fil se suit sans difficulté majeure : basculement, conséquences pour le contrôle, frontière, calibration, répétition. L'unique constat de gravité A est une tournure calquée en ouverture, facile à corriger.

**Sections les plus accessibles :**
- « Trois propriétés basculent ensemble », avec l'encadré *Mars Climate Orbiter* ;
- « La frontière en dents de scie », jusqu'à l'encadré sur les omissions : exemples concrets, définitions claires ;
- l'exemple quantitatif, bien posé ; ses calculs, que j'ai vérifiés, sont cohérents avec le texte.

**Sections les moins accessibles :**
- l'encadré « Omission structurelle, omission de saillance… », qui dépend entièrement de la proposition « cause commune » et de son volet (a), non rappelés ;
- le paragraphe d'exposition de la borne de Kalai et Vempala (Good-Turing, lien logique elliptique, « voisin » contre « borne inférieure »).

Sur le plan du vocabulaire, deux harmonisations allégeraient la lecture :
- le terme « devinette », qui pose problème en français ;
- les noms donnés au phénomène d'invention et aux tests de référence.
