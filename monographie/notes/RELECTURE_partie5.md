# Relecture d’ensemble — Partie V (chapitres 17 et 18)

**Portée.** Relecture et harmonisation de la partie V telle que produite en premier jet : `parties/partie-5.md`, chapitres 17 et 18, `NOTES_17.md` et `NOTES_18.md`. Elle a été conduite contre `authoring_conventions.md` (§ 8, § 11), `content_spec/00_global.md` (§ 1–4, § 7, § 9), `content_spec/part5.md` (et les « Keys out » de `part4.md`), `commun/registre_termes.md`, l’article de l’auteur (`source/frame_problem_article_WF.tex`, sections *The non-specialist recipient*, *Epistemic humility as structural commitment*, *Implications for practice*) et les chapitres 0, 3, 4, 6 à 9 et 12 à 16. Les corrections ont été faites en place, sans renommer aucune étiquette. Chaque chapitre en garde la trace en tête de son `NOTES_1N.md` (paragraphe « Révision après relecture »).

**Vérifications.**
- `make verifier` : 0 erreur ; le seul avertissement est hors partie V (`tableaux/ch01-bayes-cotes.md` manquant au chapitre 1). Tous les nombres cités dans le bloc `seu-b` figurent dans `tableaux/ch17-scenarios.md` ou `tableaux/ch17-decisions.md`, à leur précision d’affichage (0,100 %, 5,00 %, 8,09 %, 0,0100 %, 16,7 %). L’arithmétique en prose hors bloc (3,85 %, « moins de quatre points », « moins d’un centième de point ») reprend les valeurs de `00_global.md` § 7 et la `.nuance` du `@sec:ch04`.
- `make chapitre CH=17` et `CH=18` se compilent, sans aucun `Overfull \hbox`.
- `make html` et `make pdf` : `build/livre.html` et `build/livre.pdf` (262 pages) se compilent avec `0 références non définies, 0 statuts manquants` (la conclusion, désormais rédigée, est incluse). Aucun `Overfull` dans les pages de la partie V. `build/livre-ecran.pdf` (suivi par git) n’a **pas** été régénéré.
- Inspection de `build/livre.html` sur la partie V : aucun `??`, aucune `ref-manquante`, aucun renvoi dont l’article ou le genre serait fautif (un seul cas trouvé et corrigé, voir § 4).
- Chaque renvoi de la partie V pointe vers une étiquette existante et antérieure, à l’exception des annonces prévues vers le `@sec:ch18` (depuis le chapitre 17) et vers la conclusion.
- Les dix étiquettes des chapitres 17 et 18 que cite la conclusion (`sec:ch17`, `sec:ch17-bacs-a-sable-verrous`, `sec:ch17-quatre-questions`, `sec:ch18`, `sec:ch18-attitude`, `sec:ch18-limite-niveau-1`, `sec:ch18-org-injection`, `sec:ch18-org-statut`, `sec:ch18-placement-qui`, `sec:ch18-placement-rag`) existent toujours. La conclusion parle du « modèle M2 », nom que le chapitre 17 donne désormais explicitement.
- Termes du registre : **marge d’humilité**, **verrou**, **bac à sable** (ch. 17), **pré-mortem** et **erreurs injectées** (ch. 18) sont mis en gras et définis une seule fois, dans leur chapitre ; aucun autre terme n’est en gras. La notation $p_w$ (*risque réel*) est introduite à l’`@eq:ch17-risque-reel`, conformément au registre.
- Aucune `.proposition` dans la partie V ; aucune fuite de document interne (pas de code de source, d’identifiant de fil ni de mention de version).

## Constats et corrections, par ordre de gravité

### 1. Exactitude de l’argument et dépendances

