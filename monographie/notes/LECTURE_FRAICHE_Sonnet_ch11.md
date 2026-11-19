# Lecture fraîche, chapitre 11 « Quand la règle est tirée des données » (Sonnet)

## 1. Ce que j'ai compris (test de lisibilité)

1. Les logiciels classiques butaient sur les tâches dont personne ne sait écrire la règle. L'apprentissage automatique la tire d'exemples et la range dans des paramètres : un « composant appris ».
2. On gagne en portée et l'on paie en garantie préalable et en lisibilité. La spécification n'a pas disparu : elle s'est déplacée dans le choix des données et de l'objectif.
3. Un modèle de langage est entraîné à prédire le fragment suivant. Sa compétence n'a pas de frontière nette. Son objectif étant la plausibilité, il peut être fluide et faux sans enfreindre de contrat (cas Mata v. Avianca). Moffatt v. Air Canada ne prouve rien sur les modèles de langage.
4. Consignes, RLHF, filtres et tests de référence « orientent » les tendances du modèle, mais ne spécifient rien. Le dressage d'un chien s'oppose au câblage d'un disjoncteur, et la loi de Goodhart met en garde contre l'optimisation d'une mesure.
5. Le chapitre 12 traitera des conséquences pour l'évaluation et l'enquête après coup.

## 2. Constats classés par gravité

Aucun constat de gravité A : le chapitre reste compréhensible de bout en bout. Les gênes réelles (B) sont surtout des dépendances non expliquées et quelques phrases elliptiques.

### Gravité B (gêne réelle)

**B1. Section « La spécification passe dans les données », 1er paragraphe.**
Passage : « l'arrière-plan ouvert d'exceptions étudié dès le @sec:ch02 envahissait l'écriture même du programme ».
Problème : « arrière-plan ouvert » est un terme technique non défini ici (possible dépendance du chapitre 2), et l'image est dense.
Proposition : « le foisonnement imprévisible d'exceptions (étudié dès le @sec:ch02) envahissait l'écriture même du programme ».
Le sens ne bouge que si « arrière-plan ouvert » est un terme technique du chapitre 2 à conserver : dans ce cas, le rappeler brièvement entre parenthèses.

**B2. Même section, après la définition.**
Passage : « repose sur un échange : on achète de la *portée*, et l'on dépense en retour la *garantie* et la *lisibilité* ».
Problème : « échange » est un calque de *trade-off*. Le lecteur comprend un « échange de données » ou un « dialogue ».
Proposition : « repose sur un arbitrage » (ou « un compromis »).
Sens inchangé.

**B3. Section « Le moteur à prédire le fragment suivant », 1er paragraphe.**
Passage : « occupent aujourd'hui le sommet de la pile logicielle » (repris à la fin : « au sommet de la pile logicielle »).
Problème : « pile logicielle » (*software stack*) est un calque. Le « sommet » n'est pas explicité : couche la plus proche de l'utilisateur ? La dernière couche d'une architecture ?
Proposition : « occupent aujourd'hui la couche la plus visible des systèmes logiciels, celle qui dialogue avec l'utilisateur ».
Cette reformulation suppose que « sommet » désigne la couche proche de l'utilisateur. Autre lecture plausible : « la couche dont dépendent les autres composants ». Je ne tranche pas.

