# Lecture fraîche — Partie 4 (« L’automatisation et ses angles morts »)

Fichier lu : `monographie/parties/partie-4.md` (introduction de partie, 5 paragraphes). Aucun autre fichier consulté.

## Résumé (test de lisibilité)

1. L’automatisation agit sur les contrôles de trois façons : elle les enchaîne (agents et pipelines, ch. 14), elle supprime les vérifications implicites du travail humain lent (ch. 15), et elle corrèle les contrôles restants quand tout le monde consulte le même modèle (ch. 16).
2. Chaque chapitre réutilise un modèle de la partie 2 ; les cas cités (Knight Capital, METR) servent d’illustrations datées, l’argument se veut indépendant des outils.
3. Le diagnostic étant posé, la partie 5 en tirera une pratique de la décision et de l’organisation des contrôles.

Le texte se lit bien dans l’ensemble ; la voix est nette. Les gênes tiennent surtout à quelques formules condensées qui supposent la partie 2 ou l’original anglais.

## Constats

### Gravité A

Aucun.

### Gravité B

**B1. « les mesures cités, de la panne de Knight Capital en 2012 à l’essai de METR en 2025, sont datés et présentés comme des études de cas »** (§1)
Gêne : « datés » a deux lectures en français, « munis d’une date, situés dans le temps » ou « dépassés ». La seconde affaiblirait les exemples, ce qui n’est sans doute pas voulu.
Reformulation : « … sont rattachés à leur date et présentés comme des études de cas ».
Risque de sens : oui. Si l’auteur voulait vraiment dire « appelés à vieillir », il faudrait plutôt écrire « … sont appelés à vieillir et sont présentés… ». Je ne tranche pas.

**B2. « modèle » dans deux sens à un paragraphe d’écart** (§1 « chaque chapitre réemploie un modèle de la @sec:partie-2 » ; §2 « on assemble les modèles en *pipelines* »)
Gêne : au §1, « modèle » désigne un modèle théorique (angles morts, blanchiment…). Au §2, le même mot désigne un modèle de langage, et ce n’est qu’après que l’on comprend le glissement.
Reformulation : au §2, « on assemble les modèles de langage en *pipelines* », ou au §1 « un modèle formel de la partie 2 ».
Risque de sens : aucun.

**B3. « ce qui ruine la comparabilité aux interfaces »** (§2)
Gêne : la formule est très condensée. « Comparabilité » et « interfaces » sont une possible dépendance à la partie 2, et on ne voit pas ce qui est comparé ni avec quoi.
Reformulation : « ce qui empêche, au passage d’une étape à l’autre, de confronter un résultat à ce qu’on en attendait ».
Risque de sens : oui. Selon le cadre de la partie 2, la comparaison pourrait porter soit entre deux résultats, soit entre un résultat et ses hypothèses. À vérifier.

**B4. « Donner le pouvoir d’agir à la couche qui offre le moins de garanties inverse ainsi l’architecture qui rendait la pile logicielle sûre. »** (§2)
Gêne : « ainsi » présente la phrase comme une conséquence, mais rien avant n’a dit que le modèle de langage est « la couche qui offre le moins de garanties », ni décrit l’architecture inversée. Le lecteur doit deviner quelle couche est visée. « Pile logicielle » est un calque de *software stack* et une possible dépendance.
Reformulation : « Confier le pouvoir d’agir au modèle de langage, la couche de la pile logicielle qui offre le moins de garanties, inverse l’architecture qui la rendait sûre. »
Risque de sens : faible. L’identification de la couche au modèle de langage est une inférence de lecteur.

**B5. « Une réponse instantanée supprime cette boucle, que personne n’avait jamais dessinée sur un organigramme. »** (§3)
Gêne 1 : « cette boucle » n’a pas d’antécédent nommé. Il faut reconstruire qu’il s’agit du va-et-vient entre l’ordre de grandeur attendu et les résultats intermédiaires.
Gêne 2 : « organigramme » se lit spontanément comme un organigramme hiérarchique. Le sens « logigramme, schéma de procédure » est possible mais vieilli.
Reformulation : « Une réponse instantanée supprime cette boucle de vérification implicite, que personne n’avait jamais inscrite dans une procédure. »
Risque de sens : oui. Avec « organigramme » au sens hiérarchique, on lit « aucun poste n’en avait la charge » ; au sens de schéma de procédure, on lit « elle ne figurait dans aucun processus formel ». Les deux lectures sont plausibles, je ne tranche pas.

**B6. « et l’aisance trompe jusqu’aux experts sur leur propre efficacité »** (§3)
Gêne : on ne sait pas de qui est l’aisance (la fluidité du texte produit par le modèle, ou la facilité ressentie par l’utilisateur). Le lien avec « leur propre efficacité » reste implicite : on devine une allusion à l’essai METR, qui n’est pas rappelé ici.
Reformulation : « et l’aisance de ses réponses trompe jusqu’aux experts, qui surestiment le gain qu’ils en tirent ».
Risque de sens : oui. « Surestiment le gain » est mon interprétation, et l’aisance pourrait aussi être celle du travail ressenti par l’expert. Je ne tranche pas.

