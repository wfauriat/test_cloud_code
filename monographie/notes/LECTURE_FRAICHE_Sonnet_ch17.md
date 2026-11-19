# Lecture fraîche du chapitre 17 « Décisions sans appel » (Sonnet)

Lecture du seul fichier `chapitres/17-decisions-sans-appel.md`, sans autre source. Aucun fichier source modifié.

## 1. Ce que j'ai compris (5 lignes)

1. Une décision fondée sur une estimation interne $p$ ignore ce que le cadre omet. Le risque réel est $p_w = 1-(1-p)(1-z)$, avec $z$ un facteur omis que le décideur ne peut ni voir ni estimer.
2. Le seul recours chiffré du chapitre est une « marge d'humilité » $b$ (jugement, pas mesure) : on n'agit que si $p+b<p^\ast$. Cela donne quatre issues (départ justifié, piège silencieux, sauvé par la marge, prudence superflue), illustrées par la course à la voile et la roulette russe.
3. Ce qui se répète se calibre (historique, scores, seuils). Une décision unique ou irréversible demande en plus un verrou : une autorisation par un comparateur indépendant.
4. Les bacs à sable permettent d'explorer à bas coût, les verrous sont réservés aux frontières de coût et d'irréversibilité ; trop de verrous usent la vigilance.
5. Le destinataire non spécialiste d'un chiffre assuré dispose de quatre questions (conditions, ce qui le ferait changer, manière la plus probable d'être faux, ce qui n'est pas modélisé), à poser à l'institution quand le chiffre vient d'un système automatisé.

## 2. Constats par gravité

### Gravité A

**A1. §1 (marge d'humilité) contre « Lecture » du bloc exemple : deux affirmations qui semblent s'opposer sur le sens de variation de la marge selon les enjeux.**
- Passage 1 : « Ce jugement doit peser d'autant plus lourd que les enjeux sont élevés, que l'acte est irréversible… »
- Passage 2 : « *Plus les enjeux sont lourds, plus la marge nécessaire est mince.* »
- Gêne : un lecteur comprend d'abord que $b$ doit être plus grand quand les enjeux croissent, puis que $b$ nécessaire diminue. Le passage 1 parle du poids du jugement et de la prudence, le passage 2 de la marge minimale qui suffit à renverser la décision. Rien ne le dit. « Enjeux élevés » est en outre ambigu : valeur absolue de $L$, ou rapport $L/\Delta U$.
- Reformulation minimale : passage 2 → « *Plus le rapport des enjeux est élevé, plus la marge qui suffit à renverser la décision est mince.* » Passage 1 → « Ce jugement doit être d'autant plus exigeant que le rapport des enjeux est élevé… ».
- Deux lectures plausibles pour le passage 1 : « exigeance du jugement » ou « valeur de $b$ ». Je ne tranche pas ; la reformulation ci-dessus suppose la première.

### Gravité B

**B1. Intro et titre : « sans appel » jamais défini.** Passage : « comment décider quand l'enjeu est sans appel » ; plus loin « quand l'enjeu est sans appel et que $p^\ast$ s'effondre ». L'expression peut signifier irréversible (aucune seconde chance) ou à rapport $L/\Delta U$ très asymétrique. Les deux se recoupent sans se confondre. Proposition : une demi-phrase d'ouverture, « (c'est-à-dire irréversible, ou tel qu'une seule erreur coûte sans commune mesure avec le gain) ». Le sens bouge selon le choix entre « irréversible » et « asymétrique ».

**B2. §1, voie du mât.** « cachée sous le manchon d'étambrai » : jargon nautique opaque. Proposition : « cachée sous la pièce qui garnit le passage du mât dans le pont (le manchon d'étambrai) ».

**B3. §1, fin du paragraphe sur $b$.** « moins d'un centième de point pour le joueur de roulette russe » : la roulette russe (seuil, estimation) n'est présentée qu'au bloc exemple. Un lecteur qui ne retient pas le @sec:ch04 ne peut vérifier le chiffre. Proposition : « … pour le joueur de roulette russe de l'exemple plus bas ».