- **Chapitre 17, lecture de `seu-b`, quatrième puce (contradiction avec le modèle M2 et le `@sec:ch04`).**
  - Texte d’origine : « *Une marge interne ne répare pas un cadre aveugle aux ordres de grandeur.* À la *Roulette russe*, le seuil de 0,0100 % ne laisse qu’un écart infime au-dessus de 0,001 %, tandis que le risque réel culmine à 16,7 %. […] seule une règle de prudence extérieure ou un contrôle indépendant empêche d’appuyer sur la détente. »
  - C’est l’inverse de ce que dit le modèle : la décision bascule dès que $b > p^\ast - p$, quel que soit $z$. À la roulette russe, cet écart est inférieur à un centième de point, si bien que la moindre marge renverse la décision ; la `.nuance` du `@sec:ch04` le disait déjà.
  - La puce dit désormais : « *Plus les enjeux sont lourds, plus la marge nécessaire est mince.* […] Le joueur ne tombe dans le piège silencieux que parce qu’il n’en prend aucune ; aucune marge, en revanche, ne lui aurait appris que le barillet était chargé. »
- **Chapitre 17, `#sec:ch17-course-revisitee`, choix de $b$.**
  - « Ajouter une marge $b$ revient à déclarer qu’on ne juge pas l’option sûre à moins qu’elle ne supporte ce recul prudentiel » employait *option sûre*, qui désigne le voilier renforcé, à contresens, et la phrase précédente (« l’écart qui sépare $p$ de $p^\ast$ mesure tout ce qui protège le choix ») restait obscure.
  - Le paragraphe est réécrit : l’écart $p^\ast - p$ indique quelle part de risque ignoré suffirait à renverser la décision (« moins de quatre points de pourcentage pour M. Y, moins d’un centième de point pour le joueur de roulette russe », comme au `@sec:ch04`), et le jugement sur $b$ pèse d’autant plus que les enjeux sont élevés, l’acte irréversible ou la conclusion fragile. Ce sont les trois critères de l’article cité.
- **Chapitre 17, inspection du mât.** « une révision du cadre réussit chaque fois que le contact avec le monde survient *avant* l’acte irréversible » affirmait trop. Le texte rattache maintenant l’épisode à la seconde voie du `@sec:ch07` (*découvrir par l’épreuve*), survenue avant l’acte, « quand changer de bateau ne coûtait presque rien ».
- **Chapitre 17, nom du modèle.** « l’extension complète du modèle M2 introduit au `@sec:ch04` » : le `@sec:ch04` ne nomme pas ce modèle (les chapitres 7 et 8 nomment M3 et M1 dans le titre de leur bloc formel). Le texte dit maintenant « ce modèle, que nous appellerons M2 », et le bloc s’intitule « Modèle M2 : décider avec un facteur omis ». L’hypothèse redondante « (ou dès que $p + b \ge 1$) » est supprimée, puisque $p^\ast < 1$.
- **Chapitre 17, quatre questions.**
  - Question 1 : « Cette question restitue l’arrière-plan $A$ » confondait la condition énoncée $A$ et l’arrière-plan $(\dots)$ de la règle $A \cap (\dots) \to B$ (registre, `sec:ch01`). Corrigé en « l’arrière-plan $(\dots)$ ».
  - Question 4 : « les facteurs $z$ laissés dans l’arrière-plan » assimilait les facteurs écartés *délibérément*, que l’on connaît, au facteur omis $z$, qui par définition échappe au décideur (piège 7). Le $z$ est retiré.
- **Chapitre 17, public de l’avant-propos.** « la majorité des acteurs évoqués dès l’avant-propos (`@sec:avant-propos-public`) — dirigeants, médecins, magistrats, responsables d’exploitation, usagers ou citoyens » : l’avant-propos s’adresse d’abord à des professionnels techniques et nomme, parmi les autres lecteurs, « le décideur ou le responsable d’institution » et « le destinataire non spécialiste ». Le texte reprend ces trois figures.
- **Chapitre 17, cohérence avec le `@sec:ch04`.**
  - Roulette russe : « persuadé que le barillet est vide » devient « persuadé que la chambre placée face au percuteur est vide », comme au `@sec:ch04`.
  - La transition vers la `.nuance` rappelle que le `@sec:ch04` avait déjà écarté la règle « partir si $p_w < p^\ast$ » (`@sec:ch04-question-ouverte`).
  - « la séparation entre croyance et utilités établie par Savage [-@savage1954] au `@sec:ch04` » devient « qu’opère la règle de Savage (`@sec:ch04-ues`) ».
