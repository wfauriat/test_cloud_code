# Corrections appliquées : partie 2 (page de partie et chapitres 5 à 9)

Source : relectures « à froid » de Sonnet et d’Opus (`notes/LECTURE_FRAICHE_*`). Une correction n’a été appliquée que si le problème était relevé par les deux lecteurs, ou par un seul et vérifié sur le texte ; si une seule lecture du passage était plausible ; si la correction était locale et minimale ; et si le sens, la portée et la force de l’affirmation restaient identiques. Les autres constats figurent dans `notes/A_TRANCHER_partie2.md`.

Aucune étiquette, clé de citation, formule, aucun nombre, titre de chapitre ou de section, bloc `:::`, statut ni renvoi n’a été modifié (contrôle automatique contre `HEAD` : seul ajout, la notation $\bar{A}$ en ch. 9, E2). Aucun terme du registre n’a été remplacé ni mis en gras ; « blanchiment » est seulement nommé en italique sur la page de partie (E2), sans définition.

## Récapitulatif

| Fichier | Corrections appliquées | dont relevées par les deux lecteurs | dont relevées par un seul lecteur et vérifiées |
| :-- | --: | --: | --: |
| `parties/partie-2.md` | 3 | 2 | 1 |
| `chapitres/05-trois-incertitudes.md` | 6 | 4 | 2 |
| `chapitres/06-detecter-une-erreur.md` | 8 | 3 | 5 |
| `chapitres/07-cadre-cause-commune.md` | 9 | 5 | 4 |
| `chapitres/08-independance-chaines.md` | 13 | 7 | 6 |
| `chapitres/09-severite-echappement.md` | 12 | 5 | 7 |
| **Total** | **51** | **26** | **25** |

Expressions communes à plusieurs fichiers : aucune correction n’a été appliquée en série. L’image « signature » (ch. 6, 8 et 9, et aussi ch. 16 à 18) a été relevée par les lecteurs des ch. 6 et 8. Elle est délibérément récurrente dans le livre et n’a pas été retouchée (voir `A_TRANCHER_partie2.md`, liste transversale).

`make verifier` après corrections : 0 erreur. Le seul avertissement (`chapitres/01-outils-logique-probabilite.md` : tableau généré absent) est hors périmètre et existait déjà. Pour le périmètre, la sortie est identique à celle d’avant les corrections, aux numéros de ligne près (références candidates « ? » et marqueur `A-VERIFIER` du ch. 5, inchangés).

---

## `parties/partie-2.md`

**E1.** Paragraphe consacré au chapitre 7.
- AVANT : « Aucune procédure de contrôle de niveau supérieur ne lève cette limite, car elle reposerait à son tour sur un cadre fini qu’il faudrait contrôler. »
- APRÈS : « Aucune procédure de contrôle de niveau supérieur ne lève cette limite, car une telle procédure reposerait à son tour sur un cadre fini qu’il faudrait contrôler. »
- Constats : Sonnet C4 ; Opus B1.
- Justification : « elle » renvoyait grammaticalement à « cette limite » ; les deux lecteurs lisent « la procédure ».

**E2.** Paragraphe consacré au chapitre 8.
- AVANT : « Ce blanchiment rend les résultats impossibles à comparer »
- APRÈS : « Cette perte, que le chapitre appelle *blanchiment*, rend les résultats impossibles à comparer »
- Constats : Sonnet B2 (première partie) ; Opus B4.
- Justification : le terme tombait avec un démonstratif comme s’il avait été défini. Il est désormais nommé, sans définition ni gras. La portée de la phrase est inchangée : « cette perte » reprend la phrase précédente, comme le faisait « ce blanchiment ». La force de « impossibles », relevée par Sonnet, est laissée à l’auteur.

**E3.** Paragraphe consacré au chapitre 9.
- AVANT : « et des alertes trop souvent fausses finissent par être négligées. »
- APRÈS : « et, quand les alertes sont trop souvent fausses, on finit par les négliger. »
- Constat : Opus C8 (vérifié).
- Justification : une alerte n’est pas « souvent fausse » ; c’est le flux d’alertes qui l’est. Même sens.

