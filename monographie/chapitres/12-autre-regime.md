# Au sommet de la pile, un autre régime {#sec:ch12}

Le @sec:ch10 a montré pourquoi les couches basses et médianes de l’informatique classique peuvent être oubliées une fois vérifiées : des composants spécifiés (@def:composant-specifie) y promettent un comportement par contrat écrit, autorisent une vérification en amont et donnent aux défaillances une adresse. Le @sec:ch11 a décrit ce qui change lorsqu’un composant appris (@def:composant-appris) tire sa règle des données : la portée s’achète au prix de la garantie, la plausibilité devient l’objectif d’entraînement et l’orientation remplace la spécification. Ce chapitre examine ce qui advient au sommet de la pile logicielle, lorsque ces composants appris deviennent des modèles de langage généralistes appelés dans des contextes ouverts : trois propriétés basculent ensemble, déplaçant le contrôle vers chaque sortie individuelle, révélant une compétence en dents de scie et obligeant — à la lumière de la calibration (@sec:ch03-calibration-historique), du cadre comme cause commune (@sec:ch07, @prop:cause-commune) et du critère de sévérité (@sec:ch09, @def:severite) — à distinguer les erreurs que la répétition d’une question décèle de celles qu’elle laisse passer.

## Trois propriétés basculent ensemble {#sec:ch12-trois-bascules}

Passer d’un appel à une base de données relationnelle ou à une routine de tri à l’appel d’un grand modèle de langage ne modifie pas un seul aspect de l’édifice technique. D’un même coup, ce que le composant promet, le visage que prend son échec et l’endroit où aboutit l’enquête après coup se retournent. On désigne par **changement de régime** ce basculement simultané, au sommet de la pile, de ce qui est promis, de la forme de l’échec et de ce que trouve l’enquête.

Trois renversements définissent ce passage :

1. *Ce qui est promis.* Dans les couches spécifiées (@sec:ch10), un composant s’engage par un contrat explicite — préconditions exigées à l’entrée et postconditions garanties en sortie — que l’on peut confronter à un énoncé écrit. Au sommet de la pile, un modèle appris (@sec:ch11) ne promet qu’une tendance statistique : on mesure une fréquence de succès en moyenne sur un test de référence, sans qu’aucune statistique de série ne garantisse la réponse particulière qui vient d’être émise.
2. *La forme de l’échec.* En dessous, une erreur se présente comme une divergence définissable par rapport à une règle écrite : arrêt d’exécution, violation de type, échec d’un test unitaire ou contradiction entre deux représentations d’une même grandeur. Au sommet, parce que l’entraînement privilégie la plausibilité (@sec:ch11), une affirmation fausse revêt la même prose claire, structurée et assurée qu’une réponse exacte ; à la seule lecture de l’énoncé produit, rien ne distingue l’échec de la réussite.
3. *Le lieu où atterrit l’enquête.* En dessous, remonter une défaillance conduit à une adresse : un module, une ligne de programme ou une interface dont la spécification a été enfreinte, et où un correctif précis peut être rédigé et contrôlé. Au sommet, l’enquête débouche sur une distribution d’exemples d’entraînement, des milliards de paramètres ajustés et une fonction objectif : il n’existe aucune ligne fautive à modifier, car on ne fusionne pas un correctif local dans une distribution de probabilité.

Il importe de bien situer la ligne de partage entre ces deux régimes. Constater ce basculement ne revient pas à soutenir qu’un modèle appris échoue plus souvent qu’un programme classique écrit par des humains. Sur de nombreuses tâches — résumer un long dossier, extraire des éléments d’un texte hétérogène, traduire un document technique —, un modèle contemporain commet souvent moins d’erreurs qu’un programme rigide ou qu’un opérateur pressé. La fréquence des fautes n’est pas l’axe du changement de régime. L’axe décisif est de savoir si une erreur est définissable par rapport à un énoncé préalable, et si un contrôle peut être exercé une fois pour toutes avant l’usage. Comme l’a établi le @sec:ch09, un producteur dont le taux d’erreur diminue mais dont les erreurs échappent aux contrôles peut encore former un système plus risqué qu’un producteur moins exact mais mieux contenu.

