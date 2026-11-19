# Lecture fraîche — chapitre 18 « Un remède à trois niveaux » (Sonnet)

Lecture à froid, du seul fichier `chapitres/18-remede-trois-niveaux.md`. Aucun autre fichier consulté, aucune modification du source.

## 1. Ce que j'ai compris du chapitre (test de lisibilité)

1. Le chapitre propose des pratiques de contrôle sur trois niveaux, chacune avec sa raison d'être, ses limites et son statut (dispositif documenté ou proposition). Les trois niveaux sont l'attitude individuelle, le placement des contrôles et l'organisation.
2. Niveau 1 : le praticien se fabrique ses propres comparateurs (attente écrite avant de lire le résultat, pré-mortem, élargissement des scénarios admis). Ils débordent le cadre de l'outil mais jamais celui de la personne, et les incitations finissent par les user.
3. Niveau 2 : placer le contrôle aux points de passage vers l'action, le confier à quelqu'un qui comprend une couche au-dessous, contrôler la représentation et pas seulement la sortie, proportionner l'effort aux enjeux et plafonner la production sur la capacité de contrôle. Le RAG est présenté comme un outil de placement, pas comme une garantie de véracité.
4. Niveau 3 : l'organisation rend la vigilance durable en dimensionnant la production sur la capacité d'évaluation, en exigeant un statut pour chaque affirmation, en tenant un historique daté et en mesurant l'échappement par des erreurs injectées (analogie avec les images de menaces fictives et le test par mutation).
5. Les trois niveaux se complètent pour couvrir les cinq conditions de détection. Le chapitre se clôt sur une grille de cinq questions à poser avant d'agir sur une affirmation, puis renvoie à la conclusion, qui soumettra le livre lui-même à ces questions.

Compréhension d'ensemble : bonne. Les points de blocage viennent surtout du fait que les « cinq conditions » ne sont jamais énumérées avant la légende de figure, et de quelques notations et termes jargonnants qui renvoient à des chapitres antérieurs.

## 2. Constats classés par gravité

### Gravité A (compréhension compromise)

