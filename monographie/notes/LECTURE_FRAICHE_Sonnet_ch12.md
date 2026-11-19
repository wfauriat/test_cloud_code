# Lecture fraîche du chapitre 12 (Sonnet) : « Au sommet de la pile, un autre régime »

Fichier lu : `chapitres/12-autre-regime.md`, seul. Les numéros de section renvoient aux titres du chapitre : §1 Trois propriétés basculent ensemble ; §2 Vérifier la couche ou contrôler les sorties ; §3 La frontière en dents de scie ; §4 Calibration générative, longue traîne et erreurs constantes.

## 1. Ce que j'ai compris du chapitre (5 lignes)

1. Quand on passe de composants spécifiés (tri, base de données) à un grand modèle de langage généraliste, trois choses changent d'un coup : la promesse (une tendance statistique, plus un contrat), la forme de l'échec (fluide, indiscernable d'une réussite) et le lieu de l'enquête (une distribution, plus une ligne fautive).
2. Le critère n'est pas la fréquence des erreurs mais le fait qu'une erreur soit définissable par rapport à un énoncé préalable, vérifiable une fois pour toutes. Il faut donc soit rebâtir un comparateur mécanique autour de la tâche, soit contrôler chaque sortie.
3. La compétence du modèle a une frontière en dents de scie, irrégulière, mouvante et invisible de l'intérieur (cas BCG). Certains échecs viennent d'une omission structurelle (facteur absent), d'autres d'une omission de saillance (facteur présent mais non mobilisé).
4. Un modèle « calibré génératif » doit inventer les faits rares et arbitraires (borne de Kalai et Vempala), et les barèmes d'évaluation qui punissent l'abstention aggravent la tendance.
5. Reposer la question plusieurs fois détecte les erreurs de devinette (réponses dispersées) mais pas les erreurs constantes (idée reçue). L'exemple chiffré le montre, avec aussi des fausses alertes.

## 2. Constats classés par gravité

### Gravité A (compréhension compromise ou contresens possible)

**A1. §3, encadré « Omission structurelle, omission de saillance et cadre comme cause commune » : le contenu de la proposition discutée n'est jamais rappelé (possible dépendance, ch. 7).**
- Passages : « On pourrait objecter à la @prop:cause-commune […] au sens où un modèle mécanique omet la corrosion saline » ; « précise exactement le champ d'application du volet (a) » ; « la fermeture établie au @sec:ch07 tient strictement » ; « confirmant ainsi la nuance annoncée au @sec:ch07 ».
- Gêne : tout l'encadré repose sur des objets du chapitre 7 que le lecteur ne peut pas reconstituer ici (l'énoncé de la proposition, son « volet (a) », la « fermeture », l'exemple de la corrosion saline, la « nuance annoncée »). Il lit une précision apportée à un énoncé qu'il n'a pas. « Modèle mécanique » est en outre ambigu (modèle de physique du mécanicien ? modèle fondé sur un comparateur mécanique ?).
- Reformulation minimale : ajouter une phrase de rappel en tête d'encadré, par exemple « Rappelons ce que dit la proposition : un contrôle calculé sur la seule représentation du modèle ne peut pas révéler un facteur que cette représentation omet ». Remplacer « volet (a) » et « fermeture » par cette formule, ou la rappeler une fois. Écrire « un modèle d'ingénierie » si c'est le sens voulu.
- Ambiguïté : je ne peux pas savoir ce que dit exactement le volet (a), donc la formule de rappel ci-dessus est une déduction à vérifier par l'auteur.

### Gravité B (gêne réelle)

**B1. Introduction, phrase unique de plus de 120 mots : « trois propriétés » ne désigne pas les trois propriétés de §1.**
- Passage : « trois propriétés basculent ensemble, déplaçant le contrôle vers chaque sortie individuelle, révélant une compétence en dents de scie et obligeant — à la lumière de la calibration (…), du cadre comme cause commune (…) et du critère de sévérité (…) — à distinguer les erreurs… ».
- Gêne : §1 définit les trois propriétés comme ce qui est promis, la forme de l'échec et le lieu de l'enquête. La phrase d'introduction énumère autre chose : déplacement du contrôle, dents de scie, partage des erreurs. Le lecteur croit à une promesse de plan qui ne sera pas tenue. La phrase est de plus encombrée de trois renvois entre tirets.
- Reformulation : couper en deux. « …trois propriétés basculent ensemble (ce qui est promis, la forme de l'échec, le lieu de l'enquête). Il en découle un déplacement du contrôle vers chaque sortie, une compétence en dents de scie, et la nécessité de distinguer les erreurs que la répétition décèle de celles qu'elle laisse passer. » Les trois renvois à la calibration, au cadre et à la sévérité peuvent passer dans la phrase suivante.
- Sens : inchangé ; seule la lecture « les trois propriétés = ces trois conséquences » disparaît, et elle est à écarter.

**B2. §1, point 1 : « sans qu'aucune statistique de série ne garantisse la réponse particulière ».**
- Gêne : « statistique de série » n'est pas une expression courante et son sens n'est pas clair (statistique sur une série de tests ? sur une série de réponses ?).
- Reformulation : « sans que la fréquence moyenne de succès ne garantisse la réponse particulière qui vient d'être émise ».

**B3. §1, point 3 : « on ne fusionne pas un correctif local dans une distribution de probabilité ».**
- Gêne : « fusionner un correctif » est un calque du *merge* informatique (git). Il est familier à un développeur, opaque à un lecteur cultivé. L'image est de plus un peu forcée.
- Reformulation : « on n'applique pas de correctif local à une distribution de probabilité ». Le sens ne bouge pas.

**B4. §1 (encadré « Définissable ne signifie pas bruyant »), puis partout : « comparateur » jamais défini dans le chapitre (possible dépendance, ch. 7 ou 9).**
- Passages : « faute de comparateur actif en exploitation » ; « un comparateur mécanique vérifiant les unités ».
- Gêne : le mot est central (tout §2, le résumé et les points clés) et apparaît dès le premier encadré sans glose. Le lecteur comprend l'idée de proche en proche, mais « comparateur actif en exploitation » reste énigmatique à sa première occurrence.
- Reformulation : à la première occurrence, ajouter une glose brève : « faute de comparateur (dispositif qui confronte la sortie à une référence indépendante) en exploitation ».

**B5. §2 : « la nature *compositionnelle* d'un grand modèle de langage généraliste ».**
- Gêne : « compositionnel » a des sens techniques précis (linguistique, informatique) qui ne correspondent pas à ce que décrit le paragraphe, à savoir une interface textuelle universelle qui permet de brancher le modèle partout et d'enchaîner ses sorties.
- Reformulation : « la nature *polyvalente et enchaînable* » ou « le caractère universel d'interface ». Le sens est celui de la phrase suivante.

**B6. §2, dernière phrase : « l'interface demeure aussi lisse, mais la garantie qui la soutenait en dessous s'est retirée ».**
- Gêne : « aussi lisse » appelle un second terme de comparaison absent (aussi lisse que quoi ?). C'est un calque de *just as smooth*. « La garantie qui la soutenait » n'est pas immédiat non plus.
- Reformulation : « l'interface reste aussi lisse qu'en dessous, mais la garantie qui la soutenait s'est retirée ».
- Sens : l'autre lecture possible (« toujours aussi lisse », sans comparaison) donne le même sens pratique.

**B7. §3, encadré BCG : « ont eu 19 points de pourcentage de moins de chances de parvenir à une solution correcte ».**
- Gêne : tournure calquée de *were 19 percentage points less likely*. « Ont eu… de moins de chances » est lourd et peut se lire comme un rapport relatif de 19 %. Or la formulation originale parle de points de pourcentage.
- Reformulation : « avaient 19 points de pourcentage de chances en moins de parvenir à une solution correcte ». « Étaient moins souvent dans le vrai, de 19 points de pourcentage » fonctionnerait aussi. Le sens ne bouge pas.

**B8. §3, mobilité entre versions : « chaque changement d'alignement ou d'outillage » et « consigne système ».**
- Gêne : « alignement » n'est pas employé ailleurs dans le chapitre, qui parle d'« orientation » et d'« ajustement postérieur à l'entraînement ». Le lecteur peut croire à un autre processus. « Consigne système » est un jargon d'ingénieur non glosé.
- Reformulation : « chaque changement d'orientation (ajustement postérieur à l'entraînement) ou d'outillage » ; « consigne système (instructions cachées qui encadrent le modèle) ».
- Si « alignement » est volontairement différent d'« orientation », le dire ; sinon harmoniser.