De plus, opposer une « divergence définissable » dans les couches classiques à une erreur fluide au sommet ne doit pas conduire à idéaliser les logiciels traditionnels : une erreur parfaitement définissable peut demeurer longtemps inaperçue.

::: {.nuance titre="Définissable ne signifie pas bruyant"}
Dire que, dans les couches classiques, l’échec prend la forme d’une divergence définissable ne veut en aucun cas dire que les programmes traditionnels crient dès qu’ils se trompent. L’informatique classique produit en abondance des erreurs qui passent inaperçues pendant des semaines ou des mois, faute de comparateur actif en exploitation.

L’accident de *Mars Climate Orbiter*, examiné au @sec:ch08 et au @sec:ch10, en fournit un exemple net [@mco1999]. Tout au long du transit vers Mars, le programme au sol `SM_FORCES` a calculé des poussées de correction en livres-force-secondes ($\text{lbf}\cdot\text{s}$) alors que la spécification d’interface exigeait des newton-secondes ($\text{N}\cdot\text{s}$), introduisant un écart d’un facteur proche de $4{,}45$. Aucune alarme décisive n’a interrompu la mission avant la perte de la sonde, le 23 septembre 1999 [@mco1999]. Ce qui sépare néanmoins ce cas du sommet de la pile tient au fait que la faute demeurait *définissable* : il existait un contrat d’interface écrit, et un comparateur mécanique vérifiant les unités aurait pu être écrit et appliqué une fois pour toutes au composant ou à l’interface. Pour un composant appris généraliste, de tels comparateurs ne peuvent exister que tâche par tâche et sortie par sortie.
:::

## Vérifier la couche ou contrôler les sorties {#sec:ch12-couche-sorties}

Les composants statistiques dépourvus de contrat complet ne datent pas d’hier. Les filtres antipourriels, les moteurs de classement documentaire et les systèmes de recommandation reposent depuis longtemps sur des règles ajustées à partir d’exemples. Mais ces outils restaient cantonnés à un produit fermé et à une tâche unique : on connaissait d’avance le type d’entrée qu’ils recevaient, le format de leur sortie et l’impact borné de chaque erreur isolée.

La nouveauté propre au sommet de la pile tient à la nature *compositionnelle* d’un grand modèle de langage généraliste. Par une simple interface textuelle, n’importe quel logiciel peut l’invoquer sur des tâches imprévues lors de l’entraînement — rédiger un avis juridique, traduire une consigne métier en requête informatique, analyser un dossier client, proposer une modification de code — puis transmettre la réponse obtenue à d’autres maillons de la chaîne de traitement. La même couche apprise irrigue aussitôt des usages hétérogènes, là où chaque couche classique jouait un rôle étroitement délimité.

Dans l’architecture classique (@sec:ch10), cette réutilisation universelle était rendue sûre par la vérification en amont : on contrôle une routine de tri une seule fois, en confrontant son code à sa spécification, et l’acquis vaut ensuite pour toutes les listes qu’on lui confiera à l’avenir. Au sommet de la pile, faute de spécification générale énonçable du comportement du modèle sur l’ensemble des tâches qu’on lui soumettra, ce geste disparaît. Ni le test de référence passé sur un jeu d’épreuves public (@sec:ch11), ni la relecture des consignes générales ne certifient la réponse particulière produite sur le dossier du jour.

Le contrôle change donc nécessairement d’échelle et de point d’application, selon deux directions complémentaires qui structureront les chapitres suivants :

- *Rebâtir un contrôle mécanique autour de la tâche*, chaque fois que la nature de cette tâche admet un comparateur mécanique indépendant du modèle. Si l’on demande à un modèle de produire un programme informatique soumis ensuite à un compilateur et à une suite de tests écrite à part, une preuve formelle contrôlée par un noyau logique, ou un objet structuré confronté à un schéma strict, l’incertitude de la génération reste enfermée dans la proposition de candidat : seule survit une sortie qui a franchi un comparateur mécanique. Le @sec:ch13 dressera l’inventaire complet des sources de comparateurs disponibles autour des composants appris.
- *Contrôler les sorties une à une*, partout où la tâche ne possède aucun comparateur mécanique suffisant — analyse documentaire, rédaction experte, synthèse de décision, conseil technique. Le contrôle doit alors quitter la couche logicielle pour s’appliquer à chaque réponse prise individuellement, après qu’elle a été produite et avant qu’elle n’entre dans un dispositif qui exécute, facture, engage ou publie. Le @sec:ch18 examinera comment placer ces contrôles sur les points de passage critiques.

