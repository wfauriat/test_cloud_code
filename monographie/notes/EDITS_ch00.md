# Corrections appliquées — chapitre 0 (« Cartographier le terrain »)

Fichier modifié : `chapitres/00-cartographier.md`. Sources : `notes/LECTURE_FRAICHE_Sonnet_ch00.md` (Sonnet) et `notes/LECTURE_FRAICHE_Opus_ch00.md` (Opus).

## Récapitulatif

- **19 corrections appliquées**, toutes locales :
  - 3 référents de pronom ou de démonstratif précisés (1, 4, 9) ;
  - 5 calques, termes impropres ou expressions télescopées remplacés par la tournure idiomatique de même sens (3, 10, 12, 15, 17) ;
  - 6 jargons remplacés par leur équivalent courant ou glosés brièvement (2, 5, 6, 8, 11, 16) ;
  - 1 correction typographique, un anglicisme mis en italique (18) ;
  - 4 découpages sans changement de mots : deux listes et deux sauts de paragraphe (7, 13, 14, 19).
- **Constats source** : 13 corrections répondent à un constat relevé par les deux lecteurs ; 6 répondent à un constat relevé par un seul lecteur et vérifié sur le texte (1, 4, 14, 15, 18, 19).
- **Éléments intacts** (vérifiés par comparaison automatique avant/après) : étiquettes, clés de citation, renvois `@sec:`/`@fig:`/`@tbl:`, titres, blocs `:::`, formules et nombres. Seuls les numéros 1 à 5 de la nouvelle liste des cinq conditions ont été ajoutés.
- **Registre** : aucun terme n’a été ajouté, aucun synonyme d’un terme du registre n’a été introduit et aucun terme n’a été mis en gras.
- **Vérification** : `make verifier` donne 0 erreur. Pour le chapitre 0, il ne signale que les citations candidates déjà présentes avant la correction (`mco1999`, `mata2023`, `becker2025`, `ue2015tip`).

---

## 1. Chapeau — référent de « Il »

- **Avant** : « chacun le sera avec précision dans le chapitre qui l’introduit. Il se referme sur l’architecture des cinq parties »
- **Après** : « chacun le sera avec précision dans le chapitre qui l’introduit. Ce chapitre se referme sur l’architecture des cinq parties »
- **Constat** : Opus C1.
- **Justification** : le nom masculin le plus proche est « le chapitre qui l’introduit ». Le sujet visé est le chapitre 0, la seule lecture plausible puisque c’est lui qui se clôt sur l’architecture et les parcours.

## 2. § Toute règle cache un arrière-plan ouvert (`sec:ch00-regle-cadre`) — « sous les rapports retenus »

- **Avant** : « l’induction la certifie *pourvu que* le contexte futur ressemble au contexte passé sous les rapports retenus. »
- **Après** : « l’induction la certifie *pourvu que* le contexte futur ressemble au contexte passé sur les points retenus. »
- **Constat** : Sonnet C4, Opus C9.
- **Justification** : la tournure littéraire est jugée obscure par les deux lecteurs, et le sens est le même. Le changement écarte en outre une collision avec « rapport », mot qui figure dans deux termes du registre (« rapport de vraisemblance », « rapport des enjeux »).

## 3. § Décider une seule fois face à des enjeux asymétriques (`sec:ch00-decider-enjeux`) — « la mise »

- **Avant** : « à la roulette russe, où la perte est sans commune mesure avec la mise, le seuil s’approche de zéro »
- **Après** : « à la roulette russe, où la perte est sans commune mesure avec le gain espéré, le seuil s’approche de zéro »
- **Constat** : Sonnet B4, Opus B3.
- **Justification** :
  - la formule qui précède ne connaît que le gain et la perte, et le seuil ne tend vers zéro que si la perte écrase le gain ;
  - « mise », au sens propre, désignerait ce que l’on engage, c’est-à-dire ici la vie, donc la perte, et la phrase deviendrait absurde ;
  - la seule lecture cohérente est donc celle du gain. « Gain espéré » reprend l’expression employée deux paragraphes plus haut.

## 4. § Décider une seule fois… — référent de « Il »

