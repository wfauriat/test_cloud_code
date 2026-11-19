# Lecture fraîche, chapitre 5 : « Trois incertitudes, et ce que mesure une barre d’erreur »

Fichier lu : `chapitres/05-trois-incertitudes.md` (seul fichier consulté).

## 1. Ce que j’ai compris (test de lisibilité)

La loi de la variance totale décompose l’incertitude sur une grandeur $Y$ en deux termes, calculés sur un ensemble d’alternatives admises $\Theta$ : la dispersion moyenne propre à chaque alternative (incertitude aléatoire) et l’écart entre les prévisions moyennes des alternatives (incertitude épistémique). La frontière entre ces deux parts est un choix de modélisation, comme le montre le dé. Une troisième incertitude, dite ontologique, porte sur le cadre lui-même (variables, catégories, classe de modèles) ; elle n’est pas une quantité calculable : une alternative jamais admise ne produit aucun désaccord, donc aucune barre d’erreur (exemples : la dinde de Russell, le risque hypothécaire avant 2008). Un facteur omis ne laisse aucune trace s’il est resté constant ; s’il a varié, il gonfle le bruit sans être identifié. Les coefficients de sécurité et les outils de robustesse restent dans le cadre (exemple : la ferrure exposée à la corrosion), et le cas Challenger montre une situation mixte, entre défaut de représentation des données et objection écartée.

Le fil principal se suit bien. Les gênes viennent surtout du flottement du mot « désaccord », de quelques passages elliptiques (2008, Challenger, encadré formel) et de la dernière section, dont l’enchaînement vers Challenger est faible.

## 2. Constats classés par gravité

### Gravité A (compréhension compromise ou contresens possible)

**A1. §« La loi de la variance totale » contre §« Une barre d’erreur mesure un désaccord » (et introduction, Points clés) : sens flottant de « désaccord ».**
- Passages : §1, « séparant ce qui tient à la variabilité attendue sous une hypothèse donnée de ce qui tient au désaccord entre les hypothèses » ; @prop:desaccord, « Tout énoncé quantitatif d’incertitude résume à quel point les membres d’un ensemble spécifié d’alternatives admises sont en désaccord » ; introduction, « toute barre d’erreur mesure uniquement le désaccord à l’intérieur d’un ensemble d’alternatives admises ».
- Ce qui gêne : en §1, « désaccord » ne désigne que le terme épistémique (second terme). La proposition l’applique ensuite à *toute* incertitude chiffrée, y compris le terme aléatoire, qui est une dispersion *interne* à chaque alternative et non un désaccord entre elles (le §4 le dit lui-même : « Du côté aléatoire, on mesure comment varient des tirages […] sous une même loi admise »). Le lecteur peut donc comprendre la proposition comme portant seulement sur le terme épistémique.
- Deux lectures plausibles, que je ne tranche pas : (a) « désaccord » au sens large, qui couvre aussi la variabilité des tirages sous une même loi ; (b) « désaccord » au sens strict de §1, auquel cas la proposition semble laisser de côté le terme aléatoire.
- Reformulation minimale, qui ne vaut que pour la lecture (a) : en §1, remplacer « au désaccord entre les hypothèses » par « à l’écart entre les prévisions des hypothèses », puis ajouter après l’énoncé de la proposition une phrase du type « Le mot désaccord s’entend ici au sens large : variabilité des tirages sous une loi admise comme écart entre alternatives admises. » Si l’auteur visait (b), c’est la proposition qu’il faudrait reformuler, et le sens changerait.

### Gravité B (gêne réelle)

**B1. §« L’incertitude ontologique » : « La question n’est plus « quelle est la valeur de $X$ ? », ni « mes barres d’erreur sur $Y$ sont-elles étroites ou larges ? ». »**
- Ce qui gêne : jusqu’ici, les incertitudes aléatoire et épistémique portaient sur $Y$ et sur $\theta$, jamais sur la valeur de $X$. La première question ne renvoie à rien de ce qui précède, et l’on bute dessus.
- Reformulation : « quelle est la valeur de $\theta$ ? ». Attention : si $X$ est voulu (incertitude de mesure sur les variables du cadre), le sens change. Ne pas trancher sans l’auteur.

