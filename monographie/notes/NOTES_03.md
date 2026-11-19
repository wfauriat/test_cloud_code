# Notes — Chapitre 03

*Révision après relecture (deuxième passe).* Le chapitre a été relu contre `authoring_conventions.md`, `content_spec/00_global.md`, `content_spec/part1.md`, le registre et les chapitres 1, 2 et 4, puis réécrit en conservant toutes ses étiquettes (`sec:ch03`, `sec:ch03-mondes-possibles`, `sec:ch03-raisonner-envers`, `sec:ch03-prevision-previsionniste`, `sec:ch03-calibration-historique`, `fig:ch03-score-log`, `eq:ch03-score-espere`), auxquelles renvoie le chapitre 4. Corrections principales, par ordre de gravité :
- **Contradiction avec le chapitre 1 :** la cohérence devait « interdire d’attribuer la valeur zéro » à une éventualité non exclue. Les axiomes ne l’interdisent pas ; le chapitre 1 parle de prudence, et le chapitre 3 aussi désormais.
- **Affirmation statistique contestable :** « deux personnes partageant la même information […] doivent aboutir aux mêmes probabilités » (thèse de Jaynes, que de Finetti et Lindley ne partagent pas) remplacée par : un écart entre deux jugements n’est pas un caprice, il se localise et se discute.
- **Erreur mathématique :** le bloc formel présentait comme « singulier » le fait que le score logarithmique ne dépende que de la probabilité de l’issue observée. Pour un événement binaire, le score quadratique a la même propriété. Ce trait a été remplacé par l’additivité exacte de la surprise sur des issues indépendantes, propre au score logarithmique. La preuve du minimum passe par le signe de la dérivée (plus simple que la dérivée seconde) ; la dérivée du score quadratique est donnée.
- **Dépendances :**
  - la fin du chapitre paraphrasait presque mot pour mot la définition de *décision unique* (chapitre 4). Elle se limite maintenant à dire que la calibration exige la répétition, avec renvoi au chapitre 17 ;
  - l’annonce que M. X et M. Y feront des choix opposés (résultat clé du chapitre 4) a été retirée ;
  - les renvois en avant non prévus par la spec (chapitres 4 et 12) sont devenus des annonces sans étiquette (« le chapitre suivant », « plus loin »). Seuls restent étiquetés les renvois prévus : la dinde vers le @sec:ch05, calibrer ou protéger vers le @sec:ch17.
- **Arithmétique hors §7 :** le calcul de la dinde (1/0,999 ≈ 1,001 ; 100 matins ≈ 1,11 ; 364 matins ≈ 1,44) introduisait des nombres absents de `00_global.md` §7, et l’expression « au plus 1,001 » était inexacte. L’argument est désormais qualitatif, et le seul nombre employé, 0,999, vient de §7.
- **Exemple quantitatif :** « 6,91 − 3,00 = 3,91 = ln 50 » faisait apparaître un nombre absent du tableau ; le texte dit désormais que l’écart des surprises est le logarithme du rapport, qui vaut 50. Le reste du bloc emploie les valeurs du tableau généré, à la précision affichée. La légende de la figure se comprend sans le texte.
- **Accords des renvois :** « au @sec:ch00-parcours », « au @sec:ch01-probabilite-conditionnelle », « au @sec:ch02-monde-action » donnaient « au section… ». Les sous-sections du chapitre 0 (`sec:ch00-mer-probabilites`, `sec:ch00-regle-cadre`) sont de niveau 3 et se rendent par leur titre (« au La mer ne consulte pas nos probabilités ») : le renvoi porte désormais sur le @sec:ch00. Tous les renvois ont été contrôlés dans un rendu HTML combiné des chapitres 0 à 4 (« la section 1.4 », « le chapitre 1 », « l’équation (2.1) », « le tableau 3.1 et la figure 3.1 »).
- **Terminologie :**
  - le mot *agent* (terme du chapitre 14, au sens d’agent fondé sur un modèle de langage) a été supprimé partout. Le texte dit « celui qui l’énonce », « une personne », « le prévisionniste » ;
  - suppression de *vraisemblance* au sens courant (« avec une écrasante vraisemblance »), réservée au *rapport de vraisemblance* ;
  - suppression de « sensible à » (proche de *sensibilité*, chapitre 9) et de « seuil » au sens décisionnel (chapitre 4) ;
  - suppression de l’anglicisme « évidence statistique » ;
  - les quatre termes du chapitre ne sont plus remis en gras dans les *Points clés*.