- **Avant** : « tandis que le monde ne consulte pas ce chiffre. Il répond selon ce qui est, y compris tout ce que le cadre a laissé dans $(\dots)$. »
- **Après** : « tandis que le monde ne consulte pas ce chiffre. Le monde, lui, répond selon ce qui est, y compris tout ce que le cadre a laissé dans $(\dots)$. »
- **Constat** : Opus B4.
- **Justification** : « Il » peut renvoyer à « ce chiffre » ou à « le décideur ». Le titre de la sous-section précédente (« La mer ne consulte pas nos probabilités ») confirme que le sujet est le monde, seule lecture plausible.

## 5. § Ce que mesure — et ce que tait — une barre d’erreur (`sec:ch00-barre-erreur`) — pléonasme et jargon

- **Avant** : « Qu’on l’obtienne en faisant varier des paramètres, en tirant des échantillons par rééchantillonnage ou en confrontant plusieurs sous-modèles »
- **Après** : « Qu’on l’obtienne en faisant varier des paramètres, en rééchantillonnant les données ou en confrontant plusieurs sous-modèles »
- **Constat** : Sonnet B5, Opus C10. Sonnet C12 devient en outre sans objet (voir A_TRANCHER, rejet R16).
- **Justification** :
  - « tirer des échantillons par rééchantillonnage » est redondant, et le sens est inchangé ;
  - « les données » apparaissent désormais avant la mention de « la collecte des données » deux phrases plus loin, ce qui comble le manque de préparation relevé par Sonnet C12.

## 6. Même section — « balayages paramétriques »