**B9. §3, troisième caractéristique : « L'indiscernabilité depuis l'intérieur » ; « Aucune alarme interne ».**
- Gêne : « l'intérieur » de quoi ? Le corps du texte dit « vue de l'interface conversationnelle » et les points clés disent « de l'intérieur de la conversation ». Le titre est donc opaque. « Alarme interne » est ambigu (interne au modèle ou à l'interface ?). Il se heurte plus loin à l'encadré « Deux sens de calibration », qui admet un indice d'incertitude dans le modèle.
- Reformulation : titre « L'indiscernabilité à la lecture de la réponse » ; « Aucune alarme n'est affichée à l'utilisateur ».
- Deux lectures de « interne » (dans le modèle / dans l'interface) : la seconde est cohérente avec la suite, la première la contredit. Je ne tranche pas.

**B10. §3, passage vers la théorie du cadre : saut non annoncé et mot « omission » sans antécédent.**
- Passage : « Cette sensibilité déroutante aux détails du contexte éclaire aussi un lien profond avec la théorie du cadre développée au @sec:ch07. Lorsqu'un modèle échoue… la nature de l'omission n'est pas toujours la même. »
- Gêne : on passe de la pratique d'exploitation (cartographier la frontière) à la théorie sans transition. « L'omission » surgit comme si l'échec était déjà une omission, ce que le lecteur ne sait pas (possible dépendance ch. 7). « Un lien profond » est vague. « Cadre » et « représentation » alternent sans que l'on voie s'ils sont équivalents (« non enregistrée dans le cadre » / « absent de la représentation »).
- Reformulation : « Cette sensibilité au contexte rejoint la théorie du cadre (ch. 7), pour laquelle un échec vient de ce que le système omet un facteur pertinent. Lorsqu'un modèle échoue…, cette omission n'est pas toujours de même nature. »

**B11. §3, encadré : « Dans l'apologue de Dennett, le premier robot représentait parfaitement que la bombe reposait sur le chariot ».**
- Gêne : l'apologue (robots, bombe, chariot) n'est pas raconté, et « le premier robot » suppose que le lecteur sache qu'il y en a plusieurs.
- Reformulation : ajouter une demi-phrase : « Dans l'apologue de Dennett (un robot chargé de sortir un chariot d'une pièce où une bombe est posée dessus), le premier robot… ».

