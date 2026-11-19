# Lecture fraîche — partie 2 (« Ce qui peut nous détromper »)

## Résumé (test de lisibilité)

La partie annonce qu'elle étudie, avec des exemples hors IA, ce qui peut avertir qu'une représentation finie a omis l'essentiel. Elle suit cinq chapitres : les types d'incertitude (une barre d'erreur ne voit pas ce que le cadre ignore) ; les cinq conditions pour qu'une comparaison révèle une erreur ; l'inutilité des contrôles internes au même cadre contre les omissions ; l'indépendance relative des contrôles, en chaîne ou croisés ; la valeur d'un contrôle (fausses alertes, risque = probabilité d'erreur × probabilité qu'elle échappe aux contrôles). Elle se clôt sur le passage à l'informatique (partie suivante). Le texte se lit bien dans l'ensemble ; je n'ai rien trouvé qui compromette la compréhension.

## Constats

### Gravité A
Aucun.

### Gravité B

**B1.** « Un contrôle réussi n’apporte une preuve que dans la mesure où il aurait échoué si l’affirmation avait été fausse. »
« Réussi » est ambigu : contrôle « bien exécuté » ou contrôle « passé sans alerte » ? La suite (« aurait échoué ») impose la seconde lecture mais le lecteur peut d'abord comprendre la première.
Reformulation : « Un contrôle passé sans alerte n’apporte une preuve que… » (sens inchangé si la lecture « sans alerte » est bien celle visée ; si l'auteur pensait « bien exécuté », le sens change).

**B2.** « Ce blanchiment rend les résultats impossibles à comparer »
« Blanchiment » apparaît ici pour la première fois, avec un démonstratif, comme s'il avait été défini ; il faut deviner que c'est la perte des conditions, unités et origine. En outre « impossibles » est fort face au « souvent » de la phrase précédente.
Reformulation : « Ce blanchiment (le résultat arrive en aval dépouillé de ses conditions) rend… difficiles à comparer ». Deux lectures possibles de la force de l'effet (« impossible » voulu vs « difficile ») : ne pas trancher sans l'auteur.

**B3.** « Il leur faut pourtant partager assez pour pouvoir être comparés, si bien qu’un comparateur plus éloigné demande le plus souvent davantage de travail pour que son objection porte. »
Le lien logique est implicite : « si bien que » suggère une conséquence directe du partage minimal, mais l'étape intermédiaire (plus on est éloigné, plus il faut de travail pour rendre comparable) n'est pas dite.
Reformulation : « …; plus un comparateur est éloigné, plus il faut de travail pour le rendre comparable et faire porter son objection. » Sens stable si c'est bien l'idée ; autre lecture possible (« travail » = effort de l'objecteur pour convaincre) qui changerait légèrement le sens.

**B4.** « Le chapitre décompose surtout le risque réel en un produit de deux facteurs »
« Surtout » peut signifier « principalement / avant tout » ou « en particulier » ; il n'est pas clair non plus s'il oppose ce point aux précédents. « Réel » oppose-t-il à « apparent » ? Peu clair.
Reformulation : « Le chapitre décompose aussi le risque en un produit de deux facteurs » (si « avant tout » était voulu : « Son apport principal est de décomposer… »). Le sens bouge selon la lecture.

**B5.** « là où l’essai coûte peu et peut être défait »
Elliptique : « défait » = réversible (on peut annuler l'essai) ? ou « démenti » ? Le lecteur comprend probablement « réversible ».
Reformulation : « là où l’essai coûte peu et reste réversible ». Si « démenti » était voulu, le sens change.

### Gravité C

**C1.** « Or, lorsque les erreurs deviennent rares, un contrôleur dont le taux de fausses alertes ne change pas émet surtout des alertes injustifiées. »
« Or » n'est pas adversatif ici ; « contrôleur » (personne ou dispositif) n'est pas défini ; le raisonnement (taux de fausses alertes fixe, erreurs rares, donc alertes surtout fausses) reste implicite mais se devine.
Reformulation : « Mais lorsque les erreurs deviennent rares, un contrôle dont le taux de fausses alertes reste constant… ». Sens inchangé.

**C2.** « Le désaccord doit en outre se manifester avant que l’on agisse. »
Dans une énumération numérotée (d'abord / ensuite / puis / enfin), « en outre » rompt le rythme ; on hésite sur le nombre de conditions (cinq annoncées).
Reformulation : « Il faut ensuite que le désaccord se manifeste avant que l’on agisse », en ajustant les autres marqueurs. Sens inchangé.

**C3.** « un texte fixé à l’avance »
Comparateur peu parlant isolément (spécification ? protocole ? prédiction enregistrée ?). Dépend de ce que l'auteur veut dire ; pas de reformulation sans lui.

**C4.** « car elle reposerait à son tour sur un cadre fini qu’il faudrait contrôler »
« Elle » = la procédure, mais « cette limite » est le nom féminin le plus proche. Lecture correcte probable ; légère gêne.
Reformulation : « car cette procédure reposerait à son tour… ». Sens inchangé.

**C5.** « les parties suivantes montreront ce que ces machines y changent »
« Y » est flou (dans ces mécanismes ? à cette question ?).
Reformulation : « ce que ces machines changent à ces mécanismes ». Sens stable.

**C6.** « Reste à savoir ce que devient cette théorie des contrôles »
« Théorie » est employée pour la première fois ici ; l'intro parlait de « propositions » et de « cœur formel ». Cohérence terminologique à vérifier ; non bloquant.

**C7.** « Ainsi, un facteur oublié qui est resté constant… »
« Ainsi » introduit un exemple/conséquence ; acceptable, mais « Par exemple » ou « Un facteur oublié… » serait plus net. Sens inchangé.

### Possible dépendance (sans jugement)
- « représentation finie » / « la représentation a omis l’essentiel » (première phrase) : suppose un concept établi en amont (partie 1).
- « rééchantillonner » et « cause commune » (chapitre 7) : termes statistiques/fiabilité non glosés.
- « angles morts » (chapitre 8) : métaphore employée comme terme technique sans définition ; devinable.
- « règle de Bayes » (chapitre 9) : cité sans rappel ; accessible à un lecteur cultivé mais non explicité.

### Typographie
Apostrophes typographiques, ponctuation haute précédée d'espaces, italique pour *Challenger* : rien de manifestement fautif (les espaces insécables ne sont pas vérifiables à l'œil).