- **Avant** : « avec un coefficient de sécurité de 1,8, ses balayages paramétriques explorent l’incertitude aléatoire (la dispersion »
- **Après** : « avec un coefficient de sécurité de 1,8, il explore, en faisant varier systématiquement ses paramètres, l’incertitude aléatoire (la dispersion »
- **Constat** : Sonnet B5, Opus B9.
- **Justification** :
  - le jargon d’ingénierie est remplacé par sa définition courante, que les deux lecteurs proposent presque à l’identique ;
  - la tournure reprend « en faisant varier des paramètres » du paragraphe précédent ;
  - le nombre 1,8 et la parenthèse sont inchangés.

## 7. § Les cinq conditions d’un contrôle (`sec:ch00-cinq-conditions`) — phrase fleuve mise en liste

- **Avant** : « Pour qu’un contrôle arrête une erreur, il faut d’abord qu’un comparateur *existe* (…) ; il faut ensuite que ce comparateur puisse *se tromper autrement* (…) ; il faut que l’affirmation et le comparateur soient *comparables*, (…) ; il faut que le désaccord apparaisse *à temps*, (…) ; il faut enfin une *prise en compte* effective, (…) la décision. Qu’une seule de ces cinq conditions vienne à manquer »
- **Après** :
  - « Pour qu’un contrôle arrête une erreur : » ;
  - puis la liste « 1. il faut d’abord qu’un comparateur *existe* (…) ; 2. il faut ensuite que ce comparateur puisse *se tromper autrement* (…) ; 3. il faut que l’affirmation et le comparateur soient *comparables*, (…) ; 4. il faut que le désaccord apparaisse *à temps*, (…) ; 5. il faut enfin une *prise en compte* effective, (…) la décision. » ;
  - puis un nouveau paragraphe « Qu’une seule de ces cinq conditions vienne à manquer ».
- **Constat** : Sonnet B7, Opus B7.
- **Justification** :
  - la phrase d’environ 130 mots porte le cœur du chapitre, et les deux lecteurs y perdent le compte ;
  - le découpage est fait mot pour mot. Seule la virgule après « une erreur » devient un deux-points d’introduction de liste, et les italiques sont conservés ;
  - la présentation suit celle de la liste des « trois propriétés » plus loin.
  - La seconde moitié de la proposition de Sonnet (supprimer « pour lui ») n’a pas été appliquée (voir rejet R3).

## 8. § Pourquoi l’auto-vérification bute sur le cadre (`sec:ch00-auto-verification`) — « graine aléatoire »

- **Avant** : « refaire tourner une simulation avec une autre graine aléatoire ou vérifier un calcul par éléments finis »
- **Après** : « refaire tourner une simulation avec un autre tirage aléatoire ou vérifier un calcul par éléments finis »
- **Constat** : Sonnet B8, Opus B8 (en partie).
- **Justification** :
  - changer de graine revient à changer de tirage aléatoire, et les deux lecteurs proposent la même tournure ;
  - le reste de la phrase (« éléments finis », « formule analytique », « idéalisations géométriques ») est laissé à l’auteur (A_TRANCHER, T11), car le remplacer ferait perdre de la précision.

## 9. Même section — « cette clôture »

- **Avant** : « Les observations tirées du monde réel échappent en principe à cette clôture, puisque »
- **Après** : « Les observations tirées du monde réel échappent en principe à ce cercle fermé, puisque »
- **Constat** : Sonnet B9, Opus C11.
- **Justification** : le démonstratif n’avait pas d’antécédent, car le mot « clôture » n’avait pas été employé auparavant. Les deux lecteurs proposent la même tournure, qui reprend l’idée du paragraphe précédent (des contrôles qui « puisent tous à la même source »).

## 10. § L’informatique classique a gagné ses garanties… (`sec:ch00-contrats-donnees`) — « une fois pour toutes les exécutions »

- **Avant** : « mais le geste reste le même : on vérifie d’avance, une fois pour toutes les exécutions. »
- **Après** : « mais le geste reste le même : on vérifie d’avance, une seule fois, pour toutes les exécutions. »
- **Constat** : Sonnet C7, Opus C13.
- **Justification** : la phrase télescopait l’expression figée « une fois pour toutes ». La correction suit la proposition d’Opus, la plus minimale. Le sens (une vérification unique, valable pour toutes les exécutions) est inchangé.

## 11. Même section — glose de « fonction de coût »

- **Avant** : « elle a migré dans le choix des données d’entraînement, de la fonction de coût et des préférences d’évaluation, »
- **Après** : « elle a migré dans le choix des données d’entraînement, de la fonction de coût (ce que l’optimisation cherche à réduire) et des préférences d’évaluation, »
- **Constat** : Sonnet B12, Opus B11 (en partie).
- **Justification** :
  - la glose est exacte et n’affirme rien de nouveau ;
  - « optimisation » figure dans le paragraphe précédent ;
  - « préférences d’évaluation » n’est pas glosé, car Sonnet doute de son sens exact (A_TRANCHER, T11).

## 12. § Elle met les étapes en chaîne… (`sec:ch00-auto-chaines`) — « trajectoire »

- **Avant** : « Structurellement, une trajectoire de douze étapes où chacune s’appuie sur le texte produit par la précédente »
- **Après** : « Structurellement, une suite de douze étapes où chacune s’appuie sur le texte produit par la précédente »
- **Constat** : Sonnet C2, Opus C16.
- **Justification** : « trajectoire » est un calque de *trajectory* que relèvent les deux lecteurs. Le sens est inchangé et le mot n’est pas un terme du registre.

## 13. § Elle érode les vérifications humaines (`sec:ch00-auto-erosion`) — saut de paragraphe avant « Plus largement »

- **Avant** : « même chez des experts de leur propre domaine. Plus largement, tant que rédiger une prose claire »
- **Après** : « même chez des experts de leur propre domaine. » + saut de paragraphe + « Plus largement, tant que rédiger une prose claire »
- **Constat** : Sonnet B13, Opus B15.
- **Justification** : un paragraphe de plus de dix lignes enchaînait quatre idées. Le découpage ne change aucun mot.

## 14. Même section — saut de paragraphe avant « Et même lorsqu’un humain relit »

- **Avant** : « deviennent indiscernables au premier coup d’œil. Et même lorsqu’un humain relit le brouillon du modèle »
- **Après** : « deviennent indiscernables au premier coup d’œil. » + saut de paragraphe + « Et même lorsqu’un humain relit le brouillon du modèle »
- **Constat** : Opus B15.
- **Justification** : c’est le second point de coupe proposé par Opus. Le passage sur les pièges de la consigne forme une idée distincte, et aucun mot n’est changé. Le contenu de ce passage reste à trancher (T3).

## 15. § Elle corrèle les angles morts à l’échelle collective (`sec:ch00-auto-correlation`) — « les mêmes quelques »

- **Avant** : « adopte les mêmes quelques modèles de fondation, »
- **Après** : « adopte le même petit nombre de modèles de fondation, »
- **Constat** : Opus B18 (en partie).
- **Justification** : « les mêmes quelques » est un calque de *the same few*. Le terme « modèles de fondation », en usage en français, est conservé ; la question d’une glose est renvoyée à T11.

## 16. § Architecture de l’ouvrage (`sec:ch00-architecture`) — glose de « raisonner à l’envers »

- **Avant** : « l’habitude de raisonner à l’envers et l’impossibilité de juger un prévisionniste sur une seule issue »
- **Après** : « l’habitude de raisonner à l’envers (chercher quelle variation cachée de l’arrière-plan renverserait la conclusion) et l’impossibilité de juger un prévisionniste sur une seule issue »
- **Constat** : Sonnet B23, Opus C17 (« reste vague »).
- **Justification** :
  - la glose reprend la définition du registre (terme introduit en `sec:ch03`). Elle est sans gras ni définition formelle, ce qui respecte le principe du chapitre 0 ;
  - elle s’appuie sur « l’arrière-plan », notion posée plus haut dans ce chapitre ;
  - la glose proposée par Sonnet (« remonter aux causes ») contredit le registre et a été écartée (rejet R6).

## 17. Même section — « dérive le seuil »

- **Avant** : « par l’utilité espérée subjective et dérive le seuil de décision $p^\ast$ face à une décision unique »
- **Après** : « par l’utilité espérée subjective et établit le seuil de décision $p^\ast$ face à une décision unique »
- **Constat** : Sonnet B23 et C2, Opus C17.
- **Justification** : « dériver » est un calque de *derive* ; en français mathématique, il veut dire « calculer la dérivée ». Le symbole et la formule sont inchangés. La question du symbole $p^\ast$, non annoncé, est renvoyée à T14.

## 18. Même section — « pipelines » en italique

- **Avant** : « Le @sec:ch14 examine les pipelines et les agents autonomes »
- **Après** : « Le @sec:ch14 examine les *pipelines* et les agents autonomes »
- **Constat** : Opus C18.
- **Justification** : les conventions (§ 8) veulent qu’un terme anglais conservé soit mis en italique. Choisir entre une glose et un remplacement par « chaînes de traitement » est laissé à l’auteur : un remplacement donnerait « examine les chaînes de traitement […] comme des chaînes ».

## 19. Même section — phrase des exemples récurrents mise en liste

- **Avant** : « qui s’enrichissent à mesure que l’appareil conceptuel progresse : la course de voiliers de M. X et M. Y (chapitres [-@sec:ch03], [-@sec:ch04] et [-@sec:ch17]), l’ébullition de l’eau […], ainsi que les cas documentés portant sur l’usage contemporain des modèles de langage (chapitres [-@sec:ch11], [-@sec:ch12] et [-@sec:ch15]). Comme annoncé dans l’avant-propos, »
- **Après** :
  - « qui s’enrichissent à mesure que l’appareil conceptuel progresse : » ;
  - puis une liste à puces de huit lignes : « - la course de voiliers de M. X et M. Y (chapitres [-@sec:ch03], [-@sec:ch04] et [-@sec:ch17]) ; » … « - ainsi que les cas documentés portant sur l’usage contemporain des modèles de langage (chapitres [-@sec:ch11], [-@sec:ch12] et [-@sec:ch15]). » ;
  - puis un nouveau paragraphe « Comme annoncé dans l’avant-propos, ».
- **Constat** : Sonnet B25 (constat vérifié : une phrase d’environ 150 mots, avec huit éléments et vingt-cinq renvois).
- **Justification** :
  - le découpage se fait sans changer un mot. Les virgules séparant les éléments deviennent des points-virgules de fin de puce ;
  - les renvois et le « 70 % » sont inchangés ;
  - la présence de *Challenger* et le mot « courants » sont renvoyés à T19 et T20.
