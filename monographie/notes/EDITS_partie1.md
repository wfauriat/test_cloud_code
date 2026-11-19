# Corrections appliquées : partie 1 (page de partie et chapitres 1 à 4)

Source : relectures « à froid » de Sonnet et d’Opus (`notes/LECTURE_FRAICHE_*`). Une correction n’a été appliquée que si le problème était relevé par les deux lecteurs, ou par un seul et vérifié sur le texte ; si une seule lecture du passage était plausible ; si la correction était locale et minimale ; et si le sens, la portée et la force de l’affirmation restaient identiques. Les autres constats figurent dans `notes/A_TRANCHER_partie1.md`.

Aucune étiquette, clé de citation, formule, aucun nombre, titre, bloc `:::`, statut ni renvoi n’a été modifié. Aucun terme du registre n’a été remplacé, ajouté ou mis en gras.

## Récapitulatif

| Fichier | Corrections appliquées | dont relevées par les deux lecteurs | dont relevées par un seul lecteur et vérifiées |
| :-- | --: | --: | --: |
| `parties/partie-1.md` | 1 | 1 | 0 |
| `chapitres/01-outils-logique-probabilite.md` | 12 | 7 | 5 |
| `chapitres/02-cadre.md` | 6 | 6 | 0 |
| `chapitres/03-mondes-possibles.md` | 5 | 3 | 2 |
| `chapitres/04-decider.md` | 4 | 3 | 1 |
| **Total** | **28** | **20** | **8** |

Correction appliquée de la même façon dans plusieurs fichiers : « course au large » pour désigner la course des deux navigateurs (ch. 1, E12 ; ch. 3, E4), ce qui aligne les ch. 1 et 3 sur l’expression déjà employée aux ch. 2, 3 et 4.

`make verifier` après corrections : 0 erreur. Le seul avertissement du périmètre (`chapitres/01-outils-logique-probabilite.md` : tableau généré absent, `tableaux/ch01-bayes-cotes.md`) existait déjà avant les corrections et relève du mainteneur. Les autres lignes du périmètre ne diffèrent que par leurs numéros de ligne, décalés par les trois coupures de paragraphe.

---

## `parties/partie-1.md`

**E1.** Paragraphe consacré au chapitre 3.
- AVANT : « Comme une probabilité se partage ainsi entre plusieurs issues, la survenue de l’une d’elles ne permet guère de la juger : un risque de pluie élevé n’est pas démenti par une journée sèche. »
- APRÈS : « Comme une probabilité se partage ainsi entre plusieurs issues, la survenue de l’une d’elles ne permet guère de juger la probabilité annoncée : un risque de pluie élevé n’est pas démenti par une journée sèche. »
- Constats : Sonnet B1 ; Opus B2 (première partie).
- Justification : le pronom « la » avait deux antécédents féminins proches (la probabilité, l’issue). Les deux lecteurs retiennent la même lecture, confirmée par l’exemple de la pluie, et proposent la même reformulation. Le reste du constat d’Opus B2 (« situations » et « issues », « confiance » et « probabilité ») est laissé à l’auteur.

---

## `chapitres/01-outils-logique-probabilite.md`

**E1.** § Déduction et induction (`sec:ch01-modes-inference`), 1er paragraphe.
- AVANT : « de cas déjà vus, elle tire une règle, ou une prévision pour des cas qui ne l’ont pas encore été. »
- APRÈS : « de cas déjà vus, elle tire une règle, ou une prévision pour des cas que l’on n’a pas encore vus. »
- Constats : Sonnet C2 (seconde partie) ; Opus C1.
- Justification : reprise pronominale elliptique (« l’ » renvoyait à « vus ») ; même sens, reprise explicite.

**E2.** § Probabilité : règles et lectures, encadré `.formel` « Axiomes du calcul des probabilités ».
- AVANT : « (elle contient $\Omega$ et elle est stable par passage au complémentaire et par réunion dénombrable) »
- APRÈS : « (elle contient $\Omega$ et elle est stable par passage au complémentaire et par réunion dénombrable : le complémentaire d’un événement, comme la réunion d’une suite d’événements, est encore un événement) »
- Constats : Sonnet B12 (première partie) ; Opus C4.
- Justification : courte glose d’un jargon. Elle énonce la définition même de la stabilité et n’ajoute aucune affirmation. L’expression technique est conservée.

