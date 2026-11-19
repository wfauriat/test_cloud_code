# Relecture d’ensemble — Partie IV (chapitres 14 à 16)

**Portée.** Relecture et harmonisation de la partie IV telle que produite en premier jet : `parties/partie-4.md` et chapitres 14, 15 et 16. Elle a été conduite contre `authoring_conventions.md` (§ 8, § 11), `content_spec/00_global.md` (§ 1–4, § 7, § 9), `content_spec/part4.md`, `commun/registre_termes.md` et les chapitres 0 et 6 à 13. Les corrections ont été faites en place, sans renommer aucune étiquette. Chaque chapitre en garde la trace en tête de son `NOTES_1N.md` (paragraphe « Révision après relecture »).

**Vérifications.**
- `make verifier` : 0 erreur ; le seul avertissement est hors partie IV (`tableaux/ch01-bayes-cotes.md` manquant au chapitre 1). Tous les nombres des blocs `chain-b` et `escape-b` correspondent aux tableaux générés.
- `make chapitre CH=14`, `CH=15` et `CH=16` se compilent. Les seuls `Overfull \hbox` (< 2 pt) viennent des renvois `??` propres à l’aperçu, et d’un tableau généré au chapitre 16 (0,96 pt).
- `make html` et `make pdf` : `build/livre.html` et `build/livre.pdf` (252 pages) se compilent avec `0 références non définies, 0 statuts manquants`. `build/livre-ecran.pdf` (suivi par git) n’a **pas** été régénéré par cette passe (la partie V est en cours de rédaction dans une autre session, qui l’a peut-être reconstruit entre-temps).
- Inspection de `build/livre.html` sur la partie IV : aucun `??`, aucune `ref-manquante`, aucun renvoi croisé dont l’article ou le genre serait fautif.
- Chaque renvoi (`@sec:`, `@prop:`, `@def:`, `@eq:`, `@fig:`, `@tbl:`) de la partie IV pointe vers une étiquette existante, et vers une section antérieure, à l’exception des annonces prévues vers les chapitres 16, 17 et 18.
- Termes du registre : **agent** (ch. 14), **signe révélateur**, **signal coûteux**, **équilibre mélangeant**, **complaisance** (ch. 15) et **blanchiment de provenance** (ch. 16) sont mis en gras et définis une seule fois, dans leur chapitre. Aucun terme réservé à la partie V (*marge d’humilité*, *bac à sable*, *verrou*, *pré-mortem*, *erreurs injectées*) n’est employé ; les annonces vers les chapitres 17 et 18 passent par des périphrases.

## Constats et corrections, par ordre de gravité

### 1. Exactitude de l’argument
- **Chapitre 16, `.nuance` « Séparer la corrélation des causes et l’usure des alertes » (piège 5).**
  - Le second paragraphe affirmait que le risque ne peut monter, « ou un dispositif jadis protecteur perdre presque toute utilité », que si un autre paramètre bouge. Cela contredisait le premier paragraphe et le `@sec:ch09` : l’usure des alertes suffit à elle seule à rendre le contrôleur décoratif. L’incise a été supprimée.
  - « supprime la quasi-totalité de l’usure due aux fausses alertes » était faux. L’échappement passe de 96,3 % à 81,9 % pour un plancher de 68,0 %, soit environ la moitié de l’usure récupérée. Le texte dit maintenant « réduit nettement l’usure ».
- **Chapitre 16, bloc `escape-b`, dernier paragraphe.**
  - « il suffirait […] d’une corrélation encore plus élevée pour que le risque total augmente » était impossible : à $P(\text{faux}) = 2\,\%$, le risque ne peut dépasser 2 %, contre 5,57 % entre pairs.
  - Le texte dit désormais que c’est l’ampleur de la baisse du taux d’erreur qui décide du sens de la variation, et qu’à corrélation égale une baisse plus modeste suffirait. Vérifié : à 8 % d’erreurs avec $c = 60\,\%$, le risque vaut environ 7,1 %.
- **Chapitre 16, lecture de `escape-b`, première puce.**
  - « Une division par cinq du taux d’erreur peut laisser le contrôleur presque décoratif » attribuait l’effet à la seule baisse du taux d’erreur, alors que le scénario fait aussi monter $c$.
  - La puce nomme désormais les deux mécanismes : la sensibilité tombe de 72 % à 32 % par corrélation, et la VPP de 61,5 % à 11,6 %.
  - La deuxième puce dit « récupère une partie » au lieu de « récupère la part ».