**B2. §« L’incertitude ontologique » : « Au-delà de leurs nuances propres, ces travaux visent le même écart fondamental. »**
- Ce qui gêne : on ne sait pas entre quoi et quoi se situe cet « écart ».
- Reformulation : « ces travaux visent la même chose : un doute qui porte sur le cadre lui-même, et non sur les valeurs calculées à l’intérieur. »

**B3. §« L’incertitude ontologique » : « les matins tranquilles départagent déjà mal un fermier toujours bienveillant d’un danger quotidien minime. »**
- Ce qui gêne : « départager A de B » n’est pas idiomatique (on départage deux candidats). C’est un calque probable de « distinguish A from B ».
- Reformulation : « les matins tranquilles distinguent déjà mal un fermier toujours bienveillant d’un danger quotidien minime. »

**B4. §« L’incertitude ontologique » : « les modèles d’évaluation du risque […] n’ont pas signalé le danger de défauts corrélés à l’échelle nationale par des intervalles de confiance très larges : ils ne produisaient tout simplement pas ce scénario ».**
- Ce qui gêne : la portée de la négation est ambiguë. On peut d’abord lire « ils ont signalé le danger, mais pas au moyen d’intervalles larges ». Seule la suite rétablit le sens.
- Reformulation : « n’ont pas signalé le danger […] en affichant des intervalles de confiance très larges ; ils ne produisaient tout simplement pas ce scénario. » Le sens ne bouge pas.

**B5. §« Une barre d’erreur mesure un désaccord », phrase d’ouverture : « Pourquoi ce que le cadre laisse de côté ne se traduit-il pas par des barres d’erreur prudemment élargies, mais disparaît-il purement et simplement du tableau ? »**
- Ce qui gêne : quelques paragraphes plus loin, la puce 2 et l’encadré « nuance » établissent qu’un facteur omis qui a varié élargit bel et bien les barres d’erreur. La question pose donc une prémisse que le texte corrige ensuite (le même problème touche « uniquement » dans l’introduction).
- Reformulation : « Pourquoi ce que le cadre laisse de côté ne se traduit-il pas, en général, par des barres d’erreur prudemment élargies […] ? » ou « ne se traduit-il pas *à coup sûr* par… ». Le sens est légèrement nuancé, sans toucher à l’argument.

**B6. §« Une barre d’erreur mesure un désaccord » : « dire qu’un facteur omis par le cadre ne figure pas dans $\Theta$ ne signifie pas… ».**
- Ce qui gêne : $\Theta$ a été défini comme un ensemble d’*hypothèses ou de modèles*, et les *variables* relèvent du cadre ($X$). Dire qu’un *facteur* « figure dans $\Theta$ » mêle deux niveaux que le §3 venait de distinguer.
- Reformulation : « dire qu’un facteur omis par le cadre n’intervient dans aucune des alternatives de $\Theta$ ne signifie pas… ».

**B7. Encadré « Ce que pèse la décomposition de la variance » : « sa variance s’est ajoutée à la dispersion résiduelle estimée ».**
- Ce qui gêne : « sa » renvoie grammaticalement à $z$, alors que c’est la variance de l’*effet* de $z$ sur $Y$ qui s’ajoute.
- Reformulation : « la variance de son effet sur $Y$ s’est ajoutée… ». C’est une clarification, mais l’auteur doit confirmer que c’est bien ce qu’il veut dire.

