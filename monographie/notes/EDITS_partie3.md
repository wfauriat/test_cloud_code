# Corrections appliquées : partie 3 (page de partie et chapitres 10 à 13)

Source : relectures « à froid » de Sonnet et d’Opus (`notes/LECTURE_FRAICHE_*`). Une correction n’a été appliquée que si toutes ces conditions étaient réunies :
- le problème était relevé par les deux lecteurs, ou par un seul et vérifié sur le texte ;
- une seule lecture du passage était plausible ;
- la correction restait locale et minimale ;
- le sens, la portée et la force de l’affirmation restaient identiques.

Les autres constats figurent dans `notes/A_TRANCHER_partie3.md`.

Aucune étiquette, clé de citation, formule, aucun nombre, titre de section, bloc `:::`, statut ni renvoi n’a été modifié. Aucun terme du registre n’a été remplacé, ajouté, déplacé ou mis en gras. Le facteur 4,45 et toutes les valeurs de l’exemple quantitatif du ch. 12 sont intacts.

## Récapitulatif

| Fichier | Corrections appliquées | dont relevées par les deux lecteurs | dont relevées par un seul lecteur et vérifiées | dont étendues d’un autre fichier |
| :-- | --: | --: | --: | --: |
| `parties/partie-3.md` | 3 | 2 | 1 | 0 |
| `chapitres/10-couches-basses.md` | 14 | 5 | 9 | 0 |
| `chapitres/11-regle-tiree-des-donnees.md` | 17 | 8 | 9 | 0 |
| `chapitres/12-autre-regime.md` | 14 | 7 | 7 | 0 |
| `chapitres/13-synthese-deux-axes.md` | 10 | 3 | 6 | 1 |
| **Total** | **58** | **25** | **32** | **1** |

Correction appliquée de la même façon dans plusieurs fichiers : suppression du point final après un guillemet fermant, quand la citation se termine déjà par un point d’interrogation (« … ? ». devient « … ? »). La correction a été relevée au ch. 11 (Opus C5) et étendue au ch. 13 (E10), seule autre occurrence du périmètre.

`make verifier` après corrections : 0 erreur. Le seul avertissement (`chapitres/01-outils-logique-probabilite.md` : tableau généré absent, `tableaux/ch01-bayes-cotes.md`) est hors périmètre. Pour le périmètre, on ne trouve que des lignes informatives qui existaient déjà avant les corrections :
- les citations de références candidates (« ? ») ;
- un marqueur `[@A-VERIFIER: …]` au ch. 11, laissé intact.

Le `git diff` des cinq fichiers a été relu : il ne contient que les changements décrits ci-dessous.

---

## `parties/partie-3.md`

**E1.** 1er paragraphe.
- AVANT : « reprend les résultats de la @sec:partie-2 et les porte sur l’empilement des couches logicielles »
- APRÈS : « reprend les résultats de la @sec:partie-2 et les applique à l’empilement des couches logicielles »
- Constats : Sonnet C1 ; Opus C2.
- Justification : « porter sur », au sens de « transposer », est peu idiomatique. Le verbe retenu est celui du chapeau du ch. 10 (« nous appliquons cette grille à l’empilement »).

**E2.** 1er paragraphe.
- AVANT : « Les observations sur les modèles actuels, appelées à vieillir vite, sont datées et présentées comme des études de cas »
- APRÈS : « Les observations sur les modèles actuels, appelées à vieillir vite, sont accompagnées de leur date et présentées comme des études de cas »
- Constat : Opus B1 (vérifié sur le texte).
- Justification : juste après « appelées à vieillir vite », « datées » se lit « dépassées ». Le sens voulu, « elles portent une date », est celui des encadrés `.cas` avec `date="…"`.

**E3.** Paragraphe consacré au chapitre 10.
- AVANT : « Il en va encore ainsi lorsqu’un logiciel produit des résultats faux pendant des mois »
- APRÈS : « Il en va ainsi même lorsqu’un logiciel produit des résultats faux pendant des mois »
- Constats : Opus B3 (ambiguïté de « encore ») ; Sonnet B2 (la phrase se lit presque comme un contre-exemple).
- Justification : « encore » pouvait se lire « de nouveau ». Le sens voulu, « même dans ce cas », est confirmé par le ch. 10. L’ajout de la cause de la perte de la sonde, proposé par les deux lecteurs, n’a pas été fait : il ajouterait une affirmation (voir A_TRANCHER).