- **Chapitre 14, après l’exemple `chain-b`.** « même cet écart reste calculé dans l’hypothèse idéale où chaque étape sait encore lire… » portait sur la chaîne *sans* contrôle, que l’hypothèse de comparabilité ne concerne pas. La phrase porte maintenant sur le bénéfice des contrôles croisés.
- **Chapitre 14, `#sec:ch14-blanchiment`.** La liste annoncée comme « les deux proches cousins du blanchiment déjà distingués » commençait par l’effacement des *hypothèses*, qui est le blanchiment lui-même ; le `@sec:ch08` nomme comme cousins l’effacement des unités et des définitions, et celui de la provenance. L’annonce et la première puce sont réalignées, et le chapitre 16 nomme désormais les deux cousins dans les mêmes termes que le `@sec:ch08`.
- **Chapitre 15, `#sec:ch15-friction-comparateurs`.** « sa capacité à *se tromper autrement* qu’un écart soudain » était un contresens. Le texte dit maintenant « que le résultat final ».
- **Chapitre 15, `#sec:ch15-bainbridge-consigne`.** « Rapportée au modèle du contrôleur de la `@sec:ch09-severite` » confondait la sévérité et le modèle M1. Le texte dit maintenant « Rapportée au critère de sévérité ».

### 2. Provenance, affirmations empiriques et datation
- Aucune fuite de document interne (vérifié : pas de code de source, d’identifiant de fil ni de mention de version).
- **Affirmations empiriques non citées, adoucies au chapitre 16.**
  - « la quasi-totalité des tests de référence publics et des tableaux de bord internes » est alignée sur la formulation du `@sec:ch09`.
  - « presque aucune organisation ne mesure… » devient « beaucoup plus rarement ».
- **Datation (piège 9).** « les modèles actuels » (ch. 15) devient « les modèles de langage ». « L’ergonome Lisanne Bainbridge » devient « Lisanne Bainbridge », car cette qualification n’est pas vérifiée et n’est pas utile à l’argument.

### 3. Statuts
- La partie IV ne contient aucune `.proposition` ; les propositions réemployées (`@prop:chaines`, `@prop:independance`, `@prop:cause-commune`, `@prop:comparateur`) gardent leur statut d’origine et ne sont jamais présentées comme plus fortes qu’elles ne sont. Au chapitre 16, « La sévérité d’un tel recoupement est nulle » devient « à peu près nulle ».

### 4. Terminologie
- **« historique » :** c’est un terme du registre (`sec:ch03`, *track record*). Au chapitre 14, il désignait le contexte d’un agent (« l’état courant de son historique ») et un journal effacé (« efface un historique »). Le texte dit désormais « tout son contexte accumulé » et « efface des données ». Ses emplois aux chapitres 15 et 16 sont corrects.
- **« vérification croisée »** (ch. 14, `chain-b`) était un synonyme de *contrôle croisé*, terme du registre. Remplacé par « contrôle croisé ».
- **« régime » :**
  - « le système quitte le régime des réponses pour entrer dans celui des actions » (ch. 14) et « quitte le régime des réponses » (page de partie) réemployaient le mot hors du sens de *changement de régime* (`sec:ch12`). Le texte dit maintenant que le système « ne produit plus des réponses, mais des actions ».
  - Le mot « régime » n’apparaît plus dans la partie IV.
- **Nom des cinq conditions :** « *à temps* » (ch. 14) devient « *arrivée à temps* », nom donné au `@sec:ch06`.
- **Renvois plus précis vers le chapitre 13 :** `@sec:ch13-propres-controles` (ch. 15, trois emplois), `@sec:ch13-enonce-avance` et `@sec:ch13-le-monde` (ch. 14), au lieu du renvoi générique `@sec:ch13-quatre-sources`. Au chapitre 14, la réussite des couches basses est désormais formulée avec les termes du `@sec:ch13` : la *vérification* réussit, mais la question de *validation* n’est posée par personne.

### 5. Français
- **Chapeaux :** les trois chapeaux (10 à 15 lignes chacun) sont ramenés à environ six lignes, plus près des « 3 à 5 lignes » des conventions. Le paragraphe final du chapitre 16, qui annonce la partie V, est resserré.
- **Analogie de l’arête et de l’hélicoptère (ch. 15) :** réécrite. Elle contenait « une vue propre sur ses propres chaussures » et « la descente […] ne présente aucune pente ».
- **Tournures :**
  - « tordus » devient « épineux » ; « grimpe à l’approche de » devient « se rapproche de » ;
  - « deux disciplines réunies ensemble » (pléonasme) et « cette double asymétrie » (notion jamais introduite) deviennent « qu’à deux conditions » ;
  - « deviné à demi-mot » devient « deviné » ; le double « contourner » est levé ; le *ne* explétif après « sans que » est supprimé ;
  - « une limite structurale absolue » devient « une limite de principe » ;
  - « Une fois les échanges ouverts » devient « Dès l’ouverture des marchés ».
- **Intensifs :** une quinzaine de « exactement » et « précisément » superflus sont supprimés.

### 6. Typographie
- *pipelines* est mis en italique dans le titre de `#sec:ch14-pipelines`, comme partout ailleurs.

