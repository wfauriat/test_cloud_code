# Registre des termes et des notations

Source unique de la terminologie et des notations de la monographie. Le glossaire (annexe B) et la table des notations (annexe C) en sont générés : `make glossaire`.

**Règles d’usage :**
- un terme est mis en **gras** et défini uniquement dans le chapitre indiqué dans la colonne « Introduit » ; ailleurs, on l’emploie sans le redéfinir ;
- aucun synonyme pour le sens technique d’un terme du registre ;
- un terme nouveau se propose dans `notes/NOTES_NN.md` ; le mainteneur l’ajoute ici.

**Format :** une ligne de tableau par entrée. Ne pas modifier les colonnes : le script de génération lit ce fichier.
- **Introduit :** l’étiquette du chapitre (`sec:chNN`).
- **Étiquette :** la définition formelle correspondante (`def:…`), si elle existe.

## Termes

| Terme | Anglais | Définition | Introduit | Étiquette |
| :-- | :-- | :-- | :-- | :-- |
| représentation | picture | Construction (mesures, catégories, équations, probabilités) d’après laquelle un agent agit ; c’est à l’action que le monde répond, non à la représentation. | sec:ch02 | def:representation |
| cadre | frame | Spécification finie à l’intérieur de laquelle un raisonnement opère : variables, catégories, classe de modèles et objectif retenus. Il est choisi avant toute inférence. | sec:ch02 | def:cadre |
| problème du cadre | frame problem | Impossibilité de spécifier à l’avance tout ce qui est pertinent ; né en intelligence artificielle, il est pris ici dans un sens épistémologique général. | sec:ch02 | |
| déduction, induction | deduction, induction | Inférence nécessaire à partir de prémisses ; généralisation à partir de régularités observées. L’une et l’autre ne valent que « pourvu que » leurs conditions soient remplies. | sec:ch01 | |
| rapport de vraisemblance | likelihood ratio | Rapport des probabilités d’une observation sous deux hypothèses ; il multiplie la cote de l’une contre l’autre. | sec:ch01 | |
| score logarithmique | logarithmic score | Surprise d’une issue, −ln Pr(issue), sous la prévision qui lui attribuait la probabilité Pr. | sec:ch01 | |
| mondes possibles | possible worlds | Situations compatibles avec ce que l’on sait ; une probabilité dit quel poids accorder à chacune. | sec:ch03 | |
| raisonner à l’envers | reasoning in reverse | Chercher quelle variation cachée dans l’arrière-plan renverserait la conclusion, plutôt que de défendre une réponse unique. | sec:ch03 | |
| calibration | calibration (confidence) | Accord, sur un grand nombre de cas, entre les probabilités annoncées et les fréquences observées. | sec:ch03 | |
| historique | track record | Relevé des affirmations passées, avec leurs conditions, confronté a posteriori aux issues observées. | sec:ch03 | |
| utilité espérée subjective (UES) | subjective expected utility (SEU) | Règle de décision de Savage : choisir l’acte dont l’utilité espérée est la plus élevée, calculée avec ses propres probabilités. | sec:ch04 | |
| seuil p∗ | threshold p∗ | Probabilité d’échec au-delà de laquelle l’option risquée cesse d’être préférable : p∗ = ΔU / (ΔU + L). | sec:ch04 | |
| rapport des enjeux | stakes ratio L/ΔU | Rapport de la perte en cas d’échec au gain en cas de succès, tous deux mesurés par rapport à l’option sûre. | sec:ch04 | |
| décision unique | one-shot decision | Décision prise une seule fois, sans série d’essais, et dont la réponse du monde n’arrive qu’après l’acte. | sec:ch04 | |
| incertitude aléatoire | aleatory uncertainty | Variabilité que l’on traite comme irréductible entre des répétitions jugées identiques. | sec:ch05 | |
| incertitude épistémique | epistemic uncertainty | Manque de connaissance sur des paramètres ou des sous-modèles, réductible par des données ou un modèle plus fin. | sec:ch05 | |
| incertitude ontologique | ontological uncertainty | Doute sur la pertinence même des variables, des catégories et de la classe de modèles retenues. | sec:ch05 | |
| ensemble des alternatives admises | admitted set | Ensemble des hypothèses ou modèles sur lequel une incertitude est calculée ; ce qui n’y figure pas ne pèse pas. | sec:ch05 | |
| affirmation | claim | Énoncé portant sur un fait : réponse d’un modèle, prévision, rapport de mesure. | sec:ch06 | def:affirmation |
| contrôle | check | Confrontation d’une affirmation à un comparateur censé concorder avec elle. | sec:ch06 | def:controle |
| comparateur | comparator | Ce à quoi l’on confronte une affirmation : une autre affirmation, un texte fixé à l’avance ou une observation du monde. | sec:ch06 | def:comparateur |
| se tromper autrement | fail differently | Pour une cause d’erreur donnée, un comparateur se trompe autrement qu’une affirmation si cette cause ne les fausse pas tous deux de la même manière. | sec:ch06 | |
| prise en compte | uptake | Fait que quelqu’un prenne acte d’un désaccord et ait l’autorité pour agir en conséquence. | sec:ch06 | def:prise-en-compte |
| taux d’erreur | error rate | Probabilité qu’une affirmation soit fausse. | sec:ch06 | |
| probabilité d’échappement | escape probability | Probabilité qu’une affirmation fausse débouche sur une action sans avoir été contredite à temps. | sec:ch06 | def:echappement |
| défaillance de mode commun | common-mode failure | Défaillance simultanée de protections redondantes, sous l’effet d’une cause qu’elles partagent. | sec:ch07 | |
| dérive de distribution | distribution shift | Changement, en exploitation, d’un facteur resté constant pendant la collecte des données ; les contrôles fondés sur ces données ne pouvaient pas le voir. | sec:ch07 | |
| angle mort | blind spot | Ensemble des causes d’erreur qu’un composant (personne, équipe, programme, modèle) est incapable de percevoir. | sec:ch08 | def:angle-mort |
| chaîne | chain | Composition en série : chaque composant tient pour acquis le résultat du précédent ; les angles morts s’additionnent. | sec:ch08 | |
| contrôle croisé | cross-check | Composition en parallèle : deux composants se prononcent sur la même affirmation et l’on relève leurs désaccords ; seul l’angle mort commun subsiste. | sec:ch08 | |
| blanchiment | laundering | Perte des conditions d’un résultat au moment où il change de mains : un résultat conditionnel arrive en aval comme un fait établi. | sec:ch08 | def:blanchiment |
| producteur, contrôleur | producer, checker | Celui qui produit une affirmation ; celui qui la contrôle. | sec:ch08 | |
| sévérité | severity | Un contrôle réussi n’est probant que dans la mesure où il aurait échoué si l’affirmation avait été fausse (Mayo). | sec:ch09 | def:severite |
| taux de base | base rate | Fréquence d’une condition dans la population examinée, avant tout test. | sec:ch09 | |
| sensibilité | sensitivity | Probabilité qu’un contrôle signale une erreur quand il y en a une. | sec:ch09 | |
| taux de fausses alertes | false-alarm rate | Probabilité qu’un contrôle signale une erreur quand il n’y en a pas. | sec:ch09 | |
| valeur prédictive positive (VPP) | positive predictive value (PPV) | Proportion des alertes qui correspondent à de vraies erreurs. | sec:ch09 | |
| appariement des probabilités | probability matching | Tendance à réagir aux alertes à une fréquence calquée sur leur fiabilité perçue. | sec:ch09 | |
| composant spécifié | specified (stated) component | Composant dont quelqu’un a écrit les règles et qu’on peut doter d’une spécification vérifiable, c’est-à-dire d’un contrat. | sec:ch10 | def:composant-specifie |
| contrat | contract | Engagement écrit d’un composant : ce qu’il exige de l’appelant (précondition) et ce qu’il garantit en retour (postcondition). | sec:ch10 | |
| vérification en amont | front-loaded verification | Contrôle d’un composant fait une fois, par rapport à sa spécification, et valable pour toutes ses exécutions futures. | sec:ch10 | |
| adresse (d’une défaillance) | address (of a failure) | Endroit précis où une spécification écrite, ou qu’on aurait pu écrire, a été enfreinte. | sec:ch10 | |
| composant appris | learned component | Composant dont les règles ont été ajustées sur des exemples et n’existent que sous forme de paramètres. | sec:ch11 | def:composant-appris |
| consigne | prompt | Texte soumis à un modèle de langage pour orienter sa réponse (*prompt*). | sec:ch11 | |
| test de référence | benchmark | Batterie d’évaluation standardisée, publique ou interne (*benchmark*). | sec:ch11 | |
| orienter (un modèle) | steering | Infléchir les tendances d’un modèle (consignes, ajustement sur des préférences) sans établir de contrat vérifiable. | sec:ch11 | |
| changement de régime | regime flip | Basculement simultané, au sommet de la pile, de ce qui est promis, de la forme de l’échec et de ce que trouve l’enquête. | sec:ch12 | |
| frontière en dents de scie | jagged frontier | Limite irrégulière, difficile à prévoir et mouvante, de la compétence d’un modèle. | sec:ch12 | |
| calibration générative | generative calibration | Accord entre la distribution des énoncés produits par un modèle et celle de ses données d’entraînement ; elle entraîne l’invention de faits rares. | sec:ch12 | |
| omission structurelle | structural omission | Facteur absent de la représentation. | sec:ch12 | |
| omission de saillance | salience omission | Facteur représenté mais non mobilisé pour la question posée. | sec:ch12 | |
| erreur signalée, erreur silencieuse | signalled, silent error | Erreur que contredit au moins un comparateur ; erreur que rien ne contredit. | sec:ch13 | |
| vérification, validation | verification, validation | Résoudre correctement le problème tel qu’il est posé ; poser un problème qui représente assez fidèlement la réalité pour l’usage prévu. | sec:ch13 | |
| agent | agent | Modèle de langage qui poursuit un but en boucle : planifier, appeler un outil, lire le résultat, recommencer. | sec:ch14 | |
| signe révélateur | tell | Marque visible de l’incertitude de celui qui produit un résultat : hésitation, précautions de langage, forme approximative. | sec:ch15 | |
| signal coûteux | costly signal | Indice crédible parce qu’il coûte à produire ; il perd sa valeur quand il devient gratuit. | sec:ch15 | |
| équilibre mélangeant | pooling equilibrium | Situation où des produits de qualités différentes deviennent indiscernables et se vendent au même prix. | sec:ch15 | |
| complaisance | sycophancy | Tendance d’un modèle à adopter les présupposés de son interlocuteur. | sec:ch15 | |
| blanchiment de provenance | provenance laundering | Perte de l’origine d’une information, si bien que des copies d’une même source passent pour des témoignages indépendants. | sec:ch16 | |
| marge d’humilité | humility buffer | Marge ajoutée délibérément à l’estimation du risque pour ce que la représentation pourrait omettre ; elle relève du jugement, non de la mesure. | sec:ch17 | |
| bac à sable | sandbox | Environnement isolé où les actions n’ont aucun effet extérieur, et où l’on peut donc interroger le monde à peu de frais. | sec:ch17 | def:bac-a-sable |
| verrou | gate | Point où une action attend une autorisation, parce que la réponse du monde coûterait trop cher ou serait irréversible. | sec:ch17 | def:verrou |
| pré-mortem | pre-mortem | Exercice consistant à supposer que le projet a échoué et à écrire pourquoi, avant de l’engager. | sec:ch18 | |
| erreurs injectées | seeded errors | Erreurs introduites volontairement dans ce que l’on soumet à la relecture, pour mesurer combien passent au travers. | sec:ch18 | |