**B7. « Relire le brouillon d’un modèle, c’est lire deux fois la même représentation »** (§3)
Gêne : la phrase est elliptique. On ne voit pas pourquoi relire reviendrait à lire deux fois la même chose ; il faut comprendre que le relecteur adopte le cadrage du brouillon au lieu d’en construire un autre. « Représentation » est une possible dépendance à la partie 2.
Reformulation : « Relire le brouillon d’un modèle, c’est épouser son cadrage : on lit deux fois la même représentation au lieu d’en confronter deux. »
Risque de sens : modéré. Le sens exact de « représentation » dans le livre pourrait être plus technique.

**B8. « le taux d’erreur baisse ; mais […] la probabilité d’échappement monte »** (§4)
Gêne : un lecteur peut y voir une contradiction (moins d’erreurs, mais plus d’erreurs qui passent ?). Il faut comprendre que l’échappement est une probabilité conditionnelle, celle qu’une erreur restante passe le relecteur. « Probabilité d’échappement » est une possible dépendance.
Reformulation : « … et la probabilité qu’une erreur restante échappe au relecteur monte ».
Risque de sens : oui. Si la partie 2 définit l’échappement comme une probabilité globale et non conditionnelle, la reformulation fausserait le propos. À vérifier.

**B9. « Un modèle entraîné sur l’archive écrite est un prêteur unique pour tous les emprunteurs : il attrape les erreurs de l’emprunteur, jamais celles du prêteur. »** (§4)
Gêne : la métaphore prêteur/emprunteur n’est pas introduite ici. On ne sait pas ce qui est prêté (des connaissances ? des formulations ?), et c’est une possible dépendance à la partie 2. « Attrape » est un calque de *catches*.
Reformulation : « Un modèle entraîné sur l’archive écrite est une source unique à laquelle tous empruntent : il repère les erreurs de ceux qui lui empruntent, jamais les siennes. »
Risque de sens : faible, si la métaphore est bien celle de l’emprunt de connaissances.

### Gravité C

**C1. « elle met les contrôles en chaîne »** (§1)
Gêne : le §2 décrit des étapes ou des modèles mis en chaîne, plutôt que des contrôles. Le décalage est léger.
Reformulation : « elle met les traitements en chaîne ».
Risque de sens : possible, si l’auteur considère chaque étape comme un contrôle.

**C2. « chaque chapitre réemploie un modèle de la @sec:partie-2, qu’il s’agisse des angles morts d’une chaîne, du blanchiment, de la sévérité ou de la probabilité d’échappement »** (§1)
Gêne : la phrase énumère quatre modèles pour trois chapitres. « Blanchiment » et « sévérité » sont de possibles dépendances : ils ne réapparaissent pas explicitement dans la suite de l’introduction.
Reformulation : « chaque chapitre réemploie un ou deux modèles de la partie 2 : … ».
Risque de sens : aucun.

**C3. « l’essai de METR »** (§1)
Gêne : le sigle n’est pas expliqué, et ce n’est peut-être pas nécessaire dans une introduction. Possible dépendance.
Reformulation : « l’essai de l’organisme METR ».
Risque de sens : aucun.

**C4. « *pipelines* », « trajectoire de douze étapes »** (§2)
Gêne : ce sont des anglicismes ou du jargon d’agents ; l’italique les signale, ce qui reste acceptable. « Trajectoire » au sens de suite d’actions d’un agent peut surprendre.
Reformulation (facultative) : « en chaînes de traitement (*pipelines*) » ; « une suite de douze étapes ».
Risque de sens : aucun.

**C5. « Le chapitre rappelle enfin l’ironie de l’automatisation »** (§3)
Gêne : « enfin » annonce le dernier point, mais deux autres idées suivent (relecture du brouillon, complaisance).
Reformulation : supprimer « enfin » ou remplacer par « aussi ».
Risque de sens : aucun.

**C6. « l’usure des alertes »** (§4)
Gêne : l’expression est compréhensible, mais l’usage français établi pour *alert fatigue* est « fatigue d’alerte » ou « lassitude face aux alertes ».
Reformulation : « la lassitude face aux alertes ».
Risque de sens : aucun.

**C7. « contrôleur », « comparateur », « relecteur » dans la même phrase ou à une phrase d’écart** (§4)
Gêne : les trois termes alternent pour ce qui semble être la même fonction, ou pas, ce qui peut faire hésiter. « Plancher fixé par les causes partagées » est une possible dépendance.
Reformulation : aucune si les termes sont définis distinctement en partie 2. Sinon, unifier.
Risque de sens : à vérifier contre les définitions de la partie 2.

**C8. « comment trancher une décision qui ne se jouera qu’une fois »** (§5)
Gêne : « trancher une décision » est une collocation peu idiomatique, puisqu’on tranche une question et qu’on prend une décision.
Reformulation : « comment trancher quand la décision ne se jouera qu’une fois ».
Risque de sens : aucun.

### Typographie

Rien de manifeste : apostrophes typographiques, ponctuation haute espacée et majuscules sont cohérentes. Les espaces insécables avant « : » et « ; » ne sont pas vérifiables à l’œil dans la source.
