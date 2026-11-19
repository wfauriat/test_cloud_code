# Lecture fraîche du chapitre 3 (« Mondes possibles : la probabilité comme jugement »)

Lecteur : Sonnet, première lecture, texte seul. Aucun fichier modifié hors ce rapport.

## 1. Ce que j'ai compris (test de lisibilité)

1. Une probabilité n'est pas une propriété cachée de l'objet : c'est un poids réparti sur des « mondes possibles », donc un jugement relatif à une information et à un cadre. Deux personnes cohérentes peuvent donc diverger.
2. « Raisonner à l'envers » consiste à chercher quelle variation plausible de l'arrière-plan (…) renverserait la conclusion, avec un garde-fou contre les scénarios extravagants. « Subjectif » ne veut pas dire arbitraire : cohérence et confrontation aux faits.
3. Exemple des navigateurs M. X (5 %) et M. Y (0,1 %) : une seule course juge mal les prévisions. Si le bateau tient, le rapport de vraisemblance (0,951) ne départage presque rien ; s'il casse, le rapport de 50 favorise M. X sans le consacrer. La dinde illustre le même piège.
4. Seule la répétition permet de juger : calibration (accord probabilités annoncées / fréquences), insuffisante seule (météo à 30 % constant), complétée par les règles de score strictement propres (preuve avec le score logarithmique) et par un historique écrit avant l'issue.
5. Limite : on ne calibre pas ce qui n'arrive qu'une fois ; le choix en pareil cas relève du chapitre 4 et du chapitre 17. Je n'ai pas compris à quoi renvoie exactement « protéger autrement » (voir B17).

## 2. Constats classés par gravité

Légende : section = section du chapitre ; reformulation = proposition minimale.

### Gravité A (compréhension compromise ou contresens possible)

**A1. Sec. 3, encadré « Ce qu'une seule course dit… », Lecture.**
Passage : « Une issue à laquelle on donnait 0,1 % se produit en moyenne une fois sur mille lorsque l'estimation est juste ».
Gêne : « juste » réintroduit l'idée d'une valeur vraie, que tout le début du chapitre (et la phrase « aucune règle… ne permet de déclarer l'un juste et l'autre faux ») vient d'écarter. Deux lectures plausibles : (a) « juste » = bien calibrée, au sens de la fréquence à long terme ; (b) « juste » = égale à une chance objective. Je ne tranche pas.
Reformulation minimale : si (a), « lorsque l'estimation est bien calibrée » ; si (b), l'auteur doit juger si cette phrase contredit sa thèse.

**A2. Sec. 3, même encadré, Lecture, dernière partie.**
Passage : « L'exemple ne dit pas, enfin, quel bateau il fallait choisir : la réponse dépend aussi de ce que coûte une casse et de ce que rapporte une victoire. »
Gêne : l'exemple ne comporte ni plusieurs bateaux à choisir, ni victoire, ni enjeu chiffré. On ne comprend pas de quelle décision il est question ; la phrase ne se comprend que si l'on devine le renvoi au chapitre 4.
Reformulation minimale : « L'exemple ne dit pas, enfin, s'il fallait prendre le départ : la réponse dépend aussi de ce que coûte une casse et de ce que rapporte l'arrivée. » (Le sens risque de bouger si l'auteur pense à un autre choix, par exemple le choix de la prévision à suivre.)

### Gravité B (gêne réelle)

**B1. Introduction.**
Passage : « Le lecteur qui arrive ici par l'un des parcours de la @sec:ch00-parcours pourra s'y reporter au besoin. »
Gêne : « s'y » est flou (la section des parcours ? les chapitres 1 et 2 ? les définitions citées juste avant ?).
Reformulation : « pourra, au besoin, se reporter à ces deux chapitres. » Deux lectures possibles : ces deux chapitres, ou les définitions citées. Je ne tranche pas.

