# Corrections appliquées : partie 4 (page de partie et chapitres 14 à 16)

Source : relectures « à froid » de Sonnet et d’Opus (`notes/LECTURE_FRAICHE_*`). Une correction n’a été appliquée que si le problème était relevé par les deux lecteurs, ou par un seul et vérifié sur le texte ; si une seule lecture du passage était plausible ; si la correction était locale et minimale ; et si le sens, la portée et la force de l’affirmation restaient identiques. Les autres constats figurent dans `notes/A_TRANCHER_partie4.md`.

Aucune étiquette, clé de citation, formule, aucun nombre, titre, bloc `:::`, statut ni renvoi n’a été modifié. Aucun terme du registre n’a été remplacé par un synonyme ni mis en gras ; une correction (« prise en compte des alertes ») rétablit au contraire le terme du registre là où un synonyme s’était glissé.

## Récapitulatif

| Fichier | Corrections appliquées | dont relevées par les deux lecteurs | dont relevées par un seul lecteur et vérifiées | dont appliquées par cohérence avec un autre fichier |
| :-- | --: | --: | --: | --: |
| `parties/partie-4.md` | 1 | 0 | 0 | 1 |
| `chapitres/14-chaines-qui-agissent.md` | 7 | 5 | 2 | 0 |
| `chapitres/15-erosion-verifications.md` | 8 | 5 | 3 | 0 |
| `chapitres/16-angles-morts-collectifs.md` | 8 | 7 | 1 | 0 |
| **Total** | **24** | **17** | **6** | **1** |

Correction appliquée de la même façon dans plusieurs fichiers : « l’écoute des alertes » devient « la prise en compte des alertes » (ch. 16, E8, Points clés ; partie 4, E1), ce qui aligne ces deux passages sur le terme du registre (prise en compte, notation $u$) employé dans le corps du ch. 16.

`make verifier` après corrections : 0 erreur. Le seul avertissement du rapport (`chapitres/01-outils-logique-probabilite.md` : tableau généré absent) est hors périmètre. Les lignes du périmètre ne concernent que des citations de références candidates (`sec2013knight`, `mco1999`, `becker2025`, `spence1973`, `akerlof1970`, `bainbridge1983`, `sharma2023`, `bliss1995`, `shumailov2024`), déjà présentes avant les corrections ; aucune ligne n’a changé de numéro (aucune coupure de paragraphe).

---

## `parties/partie-4.md`

**E1.** Paragraphe consacré au chapitre 16.
- AVANT : « rendre le contrôleur plus précis rétablit l’écoute des alertes, mais seul un comparateur qui se trompe autrement »
- APRÈS : « rendre le contrôleur plus précis rétablit la prise en compte des alertes, mais seul un comparateur qui se trompe autrement »
- Constats : non relevé par les lecteurs de la partie 4 ; appliqué par cohérence avec le ch. 16, E8 (Sonnet ch16 C11 ; Opus ch16 C13).
- Justification : « écoute des alertes » désigne la grandeur $u$, que le registre nomme « prise en compte » (« proportion des alertes suivies d’effet ») ; le ch. 16 l’appelle ainsi dans son corps. Même correction qu’aux Points clés du ch. 16, dont cette phrase est le résumé.

---

## `chapitres/14-chaines-qui-agissent.md`

**E1.** Chapeau.
- AVANT : « Pour le dire, ce chapitre reprend deux acquis du @sec:ch08 »
- APRÈS : « Pour y répondre, ce chapitre reprend deux acquis du @sec:ch08 »
- Constats : Sonnet B1 ; Opus B1.
- Justification : « le » n’avait pas de référent ; la phrase précédente est une question (« Que se passe-t-il lorsque… ? »), à laquelle « y » renvoie. Les deux lecteurs proposent la même tournure.

**E2.** Chapeau, même phrase.
- AVANT : « une chaîne cumule les angles morts, quand un contrôle croisé n’en garde que la part commune »
- APRÈS : « une chaîne cumule les angles morts, alors qu’un contrôle croisé n’en garde que la part commune »
- Constats : Opus B1 ; Sonnet B2 (sa reformulation emploie aussi « alors qu’ »).
- Justification : « quand » pouvait se lire comme temporel ; seule la lecture adversative a un sens (chaîne et contrôle croisé sont deux compositions différentes). Le reste de Sonnet B2 (couper le chapeau) est rejeté (voir A_TRANCHER).

