# Décisions sur les arbitrages de la synthèse

Journal des décisions prises sur les points du groupe 2 de `notes/SYNTHESE_A_TRANCHER.md`, au fil d'une revue interactive avec l'auteur. Pour chaque point : la décision et sa portée. Un point « ouvert » est réservé à une discussion ultérieure. Un point « bloquant » doit être tranché avant toute application, parce qu'il touche de nombreux fichiers.

Aucune décision n'est encore appliquée au texte.

## Politiques éditoriales (§ 3.3)

- **N1. La notation $(\dots)$ en texte courant.** *Adopté*, après discussion. L'auteur juge la notation, reprise de la perspective de Pearl, trop proche de l'exposé oral d'origine. « Le reste » et « non-spécifié » ont été écartés (collisions avec le « remainder » de l'article et avec « composant spécifié »). La règle retenue :
  - dans les formules affichées, $A \cap (\dots) \rightarrow B$ ne change pas : les points de suspension montrent que la liste est ouverte ;
  - au ch. 1, une phrase nomme la parenthèse et donne la lettre : « l'**arrière-plan tacite**, noté aussi $\mathcal{T}$ dans le texte » ;
  - en prose, « l'arrière-plan tacite $\mathcal{T}$ » à la première mention de chaque chapitre, puis le nom seul. La lettre seule n'apparaît que là où une phrase manipule l'arrière-plan (« une variation de $\mathcal{T}$ »). Jamais de « $(\dots)$ » nu en prose ;
  - « arrière-plan tacite » devient un terme du registre, introduit en gras au ch. 1, et la ligne des notations est mise à jour ;
  - V19 est réglé du même coup : « arrière-plan tacite » et « conditions tacites » remplacent « conditions tues », « arrière-plan tu », « conditions sous-entendues » et « arrière-plan non énoncé ».

  Portée : le registre et une quinzaine de passages répartis dans 13 fichiers. À surveiller : au ch. 2, l'encadré causal emploie $T$ pour la variable d'intervention ($\mathrm{do}(T = t)$), dont la forme est proche de $\mathcal{T}$. On pourrait la renommer, sans urgence.

## Formulations du registre (§ 3.1)

- **R1. « ne vaut que » (déduction, induction).** *Adopté.* « ne garantit sa conclusion que si… » sur la page de la partie 1 ; « ne garantissent leur conclusion que « pourvu que »… » dans le registre, les PC du ch. 1 et le chapeau du ch. 2.
- **R2. « spécification finie ».** *Adopté.* Le terme est gardé, avec une glose unique à la définition du ch. 2 : « finie, c'est-à-dire bornée et donc incomplète ».
- **R4. Sévérité.** *Adopté.*
  - Le registre, la page de la partie 2, le ch. 9 et la conclusion disent : « Un contrôle passé sans alerte n'est probant que dans la mesure où il aurait donné l'alerte si l'affirmation avait été fausse (Mayo) ».
  - Au ch. 9, une phrase est ajoutée après la définition : « On la mesure par $\Pr(\bar A \mid E)$, la probabilité que le contrôle donne l'alerte quand l'affirmation est fausse. »
- **R5. Comparateur : « un texte fixé à l'avance ».** *Ouvert*, réservé à la discussion. Non bloquant.
- **R6. Vérification en amont.** *Adopté.* Dans le registre et au ch. 10 : « Contrôle d'un composant fait une fois, par rapport à sa spécification, et qui porte sur le composant plutôt que sur chacune de ses sorties : ce qu'il établit vaut pour toutes ses exécutions futures. » Dans les PC du ch. 10 : « peut contrôler le composant une fois pour toutes ».
- **G1-4. Probabilité d'échappement** (point du groupe 1, confirmé ici parce qu'il modifie le registre). *Adopté.*
  - Dans le registre, au ch. 6 et au ch. 9 : « Probabilité qu'une affirmation fausse débouche sur une action sans qu'un désaccord ait été détecté et pris en compte à temps. »
  - Dans l'encadré du ch. 6 : « c'est-à-dire la probabilité de l'événement contraire $\overline{D}$ : atteindre l'action sans qu'un désaccord ait été détecté et pris en compte à temps ».