## Notations

| Symbole | Signification | Introduit |
| :-- | :-- | :-- |
| Pr(·), Pr(B \| A) | probabilité ; probabilité conditionnelle de B sachant A | sec:ch01 |
| A ∩ (…) → B | règle à conditions sous-entendues : (…) désigne l’arrière-plan non énoncé | sec:ch01 |
| X, x | variables représentées dans le cadre ; leurs valeurs | sec:ch02 |
| p | probabilité d’échec estimée par le décideur | sec:ch04 |
| L, ΔU | perte en cas d’échec ; gain en cas de succès (par rapport à l’option sûre) | sec:ch04 |
| p∗ | seuil de décision ΔU / (ΔU + L) | sec:ch04 |
| Θ, θ | ensemble des hypothèses admises ; une hypothèse | sec:ch05 |
| z | facteur omis, hors du cadre | sec:ch07 |
| P(E) | taux d’erreur : probabilité qu’une affirmation soit fausse | sec:ch06 |
| B_i, B_cmp | angle mort du composant i ; angle mort de la comparaison | sec:ch08 |
| N, q | nombre d’étapes d’une chaîne ; facteur omis partagé par toutes les étapes | sec:ch08 |
| c, m, f, s | part des causes d’erreur partagées ; taux d’oubli sur les autres erreurs ; taux de fausses alertes ; sensibilité | sec:ch09 |
| u | prise en compte : proportion des alertes suivies d’effet | sec:ch09 |
| b | marge d’humilité | sec:ch17 |
| p_w | risque réel : 1 − (1 − p)(1 − z) | sec:ch17 |