---

## `chapitres/05-trois-incertitudes.md`

**E1.** Chapeau.
- AVANT : « Le lecteur qui suit l’un des parcours de la @sec:ch00-parcours pourra s’y reporter au besoin. »
- APRÈS : « Le lecteur qui suit l’un des parcours de la @sec:ch00-parcours pourra se reporter au besoin à ces chapitres. »
- Constats : Sonnet B1 (première partie) ; Opus C (introduction).
- Justification : « s’y » pouvait renvoyer aux chapitres cités ou au parcours ; les deux lecteurs lisent « les chapitres cités ».

**E2.** § L’incertitude ontologique (`sec:ch05-incertitude-ontologique`), paragraphe de la dinde.
- AVANT : « les matins tranquilles départagent déjà mal un fermier toujours bienveillant d’un danger quotidien minime. »
- APRÈS : « les matins tranquilles distinguent déjà mal un fermier toujours bienveillant d’un danger quotidien minime. »
- Constats : Sonnet B3 ; Opus B3.
- Justification : « départager A de B » n’est pas idiomatique (calque de *distinguish A from B*) ; « distinguer A de B » a le même sens.

**E3.** § Une barre d’erreur mesure un désaccord (`sec:ch05-barre-erreur-desaccord`), après la proposition.
- AVANT : « Une hypothèse absente de $\Theta$ y reçoit un poids nul ; »
- APRÈS : « Une hypothèse absente de $\Theta$ reçoit un poids nul dans ces moyennes ; »
- Constat : Opus C (§4, vérifié).
- Justification : « y » pouvait se lire « dans $\Theta$ », ce qui contredit « absente de $\Theta$ » ; le référent est « des moyennes prises sur l’ensemble $\Theta$ », à la phrase précédente.

**E4.** Encadré `.nuance` « Ce que signifie le silence d’une barre d’erreur », 2e paragraphe.
- AVANT : « ne laisse littéralement aucune trace dans l’écart calculé. »
- APRÈS : « ne laisse littéralement aucune trace dans la barre d’erreur calculée. »
- Constats : Sonnet C8 (première partie) ; Opus C (encadré « nuance »).
- Justification : « écart » pouvait se lire « écart-type » ou « différence ». Les deux lecteurs proposent « barre d’erreur », objet de l’encadré et de son titre. « Décalage réel », plus loin, est conservé.

**E5.** § Pourquoi les outils de robustesse restent à l’intérieur du cadre (`sec:ch05-outils-robustesse`), avant-dernier paragraphe.
- AVANT : « Le danger ne vient donc pas du coefficient de sécurité ni des études de robustesse elles-mêmes, mais de l’illusion qu’elles entretiennent lorsqu’on confond »
- APRÈS : « Le danger ne vient donc pas du coefficient de sécurité ni des études de robustesse elles-mêmes, mais de l’illusion qu’entretiennent ces outils lorsqu’on confond »
- Constat : Sonnet C3 (vérifié).
- Justification : « elles » ne reprenait que « les études », alors que la phrase suivante (« une marge de 1,8 ou une batterie de tests ») vise les deux. « Ces outils » reprend le mot de la section, qui couvre aussi le coefficient de sécurité.

**E6.** Même paragraphe.
- AVANT : « peut se croire déjà acquittée de l’incertitude ontologique »
- APRÈS : « peut se croire déjà quitte de l’incertitude ontologique »
- Constats : Sonnet C2 ; Opus C (§5).
- Justification : impropriété lexicale ; « se croire quitte de » est l’idiome de même sens.

---

## `chapitres/06-detecter-une-erreur.md`

