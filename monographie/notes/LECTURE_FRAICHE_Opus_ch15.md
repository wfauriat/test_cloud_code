# Lecture fraîche — chapitre 15 « L’érosion des vérifications humaines »

Lecteur : Opus (première lecture, seul le fichier `chapitres/15-erosion-verifications.md` a été lu).

## 1. Résumé de ce que j’ai compris (test de lisibilité)

1. Le travail lent produisait de lui-même des repères (attentes, résultats intermédiaires) qui servaient de comparateurs ; la génération instantanée les supprime sans que personne s’en aperçoive.
2. Les modèles parlent toujours avec la même assurance : la marque visible du doute (« signe révélateur ») disparaît, et la fluidité fausse même l’idée qu’on se fait de sa propre efficacité (essai METR : 19 % plus lent, 20 % plus rapide selon l’impression).
3. La belle forme n’est plus un signal coûteux du travail de fond : travail contrôlé et brouillon lisse deviennent indiscernables (équilibre mélangeant, Spence, Akerlof) ; seule une divulgation auditée en sort.
4. Ironie de Bainbridge : automatiser le courant atrophie les compétences que l’exception exige ; relire un brouillon du modèle, c’est lire deux fois la même représentation ; et demander au modèle de relire son travail se heurte au cadrage par la consigne et à la complaisance.
5. Un humain et un modèle ne forment un contrôle croisé que si l’humain juge d’abord seul, puis interroge le modèle sans lui transmettre sa réponse ni son inclination.

Le fil général se suit bien ; les difficultés se concentrent dans quelques passages techniques (fin de la section 2, paragraphe chiffré de la section 4) qui reposent sur des notions définies ailleurs.

## 2. Constats classés par gravité

### Gravité A — compréhension compromise ou contresens possible

**A1. Section « L’ironie de Bainbridge… », 3e paragraphe après l’intro (« Imaginons un analyste… »)**
Passage : « mais vis-à-vis de ce que le cadre du modèle a laissé dans $(\dots)$ ou d’une erreur constante de ses données d’entraînement »
Gêne : la notation $(\dots)$ est illisible pour qui n’a que ce chapitre ; on ne sait pas si c’est une notation définie ailleurs (par ex. la case « autres possibilités » d’un cadre) ou un reste de rédaction.
Proposition : « vis-à-vis de ce que le cadre du modèle a laissé hors champ ». Attention : deux lectures plausibles — soit $(\dots)$ est une notation formelle d’un chapitre antérieur (il faudrait alors la rappeler en clair : « … a laissé dans la catégorie résiduelle $(\dots)$, c’est-à-dire hors de ses hypothèses explicites »), soit c’est un espace réservé oublié. Je ne tranche pas.

**A2. Section « L’ironie de Bainbridge… », paragraphe « Rapportée au critère de sévérité… »**
Passage : « Si la probabilité que le modèle dise « votre raisonnement paraît solide » lorsque l’affirmation est fausse mais présentée avec assurance ($\Pr(A \mid E)$ dans l’@eq:ch09-accord-cotes) se rapproche de $\Pr(A \mid \bar{E})$, le rapport de vraisemblance de son accord s’effondre vers $1$. »
Gêne : $A$, $E$ et $\bar{E}$ ne sont pas définis dans le chapitre, et seule la moitié de la comparaison est dite en mots (rien n’indique ce que représente $\Pr(A \mid \bar{E})$) ; de plus « présentée avec assurance » n’apparaît pas dans la notation, ce qui laisse se demander si $E$ désigne « affirmation fausse » ou « affirmation fausse et assurée ». Possible dépendance (chapitre 9).
Proposition : « Si la probabilité que le modèle approuve ($A$) une affirmation fausse ($E$), $\Pr(A \mid E)$, se rapproche de la probabilité qu’il approuve une affirmation juste, $\Pr(A \mid \bar{E})$, le rapport de vraisemblance de son accord tombe vers $1$ : son approbation n’apporte plus d’information. » Le sens peut bouger si, dans l’équation du chapitre 9, $E$ signifie autre chose qu’« erreur » ; et la place de « présentée avec assurance » (condition de l’événement ou simple circonstance) reste à décider par l’auteur.

