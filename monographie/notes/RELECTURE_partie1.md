# Relecture d’ensemble — Partie I (chapitres 1 à 4)

**Portée.** Les chapitres 2, 3 et 4 ont d’abord été relus et corrigés un à un ; chaque relecture est consignée en tête du fichier `NOTES_0N.md` correspondant (paragraphe « Révision après relecture (deuxième passe) »). Le chapitre 1 avait déjà été révisé. La présente passe relit la partie comme un tout, chapitres 1 à 4. Elle vise la cohérence d’un chapitre à l’autre (vocabulaire, exemples, renvois, notations) et la lisibilité du français : tournures calquées sur l’anglais, phrases ambiguës, formulations obscures à la première lecture.

**Vérifications.**
- `make chapitre CH=01` à `CH=04` : les quatre aperçus se compilent.
- `make verifier` : 0 erreur ; 1 avertissement (le tableau généré `tableaux/ch01-bayes-cotes.md` manque).
- Compilation HTML combinée des chapitres 0 à 4 : tous les renvois internes à la partie se résolvent, et aucun ne se rend avec un article ou un genre fautif (« au section », « la chapitre »…). Seuls restent non définis les renvois vers les chapitres 5 à 18, encore à l’état d’ébauche.
- Aucun terme du registre n’est employé avant son chapitre d’introduction. Chaque terme introduit dans la partie est mis en gras une seule fois, dans le bon chapitre.

## Corrections apportées lors de la passe d’ensemble