- **Chapitre 17, décision unique.** « Un taux de réussite élevé sur des bancs d’essai antérieurs n’est jamais une promesse pour *cette* instance : un risque de 1 % finit par se réaliser » : la seconde proposition, qui porte sur une série, n’éclairait pas le cas unique. Le texte dit que l’instance « peut tomber parmi les rares échecs, se situer au-delà de la frontière en dents de scie de l’outil ou dépendre d’un facteur $z$ absent des séries passées ».
- **Chapitre 17, `#sec:ch17-bacs-a-sable-verrous`.** La règle de prudence que le `@sec:ch07` (`#sec:ch07-deux-voies`) avait déjà formulée (« explorer là où la réponse du monde est peu coûteuse et réversible… ») est désormais explicitement reprise comme ce que les deux dispositifs mettent en forme. Le premier jet la reformulait sans la citer.
- **Chapitre 18, attente préalable.** « La raison d’être de ce geste tient autant à la comparabilité qu’à la différence » : le geste fait exister un comparateur formé sans le brouillon, donc l’*existence* et la *différence*. Corrigé, avec une réserve (« a de bonnes chances de se tromper autrement »).
- **Chapitre 18, `#sec:ch18-placement-ou`.** « dès qu’une frontière franchit ce périmètre protégé vers une action irréversible ou vers un blanchiment en aval » n’avait pas de sens (une frontière ne franchit rien, et le blanchiment n’est pas une destination). Le texte dit désormais : « Dès qu’un résultat quitte ce périmètre pour devenir une action irréversible, ou une prémisse que l’aval ne remettra plus en cause… »
- **Chapitre 18, mot d’ordre « humain dans la boucle ».** « qui parcourt à la hâte une alerte sur deux dans un outil peu sévère (`@sec:ch09`) » confondait la sévérité (une propriété du contrôle réussi) et la faible valeur prédictive positive, qui est le mécanisme du `@sec:ch09`. Le texte dit : « qui ne lit plus qu’une alerte sur deux d’un contrôleur dont presque toutes les alertes sont fausses ».
- **Chapitre 18, test par mutation (bloc `.cas`).**
  - « DeMillo, Lipton et Sayward ont proposé dès 1978 » affirmait une priorité que la référence ne garantit pas : l’article de 1978 est la référence classique, mais l’idée lui est antérieure. Le texte dit « présenté par… en 1978 ».
  - « un mutant qui survit révèle aussitôt un angle mort » ignorait les mutants équivalents au programme d’origine. Le texte ajoute « à moins qu’il ne se comporte exactement comme l’original », et la sévérité est dite nulle « pour cette faute ».
- **Chapitre 18, élargir les mondes possibles.** « dans l’esprit des diagnostics méthodologiques proposés par ailleurs [@fauriat2026frame] » renvoyait vaguement à l’article. Le texte reprend fidèlement ses trois questions : hypothèse amont différente ; hypothèses que l’on ne peut pas mettre à l’épreuve, même en principe ; barres d’erreur qui auraient ou non signalé les défaillances imaginables.
- **Chapitre 18, articulation des trois niveaux.**
  - « en installant des verrous […] plutôt qu’après exécution ou en noyant le bruit intermédiaire » et « l’utilisateur devient aveugle au premier contact » n’avaient pas de sens clair. Réécrits.
  - **Structure :** `#sec:ch18-articulation`, qui porte sur les trois niveaux, était une sous-section (`###`) du niveau 3. Elle devient une section (`##`). L’étiquette est inchangée ; la numérotation des deux dernières sections se décale (18.4 et 18.5).
- **Chapitre 17, citation étirée.** `bliss1995` était cité pour l’usure de la vigilance devant des demandes d’autorisation bénignes, alors que son champ `averifier` porte sur les alarmes. La citation est retirée ; le texte dit que ces demandes « subissent le sort des alertes presque toujours fausses (`@sec:ch09-comportement-alertes`) ».