### Gravité B — gêne réelle

**B1. Section « La friction fabriquait des comparateurs », paragraphe « Rapportée aux cinq conditions… »**
Passage : « C’est cette deuxième source de comparateurs que le @tbl:ch13-sources nomme « vos propres contrôles » »
Gêne : rien dans le chapitre n’a introduit de liste de sources ; le lecteur cherche une « première source » et ne sait pas si « deuxième » renvoie aux « deux sortes de repères » (attentes / résultats intermédiaires) ou à la deuxième ligne d’un tableau du chapitre 13.
Proposition : « C’est cette source de comparateurs, la deuxième du @tbl:ch13-sources, que ce tableau nomme « vos propres contrôles » ». Si « deuxième » désignait en fait les résultats intermédiaires (deuxième puce), le sens change : à vérifier par l’auteur.

**B2. Section « La perte du signe révélateur », 3e paragraphe**
Passage : « L’effort de contrôle se concentre spontanément là où le producteur laisse paraître qu’il pourrait deviner. »
Gêne : calque de « might be guessing » ; en français, « deviner » sans complément se lit « trouver juste par intuition », presque l’inverse du sens voulu.
Proposition : « là où le producteur laisse paraître qu’il avance peut-être au jugé. »

**B3. Section « La perte du signe révélateur », 3e paragraphe**
Passage : « il sert de déclencheur de vigilance pour la prise en compte (@def:prise-en-compte) »
Gêne : « la prise en compte » employée seule comme terme technique est opaque (prise en compte de quoi ?) ; possible dépendance.
Proposition : « il déclenche la vigilance nécessaire à la prise en compte d’un désaccord (@def:prise-en-compte) » — à ajuster selon la définition réelle, que je ne connais pas.

**B4. Section « La perte du signe révélateur », 4e paragraphe**
Passage : « le signal interne d’incertitude n’a pas nécessairement disparu de la distribution du modèle : pour les erreurs de devinette, il s’est déplacé dans la dispersion entre plusieurs tirages indépendants ; […] Et devant une erreur constante, reposer la question ne fait que reproduire la même prose imperturbable. »
Gêne : trois notions techniques enchaînées sans rappel (« distribution du modèle », « tirages », opposition « erreur de devinette » / « erreur constante ») ; un lecteur non spécialiste perd le fil. Possible dépendance (chapitre 12). « Erreurs de devinette » sonne en outre étrangement en français.
Proposition (minimale) : « … pour les erreurs commises au hasard (erreurs de devinette), il se manifeste par des réponses qui varient d’un tirage à l’autre quand on repose la question ; […] Et devant une erreur constante, que le modèle reproduit à chaque tirage, reposer la question… »

**B5. Section « L’ironie de Bainbridge… », 1er paragraphe, et introduction du chapitre**
Passage : « un quatrième mécanisme vient miner la solidité de ce contrôle »
Gêne : le décompte n’est pas tenu ailleurs : la section 2 parle d’un « second mécanisme » puis d’un « second effet », la section 3 de « le phénomène suivant » ; le lecteur ne sait pas si l’effet METR compte. De plus, l’annonce du plan dans l’introduction ne mentionne pas l’ironie de Bainbridge.
Proposition : remplacer par « un autre mécanisme » ; et, dans l’introduction, ajouter « que l’automatisation des tâches courantes émousse les compétences requises par l’exception » avant « et qu’une personne et un modèle… ».

**B6. Section « L’ironie de Bainbridge… », paragraphe « Cette dynamique générale explique… »**
Passage : « Cette dynamique générale explique pourquoi la posture devenue la plus courante […] échoue si souvent à constituer un véritable contrôle croisé »
Gêne : connecteur trompeur : l’ironie de Bainbridge porte sur l’atrophie des compétences et l’émoussement de la vigilance, alors que l’explication qui suit repose sur l’adoption du cadre du modèle ; le lien de causalité annoncé n’est pas celui qui est développé.
Proposition : « Cette dynamique éclaire aussi pourquoi… » (le sens bouge peu ; si l’auteur voulait dire que l’atrophie est bien la cause, il faudrait l’expliciter dans le paragraphe suivant).