**B2. Sec. 1 et introduction : « mondes possibles » avant sa définition, et deux échelles de « monde ».**
Passage : « elle répartit un poids sur des mondes possibles » (introduction), puis la définition « les situations compatibles avec ce que l'on sait », puis « Chacun de ces états définit un monde possible où $A$ est vrai ».
Gêne : le terme sert dès le titre et l'introduction. Plus loin, un « monde » est tantôt une situation globale (mât cassé ou non), tantôt un état fin de l'arrière-plan. Le Pr(B | A) du paragraphe suivant pondère aussi ces mondes. Le lecteur ne sait pas quelle granularité retenir. En outre, Russell et Norvig partent de situations « concevables », alors que la définition parle de situations « compatibles avec ce que l'on sait ».
Reformulation : ajouter dans le premier paragraphe de la sec. 1 « (ce que l'on appellera plus bas des mondes possibles) » et, dans la définition, « une situation, décrite aussi finement qu'on le souhaite ». Le sens ne bouge pas.

**B3. Sec. 1, paragraphe commençant « Cette lecture s'accorde avec l'écriture des règles pratiques… ».**
Passage : « dans chaque case, $\Pr(Y \mid X = x)$ pèse des mondes qui partagent les mêmes valeurs $x$, mais qui diffèrent par tout ce que le cadre laisse dans $(\dots)$ ».
Gêne : paragraphe très dense (six renvois d'équations et de sections, notations $A$, $B$, $X$, $Y$, $\cap$, $\rightarrow$ supposées connues). « pèse des mondes » est étrange (on pèse un événement, on répartit un poids). Les variables $X$ et $Y$ ne sont pas rappelées (possible dépendance du chapitre 2).
Reformulation : couper en deux à « L'@eq:ch02-cond-cadre prolonge la même image » ; « Pr(Y | X = x) répartit le poids entre des mondes qui partagent… ». Rappeler en quelques mots ce que sont $X$ et $Y$.

**B4. Sec. 1.**
Passage : « et il ne fera pas « une course à 5 % » ».
Gêne : tournure elliptique. Il faut deviner que le mât n'aura pas « à moitié » cassé 5 % du temps, c'est-à-dire que l'issue est binaire.
Reformulation : « et la course ne se déroulera pas « à 5 % » : le mât tiendra jusqu'à l'arrivée, ou il cassera. » Le sens ne bouge pas.

**B5. Sec. 2.**
Passage : « raisonner à l'envers ne consiste pas à chauffer une quatrième fois de l'eau pure au niveau de la mer ».
Gêne : « quatrième » suppose que le lecteur se souvienne que le tableau du chapitre 2 contenait trois chauffes (possible dépendance). Le tableau n'est qu'un renvoi.
Reformulation : « à chauffer une fois de plus de l'eau pure au niveau de la mer ».

**B6. Sec. 2, passage de la sous-partie « garde-fou » à l'objection.**
Passage : « Donner ce rôle au jugement appelle une objection classique ».
Gêne : « ce rôle » n'a pas de référent clair. Le paragraphe précédent parle du garde-fou et de l'examen des variations, pas d'un « rôle » du jugement. Le saut vers la discussion « subjectif/arbitraire » n'est pas annoncé.
Reformulation : « Lire ainsi la probabilité comme un jugement appelle une objection classique ». Le sens ne bouge pas.

**B7. Sec. 2 : tension apparente entre le garde-fou et la règle de prudence.**
Passage : « ne donner une probabilité nulle qu'à ce qui est logiquement exclu » (cohérence), face à « Raisonner à l'envers ne consiste pas à inventer des scénarios extravagants… au motif que rien n'est logiquement impossible » (garde-fou).
Gêne : un lecteur peut conclure que la météorite doit à la fois être écartée et ne pas recevoir de probabilité nulle. Deux lectures : (a) poids infime mais non nul, sans examen ; (b) on ne l'examine pas, donc on lui donne zéro. Je ne tranche pas.
Reformulation : si (a), ajouter à la règle de prudence « , même si l'on décide de ne pas examiner ces mondes ».

**B8. Sec. 3.**
Passage : « Avant le départ, lequel des deux a raison ? Ni l'un ni l'autre, et ce n'est pas faute de rigueur ».
Gêne : en français, « ni l'un ni l'autre » signifie d'abord que les deux ont tort. Le sens voulu est que la question n'a pas de réponse (ni l'un ni l'autre ne peut être déclaré avoir raison).
Reformulation : « Aucun des deux ne peut être déclaré avoir raison, et ce n'est pas faute de rigueur ».

**B9. Sec. 3, exemple chiffré, puces.**
Passage : « il ne multiplie que par 0,951 la cote que l'on accordait à la prévision de M. X contre celle de M. Y ».
Gêne : une « cote » s'applique à une hypothèse vraie ou fausse ; ici on cote deux prévisions comme si c'étaient deux hypothèses rivales. Un lecteur cultivé non spécialiste ne voit pas ce que signifie « la cote d'une prévision contre une autre » (dépendance du chapitre 1).
Reformulation : « il ne multiplie que par 0,951 la cote de « M. X a la bonne prévision » contre « M. Y a la bonne prévision » ». Le sens risque de bouger : « bonne » renvoie à la même ambiguïté que A1.

**B10. Sec. 3, encadré, Lecture.**
Passage : « L'exemple montre d'abord que les deux issues n'ont pas le même poids. »
Gêne : « poids » désigne dans tout le chapitre la probabilité répartie sur les mondes ; ici il s'agit du pouvoir de discrimination d'une issue. Le paragraphe lui-même est un bloc de huit phrases avec trois « enseignements » enchaînés (« d'abord », « ensuite », « enfin »), peu aérés.
Reformulation : « n'ont pas la même force probante » (le sens est préservé ; reste à vérifier que c'est bien l'intention). Couper le paragraphe en trois, un par enseignement.

**B11. Sec. 3, après l'encadré.**
Passage : « Elle explique une faiblesse constante du raisonnement ordinaire : une issue sans histoire n'apporte presque aucune information. »
Gêne : ce qui suit les deux-points est un fait, non une faiblesse. La faiblesse est de prendre l'absence d'incident pour une confirmation. « presque aucune information » est de plus général : l'information est nulle uniquement pour départager les deux hypothèses du cas considéré.
Reformulation : « Elle éclaire une faiblesse constante du raisonnement ordinaire, qui prend une issue sans histoire pour une confirmation alors qu'elle n'apporte presque aucune information sur le point en litige. »

**B12. Sec. 3, paragraphe de la dinde.**
Passage : « C'est sur cette pente que glisse la dinde inductiviste, déjà rencontrée au @sec:ch00, et que le @sec:ch05 étudiera en détail. »
Gêne : « que » est ambigu (la dinde ? la pente ?). « inductiviste » est du jargon renvoyé aux chapitres antérieurs, et l'histoire n'est pas résumée avant « Chaque matin, le fermier lui apporte le grain » (lecteur qui n'a pas lu le ch. 0).
Reformulation : « …la dinde inductiviste du @sec:ch00 (le @sec:ch05 en reprendra l'étude). » Résumer l'histoire en une demi-phrase si l'on veut un chapitre lisible seul.

**B13. Sec. 3, fin de la dinde.**
Passage : « Le @sec:ch05 tirera les conséquences de cette seconde limite. Retenons ici la première ».
Gêne : aucune « première » ni « seconde limite » n'a été annoncée. On reconstitue que la première est la lenteur de l'accumulation et la seconde le danger hors du cadre, mais le texte ne les numérote pas avant.
Reformulation : annoncer en amont, dans « Mais elle pèse lentement, et à une condition », « deux limites : la lenteur…, puis la condition… », ou écrire « cette autre limite » et « la première, la lenteur ». Le sens ne bouge pas.

**B14. Sec. 4, début du paragraphe sur les règles de score.**
Passage : « Pour évaluer des prévisions probabilistes dans la durée, il faut donc une manière de les noter… »
Gêne : « donc » est trompeur. Le paragraphe précédent montre que la calibration ne suffit pas à rendre un prévisionniste utile (absence de discrimination). Or le critère qui suit (ne pas inciter à tricher) est autre : il garantit l'honnêteté, et seulement ensuite et indirectement la discrimination. Le lecteur attend une réponse au problème « calibré mais inutile ».
Reformulation : « Pour évaluer ces prévisions dans la durée, il faut aussi une manière de les noter… ». Deux lectures possibles de l'intention : (a) le score répond au problème de l'inutilité ; (b) c'est un autre point. Je ne tranche pas.

**B15. Sec. 4.**
Passage : « une telle règle avantage en outre, en moyenne et parmi des prévisionnistes également calibrés, celui qui annonce des probabilités élevées les jours où il pleuvra et faibles les autres. »
Gêne : phrase très condensée et sans démonstration, alors que c'est elle qui relie le score au problème de la discrimination. « pleuvra » (futur) mêle jour de la prévision et jour constaté.
Reformulation : « …avantage en outre, en moyenne, celui qui, à calibration égale, annonce des probabilités élevées les jours de pluie et faibles les jours secs. » (À vérifier : « les jours de pluie » est ex post.)

**B16. Sec. 4, paragraphe de l'historique.**
Passage : « distinguer deux situations qui produisent les mêmes écarts ».
Gêne : « écarts » n'est pas défini (écarts entre prévisions et fréquences ? entre prévisions et issues ?).
Reformulation : « …deux situations qui produisent le même écart entre prévisions et fréquences ».

**B17. Sec. 4, dernier paragraphe.**
Passage : « ce que l'on peut calibrer de ce qu'il faut protéger autrement ».
Gêne : « protéger » est elliptique : protéger quoi, contre quoi ? On devine : se prémunir contre ce qu'on ne peut pas évaluer par la répétition. Je n'ai pas pu reconstituer l'idée avec certitude.
Reformulation : « ce que l'on peut calibrer de ce dont il faut se prémunir par d'autres moyens ». Le sens risque de bouger selon l'idée de l'auteur (protection du système ? de la décision ?).

### Gravité C (confort, style)

**C1. Sec. 1, premier paragraphe.** « Le nombre serait alors une propriété… Il existerait alors, avant l'événement… » : « alors » répété deux fois en deux phrases. Supprimer le second (« Il existerait ainsi… »).

**C2. Sec. 1 et sec. 3 : même exemple répété.** Les deux navigateurs inspectant « le même voilier léger » et lisant « le même bulletin » apparaissent deux fois, avec des causes légèrement différentes (« fatigue cachée du gréement, ou une mer croisée imprévue » puis « défaut caché ou coup de vent imprévu »). Si la répétition est voulue (rappel), unifier les termes ; sinon alléger la sec. 1 par un renvoi à la sec. 3. Ne touche pas à l'argument.

**C3. Sec. 2.** « au point de changer le parti retenu » : « parti » est vieilli pour « décision ». Proposer « la décision retenue » (même sens).

**C4. Sec. 2.** « justifier la troisième décimale » : 0,1 % a une seule décimale écrite ; la troisième décimale n'existe qu'en 0,001. Proposer « justifier le chiffre après la virgule » ou « justifier la précision du chiffre ».

**C5. Sec. 2.** « Lorsque deux personnes aboutissent à des chiffres différents, l'écart n'est donc pas un caprice. » : « donc » un peu fort, car la cohérence autorise des poids très différents. Proposer « l'écart n'est pas nécessairement un caprice » (deux lectures : (a) « n'est pas » absolu ; (b) « peut ne pas être ». Je ne tranche pas).

**C6. Sec. 2 / Points clés.** Le texte dit « les variations… plausibles… ou que les éléments disponibles ne permettent pas raisonnablement d'écarter », les Points clés disent « plausible, ou impossible à écarter ». « impossible » est plus fort que « pas raisonnablement ». Harmoniser (« difficile à écarter »).

**C7. Sec. 3.** « Le jugement rétrospectif est prompt. » : « prompt » (calque de l'anglais « prompt » ?) est inusité pour « hâtif ». Proposer « expéditif ».

**C8. Sec. 3.** « dépasse de loin les régates » alors que l'exemple est une « course au large » (et la sec. 4 parle d'une « traversée océanique ») : trois termes pour la même chose. Proposer « les courses en mer » ou « le monde de la voile ».

**C9. Sec. 4.** « ramener ses chiffres vers la moyenne par prudence » puis « arrondir à 50 % par frilosité » : la « moyenne » (fréquence de base) et 50 % ne sont pas la même chose. Harmoniser, par exemple « vers une valeur moyenne ou 50 % ».

**C10. Sec. 4.** « règles de score *strictement propres* » : « propre » calque de l'anglais « proper », faux ami (propre = à soi ou net). Le texte ne l'explique pas avant « Elle est strictement propre lorsque… ». Ajouter une demi-phrase explicative. Aussi « pénalité moyenne attendue » est pléonastique : « pénalité espérée » (terme employé dans l'encadré).

**C11. Sec. 4.** « Le mot de calibration a ici un sens précis… le premier des deux sens qu'il prendra » : répète la définition qui précède et annonce un second sens (« modèles génératifs ») sans plus de précision. Supprimer la première moitié et garder seulement la mise en garde.

**C12. Sec. 4, dernier paragraphe.** « On peut calibrer des prévisions météorologiques quotidiennes, l'évaluation du risque de défaut de paiement… ou un tri automatique… On ne calibre pas une traversée océanique » : on calibre des prévisions, non une traversée ni un tri. Coordination bancale. Proposer « On peut calibrer des prévisions portant sur… ».

**C13. Sec. 2.** « la lecture comme jugement rend visible ce qu'un chiffre présenté comme objectif, et qui n'appartiendrait à personne, laisserait dans l'ombre » : calque de « reading as judgment », phrase lourde. Proposer « la lecture en termes de jugement ».

**C14. Points clés, premier point.** « et notamment sur les états de l'arrière-plan » : « notamment » est ambigu (les mondes possibles sont-ils autre chose que ces états ?). Cf. B2.

### Typographie
Rien de manifestement fautif (espaces avant « : » ; « % », guillemets, majuscules). Pas de signalement.

### Vérifications de calcul faites en lecture (pas de constat)
Le rapport 50, les surprises 3,00 / 6,91 / 0,051 / 0,001, le rapport 0,951 et les deux dérivées de l'encadré sont cohérents entre eux.

## 3. Appréciation globale

Sections les plus accessibles : « Prévision et prévisionniste » (sauf la Lecture de l'encadré), l'exemple météorologique de la calibration (70 % et 30 %), et la discussion sur « subjectif » dans la sec. 2. Les exemples sont concrets, le fil narratif est clair et l'encadré chiffré se vérifie à la lecture.

Sections les moins accessibles :
- Le paragraphe de la sec. 1 sur $A \cap (\dots) \rightarrow B$ (notations des chapitres antérieurs, six renvois, densité) ;
- La Lecture de l'encadré, avec ses glissements (« estimation juste », « quel bateau », « poids ») ;
- Le milieu de la sec. 4 (de « Pour évaluer des prévisions… » à l'encadré formel) : connecteur trompeur, phrase condensée sur la discrimination, terme « propre » inexpliqué ;
- La toute fin de la sec. 4 (« protéger autrement »).

Les renvois aux autres chapitres (ch0, ch1, ch2) supposent en plusieurs endroits que le lecteur a tout en tête (dinde, tableau de l'ébullition, cote, score) : un résumé d'une demi-phrase à chaque fois améliorerait nettement la lecture isolée.