**A1. [Niveau 1, « Se donner une attente… » ; repris au Niveau 2 et au RAG] Les « cinq conditions » ne sont jamais énumérées avant la figure.**
Passage : « Ce geste agit sur deux des cinq conditions (@sec:ch06-cinq-conditions). » Autres occurrences : « les cinq conditions de la @sec:ch06-cinq-conditions », « La technique agit ainsi sur deux des cinq conditions ».
Gêne : le lecteur ne sait ni quelles sont les cinq conditions ni quelles sont les « deux » visées. Toute l'architecture du chapitre (« quatrième condition », « deuxième et troisième condition ») repose sur une liste qui n'apparaît que dans la légende de la @fig:ch18-trois-niveaux, puis dans les cinq questions finales. Pour un lecteur qui n'a pas le chapitre 6 en tête, les numéros d'ordre sont opaques.
Reformulation minimale : à la première occurrence, intercaler la liste, par ex. « les cinq conditions de détection (existence d'un comparateur, capacité à se tromper autrement, comparabilité, arrivée à temps, prise en compte) ». Puis nommer : « Ce geste agit sur l'existence et sur la différence. » Même nommage pour le RAG (comparabilité et arrivée à temps, déjà nommées, il suffit alors de la liste initiale). Le sens ne bouge pas.

**A2. [Niveau 1, « Pratiquer le pré-mortem »] Notation « $(\dots)$ » inintelligible.**
Passage : « quelle variation de l'arrière-plan $(\dots)$ (@eq:ch01-regle) ».
Gêne : à l'affichage, le lecteur voit des points de suspension mathématiques suivis d'un renvoi d'équation. « Arrière-plan » n'est pas défini et on ne comprend pas ce que « variation de l'arrière-plan (…) » désigne.
Reformulation minimale : remplacer par une paraphrase sans formule (« quelle variation du contexte non représenté (l'arrière-plan du ch. 1) »), ou expliciter ce que les points représentent. Le sens dépend de ce que la formule désigne ; je ne peux pas trancher.

### Gravité B (gêne réelle)

**B1. [Niveau 2, introduction vs « Qui »] « couche » employé en deux sens.**
Passages : « le contrôle ne peut plus porter sur la couche prise en bloc » (couche de la pile technique) ; « comprenant au moins une couche au-dessous » (couche de compétence sous l'interface).
Gêne : un même mot désigne deux notions. Le lecteur peut croire que « la couche au-dessous » est la couche inférieure de la pile.
Reformulation minimale : dans l'introduction, « le contrôle ne peut plus porter sur l'ensemble du composant pris en bloc » ; garder « couche au-dessous » pour la compétence. Le sens ne bouge pas si « couche prise en bloc » vise bien la pile, ce que « sommet de la pile » laisse penser.

**B2. [Niveau 1, « Élargir… »] Symboles $b$ et $z$ non définis.**
Passage : « une marge $b$ ajoutée au risque estimé, qui relève du jugement et non d'une mesure de $z$ ».
Gêne : $z$ n'est pas défini. « qui » peut renvoyer à la marge ou au risque estimé.
Reformulation minimale : « une marge $b$ (§17) ajoutée au risque estimé ; cette marge relève du jugement, non d'une mesure de $z$ (la grandeur qui nous échappe) ». Selon ce que représente $z$, la glose change ; à vérifier.

**B3. [Niveau 1, « Élargir… »] Flottement terminologique : « mondes possibles » / « alternatives admises ».**
Passage : titre « l'ensemble des mondes possibles » ; texte « l'ensemble des alternatives admises $\Theta$ ».
Gêne : le lecteur ne sait pas si ce sont deux notions ; $\Theta$ n'est pas introduit.
Reformulation minimale : « l'ensemble des mondes possibles admis, noté $\Theta$ ». Choisir un seul terme.

**B4. [passim] Jargon des chapitres antérieurs non glosé (possibles dépendances).**
Ces termes sont utilisés sans définition dans le chapitre et sont inintelligibles sans les chapitres 6 à 17 :
- « prêteur unique » (« cercle du prêteur unique », « un même prêteur », « défaut du prêteur unique auquel toute la profession emprunte »), métaphore jamais expliquée, utilisée au moins quatre fois ;
- « blanchiment » (aux interfaces, de provenance) ;
- « équilibre mélangeant » ;
- « frontière en dents de scie », « omission structurelle, omission de saillance » ;
- « garantie préalable » et « sommet de la pile » ;
- « noyau de preuve » ;
- « chiffre nu » ;
- « sévérité du contrôle » ;
- « angle mort » (renvoi à une définition seulement) ;
- « contrôle croisé ».
Reformulation minimale : une demi-phrase de rappel au premier emploi (ex. « le cercle du prêteur unique (la dépendance de tous à une même source de jugement) »). Le contenu exact est à fixer par l'auteur ; je ne sais pas quelle est la définition exacte de « prêteur ».

**B5. [Niveau 2 « Combien », RAG, Niveau 3 « injection »] Notations et « échappement » avant leur définition.**
Passages : « le rapport des enjeux $L/\Delta U$ fixe le seuil $p^\ast$ » ; « sans réduire l'échappement » (section RAG) ; « $P(E)$ … $\Pr(\bar{C} \mid E)$ … $B_{\text{cmp}}$ ».
Gêne : le mot « échappement » est employé au Niveau 2 (RAG) et dans l'introduction du Niveau 3 (« ce que laissent passer ses propres filtres » n'est pas le mot) bien avant d'être posé comme probabilité dans la quatrième pratique, où il n'est d'ailleurs que rattaché à une définition par renvoi. Les symboles $L$, $\Delta U$, $p^\ast$, $E$, $\bar C$ ne sont pas glosés ; le lecteur ne sait pas que $\bar C$ signifie « le contrôle ne signale pas ».
Reformulation minimale : « l'échappement (la part des erreurs que le contrôle laisse passer) » à la première occurrence ; « $\Pr(\bar{C} \mid E)$ (probabilité que le contrôle ne signale pas une erreur $E$ réellement présente) ». Pas de changement de sens.

**B6. [Cinq questions, question 3] « conditions » : homonymie avec les « cinq conditions ».**
Passage : « Les conditions sont-elles énoncées de sorte que les deux puissent être comparés ? »
Gêne : dans ce chapitre, « conditions » désigne tantôt les cinq conditions de détection, tantôt les hypothèses de l'affirmation. Le « les deux » n'a pas d'antécédent immédiat dans l'encadré (c'est l'affirmation et le comparateur, mentionnés aux questions 1 et 2).
Reformulation minimale : « Les hypothèses et les unités sont-elles énoncées de sorte que l'affirmation et le comparateur puissent être comparés ? » Le sens est probablement conservé ; l'autre lecture (conditions = les cinq conditions) paraît improbable.

**B7. [Niveau 3, titre / quatre pratiques / Articulation] Le titre et la synthèse ne correspondent pas aux quatre pratiques.**
Passages : titre « L'organisation : indépendance, statut, historique et mesure » ; pratiques réelles : capacité, statut, historique, injection ; dans l'Articulation : « en évitant de dépendre d'un prêteur unique » et « en protégeant l'autorité de celui qui alerte ».
Gêne : « indépendance » est dans le titre et les deux engagements de l'Articulation (éviter le prêteur unique, protéger l'autorité de celui qui alerte) n'ont pas de pratique dédiée dans le corps du niveau 3. Seul « arbitrage explicite de la direction » et « contrôleurs nommés » s'en rapprochent.
Reformulation minimale : aligner le titre sur les pratiques (« capacité, statut, historique et mesure »), ou ajouter dans l'une des pratiques la phrase manquante sur l'indépendance de source et l'autorité d'alerte. Le choix change le contenu ; je ne tranche pas.

**B8. [Niveau 3, introduction vs fin de la quatrième pratique] Statut de la quatrième pratique contradictoire.**
Passages : « Les trois premières sont des propositions … ; la quatrième transpose des méthodes déjà pratiquées dans deux domaines » ; puis : « Transposer les erreurs injectées aux flux d'analyse … reste en revanche une *proposition* ».
Gêne : la quatrième pratique est présentée comme appuyée, puis comme une proposition. Le lecteur ne sait quel est son statut, alors que le chapitre annonce préciser « dispositif documenté ou proposition ».
Reformulation minimale : « la quatrième s'appuie sur des méthodes déjà pratiquées dans deux domaines, mais sa transposition ici reste une proposition ».

**B9. [Niveau 2, « Combien », 2e paragraphe] Connecteur trompeur.**
Passage : « Cette proportionnalité a une conséquence de flux… »
Gêne : le plafonnement par la capacité de contrôle ne découle pas de la proportionnalité aux enjeux, mais d'une contrainte de débit distincte. Le fil logique est faussé.
Reformulation minimale : « À la proportionnalité s'ajoute une contrainte de flux que l'accélération… fait souvent oublier. »

**B10. [Niveau 1, introduction] Lien non explicite entre l'observation et la « source ».**
Passage : « Ce renversement repose sur une observation simple, que le @sec:ch13 … range parmi les quatre sources de comparateurs : nos propres contrôles. »
Gêne : « que » peut renvoyer à « observation » ou à « sources » ; surtout, l'observation (le praticien en sait plus qu'il ne formalise) et « nos propres contrôles » ne sont pas la même chose. Saut elliptique.
Reformulation minimale : « Ce renversement repose sur une observation simple, qui rejoint l'une des quatre sources de comparateurs du @sec:ch13, nos propres contrôles : un praticien… » Deux lectures plausibles (l'observation illustre la source, ou lui est identifiée) ; la reformulation suit la première.

