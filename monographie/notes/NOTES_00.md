# Notes — Avant-propos et Chapitre 00

## Références à ajouter ou à vérifier
- `[@fauriat2026frame]` (vérifiée, `commun/biblio.bib`) — thèse générale sur le problème du cadre ; genèse hybride de la démarche (`#sec:avant-propos-objet`, `#sec:avant-propos-genese`, `#sec:ch00-representation`). L'affirmation de l'avant-propos selon laquelle la réflexion de l'auteur précède l'usage des modèles s'appuie sur la note de production de l'article (qui renvoie à un travail de 2022, non citable ici en vertu de la règle de l'unique autoréférence).
- `[@mco1999]` (candidate) — `#sec:ch00-trois-recits`, `#sec:ch00-chaines-croises`. Points à vérifier dans le rapport de la commission :
  - perte le 23 septembre 1999 pendant l'insertion en orbite, trajectoire passée beaucoup trop près de la planète (ce dernier point **sort du champ `averifier`** actuel : à y ajouter) ;
  - `SM_FORCES` est le **programme** au sol (le rapport parle d'un « fichier » de code, *Small Forces*) ; les données transitaient par un fichier de sortie distinct (fichier AMD, à confirmer). Le texte dit désormais « un programme au sol, `SM_FORCES` », puis « un fichier de code » ;
  - N·s exigés par la spécification d'interface, lbf·s produits, facteur ≈ 4,45 ;
  - facteurs organisationnels cités : effectifs insuffisants, doutes de l'équipe de navigation sur la trajectoire restés sans suite, absence de recalcul indépendant (formulations à confronter au rapport).
- `[@mata2023]` (candidate) — `#sec:ch00-trois-recits`, `#sec:ch00-contrats-donnees`. Points à vérifier : mémoire des avocats **du demandeur** en opposition à la demande de rejet d'Avianca (début 2023) ; six décisions inexistantes ; le modèle avait assuré qu'elles figuraient dans les bases juridiques ; ordonnance de sanctions de juin 2023 (amende et autres mesures).
- `[@becker2025]` (candidate) — `#sec:ch00-trois-recits` (encadré `.cas` daté 2025). Points à vérifier : essai randomisé, développeurs expérimentés de logiciels libres sur leurs propres dépôts, outils « du début de 2025 », ≈ 19 % de temps en plus mesuré, ≈ 20 % d'accélération estimée après coup.
- `[@ue2015tip]` (candidate, **nouvelle citation au chapitre 0**) — `#sec:ch00-remedes`, projection d'images de menaces fictives dans le contrôle des bagages. L'affirmation correspond exactement au champ `averifier` (prévu pour le chapitre 18).

## Termes proposés (absents du registre)
- Aucun. Conformément au statut du chapitre 0, aucun terme du registre n'y est mis en gras ni défini formellement ; les notions apparaissent sous forme de gloses informelles (« ce que nous appellerons un cadre », « un angle mort », « on parlera alors de calibration »).

## Paramètres / figures demandés
- `ch00-serie-parallele` — schéma conceptuel — `figures/ch00-serie-parallele.pdf` (`#fig:ch00-serie-parallele`, `#sec:ch00-chaines-croises`) : pictogramme opposant la composition en série (chaîne : les angles morts s'additionnent, plus les erreurs d'interface) et la composition en parallèle (contrôle croisé : seul l'angle mort commun subsiste).
- `ch00-carte-ouvrage` — schéma synoptique — `figures/ch00-carte-ouvrage.pdf` (`#fig:ch00-carte-ouvrage`, `#sec:ch00-architecture`) : carte d'une page des cinq parties et des étapes de l'argument.

## Écarts par rapport à la spec
- **Seuil de décision écrit en mots.** La spec autorise une formule « en mots » ; la seconde formule affichée est donc `seuil = gain / (gain + perte)` et non `p∗ = ΔU / (ΔU + L)`, car les notations p∗, ΔU et L sont introduites au chapitre 4 selon le registre. Le chapitre garde deux formules affichées, le maximum prévu.
- **Énigme arithmétique.** Elle oppose deux organisations « imaginaires, avec des chiffres choisis pour l'illustration » plutôt qu'un « système classique » et un « système automatisé », pour ne pas laisser croire que 90 % d'échappement décrit un système réel. Valeurs inchangées (`00_global.md` §7). Le tableau `tableaux/ch09-taux-echappement.md` n'est pas inclus (collision d'étiquette, voir plus bas).
- **Ajouts hors liste de sections, conservés :** une sous-section sur la barre d'erreur (aperçu de P1, étape S5) et la dinde inductiviste (aperçu de S2), toutes deux informelles.
- **Question à se poser :** formulée sans accord en genre du lecteur (« le dernier chiffre d'après lequel vous avez agi »).

## Corrections apportées à la première version
Avant-propos :
- « rédiger les brouillons successifs » remplacé par « rédiger une large part du texte lui-même » (règle : ne jamais mentionner de brouillons ; et ne pas sous-estimer l'apport des modèles). **À confirmer par l'auteur :** la note de production de l'article va plus loin (« la prose a été générée par un modèle de langage ») ; le degré de divulgation retenu ici est une décision d'auteur.
- Ajout : le fond de l'argument doit beaucoup à la littérature citée (cohérent avec la note de l'article).
- « l'un des résultats centraux » (régression des méta-procédures) devenu « l'un des arguments centraux » : ce point n'est pas une proposition à statut.
- « une meilleure hypothèse de travail » (calque) → « la meilleure hypothèse de travail » ; « que l'on prépare à la contradiction » → « que l'on expose volontiers à la contradiction ».
- Compromis indépendance–comparabilité nuancé (« en général ») : c'est une *hypothèse de travail*.
- « statisticiens » retiré du public premier (ceux qui ont « rarement pratiqué » les probabilités) ; ils restent dans la liste des profils du paragraphe suivant.
- Termes techniques remplacés par du langage courant avant le chapitre 0 (« blanchiment de provenance », « comparateurs capables de se tromper autrement »).
- Pronom « il » pour l'auteur évité ; double citation de l'article dans le même paragraphe supprimée ; « sceau de curation » → « gage réel […] mais non une garantie absolue » ; « la clôture de son propre cadre » (peu clair) → « ne peut certifier son propre cadre ».
- Règle du texte principal : « maillon logique de la démonstration » → « maillon du raisonnement » ; ajout d'une phrase rappelant que les exemples quantitatifs et les études de cas font partie du fil (conventions §4).
- Statuts : ajout d'une phrase sur les énoncés à statut composite (P3, P4).

Chapitre 0 :
- *Mars Climate Orbiter* : « orbite haute » (inexact) et « neuf mois » (hors champ de la citation) retirés ; `SM_FORCES` présenté comme le programme ; « unités impériales » → « unité anglo-saxonne » ; citation rapprochée du facteur 4,45.
- *Mata v. Avianca* : ce n'était pas un « mémoire en défense » mais l'opposition du demandeur à une demande de rejet ; « plus d'une demi-douzaine d'arrêts d'appel » → « une demi-douzaine de décisions » ; « complets avec » (calque) supprimé ; « sanctions disciplinaires » → amende et autres sanctions (juin 2023) ; « printemps 2023 » → « début de 2023 ».
- METR : « les meilleurs outils du moment » → « outils récents » ; la phrase de synthèse ne prête plus à l'étude une causalité qu'elle n'établit pas (« la fluidité altère le jugement ») ; les chiffres datés ne figurent plus que dans l'encadré `.cas` (pitfall 9), le texte courant y renvoie.
- M. X nommé dès sa première apparition.
- Prévisionniste : la version précédente disait qu'une traversée « ne permet jamais » de juger ; conforme à la spec du chapitre 3 désormais (si le mât casse, l'issue plaide nettement contre M. Y ; si le bateau tient, elle ne départage presque rien).
- Barre d'erreur : « n'élargit donc jamais » corrigé selon la note de robustesse de P1 (un facteur omis qui a varié entre dans la dispersion, non attribué).
- Cinq conditions : « la probabilité d'échappement grimpe à 100 % » restreint au contrôle considéré.
- P3b : ajout de la condition « à travers ce que l'on a enregistré » ; « sera pris en défaut » → « peut être pris en défaut ».
- Contrôle croisé : le prix de l'indépendance est présenté comme une tendance (« le plus souvent »), conformément au statut d'hypothèse de travail.
- Informatique classique : « pendant soixante-dix ans » (chiffre non sourcé, et faux pour l'apprentissage automatique) supprimé ; limite de Dijkstra signalée en une phrase ; l'échec dans les couches basses est désormais dit « définissable », non bruyant (pitfall 4), avec l'exemple des unités de la sonde, erreur restée longtemps silencieuse.
- Ajout d'une phrase sur le réinterrogatoire : il révèle les erreurs où le modèle devine, non les erreurs constantes (pitfall 8, S12).
- Automatisation : « pipelines » → « chaînes de traitement » ; « hypothèses blanchies à chaque passage » nuancé ; « les institutions tendent à » (affirmation empirique non sourcée) → « la tentation est forte ».
- Fausses alertes : la baisse d'écoute est attribuée au comportement, non au calcul (pitfall 5).
- Remèdes : « verrou » aligné sur la définition du registre ; limite de l'attitude individuelle ajoutée (notre expérience déborde le cadre du modèle, jamais le nôtre) ; citation `ue2015tip` ajoutée.
- Architecture : « des lois » → « des mécanismes » ; « démontre » → « montre » ; « tous ses exemples » → « ses exemples » (+ finance, pour le cas des modèles hypothécaires) ; « la vraisemblance » → « la plausibilité, et non la vérité » (évite la collision avec le sens statistique de *vraisemblance*, cf. « rapport de vraisemblance »).
- Points clés : la quatrième puce ne présente plus l'aisance des erreurs comme une conséquence de la dépense de la garantie.
- Chapeau : une phrase signale que les mots employés seront définis dans leurs chapitres.

## Harmonisation après la partie V et la conclusion
- **Avant-propos, `#sec:avant-propos-posture`** : « quelles observations empiriques suffiraient à mettre l’argument en défaut » devient « pourraient mettre l’argument en défaut ». C’est la posture du livre et la formulation de `parties/partie-5.md`, que la conclusion (`#sec:conclusion-refutation`) reprend.
- **Chapitre 0, « frontières de régime » (placement des contrôles et dernier point clé)** : remplacé par « points de passage vers l’action », la formule retenue au chapitre 18 (`#sec:ch18-placement-ou`). Il n’y a plus de collision avec le changement de régime du chapitre 12, et le livre n’emploie plus « frontière de régime » nulle part.
- **Chapitre 0, `#tbl:ch00-parcours`, ligne « Parcours critique »** : ajout des encadrés *Nuance* des chapitres 7 et 16, qui portent des tensions recensées par la conclusion (omission de saillance ; corrélation et usure des alertes). **Écart** par rapport à `course_outline.md` § 5, qui reste à aligner.
- **Chapitre 0, exemple des deux organisations** : « ne mesurent guère que le premier facteur » devient « notent le producteur seul : ils ne mesurent que le premier facteur ». La formulation porte désormais sur ce que mesure un test de référence par construction, et non sur un relevé empirique ; elle est alignée sur les chapitres 9 et 16.

## Incohérences repérées ailleurs
- `content_spec/00_global.md` §7 et `tableaux/ch09-taux-echappement.md` : la spec indique que ce tableau peut servir aussi au chapitre 0, mais il porte en dur l'étiquette `{#tbl:ch09-taux-echappement}` ; l'inclure aux chapitres 0 et 9 provoquerait un avertissement d'étiquette en double. Il reste réservé au chapitre 9.
- `content_spec/00_global.md` §8, `part3.md` (ch. 10) et champ `averifier` de `mco1999` : « SM_FORCES file » ; selon le rapport, `SM_FORCES` désigne le logiciel au sol, les données passant par un fichier de sortie distinct. À préciser pour les chapitres 8 et 10.
- `filtres/monographie.lua` : une référence à une cible non numérotée (`@sec:conclusion`) affiche le titre complet ; « la conclusion (@sec:conclusion) » donne donc « la conclusion (Conclusion : la méthode appliquée à elle-même) ». Le chapitre 0 a été reformulé pour l'éviter ; l'avant-propos garde cette forme, acceptable. Une forme courte (« la conclusion ») pourrait être utile au mainteneur.
- `commun/exemples_courants.md` est encore un gabarit vide ; la liste des exemples courants du chapitre 0 suit `course_outline.md` §4.
