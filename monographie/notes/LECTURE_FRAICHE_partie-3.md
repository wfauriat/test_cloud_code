# Lecture fraîche : partie 3 (« De l'informatique classique à l'IA »)

## Résumé de ce que j'ai compris (test de lisibilité)

La partie présente quatre chapitres : en informatique classique, un contrat écrit permet de contrôler un composant à l'avance et de localiser toute défaillance ; avec l'apprentissage automatique, la règle vient des données, il n'y a plus de contrat vérifiable ni d'« adresse » de l'erreur, et une réponse fausse ressemble à une réponse juste ; il faut alors reconstruire des contrôles (comparateurs mécaniques, ou contrôle sortie par sortie), et le dernier chapitre classe les erreurs selon deux questions (cause interne ou externe au « cadre », signalée ou non). La partie suivante traitera des chaînes automatisées. Le fil général est clair ; ce qui résiste, c'est le détail de certaines phrases du chapitre 13 et quelques raccourcis (Mars Climate Orbiter, « faits rares »).

## Constats

### Gravité A

**A1. « La réponse à la première question est fixée par le cadre et ne peut pas être examinée de l'intérieur »**
Gêne : la phrase est quasi tautologique ou obscure (le cadre « fixe » la réponse à la question de savoir si la cause est dans ou hors du cadre ?). On ne sait pas ce qui est « examiné » ni pourquoi c'est impossible de l'intérieur.
Deux lectures plausibles : (a) ce qui est dans ou hors du cadre est une décision de modélisation, donc on ne peut pas le contester sans sortir du cadre ; (b) on ne peut pas savoir, depuis l'intérieur, si une cause externe existe (facteur omis, donc invisible). Je ne tranche pas.
Reformulation minimale (lecture a) : « la réponse à la première question tient à la manière dont le cadre a été tracé, et on ne peut pas la remettre en cause en restant à l'intérieur de ce cadre ». Pour (b) : « on ne peut pas répondre à la première question en restant à l'intérieur du cadre, puisqu'un facteur omis n'y apparaît pas ». Le sens bouge selon le choix.

### Gravité B

**B1. « Les composants appris produisent des erreurs du type le plus délicat : leur cause est interne au cadre, et rien ne les signale. »**
Gêne : « le plus délicat » semble contredit par la suite (« Aucun contrat ne fait entrer dans le cadre un facteur que ce cadre a omis »), qui évoque un cas externe et non signalé, a priori pire. Le lecteur ne voit pas la grille des quatre cas ni le critère de « délicat ».
Deux lectures : le plus délicat parce que le plus fréquent/propre aux composants appris, ou le plus délicat parce qu'on pourrait l'éviter et qu'on ne le fait pas (interne, donc corrigeable en principe). Je ne tranche pas.
Reformulation minimale : « des erreurs d'un type particulier, et particulièrement difficile à traiter : ... » ou « le type le plus délicat parmi ceux que l'on pourrait en principe exclure ». Le sens bouge.