**E3.** § Probabilité : règles et lectures, après l’encadré.
- AVANT : « Deux lectures principales leur en donnent un. »
- APRÈS : « Deux lectures principales donnent un sens à ces nombres. »
- Constats : Sonnet B13 ; Opus C5.
- Justification : cascade de pronoms (« leur », « en », « un ») ; le référent est celui de la phrase précédente (« non le sens des nombres »).

**E4.** § Réviser un jugement : la règle de Bayes sous forme de cotes, après la définition de la cote.
- AVANT : « soit une chance contre quatre, et une probabilité de 50 % à une cote de $1$. »
- APRÈS : « soit une chance contre quatre (un cas favorable pour quatre défavorables), et une probabilité de 50 % à une cote de $1$. »
- Constat : Sonnet B1 (vérifié sur le texte).
- Justification : l’expression est juste, mais elle se confond aisément avec « une chance sur quatre » (25 %), juste à côté d’une probabilité de 20 %. La glose explicite l’expression sans changer ni ajouter de valeur.

**E5.** § Réviser un jugement, 2e paragraphe.
- AVANT : « On peut écrire cette règle directement en probabilités, mais le dénominateur $\Pr(E)$ y masque le mécanisme de la révision. »
- APRÈS : « On peut écrire cette règle directement en probabilités (voir l’encadré ci-dessous), mais le dénominateur $\Pr(E)$ y masque le mécanisme de la révision. »
- Constats : Sonnet B2 ; Opus B2.
- Justification : le texte commentait une formule que le lecteur n’avait pas encore vue. Le renvoi pointe vers l’encadré « Dérivation de la règle de Bayes sous forme de cotes », qui la donne.

**E6.** § Réviser un jugement, après l’@eq:ch01-bayes-cotes.
- AVANT : « Autrement dit, la cote *a posteriori* est la cote *a priori* multipliée par le rapport de vraisemblance. »
- APRÈS : « Autrement dit, la cote *a posteriori* (après l’observation) est la cote *a priori* (avant l’observation) multipliée par le rapport de vraisemblance. »
- Constat : Opus B3 (vérifié : première occurrence des deux locutions dans un chapitre qui « ne suppose rien des autres »).
- Justification : glose d’une locution technique qu’un lecteur cultivé peut entendre au sens philosophique (indépendant de l’expérience ou issu d’elle). La notation $\text{cote}(H \mid E)$, aussi signalée, n’est pas glosée.

**E7.** Encadré `.exemple-quantitatif` « Réviser la probabilité d’un défaut… », Mise en place (coupure de paragraphe).
- AVANT : « […] $\Lambda(T^-) = 0{,}25 / 0{,}85 = 5/17 \approx 0{,}294$. On part de deux jugements *a priori* : […] »
- APRÈS : « […] $\Lambda(T^-) = 0{,}25 / 0{,}85 = 5/17 \approx 0{,}294$. » puis, dans un nouveau paragraphe, « On part de deux jugements *a priori* : […] »
- Constat : Sonnet B3 (vérifié : un seul paragraphe porte le comportement de la sonde, les deux rapports de vraisemblance et les deux a priori).
- Justification : paragraphe coupé entre le comportement de la sonde et les jugements a priori, sans changer un mot ni un nombre.

**E8.** Même encadré, Mise en place.
- AVANT : « et à 20 % pour une soudure d’une zone qui a subi des contraintes inhabituelles. »
- APRÈS : « et à 20 % pour une soudure d’une zone suspecte, qui a subi des contraintes inhabituelles. »
- Constats : Sonnet B4 (première partie) ; Opus C12 (troisième partie).
- Justification : la légende, le calcul et la lecture parlent de « zone suspecte » sans que la mise en place ait fait le lien. Le nom est maintenant donné dès la première mention. La seconde partie de ces constats (« la seconde sonde ») est laissée à l’auteur.

