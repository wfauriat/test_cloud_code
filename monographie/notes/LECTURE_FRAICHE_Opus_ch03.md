# Lecture fraîche — Chapitre 3 « Mondes possibles : la probabilité comme jugement »

Lecteur : Opus (première lecture, seul le fichier `chapitres/03-mondes-possibles.md` a été lu).

## 1. Résumé de ce que j'ai compris (test de lisibilité)

1. Une probabilité n'est pas une propriété de l'objet : elle répartit un poids total de 1 entre les « mondes possibles », c'est-à-dire les situations compatibles avec ce que l'on sait, dont les états cachés de l'arrière-plan $(\dots)$.
2. Il en découle une attitude, « raisonner à l'envers » : chercher quelle variation plausible de l'arrière-plan renverserait la conclusion, sans tomber dans les scénarios extravagants.
3. Cette lecture « subjective » n'est pas arbitraire : elle est tenue par la cohérence (règles du calcul, règle de Bayes) et par la confrontation aux faits.
4. Une issue isolée juge mal une prévision, surtout quand l'issue attendue se produit (exemple de M. X à 5 % et M. Y à 0,1 % : rapport 50 si casse, 0,951 sinon ; la dinde).
5. Seule une série permet de juger un prévisionniste : il faut un historique écrit, une règle de score strictement propre (le score logarithmique en est une) et un examen de la calibration, qui exige la répétition et fait donc défaut pour l'unique.

## 2. Constats classés par gravité

### Gravité A (compréhension compromise ou contresens possible)