**B4. §1, liste des « quatre issues ».** Le texte annonce quatre issues, mais l'item 3 introduit un cinquième libellé (« renoncement justifié »). La légende de la figure parle d'une issue « sauvé par la marge », alors que le quadrant en haut à droite est nommé « renoncement justifié ». Proposition : « quatre issues, dont l'une se décline en deux cas », et, dans la légende, « *renoncement justifié* en haut à droite (dont le cas *sauvé par la marge*) ».

**B5. Bloc formel, hypothèse 2.** « un facteur omis ne produit aucun désaccord dans l'ensemble des alternatives admises (@prop:desaccord) » : l'« ensemble des alternatives admises » renvoie à un chapitre antérieur et n'est pas rappelé. Possible dépendance. Proposition : « aucun désaccord entre les modèles que le cadre juge admissibles ». Je ne sais pas si cela déforme la proposition d'origine.

**B6. Après le bloc exemple.** « Le tableau ravive une tentation » : le chapitre compte trois objets (figure, deux tableaux, plus le bloc), et le « tableau » visé n'est pas identifiable. Proposition : « Cet exemple ravive une tentation… ».

**B7. Même phrase.** « cette règle, d'apparence rigoureuse, est contradictoire » : l'encadré montre que la règle est inapplicable ou conceptuellement confuse (elle exige un nombre inaccessible), pas qu'elle se contredit. Proposition : « est inapplicable » ou « confond deux choses ». Si l'auteur tient à « contradictoire » (si $z$ était accessible il ne serait plus omis), l'argument est dans l'encadré mais gagne à être annoncé ainsi.

**B8. Encadré « Pourquoi le risque omis… ».** Trois points de lisibilité.
- « une troisième quantité mesurable » : troisième après lesquelles ? L'énumération n'est pas donnée.
- « il figurerait déjà dans $p$ et dans $\Theta$ » : $\Theta$ n'est pas défini dans le chapitre.
- « aucune décomposition de la variance sur l'ensemble des alternatives admises » : jargon très dense.
- Propositions : nommer les deux quantités déjà mesurables, glosser $\Theta$ (« l'espace des paramètres du cadre ») si c'est bien cela, simplifier la dernière formule en « aucune mesure du désaccord entre alternatives admises ».

**B9. §1 et « Lecture » (premier point).** « Il ne lui reste qu'un levier » ; « *La marge d'humilité est le seul levier du décideur contre ce que le cadre omet.* » Cette exclusivité contredit la suite du chapitre, qui propose verrous, comparateurs indépendants, bacs à sable. Proposition : « le seul levier **de l'estimation** » ou « le seul levier **dans le calcul de décision** ». Sens inchangé si l'on lit « dans ce modèle ».

**B10. « Lecture », troisième point.** « *La marge a un prix, d'autant plus faible que les enjeux sont asymétriques.* » Le lien logique est elliptique (prix relatif à quoi ?), et « asymétriques » alterne avec « lourds » dans le point suivant et avec « élevés » en §1 : trois mots pour une même idée (le rapport $L/\Delta U$). Proposition : « *La marge a un prix, d'autant plus faible, comparé à la perte évitée, que le rapport des enjeux est élevé.* » et un seul vocabulaire (« rapport des enjeux ») dans les trois endroits.

**B11. Calcul et « Lecture », roulette russe.** Le texte alterne « la chambre placée face au percuteur est vide », « une chambre sur six est chargée », « la chambre chargée ($1/6$) », « le barillet était chargé ». Le lecteur ne sait pas si $z$ est la probabilité qu'une des six chambres soit chargée ou que le barillet soit effectivement chargé. « La chambre chargée ($1/6 \approx 16,7\,\%$) » est de plus un contresens littéral (une chambre n'a pas de probabilité). Proposition : « puisqu'une chambre sur six est chargée, le risque réel atteint 16,7 % » ; dernier point : « ne lui aurait appris qu'une chambre était chargée ».