**E9.** Même encadré, légende de la @fig:ch01-bayes-cotes.
- AVANT : « Le même signal anormal multiplie la cote par 5 dans les deux cas, mais seule la soudure de la zone suspecte franchit la barre d’une chance sur deux. »
- APRÈS : « Le même signal anormal multiplie la cote par 5 pour les deux soudures, mais seule la soudure de la zone suspecte franchit la barre d’une chance sur deux. »
- Constat : Opus B5 (vérifié).
- Justification : « les deux cas » suivait l’énumération de quatre situations ; le référent voulu est celui des deux soudures (lot courant, zone suspecte). L’ajout « après ce seul signal », aussi proposé, n’est pas repris : il devient inutile une fois le référent fixé.

**E10.** Même encadré, Lecture.
- AVANT : « multiplier la cote par 5 laisse la soudure du lot courant probablement saine (17,2 %), mais »
- APRÈS : « multiplier la cote par 5 laisse la soudure du lot courant probablement saine (probabilité de défaut : 17,2 %), mais »
- Constat : Opus B6 (vérifié).
- Justification : accolé à « saine », le pourcentage se lisait comme une probabilité d’être saine, alors qu’il s’agit de la probabilité de défaut. Le nombre est inchangé.

**E11.** § Mesurer la qualité d’une prévision : la surprise, exemple du verger.
- AVANT : « il correspond à un rapport de vraisemblance de 10 en faveur du premier. »
- APRÈS : « il correspond, si l’on traite chaque prévision comme une hypothèse, à un rapport de vraisemblance de 10 en faveur du premier. »
- Constats : Sonnet B9 ; Opus B10.
- Justification : le rapport de vraisemblance n’avait été défini que pour deux hypothèses. L’incise annonce l’extension que le paragraphe suivant et l’encadré formalisent (« rapport de vraisemblance de l’issue observée sous la première prévision contre la seconde »). Aucune affirmation n’est ajoutée.

**E12.** § Mesurer la qualité d’une prévision, paragraphe « On voit ainsi le lien… ».
- AVANT : « pour comparer les estimations de deux navigateurs avant une même course, et pour examiner »
- APRÈS : « pour comparer les estimations de deux navigateurs avant une même course au large, et pour examiner »
- Constats : Sonnet C15 ; Opus C15.
- Justification : sans contexte, « navigateurs » pouvait évoquer des logiciels. « Course au large » est l’expression employée pour cette même course aux ch. 2, 3 et 4. (Même correction au ch. 3, E4.)

---

## `chapitres/02-cadre.md`

**E1.** § Le cadre comme spécification finie, encadré `.formel` « Conditionnement sur les variables du cadre ».
- AVANT : « Les lois $\Pr(Y \mid X = x)$ moyennent tacitement son effet sur les valeurs qu’il prenait là où elles ont été établies ; »
- APRÈS : « Les lois $\Pr(Y \mid X = x)$ moyennent tacitement l’effet de ce facteur sur les valeurs qu’il prenait là où ces lois ont été établies ; »
- Constats : Sonnet B6 ; Opus B6.
- Justification : trois pronoms (« son », « il », « elles ») renvoyaient à des référents différents dans une même proposition ; les deux référents nominaux sont rétablis. « Là où » est conservé : la proposition « dans les conditions où » élargissait le sens.

**E2.** § Le cadre comme spécification finie, après l’encadré formel.
- AVANT : « Le compromis est plus serré qu’il n’y paraît. »
- APRÈS : « L’arbitrage est plus délicat qu’il n’y paraît. »
- Constats : Sonnet B7 ; Opus C12.
- Justification : les deux lecteurs y voient un calque de *the trade-off is tighter* et proposent tous deux « arbitrage ». « Délicat » (Opus) est retenu ; l’ajout d’une phrase proposé par Sonnet (« il faut choisir entre énoncer plus et énoncer moins ») ne l’est pas.

