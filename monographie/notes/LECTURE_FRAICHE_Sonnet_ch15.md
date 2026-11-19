# Lecture fraîche du chapitre 15 (« L'érosion des vérifications humaines »)

Lecteur : Sonnet 5.5, première lecture, texte seul.

## 1. Ce que j'ai compris (test de lisibilité)

1. Quand un humain produisait lui-même un résultat, la lenteur lui fournissait sans qu'il s'en aperçoive des repères (attentes, résultats intermédiaires) qui pouvaient contredire le résultat final. Les modèles suppriment cette friction, donc ces repères, sans que l'organigramme le montre.
2. Un modèle répond toujours du même ton assuré : le signe qui trahit le doute (hésitation, forme bancale) disparaît. L'essai METR montre que l'impression de gagner du temps peut être l'inverse de la mesure.
3. La belle forme servait de signal coûteux de la qualité du fond. Devenue gratuite, elle ne trie plus : on arrive à un « équilibre mélangeant » (Spence, Akerlof). Seule une divulgation auditée peut rétablir un tri.
4. Ironie de Bainbridge : l'opérateur qui ne pratique plus les tâches courantes perd les compétences et la vigilance dont l'exception a besoin. Relire un brouillon de modèle revient à lire deux fois la même représentation.
5. Demander au modèle de relire sa propre solution transmet le cadre et provoque de la complaisance. Pour un vrai contrôle croisé, la personne fixe d'abord son avis par écrit, puis soumet au modèle le problème « nu » ; le chapitre renvoie au ch. 16 pour l'échelle collective.

Verdict : le fil se suit bien. Les difficultés viennent surtout des dépendances non rappelées (jargon des chapitres 6, 8, 9, 11, 12), de quelques phrases très denses, et d'un passage apparemment cassé en section 4.

## 2. Constats classés par gravité

### Gravité A (2)