---

## `chapitres/10-couches-basses.md`

**E1.** Chapeau, dernière phrase.
- AVANT : « et au fait que chaque défaillance y conserve une adresse — tout en marquant la limite précise où s’arrête cette garantie lorsqu’une règle reste lettre morte. »
- APRÈS : « et au fait que chaque défaillance y conserve une adresse. Il marque aussi la limite précise où s’arrête cette garantie lorsqu’une règle reste lettre morte. »
- Constats : Sonnet C17 ; Opus C1 (phrase d’annonce trop longue).
- Justification : phrase coupée au tiret. Le fond est inchangé ; le gérondif devient une proposition indépendante de même sujet (« ce chapitre »).

**E2.** Encadré `.outils` « Triplets de Hoare et programmation par contrat », dernier paragraphe.
- AVANT : « les étages internes évitent la duplication défensive de contrôles redondants »
- APRÈS : « les étages internes évitent les contrôles défensifs redondants »
- Constats : Sonnet C4 ; Opus C4.
- Justification : « duplication » et « redondants » disaient deux fois la même chose. Le sens et le terme « défensif » sont conservés.

**E3.** § Des opérations élémentaires à la composition, 1er paragraphe.
- AVANT : « additionner deux entiers, comparer deux mots, déplacer une valeur »
- APRÈS : « additionner deux entiers, comparer deux valeurs, déplacer une valeur »
- Constat : Opus C6 (vérifié sur le texte).
- Justification : un non-spécialiste lit « mot » comme un mot de la langue. Le mot machine est une valeur ; le sens technique est conservé.

**E4.** Même phrase.
- AVANT : « sauter à une autre adresse d’instruction selon le résultat d’un test. »
- APRÈS : « sauter à une autre instruction du programme selon le résultat d’un test. »
- Constats : Opus B2 ; Sonnet C7.
- Justification : « adresse », pris ici au sens d’adresse mémoire, entrait en collision avec le terme du registre (adresse d’une défaillance) défini plus loin dans le chapitre.

**E5.** Même section, 3e paragraphe.
- AVANT : « En remontant de la couche matérielle vers un compilateur, […] aucun ingrédient mystérieux n’apparaît en chemin. »
- APRÈS : « Si l’on remonte de la couche matérielle vers un compilateur, […] aucun ingrédient mystérieux n’apparaît en chemin. »
- Constat : Opus C7 (vérifié sur le texte).
- Justification : gérondif mal rattaché, car son sujet n’était pas celui du verbe principal (« aucun ingrédient »).

**E6.** Même section, 4e paragraphe.
- AVANT : « la complexité interne de ce qui se trouve au-dessous devient transparente pour l’étage supérieur. »
- APRÈS : « la complexité interne de ce qui se trouve au-dessous devient invisible pour l’étage supérieur. »
- Constat : Opus B1 (vérifié sur le texte).
- Justification : faux ami du jargon informatique. En français courant, ce qui est transparent se voit à travers, ce qui inverse le sens voulu (« qu’on n’a pas à voir »).

**E7.** Même section, analogie du conteneur.
- AVANT : « l’infrastructure de transport ignore le détail de la cargaison et passe à l’échelle mondiale sans ouvrir les boîtes »
- APRÈS : « l’infrastructure de transport ignore le détail de la cargaison et s’étend à l’échelle mondiale sans ouvrir les boîtes »
- Constats : Sonnet C6 (première partie) ; Opus C8.
- Justification : calque de *scale up*, mal combiné avec « mondiale ». « Pièces de coin », l’autre point du constat de Sonnet C6, est le terme normalisé et reste inchangé.

**E8.** § Vérifier une fois, avant l’usage, liste, 1re puce.
- AVANT : « ou de passer un type `LivreForceSeconde` là où la signature attend un `NewtonSeconde` »
- APRÈS : « ou de passer une valeur de type `LivreForceSeconde` là où la signature attend un `NewtonSeconde` »
- Constat : Opus C11 (première partie, vérifiée sur le texte).
- Justification : on passe une valeur d’un type, non un type. Les noms de type ne changent pas, ni « signature » (glose éventuelle laissée à l’auteur).