**B2. « Il en va encore ainsi lorsqu'un logiciel produit des résultats faux pendant des mois sans qu'aucune alarme ne l'arrête, comme lors de la perte de la sonde *Mars Climate Orbiter*. »**
Gêne : le lecteur ne sait pas quelle règle écrite a été enfreinte dans ce cas (confusion d'unités entre deux modules ?), donc l'exemple illustre mal « la défaillance a une adresse ». « Il en va encore ainsi » + « sans alarme » se lit presque comme un contre-exemple. « l'arrête » : « l'» = le logiciel (ou les résultats ?).
Reformulation minimale : « ... comme lors de la perte de la sonde *Mars Climate Orbiter*, où deux modules ne comptaient pas dans les mêmes unités : l'interface enfreinte était identifiable. » Le sens ne bouge pas ; j'ajoute seulement l'information implicite.

**B3. « Parce que cette promesse est écrite, et pour peu qu'elle soit appliquée mécaniquement, on peut contrôler... »**
Gêne : « elle » (la promesse ? la vérification ?) et « appliquée mécaniquement » (vérifiée par un outil ? respectée à chaque appel ?) sont flous ; la condition est lourde à construire (« Parce que... et pour peu que »).
Reformulation minimale : « Parce que cette promesse est écrite, et pourvu que son respect soit vérifié mécaniquement, on peut ... ». Le sens risque de bouger si « appliquée » visait l'exécution plutôt que la vérification.

**B4. « Il montre qu'un modèle qui reproduit fidèlement la distribution de ses données d'entraînement est conduit à inventer des faits rares. »**
Gêne : raccourci non expliqué ; « fidèlement » et « inventer » semblent contradictoires, et « faits rares » n'est pas défini. Passage incompréhensible sans le chapitre.
Reformulation minimale : « ... est conduit à produire des réponses plausibles même pour des faits trop rares dans les données pour être appris (par exemple une référence unique) ». Sens possible à préciser : l'invention vient-elle de la rareté ou de l'optimisation de la plausibilité ?

**B5. « ou bien les placer sur chaque sortie, une à une »**
Gêne : qui contrôle (humain, autre outil) et comment, sans comparateur ? Le lecteur doit déduire qu'il s'agit d'un contrôle au cas par cas.
Reformulation minimale : « ... ou bien contrôler chaque sortie individuellement ». Sens inchangé.

**B6. « quatre sources de comparateurs (un texte fixé à l'avance, ses propres contrôles, un autre raisonneur, le monde) »**
Gêne : « ses » n'a pas de référent clair (le modèle ? le composant ? l'utilisateur ?). « un texte fixé à l'avance » est énigmatique (spécification ? référence ?).
Reformulation minimale : « ... (une spécification écrite à l'avance, les propres contrôles du composant, un autre raisonneur, le monde) ». Le sens bouge selon le référent retenu pour « ses ».

**B7. « Les consignes, l'ajustement sur des préférences humaines et les tests de référence orientent le modèle »**
Gêne : « consignes » (instructions fournies au modèle), « ajustement » et « tests de référence » ne se comprennent qu'avec le jargon ; surtout, des tests de référence qui « orientent » le modèle surprend (ils mesurent, ne dirigent pas).
Reformulation minimale : « ... et l'évaluation sur des tests de référence orientent le développement du modèle ». Possible dépendance : « consignes », « ajustement sur préférences ».

**B8. « Ces composants » (dernier paragraphe) et « s'effacent devant eux »**
Gêne : après un paragraphe sur composants appris et composants spécifiés, « ces composants » est ambigu ; « devant eux » pourrait viser les composants ou les processus.
Reformulation minimale : « ces composants appris » ; « s'effacent devant ces processus ». Sens plus probable : composants appris ; à confirmer.

**B9. Possible dépendance : « comparateur », « cadre », « raisonneur »**
Termes employés comme acquis (« comparateur mécanique », « à l'intérieur du cadre ») dont le lecteur a peut-être la définition en partie 2, mais ils sont absents de ce texte ; je signale sans juger.

### Gravité C

**C1.** « reprend les résultats de la @sec:partie-2 et les porte sur l'empilement des couches logicielles » : « porter sur » est un calque (carry over/apply to). Proposition : « les transpose à l'empilement ».

**C2.** « la théorie des contrôles » : usage courant « théorie du contrôle » ; possible terme technique voulu, à confirmer.

**C3.** « une frontière irrégulière » : probable calque de *jagged frontier* ; « frontière en dents de scie » ou « dentelée » serait plus parlant. Possible dépendance.

**C4.** « Il montre... Il montre enfin... » enchaîné après « le modèle » : « Il » peut être lu comme le modèle ; remplacer par « Le chapitre montre ».

**C5.** « un autre raisonneur » : néologisme/calque de *reasoner*, compréhensible mais étrange.

**C6.** « la validation, qui consiste à poser un problème assez fidèle à la réalité et qui ne s'automatise pas » : le second « qui » peut se rattacher à « problème » ou « réalité ». Proposition : « ..., et qui ne s'automatise pas » -> « ; elle ne s'automatise pas ».

**C7.** « non par nature, mais grâce au contrat écrit » : « par nature » reste allusif (nature du composant). Passable.

**C8.** Typographie : rien de manifeste (guillemets, espaces insécables, ponctuation conformes).

Les passages sur le chapitre 10, 11 et 12 (hors points ci-dessus) fonctionnent bien.
