# Relecture d’ensemble — Partie II (chapitres 5 à 9)

**Portée.** Les chapitres 5, 6, 7, 8 et 9 ont été relus et corrigés un à un contre `authoring_conventions.md` (§ 11), `content_spec/00_global.md`, `content_spec/part2.md`, `monographie/commun/registre_termes.md` et les parties 0 et I ; chaque relecture est consignée en tête du fichier `NOTES_0N.md` correspondant (paragraphe « Révision après relecture (deuxième passe) »). La présente passe relit la partie II comme un tout (`parties/partie-2.md` et chapitres 5 à 9), afin d’assurer la cohérence des exemples courants, du vocabulaire, des notations, des renvois croisés et de la lisibilité du français.

**Vérifications.**
- `make verifier` : 0 erreur ; 1 avertissement (tableau généré `tableaux/ch01-bayes-cotes.md` manquant, hors partie II) ; 0 avertissement dans les chapitres 5 à 9 ; 1 marqueur libre `[@A-VERIFIER: …]` au chapitre 5 et 42 citations de clés candidates (`biblio_a_verifier.bib`) dans les chapitres 5 à 9.
- `make chapitre CH=05` à `CH=09` : les cinq aperçus (PDF et HTML) se compilent sans erreur.
- `make pdf`, `make pdf ECRAN=1` et `make html` : `build/livre.pdf` (149 pages), `build/livre-ecran.pdf` (147 pages) et `build/livre.html` se compilent sans erreur LaTeX ni référence non définie. Le préambule de la partie II (`parties/partie-2.md`) tient exactement sur une page dans les deux éditions PDF (p. 70 de `livre.pdf`, p. 68 de `livre-ecran.pdf`).
- Inspection de `build/livre.html` sur les parties 0 à II : aucune référence manquante (`ref-manquante`), aucune occurrence de `??`, et tous les renvois croisés portent l’article et le genre français corrects (« la section », « le chapitre », « l’équation », « la proposition », « la définition », « la figure », « le tableau »).
- Aucun terme du registre n’est employé avant son chapitre d’introduction. Chaque terme attribué à la partie II est mis en gras et défini une seule fois, dans son chapitre d’introduction.

## Corrections apportées lors de la passe d’ensemble

### Cohérence entre chapitres et avec la partie I
- **Dossier *Challenger* (ch. 5 et ch. 6) :** harmonisation entre la nuance du chapitre 5 et l’étude de cas du chapitre 6. Les deux mentionnent désormais la date du 28 janvier 1986 rattachée à `rogers1986`, et l’ensemble des 23 vols antérieurs documentés rattaché à `tufte1997` (point restant à confirmer contre la source primaire lors de la passe bibliographique).
- **Ferrure mécanique :** le renvoi de la section 5.5 s’appuie sur le `@sec:ch00` (où la ferrure est déjà présentée avec le même coefficient de sécurité de 1,8) et annonce les chapitres 7 et 8 ; le chapitre 7 rappelle à son tour le coefficient de 1,8 ; au chapitre 8, la mise en correspondance de la ferrure avec le `@tbl:ch08-comparateurs` distingue la seconde exécution du même calcul (première ligne du tableau) du contrôle analytique à la main (troisième ligne : « Autre méthode, même modèle »).
- **Eau bouillante (ch. 2 et ch. 5) :** au chapitre 5, « les 101 °C de l’eau salée » laissait entendre que l’eau salée bout à 101 °C, alors qu’au chapitre 2 elle reste calme à cette température ; corrigé en « l’eau salée encore calme à 101 °C, ni l’ébullition vers 85 °C au sommet du mont Blanc ».
- **Notation $z$ :** introduite de façon informelle une seule fois au chapitre 5 (la seconde introduction dans le bloc formel est devenue un rappel), puis formalisée au chapitre 7 avec mention explicite du lien au `@sec:ch05`.
- **Terme réservé *régime* (ch. 8 vs ch. 12) :** les trois emplois de « régime stationnaire / régime inadéquat » en thermique au chapitre 8 ont été remplacés par « fonctionnement permanent / état permanent », afin de ne pas entrer en collision avec le *changement de régime* du chapitre 12. (« Taux stationnaire » au chapitre 9 est conservé.)
- **Autres termes réservés aux parties suivantes :**
  - chapitre 7 : « validation croisée » (deux fois, alors que *validation* est fixé au `@sec:ch13`) devient « recoupement par partitions successives (souvent appelé *validation croisée*) » puis « partitions d’un tel recoupement » ; la nuance du chapitre 7 annonce explicitement la distinction de l’*omission de saillance* au `@sec:ch12` ;
  - chapitre 8 : « contrôleur de gestion » devient « examen comptable » ; « vérification rapide d’ordre de grandeur » devient « évaluation rapide d’ordre de grandeur » ;
  - chapitre 9 : « trop complaisant » (terme *complaisance* réservé au `@sec:ch15`) devient « trop indulgent » ; « rester silencieux » (trois occurrences, proche d’*erreur silencieuse* au `@sec:ch13`) devient « ne signale rien / ne pas signaler d’erreur / n’émettre aucune alerte ».
