# Notes — Chapitre 01

*Révision après relecture (deuxième passe).* Le chapitre a été relu contre `authoring_conventions.md`, `content_spec/00_global.md`, `content_spec/part1.md` et le registre, puis réécrit en conservant toutes les étiquettes (sections, équations, figure) et l’exemple de la poutre, auxquels renvoient les chapitres 2 et 3. Corrections principales :
- **Erreur logique :** le syllogisme de la poutre n’était pas valide tel qu’écrit (la prémisse mineure n’affirmait pas que la poutre est en acier homogène, alors que le texte déclarait ensuite « la prémisse d’homogénéité » fausse). La prémisse est désormais explicite, et l’exemple du métal sert de cas valide *et* solide.
- **Validité et solidité :** la phrase « la déduction transmet la vérité *pourvu que* les idéalisations correspondent » confondait les deux notions. Elle dit maintenant que la déduction transporte la vérité, ou l’erreur, des prémisses.
- **Physique :** « surfusion » (refroidissement sous le point de fusion) remplacé par « retard à l’ébullition ». Le cas de l’altitude ne réfute pas « si on la porte à 100 °C, elle bout » ; il montre que la valeur de 100 °C elle-même dépend de la pression.
- **Bloc formel du score :** « la cohérence probabiliste interdit » une probabilité nulle était faux, puisque les axiomes l’autorisent. Le texte parle désormais de prudence.
- **Terminologie :** « contrôle » (terme du chapitre 6) retiré de l’exemple quantitatif (« examen par ultrasons ») ; « alerte » (chapitre 9) retiré ; « rapport de plausibilité », synonyme de *cote*, supprimé ; « raisonneur rationnel » (calque) remplacé.
- **Gras :** *déduction* et *induction* étaient en gras deux fois ; « formule des probabilités totales », absente du registre, était en gras. Elle passe en italique.
- **Références :** « au @sec:ch00-parcours » produisait « au section… ». Remplacé par « à la @sec:ch00-parcours ».
- Chapeau allégé ; *Points clés* resserrés sur les cinq points prévus par la spec, plus celui des règles à conditions tues ; additivité de la surprise ramenée dans le texte principal (règle du texte principal : le @sec:ch03 en a besoin pour noter un prévisionniste sur la durée).

## Références à ajouter ou à vérifier
- `[@hume1748]` (clé candidate) — problème de l’induction, `#sec:ch01-modes-inference`. Même affirmation que celle prévue au champ `averifier` (qui ne mentionne que le chapitre 7).
- `[@definetti1974]`, `[@jaynes2003]`, `[@lindley2006]` (clés candidates) — lecture de la probabilité comme jugement, `#sec:ch01-probabilite`. Même affirmation que celle des champs `averifier`, qui ne mentionnent que le chapitre 3 : ajouter le chapitre 1.
- Facultatif, non cité dans le texte : les axiomes sont attribués à Kolmogorov sans référence. Entrée proposée si le mainteneur souhaite une citation : `@book{kolmogorov1933, author = {Kolmogorov, Andreï N.}, title = {Grundbegriffe der Wahrscheinlichkeitsrechnung}, publisher = {Springer}, address = {Berlin}, year = {1933}}`.
- Facultatif, non cité : le bloc `.nuance` évoque le problème de la classe de référence (choix de la série de comparaison en lecture fréquentiste). Une référence possible, à vérifier : Hájek, A. (2007), « The reference class problem is your problem too », *Synthese*, 156(3), 563–585.
- Aucun marqueur `[@A-VERIFIER: …]` dans le chapitre ; aucune donnée empirique chiffrée (tous les nombres sont illustratifs ou arithmétiques).