**E3.** § Des *pipelines* d’IA comme chaînes orchestrées, analogie de la chaîne de montage.
- AVANT : « Sur une ligne d’assemblage, chaque poste »
- APRÈS : « Sur une ligne d’assemblage automobile, chaque poste »
- Constats : Sonnet C4 ; Opus C2.
- Justification : la phrase suivante parle de « la route qu’il va emprunter » sans avoir nommé de véhicule. L’adjectif ne fait qu’expliciter ce que la route impliquait ; la proposition d’Opus est retenue parce qu’elle laisse intacte la phrase sur la route.

**E4.** § Un danger opérationnel : des réponses aux actions, 1er paragraphe.
- AVANT : « s’interpose au moins le temps de lecture et la décision de l’utilisateur. »
- APRÈS : « s’interposent au moins le temps de lecture et la décision de l’utilisateur. »
- Constat : Sonnet C3 (vérifié : sujet inversé, double, coordonné par « et »).
- Justification : accord du verbe avec un sujet pluriel.

**E5.** Même section, paragraphe qui suit l’encadré Knight Capital.
- AVANT : « mais du moins n’y frappait-elle que des programmes dont quelqu’un avait écrit les règles »
- APRÈS : « mais du moins n’y concernait-elle que des programmes dont quelqu’un avait écrit les règles »
- Constat : Opus C14 (vérifié : le sujet est « la vitesse d’exécution », qui ne « frappe » pas des programmes).
- Justification : impropriété lexicale ; le sens (le phénomène ne touchait que des programmes spécifiés) est inchangé.

**E6.** § Le blanchiment dans les chaînes d’IA, 1er paragraphe (Mars Climate Orbiter).
- AVANT : « des impulsions dépourvues de mention d’unité, effaçant l’écart entre livres-force-secondes et newton-secondes [@mco1999] »
- APRÈS : « des impulsions dépourvues de mention d’unité, effaçant la distinction entre livres-force-secondes et newton-secondes [@mco1999] »
- Constats : Sonnet A1 ; Opus C15.
- Justification : « effacer l’écart » pouvait se lire « supprimer la différence » (contresens) ; ce qui est effacé, c’est la distinction des unités, l’écart numérique demeurant. Le verbe de l’auteur, qui fait écho à « l’effacement » des hypothèses plus loin, est conservé (proposition d’Opus) ; « masquant l’écart » (Sonnet) n’est pas repris.

**E7.** § Autorité d’exécution et garanties inversées, 1re phrase.
- AVANT : « Rassemblons maintenant la vue d’ensemble de l’édifice logiciel tracée dans la @sec:partie-3 et ce que l’enchaînement des étapes dans un agent vient y déplacer. »
- APRÈS : « Reprenons maintenant la vue d’ensemble de l’édifice logiciel tracée dans la @sec:partie-3, et voyons ce que l’enchaînement des étapes dans un agent vient y déplacer. »
- Constats : Sonnet C11 ; Opus C10.
- Justification : le verbe régissait deux compléments hétérogènes (zeugme). « Reprenons » est proposé par les deux lecteurs ; « voyons » (Sonnet) rétablit un verbe pour le second complément, sans toucher à la suite.

---

## `chapitres/15-erosion-verifications.md`

**E1.** § La friction fabriquait des comparateurs, paragraphe « Rapportée aux cinq conditions… ».
- AVANT : « C’est cette deuxième source de comparateurs que le @tbl:ch13-sources nomme « vos propres contrôles » (@sec:ch13-propres-controles). »
- APRÈS : « C’est cette source de comparateurs que le @tbl:ch13-sources nomme, en deuxième position, « vos propres contrôles » (@sec:ch13-propres-controles). »
- Constats : Sonnet B2 ; Opus B1.
- Justification : « deuxième » faisait chercher une première source dans le chapitre, ou se rapporter à la deuxième puce. Vérifié au ch. 13 (lecture seule) : « Vos propres contrôles » est bien la deuxième des sources de la liste et la deuxième ligne du @tbl:ch13-sources. Le rang est conservé, mais rattaché explicitement au tableau (lecture d’Opus) ; aucun nombre n’est ajouté.

**E2.** § La perte du signe révélateur, 3e paragraphe.
- AVANT : « pas plus que l’assurance d’un orateur ne prouve qu’elle soit juste. »
- APRÈS : « pas plus que l’assurance d’un orateur ne prouve que l’affirmation soit juste. »
- Constat : Sonnet C5 (vérifié : « elle » se rattachait grammaticalement à « assurance »).
- Justification : pronom au référent flou ; le référent voulu (l’affirmation) est rétabli.