**E1.** § Cinq conditions (`sec:ch06-cinq-conditions`), première phrase.
- AVANT : « Munis de ces trois termes, nous pouvons énoncer le principe général de la détection d’erreur. »
- APRÈS : « Munis de ces trois notions (affirmation, contrôle, comparateur), nous pouvons énoncer le principe général de la détection d’erreur. »
- Constat : Opus B2 (vérifié).
- Justification : la section précédente se clôt sur les trois *familles* de comparateurs, ce qui brouillait le référent. Le chapeau parle des « notions d’affirmation, de contrôle et de comparateur », et la proposition qui suit les emploie ; aucune autre lecture n’est plausible.

**E2.** § Taux d’erreur et probabilité d’échappement (`sec:ch06-echappement`), 2e paragraphe.
- AVANT : « expose moins qu’un outil plus exact dont les fautes passent sans contradiction. »
- APRÈS : « expose à moins de risque qu’un outil plus exact dont les fautes passent sans contradiction. »
- Constats : Sonnet C7 ; Opus C11.
- Justification : l’emploi intransitif d’« exposer » est elliptique ; le complément manquant est rétabli.

**E3.** Encadré `.formel` « Condition nécessaire de détection et échappement total », 1er paragraphe.
- AVANT : « un contrôle particulier chargé de l’examiner avant qu’une action soit engagée. »
- APRÈS : « un contrôle particulier chargé d’examiner l’affirmation avant qu’une action soit engagée. »
- Constat : Opus B9 (vérifié).
- Justification : « l’ » pouvait renvoyer à « la sous-classe d’erreurs » ; par définition, un contrôle examine une affirmation (@def:controle).

**E4.** § Le cas Challenger, encadré `.cas`, 2e paragraphe.
- AVANT : « les données retenues ne faisaient pas apparaître la tendance nette de dégradation par temps froid, que révèle au contraire l’ensemble des 23 vols antérieurs documentés lorsqu’on les porte tous sur un même axe de température [@tufte1997]. »
- APRÈS : « les données retenues ne faisaient pas apparaître la tendance nette de dégradation par temps froid. L’ensemble des 23 vols antérieurs documentés révèle au contraire cette tendance lorsqu’on les porte tous sur un même axe de température [@tufte1997]. »
- Constat : Sonnet C10 (vérifié : environ 70 mots).
- Justification : phrase trop longue coupée en deux ; la relative devient une phrase autonome. Nombre, citation et fond inchangés.

**E5.** § Le cas Challenger, puce « Comparabilité », dernière phrase.
- AVANT : « Les graphiques ne rapprochaient pas dans une forme lisible ce que les vols antérieurs montraient de la température prévue pour le lendemain. »
- APRÈS : « Les graphiques ne mettaient pas en regard, sous une forme lisible, ce que montraient les vols antérieurs et la température prévue pour le lendemain. »
- Constats : Sonnet B6 ; Opus B12.
- Justification : « ce que les vols montraient de la température » se lisait « au sujet de la température ». Les deux lecteurs retiennent la même construction (mettre en regard X et Y). C’est la reformulation d’Opus, la plus proche du texte.

**E6.** § Ce que montrent un désaccord et un accord (`sec:ch06-accord-desaccord`), 2e paragraphe.
- AVANT : « Le premier calcul peut comporter une erreur de modélisation ou de codage ; mais le comparateur peut lui aussi être fautif »
- APRÈS : « L’affirmation elle-même peut comporter une erreur de modélisation ou de codage ; mais le comparateur peut lui aussi être fautif »
- Constat : Opus B13 (vérifié).
- Justification : le premier calcul cité dans la phrase précédente est le calcul à la main, c’est-à-dire le comparateur. L’opposition « affirmation / comparateur » qui suit fixe le sens voulu.

**E7.** Même section, dernier paragraphe.
- AVANT : « puisqu’il démontre qu’un des deux côtés au moins fait défaut ; »
- APRÈS : « puisqu’il démontre qu’un des deux côtés au moins est erroné ; »
- Constat : Opus B14 (vérifié).
- Justification : faux sens. « Faire défaut » signifie « manquer », sens que le chapitre emploie ailleurs (« l’une des conditions fait défaut »). Le texte dit plus haut « au moins l’un des deux termes est faux ».