**E3.** § La rigueur formelle ne lève pas cette limite, paragraphe sur la déduction (coupure de paragraphe).
- AVANT : « […] elle ne la crée pas et ne la certifie pas. Considérons à nouveau la poutre de la @sec:ch01-modes-inference. […] »
- APRÈS : « […] elle ne la crée pas et ne la certifie pas. » puis, dans un nouveau paragraphe, « Considérons à nouveau la poutre de la @sec:ch01-modes-inference. […] »
- Constats : Sonnet C15 ; Opus C16 (première partie).
- Justification : paragraphe de plus de deux cents mots qui mêlait principe et exemple. Il est coupé à l’endroit proposé par les deux lecteurs, sans changer un mot.

**E4.** Même section, paragraphe sur l’induction.
- AVANT : « Or choisir les grandeurs mesurées, les variables sur lesquelles on conditionne et la série de référence qui définissent cette ressemblance, c’est encore choisir un cadre. »
- APRÈS : « Or choisir les grandeurs mesurées, les variables sur lesquelles on conditionne et la série de référence (les cas que l’on tient pour semblables) qui définissent cette ressemblance, c’est encore choisir un cadre. »
- Constats : Sonnet B10 ; Opus B8.
- Justification : au ch. 1, « série de référence » n’apparaît que dans un encadré `.nuance`, facultatif ; le texte principal du ch. 2 l’emploie sans rappel. La glose reprend les mots mêmes de cet encadré (« décider quels cas l’on tient pour semblables »). L’accord pluriel de « définissent » (trois antécédents coordonnés), mis en doute par Sonnet, est correct et conservé.

**E5.** Même section, paragraphe sur Pearl et la prédiction conforme.
- AVANT : « elle garantit que l’ensemble prédit contiendra la vraie valeur avec au moins la fréquence choisie »
- APRÈS : « elle garantit que l’ensemble de valeurs qu’elle prédit contiendra la vraie valeur avec au moins la fréquence choisie »
- Constats : Sonnet B11 (dernière partie) ; Opus B9.
- Justification : « l’ensemble prédit » surgissait sans qu’on sache que la méthode prédit un ensemble de valeurs. La glose est minimale : l’ajout « valeurs plausibles », proposé par Opus, n’est pas repris, car il aurait ajouté une caractérisation.

**E6.** Encadré `.cas` « Un modèle clinique face à un changement de population ».
- AVANT : « Entre-temps, l’organisation des urgences a changé les critères d’admission »
- APRÈS : « Entre-temps ou ailleurs, l’organisation des urgences a changé les critères d’admission »
- Constats : Sonnet C13 ; Opus C18.
- Justification : le connecteur ne convenait qu’au second scénario (« quelques années plus tard »), non au premier (« dans une autre région »). L’indicatif est conservé, car la proposition « a pu changer » affaiblissait l’assertion.

---

## `chapitres/03-mondes-possibles.md`

**E1.** § Mondes possibles, 1er paragraphe.
- AVANT : « Il existerait alors, avant l’événement, une seule « vraie » valeur »
- APRÈS : « Il existerait ainsi, avant l’événement, une seule « vraie » valeur »
- Constats : Sonnet C1 ; Opus C2.
- Justification : « alors » était répété dans deux phrases consécutives ; « ainsi » garde la valeur consécutive.

**E2.** § Mondes possibles, 2e paragraphe.
- AVANT : « Une assertion probabiliste n’écarte rien de plus que ce que l’on sait déjà ; elle répartit »
- APRÈS : « Une assertion probabiliste n’écarte rien de plus que ce que l’on sait déjà exclu ; elle répartit »
- Constat : Opus B1 (vérifié).
- Justification : on écarte des situations, non un savoir. Un mot rétablit la seule lecture possible (rien de plus que ce que l’on sait déjà exclu).

**E3.** § Mondes possibles, paragraphe « Cette lecture s’accorde… » (coupure de paragraphe).
- AVANT : « […] c’est la part des situations cachées dans $(\dots)$ où la règle fonctionne. L’@eq:ch02-cond-cadre prolonge la même image. […] »
- APRÈS : « […] c’est la part des situations cachées dans $(\dots)$ où la règle fonctionne. » puis, dans un nouveau paragraphe, « L’@eq:ch02-cond-cadre prolonge la même image. […] »
- Constats : Sonnet B3 (première partie) ; Opus B3 (première partie).
- Justification : c’est le paragraphe le plus dense du chapitre. Il est coupé au point proposé par les deux lecteurs, sans changer un mot. Les rappels de $X$ et $Y$, aussi proposés, ne sont pas ajoutés (voir A_TRANCHER).