**E3.** § La friction fabriquait des comparateurs, image de l’alpiniste, dernière phrase.
- AVANT : « la génération instantanée dépose le lecteur au bout du chemin »
- APRÈS : « la génération instantanée dépose l’analyste au bout du chemin »
- Constats : Sonnet C4 (première partie) ; Opus C3.
- Justification : dans un livre, « le lecteur » se lit d’abord comme le lecteur de l’ouvrage ; la personne visée est celle qui reçoit le résultat généré, que la section appelle « l’analyste ». Sonnet propose « l’analyste », Opus « l’utilisateur » ; « l’analyste » est le mot de la section. « Antécime » (seconde partie de Sonnet C4) est conservé.

**E4.** § La forme ne signale plus le fond, définition en gras de « signal coûteux ».
- AVANT : « un indice observable qui reste crédible parce qu’il coûte cher à produire — en temps, en effort ou en maîtrise — lorsqu’on ne possède pas la qualité signalée, si bien qu’il perd sa valeur de tri »
- APRÈS : « un indice observable qui reste crédible parce qu’il coûte cher à produire — en temps, en effort ou en maîtrise — à qui ne possède pas la qualité signalée, si bien qu’il perd sa valeur de tri »
- Constats : Sonnet B10 ; Opus B8.
- Justification : la condition essentielle, rejetée après l’incise, se lisait d’abord comme une circonstance (« lorsque »). « À qui » la rattache au coût, sans changer le sens. La définition reste en gras, au même endroit, avec les mêmes éléments ; le découpage en deux phrases, proposé par les deux lecteurs, n’est pas appliqué, pour ne pas remanier la phrase de définition.

**E5.** Même section, paragraphe « Avec les modèles génératifs… ».
- AVANT : « la sévérité de la belle forme contre une affirmation infondée est tombée près de zéro »
- APRÈS : « la sévérité de la belle forme contre une affirmation infondée est tombée à près de zéro »
- Constat : Opus C9 (vérifié).
- Justification : préposition manquante dans la locution « tomber à près de ». Le reste de la phrase, signalé par Sonnet B9, est laissé à l’auteur.

**E6.** Encadré `.outils` « Signaux coûteux et marché des véhicules d’occasion », point 1.
- AVANT : « l’équilibre séparateur s’effondre et tous les types émettent le même signal. »
- APRÈS : « l’équilibre séparateur s’effondre et tous les types (c’est-à-dire tous les niveaux de qualité) émettent le même signal. »
- Constats : Sonnet C7 ; Opus B10.
- Justification : « types », au sens de la théorie des signaux, n’était pas défini. La glose reprend les mots de la même phrase (« séparer les niveaux de qualité ») et n’ajoute aucune affirmation. « Équilibre séparateur » se comprend par opposition à « équilibre mélangeant » et n’est pas glosé.

**E7.** Encadré `.nuance` « Sortir du mélange par une divulgation crédible », dernière phrase.
- AVANT : « la mention de conformité se mêle au bruit de surface au lieu de l’ordonner. »
- APRÈS : « la mention de conformité se mêle au bruit de surface au lieu d’y mettre de l’ordre. »
- Constats : Sonnet C8 ; Opus C12.
- Justification : « ordonner » se lisait aussi « commander » ; le sens voulu est « mettre en ordre », que la tournure retient sans ambiguïté. Les deux lecteurs proposaient « trier », qui ajoutait un objet (« les productions ») ; la correction garde le seul sens du verbe.

**E8.** § L’ironie de Bainbridge et les deux pièges de la consigne, second piège.
- AVANT : « optimisés pour ce score, les modèles apprennent à exploiter ce biais d’approbation. »
- APRÈS : « optimisés pour être ainsi préférés, les modèles apprennent à exploiter ce biais d’approbation. »
- Constat : Sonnet B17 (vérifié : aucun « score » n’est nommé auparavant ; la phrase parle de réponses que des évaluateurs « tendent à préférer »).
- Justification : démonstratif sans antécédent ; « ainsi préférés » renvoie à la préférence décrite juste avant, sans rien ajouter sur le mécanisme d’ajustement.

---

## `chapitres/16-angles-morts-collectifs.md`