**E8.** Points clés, 4e puce.
- AVANT : « l’omission des vols sans dommage sur le graphique examiné la veille a privé l’analyse de différence et de comparabilité, »
- APRÈS : « l’omission des vols sans dommage sur le graphique examiné la veille a fait céder les conditions de différence et de comparabilité, »
- Constats : Sonnet C17 ; Opus C21.
- Justification : « priver de différence » se lit comme un nom commun. « Céder » est le verbe que le chapitre emploie pour les conditions.

---

## `chapitres/07-cadre-cause-commune.md`

**E1.** § La défaillance de mode commun (`sec:ch07-mode-commun`), exemple des pompes.
- AVANT : « elles ne forment qu’un double câblage sous une vulnérabilité unique. »
- APRÈS : « elles ne forment qu’une protection dédoublée, exposée à une vulnérabilité unique. »
- Constats : Sonnet C2 ; Opus C3.
- Justification : image peu claire (« double câblage sous ») ; même idée d’une seule protection dédoublée, d’après la reformulation d’Opus.

**E2.** § Le cadre comme cause commune (`sec:ch07-cause-commune`), 2e paragraphe.
- AVANT : « reprenant la lettre esquissée au @sec:ch05 »
- APRÈS : « reprenant la lettre introduite de façon informelle au @sec:ch05 »
- Constat : Opus C4 (vérifié).
- Justification : on n’« esquisse » pas une lettre. Le ch. 5 écrit : « que nous noterons $z$ de façon informelle ».

**E3.** Même section, paragraphe du mécanisme.
- AVANT : « l’accord ou le désaccord entre $f_1(x)$ et $f_2(x)$ est déjà arrêté — tout au plus à des tirages internes sans lien avec $z$. »
- APRÈS : « l’accord ou le désaccord entre $f_1(x)$ et $f_2(x)$ est déjà arrêté, aux tirages internes près, qui n’ont aucun lien avec $z$. »
- Constats : Sonnet B2 ; Opus B1.
- Justification : phrase agrammaticale (« près » manquant) ; les deux lecteurs proposent la même tournure.

**E4.** Même paragraphe.
- AVANT : « Le rapport de vraisemblance de cet accord, conditionnellement à $x$, vaut exactement $1$ : »
- APRÈS : « Le rapport de vraisemblance de cet accord (erreur importante contre erreur faible), conditionnellement à $x$, vaut exactement $1$ : »
- Constats : Sonnet B3 ; Opus C7.
- Justification : un rapport de vraisemblance s’entend toujours « de quoi contre quoi », et le texte courant ne le disait pas. La glose reprend les deux hypothèses du modèle M3 ($H_{\text{grand}}$, $H_{\text{petit}}$) sans rien ajouter.

**E5.** Encadré `.formel` « Modèle M3 », *Argument*.
- AVANT : « $H_{\text{grand}}$ (l’erreur $|e(x, z)|$ dépasse une tolérance fixée) »
- APRÈS : « $H_{\text{grand}}$ (l’erreur $|e(x, z)|$ dépasse un seuil fixé) »
- Constat : Opus B6 (vérifié).
- Justification : « tolérance » désignait déjà le seuil de concordance de l’événement $A$ (« au sens d’une tolérance convenue »). Ce sont deux seuils distincts, et le second prend un autre nom. Le premier emploi est conservé.