- **Genre des renvois croisés :**
  - chapitre 7 : `au @sec:ch02-rigueur-formelle` (deux fois) et `dès le @sec:ch01-modes-inference` se rendaient en « au section 2.4 » et « dès le section 1.1 » ; corrigés en `à la @sec:ch02-rigueur-formelle` et `dès la @sec:ch01-modes-inference`.
- **Mise en gras unique et titres de section :**
  - chapitre 5 : suppression du numéro figé « la proposition 1 » dans le titre de la section 5.4 (`Une barre d’erreur mesure un désaccord`) ;
  - chapitre 8 : *blanchiment* n’est plus mis en gras qu’une seule fois, dans la `@def:blanchiment`.
- **`parties/partie-2.md` :** ajustement de deux tournures pour la précision et l’écho exact avec les chapitres (« au sein d’un ensemble d’alternatives admises », « à travers ce que le cadre enregistre »).

### Exactitude formelle et chiffrée, et français
- **Chapitre 5 :** reprise de calques (« n’ont pas averti […] en produisant », « ajuste trop étroitement ») et des termes usuels de corrosion (« corrosion par piqûres et fissuration par corrosion sous contrainte ») ; citation `rogers1986` ajoutée sur la date de l’accident ; découpe plus nette du chapeau et reformulation d’une parenthèse vague (« plus loin dans l’ouvrage »).
- **Chapitre 6 :** dans le bloc formel, l’énoncé final sur $0 < \Pr(C_j \mid E_k) < 1$ ne dérivait pas de la seule inclusion $D \subseteq \bigcap_j C_j$ (qui borne $\Pr(D \mid E_k)$ par le haut) ; reformulé avec exactitude. Remplacement de « mécanismes tout à fait indépendants » et « défaillances indépendantes » par « mécanismes qui lui sont propres » et « défaillances distinctes » pour ne pas suggérer une indépendance probabiliste absente du modèle. Suppression du futur « Comme le montrera le dépouillement… ».
- **Chapitre 7 :** identification explicite du « Modèle M3 » avant et dans le titre du bloc formel ; allégement des répétitions de « dans le cadre ».
- **Chapitre 8 :** dans le bloc `.outils`, précision que les pannes propres $p'_j$ sont supposées indépendantes entre elles ; dans le bloc M1, renvoi au modèle du contrôleur du chapitre 9 formulé avec les termes du livre (« contrôle réussi », « fausses alertes ») ; dans le troisième point clé, remplacement d’« augmentée des écarts que la comparaison ne sait pas exprimer » (trop proche de $(B_1 \cap B_2) \cup B_{\text{cmp}}$) par « compte tenu des écarts que la comparaison ne sait pas exprimer » ; « serrer un couple » corrigé en « serrer au couple ».
- **Chapitre 9 :** retrait de la valeur intermédiaire `0,61538...` dans le bloc `.exemple-quantitatif` pour n’y laisser que les nombres présents dans `tableaux/ch09-echappement.md` ; renvoi explicite aux cinq conditions du `@sec:ch06` pour l’événement $C$ ; clarification de la phrase sur la dépendance entre baisse de $P(E)$ et échappement ; harmonisation de la formulation entre les deux puces du petit exemple $1\,\% \times 90\,\%$ contre $10\,\% \times 1\,\%$ et à la clôture de la partie.

