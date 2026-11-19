# Lecture fraîche — Chapitre 6 « Détecter une erreur : comparateurs et cinq conditions »

Lecteur : Opus, première lecture, sans autre fichier que `chapitres/06-detecter-une-erreur.md`.

## 1. Résumé de ce que j'ai compris (test de lisibilité)

1. Une affirmation (sortie de modèle, prévision, mesure) ne montre pas d'elle-même qu'elle est fausse : pour déceler une erreur, il faut la confronter à un comparateur (une autre affirmation, un texte fixé à l'avance ou une observation). Cette confrontation s'appelle un contrôle.
2. Pour qu'un contrôle arrête une erreur, cinq conditions doivent être réunies en même temps : un comparateur existe, il peut se tromper autrement, les deux termes sont comparables, le désaccord arrive à temps, et quelqu'un en prend acte et a l'autorité d'agir.
3. La probabilité d'échappement (une erreur atteint l'action sans être arrêtée) est distincte du taux d'erreur P(E). Si une condition manque entièrement pour une famille d'erreurs, elle vaut 1, quel que soit P(E). Le chapitre 9 la quantifiera.
4. *Challenger* : le comparateur existait et arrivait à temps, mais le graphique tronqué (vols sans dommage omis) a ruiné la différence et la comparabilité, et l'objection des ingénieurs n'a pas été prise en compte.
5. Asymétrie : un désaccord prouve qu'au moins un des deux termes est faux (sans dire lequel), alors qu'un accord ne prouve quelque chose que si le comparateur pouvait réellement contredire l'affirmation.

Le fil général se suit bien. Les points d'achoppement tiennent surtout à la définition de la probabilité d'échappement, à la métaphore des barrages et à quelques référents flous.

## 2. Constats classés par gravité

### Gravité A : compréhension compromise ou contresens possible