### 2. Provenance, affirmations empiriques et attributions
- Aucune fuite de document interne (vérifié par `make verifier` et par recherche des codes de source).
- **Affirmations non citées adoucies (ch. 18).**
  - « une limite économique et psychologique bien documentée [@fauriat2026frame] » : l’article n’est pas une documentation empirique ; le texte parle des incitations, avec la citation pour l’argument seul.
  - « cette mesure directe de l’échappement existe et fonctionne depuis longtemps » devient « est pratiquée depuis longtemps ».
  - « on ignore presque toujours quelle proportion des fautes réelles franchit… » devient « beaucoup plus rarement », comme au `@sec:ch16` après sa relecture.
  - « que les organisations oublient presque toujours » devient « fait souvent oublier » ; « supprime cette prime à l’assurance de façade » devient « réduit » ; « hors des milliards de poids opaques » (ordre de grandeur non cité) devient « hors des paramètres ».
- **Attributions à l’article de l’auteur, restreintes à ce qu’il soutient.**
  - Ch. 18, niveau 3 : « Les trois premières forment des propositions d’architecture institutionnelle […] [@fauriat2026frame] ». L’article soutient la protection de la capacité d’évaluation et l’argument des incitations, non l’affichage du statut ni l’historique. La citation est gardée là où l’article les soutient (`#sec:ch18-org-capacite`, `#sec:ch18-org-statut` pour la pénalité de l’honnêteté), et retirée de la phrase générale.
  - Ch. 17 : les quatre questions, le « transfert de responsabilité déguisé en information », l’« injonction déguisée en information » et le déplacement des questions vers l’institution sont bien dans l’article (section *The non-specialist recipient of expert claims*). La mention « plutôt que d’une norme consacrée par des essais empiriques » est conservée (« non comme une méthode éprouvée par des études empiriques »), conformément à la consigne de `part5.md` sur le degré d’appui.
- **Citations répétées dans un même paragraphe** : `ue2015tip` (trois fois), `demillo1978` (trois fois) et `lewis2020` (deux fois) sont ramenées à une seule occurrence.

### 3. Statuts
- **`@prop:independance` (ch. 18, `#sec:ch18-placement-combien`).** « le long du compromis énoncé par la `@prop:independance` : l’indépendance a un coût » présentait comme acquis ce que `00_global.md` § 3 et le chapitre 8 tiennent pour une *hypothèse de travail*. Le texte dit maintenant : « La `@prop:independance` retient comme hypothèse de travail que l’indépendance a un coût, qui tend à croître avec elle ».
- **`@prop:cause-commune` (ch. 18, `#sec:ch18-limite-niveau-1`).** « une frontière infranchissable établie par la `@prop:cause-commune` » devient « la limite qu’énonce la `@prop:cause-commune` » (*résultat sous hypothèses*).
- **Modèle M2 (ch. 17).** Le statut de $b$ (« ni une mesure ni un estimateur de $z$ ») et le caractère de pratique proposée, non démontrée, sont désormais dits dans le texte principal et pas seulement dans les blocs.

### 4. Terminologie
- **« frontières de changement de régime » (ch. 18, cinq emplois dont un titre ; page de partie, un emploi).**
  - Le registre ne connaît que *changement de régime* (`sec:ch12`), défini comme le basculement simultané, au sommet de la pile, de la promesse, de la forme de l’échec et de l’enquête. Le premier jet détournait ce terme vers une autre notion : l’endroit où une sortie commence à être tenue pour acquise.
  - *Frontière de régime* n’est pas non plus disponible : absente du registre, l’expression est rattachée au `@sec:ch12` par `00_global.md` § 5, et le `@sec:ch12` ne l’emploie pas. Le coordinateur a signalé la même collision pendant la passe.
  - Le mot « régime » disparaît donc de la partie V. `#sec:ch18-placement-ou` s’intitule « Où : aux points de passage vers l’action », en écho à l’annonce du `@sec:ch12` (« placer ces contrôles sur les points de passage critiques »). Le texte rappelle que, pour un composant appris, ce point est celui où « une réponse qu’aucun contrat ne garantit entre dans un dispositif qui exécute, facture, engage ou publie » (`@sec:ch12-couche-sorties`). La puce du niveau 2, la question 4 et les *Points clés* suivent ; la page de partie dit « là où une sortie commence à être tenue pour acquise ».