**B7. Section « L’ironie de Bainbridge… », premier piège**
Passage : « plus elle favorise une omission de saillance (@sec:ch12) sur toute piste divergente »
Gêne : « omission de saillance » est un jargon non rappelé (possible dépendance) et « favoriser une omission sur une piste » est une construction obscure.
Proposition : « plus elle pousse le modèle à passer sous silence toute piste divergente (omission de saillance, @sec:ch12) ».

**B8. Section « La forme ne signale plus le fond », définition de « signal coûteux »**
Passage : « un indice observable qui reste crédible parce qu’il coûte cher à produire — en temps, en effort ou en maîtrise — lorsqu’on ne possède pas la qualité signalée, si bien qu’il perd sa valeur de tri dès qu’il devient presque gratuit »
Gêne : la condition essentielle (« lorsqu’on ne possède pas la qualité ») est rejetée après l’incise et se lit d’abord comme une circonstance temporelle ; la définition est difficile à suivre d’un trait.
Proposition : « un indice observable qui reste crédible parce qu’il coûte cher à produire (en temps, en effort ou en maîtrise) à qui ne possède pas la qualité signalée ; il perd donc sa valeur de tri dès qu’il devient presque gratuit. »

**B9. Encadré « Sortir du mélange par une divulgation crédible »**
Passage : « à l’opposé exact du blanchiment défini à la @def:blanchiment »
Gêne : « blanchiment » n’est pas rappelé ; au sens courant (argent sale), le rapprochement est déroutant. Possible dépendance.
Proposition : « à l’opposé exact du blanchiment (@def:blanchiment), qui fait passer un résultat non contrôlé pour contrôlé » — formulation à valider selon la définition réelle.

**B10. Encadré « Signaux coûteux et marché des véhicules d’occasion », point 1**
Passage : « l’équilibre séparateur s’effondre et tous les types émettent le même signal »
Gêne : « équilibre séparateur » et « types » (au sens économique) ne sont pas définis ; le premier se devine par opposition à « équilibre mélangeant », le second non.
Proposition : « la séparation s’effondre et producteurs compétents comme incompétents émettent le même signal ».

**B11. Points clés, dernier point**
Passage : « et soumet ensuite le problème nu sans transférer son cadre par la consigne »
Gêne : incohérence avec le corps, qui admet aussi de soumettre un texte déjà rédigé en demandant les failles sans signaler la conclusion ; le point clé ne retient qu’une des deux voies.
Proposition : « et interroge ensuite le modèle sans lui transmettre sa réponse ni son inclination (problème nu ou recherche de failles sans conclusion affichée) ».

**B12. Section « L’ironie de Bainbridge… », paragraphe « La conclusion pratique de ces deux pièges… »**
Passage : « La conclusion pratique de ces deux pièges est nette »
Gêne : la première condition (se forger un avis avant de lire le modèle) découle du scénario du brouillon (paragraphe « Imaginons un analyste… »), pas des deux pièges, qui concernent le modèle relecteur ; l’enchaînement attribue la conclusion à la mauvaise prémisse.
Proposition : « La conclusion pratique de cette analyse est nette ».

### Gravité C — confort et style

**C1. Introduction** — « lorsqu’aucun agent n’est branché sur le monde » : image vague, proche du calque. Proposition : « lorsqu’aucun agent n’agit directement sur le monde ».

**C2. Introduction** — la phrase « Ce chapitre s’appuie sur les cinq conditions… » enchaîne quatre dépendances et une citation de constat ; dense. Proposition : la couper après « (@sec:ch11) » : « … (@sec:ch11). Il reprend aussi un constat de la @sec:ch13-propres-controles : … ».