**E9.** Même liste, 4e puce.
- AVANT : « comme le déréférencement d’un pointeur nul, le débordement de tableau ou la division par zéro. »
- APRÈS : « comme le déréférencement d’un pointeur nul, le débordement de tableau (deux formes d’accès à une zone de mémoire inexistante ou hors limites) ou la division par zéro. »
- Constats : Opus C13 ; Sonnet B6 (en partie).
- Justification : courte glose de jargon, reprise de la proposition d’Opus. Elle énonce ce que désignent les deux défauts et n’ajoute aucune affirmation. Les autres gloses demandées par Sonnet B6 (« ordre total », « signature ») sont laissées à l’auteur.

**E10.** Même section, paragraphe sur Dijkstra.
- AVANT : « vis-à-vis d’un modèle donné de la machine — et comme l’a établi la @sec:ch02-rigueur-formelle, la rigueur d’une preuve reste elle-même relative au cadre »
- APRÈS : « vis-à-vis d’un modèle donné de la machine. Et, comme l’a établi la @sec:ch02-rigueur-formelle, la rigueur d’une preuve reste elle-même relative au cadre »
- Constat : Opus B7 (vérifié sur le texte).
- Justification : phrase trop dense coupée au tiret. Aucun mot du fond ne change, et le renvoi est conservé.

**E11.** Même section, paragraphe « Pourtant, la limite rappelée par Dijkstra… ».
- AVANT : « En reprenant la grille des cinq conditions du @sec:ch06 (@sec:ch06-cinq-conditions), ce geste résout d’avance »
- APRÈS : « Si l’on reprend la grille des cinq conditions du @sec:ch06 (@sec:ch06-cinq-conditions), ce geste résout d’avance »
- Constat : Opus B6 (seconde partie : gérondif mal rattaché, vérifié sur le texte).
- Justification : ce n’est pas « ce geste » qui reprend la grille. Le rappel de la condition « d’arrivée à temps » et le verbe « saisir » sont laissés à l’auteur.

**E12.** Encadré `.cas` « Le rapport d’enquête sur Mars Climate Orbiter (1999) », 1er paragraphe.
- AVANT : « la cause technique immédiate de l’accident et les facteurs organisationnels qui l’avaient laissée se prolonger »
- APRÈS : « la cause technique immédiate de l’accident et les facteurs organisationnels qui avaient laissé l’erreur se prolonger »
- Constat : Opus B8 (vérifié sur le texte).
- Justification : le pronom « l’ » renvoyait grammaticalement à « la cause technique » ; or ce qui se prolonge, c’est l’erreur. Le référent est désormais explicite.

**E13.** Même encadré, 2e paragraphe.
- AVANT : « au lieu des newton-secondes ($\text{N}\cdot\text{s}$) prescrites par le document de spécification d’interface »
- APRÈS : « au lieu des newton-secondes ($\text{N}\cdot\text{s}$) prescrits par le document de spécification d’interface »
- Constat : Sonnet C11 (vérifié sur le texte).
- Justification : faute d’accord. Les noms d’unités composés prennent le genre de leur premier élément (« le newton-seconde », comme « le newton-mètre »).

**E14.** § Les défaillances ont une adresse, paragraphe « Toutefois, *Mars Climate Orbiter*… ».
- AVANT : « même si le code laisse encore désigner après coup ce qu’il aurait dû faire. »
- APRÈS : « même si le code permet encore de désigner après coup ce qu’il aurait dû faire. »
- Constat : Opus C15 (vérifié sur le texte).
- Justification : tournure « laisser désigner » lourde et peu claire ; le sens est le même.

---

## `chapitres/11-regle-tiree-des-donnees.md`

**E1.** § La spécification passe dans les données, paragraphe « Le prix payé… ».
- AVANT : « rien dans les poids du modèle n’avertit ni ne borne l’écart. »
- APRÈS : « rien dans les poids du modèle (ses paramètres numériques) n’avertit ni ne borne l’écart. »
- Constats : Opus B2 (première partie) ; Sonnet C1 (seconde partie).
- Justification : « poids » apparaît ici pour la première fois, alors que le texte disait « paramètres ». La glose dit qu’il s’agit du même objet. « Hors de l’échantillon » est laissé à l’auteur.