- **« cadre d’analyse »** (ch. 17, deux emplois : « le cadre d’analyse de ce livre », « ce cadre d’analyse ») employait *cadre*, terme du registre, dans un sens courant. Supprimé.
- **Formes déformées ou non enregistrées :**
  - « une dent de scie de compétence » (ch. 18) devient « au-delà de la frontière en dents de scie » ;
  - « par blanchiment textuel » (ch. 18) devient « ce qui est encore du blanchiment » ;
  - « bancs d’essai antérieurs » (ch. 17, pour des *benchmarks*) devient « tests de référence » ;
  - « qualification vérifiée » (ch. 18) devient « qualification attestée », pour réserver *vérification* au sens du `@sec:ch13`.
- **Nom des conditions :** « *arriver à temps* » (ch. 17) devient « *arrivée à temps* », nom donné au `@sec:ch06`.
- **Notation :** la légende de la `@fig:ch17-decisions` écrivait « $\text{risque réel}/p^\ast$ » ; elle écrit $p_w/p^\ast$.
- ***découvrir par l’épreuve*** est mis en italique, comme au `@sec:ch07`.
- **Renvois plus précis :**
  - `@sec:ch13-propres-controles` au lieu de `@tbl:ch13-sources` et `@sec:ch13-quatre-sources` (ch. 18) ;
  - `@sec:ch07-regression` au lieu de `@sec:ch07` pour la méta-procédure (chapeau du ch. 18) ;
  - `@sec:ch17-calibrer-verrouiller` au lieu de `@sec:ch17` (historique) ;
  - `@sec:ch18-placement-qui` au lieu de `@sec:ch18-placement` (`.nuance`) ;
  - `@sec:ch04-ues` (règle de Savage).
- **Genre :** « Sa limite a déjà été pointée dans la discussion du `@sec:ch15-effondrement-signal` » se rendait en « du section 15.3 ». Corrigé en « à la `@sec:ch15-effondrement-signal` ».

### 5. Français
- **Chapeaux :** celui du chapitre 17 (deux paragraphes, environ quatorze lignes) et celui du chapitre 18 (environ treize lignes) sont ramenés à environ six lignes chacun, comme ceux de la partie IV. Le paragraphe final du chapitre 18, qui récapitulait les cinq parties, est resserré.
- **Calques et tournures :**
  - « un module de recherche va extraire » devient « extrait » ;
  - « si l’agent a licence de réécrire » devient « un agent qui peut réécrire » ;
  - « une revue explicite de feu vert sur chaque sous-système » devient « une revue formelle, sous-système par sous-système, avant toute autorisation » ;
  - « reconnaître une faille de concurrence » devient « repérer un accès concurrent mal protégé » ;
  - « ne brise pas la clôture du prêteur unique » devient « ne fait pas sortir du cercle du prêteur unique » ;
  - « trois illusions symétriques » devient « trois illusions » ; « outil propriétaire » devient « outil particulier » ;
  - « dédoublement irréductible », « vulnérabilité de l’écart » et « à l’exact opposé d’une chaîne de caractères nue » sont réécrits ;
  - « ajourner une coulée de béton » devient « reporter le coulage d’une dalle de béton ».
- **Raisonnement circulaire :** « C’est précisément parce qu’une telle évaluation exige de rapprocher des probabilités annoncées d’une fréquence observée […] que la calibration suppose la répétition pour exister » est réécrit en deux phrases simples.
- **Intensifs :** une vingtaine de « exactement », « précisément », « directement », « strictement » et « la toute première » superflus sont supprimés.
- ***Points clés* :** cinq puces par chapitre, chacune en une phrase. Le chapitre 18 passe de six à cinq puces : les limites des erreurs injectées sont fondues dans la puce sur l’organisation.

### 6. Typographie
- *threat image projection* est mis en bas de casse et en italique, comme les autres termes anglais glosés ; l’abréviation TIP est gardée.
- Les cinq issues du modèle M2 sont en italique et reprennent mot pour mot les libellés des tableaux générés (*départ justifié*, *piège silencieux*, *sauvé par la marge*, *renoncement justifié*, *prudence superflue*).