Tant que ce déplacement n’est pas opéré — c’est-à-dire tant qu’un système en aval consomme la sortie d’un modèle comme une chaîne de caractères fiable, à la manière d’un résultat issu d’une couche spécifiée —, la chaîne entière (@sec:ch08) hérite d’un angle mort qui n’existait pas au même degré dans les couches inférieures : l’interface demeure aussi lisse, mais la garantie qui la soutenait en dessous s’est retirée.

## La frontière en dents de scie {#sec:ch12-frontiere-dents-scie}

Si les garanties globales s’effacent, on pourrait espérer se repérer par l’expérience : apprendre, à force de pratique, quelles tâches « faciles » le modèle maîtrise à coup sûr et quelles tâches « difficiles » il vaut mieux garder à l’écart. Cet espoir se heurte à un trait propre aux composants appris à grande échelle : leur compétence ne suit pas l’échelle humaine de la difficulté. Parce que le modèle accumule des régularités statistiques là où ses données d’entraînement et son objectif de prédiction le lui ont permis (@sec:ch11), ses réussites et ses échecs dessinent un relief déroutant. On appelle **frontière en dents de scie** cette limite irrégulière, difficile à prévoir et mouvante de la compétence d’un modèle.

Une expérience de terrain menée dans une firme de conseil illustre de façon frappante ce qui se produit lorsque des spécialistes franchissent sans le voir l’une de ces dents de scie.

::: {.cas titre="L’expérience de terrain au Boston Consulting Group : juste hors de la frontière" date="2023"}
En 2023, Fabrizio Dell’Acqua et ses coauteurs ont mené une expérience contrôlée auprès de 758 consultants du Boston Consulting Group afin de mesurer l’effet de l’assistance par un grand modèle de langage (GPT-4) sur des tâches réalistes de conseil [@dellacqua2023]. Comme l’a montré le @sec:ch11, sur les tâches situées à l’intérieur de la zone de compétence du modèle, les gains de productivité et de qualité étaient nets.

Les chercheurs avaient toutefois conçu une autre tâche réaliste destinée à se situer *juste au-delà* de la limite de compétence de GPT-4, tout en conservant exactement la même apparence de travail courant. Sur cette tâche hors frontière, les consultants assistés par le modèle ont eu 19 points de pourcentage de moins de chances de parvenir à une solution correcte que ceux qui travaillaient sans aide algorithmique [@dellacqua2023].

L’analyse met en évidence le mécanisme de cette dégradation : l’outil produisait des réponses tout aussi fluides, structurées et convaincantes de part et d’autre de la limite. Faute de marque visible signalant le franchissement de la frontière, une partie des utilisateurs a relâché ses propres contrôles et repris à son compte un raisonnement erroné [@dellacqua2023].
:::

Trois caractéristiques rendent cette frontière en dents de scie particulièrement piégeuse dans la pratique, indépendamment de telle génération d’outils ou de telle version particulière de modèle :

- *L’irrégularité locale.* Un modèle peut réussir un exercice complexe de synthèse ou de programmation et échouer sur une tâche voisine qui paraît plus simple, ou sur le même problème formulé sous un angle légèrement différent. La réussite sur un cas proche ne fonde aucune certitude sur le cas adjacent.
- *La mobilité entre versions.* Chaque mise à jour des paramètres, chaque changement d’alignement ou d’outillage déplace les pointes et les creux de la frontière. Une tâche fiable hier peut basculer hors compétence après une modification mineure de la consigne système ou du modèle sous-jacent, sans avertissement.
- *L’indiscernabilité depuis l’intérieur.* Vue de l’interface conversationnelle, une réponse émise de chaque côté de la frontière garde la même aisance de ton. Aucune alarme interne n’informe l’utilisateur ou le programme appelant que la requête vient de tomber dans un creux de compétence.