**A1 — Points clés, 2e puce**
Passage : « chercher quelle variation plausible, ou impossible à écarter, de cet arrière-plan renverserait la conclusion »
Gêne : le corps du texte (§ Raisonner à l'envers) dit « que les éléments disponibles ne permettent pas *raisonnablement* d'écarter » et rejette expressément la météorite « au motif que rien n'est logiquement impossible » ; « impossible à écarter », sans « raisonnablement », peut se lire comme « non exclu logiquement », c'est-à-dire exactement ce que le garde-fou interdit.
Reformulation minimale : « quelle variation plausible, ou que l'on ne peut raisonnablement écarter, de cet arrière-plan… ». Le sens ne bouge pas si l'on retient la lecture du corps du texte, ce qui semble l'intention.

**A2 — Encadré « Ce qu'une seule course dit de deux prévisions », Lecture**
Passage : « Une issue à laquelle on donnait 0,1 % se produit en moyenne une fois sur mille lorsque l'estimation est juste »
Gêne : tout le chapitre refuse l'idée d'une « vraie » valeur (§ Mondes possibles) et dit qu'aucune règle ne permet de déclarer l'une des estimations « juste » (§ Prévision et prévisionniste) ; « lorsque l'estimation est juste » réintroduit justement cette idée et peut faire croire à une contradiction avec la thèse.
Deux lectures plausibles, que je ne tranche pas : (a) « lorsque l'estimation est bien calibrée », c'est-à-dire sur l'ensemble des cas où l'on annonce 0,1 % ; (b) « si 0,1 % était la vraie fréquence de ce type d'avarie ». Selon la lecture retenue, une reformulation possible est : « …se produit en moyenne une fois sur mille chez un prévisionniste bien calibré » (lecture a). Le sens change si c'est (b) qui est visée.

### Gravité B (gêne réelle)

**B1 — § Mondes possibles, 2e paragraphe**
Passage : « Une assertion probabiliste n'écarte rien de plus que ce que l'on sait déjà »
Gêne : on n'« écarte » pas ce que l'on sait ; il faut comprendre « n'écarte pas d'autres situations que celles déjà exclues par ce que l'on sait », et la phrase demande une relecture.
Reformulation : « Une assertion probabiliste n'écarte aucune situation de plus que celles que l'on sait déjà exclues ; elle répartit… ».

**B2 — § Mondes possibles, 2e paragraphe**
Passage : « et il ne fera pas « une course à 5 % » »
Gêne : la formule entre guillemets n'a de sens que si l'on se souvient du chapitre 2 ; sans cela, le lecteur ne sait pas ce qu'est une « course à 5 % » (une course à demi cassée ? une course où le mât casse un peu ?).
Reformulation : « et il ne fera pas une course qui serait « cassée à 5 % » : le mât tiendra jusqu'à l'arrivée, ou il cassera. » (possible dépendance au ch. 2 ; le sens ne bouge pas).

**B3 — § Mondes possibles, 4e paragraphe (« Cette lecture s'accorde… »)**
Passage : « Les variables $X$ du cadre découpent les mondes possibles en cases, une par valeur $x$ ; dans chaque case, $\Pr(Y \mid X = x)$ pèse des mondes… »
Gêne : le paragraphe empile la notation $A \cap (\dots) \rightarrow B$, $\Pr(B \mid A)$, puis $X$, $Y$, $x$ sans rappeler ce que désignent $X$ et $Y$ (possibles dépendances aux ch. 1 et 2) ; pour un lecteur cultivé qui arrive par un parcours, c'est le passage le plus opaque du chapitre.
Reformulation minimale : couper le paragraphe avant « L'@eq:ch02-cond-cadre prolonge… » et ajouter un rappel en incise : « Les variables $X$ retenues dans le cadre (ce que l'on observe) découpent… ; dans chaque case, $\Pr(Y \mid X = x)$, la probabilité de l'issue $Y$, pèse… ». À vérifier par l'auteur que « ce que l'on observe » / « l'issue » correspondent bien aux définitions du ch. 2.

**B4 — § Raisonner à l'envers, 3e paragraphe**
Passage : « ne consiste pas à chauffer une quatrième fois de l'eau pure au niveau de la mer »
Gêne : « une quatrième fois » suppose trois essais dans le tableau du ch. 2 ; sans le tableau sous les yeux, le lecteur ne comprend pas pourquoi « quatrième ».
Reformulation : « ne consiste pas à chauffer une fois de plus de l'eau pure… » (le sens ne bouge pas).

**B5 — § Raisonner à l'envers, 5e paragraphe**
Passage : « Donner ce rôle au jugement appelle une objection classique »
Gêne : « ce rôle » renvoie-t-il au paragraphe précédent (juger quelles variations sont plausibles) ou à la thèse de la section 1 (la probabilité comme poids accordé par une personne) ? La suite (« Si une probabilité exprime le poids qu'une personne accorde… ») suggère la seconde lecture, mais l'enchaînement immédiat suggère la première.
Reformulation, sans trancher : « Faire ainsi reposer la probabilité sur un jugement appelle une objection classique » (cette formulation couvre les deux lectures).

**B6 — § Raisonner à l'envers, dernier paragraphe**
Passage : « la lecture comme jugement rend visible ce qu'un chiffre présenté comme objectif, et qui n'appartiendrait à personne, laisserait dans l'ombre »
Gêne : « la lecture comme jugement » est une ellipse peu idiomatique, et l'objet de « rend visible » (les hypothèses, l'information, le cadre ?) reste implicite.
Reformulation : « lire la probabilité comme un jugement rend visibles les hypothèses et l'information qu'un chiffre présenté comme objectif, et qui n'appartiendrait à personne, laisserait dans l'ombre ». À vérifier : l'auteur pense peut-être aussi aux mondes jugés plausibles.

**B7 — § Prévision et prévisionniste, 3e paragraphe**
Passage : « Avant le départ, lequel des deux a raison ? Ni l'un ni l'autre »
Gêne : « ni l'un ni l'autre » se lit spontanément comme « tous deux ont tort », alors que la suite dit que la question n'a pas de réponse (« aucune règle […] ne permet de déclarer l'un juste et l'autre faux »).
Reformulation : « Avant le départ, lequel des deux a raison ? La question n'a pas de réponse, et ce n'est pas faute de rigueur : … ».

**B8 — Encadré, Lecture, fin**
Passage : « L'exemple ne dit pas, enfin, quel bateau il fallait choisir »
Gêne : les deux navigateurs évaluent *le même* voilier ; aucun choix entre bateaux n'a été posé dans le chapitre, et la phrase surgit sans antécédent (possible dépendance à la course du ch. 0 ou du ch. 2).
Deux lectures : (a) le choix entre le voilier léger et un autre bateau, posé dans un chapitre antérieur ; (b) le choix de prendre ou non le départ avec ce voilier. Reformulation selon (a) : « quel bateau il fallait choisir pour la course (voilier léger ou autre) » ; selon (b) : « s'il fallait prendre le départ avec ce voilier ».

**B9 — § Prévision et prévisionniste, paragraphe après l'encadré**
Passage : « Elle explique une faiblesse constante du raisonnement ordinaire : une issue sans histoire n'apporte presque aucune information. »
Gêne : ce qui suit les deux-points est un fait, non une faiblesse ; la faiblesse (tenir une suite d'issues sans histoire pour une preuve de sûreté) n'est pas dite.
Reformulation : « Elle explique une faiblesse constante du raisonnement ordinaire, qui tient pour une preuve de sûreté une issue sans histoire, alors qu'une telle issue n'apporte presque aucune information. »

**B10 — § Prévision et prévisionniste, paragraphe de la dinde**
Passage : « Le @sec:ch05 tirera les conséquences de cette seconde limite. Retenons ici la première »
Gêne : les deux « limites » n'ont pas été annoncées ni étiquetées ; le lecteur doit reconstruire que la première est la lenteur de l'accumulation (ou le faible pouvoir de départage d'un matin) et la seconde l'absence du danger dans le cadre.
Reformulation : « Le @sec:ch05 tirera les conséquences de cette seconde limite, un danger absent du cadre. Retenons ici la première, la lenteur avec laquelle les cas s'accumulent : … ».

**B11 — § Calibration et historique, 4e paragraphe**
Passage : « Pour évaluer des prévisions probabilistes dans la durée, il faut donc une manière de les noter qui n'incite le prévisionniste ni à ramener ses chiffres vers la moyenne… »
Gêne : « donc » suit un paragraphe sur l'insuffisance de la calibration (ne pas distinguer pluie et sec), mais la conclusion porte d'abord sur l'honnêteté des chiffres ; le lien avec la discrimination n'arrive que plus loin (« en outre »). Le connecteur annonce une conséquence qui n'est pas celle qu'on attend.
Reformulation : « Pour évaluer des prévisions probabilistes dans la durée, il faut une manière de les noter qui récompense cette capacité à distinguer les jours, sans inciter le prévisionniste ni à ramener… ». À vérifier par l'auteur que l'ordre des deux exigences lui convient ; le contenu ne change pas.

### Gravité C (confort, style)

**C1 — Introduction** : « Elle répartit un poids sur des mondes possibles ; elle invite donc à chercher ce qui renverserait une conclusion » : le « donc » saute une étape qui n'est expliquée qu'en section 2, et « mondes possibles » est employé ici avant sa définition en gras (section 1). Reformulation : « Elle répartit un poids sur des mondes possibles, ce qui invite à chercher… ».

**C2 — § Mondes possibles, 1er paragraphe** : « Le nombre serait alors une propriété… Il existerait alors… » : double « alors ». Reformulation : « Il existerait ainsi, avant l'événement… ».

**C3 — § Mondes possibles, 2e paragraphe** : « le 5 % du navigateur » : « le navigateur », avec l'article défini, renvoie à un personnage du ch. 2 (possible dépendance) ; le lecteur se raccroche au « marin » du paragraphe précédent, ce qui suffit.

**C4 — § Mondes possibles, dernier paragraphe, et § Prévision et prévisionniste, 2e et 3e paragraphes** : la scène des deux navigateurs qui « inspectent le même voilier léger et lisent le même bulletin » est racontée deux fois, la seconde avec des noms (M. X, M. Y). Le lecteur peut se demander s'il s'agit des mêmes personnes. Reformulation minimale : au début de la section 3, « Reprenons les deux navigateurs, que nous appellerons M. X et M. Y : … ».

**C5 — § Raisonner à l'envers, 3e paragraphe** : « au point de changer le parti retenu : une sollicitation d'un autre type » : « parti » (au sens de choix de conception) et « sollicitation » (au sens mécanique) sont des termes d'ingénieur. Reformulation : « au point de changer la solution retenue : une charge d'un autre type ».

**C6 — § Raisonner à l'envers, 4e paragraphe** : « noie l'attention et paralyse l'action autant que l'aveuglement » : deux lectures (l'aveuglement paralyse aussi l'action, ou la liste est aussi nuisible que l'aveuglement). Reformulation neutre : « …noie l'attention et paralyse l'action : elle nuit autant que l'aveuglement. » (cette formulation retient la seconde lecture, qui paraît la plus probable, à confirmer).

**C7 — § Prévision et prévisionniste, 2e et 3e paragraphes** : « le bateau casse », « brise le mât », « Si le mât casse », « le voilier casse » : le sujet de « casser » alterne entre le mât et le bateau, alors que l'événement a été défini largement (démâtage ou avarie forçant l'abandon). Reformulation : « Si le bateau casse » au 4e paragraphe, pour rester sur l'événement défini.

**C8 — Encadré, Mise en place** : « le rapport de vraisemblance de l'issue observée sous la prévision de M. X contre celle de M. Y » : « sous la prévision » est un calque possible de *under* ; usuel chez les statisticiens, moins naturel pour le lecteur cultivé. Reformulation : « selon la prévision de M. X, rapportée à celle de M. Y ».

**C9 — Encadré, « Si le bateau casse »** : « l'écart des deux surprises est le logarithme du rapport de vraisemblance, qui vaut $0{,}05 / 0{,}001 = 50$ » : « qui » peut se rattacher au logarithme ou au rapport ; le calcul tranche, mais un lecteur pressé peut hésiter. Reformulation : « …est le logarithme du rapport de vraisemblance ; ce rapport vaut $0{,}05 / 0{,}001 = 50$ en faveur de M. X (et $\ln 50 \approx 3{,}91 = 6{,}91 - 3{,}00$) ». L'ajout entre parenthèses est facultatif.

**C10 — Encadré, « Si le bateau tient »** : « il ne multiplie que par 0,951 la cote » : multiplier par un nombre inférieur à 1 revient à diminuer légèrement la cote de M. X, donc à favoriser à peine M. Y ; le lecteur doit le déduire. Reformulation : « il ne fait baisser que d'environ 5 % la cote… ».

**C11 — § Prévision et prévisionniste, après l'encadré** : « dépasse de loin les régates » : l'exemple porte sur une course au large, que l'on n'appelle pas d'ordinaire une régate. Reformulation : « dépasse de loin la course au large ».

**C12 — § Prévision et prévisionniste, paragraphe de la dinde** : le paragraphe est long et mêle le calcul, la condition sur le cadre, Noël et l'annonce du ch. 5 ; « la dinde inductiviste » est une possible dépendance au ch. 0. On pourrait couper avant « Une longue série de matins tranquilles… ».

**C13 — § Calibration et historique, 4e paragraphe et encadré formel** : la même notion est nommée « pénalité moyenne attendue », « pénalité qu'il s'attend à subir » et « pénalité espérée ». Harmoniser sur « pénalité espérée », en la glosant une fois par « moyenne attendue ».

**C14 — § Calibration et historique, 4e paragraphe** : « gonfler un 75 % en 95 % » : construction peu idiomatique. Reformulation : « porter un 75 % à 95 % ».

**C15 — § Calibration et historique, 5e paragraphe** : « si le projet réussit » : « le projet » surgit sans antécédent après l'exemple du voilier. Reformulation : « si un projet réussit ».

**C16 — § Calibration et historique, 6e paragraphe** : « ce que l'on peut calibrer de ce qu'il faut protéger autrement » : « protéger » reste vague (protéger quoi, contre quoi ?). Reformulation : « ce dont il faut se prémunir par d'autres moyens ». À vérifier par l'auteur, car le sens peut bouger selon ce que le ch. 17 entend par « protéger ».

## 3. Appréciation globale

Le chapitre se lit bien : la ligne d'argument (le poids sur des mondes, raisonner à l'envers, le subjectif n'est pas l'arbitraire, une issue juge mal, la série juge mieux) est nette et les transitions entre sections sont pour la plupart annoncées. Les sections les plus accessibles sont « Raisonner à l'envers », hors l'enchaînement vers l'objection, et « Calibration et historique », dont l'exemple du météorologue à 30 % est très parlant. Le passage le moins accessible est le 4e paragraphe de « Mondes possibles », chargé de notations héritées des ch. 1 et 2. Viennent ensuite le paragraphe de la dinde, dense et dont les deux « limites » ne sont pas nommées, et la fin de la lecture de l'encadré, où surgit un choix de bateau sans antécédent. Les deux points A sont des écarts de formulation qui risquent de faire croire que le texte contredit sa propre thèse (une « estimation juste », une variation « impossible à écarter »). Ils se corrigent en quelques mots.