**B11. [Niveau 2, « Où »] Syntaxe lourde et construction douteuse.**
Passage : « aux points de passage où une sortie cesse d'être lue comme une ébauche que l'on discute pour être tenue pour acquise ».
Gêne : « pour être tenue pour acquise » se lit d'abord comme une finale (« discute afin d'être tenue ») ; phrase très longue avec liste de cinq critères.
Reformulation minimale : « où une sortie cesse d'être une ébauche que l'on discute et se trouve tenue pour acquise : elle s'exécute… ».

**B12. [Niveau 2, « Quoi »] « automatisé autour de la tâche ».**
Passage : « ce contrôle peut souvent être automatisé autour de la tâche (@sec:ch13-enonce-avance) ».
Gêne : on ne voit pas ce que signifie « autour de la tâche » (enrobé ? appliqué à la sortie ?). Dépend du ch. 13.
Reformulation minimale : « ce contrôle peut souvent être automatisé, en l'appliquant à chaque sortie de la tâche ». Interprétation incertaine.

**B13. [Encadré « Ce que mesurent… », point 1] « la revue structurelle de la ferrure » jamais introduite.**
Passage : « Dans la revue structurelle de la ferrure (@sec:ch05, @sec:ch08, @sec:ch13) ».
Gêne : la ferrure est un exemple récurrent du livre, mais n'apparaît pas dans ce chapitre ; le lecteur ne sait de quoi il s'agit. De plus, la phrase suivante est très longue.
Reformulation minimale : « Dans l'exemple de la ferrure (pièce métallique calculée par éléments finis, ch. 5) ». Scinder la phrase après « maintenance d'ouvrages côtiers ».

