# Lecture fraîche — chapitre 17 « Décisions sans appel »

Lecteur : Opus, première lecture, seul le fichier `chapitres/17-decisions-sans-appel.md` a été lu.

## 1. Résumé de ce que j'ai compris (test de lisibilité)

1. La règle de l'utilité espérée subjective décide sur le risque estimé $p$, alors que l'issue dépend d'un risque réel $p_w$ qui inclut un facteur omis $z$, invisible depuis le cadre.
2. Le décideur ne peut pas estimer $z$. Il peut seulement ajouter une « marge d'humilité » $b$, qui relève du jugement, et ne s'engager que si $p + b < p^\ast$. Le croisement donne quatre issues : départ justifié, piège silencieux, sauvé par la marge (ou renoncement justifié), prudence superflue.
3. On calibre les décisions qui se répètent dans un environnement stable. Pour une décision unique et irréversible, il faut en plus un « verrou », c'est-à-dire une autorisation donnée par un comparateur indépendant avant d'agir.
4. On explore librement dans un « bac à sable », où la réponse du monde est bon marché et réversible. On réserve les verrous aux frontières de coût et d'irréversibilité, sans les multiplier.
5. Devant un chiffre assuré, le destinataire pose quatre questions : conditions, sensibilité, manière la plus probable d'être faux, ce qui n'a pas été modélisé. Pour un système automatisé, il les adresse à l'institution qui le déploie.

## 2. Constats classés par gravité

### Gravité A (compréhension compromise ou contresens possible)

**A1. Exemple quantitatif, « Lecture », 4e puce.**
Passage : « *Plus les enjeux sont lourds, plus la marge nécessaire est mince.* »
Problème : lue seule, la phrase semble recommander moins de prudence quand les enjeux augmentent. Cela contredit en apparence le § « Comment fixer $b$ », où le jugement « doit peser d'autant plus lourd que les enjeux sont élevés ». Le sens visé est sans doute « la marge qui suffit à renverser la décision », mais la formule permet le contresens.
Proposition : « Plus les enjeux sont lourds, plus la marge qui suffit à renverser la décision est mince. » Le sens ne bouge pas si c'est bien la lecture visée.

### Gravité B (gêne réelle)