## Page de partie (`parties/partie-5.md`)
Le premier jet (1 084 mots, cinq phrases de plus de cinquante mots) était le plus long des cinq et détonnait avec les pages des parties I à IV. Il détaillait jusqu’aux limites de chaque pratique (« protéger les tests de contrôle contre toute réécriture », « sans les multiplier sur des actes bénins », etc.). Il a été réécrit dans le style des parties I à IV : environ 570 mots, un paragraphe d’ouverture, un paragraphe par chapitre et une phrase de clôture vers la conclusion. Le contenu essentiel est inchangé ; les détails sont laissés aux chapitres. La page tient sur une page dans `livre.pdf`. Les termes du registre (marge d’humilité, verrou, bac à sable, pré-mortem, erreurs injectées, probabilité d’échappement) y sont employés sans gras ni définition, comme les pages précédentes le font pour leurs propres termes.

## Harmonisation avec le reste du livre
- **Chapitre 0** (`#sec:ch00-remedes`, `#sec:ch00-architecture`) : les quatre questions ont le même libellé, et les trois niveaux le même contenu ; le pré-mortem (« six mois ») et la projection d’images de menaces concordent. Seul écart restant, hors périmètre : « frontières de régime » aux l. 154 et 212 (voir les points ouverts).
- **Chapitre 4** : rapport des enjeux, seuil, estimations et roulette russe sont identiques ; le chapitre 17 reprend désormais l’écart $p^\ast - p$ de la `.nuance` du `@sec:ch04` et la tentation déjà écartée d’une règle sur le « vrai » risque.
- **Chapitre 3** : calibration, historique, bulletin de pluie à 70 % et règles de score strictement propres sont repris sans écart.
- **Chapitres 6 à 9** : noms des cinq conditions, argument $u = 1$ du `@sec:ch09-comportement-alertes`, notation $\Pr(\bar{C} \mid E)$ de l’`@eq:ch09-risque`, statut de la `@prop:independance`.
- **Chapitre 7** : deux voies, règle de prudence, exemples de la ferrure en air sec et de l’automate qui ignore la couleur des fils.
- **Chapitres 12 et 14 à 16** : les annonces faites vers la partie V correspondent désormais au contenu des chapitres 17 et 18. Cela vaut pour le `@sec:ch12` (« points de passage critiques »), pour le `@sec:ch14` (`#sec:ch14-autorite-garanties` : espaces d’essai contre frontières d’autorisation), pour la `.nuance` du `@sec:ch15` (historique et erreurs glissées dans la relecture) et pour le `@sec:ch16` (`#sec:ch16-taux-echappement` et fin de `#sec:ch16-etranglement-evaluation`). Le point 4 de `RELECTURE_partie4.md` est clos.

## Choix de vocabulaire communs à la partie
- **Termes introduits :** **marge d’humilité** ($b$), **verrou**, **bac à sable** (ch. 17) ; **pré-mortem**, **erreurs injectées** (ch. 18). La notation $p_w$, ou *risque réel*, est introduite à l’`@eq:ch17-risque-reel`. Le bloc formel du chapitre 17 nomme le modèle « M2 ».
- **Expressions non enregistrées employées en langue courante :**
  - « points de passage vers l’action » ;
  - « partager l’interface », « comprendre une couche au-dessous » ;
  - « contrôler la sortie », « contrôler la représentation » ;
  - « ancrage documentaire », « génération augmentée par récupération » (*retrieval-augmented generation*, RAG) ;
  - « test par mutation », « mutants » ;
  - « projection d’images de menaces fictives » (TIP) ;
  - « transfert de responsabilité déguisé en information », « injonction déguisée en information ».

  Aucune ne demande d’entrée au registre, sauf si l’auteur souhaite faire de « points de passage vers l’action » une notion technique (voir les points ouverts).

## Écarts par rapport à la spec (maintenus)
- Une seule figure, `ch17-decisions`, réunit la grille des quatre issues et le tracé de $p_w$ contre $p + b$ (déjà signalé dans `NOTES_17.md`).
- Les chiffres de l’exemple `seu-b` sont donnés à la précision des tableaux générés (0,100 %, 5,00 %, 8,09 %), et non arrondis comme dans `00_global.md` § 7.
- Les *Points clés* comptent cinq puces par chapitre (spec : cinq et quatre), dans la fourchette de 4 à 7 des conventions.
- Le pré-mortem n’est attribué à personne : aucune référence n’existe dans les deux fichiers bibliographiques.