**E4.** § Prévision et prévisionniste, après l’encadré.
- AVANT : « Cette asymétrie entre l’issue attendue et l’issue rare dépasse de loin les régates. »
- APRÈS : « Cette asymétrie entre l’issue attendue et l’issue rare dépasse de loin la course au large. »
- Constats : Sonnet C8 ; Opus C11.
- Justification : impropriété lexicale, car une course au large n’est pas d’ordinaire une régate. « Course au large » est l’expression du chapitre (et des ch. 2 et 4) pour cet exemple. (Même alignement au ch. 1, E12.)

**E5.** § Calibration et historique des prévisions, paragraphe sur l’historique.
- AVANT : « si le projet réussit, un pari imprudent prend après coup l’allure d’une estimation solide. »
- APRÈS : « si un projet réussit, un pari imprudent prend après coup l’allure d’une estimation solide. »
- Constat : Opus C15 (vérifié : aucun projet n’est mentionné auparavant dans le chapitre).
- Justification : l’article défini supposait un antécédent absent ; l’indéfini donne la valeur générique voulue.

---

## `chapitres/04-decider.md`

**E1.** § La course à la voile, paragraphe « L’inégalité… s’écrit aussi… ».
- AVANT : « l’option risquée l’emporte lorsque la cote du succès contre l’échec dépasse le rapport des enjeux. »
- APRÈS : « l’option risquée l’emporte lorsque la cote du succès contre l’échec, c’est-à-dire le rapport de leurs probabilités, dépasse le rapport des enjeux. »
- Constats : Sonnet B9 (première partie) ; Opus B1.
- Justification : en français courant, la « cote » d’un pari désigne aussi le multiplicateur de gain du bookmaker. La glose, en mots et sans formule ajoutée, reprend la définition du ch. 1 (« le rapport de sa probabilité à celle de son contraire »).

**E2.** Même paragraphe.
- AVANT : « Dès que la perte dépasse le gain, le seuil passe au-dessous de 50 %, et il baisse d’autant plus que l’écart entre les deux est grand. »
- APRÈS : « Dès que la perte dépasse le gain, le seuil passe au-dessous de 50 %, et il baisse d’autant plus que le rapport entre les deux est grand. »
- Constat : Opus B2 (vérifié).
- Justification : « écart » évoque une différence, alors que la phrase suivante (« seul compte le rapport sans dimension $L/\Delta U$ »), l’@eq:ch04-seuil et l’encadré de dérivation (« Le seuil décroît quand le rapport des enjeux croît ») établissent que seul compte le rapport. Un seul mot change, et le sens devient celui de l’équation et de la phrase suivante.

**E3.** § La course à la voile, dernier paragraphe.
- AVANT : « (la règle de Bayes, sous la forme de l’@eq:ch01-bayes-cotes, dit de combien elle doit la déplacer) »
- APRÈS : « (la règle de Bayes, sous la forme de l’@eq:ch01-bayes-cotes, dit de combien cette information doit déplacer l’estimation) »
- Constats : Sonnet B2 ; Opus C8.
- Justification : deux pronoms féminins voisins (« elle », « la ») ; les deux lecteurs retiennent la même lecture (l’information déplace l’estimation).

**E4.** Encadré `.exemple-quantitatif` « Seuil de décision et rapport des enjeux… », légende de la @fig:ch04-seuil.
- AVANT : « Le décideur part lorsque son estimation $p$ se trouve au-dessous de la courbe. »
- APRÈS : « Le décideur choisit l’option risquée lorsque son estimation $p$ se trouve au-dessous de la courbe. »
- Constats : Sonnet C8 ; Opus C10.
- Justification : la courbe vaut aussi pour la roulette russe, où « partir » n’a pas de sens ; « option risquée » est l’expression du chapitre. Les « part » et « renonce » propres aux navigateurs, plus loin dans la légende, sont conservés. Aucun nombre n’est touché.
