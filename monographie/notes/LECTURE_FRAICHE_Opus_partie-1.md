# Lecture fraîche — Partie 1 (« Agir d’après une représentation »)

Lecteur : Opus, première lecture, sans autre fichier que `parties/partie-1.md`.

## Résumé (test de lisibilité)

Nous agissons d’après une représentation du monde, alors que c’est le monde qui répond ; cette partie rassemble les outils (logique, probabilités, décision) en montrant ce que chacun suppose sans le dire. Toute conclusion dépend de conditions jamais toutes énoncées, d’où la nécessité de fixer un cadre, à l’intérieur duquel la rigueur ne garantit pas la justesse ; la probabilité y est un jugement de confiance, qui ne se juge que sur une série de prévisions, et le risque acceptable dépend des enjeux, surtout pour une décision unique. Comme tous ces calculs se font dans le cadre, la partie 2 se demande ce qui peut avertir à temps que le cadre a omis l’essentiel.

Impression générale : texte clair, bien enchaîné, très peu de gêne. Les constats ci-dessous sont peu nombreux et majoritairement mineurs.

## Constats

### Gravité A

Aucun.

### Gravité B

**B1.** « Une déduction ne vaut que si ses prémisses sont vraies »
- Gêne : « vaut » a deux lectures. (a) La conclusion d’une déduction n’est garantie vraie que si les prémisses le sont (lecture probable, cohérente avec « aucun ne livre de conclusion sans condition ») ; (b) la déduction n’est *valide* que si les prémisses sont vraies — ce qui serait faux pour un lecteur formé en logique, la validité étant indépendante de la vérité des prémisses. Le second sens risque d’être lu comme une erreur.
- Reformulation minimale : « Une déduction ne garantit sa conclusion que si ses prémisses sont vraies ».
- Sens : bouge si l’auteur visait autre chose que la lecture (a) ; je ne tranche pas, mais (a) semble l’intention.

**B2.** « Comme une probabilité se partage ainsi entre plusieurs issues, la survenue de l’une d’elles ne permet guère de la juger »
- Gêne : « la » peut renvoyer à « une probabilité » (lecture la plus naturelle vu l’exemple de la pluie) ou à « l’une d’elles » (l’issue). Par ailleurs, la phrase précédente parle de « situations », celle-ci d’« issues » : glissement de terme qui laisse un instant hésiter s’il s’agit de la même chose. Enfin, c’est la confiance, non la probabilité, qui « se partage ».
- Reformulation minimale : « Comme la confiance se répartit ainsi entre plusieurs issues, la survenue de l’une d’elles ne suffit guère à juger la probabilité annoncée ».
- Sens : stable si l’on retient la lecture « juger la probabilité » ; si l’auteur voulait autre chose, à vérifier.

**B3.** « et avoir raison en moyenne ne protège de rien »
- Gêne : « avoir raison en moyenne » sonne comme un calque (« being right on average ») et suppose la notion d’espérance / de décision bonne en moyenne, non introduite ici (possible dépendance au ch. 4). « ne protège de rien » est par ailleurs plus absolu que ce que la phrase démontre (on attend « ne protège pas de cette issue »).
- Reformulation minimale : « et une décision qui serait gagnante en moyenne sur de nombreux essais ne protège pas de cette issue ».
- Sens : peut bouger légèrement — « de rien » (portée générale) vs « de cette issue » (portée restreinte) ; deux lectures plausibles, ne pas trancher sans l’auteur.

### Gravité C

**C1.** « Encore faut-il savoir ce qu’exprime une probabilité. »
- Gêne : « Encore faut-il » annonce une condition préalable à ce qui précède, mais le paragraphe précédent porte sur le cadre, non sur les probabilités ; la transition est un peu abrupte (le lien implicite est : « les modèles du cadre sont souvent probabilistes »).
- Reformulation minimale : « Reste à savoir ce qu’exprime une probabilité, outil central de ces modèles. »
- Sens : stable.

**C2.** « quelles variables, quelles catégories et quels modèles compteront »
- Gêne : « compteront » peut se lire « seront pris en compte » ou « auront de l’importance » ; nuance faible. « Variables » et « modèles » employés sans définition (possible dépendance, sans gravité pour un lecteur cultivé).
- Reformulation minimale : « … seront pris en compte ».
- Sens : stable dans les deux lectures.

**C3.** « Cette première partie réunit les outils qui permettent de raisonner et de décider dans ces conditions »
- Gêne : « dans ces conditions » renvoie à toute la phrase précédente (agir d’après une représentation, le monde répondant) ; compréhensible, mais légèrement vague, et le mot « conditions » est repris au paragraphe suivant dans un autre sens (conditions de validité d’une conclusion).
- Reformulation minimale : « … de raisonner et de décider dans cette situation ».
- Sens : stable.

**C4.** Typographie : les espaces avant « : », « ; », « ? » et entre « 100 » et « °C » sont des espaces ordinaires (U+0020), non insécables. Sans traitement automatique à la composition (babel-french, etc.), risque de ponctuation rejetée en début de ligne.
- Correction : espace fine insécable (U+202F) avant « ; ? », insécable (U+00A0) avant « : » et dans « 100 °C », sauf si la chaîne de composition s’en charge.

## Décompte

- A : 0
- B : 3
- C : 4