- **Rappels au lieu de redéfinitions :** le chapitre ne réaffiche plus la formule de la probabilité conditionnelle, ne redéfinit plus la surprise et reprend la lecture « part des mondes » de la @sec:ch01-probabilite-conditionnelle en la citant.
- **Français :** chapeau ramené de 9 à 6 phrases ; phrases longues scindées ; style nominal et chaînes de deux-points réduits ; formules vagues ou peu idiomatiques réécrites (« exposition au dehors », « la répartition de notre plausibilité », « mondes du centre de la distribution », « pas davantage que M. Y s’il démâte une fois sur mille », « dans trois mondes compatibles sur dix », « ce qui distingue la logique classique… tient à la façon dont chacun traite… »). L’assertion logique d’exemple est désormais « le mât tiendra » (et non la règle d’ébullition, que le chapitre 1 montre fausse sans qualification). Environ 10 % de mots en moins.

## Références à ajouter ou à vérifier
- `[@russell2021]` (clé candidate) — assertions logiques qui excluent des mondes, assertions probabilistes qui pèsent ceux qui restent, `#sec:ch03-mondes-possibles`. Conforme au champ `averifier` : chapitre et page à préciser (4e édition, chapitre « Quantifying Uncertainty »).
- `[@definetti1974]`, `[@jaynes2003]`, `[@lindley2006]` (clés candidates) — probabilité comme jugement ; « subjectif » ne veut pas dire arbitraire, `#sec:ch03-raisonner-envers`. Conforme aux champs `averifier`.
- `[@savage1954]` (clé candidate) — cité au même endroit pour la probabilité personnelle. Le champ `averifier` ne mentionne que l’utilité espérée subjective : y ajouter la probabilité personnelle pour le chapitre 3 (le chapitre ne parle pas d’utilité espérée).
- `[@gneiting2007]` (clé candidate) — définition des règles de score propres et strictement propres ; score logarithmique et score quadratique (de Brier) comme exemples, `#sec:ch03-calibration-historique` et bloc `.formel`. Conforme au champ `averifier`. La phrase « appliquée à toute une série, une telle règle avantage, en moyenne et parmi des prévisionnistes également calibrés, celui qui distingue le mieux les cas » relève de la décomposition calibration–résolution des scores propres : à confirmer dans Gneiting et Raftery (2007), sinon proposer Bröcker (2009), « Reliability, sufficiency, and the decomposition of proper scores », *Quarterly Journal of the Royal Meteorological Society*, 135(643), 1512–1519 (à vérifier).
- `russell1912` n’est pas cité : la dinde n’est ici qu’annoncée (rappel du chapitre 0, développement au chapitre 5, où la référence est prévue).
- Aucun marqueur `[@A-VERIFIER: …]` ; aucune donnée empirique chiffrée (voilier, météorologues à 70 % et à 30 %, dinde : exemples illustratifs).

## Termes proposés (absents du registre)
- Aucun terme nouveau. Les quatre termes du chapitre (**mondes possibles**, **raisonner à l’envers**, **calibration**, **historique**) sont en gras et définis une seule fois. La définition d’**historique** évite *affirmation* (chapitre 6) et parle de « prévisions passées ».
- *propre*, *strictement propre* (règles de score) et *score de Brier* restent en italique ou en clair, faute d’entrée au registre. À ajouter au glossaire si le mainteneur le souhaite : « règle de score strictement propre — *strictly proper scoring rule* — règle de notation des prévisions probabilistes dont la pénalité moyenne attendue n’est minimale que si l’on annonce sa probabilité véritable ».
- *cote* est employé sans définition, comme au chapitre 1 (proposition d’entrée dans `NOTES_01.md`).
- **Notation :** le bloc formel emploie $S(p, y)$ (pénalité d’une règle de score), $q$ (probabilité véritablement jugée) et $\mathbb{E}_q$ (espérance sous ce jugement). $S(p, y)$ étend le $S(p)$ du chapitre 1 ; ces symboles sont locaux au bloc et n’ont pas besoin de la table des notations, sauf choix contraire du mainteneur. $p$ y désigne une probabilité annoncée quelconque, comme au chapitre 1, et non la probabilité d’échec du registre (chapitre 4).
- **Mot *agent* :** le registre réserve *agent* au sens du chapitre 14. Ce chapitre ne l’emploie plus au sens courant. Choix proposés aux autres chapitres : « celui qui l’énonce » ou « celui qui agit », « le prévisionniste », « le décideur », « une personne, une équipe ou une organisation ».