La conséquence pratique est immédiate : savoir où passe la frontière pour *vos* tâches réelles ne se lit pas sur un classement général ni sur un test de référence public (@sec:ch11). Cartographier cette limite constitue une tâche continue d’exploitation, qu’il faut recommencer à mesure que les cas d’usage évoluent et que les modèles changent.

Cette sensibilité déroutante aux détails du contexte éclaire aussi un lien profond avec la théorie du cadre développée au @sec:ch07. Lorsqu’un modèle échoue sur une question dont les ingrédients figurent pourtant dans ses textes d’entraînement, ou même dans la consigne qui lui est soumise, la nature de l’omission n’est pas toujours la même. Il convient de distinguer deux mécanismes :

- On parle d’**omission structurelle** lorsqu’un facteur pertinent est absent de la représentation elle-même : par exemple un fait postérieur à la date d’arrêt des données d’entraînement, une donnée confidentielle absente du contexte fourni, ou une grandeur physique non enregistrée dans le cadre.
- On parle d’**omission de saillance** lorsqu’un facteur pertinent est bien représenté — inscrit dans les paramètres du modèle ou même présent dans le texte de la consigne —, mais n’est pas mobilisé pour répondre à la question posée. Parce que cette mobilisation dépend fortement de la formulation, de l’ordre des éléments et des indices saillants dans l’énoncé, deux questions presque équivalentes peuvent solliciter des régions différentes de la représentation, contribuant directement à dessiner une frontière en dents de scie.

Cette distinction affine directement l’un des piliers de la deuxième partie de l’ouvrage, la @prop:cause-commune (@sec:ch07), et renoue avec l’origine historique du problème du cadre rappelée à la @sec:ch02-probleme-cadre.

::: {.nuance titre="Omission structurelle, omission de saillance et cadre comme cause commune"}
On pourrait objecter à la @prop:cause-commune (@sec:ch07) qu’un grand modèle de langage entraîné sur une part immense des écrits disponibles ne « manque » presque jamais d’une variable au sens où un modèle mécanique omet la corrosion saline : presque tous les concepts usuels apparaissent quelque part dans ses données d’entraînement, et les données du dossier figurent souvent dans la consigne elle-même.

En réalité, dès la naissance du problème du cadre en intelligence artificielle (@sec:ch02-probleme-cadre), John McCarthy et Patrick Hayes [@mccarthy1969] puis Daniel Dennett [@dennett1984] montraient que la difficulté ne porte pas uniquement sur ce qui manque dans la liste des faits, mais sur la *pertinence* de faits déjà représentés. Dans l’apologue de Dennett, le premier robot représentait parfaitement que la bombe reposait sur le chariot ; il n’a tout simplement pas mobilisé cette relation au moment de tirer le chariot hors de la pièce [@dennett1984].

Distinguer omission structurelle et omission de saillance précise exactement le champ d’application du volet (a) de la @prop:cause-commune :

- devant une *omission structurelle* (le facteur est absent de la représentation), la fermeture établie au @sec:ch07 tient strictement : aucun comparateur calculé sur cette seule représentation ne peut révéler l’effet du facteur manquant ;
- devant une *omission de saillance* (le facteur est représenté mais non mobilisé), le volet (a) de la @prop:cause-commune ne tient que pour les contrôles qui réutilisent les mêmes paramètres ajustés et la même formulation de la consigne — confirmant ainsi la nuance annoncée au @sec:ch07. Reformuler la question, décomposer le problème ou interroger un autre cheminement peut parfois faire émerger une relation qui dormait dans la représentation sans agir. Mais rien, dans la formulation initiale prise seule, ne garantit qu’on saura deviner quelle reformulation la réveillera.
:::

## Calibration générative, longue traîne et erreurs constantes {#sec:ch12-calibration-longue-traine}

Une deuxième famille d’échecs au sommet de la pile ne tient ni à la formulation d’une consigne ni à la complexité d’un raisonnement, mais à la statistique même de la génération sur des faits rares et arbitraires — dates de naissance, cotes d’archives, numéros de référence, citations juridiques — que nulle règle générale ne permet de déduire. Pourquoi un modèle bien entraîné sur des textes exacts continue-t-il d’inventer de tels faits avec aisance ? Et dans quels cas suffit-il de lui reposer la question pour le prendre en défaut ?

