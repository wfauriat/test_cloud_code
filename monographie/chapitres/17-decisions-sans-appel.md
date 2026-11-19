# Décisions sans appel {#sec:ch17}

Le @sec:ch04 s’achevait sur une question laissée ouverte (@sec:ch04-question-ouverte) : comment décider quand l’enjeu est sans appel, alors que la règle de l’utilité espérée subjective ne consulte que les probabilités formées dans notre cadre ? Les parties suivantes ont montré pourquoi ce manque ne se répare pas de l’intérieur : aucun contrôle calculé dans le cadre ne décèle ce que le cadre omet (@prop:cause-commune), et l’automatisation transforme ces omissions en actes qui s’exécutent (@sec:ch14). Ce chapitre en tire des pratiques de décision, présentées avec leurs raisons et leurs limites plutôt que comme des règles. Il reprend la course à la voile pour définir la marge d’humilité, sépare ce que l’on peut calibrer de ce qu’il faut verrouiller, articule bacs à sable et verrous, et propose quatre questions à poser devant tout chiffre assuré, c’est-à-dire présenté avec assurance, sans ses conditions.

## La course à la voile revisitée {#sec:ch17-course-revisitee}

Retrouvons M. X et M. Y sur le quai, peu avant le départ de la course au large des chapitres [-@sec:ch03] et [-@sec:ch04] (@sec:ch04-course-voile). Tous deux hésitent entre un *voilier léger* et un *voilier renforcé*, pris comme option sûre, et font le même bilan des enjeux : une casse en mer imposerait un remorquage coûtant vingt-cinq fois ce que rapporterait le succès ($L/\Delta U = 25$). Le seuil de l’@eq:ch04-seuil vaut donc $p^\ast = 1/26$, soit environ 3,85 %. M. X estime la probabilité de casse du voilier léger à 5 % et renonce à le prendre ; M. Y l’estime à 0,1 % et s’apprête à partir.

Supposons d’abord que M. Y, avant le coup de canon, monte à bord inspecter le gréement et découvre une fissure à la base du mât. Sa représentation change aussitôt : ce qu’il vient de voir exclut les mondes possibles où le mât est sain, son estimation $p$ passe très au-dessus de 3,85 %, et il choisit le voilier renforcé. C’est la seconde voie décrite au @sec:ch07 (@sec:ch07-deux-voies), *découvrir par l’épreuve* : le contact avec le monde a fait entrer dans la représentation un facteur qui n’y figurait pas, et il est survenu avant l’acte, quand changer de bateau ne coûtait presque rien.

Supposons maintenant que la fissure existe, mais qu’elle soit cachée sous le manchon d’étambrai (la pièce qui entoure le mât à son passage dans le pont), que M. Y n’a ni démonté ni songé à soupçonner. Rien ne bouge dans sa représentation : son estimation reste à 0,1 %, bien au-dessous de 3,85 %, et il prend le départ sur le voilier léger. Or c’est le mât réel que la mer éprouve, non la fiche technique (@sec:ch02-monde-action). Si ce défaut, ou tout autre mécanisme laissé hors du cadre (@sec:ch07), ajoute une probabilité d’échec $z$ indépendante des causes déjà comptées dans $p$, le voilier n’arrive intact que s’il échappe à la fois aux périls représentés (probabilité $1 - p$) et au facteur omis (probabilité $1 - z$). La probabilité d’échec dans le monde, que nous appellerons le *risque réel* et noterons $p_w$, vaut donc :