**E2.** Même section, paragraphe « La spécification n’a pourtant pas disparu » (deux occurrences).
- AVANT : « satisfait-elle la postcondition du contrat ? ». Devant » ; « qu’a-t-on laissé hors des données ? ». Comme »
- APRÈS : « satisfait-elle la postcondition du contrat ? » Devant » ; « qu’a-t-on laissé hors des données ? » Comme »
- Constat : Opus C5 (vérifié sur le texte).
- Justification : typographie. Quand la citation finit la phrase sur un point d’interrogation, on ne met pas de point après le guillemet fermant. Correction étendue au ch. 13 (E10).

**E3.** § Le moteur à prédire le fragment suivant, 1er paragraphe.
- AVANT : « appelés *tokens* — mots entiers, racines, syllabes ou caractères isolés selon le découpage statistique retenu —, puis on répète la même épreuve »
- APRÈS : « appelés *tokens* : mots entiers, racines, syllabes ou caractères isolés selon le découpage statistique retenu. On répète ensuite la même épreuve »
- Constat : Opus C7 (seconde partie, vérifiée sur le texte).
- Justification : phrase de cinq étapes et deux incises, coupée après la glose de *tokens*. Le contenu est inchangé.

**E4.** Même section, 2e paragraphe.
- AVANT : « Personne ne saisit dans un tel système les règles de la grammaire »
- APRÈS : « Personne n’inscrit dans un tel système les règles de la grammaire »
- Constats : Opus A1 ; Sonnet C3.
- Justification : « saisir » pouvait se lire « comprendre », ce qui contredit le paragraphe (personne n’entre ces règles dans le système). Les deux lecteurs proposent la même correction.

**E5.** Même section, 3e paragraphe (*logit lens*).
- AVANT : « Sur des modèles ouverts de taille modeste, on peut observer »
- APRÈS : « Sur des modèles ouverts de taille modeste, dont les paramètres sont publics, on peut observer »
- Constat : Sonnet C4 (vérifié sur le texte).
- Justification : « ouverts » est un calque d’*open models* ; la glose dit ce qui permet l’expérience décrite (l’accès aux états internes).

**E6.** Même phrase.
- AVANT : « on peut observer cette structure interne se former étape par étape à travers les couches du réseau. »
- APRÈS : « on peut observer ces régularités s’organiser en une structure interne, étape par étape, à travers les couches du réseau. »
- Constat : Opus B3 (vérifié sur le texte).
- Justification : le démonstratif « cette structure interne » n’avait pas d’antécédent. Le paragraphe précédent parle des « régularités » qui « se déposent dans les paramètres ».

**E7.** Même section, dernier paragraphe.
- AVANT : « sans que rien en lui n’avertisse d’avoir franchi une limite. »
- APRÈS : « sans que rien en lui n’avertisse qu’il a franchi une limite. »
- Constats : Sonnet C5 (première partie) ; Opus C12 (seconde partie).
- Justification : l’infinitif avait pour sujet grammatical « rien », alors que c’est le modèle qui franchit la limite. « Cette genèse » n’a pas été modifié.

**E8.** § Fluide et faux sans enfreindre aucune règle, 2e paragraphe.
- AVANT : « comme celui de *Mars Climate Orbiter* (@sec:ch08, @sec:ch10) délivre un résultat erroné »
- APRÈS : « comme celui de *Mars Climate Orbiter* (@sec:ch08, @sec:ch10) fournit un résultat erroné »
- Constat : Opus C14 (vérifié sur le texte).
- Justification : faux ami (*deliver*). En français, « délivrer » signifie libérer, ou remettre un document officiel.

**E9.** Même section, 3e paragraphe.
- AVANT : « Mais dès que la donnée est rare, l’événement particulier ou la question ambiguë, composer un paragraphe bien charpenté, conforme aux usages du genre et assuré dans son ton demeure une suite hautement probable de la consigne. »
- APRÈS : « Mais dès que la donnée est rare, que l’événement est particulier ou que la question est ambiguë, un paragraphe bien charpenté, conforme aux usages du genre et assuré dans son ton, demeure une suite hautement probable de la consigne. »
- Constats : Sonnet B6 ; Opus B4.
- Justification : verbes manquants rétablis dans la série. Le sujet « composer », un infinitif, ne pouvait pas être une « suite » ; il devient « un paragraphe ». Le sens est inchangé.