**B12. §4, passim : « devinette ».**
- Passages : « les erreurs de devinette », « une devinette tombée juste par hasard », « la devinette assurée », « réponse devinée à tort », jusque dans les points clés.
- Gêne : en français, « devinette » désigne une énigme-jeu, pas l'acte de deviner. Calque de *guess*. Le sens est compris après coup mais accroche à chaque occurrence.
- Reformulation : « conjecture », « réponse au hasard » ou « réponse hasardée » (« les erreurs de conjecture », « une conjecture tombée juste »). Le sens ne bouge pas.

**B13. §4, passage sur les singletons : saut logique et jargon.**
- Passage : « Par un raisonnement statistique apparenté à l'estimation de Good-Turing, si le modèle reproduit fidèlement la distribution… il ne peut distinguer un fait vrai aperçu une seule fois d'une multitude d'énoncés plausibles mais faux… ».
- Gêne : « Good-Turing » est du jargon pour un lecteur non spécialiste. Surtout, le lien entre « proportion de singletons » et « taux d'invention » n'est pas explicité : pourquoi la part des faits vus une fois fixe-t-elle le taux d'énoncés faux ? Le lecteur doit croire sur parole le « donc » de la phrase suivante. « Générativement calibré » est lourd.
- Reformulation minimale : glose de Good-Turing (« estimation de la probabilité des événements jamais ou rarement observés ») et une phrase pont du type « la proportion de faits vus une seule fois mesure celle des faits que le modèle ne saura pas distinguer d'une invention ». À valider par l'auteur : c'est un ajout d'explication, pas de contenu mathématique. « Pour rester calibré au sens génératif ».

**B14. §4 : « à un taux voisin de la proportion de singletons » contre la borne « ≳ » de l'encadré (et « comparable » dans les points clés).**
- Gêne : « voisin de » et « comparable » suggèrent une égalité approximative. L'encadré établit une borne inférieure (au moins). Un lecteur peut retenir « taux d'invention ≈ taux de singletons », ce qui est plus fort que ce qu'affirme l'encadré.
- Reformulation : « à un taux au moins voisin de… » ou « d'au moins l'ordre de… » ; points clés : « à une fréquence au moins comparable au taux de singletons ».
- Deux lectures : approximation d'égalité (ce que le texte courant dit) ou minorant (ce que dit l'encadré). Je ne tranche pas ; l'encadré fait foi pour la rigueur.