**A1. § Taux d'erreur et probabilité d'échappement, définition `def:echappement`**
Passage : « La **probabilité d'échappement** est la probabilité qu'une affirmation fausse débouche sur une action sans avoir été contredite à temps. »
Problème : la définition parle d'une erreur « contredite », alors que la condition 5 et l'événement $D$ (« détectée et prise en compte avant l'action ») exigent davantage. Or dans *Challenger*, l'affirmation a bien été contredite à temps par les ingénieurs. Prise à la lettre, la définition ne compte donc pas ce cas comme un échappement, ce qui contredit l'affirmation selon laquelle l'échec de la cinquième condition donne un échappement égal à 1. La même formule revient au § formel (« atteindre l'action sans avoir été contredite à temps »). En revanche, le § 73 dit « sans contradiction utile », ce qui va dans l'autre sens.
Reformulation minimale : « …sans qu'un désaccord ait été détecté et pris en compte à temps. » On peut aussi garder la formule et ajouter « contredite à temps de façon suivie d'effet ». Le sens ne bouge pas si l'intention est bien celle de l'événement $D$. Il faut appliquer la même correction à la ligne du § formel.

**A2. § Cinq conditions, légende de la figure et paragraphe qui la suit**
Passage : « les cinq conditions agissent comme cinq barrages placés l'un derrière l'autre […] si un seul barrage manque ou cède devant un type d'erreur donné, toute erreur de ce type traverse le contrôle sans obstacle. »
Problème : pour un lecteur cultivé, des barrages successifs sont redondants. Si l'un cède, les suivants retiennent encore l'eau (c'est l'image courante de la « défense en profondeur »). Le texte veut dire l'inverse : les cinq conditions sont *conjointes*, et il suffit qu'une manque pour que tout passe. L'image installe donc l'intuition contraire à la thèse.
Reformulation minimale : « les cinq conditions agissent comme les cinq maillons d'une même chaîne : il suffit qu'un seul maillon manque ou cède devant un type d'erreur donné pour que toute erreur de ce type traverse le contrôle sans obstacle. » La légende de la figure (« cinq barrages successifs ») est à aligner, et peut-être le dessin lui-même. Le sens de l'argument ne bouge pas.

### Gravité B : gêne réelle

**B1. § Affirmation, contrôle et comparateur, définition `def:controle`**
Passage : « Un **contrôle** est la confrontation d'une affirmation à un comparateur censé concorder avec elle. »
Problème : « comparateur » est employé ici (et déjà dans le titre du chapitre et l'introduction) avant sa définition, qui vient juste après.
Reformulation minimale : placer la définition du comparateur avant celle du contrôle, en adaptant « ce à quoi l'on confronte une affirmation ». Le sens ne change pas.

**B2. § Cinq conditions, première phrase**
Passage : « Munis de ces trois termes, nous pouvons énoncer… »
Problème : la section précédente se termine sur les trois *familles* de comparateurs (« Cette tripartition »). Le lecteur peut donc croire que « ces trois termes » désigne ces familles, et non les trois notions définies (affirmation, contrôle, comparateur).
Reformulation minimale : « Munis de ces trois notions (affirmation, contrôle, comparateur), … ».

**B3. § Cinq conditions et Points clés : la proposition ne dit pas la même chose que les conditions qui en découlent**
Passages : la proposition dit « …et que quelqu'un en prend acte » ; la définition de la prise en compte dit « prenne acte d'un désaccord **et ait l'autorité pour agir** » ; le § formel dit « D'après la @prop:comparateur, une détection suivie d'effet exige la réunion simultanée des cinq conditions » ; le premier point clé dit « Une erreur n'est détectée **avant l'action** que lorsque… ».
Problème : la proposition ne mentionne ni l'autorité ni le délai, alors que le formel en tire les cinq conditions « d'après » elle et que le point clé y ajoute « avant l'action ». Le lecteur ne sait pas lequel des énoncés est le critère de référence. Le passage des trois éléments de la proposition aux cinq conditions n'est d'ailleurs jamais explicité (« elle fait apparaître cinq conditions »).
Reformulation minimale : aligner le point clé sur la proposition (supprimer « avant l'action »). Dans le formel, écrire « D'après la @prop:comparateur **et les cinq conditions qu'elle fait apparaître**, … ». Je ne tranche pas sur le fond : l'auteur peut aussi préférer enrichir la proposition.

**B4. § Cinq conditions, condition 2 (Différence)**
Passage : « Recalculer la même formule dans le même tableur débusque une erreur de saisie manuelle, mais non une faute dans la formule elle-même. »
Problème : on peut lire la phrase de deux façons. (a) On ressaisit les données et on relance la même formule, ce qui fait apparaître une faute de frappe. (b) On relance simplement le calcul, ce qui ne débusque rien, puisque la saisie fautive reste la même. La lecture (b) rend la phrase fausse.
Reformulation minimale, si (a) est voulu : « Ressaisir les données dans la même formule du même tableur débusque une erreur de saisie… ». Le sens dépend de la lecture retenue.

**B5. § Cinq conditions, définition `def:prise-en-compte`**
Passage : « La **prise en compte** est le fait que… »
Problème : le terme est employé avant d'être défini, au § « Disons-le sans détour » (« une prise en compte ») et comme intitulé de la condition 5.
Reformulation minimale : à la première occurrence, ajouter « (notion définie plus bas) », ou accepter l'écart, qui est court.

**B6. § Cinq conditions, paragraphe qui suit la définition de la prise en compte**
Passages : « il faut que **cette personne** *ait l'autorité pour agir* » puis « ne dispose ni du pouvoir de bloquer l'opération **ni de l'écoute de celui qui décide** ».
Problème : la définition semble exiger que la même personne prenne acte et ait l'autorité. L'exemple admet au contraire qu'il suffise que celui qui constate soit écouté par celui qui décide, ce qui fait intervenir deux personnes. Les deux lectures sont plausibles.
Reformulation minimale : « …que le désaccord parvienne à quelqu'un qui *ait l'autorité pour agir* ». Le sens bouge si l'auteur voulait vraiment une seule personne : c'est à trancher par lui.

**B7. § Taux d'erreur et probabilité d'échappement, avant-dernier paragraphe**
Passage : « un comparateur ne décèle qu'une fraction des fautes, produit parfois des désaccords injustifiés sur des affirmations exactes, ou n'est suivi d'effet qu'une partie du temps. La probabilité d'échappement prend alors des valeurs intermédiaires »
Problème : les fausses alertes sur des affirmations *exactes* ne modifient pas la probabilité d'échappement, puisque celle-ci porte sur des affirmations *fausses*. Le connecteur « alors » les présente pourtant comme une cause de valeurs intermédiaires.
Reformulation minimale : sortir ce membre de l'énumération, par exemple : « …ou n'est suivi d'effet qu'une partie du temps (il peut aussi, à l'inverse, signaler à tort des affirmations exactes). » Le sens est conservé si l'auteur ne voulait pas lier les fausses alertes à l'échappement.

**B8. § formel, premier paragraphe**
Passage : « de probabilité $P(E) = \Pr(E) > 0$ »
Problème : deux notations désignent la même chose, ce qui laisse croire à une nuance qui n'existe pas. Le texte passe ensuite à $\Pr$ seul.
Reformulation minimale : « de probabilité $P(E) > 0$ (que l'on notera aussi $\Pr(E)$) ». On peut aussi expliquer que $P(E)$ est le nom du taux d'erreur et $\Pr$ l'opérateur de probabilité.

**B9. § formel, premier paragraphe**
Passage : « un contrôle particulier chargé de **l'**examiner avant qu'une action soit engagée »
Problème : le pronom peut renvoyer à « l'affirmation » ou à « la sous-classe d'erreurs ».
Reformulation minimale : « chargé d'examiner l'affirmation avant… ».

**B10. § formel, avant la dernière équation**
Passage : « La probabilité conditionnelle qu'une erreur de la sous-classe $E_k$ échappe à ce contrôle — c'est-à-dire l'événement contraire $\overline{D}$, atteindre l'action sans avoir été contredite à temps — vaut donc »
Problème : l'apposition assimile une probabilité à un événement. Elle reprend aussi la formule « contredite à temps » (voir A1).
Reformulation minimale : « La probabilité conditionnelle qu'une erreur de la sous-classe $E_k$ échappe à ce contrôle, c'est-à-dire la probabilité de l'événement contraire $\overline{D}$ (atteindre l'action sans avoir été détectée et prise en compte à temps), vaut donc ».

**B11. § Le cas Challenger, puce « Différence »**
Passage : « En n'affichant que les vols affectés de dommages, le graphique a sélectionné un sous-ensemble qui ne pouvait plus contredire clairement la confiance affichée… »
Problème : la condition 2 a été définie comme une *cause d'erreur commune* qui fausse l'affirmation et le comparateur de la même manière. Le lecteur ne voit pas quelle cause commune est en jeu ici. Une sélection des données ressemble plutôt à un défaut de comparabilité, voire d'existence. Le lien avec la définition reste implicite.
Reformulation minimale : expliciter le lien en une incise, par exemple « …un sous-ensemble qui, comme l'affirmation, laissait hors de vue l'effet du froid, et ne pouvait donc plus contredire… ». Le sens risque de bouger : c'est à l'auteur de dire quelle « cause commune » il vise.

**B12. § Le cas Challenger, puce « Comparabilité », dernière phrase**
Passage : « Les graphiques ne rapprochaient pas dans une forme lisible ce que les vols antérieurs montraient de la température prévue pour le lendemain. »
Problème : la phrase a deux constructions possibles. (a) « rapprocher X de Y » : rapprocher les enseignements des vols passés de la température prévue. (b) « ce que les vols montraient de la température » : ce qu'ils montraient *au sujet de* la température. La phrase reste alors sans complément.
Reformulation minimale, pour la lecture (a) : « Les graphiques ne mettaient pas en regard, sous une forme lisible, ce que montraient les vols antérieurs et la température prévue pour le lendemain. »

**B13. § Ce que montrent un désaccord et un accord, deuxième paragraphe**
Passage : « **Le premier calcul** peut comporter une erreur de modélisation ou de codage ; mais le comparateur peut lui aussi être fautif, parce que le calcul à la main… »
Problème : dans la phrase d'exemples qui précède, le premier calcul *cité* est le calcul à la main. « Le premier calcul » pourrait donc désigner le comparateur, alors qu'il désigne l'affirmation (le modèle par éléments finis).
Reformulation minimale : « L'affirmation elle-même (par exemple le modèle par éléments finis) peut comporter… ».

**B14. § Ce que montrent un désaccord et un accord, dernier paragraphe**
Passage : « puisqu'il démontre qu'un des deux côtés au moins **fait défaut** »
Problème : il y a un faux sens. « Faire défaut » signifie « manquer », sens dans lequel le chapitre l'emploie ailleurs (« l'une des conditions fait défaut »), et non « être erroné ».
Reformulation minimale : « qu'un des deux côtés au moins est erroné ».

### Gravité C : confort et style

**C1. § Introduction.** « …gardent **donc** le silence, ne laisse aucune trace chiffrée. Une estimation ou un calcul peut **donc** être faux… » : deux « donc » se suivent de près. On peut supprimer le premier.

**C2. § Introduction.** « un ensemble d'**alternatives** admises à l'avance » : c'est un anglicisme courant (*alternatives* au sens d'options), mais on peut lire « options » ou « hypothèses concurrentes ». La notion vient du chapitre 5 : c'est une possible dépendance.

**C3. § Affirmation…, définition `def:affirmation`.** « la **réponse** d'un modèle » : le mot est probablement un calque de *model output*. Il entre en collision avec « la réponse du monde réel » deux lignes plus haut. On peut écrire « le résultat d'un modèle ».

**C4. § Affirmation…, phrase qui suit les définitions.** « **Cette définition** regroupe trois familles » : deux définitions précèdent. Écrire « La définition du comparateur regroupe… ».

**C5. § Affirmation…, famille 2.** Une « loi de conservation de l'énergie » est rangée sous « Un texte fixé à l'avance ». Un lecteur hésitera à appeler « texte » une loi physique. On peut écrire « à une règle, à une norme, à une loi physique ou à une spécification ». Aucune modification de contenu n'est nécessaire.

**C6. § Affirmation…, dernier paragraphe.** La « tripartition » est annoncée comme détaillée plus tard « en quatre sources distinctes ». Le passage de trois à quatre peut intriguer. Une incise suffirait (« en quatre sources, dont l'une dédouble… ») si l'auteur le souhaite. Sinon, laisser.

**C7. § Cinq conditions.** Le paragraphe « Disons-le sans détour : … presque définitionnelle … grille d'examen » et l'encadré *nuance* (« presque définitionnelle … grille d'examen qu'elle déploie ») disent deux fois la même chose, presque dans les mêmes mots, à quinze lignes d'écart. On peut alléger l'un des deux.

**C8. § Cinq conditions, condition 3.** « Comparer une poussée calculée en livres-force à une limite exprimée en newtons, […] **sans en préciser les conditions** interdit… » : la phrase est longue, et « sans en préciser les conditions » semble ne porter que sur le dernier exemple. Les deux premiers paraissent alors anodins, puisqu'une conversion suffit. On peut ajouter « sans conversion » au premier, ou couper la phrase.

**C9. § Cinq conditions, condition 4.** « une fois le public **engagé** » : on comprend « une fois le public engagé sur la passerelle », mais le mot est vague. Écrire « une fois le public sur la passerelle ».

**C10. § Taux d'erreur…, premier paragraphe.** « un poids de jugement accordé aux **mondes possibles** » : la notion n'est pas définie ici. C'est une possible dépendance du chapitre 3.

**C11. § Taux d'erreur…, deuxième paragraphe.** « un outil sujet à des erreurs fréquentes […] **expose moins** qu'un outil plus exact » : l'emploi intransitif de « expose » est elliptique. On peut écrire « fait courir moins de risque que… ». Dans le même paragraphe, le taux d'erreur, défini pour *une affirmation*, est appliqué à « une équipe ou un système ». Le glissement est léger.

**C12. § Taux d'erreur…, troisième paragraphe, et Points clés.** « Peu importe alors que le taux d'erreur $P(E)$ soit de 10 %… » : $P(E)$ porte sur toutes les erreurs, alors que le raisonnement porte sur une famille ($E_k$). Le lecteur attentif se demandera lequel des deux taux est visé. On peut écrire « que ces erreurs soient fréquentes ou rares ». La vérité de l'énoncé n'est pas en cause.

**C13. Vocabulaire flottant pour le même objet.** Le texte parle de « famille d'erreurs » (§ échappement, légende), de « type d'erreur » (§ figure), de « sous-classe » (formel) et de « classe d'erreurs » (Points clés). Il vaudrait mieux harmoniser, ou dire une fois que ces mots sont équivalents.

**C14. § formel, liste des $C_j$.** Plusieurs écarts de formulation séparent les événements des conditions énoncées plus haut. $C_1$ dit « existe et est **mobilisé** » au lieu de « existe et soit **disponible** ». $C_5$ dit « **exerce** l'autorité » au lieu de « **ait** l'autorité ». « pour **l'épisode** considéré » emploie un mot qui n'a pas été introduit. Ces écarts sont minimes, mais ils posent la question de savoir si l'on parle de la même chose.

**C15. § Le cas Challenger, premier paragraphe.** « une faute humaine **d'organisation** » : l'alliance est un peu étrange. On peut écrire « une faute humaine ou d'organisation ».

**C16. § Le cas Challenger, deuxième paragraphe et puce « Prise en compte ».** « la **rupture** conjointe de la différence, de la comparabilité… » et « La cinquième condition **a rompu** » : une condition « rompt » mal en français. Ailleurs, le chapitre emploie « céder » ; il vaudrait mieux s'y tenir.

**C17. § Le cas Challenger, encadré.** « Privées de ce groupe de comparaison et présentées **sans aligner** l'ensemble des vols » : le sujet implicite (les données) ne peut pas « aligner ». On peut écrire « présentées sans que l'ensemble des vols soit aligné… ». Dans le même encadré, « **la direction** demanda » ne dit pas s'il s'agit de la NASA ou de Morton Thiokol. Je ne tranche pas : il suffit de préciser.

**C18. § Le cas Challenger, dernier paragraphe.** « d'autre part l'autorité et la disposition à retenir une objection » : l'autorité manquait aux ingénieurs, la disposition manquait à la hiérarchie, mais la phrase les fond en un seul sujet. Par ailleurs, la phrase finale (« Réduire l'épisode… dossier mutilé ») est dense, avec une double hypothèse contrefactuelle. On gagnerait à la couper en deux.

**C19. § Ce que montrent un désaccord et un accord.** « au moins l'un des **deux termes** est faux » : plus haut, « terme de comparaison » désignait le seul comparateur. Ici, « les deux termes » désigne l'affirmation et le comparateur. Écrire « l'affirmation ou le comparateur, au moins, est faux ».

**C20. § Ce que montrent un désaccord et un accord.** « délivre une **signature**, non une preuve » : la métaphore (un visa administratif) est compréhensible, mais « signature » a aussi un sens technique (une trace caractéristique). « un simple visa » ou « un paraphe » lèverait l'hésitation.

**C21. Points clés, 4ᵉ puce.** « a privé l'analyse **de différence et de comparabilité** » : la tournure se lit mal. On peut écrire « a fait céder les conditions de différence et de comparabilité ».

### Possibles dépendances (notions utilisées sans définition dans le chapitre)

- « cadre » (@def:cadre), « alternatives admises à l'avance », @prop:desaccord : chapitre 5.
- « mondes possibles », « historique » (@sec:ch03-calibration-historique) : chapitre 3.
- « décision unique » (@sec:ch04-decision-unique) : chapitre 4.
- « monotonie des probabilités » (@sec:ch01-probabilite) : chapitre 1.

Dans le contexte, toutes se laissent deviner suffisamment, sauf peut-être « mondes possibles ».

### Typographie

Je n'ai relevé aucune faute typographique manifeste (guillemets, espaces insécables avant « % » et « : », majuscules). Pour « lorsque aucune », l'absence d'élision est admise.

## 3. Appréciation globale

Le chapitre est bien construit et progressif : définitions, puis principe, puis conditions, puis grandeur, puis cas, puis asymétrie. Les exemples de la vie courante, mis en regard des exemples techniques, aident beaucoup.

- **Sections les plus accessibles :** « Affirmation, contrôle et comparateur » et « Ce que montrent un désaccord et un accord ». Les exemples sont clairs et l'asymétrie est bien mise en scène, à la réserve près du faux sens « fait défaut » (B14).
- **Sections les moins accessibles :**
  - « Taux d'erreur et probabilité d'échappement ». La définition est en décalage avec la condition 5 (A1). L'énumération mélange fausses alertes et échappement (B7). L'encadré formel a une double notation et des écarts de formulation (B8 à B10, C14).
  - La métaphore des barrages, dans « Cinq conditions » (A2), va contre la thèse.
  - Dans *Challenger*, le lien avec la condition de « différence » reste implicite (B11).