**E10.** Même section, 4e paragraphe.
- AVANT : « aucune clause vérifiable en amont n’interdit la fabrication sur la requête suivante. »
- APRÈS : « aucune clause vérifiable en amont n’interdit l’invention sur la requête suivante. »
- Constat : Opus B5 (première partie, vérifiée sur le texte).
- Justification : employé seul, « la fabrication » est un faux ami (*fabrication*, invention mensongère) ; en français, on lit d’abord « production ». « Invention » est le mot de la phrase précédente (« ces inventions »). La question de « requête » face à « consigne » est laissée à l’auteur.

**E11.** Même section, 5e paragraphe.
- AVANT : « la fluidité de la prose est uniforme entre les réponses justes et les réponses fabriquées. »
- APRÈS : « la prose est aussi fluide dans les réponses fabriquées que dans les réponses justes. »
- Constat : Opus C15 (vérifié sur le texte).
- Justification : calque de *uniform across*, remplacé par la comparaison idiomatique de même sens.

**E12.** Même paragraphe.
- AVANT : « la comparaison de plusieurs tirages répétés permet »
- APRÈS : « la comparaison de plusieurs tirages répétés (plusieurs réponses obtenues pour la même consigne) permet »
- Constat : Sonnet B7 (vérifié sur le texte).
- Justification : « tirages » était employé sans explication ; la glose est conforme au ch. 12 (« reposer plusieurs fois la même question »). « Consigne » y est employé dans son sens du registre.

**E13.** Même section, paragraphe après l’encadré *Mata*.
- AVANT : « l’équivalent du programme `SM_FORCES` écrivant des livres-force-secondes »
- APRÈS : « l’équivalent du programme `SM_FORCES` de *Mars Climate Orbiter* écrivant des livres-force-secondes »
- Constats : Sonnet B8 ; Opus B6.
- Justification : le programme n’était rattaché à aucune mission dans le chapitre. Le rattachement est un fait établi au ch. 10.

**E14.** Même section, transition avant l’encadré *Moffatt*.
- AVANT : « est souvent invoqué dans le même souffle comme preuve »
- APRÈS : « est souvent invoqué d’un même souffle comme preuve »
- Constat : Opus C16 (vérifié sur le texte).
- Justification : calque (*in the same breath*) remplacé par la locution française. « Ces affaires », point voisin, est laissé à l’auteur.

**E15.** § Orienter n’est pas spécifier, 1er paragraphe.
- AVANT : « ne laisse pas les modèles tels qu’ils sortent du préentraînement. Elle les entoure »
- APRÈS : « ne laisse pas les modèles tels qu’ils sortent du préentraînement, cet entraînement initial à prédire le fragment suivant. Elle les entoure »
- Constats : Sonnet B10 ; Opus C17 (première partie).
- Justification : le mot apparaît sans avoir été introduit. La glose renvoie à l’étape décrite au § Le moteur à prédire le fragment suivant et n’ajoute rien.

**E16.** Même section, paragraphe suivant l’encadré Goodhart.
- AVANT : « Du côté des tests de référence, optimiser des systèmes pour progresser sur une batterie publique finit par mesurer l’adaptation à la forme particulière de cette batterie »
- APRÈS : « Du côté des tests de référence, quand on optimise des systèmes pour progresser sur une batterie publique, celle-ci finit par mesurer l’adaptation à sa forme particulière »
- Constats : Sonnet B12 (première partie) ; Opus B9.
- Justification : le sujet suspendu est corrigé, puisque c’est la batterie qui mesure, non l’optimisation. « Imprégnation de variantes voisines », qui admet deux lectures, est conservé tel quel et listé.

**E17.** Même section, paragraphe chien et disjoncteur.
- AVANT : « l’on peut éprouver ce déclenchement d’avance contre une tolérance écrite. »
- APRÈS : « l’on peut éprouver ce déclenchement d’avance par rapport à une tolérance écrite. »
- Constats : Sonnet C11 (3e point) ; Opus C21 (seconde partie).
- Justification : calque de *against*. Le verbe « éprouver » est conservé.

---

## `chapitres/12-autre-regime.md`

**E1.** Chapeau.
- AVANT : « trois propriétés basculent ensemble, déplaçant le contrôle vers chaque sortie individuelle, révélant une compétence en dents de scie et obligeant — à la lumière »
- APRÈS : « trois propriétés basculent ensemble (ce qui est promis, la forme de l’échec et le lieu où aboutit l’enquête). Ce basculement déplace le contrôle vers chaque sortie individuelle, révèle une compétence en dents de scie et oblige — à la lumière »
- Constats : Sonnet B1 ; Opus B1.
- Justification : les deux lecteurs prenaient les trois conséquences pour les trois propriétés, et les participes semblaient avoir pour sujet « trois propriétés ». La phrase est coupée et les trois propriétés sont nommées dans les termes mêmes des Points clés. Rien n’est ajouté au fond.