## Termes proposés (absents du registre)
- **cote** — *odds* — « Rapport de la probabilité d’une hypothèse à celle de son contraire : $\Pr(H) / (1 - \Pr(H))$. » — Introduite au `sec:ch01` (en italique, faute d’entrée au registre). La définition du registre de *rapport de vraisemblance* emploie déjà le mot (« il multiplie la cote de l’une contre l’autre »), et il resservira aux chapitres 3 et 9.
- **Notations à ajouter à la table des notations (introduites au `sec:ch01`) :**
  - $\Lambda(E)$ : rapport de vraisemblance de l’observation $E$ ;
  - $S(p) = -\ln p$ : surprise (score logarithmique) ;
  - $\Omega$ : ensemble des issues retenues ;
  - $\text{cote}(H)$.
- Vocabulaire employé sans le proposer comme terme (usage standard, en italique) : *valide* / *solide* (validité et solidité d’un argument), *partition*, *formule des probabilités totales*, *retard à l’ébullition*. Si le mainteneur veut *valide* / *solide* au glossaire, je propose la définition « valide : impossible d’avoir des prémisses vraies et une conclusion fausse ; solide : valide et à prémisses vraies ».

## Paramètres / figures demandés
- **`ch01-bayes-cotes`** — `#sec:ch01-bayes`, bloc `.exemple-quantitatif` « Réviser la probabilité d’un défaut après un examen par ultrasons » (ce jeu de paramètres manque dans `00_global.md` §7 et dans `commun/parametres.py`).
  - **Paramètres** (distincts du dépistage du chapitre 9, qui utilise 1 %, 90 % et 5 %) :
    - $\Pr(T^+ \mid D) = 0{,}75$ et $\Pr(T^- \mid D) = 0{,}25$ ;
    - $\Pr(T^+ \mid \bar{D}) = 0{,}15$ et $\Pr(T^- \mid \bar{D}) = 0{,}85$ ;
    - d’où $\Lambda(T^+) = 5$ et $\Lambda(T^-) = 5/17$.
  - **Tableau demandé** (`tableaux/ch01-bayes-cotes.md`, étiquette `tbl:ch01-bayes-cotes`) :

    | Situation | Probabilité a priori | Cote a priori | Rapport de vraisemblance | Cote a posteriori | Probabilité a posteriori |
    | :-- | --: | --: | --: | --: | --: |
    | Lot courant, signal anormal | 4 % | 0,0417 | 5 | 0,208 | 17,2 % |
    | Zone suspecte, signal anormal | 20 % | 0,25 | 5 | 1,25 | 55,6 % |
    | Zone suspecte, signal normal | 20 % | 0,25 | 0,294 | 0,0735 | 6,85 % |
    | Zone suspecte, deux signaux anormaux indépendants | 20 % | 0,25 | 25 | 6,25 | 86,2 % |

    - **Légende**, qui doit reprendre les quatre caractéristiques de la sonde (75 %, 25 %, 15 %, 85 %) : « Révision par cotes de la probabilité de défaut d’une soudure. La sonde émet un signal anormal dans 75 % des cas en présence d’un défaut (normal dans 25 %), et dans 15 % des cas sur une soudure saine (normal dans 85 %). »
    - J’ai simulé la vérification numérique de `outils/verifier.py` avec ce tableau : tous les nombres cités dans la prose du bloc s’y retrouvent.
  - **Figure demandée** (`figures/ch01-bayes-cotes.pdf` et `.svg`, étiquette `fig:ch01-bayes-cotes`) : diagramme de pente, ou barres appariées, de la probabilité *a priori* à la probabilité *a posteriori* pour les quatre situations, avec une ligne de repère à 50 %. Elle doit montrer que le même facteur 5 laisse le lot courant sous 50 % et porte la zone suspecte au-dessus.
  - **Une fois le tableau généré**, remplacer « Le tableau ci-dessous » par « Le @tbl:ch01-bayes-cotes » dans le paragraphe *Calcul*. Le renvoi est omis pour l’instant, pour éviter une erreur d’étiquette non définie.
- **Exemples arithmétiques dans le texte courant, hors bloc quantitatif et absents de `00_global.md` §7 :**
  - retard de livraison : $\Pr(H) = 0{,}25$, 40 % et 4 %, d’où 13 % ;
  - gel sur un verger : 20 % contre 2 % ; surprises 1,61 et 3,91 (rapport 10), puis 0,223 et 0,020 (rapport 0,816).
  - Ils servent seulement à illustrer une formule, et chaque calcul est exact. Si le mainteneur lit la règle 6 comme couvrant tout exemple arithmétique, il faudra les ajouter au §7 et à l’annexe D ; sinon, rien à faire.