**E6.** Phrase qui annonce l’encadré `.nuance` « Portée réelle du conditionnement sur le cadre ».
- AVANT : « Cet argument formel appelle trois précisions sur son champ d’application réel : conditionner nettement sur $x$ reste une idéalisation, et l’impuissance d’un contrôle interne face à $z$ ne retire rien à son utilité »
- APRÈS : « Cet argument formel appelle trois précisions sur son champ d’application réel : conditionner nettement sur $x$ reste une idéalisation, un facteur peut être représenté sans être mobilisé, et l’impuissance d’un contrôle interne face à $z$ ne retire rien à son utilité »
- Constats : Sonnet B7 ; Opus B2.
- Justification : trois précisions étaient annoncées et deux seulement énumérées. L’élément manquant reprend le titre de la deuxième puce de l’encadré (« Représenter un facteur sans le mobiliser ») ; il n’ajoute rien au fond.

**E7.** § La régression à l’infini (`sec:ch07-regression`), paragraphe de Goodman.
- AVANT : « Imaginons qu’on appelle « vleu » (*grue* en anglais) »
- APRÈS : « Imaginons qu’on appelle « *vleu* » (*grue* en anglais) »
- Constat : Opus C13 (vérifié).
- Justification : typographie. Toutes les autres occurrences (*vleue*, *vleues*, « *vleu* ») sont en italique.

**E8.** § Comment une pertinence nouvelle entre dans un cadre (`sec:ch07-deux-voies`), paragraphe « Ces deux voies… ».
- AVANT : « l’information neuve franchit la frontière du cadre parce qu’elle n’en a pas été calculée. »
- APRÈS : « l’information neuve franchit la frontière du cadre parce qu’elle n’a pas été calculée à partir de lui. »
- Constat : Opus B12 (vérifié).
- Justification : « calculée du cadre » n’est pas idiomatique ; même sens.

**E9.** Même section, règle de prudence.
- AVANT : « éclairée par quelque intuition de ce que l’on peut y apprendre, et de recourir à des comparateurs extérieurs avant d’agir dès que la réponse du monde coûterait trop cher ou ne pourrait être effacée. »
- APRÈS : « éclairée par quelque intuition de ce que l’on peut y apprendre. À l’inverse, dès que la réponse du monde coûterait trop cher ou ne pourrait être effacée, il convient de recourir à des comparateurs extérieurs avant d’agir. »
- Constats : Sonnet C14 ; Opus C16.
- Justification : phrase de six lignes à deux branches parallèles, coupée en deux selon la proposition d’Opus. « Il convient » est repris de la première branche. Fond inchangé.

---

## `chapitres/08-independance-chaines.md`

**E1.** § Boîte à outils (`sec:ch08-serie-parallele`), montage en série.
- AVANT : « À mesure que le nombre $N$ d’étapes s’allonge, »
- APRÈS : « À mesure que le nombre $N$ d’étapes augmente, »
- Constat : Opus C1 (vérifié).
- Justification : un nombre ne s’allonge pas.

**E2.** Même section, paragraphe sur le mode commun.
- AVANT : « la fiabilité de l’ensemble ne descendra jamais au-dessous du risque porté par la cause partagée. »
- APRÈS : « la probabilité d’échec de l’ensemble ne descendra jamais au-dessous du risque porté par la cause partagée. »
- Constats : Sonnet B2 ; Opus A2.
- Justification : la phrase comparait une fiabilité à un risque, ce qui en inverse le sens. L’encadré qui suit dit bien que la probabilité d’échec « ne descend jamais au-dessous de $q$ ».

**E3.** Encadré `.outils` « Fiabilité en série, en parallèle et défaillances corrélées », puce « Système en série ».
- AVANT : « Lorsque toutes les étapes ont une même petite probabilité d’échec $p$, soit $1 - (1 - p)^N \approx Np$ au premier ordre »
- APRÈS : « Lorsque toutes les étapes ont une même petite probabilité d’échec $p$, on a $1 - (1 - p)^N \approx Np$ au premier ordre »
- Constats : Sonnet C2 ; Opus C3.
- Justification : la phrase n’avait pas de verbe principal ; la formule n’est pas modifiée.