**A1. § « L'ironie de Bainbridge… » (paragraphe de l'analyste).**
Passage : « mais vis-à-vis de ce que le cadre du modèle a laissé dans $(\dots)$ ou d'une erreur constante de ses données d'entraînement ».
Gêne : le complément de « a laissé dans » est illisible, il manque un mot (ou le LaTeX est un reste). La phrase est incompréhensible en l'état.
Proposition : « vis-à-vis de ce que le cadre du modèle a laissé hors champ, ou d'une erreur constante de ses données d'entraînement ». Si « $(\dots)$ » est voulu comme un ellipse typographique (« dans l'ombre »), il faut le dire en mots. Le sens ne bouge pas.

**A2. § « L'ironie de Bainbridge… », conclusion pratique, seconde condition.**
Passage : « elle évite de lui transmettre sa réponse ou son inclination. Elle lui soumet le problème nu […] ; ou, si elle doit lui présenter un texte déjà rédigé, elle lui demande explicitement de rechercher les failles […] sans jamais signaler la conclusion qu'elle privilégie ».
Gêne : la règle (ne pas transmettre sa réponse) et l'exception (présenter son texte rédigé) se contredisent en apparence. Le premier piège dit justement qu'une consigne détaillant une solution arrêtée transmet le cadre. Deux lectures plausibles :
(a) le texte est transmis mais sans la conclusion préférée, et le cadre n'est donc pas totalement neutralisé ;
(b) l'exception est un pis-aller, moins bon que le problème nu.
Proposition (sans trancher) : ajouter la nuance sous la forme « à défaut, et au prix d'une neutralité moindre, … » si (b), ou « même alors, le cadre du texte reste transmis » si (a).

### Gravité B (20)

**B1. Introduction, deuxième phrase.**
Passage : « Ce chapitre s'appuie sur les cinq conditions de détection du @sec:ch06 (…), sur la sévérité du @sec:ch09 (…), sur la production de texte plausible et l'orientation des modèles par des préférences humaines (@sec:ch11), et sur un constat de la @sec:ch13-propres-controles : nos propres contrôles s'effacent par défaut… ».
Gêne : phrase très longue qui empile quatre dépendances, et « Il montre » dans la phrase suivante se rattache mal à « Ce chapitre », alors que le dernier sujet nommé est « un constat ».
Proposition : couper après la liste des renvois et reprendre par « Le chapitre montre successivement… ».

**B2. § 1, fin du paragraphe sur les cinq conditions.**
Passage : « C'est cette deuxième source de comparateurs que le @tbl:ch13-sources nomme "vos propres contrôles" ».
Gêne : aucune « première source » n'a été annoncée dans ce chapitre. On peut croire qu'il s'agit de l'une des « deux sortes de repères », ou de la capacité à « se tromper autrement » ; le lecteur n'a pas le tableau du chapitre 13.
Proposition : « C'est cette source interne de comparateurs, distincte des sources externes, que le tableau… nomme… ». Le sens dépend de ce que le tableau 13 oppose réellement, ce que je ne peux pas vérifier.

**B3. § 2, déclencheur de vigilance.**
Passage : « il sert de déclencheur de vigilance pour la prise en compte (@def:prise-en-compte) ».
Gêne : « la prise en compte » est un terme technique non défini ici ; au sens ordinaire il est flou (prendre en compte quoi ? par qui ?).
Proposition : « pour la prise en compte de l'affirmation par son destinataire (@def:…) ». Un rappel de la définition en une demi-phrase serait préférable.

**B4. § 2.**
Passage : « un modèle de langage installé au sommet de la pile logicielle ».
Gêne : calque de « top of the software stack ». « Pile logicielle » n'est pas courant pour un lecteur cultivé, et l'idée (le modèle est la couche qui s'adresse à l'utilisateur) est implicite.
Proposition : « un modèle de langage placé en bout de chaîne, face à l'utilisateur ».

**B5. § 2, paragraphe sur l'uniformité de la voix.**
Passage : « pour les erreurs de devinette, il s'est déplacé dans la dispersion entre plusieurs tirages indépendants ; mais à la surface de la réponse unique […] le signe révélateur a entièrement disparu. Et devant une erreur constante, reposer la question ne fait que reproduire la même prose imperturbable. »
Gêne : trois jargons (« erreurs de devinette », calque de *guessing errors* ; « dispersion entre tirages » ; « erreur constante », sens non donné) sont enchaînés dans une phrase dense. Le contraste implicite entre les deux types d'erreurs (la dispersion trahit la devinette, pas l'erreur constante) n'est pas formulé, et le « Et » initial ne l'annonce pas.
Proposition : expliciter en une incise (« les erreurs où le modèle devine, c'est-à-dire où ses réponses varient d'un tirage à l'autre ») et remplacer « Et devant » par « En revanche, devant ».

**B6. § 2 et § 4.**
Passage : « sa frontière en dents de scie (@sec:ch12) » (deux occurrences).
Gêne : calque de *jagged frontier*. En français, « en dents de scie » évoque une oscillation, pas une frontière irrégulière, et rien ne dit ici ce que cette frontière sépare (tâches bien/mal maîtrisées). La lecture dépend entièrement du chapitre 12.
Proposition : à la première occurrence, « sa frontière irrégulière (tâches réussies, tâches manquées, sans régularité apparente, @sec:ch12) ».

**B7. § 2, paragraphe « La disparition du frottement… ».**
Passage : « produit un second effet, tout aussi déroutant, sur le jugement que celui qui travaille porte sur sa propre performance ».
Gêne : double saut non annoncé : on passe de l'effet sur le lecteur (signe révélateur) à l'effet sur l'auteur (impression de vitesse). De plus « second » entre en conflit avec « un second mécanisme de vigilance » à l'ouverture de la section. « Second » par rapport à quoi ?
Proposition : « Cette même fluidité a un autre effet, cette fois sur le jugement que l'utilisateur porte sur son propre travail ». Le sens ne bouge pas.

**B8. § 2, règle « mesurer plutôt que témoigner ».**
Passage : « la mémoire reconstruite après coup sans l'historique écrit de la @sec:ch03-calibration-historique » ; « historique confronté aux issues réelles ».
Gêne : « l'historique écrit de la § » se lit mal (la section n'a pas d'historique) ; « historique » est un terme de dépendance (ch. 3) pouvant être lu au sens de « histoire » ; « issues » est un faux ami (*outcomes*), « issues » signifiant plutôt « sorties » ou « solutions ». Même emploi en § 3 (« issues observées »).
Proposition : « sans le registre écrit décrit à la @sec:… » et « résultats effectivement observés » ; vérifier que « historique » est bien le terme du ch. 3.

**B9. § 3, fin du paragraphe sur le lien causal forme/fond.**
Passage : « Dans les termes de la @sec:ch09-severite (@def:severite), la sévérité de la belle forme contre une affirmation infondée est tombée près de zéro ».
Gêne : « sévérité » est un terme technique (probabilité qu'un test échoue si l'affirmation est fausse) rappelé nulle part. « La sévérité de la belle forme contre » est elliptique et calque d'un tour anglais.
Proposition : « la sévérité de la belle forme comme test (sa probabilité d'échouer quand l'affirmation est infondée) est tombée près de zéro ».

**B10. § 3, définition en gras de « signal coûteux ».**
Passage : « un indice observable qui reste crédible parce qu'il coûte cher à produire — en temps, en effort ou en maîtrise — lorsqu'on ne possède pas la qualité signalée, si bien qu'il perd sa valeur de tri dès qu'il devient presque gratuit ».
Gêne : la définition mêle trois idées dans une seule phrase : la crédibilité, le coût différentiel (cher seulement pour qui n'a pas la qualité) et la perte de valeur. « Valeur de tri » est du jargon. Le lecteur peut croire que tout indice coûteux est un signal.
Proposition : scinder en deux phrases : définition (coûteux pour qui n'a pas la qualité signalée, peu coûteux pour qui l'a), puis la conséquence (« si le coût disparaît, il ne permet plus de distinguer »). Sens inchangé.

**B11. § 2 et § 3, recouvrement.**
Passages : « (hésitation, précautions de langage ou forme encore approximative) » (définition du signe révélateur) et « les définitions glissaient, les paragraphes se répétaient, les renvois sonnaient faux […] ou le code refusait de compiler » (§ 3).
Gêne : le signe révélateur inclut déjà la forme approximative. La section 3 présente la perte de la forme comme un phénomène « suivant », distinct (seule la transition « une production isolée / tout l'échange social » les sépare). Le lecteur ne voit pas bien ce que la section 3 apporte de plus.
Proposition : ajouter à la transition un critère net, par exemple « le signe révélateur relève de l'auteur qui doute ; la forme comme signal relève de la qualité du travail effectivement fait ». Deux lectures sont possibles sur le découpage voulu ; je ne tranche pas.

**B12. Encadré « Sortir du mélange… ».**
Passage : « à l'opposé exact du blanchiment défini à la @def:blanchiment ».
Gêne : le « blanchiment » (à comprendre comme blanchiment épistémique ?) n'est ni défini ni évoqué dans le chapitre. Le lecteur ne sait pas à quoi s'oppose la divulgation. Le « à l'opposé exact » est fort.
Proposition : « à l'inverse du blanchiment (@def:blanchiment : [rappel en quelques mots]) ».

**B13. Encadré « Sortir du mélange… ».**
Passage : « consignant d'avance les affirmations, leur statut déclaré et leurs conditions avant de les confronter aux issues observées ».
Gêne : « leurs conditions » est ambigu : conditions de validité, de réfutation, de remise ?
Proposition : « leurs conditions de validité » ou « les résultats qui les réfuteraient », selon l'intention. Deux lectures : ne pas trancher.

**B14. § 4, deuxième face de l'ironie.**
Passage : « lorsque le flux courant paraît fluide et sans heurt — et plus encore lorsqu'aucun signe révélateur ne distingue les réponses douteuses et que la fréquence des alertes fondées recule (@sec:ch09-fausses-alertes) —, la vigilance s'émousse ».
Gêne : phrase longue à incise double, avec « alertes fondées » non défini (dépendance du ch. 9). Le rapport avec le « signe révélateur » n'est pas explicité.
Proposition : scinder en deux phrases et remplacer « alertes fondées » par « alertes qui se révèlent justifiées ».

**B15. § 4, enchaînement vers le contrôle croisé.**
Passage : « Cette dynamique générale explique pourquoi la posture […] "le modèle rédige un premier jet, et l'humain relit et corrige" échoue si souvent à constituer un véritable contrôle croisé ».
Gêne : Bainbridge (compétences perdues, vigilance) n'est pas la raison que donne le paragraphe suivant, qui invoque l'absence de représentation indépendante. Le lien causal annoncé n'est pas rempli.
Proposition : « Un autre mécanisme, plus direct, explique pourquoi… », ou bien relier explicitement les deux (perte de repères, donc pas de représentation indépendante). La seconde option change un peu l'argument : à l'auteur de choisir.

**B16. § 4, dépendances non rappelées.**
Passages : « contrôle croisé » (le terme-pivot du chapitre), « représentation indépendante (@def:representation) », « le cadre (@def:cadre) », « omission de saillance (@sec:ch12) », « (@prop:cause-commune) ».
Gêne : ces notions sont toutes renvoyées à des chapitres antérieurs. Une demi-phrase de rappel pour « contrôle croisé » et « cadre » suffirait, car ils portent la conclusion du chapitre. « Omission de saillance » est opaque.
Proposition : définir « contrôle croisé » à sa première mention en section 4, et gloser « omission de saillance » (« oubli de la piste qui ne ressort pas dans la consigne »).

**B17. § 4, second piège.**
Passage : « optimisés pour ce score, les modèles apprennent à exploiter ce biais d'approbation ».
Gêne : « ce score » n'a pas d'antécédent (la phrase parle de préférences exprimées par des évaluateurs, pas d'un score).
Proposition : « optimisés pour obtenir ces préférences, les modèles apprennent… ».

**B18. § 4, paragraphe sur la sévérité.**
Passage : « ($\Pr(A \mid E)$ dans l'@eq:ch09-accord-cotes) se rapproche de $\Pr(A \mid \bar{E})$ ».
Gêne : A, E et \bar{E} ne sont pas introduits. On devine A = accord ; E = affirmation erronée ? La phrase précédente décrit la probabilité de l'accord « lorsque l'affirmation est fausse mais présentée avec assurance », ce qui rend la lecture de E ambiguë (fausse ? présentée avec assurance ?).
Proposition : « (notée Pr(A | E), A pour l'accord du modèle, E pour l'affirmation erronée) ». À vérifier avec la définition du ch. 9.

**B19. Introduction, § 4 et Points clés : nombre de conditions.**
Passages : « ne forment un contrôle croisé que si la personne juge d'abord par elle-même » (intro) ; « qu'à deux conditions » (§ 4) ; « que si la personne arrête d'abord sa propre représentation et soumet ensuite le problème nu » (point clé).
Gêne : l'intro annonce une condition, la section en annonce deux, et le point clé les enchaîne. Le lecteur peut croire à une incohérence.
Proposition : harmoniser l'intro (« que si la personne juge d'abord par elle-même et ne transmet pas son cadre au modèle »).

**B20. Encadré « Question ».**
Passage : « le problème posé à neuf ».
Gêne : « à neuf » (= de nouveau, à partir de zéro) est peu clair, et le chapitre dit partout « le problème nu ». Faute probable pour « posé à nu ».
Proposition : « le problème posé de façon neutre ».

### Gravité C (12)

**C1. Calques lexicaux, répartis.** « frottement » et « friction » alternent pour le même concept (§ 1 et § 2) ; « sortie(s) » pour *output* (« une sortie plausible », « sorties générées ») ; « sa propre performance » (pour efficacité ou rendement) ; « ligne de base » (*baseline*) ; « dépôts de code » (*repositories*). Aucun n'est bloquant. Proposition : choisir un seul mot pour friction/frottement ; « résultat produit » pour « sortie ».

**C2. Variantes de terminologie.** Les repères que fabriquait la friction s'appellent « repères internes », « comparateurs », « vos propres contrôles » et « comparateurs personnels » (points clés). Le lecteur peut se demander s'il s'agit de notions différentes. Proposition : fixer un terme ou noter l'équivalence une fois.

**C3. § 1, liste « Des attentes préalables ».** « le signe d'une sensibilité » est opaque (calque de *sign of a sensitivity* ?), et la liste mélange des groupes nominaux (« l'ordre de grandeur… », « le sens de variation… ») avec une relative (« ou ce qui rendrait une conclusion manifestement absurde »). Proposition : « le signe attendu d'une variation » et « ou les valeurs qui rendraient… ».

**C4. § 1, image de l'alpiniste.** « antécime » est rare pour un lecteur non montagnard ; la dernière phrase glisse de « marcheur » à « lecteur » (« dépose le lecteur au bout du chemin »), alors que l'image portait sur l'alpiniste. Proposition : « sommet secondaire » et « dépose l'analyste ».

**C5. § 2, premier paragraphe.** « pas plus que l'assurance d'un orateur ne prouve qu'elle soit juste » : « elle » se rattache grammaticalement à « assurance » et non à « affirmation ». Proposition : « ne prouve qu'une affirmation soit juste ».

**C6. Connecteur « Or ».** « Or ce qui caractérise un modèle de langage… » (§ 2), « Or personne n'avait jamais dessiné… » (§ 1) : « Or » annonce une opposition ou un pivot, mais ici il ne fait que relancer. Proposition : « Ce qui caractérise… » / « Personne n'avait… ».

**C7. Encadré Spence.** « l'équilibre séparateur » et « tous les types émettent le même signal » : les notions de « type » et d'« équilibre séparateur » ne sont pas définies dans le chapitre alors que l'équilibre mélangeant l'est. Proposition : gloser « types » par « niveaux de qualité » et « séparateur » par « qui distingue les niveaux ».

**C8. Encadré « Sortir du mélange… », dernière phrase.** « la mention de conformité se mêle au bruit de surface au lieu de l'ordonner » : le référent de « l'ordonner » est flou (le bruit ? la surface ?). Proposition : « au lieu de permettre de trier les productions ».

**C9. § 4, titre et connecteur.** Le titre dit « les deux pièges de la consigne » alors que le second piège concerne l'orientation du modèle (complaisance), pas la consigne seule. Dans le second piège, « montrent ainsi » introduit un résultat expérimental qui n'est pas une conséquence de la phrase précédente. Proposition : « Des travaux expérimentaux montrent d'ailleurs ».

**C10. § 4.** « deux pièges liés au dialogue avec le modèle referment le contrôle sur lui-même » : métaphore peu transparente. Proposition : « privent encore ce contrôle de son indépendance ».

**C11. § 4, premier piège.** « le demandeur retire par avance au modèle la latitude de le contredire » : « le » peut renvoyer au cadre ou au demandeur. Les deux lectures sont plausibles. Proposition : « de contredire ce cadre ».

**C12. § 3.** Trois formules pour une même solution : « un engagement vérifiable » (avant l'encadré), « divulgation crédible » (titre de l'encadré), « divulgation auditée » (dans le texte). Le lecteur peut croire à trois mécanismes. Proposition : poser l'équivalence dans la phrase de transition.

## 3. Appréciation globale

Sections les plus accessibles : § 1 « La friction fabriquait des comparateurs » (image claire, exemples concrets, thèse nette), et l'encadré METR, très lisible avec ses chiffres. L'explication d'Akerlof (voitures d'occasion) fonctionne bien aussi.

Sections les moins accessibles : § 4, qui concentre le jargon rappelé de quatre chapitres (contrôle croisé, représentation, cadre, saillance, sévérité) et le seul passage cassé (A1). Les points sensibles sont la seconde condition (A2) et la notation de probabilité (B18). Viennent ensuite le paragraphe de § 2 sur l'uniformité de la voix (calques et jargon de ch. 12) et la définition de « signal coûteux » (B10).

Le registre d'ensemble est soutenu mais cohérent ; les seuls vrais obstacles sont les dépendances non rappelées et une poignée de phrases surchargées. Aucune faute typographique manifeste relevée.