$$p_w = 1 - (1 - p)(1 - z) = p + z - p\,z.$$ {#eq:ch17-risque-reel}

Tant que $p$ et $z$ restent petits, le risque réel est voisin de $p + z$ : il suffit que $z$ atteigne quelques points de pourcentage pour le porter au-delà du seuil $p^\ast$, même si $p$ paraissait infime. La règle de l’utilité espérée subjective décide sur $p$ ; l’issue obéit à $p_w$.

Le décideur ne peut pas observer un facteur qui ne figure ni dans ses variables ni dans ses instruments. Il ne lui reste qu’un levier : s’imposer une retenue avant de comparer son estimation au seuil. On appelle **marge d’humilité**, notée $b$, la marge que l’on ajoute délibérément à l’estimation du risque pour tenir compte de ce que la représentation pourrait omettre ; elle relève du jugement, non de la mesure. Au lieu de partir dès que $p < p^\ast$, le décideur applique le critère à $p + b$ et ne s’engage que si :

$$p + b < p^\ast.$$ {#eq:ch17-regle-marge}

Comment fixer $b$ sans prétendre mesurer l’inconnu ? Aucun calcul ne le dit, et aucun ne peut le dire, puisque $z$ échappe par définition à la représentation. Raisonner à l’envers (@sec:ch03-raisonner-envers) offre seulement une prise, déjà relevée au @sec:ch04 : l’écart $p^\ast - p$ indique quelle part de risque ignoré suffirait à renverser la décision, moins de quatre points de pourcentage pour M. Y, moins d’un centième de point pour le joueur de roulette russe. Choisir $b$, c’est juger si l’on est prêt à parier que la représentation n’omet rien d’aussi gros. Ce jugement doit être d’autant plus exigeant que le rapport des enjeux est élevé, que l’acte est irréversible ou que la conclusion basculerait au moindre changement du cadre. Il s’agit d’une pratique de travail, proposée comme telle [@fauriat2026frame], et non d’une règle démontrée : elle reste faillible, et rien ne garantit qu’une marge donnée couvrira un défaut massif.

En croisant la décision prise sur $p + b$ (partir si $p + b < p^\ast$, renoncer sinon) avec la position du risque réel par rapport au même seuil, on obtient quatre issues :

1. *Départ justifié* ($p + b < p^\ast$ et $p_w < p^\ast$) : le décideur part, et le risque réel, y compris ce que la représentation ignore, reste au-dessous du seuil que justifient les enjeux.
2. *Piège silencieux* ($p + b < p^\ast$ et $p_w \ge p^\ast$) : le décideur part en parfaite cohérence avec son calcul, mais un facteur omis porte le risque réel au-dessus du seuil, sans que rien dans le cadre ne l’en avertisse.
3. *Sauvé par la marge* ($p < p^\ast \le p + b$ et $p_w \ge p^\ast$) : l’estimation seule invitait à partir, mais la marge fait passer $p + b$ au-dessus de $p^\ast$, et le renoncement évite un danger que le cadre ne voyait pas.
4. *Prudence superflue* ($p + b \ge p^\ast$ alors que $p_w < p^\ast$, en particulier quand $z = 0$) : aucun péril caché ne menaçait le bateau, et la marge fait manquer le gain du voilier léger. Ce manque à gagner est le prix visible de la marge d’humilité.

Le troisième quadrant comprend aussi le cas où $p \ge p^\ast$ dès l’origine, comme pour M. X : on renonce alors sans avoir besoin de marge, et l’on parlera de *renoncement justifié*.

Le bloc formel suivant énonce ce modèle, que nous appellerons M2 (le deuxième des modèles formels du livre, présentés au @sec:ch00-architecture), avec ses hypothèses et le statut exact de $b$.

::: {.formel titre="Modèle M2 : décider avec un facteur omis"}
Reprenons le modèle de décision du @sec:ch04 (@sec:ch04-course-voile) : une option risquée à issue binaire, face à une option sûre d’utilité certaine $U_{\text{sûr}}$. Le succès procure le gain $\Delta U = U_{\text{succès}} - U_{\text{sûr}} > 0$, l’échec inflige la perte $L = U_{\text{sûr}} - U_{\text{échec}} > 0$, et la règle de Savage [@savage1954] conduit au seuil de l’@eq:ch04-seuil :

$$p^\ast = \frac{\Delta U}{\Delta U + L} = \frac{1}{1 + L/\Delta U}.$$

**Hypothèses.**

1. *Facteur omis indépendant.* Un mécanisme absent du cadre ajoute une probabilité d’échec $z \in \left[0, 1\right]$, indépendante des causes de défaillance représentées dans l’estimation $p \in \left[0, 1\right]$. Le risque réel vaut alors $p_w = 1 - (1 - p)(1 - z)$ (@eq:ch17-risque-reel).
2. *Inobservabilité de $z$ depuis le cadre.* Le décideur ne peut ni lire $z$, ni l’estimer, ni faire dépendre sa règle de $z$ : un facteur omis ne produit aucun désaccord dans l’ensemble des alternatives admises (@prop:desaccord), ni aucun signal dans un contrôle calculé à partir du seul cadre (@prop:cause-commune).
3. *Décision sur $p + b$.* Le décideur choisit l’option risquée si et seulement si $p + b < p^\ast$ (@eq:ch17-regle-marge), où $b \ge 0$ est sa marge d’humilité ; sinon, il retient l’option sûre.

**Partition du plan $\bigl((p + b)/p^\ast,\, p_w/p^\ast\bigr)$.** Rapportés au seuil, la grandeur sur laquelle on décide et le risque réel découpent l’espace des situations en quatre quadrants autour du point $(1, 1)$ :

- *départ justifié* : $(p + b)/p^\ast < 1$ et $p_w / p^\ast < 1$ ;
- *piège silencieux* : $(p + b)/p^\ast < 1$ et $p_w / p^\ast \ge 1$ ;
- *renoncement justifié* ou *sauvé par la marge* : $(p + b)/p^\ast \ge 1$ et $p_w / p^\ast \ge 1$, selon que $p \ge p^\ast$ dès l’origine ou que $p < p^\ast \le p + b$ ;
- *prudence superflue* : $(p + b)/p^\ast \ge 1$ et $p_w / p^\ast < 1$.

**Statut de $b$ et limites.** La marge $b$ n’est ni une mesure ni un estimateur de $z$. C’est un jugement de prudence, appuyé sur le rapport des enjeux $L/\Delta U$ et sur la lecture à l’envers de l’écart $p^\ast - p$ (@sec:ch03-raisonner-envers). L’indépendance entre $p$ et $z$ est en outre une hypothèse simplificatrice : si un défaut caché aggrave l’effet des contraintes déjà modélisées (une fissure qui réduit la tenue du mât face aux rafales prévues), le risque réel peut dépasser la valeur de l’@eq:ch17-risque-reel.
:::

L’exemple quantitatif qui suit reprend les situations du @tbl:ch04-seuil en y ajoutant un facteur omis et une marge d’humilité, de façon à faire apparaître chacune des quatre issues.

::: {.exemple-quantitatif titre="Décider sur ce que l’on croit quand le monde réserve un risque omis (illustratif)"}
**Mise en place.** Les valeurs sont illustratives : elles servent à faire voir le fonctionnement du modèle M2 et ses quatre issues, non à évaluer une régate ou une prise de risque réelles. On reprend la course à la voile et la roulette russe du @tbl:ch04-seuil, en leur ajoutant un facteur omis $z$, invisible pour le décideur, et une marge d’humilité $b$. Pour la course, le rapport des enjeux vaut 25, ce qui fixe le seuil à 3,85 % ; M. X estime le risque de casse à 5 %, M. Y à 0,1 %. Le @tbl:ch17-scenarios compare six situations :

- *M. Y* et *M. X*, sans défaut caché ni marge ($b = 0\,\%$, $z = 0\,\%$) ;
- *M. Y, fissure non repérée* : M. Y garde son estimation de 0,1 % sans marge ($b = 0\,\%$), mais une fissure qu’il ignore ajoute dans le monde un risque indépendant de 8 % ;
- *… avec une marge* : face au même défaut caché ($z = 8\,\%$), M. Y s’impose une marge d’humilité de 4 % ;
- *Prudence superflue* : M. Y applique la même marge de 4 %, mais le mât n’a aucune fissure ($z = 0\,\%$) ;
- *Roulette russe* : le rapport des enjeux atteint 10 000, ce qui abaisse le seuil à 0,0100 % ; persuadé que la chambre placée face au percuteur est vide, le joueur estime son risque à 0,001 % sans marge ($b = 0\,\%$), alors qu’une chambre sur six est chargée ($z = 16{,}7\,\%$).

![Les quatre issues du modèle M2, sur deux axes logarithmiques : en abscisse, la grandeur sur laquelle on décide rapportée au seuil, $(p + b)/p^\ast$ ; en ordonnée, le risque réel rapporté au seuil, $p_w/p^\ast$. Les droites où chacun de ces rapports vaut $1$ séparent les quatre quadrants : *départ justifié* en bas à gauche, *piège silencieux* en haut à gauche (points orange ; les autres situations sont en bleu), *renoncement justifié* en haut à droite et *prudence superflue* en bas à droite. La flèche horizontale montre comment une marge d’humilité de 4 % fait franchir le seuil à M. Y face à une fissure cachée de 8 %, et le fait passer du *piège silencieux* à l’issue *sauvé par la marge*, qui appartient au même quadrant que le *renoncement justifié*.](figures/ch17-decisions.pdf){#fig:ch17-decisions width=90%}

::: {.inclure fichier="tableaux/ch17-scenarios.md"}
:::

**Calcul.** Le @tbl:ch17-decisions donne, pour ces six situations, la grandeur $p + b$ comparée au seuil $p^\ast$, la décision, le risque réel $p_w$ et l’issue.

::: {.inclure fichier="tableaux/ch17-decisions.md"}
:::

Pour *M. Y* sans facteur omis, on décide sur 0,1 %, au-dessous du seuil de 3,85 % : *on part*, face à un risque réel de 0,100 % (*départ justifié*). Pour *M. X*, 5 % dépasse 3,85 % : *on renonce*, pour un risque réel de 5,00 % (*renoncement justifié*). Avec une fissure non repérée qui ajoute 8 %, M. Y décide toujours sur $p + b = 0{,}1\,\% < 3{,}85\,\%$ et prend le départ, alors que l’@eq:ch17-risque-reel porte le risque réel à $1 - (1 - 0{,}001)(1 - 0{,}08) \approx 8{,}09\,\%$, plus du double du seuil : c’est le *piège silencieux*.

Avec une marge de 4 %, la grandeur de décision devient $0{,}1\,\% + 4\,\% = 4{,}1\,\%$, au-dessus de 3,85 % : M. Y renonce et se trouve *sauvé par la marge*, alors que le risque réel reste de 8,09 %. Si le mât n’a en réalité aucune fissure (*Prudence superflue*), le même calcul conduit au même renoncement, pour un risque réel de 0,100 % : on paie alors le prix de la marge en cédant l’avantage du voilier léger. Dans la *Roulette russe*, enfin, le joueur compare 0,001 % au seuil de 0,0100 % et presse la détente, alors que la chambre chargée ($1/6 \approx 16{,}7\,\%$) porte le risque réel à 16,7 %, très haut dans le quadrant du *piège silencieux*.

**Lecture.** La @fig:ch17-decisions et les tableaux [-@tbl:ch17-scenarios] et [-@tbl:ch17-decisions] font voir quatre choses.

- *Dans ce modèle, la marge d’humilité est le seul levier du décideur contre ce que le cadre omet.* Tant que $z$ reste hors de vue, aucun raffinement des variables connues ne fait apparaître la fissure. Seule la marge déplace le point vers la droite de la @fig:ch17-decisions, jusqu’à lui faire franchir la droite $(p + b)/p^\ast = 1$.
- *Se protéger d’un danger omis n’exige pas de l’estimer.* Une marge de 4 % renverse la décision face à un défaut caché de 8 %, non parce que 4 % estimerait la moitié de 8 %, mais parce que l’écart entre 0,1 % et 3,85 % était plus petit que la marge.
- *La marge a un prix, d’autant plus faible, comparé à la perte évitée, que le rapport des enjeux est élevé.* Quand $z = 0\,\%$, la prudence superflue fait manquer le gain du voilier léger. Rapporté à une perte qui vaut 25 fois ce gain dans la course, ou 10 000 fois dans la roulette russe, ce prix d’assurance reste modeste.
- *Plus le rapport des enjeux est élevé, plus la marge qui suffit à renverser la décision est mince.* À la roulette russe, l’écart entre 0,001 % et le seuil de 0,0100 % est inférieur à un centième de point : la moindre marge aurait renversé la décision, alors que le risque réel atteint 16,7 %. Le joueur ne tombe dans le piège silencieux que parce qu’il n’en prend aucune ; aucune marge, en revanche, ne lui aurait appris que le barillet était chargé.

L’exemple suppose une issue binaire, une option sûre bien définie et l’indépendance de $p$ et de $z$. Il montre comment agit la marge, sans fournir de formule pour la fixer : sa valeur relève du jugement.
:::

Cet exemple ravive une tentation que le @sec:ch04 avait déjà écartée (@sec:ch04-question-ouverte) : puisque le modèle écrit le risque réel $p_w$, pourquoi ne pas décider directement sur lui, et ne partir que si $p_w < p^\ast$ ? L’encadré suivant explique pourquoi cette règle, d’apparence rigoureuse, est contradictoire.

::: {.nuance titre="Pourquoi le risque omis ne peut pas entrer dans la règle de décision"}
Il est tentant de loger le facteur omis $z$ dans la règle elle-même, en prescrivant de n’agir que si « le véritable risque total $p_w$ » est inférieur au seuil $p^\ast$. Sous sa précision apparente, l’inégalité $p_w < p^\ast$ confond ce que contient le monde et ce dont dispose le décideur.

Dans la théorie de l’utilité espérée subjective [@savage1954], la rationalité est relative à ce que croit le décideur au moment du choix : une règle opère sur les nombres que fournit la représentation, non sur des grandeurs inaccessibles. Or $z$ désigne, par définition, ce que le cadre n’a pas retenu : aucune décomposition de la variance sur l’ensemble des alternatives admises ne le fait apparaître (@prop:desaccord, @sec:ch05), et aucun contrôle interne ne peut le lire (@prop:cause-commune, @sec:ch07). Traiter $z$ comme un paramètre que l’on consulterait avant de décider ferait de l’incertitude ontologique du @sec:ch05 une troisième quantité mesurable, à côté des incertitudes aléatoire et épistémique. Si $z$ pouvait être estimé depuis le cadre, il ne serait plus omis : il figurerait déjà dans $p$ et dans l’ensemble des alternatives admises $\Theta$.

C’est pourquoi le modèle M2 sépare strictement $p_w$, qui gouverne l’issue, et $p + b$, qui gouverne la décision. La marge d’humilité tire sa raison d’être de l’asymétrie des enjeux et de l’étroitesse de l’écart $p^\ast - p$. Sa limite est tout aussi nette : elle ne mesure rien, elle expose à la prudence superflue quand $z = 0$, et elle ne remplace pas un contrôle indépendant lorsque les conséquences sont irréversibles.
:::

## Calibrer ce qui se répète, verrouiller ce qui ne se joue qu’une fois {#sec:ch17-calibrer-verrouiller}

La marge d’humilité donne une prise au jugement, mais elle laisse de côté une distinction posée au @sec:ch04 (@sec:ch04-decision-unique) : selon qu’une décision appartient à une longue série ou ne se prend qu’une fois, la réponse du monde ne joue pas le même rôle. Il en découle deux pratiques : *calibrer ce qui se répète ; verrouiller ce qui ne se joue qu’une fois*.

Lorsque des décisions comparables se répètent des centaines ou des milliers de fois face à une distribution assez stable (bulletins météorologiques quotidiens, tri de demandes médicales ou administratives, octroi de crédits courants, filtrage de messages), les issues successives forment une population d’épreuves. On peut alors s’appuyer sur une pratique statistique éprouvée, la calibration du @sec:ch03 (@sec:ch03-calibration-historique) : fixer des seuils d’action adaptés aux enjeux, ménager une zone d’abstention quand le score reste ambigu, consigner les prévisions et leurs conditions dans un historique avant que l’issue soit connue, puis comparer les fréquences observées aux probabilités annoncées à l’aide de règles de score strictement propres [@gneiting2007]. Si les prévisions se révèlent trop assurées ou les seuils trop lâches, l’écart apparaît dans l’historique et l’on corrige le dispositif pour les cas suivants. Une erreur isolée se fond dans la moyenne, pourvu qu’aucune perte ne soit ruineuse à elle seule.

La répétition sert aussi à juger ceux qui prévoient. Le @sec:ch03 (@sec:ch03-prevision-previsionniste) a montré qu’une issue isolée départage mal deux prévisions cohérentes, et presque pas du tout lorsqu’elle est l’issue attendue. La calibration est le seul moyen de juger un prévisionniste, et elle n’existe que là où les cas se répètent.

Même là où elle s’applique, la calibration a deux limites qu’il faut surveiller :

- *Elle suppose un environnement stable.* Une dérive de distribution (@sec:ch07-observations) peut rendre caducs, sans avertissement, des seuils patiemment ajustés sur le passé.
- *Elle suppose qu’aucun cas isolé n’emporte l’ensemble.* Dès qu’un seul échec, dans une série d’apparence répétitive, entraîne une ruine irréversible ou des pertes corrélées à grande échelle, comme avec les modèles de risque hypothécaire d’avant 2008 (@sec:ch05), la moyenne passée cesse de protéger.

Devant une décision unique (@sec:ch04-decision-unique), ces appuis disparaissent ensemble. Lancer un voilier léger dans une course au large, pratiquer une opération chirurgicale exceptionnelle, arrêter l’architecture d’un système critique, laisser un agent déclencher une opération irréversible sur des données de production (@sec:ch14) : aucune série de cas comparables ne compense un mauvais tirage, et le verdict du monde arrive après l’acte, quand la perte $L$ est déjà subie. Un taux de réussite élevé, mesuré sur des cas antérieurs ou sur des tests de référence, ne promet rien pour *cette* instance : elle peut tomber parmi les rares échecs, se situer au-delà de la frontière en dents de scie de l’outil (@sec:ch12-frontiere-dents-scie) ou dépendre d’un facteur $z$ absent des séries passées. Le @sec:ch09 (@sec:ch09-comportement-alertes) en a tiré la conséquence pour les alertes : quand l’enjeu est sans appel et que $p^\ast$ s’effondre, la réponse cohérente n’est pas de se fier à la moyenne, mais d’examiner chaque alerte ($u = 1$) et d’interposer un arrêt avant l’engagement.

::: {.definition #def:verrou titre="Verrou"}
Un **verrou** est un point où une action attend une autorisation, parce que la réponse du monde coûterait trop cher ou serait irréversible.
:::

Protéger une décision unique demande donc deux dispositions : une marge d’humilité du côté de l’estimation, et un verrou (@def:verrou) du côté de l’exécution, afin qu’un comparateur (@def:comparateur) capable de se tromper autrement (@prop:independance) examine l’acte avant qu’il n’atteigne le monde. Le contraste est net. Le citadin qui décide chaque matin d’emporter ou non son parapluie peut se fier à un bulletin dont l’historique atteste la calibration (@sec:ch03-calibration-historique) : une erreur lui coûte une averse et se compense sur l’année. Le lancement d’un satellite ou la migration irréversible d’une base de données critique n’offrent pas cette série : ils appellent une revue formelle, sous-système par sous-système, avant toute autorisation.

L’ingénierie de la sûreté pratique depuis longtemps ces autorisations préalables. Transposé aux systèmes automatisés, le verrou se lit à travers les cinq conditions de détection du @sec:ch06 : existence, différence, comparabilité, arrivée à temps et prise en compte (@sec:ch06-cinq-conditions). Par construction, il assure la quatrième, l’*arrivée à temps*, puisqu’il bloque l’action avant que le monde réponde. Il ne suffit pas pour autant. Si l’autorisation émane du même cadre ou du même modèle que l’action, la *différence* manque (@prop:cause-commune) ; si les hypothèses et la provenance ont été effacées en chemin, la *comparabilité* manque (@def:blanchiment) ; si l’opérateur approuve machinalement sous la pression des délais, la *prise en compte* manque (@def:prise-en-compte, @sec:ch16-etranglement-evaluation). Un verrou sans comparateur indépendant ni réelle autorité de refus ne produit qu’une signature.

## Bacs à sable et verrous {#sec:ch17-bacs-a-sable-verrous}

À insister sur les verrous, on pourrait conclure qu’il faut interdire d’avance toute initiative autonome. Deux acquis de l’ouvrage semblent ici se heurter :

- le @sec:ch07 (@sec:ch07-deux-voies) a montré qu’une pertinence nouvelle n’entre dans un cadre que du dehors : en étant averti par un autre point de vue, ou en *découvrant par l’épreuve*, c’est-à-dire en agissant sur le monde, ce que l’apprentissage par renforcement appelle l’exploration [@sutton2018]. Interdire toute exploration figerait nos représentations dans leurs lacunes ;
- le @sec:ch14 (@sec:ch14-autorite-garanties) a montré ce qu’il en coûte de confier l’autorité d’agir à la couche de la pile qui offre le moins de garanties, le modèle de langage, quand des agents exécutent des opérations réelles plus vite que quiconque ne peut réagir, comme lors de l’incident de Knight Capital [@sec2013knight].

La tension se résout dès que l’on tient ensemble deux idées. D’une part, *toute action est aussi une question posée au monde* : exécuter un programme, lancer une simulation ou modifier un état renvoie une réponse qui met la représentation à l’épreuve. D’autre part, ce qui sépare l’exploration utile de l’imprudence n’est pas le caractère actif ou passif du système, mais le *coût* et la *réversibilité* de la réponse. Le @sec:ch07 en avait tiré une règle de prudence : explorer là où la réponse du monde est peu coûteuse et réversible, recourir à des comparateurs extérieurs là où elle coûterait trop cher ou serait irréversible. Deux dispositifs lui donnent forme.

::: {.definition #def:bac-a-sable titre="Bac à sable"}
Un **bac à sable** est un environnement isolé où les actions n’ont aucun effet extérieur, et où l’on peut donc interroger le monde à peu de frais.
:::

Le monde qu’on y interroge est réel lorsqu’il est lui-même calculatoire (le compilateur, les tests, une base de données d’essai) ; ailleurs, le bac à sable n’interroge que ce qu’il reproduit.

Dans un bac à sable (@def:bac-a-sable), interroger le monde coûte peu et se défait : un opérateur ou un agent peut essayer, recevoir des démentis concrets et corriger sa représentation sans infliger de perte $L$ à l’extérieur. Un verrou (@def:verrou) marque au contraire la frontière au-delà de laquelle la réponse du monde coûterait trop cher ou serait irréversible. L’exploration s’arrête là, et un autre comparateur (le jugement d’une personne compétente, un contrôle formel, un jeu d’essais indépendant) doit tenir lieu de monde avant que l’acte franchisse la frontière.

Cette distinction explique où réussissent les agents de programmation, comme l’avait relevé le @sec:ch14 (@sec:ch14-autorite-garanties). Lorsqu’un agent modifie du code dans un dépôt isolé, l’outillage classique de l’informatique (compilateur, vérificateur de types, analyseur statique, batterie de tests écrite à l’avance : @sec:ch13-enonce-avance) lui oppose un monde déterministe qui répond en quelques secondes, presque gratuitement et de façon entièrement réversible. Si une piste échoue, le test rejette la modification, l’agent corrige au tour suivant, et rien n’a atteint la production. La boucle peut donc explorer vite, tant que des comparateurs mécaniques isolés lui renvoient à chaque étape un verdict fidèle. Dès qu’il s’agit de toucher une base de données vivante, d’écrire à un client, de modifier des droits d’accès ou d’engager un paiement, l’environnement ne répond plus à bas coût, et l’action doit passer un verrou.

Le génie logiciel et la sûreté des systèmes pratiquent depuis longtemps cette architecture à deux zones, sous la forme d’environnements cloisonnés et de séparation des privilèges. Cette architecture a deux limites :

- *Un bac à sable ne révèle que ce qu’il modélise.* Selon le second volet de la @prop:cause-commune (@sec:ch07-observations), si le simulateur ou les tests laissent constante une condition critique, comme les essais en air sec d’une ferrure destinée à la mer ou l’automate dont les capteurs ignorent la couleur des fils, aucune répétition dans le bac à sable ne fera apparaître le facteur qui manquera en exploitation. De plus, un agent qui peut réécrire les tests chargés de le contrôler, comme le décrivait la @sec:ch14-chaine-n-maillons, prive ce comparateur de son indépendance. Les tests de contrôle, les secrets d’accès et la mise en production doivent donc rester hors de sa portée, derrière un verrou.
- *Multiplier les verrous sur des actes bénins use la vigilance.* Si chaque opération locale et réversible appelle une demande d’autorisation, ces demandes sont presque toutes sans danger, et elles subissent le sort des alertes presque toujours fausses (@sec:ch09-comportement-alertes) : l’approbation devient un clic réflexe qui laisse passer la rare opération dangereuse. Un verrou ne garde sa force que s’il est posé avec parcimonie, aux véritables frontières de coût et d’irréversibilité.

## Recevoir un chiffre assuré : quatre questions {#sec:ch17-quatre-questions}

Les trois sections précédentes adoptaient le point de vue de celui qui construit un modèle, règle un outil ou conçoit une architecture. Mais parmi ceux à qui ce livre s’adresse (@sec:avant-propos-public), le décideur, le responsable d’institution et le destinataire non spécialiste reçoivent les chiffres et les recommandations sans les avoir produits. Ils supportent les conséquences d’un cadre qu’ils n’ont ni choisi ni construit, et qu’ils n’ont ni le temps ni la spécialité d’examiner de l’intérieur.

Lorsqu’un expert, une note ou un programme transmet un chiffre unique et assuré sans les conditions dans lesquelles il a été obtenu, le blanchiment des chapitres [-@sec:ch08] et [-@sec:ch14] (@def:blanchiment) change de nature pour celui qui le reçoit : il devient un *transfert de responsabilité déguisé en information* [@fauriat2026frame]. On demande au destinataire d’accepter comme un fait ce qui dépend de définitions, de données datées et d’omissions décidées en amont. Sans pouvoir refaire l’analyse, il a besoin d’un moyen simple de juger si le nombre peut porter une décision.

Ce moyen, proposé comme une pratique de travail [@fauriat2026frame] et non comme une méthode éprouvée par des études empiriques, tient en quatre questions directes, qui ne demandent aucun bagage mathématique :

1. *Sous quelles conditions ce chiffre tient-il ?* La question fait réapparaître l’arrière-plan tacite $\mathcal{T}$ et les limites de validité que le blanchiment a effacés : à quelle population, à quelle échelle de temps, avec quelles définitions et pour quel usage le résultat vaut-il ?
2. *Qu’est-ce qui le ferait changer sensiblement ?* C’est raisonner à l’envers (@sec:ch03-raisonner-envers) : sur quelles hypothèses fragiles repose le résultat, et une variation plausible le ferait-elle passer de l’autre côté du seuil $p^\ast$ qui compte pour la décision ?
3. *Quelle est la manière la plus vraisemblable dont il pourrait être faux ?* La question demande à celui qui avance le chiffre de nommer son angle mort le plus probable (@def:angle-mort), plutôt que de défendre la précision apparente d’une valeur ponctuelle.
4. *Qu’a-t-on délibérément choisi de ne pas modéliser ?* La question trace la frontière entre les variables $X$ retenues dans le cadre (@def:cadre) et les facteurs laissés dans l’arrière-plan : c’est là que l’incertitude ontologique (@sec:ch05-incertitude-ontologique) échappe aux barres d’erreur.

Poser ces questions n’exige aucune compétence de spécialiste ; leur efficacité dépend en revanche d’une attitude, des deux côtés. Celui qui reçoit le chiffre doit être prêt à demander ses conditions, et chacun doit accepter « nous ne savons pas » ou « nous n’avons pas modélisé ce facteur » comme des réponses informatives, non comme des aveux d’échec. Le @sec:ch12 (@sec:ch12-calibration-longue-traine) l’a montré pour les modèles de langage : une évaluation qui note l’abstention comme une erreur pousse à deviner [@kalai2025]. Une culture professionnelle qui sanctionne l’aveu d’ignorance tend à produire le même effet sur les personnes. Savoir ce qu’une estimation laisse dans l’ombre éclaire la décision ; le taire derrière une décimale la fausse.

Le bulletin de pluie du @sec:ch03 (@sec:ch03-calibration-historique) montre ce qui sépare un fait nu d’une information qui laisse au destinataire sa part de décision [@fauriat2026frame]. Comparons deux annonces : « il pleuvra demain » et « 70 % de chances de pluie demain ». La première paraît plus nette et plus commode ; en réalité, elle retire la décision à celui qui la reçoit. Le prévisionniste y a déjà appliqué, en silence, son propre seuil de prudence : c’est une *injonction déguisée en information*. La seconde respecte la séparation entre croyances et utilités qu’opère la règle de Savage (@sec:ch04-ues) : chacun peut décider selon *ses* enjeux $L/\Delta U$, prendre un parapluie pour un trajet ordinaire, reporter le coulage d’une dalle de béton ou une opération qu’une averse compromettrait gravement. Ces enjeux, aucun cadre du météorologue ne les contient.

Lorsque le chiffre ou la recommandation sort d’un système automatisé (score de crédit, priorité de tri, synthèse documentaire, réponse d’un assistant conversationnel), les quatre questions restent les mêmes, mais *leur destinataire change* [@fauriat2026frame]. Interroger le modèle lui-même sur ce qu’il ignore ne sert à rien : il produirait, du même ton assuré, des justifications plausibles ou complaisantes plutôt que la trace réelle de ses hypothèses (@sec:ch15-bainbridge-consigne). Souvent, il n’existe pas non plus d’expert unique qui aurait arrêté le cadre : celui-ci est réparti entre les données d’entraînement, l’orientation du modèle, les consignes et l’assemblage logiciel (@sec:ch11, @sec:ch14).

C’est donc à l’*institution* qui conçoit, déploie et engage le système que les quatre questions doivent être posées. Si elle ne peut dire en quelques phrases dans quelles conditions le résultat vaut, ce qui le ferait basculer et ce qui a été laissé hors du modèle, le chiffre n’est pas prêt à soutenir une décision irréversible. Le @sec:ch16 (@sec:ch16-etranglement-evaluation) a montré la fragilité de cette exigence : la capacité d’une institution à répondre honnêtement (conserver la provenance, entretenir des équipes capables de regarder sous l’interface, ne pas sacrifier la relecture au débit) est justement ce que la course au volume tend à vider. Préserver cette capacité demande d’organiser ensemble l’attitude des personnes, le placement des contrôles et les règles collectives : c’est l’objet du @sec:ch18.

::: {.question}
Pour votre prochain déploiement irréversible, quel est le rapport des enjeux $L/\Delta U$, quel seuil $p^\ast$ en découle, et votre estimation du risque, augmentée d’une marge d’humilité $b$ pour ce que votre représentation pourrait omettre, reste-t-elle au-dessous de ce seuil ?
:::

## Points clés {.points-cles}

- Le monde réserve des chances d’échec que la représentation ne montre pas : le risque réel $p_w = 1 - (1 - p)(1 - z)$ combine le risque estimé dans le cadre et un facteur omis $z$ qu’aucun contrôle interne ne sait lire.
- La marge d’humilité $b$ est un jugement, non une estimation de $z$ : elle peut protéger une décision unique du piège silencieux, au prix d’une prudence superflue quand aucun péril caché n’existe.
- On calibre ce qui se répète dans un environnement stable ; une décision unique et irréversible, qu’aucun taux passé ne protège, appelle, en plus d’une marge d’humilité, un verrou, où l’action attend l’accord d’un contrôle indépendant.
- Toute action étant aussi une question posée au monde, mieux vaut la poser là où la réponse est peu coûteuse et réversible : on explore librement dans un bac à sable, et l’on réserve les verrous aux frontières de coût et d’irréversibilité, sans confondre le bac à sable avec le monde.
- Devant tout chiffre assuré, quatre questions font réapparaître ses conditions et ses omissions ; elles supposent d’accepter « nous ne savons pas » comme une réponse, et s’adressent à l’institution responsable quand le chiffre sort d’un système automatisé.