**E4.** § Les angles morts d’un composant (`sec:ch08-angles-morts`), dernier paragraphe.
- AVANT : « Deux conséquences suivent immédiatement de la @def:angle-mort. »
- APRÈS : « Deux remarques complètent la @def:angle-mort. »
- Constats : Sonnet C3 ; Opus C4.
- Justification : le second point (l’angle mort de la comparaison) ne découle pas de la définition ; le connecteur était trompeur. Renvoi conservé.

**E5.** Même paragraphe.
- AVANT : « (introduit dans le modèle formel de la @sec:ch08-chaines-controles) »
- APRÈS : « (repris dans le modèle formel de la @sec:ch08-chaines-controles) »
- Constat : Opus C4, seconde partie (vérifié).
- Justification : la notation $B_{\text{cmp}}$ est posée ici même (« nous noterons ») ; le modèle M1 la reprend.

**E6.** § L’indépendance est relative (`sec:ch08-independance`), la copie exacte.
- AVANT : « et ne contrôlent rien l’une chez l’autre (à peine une panne matérielle fugitive). »
- APRÈS : « et ne contrôlent rien l’une chez l’autre (tout au plus une panne matérielle fugitive). »
- Constat : Opus B9 (vérifié).
- Justification : le sens voulu est « tout au plus » ; « à peine » se lit « presque pas ».

**E7.** Même section, après la liste sur la ferrure.
- AVANT : « Ce dernier point illustre d’ailleurs une subtilité capitale de la @prop:independance : »
- APRÈS : « Ce dernier point appelle d’ailleurs une précision capitale sur la @prop:independance : »
- Constats : Sonnet B5 ; Opus B6.
- Justification : le dernier point (un essai en brouillard salin, la question d’un chimiste) illustre la tendance et non l’exception, qui n’arrive qu’avec l’encadré suivant. Le connecteur trompeur est remplacé, sans l’affirmation qu’Opus proposait d’ajouter.

**E8.** Même section, paragraphe de Levins.
- AVANT : « Deux traditions très éloignées, le génie logiciel critique et l’écologie théorique, »
- APRÈS : « Deux traditions très éloignées, le génie des logiciels critiques et l’écologie théorique, »
- Constat : Opus B8 (vérifié).
- Justification : calque de *safety-critical software engineering*, qui se lisait « un génie logiciel qui critique ». « Logiciels critiques » est l’usage français. La glose proposée par Opus n’a pas été ajoutée.

**E9.** Même paragraphe.
- AVANT : « Richard Levins formulait l’espoir de la multiplicité des modèles »
- APRÈS : « Richard Levins formulait l’espoir placé dans la multiplicité des modèles »
- Constats : Sonnet C4 (dernière partie) ; Opus C9 (première partie).
- Justification : complément du nom elliptique ; même sens. La formule « *que pourvu que* » est conservée, car c’est l’expression du livre.

**E10.** Encadré `.nuance` « Deux précisions sur l’angle mort du contrôle croisé », 1er paragraphe.
- AVANT : « ne nuit qu’aux erreurs que le producteur n’a pas su éviter ni retenir lui-même »
- APRÈS : « ne nuit qu’aux erreurs que le producteur n’a pas su éviter ni repérer lui-même »
- Constats : Sonnet C9 ; Opus B13.
- Justification : « retenir » se lisait « garder, mémoriser » ; les deux lecteurs y lisent « intercepter, repérer ». C’est le mot de Sonnet, le plus naturel pour une erreur propre.

**E11.** Même encadré, 2e paragraphe.
- AVANT : « mais le modèle ne *dérive* aucun optimum. »
- APRÈS : « mais le modèle n’*établit* aucun optimum. »
- Constat : Sonnet B7 (vérifié).
- Justification : calque de *derive*. L’opposition en italique avec « *suggère* » est conservée.

**E12.** Encadré `.cas` « Les nombres nus de Mars Climate Orbiter », 2e paragraphe.
- AVANT : « n’avaient les moyens de repérer automatiquement l’incompatibilité des grandeurs. »
- APRÈS : « n’avaient les moyens de repérer automatiquement l’incompatibilité des unités. »
- Constat : Opus C17, première partie (vérifié).
- Justification : la grandeur (une impulsion) est la même ; ce sont les unités qui diffèrent, comme le dit tout l’encadré.