## Choix de vocabulaire communs à la partie (pour les chapitres suivants)
- **« agent » :** absent de toute la partie II (terme réservé au `@sec:ch14`). À la place : « celui qui », « personne », « équipe », « technicien », « automate d’essais et d’erreurs » (ch. 7), « acteurs — humains ou logiciels » (ch. 8), « producteur / contrôleur » (introduits au ch. 8).
- **« régression à l’infini » :** reprise homogène de l’expression de la partie I (ch. 2) au chapitre 7 et dans `parties/partie-2.md` (sans employer « régression » au sens statistique).
- **Exemples courants :** *ferrure métallique* avec coefficient de sécurité de `1,8` (ch. 5, 7, 8) ; *dinde inductiviste* et poulet de Russell (ch. 5) ; *eau bouillante* calme à `101 °C` et bouillant vers `85 °C` au mont Blanc (ch. 5) ; *Challenger*, 28 janvier 1986 et 23 vols antérieurs documentés (ch. 5, 6) ; *Mars Climate Orbiter*, 23 septembre 1999, programme au sol `SM_FORCES`, $\text{lbf}\cdot\text{s}$ contre $\text{N}\cdot\text{s}$, facteur proche de `4,45` (ch. 8).
- **Taux d’erreur :** la notation $P(E)$ du registre et du chapitre 6 est conservée, et son équivalence avec l’étiquette `P(faux)` des graphiques et tableaux générés est explicitée à la section 9.5.

## Écarts par rapport à la spec
- **Chapitre 5 :** le terme *ensemble des alternatives admises* et les notations $\Theta, \theta$ sont définis dès la section 5.1 (où la loi de la variance totale l’exige) plutôt qu’à la section 5.4 ; le bloc `.formel` porte l’argument de la variance totale tandis que le bloc `.outils` en rappelle les définitions et la dérivation ; le coefficient de sécurité est unifié à `1,8` (sans le `1,5` mentionné ailleurs dans les fils sources) ; un renvoi vers le `@sec:ch07` accompagne l’introduction informelle de $z$ (`00_global.md` § 6).
- **Chapitre 6 :** ajout d’un bloc `.nuance` immédiatement après `@prop:comparateur` pour en expliciter le statut définitionnel et la portée (`00_global.md` § 3 et `authoring_conventions.md` § 4).
- **Chapitre 7 :** les volets `(a)` et `(b)` de `@prop:cause-commune` sont réunis dans un même énoncé sous `statut="résultat sous hypothèses"`, avec précision dans le corps du bloc que `(b)` est illustré ensuite par des constats empiriques (le filtre et le vérificateur n’acceptant qu’une étiquette et un statut simple par proposition).
- **Chapitre 8 :** `@prop:independance` porte `statut="hypothèse de travail"` et précise son statut composite à l’intérieur de l’énoncé (première phrase : définition ; compromis coût/indépendance : hypothèse de travail) ; la spec de `part2.md` place `chain-a` dans les blocs, intégré ici en fin de section 8.5 après M1 ; le `@tbl:ch08-comparateurs` comporte une quatrième colonne « Coût indicatif » en plus de la légende.
- **Chapitre 9 :** les trois petits exemples chiffrés (`tbl:ch09-depistage`, `tbl:ch09-desaccords`, `tbl:ch09-taux-echappement`) sont inclus dans le texte principal (avec un bloc `.outils` en 9.1), réservant le bloc `.exemple-quantitatif` au modèle M1 complet (`fig:ch09-echappement` et `tbl:ch09-echappement`).