- **R8. Erreur signalée, erreur silencieuse.** *Adopté.* Dans le registre et au ch. 13 : « Erreur que contredit au moins un comparateur avant l'action ; erreur que rien ne contredit avant l'action. »
- **R9. Bac à sable et verrou.** *Adopté.*
  - Les deux définitions du registre sont gardées.
  - « ne pourrait (plus) être effacée » devient « serait irréversible » au ch. 17 (trois occurrences) et sur la page de la partie 5 ; sur cette page, « elle » devient « cette réponse ».
  - Phrase ajoutée au ch. 17, après la définition du bac à sable : « Le monde qu'on y interroge est réel lorsqu'il est lui-même calculatoire (le compilateur, les tests, une base de données d'essai) ; ailleurs, le bac à sable n'interroge que ce qu'il reproduit. »
- **R11. Prise en compte.** *Adopté.*
  - Dans le registre et au ch. 6 : « Fait qu'un désaccord parvienne à quelqu'un qui à la fois en prend acte et a l'autorité pour agir en conséquence. »
  - Dans l'encadré du ch. 6 ($C_5$) : « ait l'autorité » au lieu d'« exerce l'autorité ».
  - Cette définition alimente la discussion D4 sur *Challenger*.
- **R3. « décision unique ».** *Adopté.* Nouvelle définition, dans le registre et au ch. 4 : « décision prise sans série d'essais comparables, si bien qu'une issue malheureuse ne peut être compensée par d'autres cas : la réponse du monde n'arrive qu'après l'acte, trop tard pour le corriger ».
- **N2. Rappels de termes hors de leur chapitre.** *Adopté.* Un rappel bref par chapitre est autorisé, repris mot pour mot de la définition du registre, sans gras. Il concerne les termes introduits au moins deux parties plus tôt, et les chapitres d'entrée des parcours de lecture du ch. 0. Environ 25 points deviennent applicables.
- **N3. Modèles M1 à M3.** *Adopté.* On garde la numérotation de la spec. La série est présentée une fois au ch. 0 (§ Architecture), et chaque première mention dans un chapitre est accompagnée de quelques mots de description (« le modèle M1, des angles morts et de l'échappement, @sec:ch08 »). Huit fichiers.
- **N4. $P(E)$, $\Pr(E)$, $P(\text{faux})$.** *Adopté.* Les trois notations sont gardées. L'équivalence est posée à la première occurrence aux ch. 6, 9 et 16. En prose, $c$ s'écrit en pourcentage, comme dans les tableaux.
- **R10. Affirmation et observation.** *Adopté.* « rapport de mesure » reste dans la définition de l'affirmation. Au ch. 6, la famille 3 devient : « une observation du monde (le fait observé lui-même, non le rapport qui en rend compte) ».

## Vocabulaire transversal (§ 3.2)

- **V20. Les cinq conditions.** *Adopté.*
  - Noms fixés : existence, différence, comparabilité, arrivée à temps, prise en compte.
  - Nom de la grille : « les cinq conditions de détection ».
  - Chaque chapitre qui s'appuie sur elles les énumère à la première mention, avec « différence (se tromper autrement) ».
  - Fichiers concernés : ch. 6, 8 à 10, 13, 14, 17, 18 et la conclusion. La métaphore des « barrages » est traitée à part (S2).
- **V21. Comparabilité, lisibilité, comparaison fidèle.** *Ouvert*, réservé à la discussion. Non bloquant.
- **V1. Exact, précis, fiable.** *Ouvert*, réservé à la discussion. Non bloquant.
- **V2. Statut.** *Adopté*, après discussion. Les deux sens reçoivent deux expressions distinctes.
  - Pour les propositions du livre : « statut épistémique » (le mot de l'avant-propos), ou « statut » seul au voisinage des propositions. Glose à la première occurrence : « (définition, résultat sous hypothèses, hypothèse de travail ou constat empirique) ».
  - Pour un résultat dans un processus réel de décision ou de prévision : « état de vérification », glosé une fois : « exploratoire ou établi, ce qui a été contrôlé de façon indépendante et par qui, sous quelles hypothèses principales ».
  - Fichiers concernés : ch. 0, pages des parties 2 et 5, ch. 18 (y compris un titre de section), conclusion.
  - Écartés : « niveau de confiance », en collision avec le niveau de confiance statistique ; « force de l'affirmation », qui évoque l'assurance plutôt que le contrôle.
- **V3. Signature.** *Adopté.* Le motif est gardé. Il est glosé une fois, à la première occurrence du ch. 6 : « une signature au bas du dossier, qui engage sans rien prouver ».
- **V4. Couche.** *Adopté.*
  - « couche » est réservé à la pile logicielle.
  - Pour la compétence du relecteur : « comprendre le niveau situé sous l'interface que l'on contrôle », avec les exemples de la source à la première occurrence (ch. 0, ch. 18) : « le code sous le programme généré, la physique sous le nombre calculé ».
  - Au ch. 17 : « la couche de la pile qui offre le moins de garanties (le modèle de langage) ».
- **V5. Devinette.** *Adopté*, après discussion. On écrit « erreurs hasardées », par opposition aux « erreurs constantes ». Pour l'acte : « le modèle hasarde une réponse ». Pour un tirage : « une réponse hasardée ». Fichiers concernés : ch. 12 à 15 et la conclusion.
- **V6. Invention.** *Adopté.*
  - « invention » est le terme courant, avec « (ce qu'on appelle couramment une hallucination) » à la première occurrence du ch. 11.
  - « confabulation » n'est employé que pour rapporter l'usage de Farquhar et al.
  - Dans le passage sur l'ajustement par préférences : « modèle de récompense » partout, au lieu de « modèle auxiliaire ».
- **V7. Orienter.** *Adopté.*
  - « orienter » et « orientation » désignent l'effet ; ils remplacent « alignement » et « alignés » (ch. 12, 13).
  - « ajustement sur des préférences humaines » désigne le moyen, toujours avec la même préposition (ch. 15, 16).
- **V8. Consigne et requête.** *Adopté.*
  - « consigne » partout où l'on parle d'un *prompt* (ch. 10 à 12).
  - « requête informatique » est gardé au ch. 12.
  - « consigne système » est glosé une fois : « instructions placées en tête de chaque échange, que l'utilisateur ne voit pas ».
- **V16. Les trois effets de l'automatisation.** *Adopté.*
  - Page de la partie 5 et chapeau du ch. 18 : « met nos contrôles en chaîne, en retire certains et corrèle ceux qui restent ».
  - Titres du ch. 0, avec un sujet explicite (étiquettes inchangées) : « L'automatisation met les étapes en chaîne et fait passer les erreurs à l'acte » ; « L'automatisation érode les vérifications humaines » ; « L'automatisation corrèle les angles morts à l'échelle collective ».
- **Harmonisations adoptées en lot.**
  - V9 : « théorie des contrôles », partout.
  - V10 : « classe d'erreurs ».
  - V11 : « prendre une décision », au lieu de « trancher une décision » (page de la partie 4, ch. 16, avant-propos, ch. 18).
  - V12 : « se former d'abord son propre jugement » ou « fixer d'abord sa propre estimation », au lieu d'« arrêter ».
  - R7 : « les angles morts se cumulent » (registre, ch. 8).
  - V17 : « exemples récurrents » (ch. 0, avant-propos).
  - V13 : « lassitude face aux alertes », au lieu d'« usure des alertes », partout, y compris dans un titre de bloc au ch. 16.
  - V15 : « recueil de règles » (page de la partie 5, ch. 18).
- **V14. Chiffre assuré.** *Adopté.* L'expression est gardée. Elle est glosée une fois, à la première occurrence du ch. 17 : « un chiffre assuré, c'est-à-dire présenté avec assurance, sans ses conditions ».
- **V18. « De l'intérieur ».** *Adopté.* Le référent est nommé à chaque occurrence :
  - « de l'intérieur du cadre » (page de la partie 3, ch. 13) ;
  - « à l'usage » (ch. 12) ;
  - « de l'intérieur de son propre cadre » (ch. 16).

## Contenu et structure (§ 3.4)

- **S14. Critère de la probabilité nulle.** *Adopté.*
  - Le critère est harmonisé sur « logiquement impossible » (règle de Cromwell) aux ch. 1 et 3.
  - Au ch. 3, la règle de prudence est complétée : « même lorsqu'on décide de ne pas examiner certains mondes : ne pas s'y attarder n'est pas leur donner zéro ».
  - Le PC du ch. 3 reprend la formulation du corps : « que l'on ne peut raisonnablement écarter ».
- **S6. La roulette russe (ch. 4, ch. 17).** *Ouvert*, réservé à la discussion. Non bloquant.
- **S5. 2008 (ch. 5).** *Adopté.*
  - L'encadré est récrit : la quasi-indépendance, estimée sur une période sans baisse nationale, était figée dans la structure des modèles, si bien qu'un couplage généralisé ne pouvait pas être engendré.
  - Les faits sont à vérifier lors de la passe bibliographique.
- **S4. Hypothèses du volet (b) de @prop:cause-commune (ch. 7).** *Adopté.*
  - Phrase ajoutée après la proposition : « Le volet (a) repose sur les hypothèses du modèle M3 ci-dessous. Le volet (b) suppose que les observations sont produites par le monde et non calculées dans le cadre, que $z$ a varié pendant leur collecte, et que son effet ne se lit que sur les grandeurs enregistrées, issue comprise, sous la forme d'une dispersion que rien n'attribue. »
  - « volet » partout, au lieu de « partie ».