**E2.** § Trois propriétés basculent ensemble, 1er paragraphe.
- AVANT : « ne modifie pas un seul aspect de l’édifice technique. »
- APRÈS : « ne modifie pas seulement un aspect de l’édifice technique. »
- Constat : Opus A1 (vérifié sur le texte).
- Justification : contresens. En français, « ne modifie pas un seul aspect » se lit « n’en modifie aucun », alors que la phrase suivante dit que tout se retourne « d’un même coup ».

**E3.** Même section, point 1.
- AVANT : « sans qu’aucune statistique de série ne garantisse la réponse particulière qui vient d’être émise. »
- APRÈS : « sans qu’aucune statistique établie sur une série d’essais ne garantisse la réponse particulière qui vient d’être émise. »
- Constats : Sonnet B2 ; Opus B2.
- Justification : « statistique de série » n’est pas une expression française. Les deux lecteurs y voient une statistique agrégée sur une série d’essais, ce que confirme le début de la phrase (« fréquence de succès en moyenne sur un test de référence »).

**E4.** Même section, point 3.
- AVANT : « 3. *Le lieu où atterrit l’enquête.* »
- APRÈS : « 3. *Le lieu où aboutit l’enquête.* »
- Constat : Opus C1 (vérifié sur le texte).
- Justification : calque de *lands*. Le verbe est aligné sur la phrase de définition (« l’endroit où aboutit l’enquête ») et sur les Points clés. Il s’agit d’un intitulé de puce, non d’un titre de section.

**E5.** Même point.
- AVANT : « car on ne fusionne pas un correctif local dans une distribution de probabilité. »
- APRÈS : « car on n’applique pas un correctif local à une distribution de probabilité. »
- Constats : Sonnet B3 ; Opus C2.
- Justification : jargon de développeur calqué de *merge a patch*. Les deux lecteurs proposent la même correction.

**E6.** § Vérifier la couche ou contrôler les sorties, 1re puce.
- AVANT : « l’incertitude de la génération reste enfermée dans la proposition de candidat : »
- APRÈS : « l’incertitude de la génération reste enfermée dans l’étape où le modèle propose un candidat : »
- Constat : Opus B5 (vérifié sur le texte).
- Justification : calque obscur (*candidate proposal*), remplacé par une tournure de même sens.

**E7.** Même section, dernier paragraphe.
- AVANT : « l’interface demeure aussi lisse, mais la garantie qui la soutenait en dessous s’est retirée. »
- APRÈS : « l’interface demeure aussi lisse qu’avant, mais la garantie qui la soutenait en dessous s’est retirée. »
- Constats : Sonnet B6 ; Opus C6 (seconde partie).
- Justification : le comparatif appelait un second terme. Les deux lecteurs notent que les comparants possibles (« qu’avant », « qu’en dessous ») donnent le même sens.

**E8.** Encadré `.nuance` « Omission structurelle, omission de saillance et cadre comme cause commune », dernière puce.
- AVANT : « et la même formulation de la consigne — confirmant ainsi la nuance annoncée au @sec:ch07. »
- APRÈS : « et la même formulation de la consigne — ce qui confirme la nuance annoncée au @sec:ch07. »
- Constat : Sonnet C9 (vérifié sur le texte).
- Justification : le participe détaché avait pour sujet grammatical « le volet (a) », qui ne confirme rien ; c’est la restriction énoncée qui confirme la nuance.

**E9.** Même puce.
- AVANT : « Reformuler la question, décomposer le problème ou interroger un autre cheminement »
- APRÈS : « Reformuler la question, décomposer le problème ou emprunter un autre cheminement »
- Constat : Opus C11 (vérifié sur le texte).
- Justification : collocation fautive, car on n’interroge pas un cheminement.