## Points à traiter hors des chapitres (mainteneur)
1. **Figures manquantes dans la partie II (4 figures, rendues en cadres de substitution) :**
   - `figures/ch05-trois-incertitudes.pdf` / `.svg` (description dans `NOTES_05.md`) ;
   - `figures/ch05-ferrure-marge.pdf` / `.svg` (description dans `NOTES_05.md`) ;
   - `figures/ch06-cinq-conditions.pdf` / `.svg` (description dans `NOTES_06.md`) ;
   - `figures/ch07-cause-commune.pdf` / `.svg` (description dans `NOTES_07.md`).
2. **Cohérence de `commun/registre_termes.md` :**
   - l. 94 : la table des notations indique `sec:ch07` pour $z$, alors que `00_global.md` § 6 indique « 5 (informal), 7 (M3) » (signalé dans `NOTES_06.md`) ;
   - l. 93 : la table des notations écrit « ensemble des hypothèses admises » alors que le tableau des termes (l. 35) fixe **ensemble des alternatives admises** (`NOTES_05.md`) ;
   - l. 18 : la définition de *représentation* emploie encore « un agent agit » au sens courant (`NOTES_02.md`, `RELECTURE_partie1.md`, `NOTES_06.md`, `NOTES_07.md`).
3. **Harmonisation d’exemples et tableaux générés :**
   - `tableaux/ch08-chaine.md` intitule sa dernière colonne « Part des défaillances restantes due à q » alors que la formule $q / \Pr(\text{échec})$ couvre les défaillances *impliquant* $q$ (`NOTES_08.md`) ;
   - `00_global.md` § 7 résume à deux chiffres significatifs (`0.76 % / 0.38 %`) des valeurs affichées à trois chiffres (`0,756 % / 0,380 %`) dans `tableaux/ch09-echappement.md` (`NOTES_09.md`) ;
   - `commun/exemples_courants.md` reste à compléter pour les chapitres 5 à 9 ;
   - `chapitres/00-cartographier.md`, l. 71, emploie « alerte » au sens courant en résumant le chapitre 6 (`NOTES_06.md`), et `00_global.md` § 8 / `biblio_a_verifier.bib` (`mco1999`) parlent encore de « fichier `SM_FORCES` » alors que `SM_FORCES` est le programme au sol (`NOTES_00.md`, `NOTES_08.md`).
4. **Entrée bibliographique à ajouter ou trancher :**
   - au chapitre 5 (`.cas` sur les modèles hypothécaires avant 2008), un marqueur libre `[@A-VERIFIER: rapport ou étude sur les modèles de risque hypothécaire et la corrélation des défauts avant 2008]` demeure dans `05-trois-incertitudes.md` (l. 52) ; deux entrées candidates (`fcic2011`, `coval2009`) sont proposées dans `NOTES_05.md`.
   - au chapitre 7, `NOTES_07.md` propose éventuellement `wolpert1996` en complément de `wolpert1997`.

## Références à vérifier dans la partie
Toutes les références de fait ou de littérature (hors `fauriat2026frame`, déjà vérifiée dans `biblio.bib`) sont des clés candidates de `biblio_a_verifier.bib` :
- **Chapitre 5 :** `wynne1992`, `walker2003`, `lempert2003`, `knight1921`, `russell1912`, `rogers1986`, `tufte1997` — et le marqueur libre pour le cas des modèles hypothécaires avant 2008 (`fcic2011` / `coval2009` proposés dans `NOTES_05.md`).
- **Chapitre 6 :** `rogers1986`, `tufte1997` (en particulier confirmer le décompte des 23 vols antérieurs documentés dans le graphique discuté par Tufte, en cohérence avec le chapitre 5).
- **Chapitre 7 :** `lazer2014`, `wolpert1997`, `hume1748`, `goodman1955`, `sutton2018`.
- **Chapitre 8 :** `levins1966`, `orzack1993`, `wimsatt1981`, `knightleveson1986`, `mco1999`.
- **Chapitre 9 :** `mayo1996`, `mayo2018`, `bliss1995`.