**E13.** § Le blanchiment aux interfaces, avant la liste des deux « cousins ».
- AVANT : « Deux cousins proches du blanchiment des hypothèses produisent des effets symétriques aux interfaces et méritent d’être distingués avec netteté : »
- APRÈS : « Deux cousins proches du blanchiment des hypothèses produisent aux interfaces des effets analogues et méritent d’être distingués avec netteté : »
- Constats : Opus B2 ; Sonnet B15 (« effets symétriques » opaque).
- Justification : rien n’est symétrique dans ce qui suit, et les deux phénomènes sont analogues. Le statut des « cousins » (blanchiment ou phénomènes distincts) est laissé à l’auteur.

---

## `chapitres/09-severite-echappement.md`

**E1.** § Sévérité d’un contrôle (`sec:ch09-severite`), 1er paragraphe.
- AVANT : « nous avons remarqué qu’un tel accord ne prouve rien tant que le contrôleur n’avait pas réellement la possibilité de contredire une affirmation fausse. »
- APRÈS : « nous avons remarqué qu’un tel accord ne prouve rien si le contrôleur n’avait pas réellement la possibilité de contredire une affirmation fausse. »
- Constats : Sonnet C5 ; Opus C4.
- Justification : concordance des temps bancale (« tant que … n’avait pas »). La reformulation d’Opus garde l’imparfait, cohérent avec le ch. 6 (« à moins que le comparateur n’ait eu »).

**E2.** Même section, 2e paragraphe.
- AVANT : « (aucune alerte n’est émise). »
- APRÈS : « (aucune alerte n’est émise ; l’événement contraire, $\bar{A}$, est l’émission d’une alerte). »
- Constat : Sonnet C4 (vérifié).
- Justification : $\bar{A}$ est employé plus loin ($s = \Pr(\bar{A} \mid E)$) sans avoir été défini ; c’est une courte glose de notation.

**E3.** Même phrase.
- AVANT : « observer cet accord multiplie la cote que l’affirmation soit juste par le rapport de vraisemblance de l’accord : »
- APRÈS : « observer cet accord multiplie la cote de justesse de l’affirmation par le rapport de vraisemblance de l’accord : »
- Constat : Opus C5 (vérifié).
- Justification : calque de *the odds that*. « Cote de justesse » est l’expression que le chapitre emploie deux paragraphes plus loin.

**E4.** Même section, paragraphe qui relie la sévérité à $s$ et $f$.
- AVANT : « il vaut encore $1$ si le contrôleur répond sans discernement, avec autant de fausses alertes que de vraies détections ($s = f$). »
- APRÈS : « il vaut encore $1$ si le contrôleur répond sans discernement, en alertant aussi souvent sur une affirmation juste que sur une affirmation fausse ($s = f$). »
- Constat : Opus A2 (vérifié).
- Justification : $s = f$ est une égalité de taux, non de nombres, et le chapitre montre justement que les nombres diffèrent selon le taux de base. La glose est alignée sur la formule entre parenthèses, qui fixe le sens.

**E5.** § Le piège des fausses alertes (`sec:ch09-fausses-alertes`), après le tableau.
- AVANT : « Ce renversement crée un piège contre-intuitif »
- APRÈS : « Ce renversement (le désaccord accuse le plus souvent le relecteur, non le producteur) crée un piège contre-intuitif »
- Constats : Sonnet B3 ; Opus C8.
- Justification : référent flou. La parenthèse d’Opus reprend la conclusion du paragraphe précédent (« Plus de neuf fois sur dix, le désaccord vient d’une fausse alerte du relecteur, et non d’une faute du producteur ») et garde le mot de l’auteur.