**B8. Même encadré : « aucune variation de la valeur présente de $z$ n’affecte le terme épistémique ».**
- Ce qui gêne : « présente » peut se lire « actuelle » (au moment de la prévision) ou « existante ». Le contraste avec « données passées », dans la phrase suivante, suggère « actuelle », mais il faut deviner.
- Reformulation : « aucune variation de la valeur actuelle de $z$ (au moment de la prévision) n’affecte… ». Le sens ne bouge pas si c’est bien la lecture voulue.

**B9. §« Pourquoi les outils de robustesse… » : « éventuellement la fatigue mécanique dans l’air sec — […] ou à une baisse de la limite de l’alliage ».**
- Ce qui gêne : « la limite de l’alliage » est elliptique pour un non-spécialiste (limite élastique ? limite de rupture ?).
- Reformulation : « une baisse de la limite de résistance de l’alliage ». Si l’auteur vise la limite d’élasticité, le terme précis change.

**B10. §« Pourquoi les outils de robustesse… », passage vers Challenger : « Avant d’examiner au @sec:ch06 comment des erreurs […] peuvent malgré tout être repérées à temps, une nuance s’impose sur un accident célèbre… ».**
- Ce qui gêne : (i) l’enchaînement est faible, car la nuance Challenger ne parle pas des outils de robustesse, sujet de la section ; (ii) la construction est bancale, le sujet implicite d’« examiner » (nous) n’étant pas celui de la principale (une nuance) ; (iii) l’annonce du chapitre 6 diffère de celle qui clôt l’encadré (« pourquoi il ne suffit pas qu’une erreur […] soit connue de quelqu’un »).
- Reformulation : « Avant d’examiner au @sec:ch06 comment des erreurs […] peuvent malgré tout être repérées à temps, nuançons la lecture d’un accident célèbre, souvent présenté trop vite comme un pur défaut de cadre. »

**B11. Encadré Challenger : « L’examen du dossier révèle en réalité une situation mixte ».**
- Ce qui gêne : on ne dit pas de quoi la situation est mélangée. Le lecteur ne sait pas quelle part relève du cadre (incertitude ontologique) et quelle part n’en relève pas.
- Reformulation : « une situation mixte : une défaillance dans la représentation des données, d’une part, et une objection exprimée mais écartée, d’autre part. » Cela reprend ce que dit l’encadré, sans toucher à l’argument.

**B12. Encadré Challenger : « le graphique des joints toriques des propulseurs à poudre examiné pendant la réunion ne montrait que les vols antérieurs… ».**
- Ce qui gêne : la chaîne de compléments du nom est elliptique, car on ne sait pas ce que le graphique met en relation.
- Reformulation : « le graphique des dommages subis par les joints toriques en fonction de la température, examiné pendant la réunion, ne montrait que… ». C’est ma lecture, inférée de la suite (« tendance liée à la température extérieure ») ; l’auteur doit la confirmer.

**B13. Points clés, puce 4 : « sans pouvoir être nommé ni extrapolé à un contexte nouveau ».**
- Ce qui gêne : ce n’est pas le facteur qui serait « extrapolé ». Le corps du texte (encadré « nuance ») dit que la dispersion mesurée ne protège pas contre un changement durable du facteur. La formulation du point clé ne correspond pas exactement au corps.
- Reformulation : « sans pouvoir être nommé, et sans protéger contre un changement durable de ce facteur dans un contexte nouveau. »

### Gravité C (confort, style)