**B12. §2, jargon statistique sans glose.** « zone d'abstention quand le score reste ambigu », « règles de score strictement propres [@gneiting2007] », « frontière en dents de scie de l'outil », « examiner chaque alerte ($u = 1$) » ($u$ non défini ici). Possibles dépendances aux chapitres 3, 9 et 12. Proposition minimale : une glose brève de « règles de score strictement propres » (« qui récompensent la probabilité honnêtement annoncée ») et de $u=1$ (« avec un coût d'examen unitaire »), s'il s'agit bien de cela.

**B13. §2, après la définition du verrou.** « un comparateur (@def:comparateur) capable de se tromper autrement (@prop:independance) » : « se tromper autrement » est elliptique. Proposition : « dont les erreurs ne sont pas celles de l'action examinée ». Sens inchangé si l'on lit « erreurs indépendantes ».

**B14. §2, dernier paragraphe.** « les cinq conditions du @sec:ch06 » ; le texte cite « la quatrième » puis trois autres (différence, comparabilité, prise en compte), jamais la cinquième. Le lecteur ne peut retrouver la numérotation. Proposition : nommer la cinquième ou écrire « parmi les cinq conditions… il assure l'*arrivée à temps* ».

**B15. §3, deuxième puce.** « confier l'autorité d'agir à la couche qui offre le moins de garanties » : « couche » n'est pas défini (couche de quoi ?). Proposition : « à la partie du système qui offre le moins de garanties (le modèle, plutôt que le contrôle) » si c'est la lecture voulue.

**B16. §3, définition et paragraphe qui suit.** Un « environnement isolé où les actions n'ont aucun effet extérieur » permet-il « d'interroger le monde à peu de frais » ? Le chapitre dit lui-même ensuite que « Un bac à sable ne révèle que ce qu'il modélise ». Le lecteur perçoit une tension : le bac à sable interroge une simulation, pas le monde. Proposition : « interroger une représentation du monde à peu de frais » (ou « tester ses actions à peu de frais »). Le sens glisse légèrement : la thèse « toute action est une question posée au monde » est conservée pour le monde réel, pas pour la simulation.

**B17. §3, limite 1.** « Selon le second volet de la @prop:cause-commune » (le premier volet n'a pas été rappelé) ; « l'automate dont les capteurs ignorent la couleur des fils » : exemple sans contexte, non compréhensible isolément. Proposition : rappeler le second volet en une demi-phrase ; soit expliciter l'exemple, soit le supprimer. Je ne propose pas de reformulation exacte faute du contexte.

**B18. §4, question 1.** « La question fait réapparaître l'arrière-plan $(\dots)$ » : la notation « $(\dots)$ » ressemble à un caractère de remplissage non résolu. Proposition : remplacer par le symbole de l'arrière-plan défini au chapitre antérieur, ou le supprimer (« l'arrière-plan et les limites de validité »).

**B19. Lisibilité d'ensemble : deux paragraphes trop denses.**
- Paragraphe « Devant une décision unique… » (§2, une dizaine de lignes, énumération à quatre infinitifs, plusieurs renvois, conclusion sur les alertes) : couper avant « Le @sec:ch09… ».
- Paragraphes « Pour M. Y sans facteur omis… » et « Avec une marge de 4 % » du Calcul : six cas dans deux paragraphes de calculs en prose, alors que le tableau les donne. Proposition : puces, une par situation.

### Gravité C

- **C1. §1 :** « On appelle marge d'humilité… la marge que l'on ajoute » : définition circulaire (marge/marge). « le supplément » ou « la majoration ».
- **C2. §1 :** « une casse en mer imposerait un remorquage coûtant vingt-cinq fois ce que rapporterait le succès » : le gain n'est pas défini (par rapport au voilier renforcé ?). Ajouter « le gain de vitesse du voilier léger ».
- **C3. Typographie, casse des libellés :** « Départ justifié / départ justifié », « Prudence superflue / prudence superflue », « Roulette russe » capitalisés dans les listes et en minuscule dans le texte. Harmoniser, par exemple en minuscule italique partout.
- **C4. Légende de la figure :** « Les droites d'équation $1$ » : lire « les droites d'équation $x=1$ et $y=1$ ».
- **C5. Lecture, deuxième point :** « non parce que 4 % estimerait la moitié de 8 % » : tournure peu idiomatique. « non parce que 4 % serait une estimation de la moitié de 8 % ».
- **C6. §2 :** « verrouiller » (titre, première phrase) précède la définition de « verrou ». Sens intuitif, mais un renvoi (« voir plus bas ») suffit.
- **C7. §2 :** « La calibration est le seul moyen de juger un prévisionniste » : « seul » est fort et la phrase précédente (« lorsqu'elle est l'issue attendue ») utilise « elle » pour l'issue, ce qui peut se lire comme « la calibration ». Proposition : « le moyen principal… » (sens plus faible, à l'auteur de décider) et « lorsque cette issue est celle que l'on attendait ».
- **C8. §3 :** « À insister sur les verrous » : calque, tournure orale. « À force d'insister sur les verrous ». « Elle a deux limites » (après « cette architecture à deux zones ») : « Elle » flou, préférer « Cette architecture a deux limites ».
- **C9. Lexique :** « secrets d'accès » (calque de *secrets*/*credentials* ; préférer « identifiants et clés d'accès »), « la boucle » (de l'agent, jamais nommée), « chiffre assuré » (ambigu : assuré au sens assurance ?), « arrêté le cadre » (fixé ?), « l'orientation du modèle » (alignement ?).
- **C10. §4 :** « le taire derrière une décimale la fausse » : « la » peut renvoyer à l'estimation ou à la décision. « …fausse la décision ».
- **C11. §4 :** les questions « ne demandent aucun bagage mathématique », mais la question 2 mentionne « le seuil $p^\ast$ » ; répété par « n'exige aucune compétence de spécialiste ». Alléger la redondance et glisser « le seuil à partir duquel la décision change ».
- **C12. Points clés, 2 :** « elle protège une décision unique du piège silencieux » : plus fort que le corps du texte (« rien ne garantit qu'une marge donnée couvrira un défaut massif »). Écrire « elle réduit l'exposition ».
- **C13. §3 :** « l'incident de Knight Capital » : cité sans explication. Une demi-phrase ou une note.
- **C14. Définition du verrou :** « parce que » porte à la fois sur le fait que l'action attend et sur la raison d'être du point. Proposition : « Un verrou est un point où une action attend une autorisation ; on le pose là où la réponse du monde coûterait trop cher ou serait irréversible. »
- **C15. Encadré question finale :** triple question dense. À scinder en deux phrases (calcul du seuil, puis test avec marge).

## 3. Appréciation globale

Les sections les plus accessibles sont le début de §1 (récit de la fissure du mât, effet de $z$, équation du risque réel), le contraste « citadin et parapluie / satellite » du §2, et les exemples du bulletin de pluie « il pleuvra demain / 70 % » du §4. Ce sont des scénarios concrets qui portent l'argument. La structure en quatre issues et l'articulation en entonnoir sont claires.

Les passages les moins accessibles sont le bloc formel et l'encadré sur $p_w$ (dépendances à $\Theta$, désaccord, variance, « troisième quantité »), le bloc « Lecture » (vocabulaire des enjeux flottant, sens de variation de $b$ à clarifier), la roulette russe (chambre/barillet), et la fin du §2 (cinq conditions, jargon de calibration). Les paragraphes numériques du Calcul sont denses. Le point le plus sensible est l'apparente contradiction sur le rôle des enjeux élevés (A1).