Pour répondre, il faut introduire le second sens du mot *calibration* annoncé à la @sec:ch03-calibration-historique. Alors que la calibration examinée au @sec:ch03 porte sur l’accord entre les probabilités annoncées et les fréquences observées, on appelle **calibration générative** l’accord entre la distribution des énoncés produits par un modèle et la distribution de ses données d’entraînement ; loin de prémunir contre l’invention, cette propriété entraîne mécaniquement la fabrication de faits rares.

Le mécanisme, démontré par Adam Tauman Kalai et Santosh Vempala [@kalai2024], tient à une propriété élémentaire des distributions à longue traîne. Considérons des faits *arbitraires*, c’est-à-dire des associations qu’aucune régularité grammaticale, logique ou causale ne permet de reconstruire à partir du contexte — par exemple la date de naissance exacte d’une personne peu connue ou l’intitulé d’un arrêt introuvable par déduction. Dans un corpus réel, une proportion importante de ces faits n’apparaît qu’une seule fois : ce sont des *singletons* (ou *monofacts*). Par un raisonnement statistique apparenté à l’estimation de Good-Turing, si le modèle reproduit fidèlement la distribution statistique des énoncés du corpus, il ne peut distinguer un fait vrai aperçu une seule fois d’une multitude d’énoncés plausibles mais faux qui n’apparaissent pas dans les données. Pour rester générativement calibré, il doit donc répartir sa probabilité sur l’ensemble des complétions plausibles — et engendrer des énoncés faux à un taux voisin de la proportion de singletons [@kalai2024]. L’encadré suivant précise l’allure de cette borne.

::: {.formel titre="La borne de Kalai et Vempala sur les faits arbitraires"}
Soit une classe de faits arbitraires qu’aucune régularité générale ne permet de prédire à partir des énoncés voisins. Kalai et Vempala ont établi une borne inférieure reliant la fréquence des inventions (hallucinations) d’un modèle de langage à la structure de longue traîne de ses données d’entraînement [@kalai2024]. Sous les hypothèses de leur analyse statistique, la relation s’exprime schématiquement par :