**B4. Même paragraphe.**
Passage : « par un score logarithmique analogue à celui du @sec:ch01 ».
Problème : un lecteur qui ne retient pas le chapitre 1 ne sait pas ce qu'est ce score. Possible dépendance.
Proposition : ajouter quelques mots de rappel : « (le score logarithmique, qui pénalise d'autant plus que le fragment observé avait reçu une faible probabilité, comme au @sec:ch01) ».
Le sens ne bouge pas, mais la glose est à valider par l'auteur.

**B5. Même section, paragraphe du *logit lens*.**
Passages : « Lorsqu'on lui soumet le début d'une phrase demandant dans quelle ville se dresse la tour Eiffel » ; « En projetant les états intermédiaires sur le vocabulaire de sortie ».
Problèmes :
- Le « lui » est loin de son référent (le modèle).
- « le début d'une phrase demandant » a deux lectures : une question posée, ou une phrase à compléter (« La tour Eiffel se trouve à… »). La suite (« la ville précise ne remonte en tête ») suggère la seconde.
- « états intermédiaires » et « vocabulaire de sortie » sont du jargon sans glose.
Proposition : « Lorsqu'on soumet au modèle une phrase inachevée dont la suite attendue est la ville où se dresse la tour Eiffel ». Pour le jargon : « les représentations calculées à mi-parcours dans le réseau ».
Si l'auteur veut dire « une question posée au modèle », la première reformulation change le sens.

**B6. Section « Fluide et faux sans enfreindre aucune règle », 3e paragraphe.**
Passage : « Mais dès que la donnée est rare, l'événement particulier ou la question ambiguë, composer un paragraphe bien charpenté […] demeure une suite hautement probable de la consigne ».
Problème : la série mêle une proposition (« la donnée est rare ») à deux groupes nominaux sans verbe. La phrase est elliptique et se lit mal.
Proposition : « Mais dès que la donnée est rare, que l'événement est particulier ou que la question est ambiguë, composer un paragraphe […] demeure une suite hautement probable de la consigne ».
Sens inchangé.

**B7. Même section, 6e paragraphe.**
Passage : « la comparaison de plusieurs tirages répétés permet, pour certaines erreurs mais non pour toutes, de repérer une réponse hasardeuse ».
Problème : « tirages » (échantillonnage de plusieurs réponses du modèle à la même consigne) n'est pas expliqué. Un lecteur cultivé pensera à un tirage au sort sans comprendre de quoi.
Proposition : « la comparaison de plusieurs réponses obtenues en reposant la même question ».
Cette formulation suppose que « tirages » désigne bien des réponses multiples à la même consigne.

**B8. Même section, paragraphe suivant l'encadré Mata.**
Passage : « l'équivalent du programme `SM_FORCES` écrivant des livres-force-secondes au lieu de newton-secondes ».
Problème : `SM_FORCES` n'est rattaché à aucune mission dans le chapitre. Le lecteur n'a que « Mars Climate Orbiter » plus haut, sans lien explicite.
Proposition : « l'équivalent du programme `SM_FORCES` de *Mars Climate Orbiter*, qui écrivait des livres-force-secondes… ».
Sens inchangé.

**B9. Même section, introduction de l'encadré Moffatt.**
Passage : « Dans les commentaires qui entourent ces affaires, un autre litige… ».
Problème : « ces affaires » est au pluriel, alors qu'une seule affaire a été traitée (Mata). Le référent est flou.
Proposition : « Dans les commentaires qui entourent l'affaire *Mata v. Avianca* » (ou, si le pluriel vise les affaires de citations inventées en général, « ces affaires de citations inventées »).
Ces deux lectures sont possibles : à trancher par l'auteur.

**B10. Section « Orienter n'est pas spécifier », 1er paragraphe.**
Passage : « ne laisse pas les modèles tels qu'ils sortent du préentraînement ».
Problème : « préentraînement » n'a pas été introduit. La section 2 parle seulement d'« entraînement », puis de « phases d'entraînement ultérieures ». Le lecteur ne sait pas que l'étape décrite plus haut était un « pré »-entraînement.
Proposition : « tels qu'ils sortent de leur entraînement initial (celui qui consiste à prédire le fragment suivant) ».
Sens inchangé.

**B11. Incohérence interne entre le corps de la section « Orienter » et les points clés.**
Passages :
- Le corps classe le test de référence parmi les moyens de « suivre leurs progrès » (il mesure) et le distingue de l'« orientation » définie comme « infléchir ses tendances, par des consignes ou par un ajustement sur des préférences ».
- Pourtant, la phrase qui suit la définition dit « Toutes ces interventions visent à orienter un modèle », ce qui inclut les tests de référence.
- Le dernier point clé écrit : « Les consignes, l'ajustement sur des préférences humaines et les tests de référence orientent les distributions du modèle ».
Problème : un test de référence mesure, il n'oriente pas directement. Il n'agit qu'indirectement, quand on optimise ses scores (voir Goodhart). Le lecteur hésite sur le statut du test.
Proposition : dans le point clé, « Les consignes et l'ajustement sur des préférences humaines orientent les distributions du modèle, les tests de référence mesurent des moyennes, et tous abaissent des fréquences d'erreur sans établir d'invariant ». Ou bien, dans le corps, préciser que les tests orientent « indirectement, par l'optimisation de leurs scores ».
Deux lectures sont possibles selon la position de l'auteur : je ne tranche pas.

**B12. Même section, paragraphe d'application de la loi de Goodhart.**
Passage : « optimiser des systèmes pour progresser sur une batterie publique finit par mesurer l'adaptation à la forme particulière de cette batterie — parfois jusqu'à l'imprégnation de variantes voisines — ».
Problèmes :
- Le sujet grammatical de « finit par mesurer » est « optimiser », alors que c'est le test qui mesure (sujet suspendu).
- « imprégnation de variantes voisines » est opaque. Deux lectures : (a) des variantes des épreuves se sont glissées dans les données d'entraînement (contamination) ; (b) le modèle s'est surajusté à des variantes proches du test.
Proposition : « optimiser des systèmes pour progresser sur une batterie publique conduit le test à mesurer l'adaptation à sa forme particulière — parfois jusqu'à une familiarité avec des variantes voisines des épreuves — ».
Je laisse ouverte la question de savoir si c'est (a) ou (b).

### Gravité C (confort, style)

**C1. Section « La spécification passe dans les données ».**
Passages : « une fonction objectif et une famille de fonctions paramétrées » ; « rien dans les poids du modèle » ; « milliards de coefficients couplés ».
Problème : « fonction objectif » n'est pas glosée. « paramètres », « poids » et « coefficients » sont employés comme synonymes sans que le lecteur en soit prévenu.
Proposition : glose brève (« une mesure d'écart à minimiser ») et, à la première occurrence de « poids », « (les paramètres du modèle) ».

**C2. Section « Le moteur… », 1er paragraphe.**
Passage : « demander au réseau d'attribuer une distribution de probabilités ».
Problème : « réseau » n'est pas défini (réseau de neurones ?).
Proposition : « demander au modèle (un réseau de neurones) d'attribuer… ».

**C3. Même section, 2e paragraphe.**
Passage : « Personne ne saisit dans un tel système les règles de la grammaire ».
Problème : « saisir » prête à confusion (comprendre ou entrer au clavier).
Proposition : « Personne n'inscrit dans un tel système… ».

**C4. Même section, paragraphe du *logit lens*.**
Passage : « Sur des modèles ouverts de taille modeste ».
Problème : « ouverts » calque de *open models* ; le lecteur peut croire à un modèle sans restriction d'usage.
Proposition : « sur des modèles dont les paramètres sont publics et de taille modeste ».

**C5. Même section, paragraphe sur la limite structurelle.**
Passage : « sans que rien en lui n'avertisse d'avoir franchi une limite » ; « cette genèse imprime aussitôt une limite structurelle ».
Problèmes :
- « d'avoir franchi » a un sujet sous-entendu ambigu (le modèle ? l'utilisateur ?).
- « genèse » est vague.
Proposition : « sans que rien en lui ne signale que la limite est franchie » ; « cette manière de se former imprime aussitôt… ».

**C6. Même section, dernier paragraphe.**
Passage : « L'étude même qui documente ces gains de portée mesure aussi cette rupture brutale ».
Problème : l'encadré BCG ne mentionne que les gains « dans le domaine de compétence ». Le lecteur ne voit pas d'où vient la « rupture » et doit croire l'auteur.
Proposition : ajouter dans l'encadré une demi-phrase sur le résultat hors domaine, ou écrire « l'étude même… mesure aussi, hors de ce domaine, une rupture brutale ».
La seconde proposition préserve le contenu.

**C7. Section « Fluide et faux… ».**
Passage : « inventions », « fabrication », « réponses fabriquées », « hallucination ».
Problème : plusieurs mots sans distinction annoncée. « Hallucination » n'apparaît qu'entre guillemets dans l'introduction de l'encadré Moffatt, sans avoir été posé. Le lecteur peut croire à des phénomènes distincts.
Proposition : poser une fois (par exemple en tête de section) « affirmation fluide et fausse (ce qu'on appelle couramment une « hallucination »)» et s'y tenir.

**C8. Section « Fluide et faux… », paragraphe suivant l'encadré Mata.**
Passage : « il ne révèle aucun bogue au sens du @sec:ch10. Rien dans la forme du texte ne trahissait l'invention. Et si l'on recherche… ».
Problème : la deuxième phrase change de sujet (détectabilité) sans lien avec la première (absence de bogue). Le « Et si » est un connecteur faible.
Proposition : « … au sens du @sec:ch10 : aucune forme du texte ne trahissait l'invention, et si l'on recherche… » (ou supprimer la phrase si elle double le propos). Je ne propose pas de suppression ferme.

**C9. Section « Orienter n'est pas spécifier », paragraphes sur RLHF et loi de Goodhart.**
Passages : « modèle auxiliaire » (texte) / « modèle de récompense » (encadré) ; « notes » / « scores de récompense » ; « consigne générale » / « L'instruction ».
Problème : variation lexicale sur un même objet, source d'hésitation.
Proposition : retenir « modèle de récompense » et « consigne ».

**C10. Même section, paragraphe sur les tests de référence.**
Passage : « Et dès que l'on pilote le perfectionnement d'un système appris en optimisant soit ces scores d'évaluation, soit une note de préférence, on se heurte à un mécanisme identifié bien avant l'apprentissage automatique : lorsqu'une mesure devient un objectif à atteindre, elle cesse d'être une bonne mesure. »
Problème : phrase très longue avec double incise, à couper.
Proposition : couper après « de préférence » : « … soit une note de préférence, on se heurte à un mécanisme identifié bien avant l'apprentissage automatique. Lorsqu'une mesure devient un objectif, elle cesse d'être une bonne mesure. »

**C11. Même section, 3 petits points de langue.**
Passages :
- « tend à primer celle qui paraît sûre d'elle » : « primer » transitif a un sens de récompense ; « privilégier » est plus naturel.
- « tient dans une opposition concrète » : « tient à ».
- « éprouver ce déclenchement d'avance contre une tolérance écrite » : « éprouver contre » est un calque ; « vérifier ce déclenchement d'avance par rapport à une tolérance écrite ».

**C12. Section « La spécification passe dans les données ».**
Passage : « pour les systèmes d'apprentissage déployés en production ».
Problème : « en production » est un calque ; « mis en service » serait plus naturel.

**C13. Points clés, 4e point.**
Passage : « n'obéit à aucune frontière nette ni prévisible ».
Problème : le corps dit « ni contour régulier ni frontière nette ». « Prévisible » est un critère nouveau, absent du corps.
Proposition : « n'a ni contour régulier ni frontière nette » (aligné sur le corps).

**C14. Section « Orienter… », paragraphes RLHF et filtres.**
Passages : « classifieurs appris » ; « apprentissage par renforcement ».
Problème : jargon d'apprentissage automatique non glosé. Un lecteur cultivé non spécialiste devine à peine ce que recouvre « renforcement ».
Proposition : une glose brève à la première occurrence (« systèmes qui rangent un texte dans une catégorie, appris eux aussi sur des exemples » ; « une méthode qui récompense les réponses jugées bonnes »).

## 3. Appréciation globale

- Les sections les plus accessibles sont « La spécification passe dans les données » (hors B1-B2, le raisonnement est clair et bien annoncé), « Fluide et faux sans enfreindre aucune règle » (sauf B6-B9) et l'opposition finale chien / disjoncteur. La structure achat/dépense (portée / garantie et lisibilité) est constante et facile à suivre.
- La section la moins accessible est « Le moteur à prédire le fragment suivant » : jargon dense (score logarithmique, réseau, états intermédiaires, vocabulaire de sortie, *logit lens*) et un exemple (la tour Eiffel) dont la formulation prête à deux lectures. La section « Orienter n'est pas spécifier » se lit bien mais contient l'incohérence B11 et quelques notions importées (préentraînement, renforcement, classifieurs).
- Dépendances sur les chapitres antérieurs : score logarithmique (ch. 1), arrière-plan ouvert d'exceptions et inférence inductive (ch. 2), précondition, postcondition, invariant, contrat (ch. 10), `SM_FORCES` (ch. 8/10). Ces rappels sont brefs ou absents ; le chapitre reste lisible seul, mais au prix de quelques notions admises sur parole.