**B1. La course à la voile revisitée, § 2.**
Passage : « le contact avec le monde a fait entrer dans la représentation un facteur qui n'y figurait pas, et il est survenu avant l'acte »
Problème : « il » peut renvoyer à « le facteur » (l'antécédent le plus proche) ou à « le contact avec le monde ». Les deux lectures sont plausibles.
Proposition : « …, et ce contact est survenu avant l'acte » (ou « et cette découverte… »). À trancher par l'auteur.

**B2. La course à la voile revisitée, § « Comment fixer $b$ ».**
Passage : « moins d'un centième de point pour le joueur de roulette russe »
Problème : le joueur de roulette russe n'a pas encore été présenté dans le chapitre. Il n'apparaît que dans l'exemple quantitatif, plus loin. C'est une possible dépendance au chapitre 4.
Proposition : « pour le joueur de roulette russe du @sec:ch04 (seuil d'environ 0,01 %) ».

**B3. Même paragraphe.**
Passage : « Ce jugement doit peser d'autant plus lourd que les enjeux sont élevés »
Problème : deux lectures sont possibles : (a) la marge choisie doit être plus grande ; (b) ce jugement doit compter davantage dans la décision. Combiné à A1, cela brouille la consigne.
Proposition : « Ce jugement doit être d'autant plus exigeant que… ». Je ne tranche pas entre (a) et (b).

**B4. Liste des quatre issues (texte) et partition (bloc formel).**
Passage : « on obtient quatre issues » puis, dans l'item 3 : « Lorsque $p \ge p^\ast$ dès le départ, comme pour M. X, on parlera simplement de *renoncement justifié*. »
Problème : on annonce quatre issues, mais il y a cinq étiquettes. La cinquième est glissée dans l'item 3, alors qu'elle ne remplit pas sa condition ($p < p^\ast$). Le lecteur ne sait plus combien de cas il y a, ni où se range M. X.
Proposition : sortir la phrase de l'item 3 et la placer après la liste : « Le troisième quadrant comprend aussi le cas où $p \ge p^\ast$ dès l'origine, comme pour M. X : on parlera alors de *renoncement justifié*. »

**B5. Bloc formel M2, hypothèse 2, et encadré « Pourquoi le risque omis… ».**
Passages : « aucun désaccord dans l'ensemble des alternatives admises » ; « aucune décomposition de la variance sur l'ensemble des alternatives admises »
Problème : ce jargon n'est pas expliqué ici. Un lecteur non spécialiste ne voit pas ce que sont ces « alternatives » ni pourquoi la variance interviendrait. C'est une possible dépendance au chapitre 5.
Proposition : ajouter une glose au premier emploi, par exemple « (les variantes de modèle que le cadre juge acceptables) ». La glose est à valider par l'auteur, car le sens exact dépend du chapitre 5.

**B6. Encadré « Pourquoi le risque omis… », § 2.**
Passage : « ferait de l'incertitude ontologique du @sec:ch05 une troisième quantité mesurable »
Problème : « troisième » suppose deux premières quantités, qui ne sont pas nommées ici. C'est une possible dépendance.
Proposition : « … une troisième quantité mesurable, à côté des incertitudes [aléatoire et épistémique ?] du @sec:ch05 ». Les noms sont à confirmer : je ne les connais pas.

**B7. Même encadré, fin du § 2.**
Passage : « il figurerait déjà dans $p$ et dans $\Theta$ »
Problème : la notation $\Theta$ n'apparaît nulle part ailleurs dans le chapitre. C'est une possible dépendance.
Proposition : « … dans $p$ et dans les paramètres $\Theta$ du cadre ».

**B8. Calibrer ce qui se répète, § 2.**
Passage : la phrase « On peut alors s'appuyer sur une pratique statistique éprouvée, … à l'aide de règles de score strictement propres »
Problème : (a) la phrase est très longue et contient une énumération de quatre opérations. (b) Le mot « score » y prend deux sens : le score d'un classement (« quand le score reste ambigu ») et la règle de notation des prévisions. (c) « règles de score strictement propres » est un terme technique non expliqué.
Proposition : couper la phrase après « (@sec:ch03-calibration-historique) ». Écrire « quand le résultat de l'outil reste ambigu » pour le premier emploi. Gloser le terme technique : « règles de score strictement propres, qui récompensent la prévision honnête ».

**B9. Calibrer ce qui se répète, § « Devant une décision unique ».**
Passages : « au-delà de la frontière en dents de scie de l'outil » ; « d'examiner chaque alerte ($u = 1$) »
Problème : ni l'image de la frontière en dents de scie ni la notation $u$ ne sont expliquées. Ce sont des possibles dépendances aux chapitres 12 et 9. La notation $u$ surtout est opaque.
Proposition : « d'examiner chaque alerte, sans exception » (la notation peut aller en note, ou être glosée : « taux d'examen $u = 1$ »). Pour la frontière : « au-delà de la frontière irrégulière de ce que l'outil réussit ».

**B10. Calibrer ce qui se répète, § « Protéger une décision unique ».**
Passage : « un comparateur (@def:comparateur) capable de se tromper autrement (@prop:independance) »
Problème : la phrase est elliptique : autrement que qui ? Le lecteur doit reconstituer « autrement que le cadre ou le système qui a produit l'action ».
Proposition : « un comparateur capable de se tromper autrement que le système qui propose l'acte ».

**B11. Calibrer ce qui se répète, dernier §.**
Passage : « le verrou se lit à travers les cinq conditions du @sec:ch06 »
Problème : quatre conditions seulement sont nommées (arrivée à temps, différence, comparabilité, prise en compte). Le lecteur cherche la cinquième, et apprend seulement que l'arrivée à temps est « la quatrième ». C'est une possible dépendance.
Proposition : nommer la cinquième ou écrire « à travers les conditions du @sec:ch06 ».

**B12. Bacs à sable et verrous, liste des deux acquis.**
Passages : « une pertinence nouvelle n'entre dans un cadre que du dehors » ; « confier l'autorité d'agir à la couche qui offre le moins de garanties »
Problème : « pertinence nouvelle » et « la couche » sont des formules propres à des chapitres antérieurs. Hors contexte, elles restent opaques. Ce sont des possibles dépendances aux chapitres 7 et 14.
Proposition : « un facteur nouvellement pertinent n'entre dans un cadre que du dehors » ; « à la couche du système (le modèle qui génère les actions ?) qui offre… ». Le contenu de la glose est à confirmer.

**B13. Quatre questions, question 1.**
Passage : « La question fait réapparaître l'arrière-plan $(\dots)$ »
Problème : la notation « (…) » s'affiche comme des points de suspension entre parenthèses. Le lecteur ne sait pas s'il s'agit d'une notation ou d'un texte manquant.
Proposition : supprimer la notation ou la gloser : « l'arrière-plan (ce que le cadre tient pour acquis) ».

**B14. Quatre questions, § 2.**
Passage : « le blanchiment des chapitres [-@sec:ch08] et [-@sec:ch14] (@def:blanchiment) change de nature »
Problème : le terme « blanchiment » est essentiel à ce paragraphe, mais n'est pas rappelé. Il apparaît déjà plus haut sans glose. C'est une possible dépendance.
Proposition : « le blanchiment des chapitres 8 et 14, c'est-à-dire l'effacement des hypothèses et de la provenance d'un chiffre, change de nature ».

**B15. Quatre questions, § « Le bulletin de pluie ».**
Passage : « ce qui sépare un fait nu d'une information qui laisse au destinataire sa part de décision », puis « c'est une *injonction déguisée en information* »
Problème : l'annonce « il pleuvra demain » est d'abord qualifiée de « fait nu », puis d'« injonction déguisée en information ». Juste avant, le texte parlait de « transfert de responsabilité déguisé en information ». Trois formules désignent la même chose, et « fait nu » va même à l'encontre de l'idée d'injonction.
Proposition : « ce qui sépare une consigne présentée comme un fait d'une information qui laisse… ».

**B16. Points clés, puce 2.**
Passage : « elle protège une décision unique du piège silencieux »
Problème : dans le corps du texte, la protection est conditionnelle : « rien ne garantit qu'une marge donnée couvrira un défaut massif ». Le point clé la présente comme acquise.
Proposition : « elle peut protéger une décision unique du piège silencieux ».

**B17. Points clés, puce 3.**
Passage : « une décision unique et irréversible, qu'aucun taux passé ne protège, appelle en outre un verrou »
Problème : « en outre » laisse entendre « en plus de la calibration ». Or le corps du texte dit que la calibration ne s'applique pas aux décisions uniques, et que le verrou s'ajoute à la marge d'humilité (« deux dispositions »). Le passage permet le contresens.
Proposition : « appelle, en plus d'une marge d'humilité, un verrou ».

### Gravité C (confort, style)

**C1. La course à la voile revisitée, § 1.**
Passage : « Le seuil de l'@eq:ch04-seuil vaut donc $p^\ast = 1/26$ »
Problème : la formule du seuil et le sens de la comparaison (on part si $p < p^\ast$) ne sont donnés que plus loin, au § « Le décideur ne peut pas observer… » et dans le bloc formel. Le lecteur les déduit du comportement de M. X.
Proposition : « … vaut donc $p^\ast = 1/(1 + 25) = 1/26$, soit environ 3,85 % : on ne part que si la probabilité de casse est inférieure à ce seuil. »

**C2. La course à la voile revisitée, § 2.**
Passage : « exclut les mondes possibles où le mât est sain »
Problème : le vocabulaire des « mondes possibles » est technique (possible dépendance), alors qu'une formule simple suffit ici.
Proposition : aucune, si le terme est défini plus tôt dans l'ouvrage. Sinon : « exclut l'hypothèse d'un mât sain ».

**C3. La course à la voile revisitée, § 3.**
Passages : « manchon d'étambrai » ; « non la fiche technique »
Problème : « étambrai » est un terme de marine rare. « La fiche technique » arrive sans annonce et désigne sans doute la représentation.
Proposition : « sous le manchon qui entoure le pied du mât » ; « non la représentation qu'on s'en fait ».

**C4. Même §.**
Passage : « que nous appellerons le *risque réel* et noterons $p_w$ »
Problème : l'indice $w$ (world) n'est pas expliqué au lecteur francophone.
Proposition : « $p_w$ (w pour *world*, le monde) ».

**C5. § « Comment fixer $b$ ».**
Passage : « Raisonner à l'envers (…) offre seulement une prise »
Problème : « seulement » se lit d'abord comme « la seule prise », alors que le sens visé est sans doute « une prise, pas un calcul ».
Proposition : « Raisonner à l'envers offre tout au plus une prise ».

**C6. Liste des issues (item 3) et bloc formel.**
Passages : « dès le départ » / « dès l'origine »
Problème : dans un passage sur une course, « dès le départ » prête à confusion avec le départ de la course. Le bloc formel, lui, dit « dès l'origine ».
Proposition : « dès l'origine » dans les deux cas.

**C7. Bloc formel M2.**
Passage : « la règle de Savage [@savage1954] »
Problème : on rencontre ce nom pour la première fois dans le chapitre, sans qu'il soit dit qu'il s'agit de la règle de l'utilité espérée subjective. Le lien n'est fait que dans l'encadré suivant.
Proposition : « la règle de Savage (utilité espérée subjective) ».

**C8. Légende de la figure.**
Passage : « Les droites d'équation $1$ séparent les quatre quadrants »
Problème : « équation 1 » ne désigne pas une droite.
Proposition : « Les droites $(p + b)/p^\ast = 1$ et $p_w/p^\ast = 1$ séparent… ».

**C9. Exemple quantitatif, § « Avec une marge de 4 % ».**
Passage : « la chambre chargée ($1/6 \approx 16{,}7\,\%$) porte le risque réel à 16,7 % »
Problème : la phrase attribue une probabilité à « la chambre chargée ». Le sens est que la chambre chargée a une chance sur six de se trouver face au percuteur.
Proposition : « la chambre chargée, qui a une chance sur six de se trouver face au percuteur, porte le risque réel à 16,7 % ».

**C10. Lecture, 4e puce, fin.**
Passage : « Le joueur ne tombe dans le piège silencieux que parce qu'il n'en prend aucune ; aucune marge, en revanche, ne lui aurait appris… »
Problème : la répétition d'« aucune » fait trébucher. On peut même lire un instant « l'absence de marge ».
Proposition : « … ; mais aucune marge, si grande soit-elle, ne lui aurait appris… ».

**C11. Transition après l'exemple.**
Passage : « Le tableau ravive une tentation »
Problème : il y a deux tableaux et une figure, et le lecteur ne sait pas lequel est visé.
Proposition : « Le @tbl:ch17-decisions ravive… » ou « Cet exemple ravive… ».

**C12. Calibrer ce qui se répète, § « La répétition sert aussi… ».**
Passage : « et presque pas du tout lorsqu'elle est l'issue attendue »
Problème : on ne sait pas qui attendait cette issue (les deux prévisions ? l'une d'elles ?).
Proposition : « lorsque les deux prévisions la jugeaient probable ». Cette proposition suppose une interprétation que je ne peux pas vérifier.

**C13. Calibrer ce qui se répète, § 1.**
Passage : « *calibrer ce qui se répète ; verrouiller ce qui ne se joue qu'une fois* »
Problème : « verrouiller » est employé comme mot d'ordre treize lignes avant la définition du verrou. C'est gérable, mais le lecteur reste en attente.
Proposition : ajouter « (le verrou est défini plus bas) », ou rien.

**C14. Définition du bac à sable.**
Passage : « un environnement isolé où les actions n'ont aucun effet extérieur, et où l'on peut donc interroger le monde à peu de frais »
Problème : il y a un léger paradoxe : on « interroge le monde » dans un lieu sans effet sur le monde.
Proposition : « … où l'on peut donc mettre sa représentation à l'épreuve à peu de frais ». Le sens bouge légèrement : à l'auteur de juger.

**C15. Bacs à sable et verrous, 1re limite.**
Passage : « l'automate dont les capteurs ignorent la couleur des fils »
Problème : l'exemple vient d'un chapitre antérieur et reste incompréhensible ici. C'est une possible dépendance.
Proposition : « l'automate (@sec:ch07) dont les capteurs… ».

**C16. Bacs à sable et verrous, 2e limite.**
Passage : « ces demandes sont presque toutes sans danger »
Problème : ce sont les opérations qui sont sans danger, pas les demandes.
Proposition : « ces demandes portent presque toutes sur des opérations sans danger ».

**C17. Quatre questions, § « Poser ces questions… ».**
Passages : « d'une attitude, des deux côtés » ; « Le @sec:ch12 … l'a montré »
Problème : seul le côté du destinataire est décrit explicitement, puis « chacun ». Le pronom « l' » annonce une idée qui vient seulement après les deux-points.
Proposition : « … et celui qui le produit, comme celui qui le reçoit, doit accepter… ».

**C18. Quatre questions, § « Lorsque le chiffre… ».**
Passages : « réparti qu'il est entre les données d'entraînement » ; « l'orientation du modèle »
Problème : « il » peut renvoyer à « le cadre » ou à « l'expert ». Le sens logique est « le cadre ». « Orientation du modèle » ressemble à un calque (alignment, steering ?) et reste vague.
Proposition : « … qui aurait arrêté le cadre : celui-ci est réparti entre… ». Pour « orientation », préciser le terme technique visé.

**C19. Points clés, puce 1.**
Passage : « qu'aucune règle interne ne sait lire »
Problème : le corps du texte dit « aucun contrôle interne ne peut le lire ». Or « règle » renvoie ailleurs à la règle de décision : le flottement terminologique gêne.
Proposition : « qu'aucun contrôle interne ne sait lire ».

**C20. Exemple quantitatif, § « Avec une marge de 4 % » (typographie).**
Passages : « (*Prudence superflue*) », « Dans la *Roulette russe*, enfin »
Problème : la majuscule en milieu de phrase se justifie comme nom de ligne de tableau, mais elle alterne avec « la roulette russe » en minuscules ailleurs.
Proposition : « dans le scénario *Roulette russe* », ou bien des minuscules partout.

## 3. Appréciation globale

Le chapitre se lit bien et suit une progression claire : modèle, pratiques de calibration et de verrou, architecture, destinataire. Les sections les plus accessibles sont la mise en situation de la course à la voile (hors le point B4), l'exemple quantitatif, dont les calculs en texte sont justes et faciles à suivre, et la section « Recevoir un chiffre assuré », avec un exemple du bulletin de pluie très parlant. Les passages les moins accessibles sont l'encadré « Pourquoi le risque omis… » et la fin de « Calibrer ce qui se répète » (§ « Devant une décision unique » et dernier §). Ils concentrent les renvois à des notions non rappelées : alternatives admises, décomposition de la variance, $\Theta$, « troisième quantité », $u = 1$, frontière en dents de scie, cinq conditions, blanchiment. Un lecteur qui n'a pas les chapitres 5 à 9 en tête y perd pied. Le risque principal de contresens tient à la formule sur la marge « mince » quand les enjeux sont lourds (A1), aggravée par l'ambiguïté de B3.