## Paramètres / figures demandés
- Aucun. `figures/ch03-score-log.pdf` / `.svg` et `tableaux/ch03-score-log.md` correspondent aux valeurs de `00_global.md` §7 (3,00 / 6,91 ; 0,051 / 0,001 ; 50 et 0,951). Tous les nombres du bloc `.exemple-quantitatif` figurent dans le tableau généré (`make verifier` : aucun avertissement pour le chapitre).
- Facultatif : si le mainteneur veut chiffrer la lenteur avec laquelle les matins paisibles s’accumulent (risque de 0,1 % par jour : facteur 1/0,999 ≈ 1,001 par matin, ≈ 1,11 après 100 matins, ≈ 1,44 après 364), il faudrait ajouter ces valeurs à `00_global.md` §7 et à l’annexe D. Le chapitre s’en passe pour l’instant.

## Écarts par rapport à la spec
- **Renvois en avant :** la spec ne prévoit que la dinde (chapitre 5) et « calibrer ou protéger » (chapitre 17). Deux annonces sans étiquette sont conservées :
  - la transition finale vers « le chapitre suivant » (la décision) ;
  - la mise en garde « un second sens [de calibration], propre aux modèles génératifs, apparaîtra plus loin ». Elle est justifiée par l’intitulé « *Calibration (first sense)* » de la spec et par l’écueil 8 de `00_global.md` §9.
- **Calibration seule insuffisante :** le paragraphe du météorologue qui annonce toujours 30 % (calibré mais inutile) n’est pas dans la spec. Il est conservé parce qu’il explique pourquoi il faut des règles strictement propres, et non la seule calibration.
- **Lien entre surprise et rapport de vraisemblance :** comme au chapitre 1, l’écart des surprises est le *logarithme* du rapport de vraisemblance (la spec parle de « *ratio of surprises* »).
- Le titre du bloc `.exemple-quantitatif` devient « Ce qu’une seule course dit de deux prévisions » (le titre n’est pas une étiquette).

## Incohérences repérées ailleurs
- Figures étirées dans les blocs (absence de `keepaspectratio`) : corrigé dans `gabarit/pdf.yaml` (`graphics: true`) ; voir `RELECTURE_partie1.md`.
- `commun/biblio_a_verifier.bib`, entrée `savage1954` : ajouter « probabilité personnelle (ch. 3) » au champ `averifier`.
- `commun/exemples_courants.md` : toujours vide. Exemples du chapitre 3 à y consigner : voilier léger de M. X (5 %) et M. Y (0,1 %) ; prévision de pluie à 70 % (et le météorologue à 30 % constant) ; dinde inductiviste (annoncée).
- **Pour la passe de cohérence de la Partie I :**
  - dénominations : le chapitre 3 emploie « voilier léger » (comme les chapitres 2 et 4 ; le chapitre 0 dit « voilier allégé »), « course au large », « quai », « M. X » / « M. Y », et l’événement « le bateau casse » / « tient » (comme le tableau généré) ;
  - les chapitres 1, 2 et 4 n’emploient plus « agent » ; mais la définition de *représentation* dans le registre dit encore « d’après laquelle un agent agit » (voir `NOTES_01.md`), et le glossaire généré la reprendra ;
  - le chapitre 4 dit « une issue isolée ne juge pas mieux une décision qu’elle ne jugeait une prévision au @sec:ch03 » : cohérent avec la formulation retenue ici (« une issue isolée juge mal une prévision ») ;
  - le chapitre 0 (`sec:ch00-mer-probabilites`) dit déjà, en aperçu, l’essentiel de la section `sec:ch03-prevision-previsionniste` ; pas de contradiction.