## Points ouverts pour l’auteur ou le mainteneur
1. **« frontière de régime ».** `00_global.md` § 5 associe *regime boundary / frontière de régime* au chapitre 12, mais le registre ne l’a pas retenue et le chapitre 12 ne l’emploie pas. Le chapitre 0 l’emploie au sens d’usage (l. 154 : « aux frontières de régime — là où une sortie cesse d’être un brouillon pour devenir un acte ou une référence » ; l. 212 : « du placement des contrôles aux frontières de régime »). Le chapitre 18 dit désormais « aux points de passage vers l’action ». Il est proposé d’aligner le chapitre 0 sur cette formule, ou bien de trancher au registre (entrée au `sec:ch12` avec son sens de pile, ou au `sec:ch18` avec le sens d’usage, puis harmonisation). *Suite donnée :* le chapitre 0 dit désormais « points de passage vers l’action » ; l’expression « frontière de régime » n’apparaît plus dans le livre.
2. **Figures à générer :** `figures/ch18-trois-niveaux.pdf` (spécification détaillée dans `NOTES_18.md`, dont la ligne du niveau 2 est mise à jour). `figures/ch06-cinq-conditions.pdf`, citée par le chapitre 18, est elle aussi encore un emplacement réservé.
3. **Pré-mortem :** une entrée candidate `klein2007` (Gary Klein, *Harvard Business Review*, 2007) est proposée dans `NOTES_18.md`. Elle est à ajouter à `biblio_a_verifier.bib` si l’auteur veut attribuer l’exercice.
4. **Champs `averifier` :**
   - `gneiting2007`, `sutton2018`, `sec2013knight` et `kalai2025` sont désormais cités aussi au chapitre 17, pour les mêmes affirmations qu’aux chapitres 3, 7, 14 et 12 ;
   - `ue2015tip` porte encore « formation des agents » (mot réservé au `@sec:ch14` dans le corps du livre) ;
   - pour `ue2015tip`, restent à vérifier contre le texte réglementaire l’enregistrement par opérateur et le lien entre taux de détection et formation, que le chapitre affirme.
5. **Pratiques générales non citées :** deux phrases du chapitre 17 restent sans référence, bien qu’elles relèvent du savoir commun de l’ingénierie : « L’ingénierie de la sûreté pratique depuis longtemps ces autorisations préalables » et « Le génie logiciel et la sûreté des systèmes pratiquent depuis longtemps cette architecture à deux zones, sous la forme d’environnements cloisonnés et de séparation des privilèges ». L’auteur peut souhaiter une référence (par exemple sur le principe du moindre privilège).
6. **Longueur :** les chapitres 17 et 18 restent un peu plus longs que ceux de la partie IV : environ 5 250 et 5 650 mots, contre 4 300 à 4 700, et treize pages chacun dans `livre.pdf`. Ils restent dans la fourchette de la spec (16 à 20 pages). Le seul doublon assumé est la liste des cinq questions, développée dans le texte puis reprise nue dans le bloc `.question`, comme la spec le demande.
7. **`commun/exemples_courants.md`** reste à compléter : course à la voile, roulette russe et bulletin de pluie (ch. 17) ; dernière apparition de la ferrure (ch. 18) ; projection d’images de menaces (ch. 0 et 18).
8. **`build/livre-ecran.pdf`** est à régénérer (`make pdf ECRAN=1`) au prochain commit.

## Références citées dans la partie
Hors l’article de l’auteur (`fauriat2026frame`, vérifié), toutes les références sont des clés candidates de `commun/biblio_a_verifier.bib`. Aucun marqueur `[@A-VERIFIER: …]` en texte libre.
- **Chapitre 17 :** `savage1954`, `gneiting2007`, `sutton2018`, `sec2013knight`, `kalai2025` (`bliss1995` retiré).
- **Chapitre 18 :** `lewis2020`, `ue2015tip`, `demillo1978`.