- **Introduction**, « Le lecteur qui suit l’un des parcours de la @sec:ch00-parcours pourra s’y reporter au besoin. » : « s’y » peut renvoyer aux chapitres cités ou au parcours. Proposition : « pourra se reporter au besoin à ces chapitres. »
- **Introduction**, première phrase : la notation $A \cap (\dots) \rightarrow B$ et quatre renvois en une phrase forment une entrée dense pour un lecteur cultivé. Possible dépendance (chapitre 1). On pourrait couper après « (@sec:ch01) ».
- **§1** : $\mathrm{Var}(Y)$ et $\mathbb{E}$ sont utilisés avant l’encadré « outils » qui les définit, et les indices $\mathbb{E}_\theta$, $\mathrm{Var}_\theta$ (« par rapport à la loi sur $\theta$ ») ne sont jamais explicités. Proposition : ajouter « (l’indice $\theta$ signifie que la moyenne ou la variance est prise sur les alternatives de $\Theta$, avec leurs poids) ».
- **§1**, « la dispersion des issues qu’elle continue de juger possibles » : « continue de » est étrange, puisqu’il n’y a pas de « avant ». Proposition : « qu’elle juge encore possibles » ou « qu’elle laisse possibles ».
- **Encadré « outils »**, dernière étape du calcul : seul le sort du second terme est indiqué ; que le premier devienne $\mathbb{E}_\theta[\mathrm{Var}(Y\mid\theta)]$ et le membre de gauche $\mathrm{Var}(Y)$ reste implicite. Une demi-phrase suffirait : « le premier devient $\mathbb{E}_\theta[\mathrm{Var}(Y \mid \theta)]$ et le membre de gauche $\mathrm{Var}(Y)$ ».
- **§2 et suivantes** : flottement lexical entre « poids de probabilité », « loi de probabilité », « distribution sur $\theta$ » et « pondération » pour désigner la même chose. Proposition : s’en tenir à « poids » ou à « loi ».
- **§2**, « La frontière entre l’une et l’autre est fonctionnelle, et non métaphysique » : « fonctionnelle » est vague, même si la suite de la phrase l’éclaire. Pas de changement nécessaire si l’auteur y tient.
- **§2**, « tirages de Monte-Carlo » ; **§4**, « tirages *a posteriori* », « ajustements par rééchantillonnage » : jargon statistique non glosé (possible dépendance).
- **§3**, phrase Wynne / Walker / Lempert / Knight : quatre auteurs et quatre étiquettes en une phrase. On pourrait la couper en deux, après « [@lempert2003] ».
- **§3**, parenthèse « (Toutes les erreurs inaperçues ne viennent pas du dehors […]) » : elle casse le fil juste avant l’exemple de 2008. On pourrait la déplacer en note ou à la fin de la section.
- **§3**, le paragraphe sur 2008 et l’encadré « cas » qui le suit disent deux fois la même chose (« ne figurait pas dans la structure » / « un mécanisme de couplage que le cadre n’admettait pas »). On pourrait alléger le paragraphe.
- **Encadré 2008** : « tranches les mieux notées » et « queue extrême » sont du jargon (titrisation, queue de distribution). Par ailleurs, « d’un État à l’autre » suppose que le lecteur sait qu’il s’agit des États-Unis. Proposition : « d’un État américain à l’autre ».
- **§3**, « tout ce que ce découpage laisse en dehors » : le « découpage » n’a pas été nommé ainsi. Proposition : « tout ce que le cadre laisse en dehors ».
- **@prop:desaccord**, statut « résultat sous hypothèses » : les hypothèses ne sont pas rappelées à proximité, et on ne les trouve que dans l’encadré formel. On pourrait ajouter un renvoi.
- **§4**, « Une hypothèse absente de $\Theta$ y reçoit un poids nul » : le référent de « y » (l’équation ou $\Theta$) est flou. Proposition : « reçoit un poids nul dans ces moyennes ».
- **§4**, image du comité, « S’ils tombent unanimement d’accord — ou s’ils ne divergent que […] —, leur accord mesure… » : « leur accord » ne couvre pas le cas de divergence. Proposition : « leur accord, ou leur faible désaccord, mesure… ».
- **§4**, « son traitement formel attendra le @sec:ch07 » : l’encadré formel qui suit donne déjà un traitement formel de $z$. Proposition : « son traitement complet attendra… ».
- **Encadré formel**, « Deux propriétés découlent immédiatement » : quatre affirmations suivent (deux propriétés, puis deux cas). Gêne légère.
- **Encadré « nuance »**, « ne laisse littéralement aucune trace dans l’écart calculé » : « écart » peut se lire « écart-type » ou « différence ». Proposition : « dans l’écart-type calculé » ou « dans la barre d’erreur calculée ».
- **§5**, « des défenses éprouvées pour élargir ses estimations » : calque probable (« widen its estimates ») ; ce sont les marges ou les intervalles que l’on élargit. Proposition : « pour élargir ses marges d’incertitude ».
- **§5**, « sur un seul modèle, trop étroitement ajusté aux observations passées » : la virgule fait porter « trop étroitement ajusté » sur le seul modèle et non sur le jeu de paramètres. Probablement voulu ; à vérifier.
- **§5**, « élargissent ou repondèrent » : néologisme. « Pondèrent à nouveau » serait plus sûr.
- **§5**, « Le danger ne vient donc pas du coefficient de sécurité ni des études » : proposition : « ne vient donc ni du coefficient de sécurité ni des études ».
- **§5**, « Une équipe qui voit passer une marge de 1,8 […] peut se croire déjà acquittée de l’incertitude ontologique » : le registre est un peu relâché (« voit passer »), et « acquittée de » est imprécis. Proposition : « Une équipe qui obtient une marge de 1,8 […] peut se croire quitte de l’incertitude ontologique. »
- **§5**, « ferrure » et « modes de ruine » sont des termes d’ingénieur non glosés (possible dépendance si le chapitre 0 les définit).
- **Encadré Challenger**, titre « représentation des données » : « représentation » est un terme technique défini au chapitre 2 (@def:representation), ici employé au sens courant. Risque léger de confusion.
- **Points clés, puce 5**, « ils élargissent les alternatives » : proposition : « ils élargissent ou pondèrent à nouveau l’ensemble des alternatives » (formulation du corps du texte).
- **Typographie** : rien de vraiment fautif (espaces avant « : ; ? », guillemets français et « 100 °C » sont corrects ; « mont Blanc » pour le sommet est conforme à l’usage).