**E1.** § Le taux d’erreur baisse, la probabilité d’échappement monte, 4e paragraphe (« Mais le mouvement s’inverse… »).
- AVANT : « la sensibilité $s = (1 - c)(1 - m)$ s’effondre et la probabilité d’échappement augmente. »
- APRÈS : « la sensibilité $s = (1 - c)(1 - m)$, où $m$ est le taux d’oubli sur les autres causes, s’effondre et la probabilité d’échappement augmente. »
- Constats : Sonnet B1 ; Opus B1 (première partie).
- Justification : $m$ figurait dans une formule du texte principal avant d’être nommé dans l’encadré. La glose reprend mot pour mot l’expression de la mise en place de l’encadré (« taux d’oubli $m$ sur les autres causes ») et la notation du registre ; la formule est inchangée. La glose proposée pour $u$ (Opus B1, seconde partie) ajoutait une cause (« les erreurs devenant rares ») et n’est pas reprise.

**E2.** Encadré `.exemple-quantitatif`, Mise en place.
- AVANT : « l’appariement des probabilités ($u = \mathrm{VPP}$) et l’examen systématique de chaque alerte »
- APRÈS : « l’appariement des probabilités ($u = \mathrm{VPP}$, VPP désignant la valeur prédictive positive) et l’examen systématique de chaque alerte »
- Constats : Sonnet B1 ; Opus B2 (première partie).
- Justification : le sigle, à sa première occurrence dans le chapitre, n’était développé qu’aux Points clés. Le développement reprend le terme du registre ; aucun nombre ni aucune formule n’est touché. Les gloses de l’appariement et de $B_{\text{cmp}}$ ne sont pas ajoutées (voir A_TRANCHER).

**E3.** § Un même prêteur pour tous les emprunteurs, 2e paragraphe.
- AVANT : « industrialise la voie qui consiste à *être averti* en un réservoir unique »
- APRÈS : « industrialise la voie qui consiste à *être averti* en la concentrant dans un réservoir unique »
- Constats : Sonnet B7 ; Opus B10.
- Justification : « industrialiser X en un réservoir » ne se construit pas ; les deux lecteurs restituent le même verbe sous-entendu. La phrase suivante (« il condense en un seul jeu de paramètres ») confirme le sens.

**E4.** Même section, 3e paragraphe.
- AVANT : « une piste classique de la littérature qu’il ignorait. »
- APRÈS : « une piste classique de la littérature que celui-ci ignorait. »
- Constat : Opus C6 (vérifié : le « il » précédent, sujet de la principale, est « l’emprunt »).
- Justification : deux « il » consécutifs à référents différents ; « celui-ci » désigne l’emprunteur, dernier nom masculin cité.

**E5.** § L’étranglement institutionnel de l’évaluation, 2e paragraphe.
- AVANT : « produire des réponses plausibles, fluides et mises en forme coûte presque zéro ; »
- APRÈS : « produire des réponses plausibles, fluides et mises en forme ne coûte presque rien ; »
- Constats : Sonnet C9 (seconde partie) ; Opus C11 (première partie).
- Justification : tour oral et calqué ; la tournure retenue est celle de la partie 4 (« ne coûte presque plus rien ») et des ch. 13 et 18. La première partie de Sonnet C9 (« goulet… retourné ») est rejetée.

**E6.** Même section, 3e paragraphe.
- AVANT : « les directions et les arbitrages budgétaires sont fortement incités à réallouer crédits, postes et attention »
- APRÈS : « les directions sont fortement incitées, dans leurs arbitrages budgétaires, à réallouer crédits, postes et attention »
- Constats : Sonnet C10 ; Opus C11 (seconde partie).
- Justification : zeugme (des arbitrages ne sont pas « incités ») ; reformulation commune aux deux lecteurs, mêmes mots.

**E7.** Même section, paragraphe de clôture de la partie.
- AVANT : « Ce constat referme l’enquête de la @sec:partie-4 sur ce que l’automatisation fait à nos contrôles. Elle les *enchaîne* d’abord »
- APRÈS : « Ce constat referme l’enquête de la @sec:partie-4 sur ce que l’automatisation fait à nos contrôles. L’automatisation les *enchaîne* d’abord »
- Constats : Sonnet B18 ; Opus B14.
- Justification : « Elle » se lisait d’abord comme « l’enquête » ; le sujet voulu est rétabli. Les « elle » suivants sont alors sans ambiguïté.

**E8.** Points clés, 3e point.
- AVANT : « restaure la valeur prédictive positive et l’écoute des alertes »
- APRÈS : « restaure la valeur prédictive positive et la prise en compte des alertes »
- Constats : Sonnet C11 ; Opus C13.
- Justification : « écoute » est un synonyme non technique de la grandeur $u$, que le corps du chapitre et le registre nomment « prise en compte ». (Même correction dans la partie 4, E1.)