## Écarts par rapport à la spec
- **Lien entre score logarithmique et rapport de vraisemblance :** `part1.md` (section 6) parle du rapport de vraisemblance comme d’un « *ratio of surprises* ». Avec $S(p) = -\ln p$, c’est la *différence* des surprises qui vaut le *logarithme* du rapport de vraisemblance. Le chapitre donne la relation exacte.
- **Bloc `.nuance` ajouté** (absent de la spec) : « Fréquence ou jugement : un débat que ce livre ne tranche pas ». Le choix de la lecture comme jugement y est présenté comme une position de travail, et la lecture fréquentiste y est montrée dépendante d’un jugement (le choix de la série de référence). Justification : `00_global.md` §2 demande de nommer les tensions. Le bloc est facultatif pour l’argument.
- **Questions d’ouverture :** la spec veut que chaque outil soit « introduit par la question à laquelle il répond ». Les lignes en italique « *Question : …* » de la version précédente pouvaient se confondre avec les blocs `.question` (« Question à se poser »). La question ouvre désormais chaque section, dans la prose.
- **Règle 6 (nombres des exemples quantitatifs) :** le tableau n’existant pas encore, les nombres du bloc ont été écrits d’après les paramètres proposés ci-dessus, à la précision prévue pour le tableau. À revérifier par `make verifier` après génération.

## Incohérences repérées ailleurs
- `content_spec/part1.md` (section 6 du chapitre 1) : remplacer « *the likelihood ratio as the ratio of surprises* » par « *the log likelihood ratio as the difference of surprises* », en cohérence avec `tableaux/ch03-score-log.md` ($\exp(6{,}91 - 3{,}00) = 50$).
- `content_spec/00_global.md` §7 et `commun/parametres.py` : `part1.md` demande un exemple quantitatif au chapitre 1, mais aucun jeu de paramètres n’est défini (voir ci-dessus).
- `commun/biblio_a_verifier.bib` : ajouter le chapitre 1 au champ `averifier` de `definetti1974`, `jaynes2003`, `lindley2006` et `hume1748`.
- `chapitres/02-cadre.md`, l. 41 et 47 : « (surfusion) » désigne le refroidissement d’un liquide sous son point de fusion. Pour l’eau qui dépasse 100 °C sans bouillir, le terme juste est « retard à l’ébullition » (ou « surchauffe »).
- `chapitres/02-cadre.md`, l. 35, 83 et 119 (deux fois) : « au @sec:ch01-… » se rend « au section 1.x ». Écrire « à la @sec:ch01-… ».
- `chapitres/02-cadre.md`, l. 41 et tableau `tbl:ch02-eau-bouillante`, étape 4 : avec la règle « si l’on porte de l’eau à 100 °C, alors elle bout », l’ébullition à 85 °C au mont Blanc ne constitue pas un contre-exemple, car l’antécédent n’est jamais atteint dans un récipient ouvert. Elle réfute la lecture « l’eau bout à 100 °C (et pas avant) ». Le chapitre 1 formule désormais ce cas ainsi : « c’est la valeur même de 100 °C qui cesse de convenir ». Une précision analogue au chapitre 2 éviterait le reproche.
- `chapitres/03-mondes-possibles.md`, l. 3 (en cours de rédaction) : « du @sec:ch00-parcours » se rend « du section 0.x ». Écrire « de la @sec:ch00-parcours ».
- `commun/registre_termes.md` : *agent* est enregistré au sens d’agent fondé sur un modèle de langage (introduit au `sec:ch14`). Or la définition de *représentation* (`sec:ch02`) emploie « un agent » au sens courant de « quiconque agit », et les chapitres 2 et 3 l’emploient ainsi. Il faudrait soit préciser l’entrée (« agent (logiciel) »), soit éviter le mot au sens courant.