**B15. §4 : « Il en résulte un contraste décisif entre deux régimes d'erreur… ».**
- Gêne : le paragraphe précédent portait sur les barèmes d'évaluation qui récompensent la conjecture. Le contraste dispersion/répétition n'en résulte pas : c'est un autre sujet (le contrôle par répétition). Connecteur trompeur et fil perdu.
- Reformulation : « Venons-en à la question posée plus haut : peut-on déceler ces erreurs en reposant plusieurs fois la même question ? Deux régimes d'erreur s'opposent… ».

**B16. §4, jargon d'échantillonnage non glosé.**
- Passages : « plusieurs tirages indépendants (avec une température d'échantillonnage non nulle) » ; « un décodage déterministe (ou une température très basse) écrase toute dispersion ».
- Gêne : « tirage », « température », « décodage déterministe » sont du vocabulaire de praticien. Le lecteur cultivé ne voit pas pourquoi une température nulle supprime la dispersion.
- Reformulation : « plusieurs réponses tirées indépendamment (le modèle étant réglé pour varier d'un tirage à l'autre : température d'échantillonnage non nulle) » ; en fin d'encadré, « si le modèle est réglé pour répondre toujours la même chose (décodage déterministe) ».

**B17. §4, exemple chiffré, cas 3 : « Quelle planète est, en moyenne, la plus proche de la Terre ? » avec Vénus fausse et Mercure « bonne réponse en moyenne sur l'orbite ».**
- Gêne : la plupart des lecteurs « savent » que Vénus est la plus proche. L'exemple déclare cette réponse fausse sans justification (« en moyenne sur l'orbite » est cryptique), et le lecteur peut soupçonner une erreur de l'auteur plutôt qu'une idée reçue. La démonstration en souffre.
- Reformulation : ajouter dans la mise en place « (en distance moyenne dans le temps, Mercure est la plus proche de la Terre, bien que Vénus s'en approche le plus à son minimum) » ; sinon ajouter un deuxième exemple de nature indiscutable.

**B18. Dernier paragraphe : « en deux axes de classement des erreurs et quatre sources de comparateurs ».**
- Gêne : « deux axes » et « quatre sources » surgissent sans avoir été annoncés ici ni définis. « Appareil épistémologique de la partie 2 » est abstrait. La section 2 annonçait par ailleurs le ch. 13 comme un « inventaire complet des sources de comparateurs » : ici, c'est une « synthèse ». Deux descriptions différentes du même chapitre.
- Reformulation : « Le chapitre 13 réunira l'appareil conceptuel de la partie 2 et cette analyse informatique en un classement des erreurs selon deux axes, puis en un inventaire des quatre sources de comparateurs. »

### Gravité C (confort, style)

- **C1. §1, « De plus, opposer une "divergence définissable"… ne doit pas conduire à idéaliser… »** : « De plus » ajoute alors que le paragraphe corrige ; préférer « Toutefois ». La phrase isolée précède en outre un encadré qui dit la même chose : on pourrait la fondre dans l'encadré.
- **C2. Introduction, « révélant une compétence en dents de scie »** : l'expression est employée avant sa définition en gras (§3). Acceptable en annonce de plan ; une glose brève suffirait (« une compétence irrégulière, dite en dents de scie »).
- **C3. §1, « un producteur dont le taux d'erreur diminue… qu'un producteur moins exact mais mieux contenu »** : « producteur » et « mieux contenu » viennent du chapitre 9 et ne sont pas explicités. Ambiguïté mineure de « contenu » (erreurs mieux limitées, ou mieux retenues).
- **C4. §2, « une preuve formelle contrôlée par un noyau logique » ; « ni la relecture des consignes générales »** : « noyau logique » est du jargon de démonstrateur ; « consignes générales » est flou (les instructions données au modèle ? la documentation du modèle ?).
- **C5. §3, « La réussite sur un cas proche ne fonde aucune certitude sur le cas adjacent »** : « proche » et « adjacent » sont presque synonymes ; la phrase n'apporte alors rien. Reprendre : « …ne fonde aucune certitude sur un cas voisin ».
- **C6. §3, « savoir où passe la frontière pour *vos* tâches réelles »** : première occurrence du vouvoiement, alors que le texte est impersonnel jusque-là (hormis la question finale). Rupture de ton légère.
- **C7. §4, « loin de prémunir contre l'invention, cette propriété entraîne mécaniquement la fabrication de faits rares » ; encadré : « elle *entraîne* mathématiquement l'invention »** : « entraîner » prête à confusion avec « entraînement » (training) dans un texte qui en parle sans cesse. Préférer « provoque » ou « implique ».
- **C8. Encadré « Deux sens de calibration », « doit être abandonnée »** : plus fort que le texte précédent (« s'écarter » de la calibration générative, notamment par l'abstention). Écart de ton qui peut se lire comme une exigence de la supprimer totalement.
- **C9. Encadré sur l'omission de saillance, « confirmant ainsi la nuance annoncée »** : participe sans sujet clair (la nuance est-elle confirmée par la phrase ou par la restriction ?). Participe détaché à rattacher : « ce qui confirme la nuance annoncée… ».
- **C10. Exemple chiffré, « reposer la question 5 fois » (Lecture, puce 1) contre « tire 5 réponses indépendantes (la réponse initiale suivie de quatre répétitions) »** : « reposer 5 fois » suggère 6 réponses. Écrire « tirer 5 réponses » ou « reposer la question 4 fois ».
- **C11. Légende de la figure : « taux d'alerte sur bonne réponse »** alors que le texte et le tableau disent « taux d'alerte à tort » : harmoniser.
- **C12. Encadré final, la citation « rien dans le modèle ne calcule de signal lorsqu'il quitte sa zone de compétence »** : cette phrase n'apparaît nulle part dans le chapitre (le passage le plus proche est « Aucune alarme interne… », §3). Le lecteur ne sait pas à qui l'attribuer. Écrire « la formule "aucune alarme interne" (§3), si on la prend trop absolument ».
- **C13. Terminologie flottante** : « hallucination » (encadré), « invention », « confabulation », « fabrication » désignent la même chose ; « test de référence », « jeu d'épreuves public », « classements publics » et « bancs d'épreuve » désignent le benchmark ; « régime » est pris dans trois sens (changement de régime, « deux régimes d'erreur », « Trois régimes de plausibilité », sans compter « ces deux régimes » en §1). Aucun contresens, mais le lecteur se demande à chaque fois s'il s'agit du même objet.
- **C14. Exemple chiffré, paragraphes « Calcul »** : les formules en ligne ($1 - (0{,}88^5 + 0{,}03^5)/0{,}91$) sont lisibles pour le calcul mais sans notation de probabilité conditionnelle ; deux mots (« sachant que la première est fausse ») suffisent déjà dans la mise en place. Phrase finale de l'exemple (déterminisme et comparaison par le sens) double-caveat dense : à couper en deux.
- **C15. §4, encadré formel : « Le sens de la borne est limpide »** : assertion de clarté qui précède une phrase pas si limpide. Supprimer « limpide » : « Le sens de la borne est le suivant ».

Vérifications faites sans anomalie : les nombres de l'exemple quantitatif (3 %, 82 %, 91 % ; 11,5 % ; 99,9 % ; 42,0 %) sont cohérents avec les distributions annoncées ; les trois distributions somment à 100 %.

## 3. Appréciation globale

**Sections les plus accessibles** : §1 (les trois renversements, nets et bien exemplifiés, avec la bonne mise au point que le critère n'est pas la fréquence d'erreur) ; l'encadré Mars Climate Orbiter ; le cas BCG ; l'exemple chiffré dans son principe (la logique dispersion/constance est claire, malgré le cas Vénus/Mercure).

**Sections les moins accessibles** : l'encadré sur l'omission structurelle et de saillance (A1, dépendance lourde au ch. 7), l'explication de la borne de Kalai et Vempala (B13, B14, saut logique et jargon), et l'introduction (phrase unique trop chargée, B1). Le vocabulaire d'échantillonnage (B16) et le mot « devinette » (B12) pèsent sur toute la fin de §4.

**Rythme** : bon dans l'ensemble, avec des encadrés bien placés. §4 est dense (théorie, institution, exemple chiffré, deux encadrés) et le connecteur « Il en résulte » (B15) y perd le fil.

## Décompte

- Gravité A : 1
- Gravité B : 18
- Gravité C : 15