**C3. Section « La friction… », dernier paragraphe** — « la génération instantanée dépose le lecteur au bout du chemin » : l’analogie passe de l’alpiniste au « lecteur » sans transition. Proposition : « dépose l’utilisateur au bout du chemin ».

**C4. Section « La perte du signe révélateur », 4e paragraphe** — « un modèle de langage installé au sommet de la pile logicielle » : « pile logicielle » (calque de *stack*) est du jargon. Possible dépendance (@sec:ch12-trois-bascules). Pas de reformulation sans connaître le sens précis.

**C5. Section « La perte du signe révélateur », 4e paragraphe** — « franchir sa frontière en dents de scie (@sec:ch12) » : image non rappelée, possible dépendance. Proposition : « franchir sa frontière en dents de scie, la limite irrégulière de ses compétences (@sec:ch12) ».

**C6. Section « La perte du signe révélateur », 5e paragraphe** — « lire une sortie plausible mais étrangère » : « étrangère » est ambigu (hors sujet ? écrite par un autre ?). Proposition : « une sortie plausible mais que l’on n’a pas écrite ».

**C7. Section « La perte du signe révélateur », après l’encadré METR** — « ne prétend pas isoler à lui seul la fluidité comme cause unique » : redondance. Proposition : « ne prétend pas isoler la fluidité comme cause unique ».

**C8. Même paragraphe** — « chronomètre contre une ligne de base » : calque de *against a baseline*. Proposition : « chronomètre comparé à une ligne de base ».

**C9. Section « La forme ne signale plus le fond », 4e paragraphe** — « est tombée près de zéro » → « est tombée à près de zéro ».

**C10. Section « La forme ne signale plus le fond », 6e paragraphe** — « le contrôle véritable sur le fond — contrôler chaque source » : répétition rapprochée de « contrôle/contrôler ». Proposition : « — vérifier chaque source dans les textes originaux ». Dans la même phrase, « le cadre » apparaît avant d’être relié à sa définition (@def:cadre, section suivante) ; possible dépendance.

**C11. Encadré « Sortir du mélange… »** — « devient elle-même une parole gratuite » : calque probable de *cheap talk* ; compréhensible mais le sens technique échappe. Proposition : « devient elle-même une déclaration gratuite (*cheap talk*) ». Même encadré : « n’importe qui, ou n’importe quelle consigne, peut joindre » — une consigne ne « joint » rien ; proposition : « n’importe qui peut, d’une simple consigne, faire joindre… ».

**C12. Encadré « Sortir du mélange… », dernière phrase** — « se mêle au bruit de surface au lieu de l’ordonner » : « ordonner » est ambigu (mettre en ordre / commander). Proposition : « au lieu de permettre de le trier ».

**C13. Points clés, deuxième point** — « un modèle […] peut tromper jusqu’aux experts sur leur propre efficacité » attribue l’effet METR à la prose du modèle, alors que le corps parle de la fluidité de l’interaction et refuse explicitement d’en faire la cause unique. Proposition : « … et la fluidité de l’échange peut tromper jusqu’aux experts sur leur propre efficacité ».

Typographie : rien de manifestement fautif relevé (espaces insécables, guillemets et majuscules corrects).

## 3. Appréciation globale

Chapitre bien construit, à la progression claire et aux images efficaces (l’alpiniste et l’hélicoptère, le marché des voitures d’occasion). Les sections les plus accessibles sont « La friction fabriquait des comparateurs » et « La forme ne signale plus le fond » (hors encadrés), qui se lisent sans aucune connaissance préalable. Les moins accessibles sont la fin de « La perte du signe révélateur » (concentration de notions du chapitre 12 : tirages, erreurs de devinette ou constantes, frontière en dents de scie) et la section « L’ironie de Bainbridge… », dont le paragraphe chiffré sur la complaisance et la notation $(\dots)$ supposent le formalisme des chapitres 7 à 9 ; c’est là que le lecteur cultivé décroche. Le décompte des mécanismes et l’annonce du plan en introduction gagneraient à être alignés.