$$\begin{aligned}
\text{taux d’hallucination} \;\gtrsim\; \text{taux de singletons} &- \text{défaut de calibration générative} \\
&- \text{termes mineurs}.
\end{aligned}$$ {#eq:ch12-kalai-vempala}

Dans cette inégalité :

- le *taux de singletons* désigne la proportion des faits arbitraires de la classe considérée qui ne figurent qu’une seule fois dans le corpus d’entraînement ;
- le *défaut de calibration générative* mesure l’écart entre la distribution des énoncés émis par le modèle et celle des données d’entraînement ;
- les *termes mineurs* regroupent des corrections statistiques d’ordre inférieur propres au cadre formel de la démonstration.

Le sens de la borne est limpide : plus un modèle approche une calibration générative exacte sur une longue traîne de faits arbitraires dominée par des singletons, plus il est contraint de fabriquer des réponses fausses. Pour abaisser ce taux d’invention en deçà du taux de singletons, le modèle doit délibérément *s’écarter* de la calibration générative — notamment en s’abstenant de répondre (« je ne sais pas ») lorsque l’information lui fait défaut [@kalai2024; @kalai2025].
:::

Pourquoi l’ajustement postérieur à l’entraînement — qui vise justement à orienter le modèle (@sec:ch11) — ne suffit-il pas, dans la pratique courante, à remplacer ces inventions par un simple « je ne sais pas » ? Dans une analyse complémentaire, Adam Tauman Kalai, Ofir Nachum, Santosh Vempala et Edwin Zhang identifient un ressort institutionnel logé dans les protocoles d’évaluation eux-mêmes [@kalai2025] : la plupart des tests de référence notent l’abstention (« je ne sais pas ») comme une mauvaise réponse — zéro point —, tout en récompensant une devinette tombée juste par hasard. Dès lors que les modèles sont optimisés ou sélectionnés selon de tels barèmes, tenter une réponse plausible rapporte en moyenne davantage que reconnaître son ignorance. Les procédures d’évaluation sélectionnent ainsi activement la devinette assurée au détriment de l’abstention.

Il en résulte un contraste décisif entre deux régimes d’erreur dès que l’on tente de contrôler un modèle à moindre coût en lui *reposant plusieurs fois la même question* :

- *Les erreurs de devinette (dispersion).* Lorsqu’un modèle ignore un fait arbitraire et devine sous contrainte de plausibilité, sa probabilité se disperse entre plusieurs réponses concurrentes. Si l’on sollicite plusieurs tirages indépendants (avec une température d’échantillonnage non nulle), les réponses varient : une date puis une autre, un numéro de référence puis un autre. La dispersion entre tirages signale alors l’incertitude. Sebastian Farquhar, Jannik Kossen, Lorenz Kuhn et Yarin Gal ont montré comment mesurer cette dispersion de façon rigoureuse par l’*entropie sémantique* — en regroupant les réponses par équivalence de sens avant d’en calculer l’entropie — afin de détecter ce type de confabulation [@farquhar2024].
- *Les erreurs constantes (répétition).* Lorsqu’une erreur provient d’une idée reçue très fréquente dans le corpus d’entraînement, ou lorsque l’ajustement postérieur concentre presque toute la probabilité sur une unique réponse erronée, le modèle produit de façon cohérente la même affirmation fausse à chaque tirage. Reposer la question ne fait naître aucun désaccord : le contrôle par répétition reste aveugle aux erreurs constantes [@farquhar2024].

Au regard du critère de sévérité (@def:severite, @sec:ch09), la différence entre ces deux régimes est nette : demander plusieurs fois au modèle de répondre ne constitue un contrôle sévère que si ses erreurs entraînent effectivement une divergence entre tirages. L’exemple quantitatif suivant chiffre cet écart sur trois questions types.

::: {.exemple-quantitatif titre="Trois régimes de plausibilité : quand reposer la question révèle ou échoue (illustratif)"}
**Mise en place.** Les distributions ci-dessous sont purement illustratives : elles sont choisies pour isoler le mécanisme d’un contrôle par répétition, non pour estimer les paramètres d’un modèle réel. On compare trois questions pour lesquelles on tire 5 réponses indépendantes (la réponse initiale suivie de quatre répétitions dans les mêmes conditions) :

1. *Fait bien connu* (« Dans quelle ville se trouve la tour Eiffel ? ») : le modèle place 97 % de sa masse de probabilité sur la bonne réponse (Paris), 2 % sur Lyon et 1 % sur Marseille.
2. *Fait rare et arbitraire* (« Quand est née une personne obscure, mentionnée une seule fois dans le corpus ? ») : ne sachant pas retrouver la date, le modèle disperse sa probabilité sur six dates plausibles : 22 % sur le 14 mai, 20 % sur le 3 août, 18 % sur la seule date exacte (le 22 novembre), 16 % sur le 9 janvier, 14 % sur le 17 octobre et 10 % sur une autre date.
3. *Idée reçue répandue* (« Quelle planète est, en moyenne, la plus proche de la Terre ? ») : piégé par une confusion fréquente dans les textes, le modèle attribue 88 % de sa probabilité à Vénus (réponse fausse), seulement 9 % à Mercure (la bonne réponse en moyenne sur l’orbite) et 3 % à Mars.

On applique la règle de contrôle suivante : une alerte est levée si les 5 réponses divergent (c’est-à-dire si elles ne sont pas toutes identiques) ; si les 5 réponses concordent, aucune alerte n’est émise. Conformément à la @def:severite (@sec:ch09), la *sévérité* du contrôle est ici la probabilité que les 5 tirages divergent sachant que la première réponse est fausse ; le taux d’*alerte à tort* est la probabilité qu’ils divergent sachant que la première réponse était juste.

![Distributions illustratives des réponses pour trois types de questions (fait bien connu, fait rare et arbitraire, idée reçue répandue), avec mise en évidence de la réponse juste, sévérité d’un contrôle par 5 tirages et taux d’alerte sur bonne réponse.](figures/ch12-plausibilite.pdf){#fig:ch12-plausibilite width=90%}

**Calcul.** Le @tbl:ch12-plausibilite présente les taux d’erreur d’une réponse isolée, la sévérité et le taux d’alerte à tort pour chaque régime.

::: {.inclure fichier="tableaux/ch12-plausibilite.md"}
:::

Dans le premier cas (*Fait bien connu*), la première réponse est fausse dans 3 % des cas (2 % Lyon et 1 % Marseille). Lorsqu’elle est fausse, la probabilité que les quatre tirages suivants reproduisent exactement la même erreur est minuscule, si bien que la sévérité dépasse 99,9 %. Lorsqu’elle est juste (Paris, 97 %), la probabilité qu’au moins un des quatre autres tirages s’écarte de Paris vaut $1 - 0{,}97^4 \approx 11{,}5\,\%$ : même sur un fait très bien connu, le contrôle déclenche une alerte à tort dans 11,5 % des cas.

Dans le deuxième cas (*Fait rare et arbitraire*), la première réponse est fausse dans 82 % des cas. Lorsque la première réponse est fausse, l’étalement entre la date à 22 %, celle à 20 %, celle à 16 %, celle à 14 % et une autre date à 10 % rend presque impossible que les 5 tirages convergent sur la même erreur : la sévérité atteint 99,9 %. Mais lorsque la première réponse tombe juste (le 22 novembre, 18 %), les quatre autres tirages s’en écartent presque toujours ($1 - 0{,}18^4 \approx 99{,}9\,\%$) : le taux d’alerte à tort atteint lui aussi 99,9 %.

Dans le troisième cas (*Idée reçue répandue*), la première réponse est fausse dans 91 % des cas (88 % Vénus et 3 % Mars). Conditionnellement au fait qu’elle soit fausse, elle vaut presque toujours Vénus, si bien que les 5 tirages répètent tous Vénus près de six fois sur dix : la sévérité tombe à $1 - (0{,}88^5 + 0{,}03^5)/0{,}91 \approx 42{,}0\,\%$. En revanche, les rares fois où le premier tirage donne la bonne réponse (Mercure, 9 %), les tirages suivants rejoignent Vénus et le contrôle lève une alerte à tort dans plus de 99,9 % des cas ($1 - 0{,}09^4$).

**Lecture.** Le @tbl:ch12-plausibilite et la @fig:ch12-plausibilite dégagent trois enseignements nets :

- *La répétition attrape efficacement la devinette.* Sur le fait rare et arbitraire, où une réponse unique a 82 % de chances d’être fausse, reposer la question 5 fois offre une sévérité de 99,9 % : la dispersion trahit l’ignorance du modèle.
- *La répétition échoue devant l’erreur constante.* Sur l’idée reçue, pourtant encore plus souvent fausse au premier tirage (91 %), la sévérité chute à 42,0 % : plus de la moitié des erreurs traversent les 5 tirages à l’unanimité sans déclencher aucune alerte.
- *La dispersion mesure l’hésitation entre tirages, jamais la vérité.* Même quand la première réponse était exacte, l’incertitude du modèle provoque 11,5 % d’alertes à tort sur le fait bien connu, 99,9 % sur le fait arbitraire et plus de 99,9 % lorsque le hasard a fait surgir la bonne réponse contre l’idée reçue.

Cet exemple ne chiffre pas le coût de traitement des alertes (étudié au @sec:ch09), ni l’effet d’une reformulation de la consigne. Il repose sur l’hypothèse de 5 tirages indépendants à température d’échantillonnage fixe : en pratique, un décodage déterministe (ou une température très basse) écrase toute dispersion et ramène la sévérité à zéro, y compris sur les faits arbitraires, tandis que l’évaluation de textes libres exige de comparer les réponses par leur sens plutôt que mot à mot [@farquhar2024].
:::

Sortir de cette logique qui pousse les modèles à inventer des faits rares exige d’agir sur les incitations mêmes de l’entraînement et de l’évaluation [@kalai2025] : apprendre aux modèles à s’abstenir lorsque leur probabilité d’exactitude est insuffisante et, dans les bancs d’épreuve, noter explicitement l’abstention au-dessus d’une réponse devinée à tort. Si les classements publics conservent encore largement une notation binaire qui pénalise l’aveu d’ignorance, toute organisation qui déploie ses propres évaluations peut dès aujourd’hui modifier son barème.

Ces résultats appellent enfin deux mises au point essentielles : la première sur la frontière entre les deux sens de *calibration*, la seconde sur la place réelle qu’occupe le signal d’incertitude dans un modèle génératif.

::: {.nuance titre="Deux sens de calibration, et où s’est logé l’indice d’incertitude"}
Deux confusions guettent la lecture de ce qui précède.

La première consiste à mêler les deux sens du mot *calibration* distingués dans cet ouvrage. La calibration au sens de la confiance (@sec:ch03-calibration-historique) — qu’une affirmation émise avec une confiance de 70 % soit exacte environ sept fois sur dix — constitue un progrès honnête et précieux, bien qu’insuffisant à lui seul devant les décisions uniques (@sec:ch04). La calibration générative, au contraire, oblige la distribution des énoncés produits à épouser celle du corpus d’entraînement ; sur les faits arbitraires de la longue traîne, elle *entraîne* mathématiquement l’invention et doit être abandonnée [@kalai2024]. Les deux notions s’articulent pourtant : c’est en s’appuyant sur une estimation calibrée de sa propre confiance qu’un modèle peut choisir de s’abstenir au lieu de suivre la calibration générative.

La seconde confusion serait de conclure de façon trop absolue que « rien dans le modèle ne calcule de signal lorsqu’il quitte sa zone de compétence ». Pour les erreurs de devinette, l’étalement de la probabilité entre de multiples réponses concurrentes forme bel et bien un indice d’incertitude réel, mesurable directement par échantillonnage répété et par entropie sémantique [@farquhar2024]. Ce qui a disparu au sommet de la pile n’est pas toute trace interne du doute, mais sa manifestation visible à la surface d’une réponse isolée : l’indice d’incertitude a migré de l’allure d’une réponse unique vers la dispersion entre plusieurs réponses — et il reste absent dès que le modèle se trompe avec constance.
:::

Avec ce chapitre s’achève l’exploration de la pile logicielle, des contrats spécifiés (@sec:ch10) aux composants appris (@sec:ch11) jusqu’au changement de régime qui touche le sommet : promesse statistique, échec fluide, enquête sans adresse, frontière en dents de scie et partage entre devinette dispersée et erreur constante. Le @sec:ch13 va maintenant synthétiser l’appareil épistémologique de la @sec:partie-2 et cette analyse informatique en deux axes de classement des erreurs et quatre sources de comparateurs.

::: {.question}
Pour les modèles de langage intégrés à votre pratique, avez-vous établi sur vos propres tâches où passe leur frontière en dents de scie, et sur quels comparateurs indépendants — au-delà d’une simple répétition de la question — repose votre contrôle avant qu’une sortie ne gouverne une action ?
:::

## Points clés {.points-cles}

- Au sommet de la pile logicielle, ce qui est promis, la forme de l’échec et le lieu où aboutit l’enquête basculent ensemble (changement de régime) : une erreur revêt la même fluidité qu’une réussite et ne renvoie à aucune adresse où appliquer un correctif local.
- L’axe du changement de régime n’est ni la fréquence moyenne des erreurs ni le fait qu’une défaillance passe inaperçue, mais l’absence de spécification écrite vérifiable en amont : les contrôles doivent être rebâtis autour des tâches qui admettent un comparateur mécanique ou placés sur chaque sortie individuelle.
- La compétence d’un modèle dessine une frontière en dents de scie, irrégulière, mouvante d’une version ou d’une formulation à l’autre et indiscernable de l’intérieur de la conversation, en partie sous l’effet d’omissions de saillance distinctes des omissions structurelles.
- Soumis à la calibration générative, un modèle doit inventer des faits rares et arbitraires à une fréquence comparable au taux de singletons de ses données d’entraînement, tandis que les évaluations qui notent l’abstention comme une erreur sélectionnent la devinette assurée.
- Interroger le modèle à plusieurs reprises constitue un contrôle sévère contre les erreurs de devinette qui dispersent les réponses, mais laisse passer les erreurs constantes répétées d’une même voix, tout en déclenchant des alertes même lorsque la première réponse était juste.