**E10.** § Calibration générative, longue traîne et erreurs constantes, paragraphe avant les deux régimes.
- AVANT : « Il en résulte un contraste décisif entre deux régimes d’erreur dès que l’on tente »
- APRÈS : « Un contraste décisif apparaît entre deux régimes d’erreur dès que l’on tente »
- Constats : Sonnet B15 ; Opus B12.
- Justification : connecteur trompeur. L’opposition entre dispersion et répétition ne découle pas des barèmes décrits au paragraphe précédent. Seul le lien causal est retiré ; le reste de la phrase est inchangé.

**E11.** Même section, 1re puce (« Les erreurs de devinette »).
- AVANT : « (avec une température d’échantillonnage non nulle) »
- APRÈS : « (avec une température d’échantillonnage non nulle, c’est-à-dire en laissant une part de hasard dans le choix de la réponse) »
- Constats : Sonnet B16 ; Opus B16.
- Justification : courte glose d’un jargon dont dépend tout l’exemple quantitatif. Elle dit ce que signifie le réglage sans rien affirmer de plus. La parenthèse de la fin de l’exemple (« ou une température très basse ») s’éclaire du même coup.

**E12.** Encadré `.exemple-quantitatif`, Mise en place (aucun nombre touché).
- AVANT : « le taux d’*alerte à tort* est la probabilité qu’ils divergent sachant que la première réponse était juste. »
- APRÈS : « le taux d’*alerte à tort* est la probabilité qu’ils divergent sachant que la première réponse est juste. »
- Constat : Opus C14 (seconde partie, vérifiée sur le texte).
- Justification : la définition est parallèle à celle de la sévérité, qui la précède immédiatement (« sachant que la première réponse est fausse ») ; le temps est harmonisé. L’écriture des nombres (« 5 » ou « cinq ») est laissée à l’auteur.

**E13.** Même encadré, Calcul, 2e cas (aucun nombre ni formule touchés).
- AVANT : « les quatre autres tirages s’en écartent presque toujours ($1 - 0{,}18^4 \approx 99{,}9\,\%$) »
- APRÈS : « au moins un des quatre autres tirages s’en écarte presque toujours ($1 - 0{,}18^4 \approx 99{,}9\,\%$) »
- Constat : Opus B13 (première partie, vérifiée par le calcul).
- Justification : la formule donne la probabilité qu’*au moins un* tirage s’écarte. La probabilité que les quatre s’écartent vaut $0{,}82^4$, soit environ 45 %, et la phrase était donc fausse à la lettre. La formulation reprend celle du 1er cas (« au moins un des quatre autres tirages »). Le 3e cas, moins net, est laissé à l’auteur.

**E14.** Paragraphe de transition final.
- AVANT : « Le @sec:ch13 va maintenant synthétiser l’appareil épistémologique de la @sec:partie-2 et cette analyse informatique en deux axes de classement des erreurs et quatre sources de comparateurs. »
- APRÈS : « Le @sec:ch13 va maintenant rassembler l’appareil épistémologique de la @sec:partie-2 et cette analyse informatique, pour en tirer deux axes de classement des erreurs et quatre sources de comparateurs. »
- Constats : Opus C18 ; Sonnet B18 (en partie : densité).
- Justification : la construction « synthétiser A et B en C et D » se lisait mal. Le sens est inchangé, et le verbe « rassembler » est celui du chapeau du ch. 13.

---

## `chapitres/13-synthese-deux-axes.md`

**E1.** Chapeau, dernière phrase.
- AVANT : « et poser un problème fidèle au réel avant d’aborder la @sec:partie-4. »
- APRÈS : « et poser un problème fidèle au réel, avant d’aborder la @sec:partie-4. »
- Constat : Opus B13 (seconde partie, vérifiée sur le texte).
- Justification : sans virgule, « avant d’aborder » semblait porter sur « poser un problème ». La virgule le rattache à « Nous détaillons ensuite ». La densité du chapeau est laissée à l’auteur.

**E2.** § Deux axes plutôt que trois sortes d’incertitude, 2e paragraphe.
- AVANT : « Au sommet de la pile, un modèle de langage qui invente une décision de justice — comme dans l’affaire *Mata v. Avianca* (@sec:ch11) [@mata2023] —, échoue sur une variante voisine de sa frontière en dents de scie ou répète une idée reçue (@sec:ch12) ne bute pas nécessairement »
- APRÈS : « Au sommet de la pile, qu’un modèle de langage invente une décision de justice — comme dans l’affaire *Mata v. Avianca* (@sec:ch11) [@mata2023] —, échoue sur une variante voisine de sa frontière en dents de scie ou répète une idée reçue (@sec:ch12), il ne bute pas nécessairement »
- Constats : Opus B11 ; Sonnet C2.
- Justification : le sujet était très long et l’on prenait « échoue » pour le verbe principal. La construction concessive rétablit la structure sans toucher aux mots du fond, aux renvois ni à la citation.