### Cohérence entre chapitres
- **Bateaux :** « voilier léger » et « voilier renforcé » partout. Le chapitre 2 écrivait encore « bateau renforcé ».
- **Intervalles :** notation française, $\left]0, 1\right]$ au chapitre 1 et $\left]0, 1\right[$ au chapitre 3, au lieu de `(0, 1]` et `(0, 1)`.
- **Renvois relatifs remplacés par des étiquettes :**
  - chapitre 3, « le chapitre suivant » devient « le @sec:ch04 » ;
  - chapitre 3, « la section suivante » devient « la @sec:ch03-calibration-historique ».
  - Le sens ne change pas, et une renumérotation ne casse plus ces renvois.

### Lisibilité et français
- **Chapitre 1 :**
  - « On peut le lire d’une traite en ouvrant la partie I » était ambigu (qui ouvre quoi ?). Devient « à l’entrée de la partie I ».
  - « Voyons Ω comme… » devient « Représentons-nous Ω comme… ».
- **Chapitre 2 :**
  - « une fissure cachée dans l’estimation du navigateur » se lisait comme une fissure *dans l’estimation*. Devient « pour le navigateur, une fissure cachée dans le mât ».
  - « On emporte enfin le même récipient ouvert » suivait un essai en récipient clos, d’où une contradiction apparente. Devient « dans un récipient ouvert cette fois ».
  - « Une nécessité irréprochable à l’intérieur d’un problème mal posé n’est qu’une nécessité à l’intérieur d’un mauvais cadre » était tautologique et obscur. Devient « Une démonstration impeccable, menée sur un problème mal posé, ne garantit rien de la situation réelle ».
  - « une décision préalable, la description dans un cas, le jugement de ressemblance dans l’autre, qu’aucune… » : la relative était trop éloignée de son antécédent. Phrase réordonnée.
  - « l’approche des causes par graphes » devient « l’approche graphique de la causalité ».
  - « suppose que les cas futurs *sont* échangeables » : subjonctif rétabli (« soient »).
  - « large cohorte » (anglicisme) devient « vaste cohorte ».
  - Supprimé, au début de la première section, une phrase qui répétait l’énumération « personne, équipe, institution… » donnée deux phrases plus haut.
  - Titre du bloc *Nuance* raccourci en « Énoncer plus ou taire plus ». La formule « aucun réglage ne supprime les deux risques » apparaissait trois fois de suite : dans le texte, dans le titre et dans la conclusion du bloc.
  - Le long paragraphe sur le problème du cadre est coupé en deux : historique, puis sens retenu dans le livre.
- **Chapitre 3 :**
  - « Ce serait une propriété du mât » (sujet flottant) devient « Le nombre serait alors une propriété du mât ».
  - « il indique où l’inférence prend appui » devient « sur quoi ».
- **Chapitre 4 :**
  - « Savage a donné à cette règle un fondement » devient « un fondement axiomatique ».
  - « Il suffit que l’un des deux termes se déplace pour que la décision change » était inexact : seul un franchissement du seuil change la décision. Devient « La décision peut basculer par l’un ou l’autre des deux termes de la comparaison », suivi des deux exemples chiffrés.
  - « La règle ne décide à la place ni de la représentation ni des valeurs » (construction bancale) devient « La règle ne se substitue ni à la représentation ni aux valeurs du décideur ».
  - « la courbe devient une droite de pente −1 » devient « se confond presque avec », car la courbe n’est qu’asymptotiquement droite.
  - « lancer une opération irréversible », qui répétait « opération chirurgicale » dans la même énumération, devient « engager une action irréversible ».

## Choix de vocabulaire communs à la partie (pour les chapitres suivants)
- **« agent » :** jamais au sens courant, puisque le terme est réservé au chapitre 14. À la place : « celui qui agit », « quiconque agit », « le décideur », « le prévisionniste », « on », ou « une personne, une équipe ou une organisation ».
- **Course au large :**
  - personnages : M. X (5 %) et M. Y (0,1 %), sur le quai ;
  - bateaux : « voilier léger » et « voilier renforcé » ;
  - événement : « le bateau casse / tient » (démâtage, ou avarie qui oblige à abandonner) ;
  - enjeux : la perte en cas de casse vaut vingt-cinq fois le gain en cas de succès.
- **Autres termes :**
  - « jeu d’étalonnage » pour les données de réglage de la prédiction conforme, afin de réserver *calibration* au sens du chapitre 3 ;
  - « série de référence » pour la classe de référence fréquentiste ;
  - « régression à l’infini » pour le report du choix du cadre (repris au chapitre 7) ;
  - « retard à l’ébullition » pour l’eau surchauffée.

## Écarts par rapport à la spec
- **Chapitre 3 :** renvoi explicite au @sec:ch04 dans la dernière section, alors que la spec ne liste pas ce lien vers l’avant. Il ne fait qu’annoncer le passage de la probabilité à la décision, sans employer aucune notion du chapitre 4. Il remplace « le chapitre suivant », qui était le même renvoi sans étiquette.
- **Chapitre 2 :** une phrase porte un marqueur `[@A-VERIFIER: Shanahan, « The Frame Problem », SEP]` (réponses techniques au problème du cadre au sens logique). On peut la supprimer sans dommage si l’on ne veut pas de cette référence ; l’entrée proposée est dans `NOTES_02.md`.

## Points à traiter hors des chapitres (mainteneur)
1. **Figures étirées (gabarit) : corrigé.**
   - Le filtre remplace les figures des blocs par du LaTeX brut. Pandoc ne voit donc plus d’image et omet, dans son modèle, le réglage `\setkeys{Gin}{…,keepaspectratio}`. Or il écrit `width=…,height=\textheight` pour une image dont seule la largeur est fixée : sans `keepaspectratio`, la figure était étirée sur toute la hauteur de la page, dans les aperçus comme dans le livre complet.
   - Correction : `graphics: true` ajouté aux variables de `gabarit/pdf.yaml`. `make essai` et `make pdf` passent ; les figures 3.1 et 4.1 ont retrouvé leurs proportions.
2. **Artefacts manquants :**
   - `tableaux/ch01-bayes-cotes.md` et `figures/ch01-bayes-cotes.pdf` (paramètres dans `NOTES_01.md`) ;
   - `figures/ch02-cible-monde-action.pdf` (description dans `NOTES_02.md`).
3. **Artefacts du chapitre 4 :**
   - la légende générée de `tbl:ch04-seuil` contient « (sans facteur omis) », notion du chapitre 7 ;
   - dans `figures/ch04-seuil`, l’étiquette « on part si p < p∗ » est placée dans la zone où l’on renonce.
4. **Registre :**
   - la définition de *représentation* dit « d’après laquelle un agent agit » ; proposer « d’après laquelle on décide et l’on agit », comme dans le texte du chapitre 2 ;
   - envisager « agent (logiciel) » pour l’entrée du chapitre 14.
5. **Chapitre 0** (hors de cette passe, à harmoniser lors de sa prochaine révision) :
   - noms des bateaux alignés sur la partie I (« voilier léger » / « voilier renforcé ») : corrigé ;
   - il emploie « agent » au sens courant (l. 23) ;
   - il énonce la règle d’ébullition sous la forme « l’eau bout à 100 °C » (cohérent en soi, mais différent de la forme conditionnelle des chapitres 1 et 2) ;
   - il écrit « le gain d’une victoire », là où le chapitre 4 précise « le gain en cas de succès, mesuré par rapport à l’option sûre ».
6. **Filtre :** les nombres et leurs unités ne sont pas solidaires ; « 101 °C » peut se couper en fin de ligne dans le tableau `tbl:ch02-eau-bouillante`.
7. **Bibliographie (champs `averifier` à compléter) :**
   - `savage1954` est cité au chapitre 3 pour la probabilité personnelle, alors que son champ ne mentionne que l’UES ;
   - `hume1748`, `definetti1974`, `jaynes2003` et `lindley2006` sont cités au chapitre 1 ;
   - `pearl1988` ne vaut que pour l’image du champ de mines ;
   - `gneiting2007` est cité pour l’avantage, sous une règle propre, du prévisionniste qui sépare mieux les cas (repli possible : Bröcker, 2009).

## Références à vérifier dans la partie
Toutes sont des candidates de `biblio_a_verifier.bib` :
- `hume1748`, `definetti1974`, `jaynes2003`, `lindley2006` (chapitres 1 et 3) ;
- `korzybski1933`, `pearl1988`, `pearl2009`, `vovk2005`, `angelopoulos2023`, `mccarthy1969`, `dennett1984` (chapitre 2) ;
- `russell2021`, `savage1954`, `gneiting2007` (chapitres 3 et 4).

S’y ajoute un marqueur en texte libre : Shanahan, *Stanford Encyclopedia of Philosophy* (chapitre 2).