### Possibles dépendances (termes non définis dans le chapitre)

Les termes suivants ne sont pas définis dans le chapitre et relèvent probablement de chapitres antérieurs :
- règle à arrière-plan ouvert $A \cap (\dots) \rightarrow B$ et @eq:ch01-regle ;
- formule des probabilités totales (@eq:ch01-totale) et forme « cotes » de la règle de Bayes (@eq:ch01-bayes-cotes) ;
- **représentation** et **cadre** (@def:representation, @def:cadre) ;
- variables $X$ du cadre (@sec:ch02-cadre-specification) ;
- tableau de l’eau bouillante (@tbl:ch02-eau-bouillante) ;
- argument des « matins tranquilles » (@sec:ch03-prevision-previsionniste) ;
- « probabilité comme jugement pesant des mondes possibles » (chapitre 3) ;
- exemple de la ferrure (chapitre 0).

Les termes en gras (ensemble des alternatives admises, incertitude aléatoire, épistémique, ontologique) sont tous définis avant leur usage technique, sauf « désaccord » (voir A1).

## 3. Appréciation globale

Le chapitre est bien construit et son argument central se suit. Les sections les plus accessibles sont « Incertitude aléatoire et incertitude épistémique » (l’exemple du dé est très clair), le début de « L’incertitude ontologique » (la dinde) et l’image du comité. Les moins accessibles sont l’encadré formel « Ce que pèse la décomposition de la variance » (référents flous, $z$ mal situé par rapport à $\Theta$) et la fin de « Pourquoi les outils de robustesse… », où l’encadré Challenger arrive sans lien net avec la section et reste elliptique sur ce qui, dans la « situation mixte », relève ou non du cadre. Le point le plus important à régler est le sens de « désaccord » (A1), qui conditionne la lecture de la proposition centrale.