**E6.** § Ce que l’on fait des alertes (`sec:ch09-comportement-alertes`), 1re phrase.
- AVANT : « Devant une alerte dont on sait que neuf fois sur dix elle est fausse, »
- APRÈS : « Devant une alerte dont on sait qu’elle est fausse neuf fois sur dix, »
- Constats : Sonnet C8 ; Opus C10.
- Justification : reprise pronominale pléonastique ; les mots ne changent pas, seul leur ordre change.

**E7.** Même phrase.
- AVANT : « tout rejeter dès que le contrôleur proteste »
- APRÈS : « rejeter le travail du producteur dès que le contrôleur proteste »
- Constat : Opus B10 (vérifié).
- Justification : « tout rejeter » pouvait se lire « rejeter les alertes », soit l’inverse du sens voulu, que l’incise suivante (« ce qui gaspille […] un travail juste ») établit.

**E8.** Même section, 3e paragraphe.
- AVANT : « — que nous noterons $u \in \left[0, 1\right]$, la proportion des alertes effectivement examinées et suivies d’effet — »
- APRÈS : « — que nous noterons $u \in \left[0, 1\right]$ et qui désigne la proportion des alertes effectivement examinées et suivies d’effet — »
- Constats : Opus C11 ; Sonnet B5 (première partie).
- Justification : deux appositions accolées ; la relative rétablit la construction. Le glissement de la « condition » du ch. 6 à une « proportion », relevé par Sonnet, est laissé à l’auteur.

**E9.** § Risque = taux d’erreur × probabilité d’échappement (`sec:ch09-risque-echappement`), 1er paragraphe.
- AVANT : « ne cause aucun tort tant qu’elle reste sur la table : »
- APRÈS : « ne cause aucun tort tant qu’elle reste sur le papier : »
- Constat : Opus C12 (vérifié).
- Justification : « sur la table » signifie plutôt « en discussion » ; le sens voulu (dans un brouillon, une note ou un calcul) est « sur le papier ».

**E10.** Même section, paragraphe qui introduit $c$ et $m$.
- AVANT : « la probabilité que le contrôleur oublie une erreur sur les autres causes ($1 - c$). »
- APRÈS : « la probabilité que le contrôleur oublie une erreur sur les autres causes (fraction $1 - c$). »
- Constat : Opus C14 (vérifié).
- Justification : la parenthèse pouvait se lire comme la valeur de $m$. Le mot « fraction » reprend l’encadré M1 (« sur la fraction complémentaire $1 - c$ »). La formule est inchangée.

**E11.** Encadré `.exemple-quantitatif`, *Mise en place*, dernière phrase.
- AVANT : « lorsque le taux d’erreur du producteur diminue sur plusieurs ordres de grandeur, face à l’absence de contrôleur. »
- APRÈS : « lorsque le taux d’erreur du producteur diminue sur plusieurs ordres de grandeur, comparés au cas sans contrôleur. »
- Constat : Opus C17 (vérifié).
- Justification : fin de phrase obscure ; la figure compare bien les courbes à la droite « sans contrôleur ». Aucun nombre touché.

**E12.** Même encadré, *Lecture*, 1re puce.
- AVANT : « la courbe bleue ($u = 1$) reste horizontale à 28,0 %, mais la courbe orange ($u = \mathrm{VPP}$) remonte vers l’échappement complet sur le panneau de gauche et rejoint visuellement, sur le panneau de droite, »
- APRÈS : « la courbe bleue ($u = 1$) reste horizontale à 28,0 % sur le panneau de gauche, mais la courbe orange ($u = \mathrm{VPP}$) remonte vers l’échappement complet sur ce même panneau et rejoint visuellement, sur le panneau de droite, »
- Constats : Opus C18 ; Sonnet C12 (seconde partie).
- Justification : la courbe bleue n’est horizontale que sur le panneau de gauche (l’échappement), non sur celui du risque. La précision de panneau est déplacée, et aucun nombre ne bouge. « Dans chacune des deux colonnes », signalé par Sonnet, est exact : le tableau généré est en colonnes.