**B14. [Niveau 2, « Qui »] Tournure peu idiomatique.**
Passage : « il joue une mise en scène, qui peut être pire que l'absence de contrôle ».
Gêne : « jouer une mise en scène » est un calque ; la fin de la phrase (« pire que l'absence de contrôle ») est donnée comme une évidence alors que c'est l'argument.
Reformulation minimale : « il joue la comédie du contrôle, ce qui peut être pire que l'absence de contrôle ».

**B15. [Articulation, niveau 2] « garantit » contredit le ton du chapitre.**
Passage : « Il garantit la *différence* et la *comparabilité* en confiant le contrôle à des personnes… »
Gêne : le chapitre répète qu'aucun dispositif ne garantit rien (« aucune ne garantit rien »), et la section « Qui » montre qu'un mauvais contrôleur ruine l'effet.
Reformulation minimale : « Il soutient la différence et la comparabilité ». Le niveau d'assurance de l'auteur peut être voulu plus fort ; à lui de trancher.

**B16. [Niveau 1, pré-mortem] « La limite tient au contexte ».**
Passage : « La limite tient au contexte : réduit à une formalité cochée en fin de réunion… »
Gêne : le « contexte » n'est pas ce qui suit ; il s'agit de la manière dont l'exercice est mené et utilisé.
Reformulation minimale : « La limite tient à l'usage qui en est fait : ».

**B17. [Niveau 1, « Élargir… »] « Pour le raisonnement… Pour l'acte » elliptique.**
Passage : « Pour le raisonnement, cette branche prend la forme de trois questions de diagnostic… Pour l'acte, elle rejoint la marge d'humilité… »
Gêne : « cette branche » renvoie à la « branche réservée à la question “et si quelque chose nous échappait ?” » ; l'opposition raisonnement/acte n'est pas annoncée. Paragraphe dense.
Reformulation minimale : couper en deux phrases et annoncer « Cette branche joue sur deux plans. Sur le plan du raisonnement, … Sur le plan de la décision, … ».

**B18. [Cinq questions, introduction] Phrase à incise trop longue.**
Passage : « Avant de transformer une affirmation, qu'elle vienne d'un calcul classique, d'un modèle appris, d'un agent ou d'un comité d'experts, en une décision qui engage le monde, cinq autres questions portent sur… »
Gêne : le complément de « transformer » est séparé de lui par l'incise ; le sujet de la phrase (« cinq autres questions ») arrive très tard.
Reformulation minimale : « Cinq autres questions portent sur le dispositif de contrôle qui entoure l'affirmation, quelle que soit son origine (calcul classique, modèle appris, agent, comité d'experts), avant qu'on la transforme en décision qui engage le monde. »