**E3.** Même paragraphe.
- AVANT : « La question porte souvent sur des faits courants »
- APRÈS : « La question posée au modèle porte souvent sur des faits courants »
- Constat : Opus C15 (vérifié sur le texte).
- Justification : « la question » n’avait pas de référent dans la phrase. Le seul plausible est la question soumise au modèle.

**E4.** Même section, 2e puce après le tableau (intitulé en italique).
- AVANT : « *La colonne dépend de ce qui entoure l’affirmation, et peut se concevoir.* »
- APRÈS : « *La colonne dépend de ce qui entoure l’affirmation, et peut être conçue.* »
- Constat : Opus B2 (vérifié sur le texte).
- Justification : « se concevoir » se lit d’abord « est imaginable ». La forme passive est celle des Points clés (« peut être conçue »).

**E5.** Encadré `.formel` « La formalité change la colonne, non la ligne », point 1.
- AVANT : « sa rigueur opère conditionnellement au cadre retenu [@fauriat2026frame]. »
- APRÈS : « sa rigueur reste relative au cadre retenu [@fauriat2026frame]. »
- Constat : Opus C5 (vérifié sur le texte).
- Justification : calque de *conditionally on*. La tournure retenue est celle du ch. 10 (« la rigueur d’une preuve reste elle-même relative au cadre »), et la citation est conservée.

**E6.** Même encadré, point 2.
- AVANT : « D’une part, toute divergence par rapport à cet énoncé sur la ligne du haut peut être mécaniquement signalée »
- APRÈS : « D’une part, sur la ligne du haut, toute divergence par rapport à cet énoncé peut être mécaniquement signalée »
- Constat : Opus C6 (vérifié sur le texte).
- Justification : le rattachement de « sur la ligne du haut » était ambigu (l’énoncé ou la divergence). La parenthèse qui suit (« déplacement de droite à gauche sur la première ligne ») confirme qu’il s’agit de la divergence.

**E7.** § Quatre sources de comparateurs, 1er paragraphe.
- AVANT : « parce qu’en pratique vos propres contrôles personnels et le recours à un autre raisonneur »
- APRÈS : « parce qu’en pratique vos propres contrôles et le recours à un autre raisonneur »
- Constats : Sonnet C6 (seconde partie) ; Opus C8 (première partie).
- Justification : pléonasme. On obtient l’intitulé exact de la source 2 et du tableau. L’alternance entre « nous » et « vous » est laissée à l’auteur.

**E8.** Même section, phrase après le tableau.
- AVANT : « Examinons chacune de ces quatre lignes pour comprendre »
- APRÈS : « Examinons chacune de ces quatre sources pour comprendre »
- Constat : Opus B1 (vérifié sur le texte).
- Justification : dans ce chapitre, « ligne » désigne partout une ligne de la matrice (lieu de la cause). Le mot désignait ici les lignes du second tableau.

**E9.** § Un énoncé fixé à l’avance, 1er paragraphe.
- AVANT : « nul ne sait écrire le contrat d’un réseau de neurones qui résume un contrat d’assurance »
- APRÈS : « nul ne sait écrire le contrat d’un réseau de neurones qui résume une police d’assurance »
- Constats : Sonnet C7 ; Opus C12.
- Justification : « contrat » est un terme du registre (ch. 10). Il revenait ici dans un autre sens dans la même phrase ; « police d’assurance » désigne le même objet.

**E10.** § Vérification et validation, 3e paragraphe (deux occurrences).
- AVANT : « que nous avons posées ? ». La validation demande » ; « pour la décision à prendre ? ». »
- APRÈS : « que nous avons posées ? » La validation demande » ; « pour la décision à prendre ? » »
- Constat : aucun lecteur du ch. 13 ; correction étendue depuis le ch. 11 (Opus C5, E2).
- Justification : même règle typographique (pas de point après le guillemet fermant quand la citation finit sur « ? »). Expression récurrente du périmètre, corrigée partout où elle apparaît.