## Page de partie (`parties/partie-4.md`)
Le premier jet (environ 1 000 mots, phrases longues et denses) détonnait avec les pages des parties I à III, que le mainteneur venait de reprendre dans un style plus simple. Il a été réécrit dans ce style : environ 750 mots, un paragraphe d’ouverture, un paragraphe par chapitre, une question de clôture vers la `@sec:partie-5`. Le contenu est inchangé. La page tient sur une page et un tiers dans `livre.pdf`. Les termes du registre y sont employés sans gras ni définition (*pipelines*, agents, signe révélateur, complaisance, contrôle croisé, probabilité d’échappement).

## Choix de vocabulaire communs à la partie (pour la partie V)
- **Termes introduits dans la partie IV :** **agent** (ch. 14) ; **signe révélateur**, **signal coûteux**, **équilibre mélangeant**, **complaisance** (glosé une fois par *sycophancy*) (ch. 15) ; **blanchiment de provenance** (ch. 16).
- **Anglicismes en italique :** *pipeline* (glosé au ch. 14), *sycophancy* (ch. 15), *lemons* (ch. 15, `.outils`).
- **Expressions non enregistrées employées en langue courante :**
  - *effondrement de modèle* (ch. 16, en italique, pour *model collapse*, `@shumailov2024`) ;
  - *ironie de l’automatisation* (ch. 15) ;
  - *divulgation crédible* (ch. 15, `.nuance`) ;
  - « modèles de fondation » (ch. 16, comme au ch. 0).
  
  Aucune n’a besoin d’une entrée au registre, sauf si le chapitre 18 les reprend comme notions techniques.
- **Périphrases réservées aux annonces vers la partie V :**
  - « espaces d’essai sans conséquence extérieure » et « frontières où l’acte doit attendre une autorisation », pour *bac à sable* et *verrou* ;
  - « glisser à dessein des erreurs connues dans la relecture », pour *erreurs injectées*.

## Écarts par rapport à la spec (maintenus)
- Les chiffres des lectures sont donnés à la précision des tableaux générés (7,11 %, 42,2 %, 96,3 %, 68,0 %), et non arrondis comme dans `part4.md` (« about 7 % », « 96 % »), conformément aux conventions (§ 6) et au vérificateur.
- Les *Points clés* comptent cinq puces par chapitre (spec : trois ou quatre), dans la fourchette de 4 à 7 des conventions.
- La `.nuance` du chapitre 16 recoupe largement le second paragraphe de la `.nuance` du `@sec:ch09`, comme la spec le prévoit ; elle se présente désormais comme un prolongement explicite.

## Points à traiter hors des chapitres (mainteneur)
1. **Figure `figures/ch16-modele-partage.pdf` / `.svg` (`scripts/fig_echappement.py`) : mise en page à revoir.**
   - Les deux panneaux de barres n’occupent chacun qu’environ un sixième de la largeur, avec un grand vide au centre.
   - Les barres du panneau « risque » (de 0 à 10 %) sont trop courtes pour être lues.
   - Le titre de ce panneau (« risque : erreurs suivies d’effet ») touche le bord droit de la figure.
   - Piste : répartir la largeur entre les panneaux (`gridspec_kw={'width_ratios': …}`) et réduire l’espace réservé aux étiquettes.
2. **`commun/exemples_courants.md`** reste à compléter : Knight Capital (ch. 14), METR (ch. 0 et 15), les vingt journalistes et la dépêche (ch. 16), *Mars Climate Orbiter* (rappel au ch. 14).
3. **`commun/registre_termes.md`, l. 18 :** la définition de *représentation* emploie encore « un agent agit » au sens courant, alors qu’*agent* a désormais son sens technique au `@sec:ch14`. Déjà signalé dans les relectures des parties I à III.
4. **Partie V en cours :** les chapitres 17 et 18 étaient en rédaction pendant cette relecture. Une fois achevés, il faudra vérifier que les annonces de la partie IV correspondent bien à leur contenu :
   - ch. 14, `#sec:ch14-autorite-garanties` : espaces d’exploration contre frontières d’autorisation ;
   - ch. 15, `.nuance` : historique et erreurs glissées dans la relecture ;
   - ch. 16, `#sec:ch16-taux-echappement` et fin de `#sec:ch16-etranglement-evaluation` : mesure de l’échappement, trois niveaux.
5. **`build/livre-ecran.pdf`** est à régénérer (`make pdf ECRAN=1`) au prochain commit.

## Références à vérifier dans la partie
Toutes les références citées sont des clés candidates de `commun/biblio_a_verifier.bib` ; aucun marqueur `[@A-VERIFIER: …]` en texte libre.
- **Chapitre 14 :** `sec2013knight` (≈ 45 minutes, > 460 millions de dollars, code dormant réactivé), `mco1999`.
- **Chapitre 15 :** `becker2025` (≈ 19 % plus lents mesurés, ≈ 20 % plus rapides estimés ; outils du début de 2025), `spence1973`, `akerlof1970`, `bainbridge1983`, `sharma2023` (entrée signalée comme « ajout suggéré » : auteurs et version publiée à confirmer).
- **Chapitre 16 :** `bliss1995`, `shumailov2024`.