**B19. [Encadré « Mesurer ce qui passe », test par mutation] Passage obscur pour un non-spécialiste.**
Passage : « Un mutant qui survit, à moins qu'il ne se comporte exactement comme l'original, signale une faute que la batterie ne pouvait pas détecter ».
Gêne : la réserve (mutant équivalent) est abstraite ; « ne pouvait pas détecter » (au lieu de « n'a pas détecté ») est plus fort que ce qui est démontré ; « sévérité nulle » n'est pas glosé.
Reformulation minimale : « Un mutant qui survit (sauf s'il se comporte exactement comme l'original, auquel cas il n'y a rien à détecter) révèle une faute que la batterie ne détecte pas : pour cette faute, la sévérité du contrôle était nulle. »

### Gravité C (confort / style)

- **C1. [Introduction]** « ni code de règles ni méta-procédure qui garantirait son propre cadre » : « code de règles » est un calque vraisemblable de « rulebook » ; « son » ambigu (chapitre ? procédure ?). Proposition : « ni recueil de règles ni méta-procédure qui garantirait son propre cadre (celui de la procédure) ». Le sens risque de bouger si « son » désigne le chapitre.
- **C2. [Niveau 1, 1er §]** « conduit à renverser cet ordre » : l'ordre n'est pas explicite (humilité après les calculs ?). Proposition : « à renverser cette hiérarchie : l'humilité vient avant les calculs, pas après ».
- **C3. [Niveau 1, 2e §]** « Encore faut-il qu'ils existent … ils disparaissent les premiers » : « ils » = comparateurs ou repères ? « les premiers » flou. Proposition : « Encore faut-il que ces comparateurs existent … ils sont les premiers à disparaître ».
- **C4. [Niveau 1, 3e §]** « avant que l'on se soit aligné sur le cadre du résultat reçu » : « aligné sur » est un anglicisme. Proposition : « avant d'avoir adopté le cadre du résultat reçu ».
- **C5. [Niveau 3, 1er §]** « la justesse du niveau 2 » : « justesse » est étrange pour un placement. Proposition : « le bon placement du niveau 2 ».
- **C6. [Niveau 3, capacité]** « le flux d'affirmations promues vers l'action » : « promues » est un calque de « promoted ». Proposition : « admises à passer à l'action ».
- **C7. [Encadré TIP]** « (*threat image projection*, TIP) » : l'acronyme n'est jamais réutilisé. Proposition : le supprimer.
- **C8. [Encadré nuance, point 3]** « accélérer la cadence des tests » : sens inattendu (on s'attend à « multiplier »). Proposition : « multiplier les tests ».
- **C9. [Encadré nuance, point 3]** « avant qu'un accident s'en charge » : idiome elliptique. Proposition : « avant qu'un accident ne le révèle ».
- **C10. [Passim]** Variation de vocabulaire : « conditions » / « barrages » (Articulation et points clés) ; « limites » (avant l'encadré) / « illusions » (dans l'encadré). Proposition : retenir un seul terme par notion ; la variante peut être voulue.
- **C11. [Cinq questions]** La liste numérotée est reprise mot pour mot dans l'encadré qui suit. Le lecteur lit deux fois les mêmes questions. Proposition : raccourcir la liste commentée, ou réserver l'encadré à la grille seule (sans changer le contenu).
- **C12. [Niveau 2, « Où »]** « On retrouve le partage du @sec:ch17 » : « partage » peut se lire comme « mise en commun » ; il s'agit de la distinction. Proposition : « la distinction ».
- **C13. [Niveau 2, « Où »]** « répond d'abord à la quatrième condition » : « d'abord » annonce une autre condition qui ne vient pas. Proposition : supprimer « d'abord ».
- **C14. [Niveau 2, « Combien »]** « la production admise jusqu'à l'action » : ambigu (production qui va jusqu'à l'action ?). Proposition : « la production admise à passer à l'action ».
- **C15. [Niveau 1, attente préalable]** « Elle ne sert donc pas à défendre… » : le « donc » enchaîne mal sur la limite (l'attente peut être arbitraire). Proposition : « Elle ne sert pas à défendre… ».
- **C16. [Introduction]** « l'automatisation les enchaîne, les érode et les corrèle » : trois verbes rapprochés dont « corréler » (transitif) est peu idiomatique ; renvoi à la partie 4 nécessaire. Proposition : « les enchaîne, les érode et les rend dépendants les uns des autres », si c'est bien ce sens.
- **C17. [Niveau 1, pré-mortem]** Le titre « Pratiquer le pré-mortem » précède la définition en gras ; acceptable, mais la définition arrive en deuxième paragraphe.
- **C18. [Points clés]** Les puces 2 et 4 sont des phrases de 60 à 70 mots avec parenthèses imbriquées. Proposition : les scinder.

Typographie : rien de manifestement fautif repéré (guillemets, apostrophes, tirets conformes). Je ne peux pas vérifier les espaces insécables à l'affichage.

## 3. Appréciation globale

Sections les plus accessibles : Niveau 1 (hors notations) pour l'attente préalable et la limite structurelle, qui s'appuie sur l'exemple du brouillard salin ; Niveau 2 « Qui » et « Quoi » (exemples parlants, enchaînement net) ; l'encadré sur les images de menaces fictives ; les points clés (exacts, mais denses).

Sections les moins accessibles : le début du Niveau 1 (« élargir les mondes possibles » : $\Theta$, $b$, $z$) ; le pré-mortem à cause de la formule « $(\dots)$ » ; Niveau 2 « Combien » (notations, enjeux, flux) ; l'introduction du Niveau 3, qui mêle titre et contenu discordants ; la quatrième pratique (notations $P(E)$, $\Pr(\bar C \mid E)$) ; l'introduction des cinq questions.

Le point qui pèse le plus sur la lecture est l'absence d'une liste explicite des cinq conditions dès leur première mention. Ensuite viennent le jargon hérité (« prêteur unique », « blanchiment », « équilibre mélangeant ») et les symboles non glosés. Hors ces points, le chapitre est bien construit et ses transitions entre niveaux sont claires.
