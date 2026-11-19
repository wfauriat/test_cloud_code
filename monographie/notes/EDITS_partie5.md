# Corrections appliquées : partie 5 (page de partie et chapitres 17 et 18)

Source : relectures « à froid » de Sonnet et d’Opus (`notes/LECTURE_FRAICHE_partie-5.md`, `notes/LECTURE_FRAICHE_Opus_partie-5.md`, `notes/LECTURE_FRAICHE_Sonnet_ch17.md`, `notes/LECTURE_FRAICHE_Opus_ch17.md`, `notes/LECTURE_FRAICHE_Sonnet_ch18.md`, `notes/LECTURE_FRAICHE_Opus_ch18.md`). Une correction n’a été appliquée que si le problème était relevé par les deux lecteurs, ou par un seul et vérifié sur le texte ; si une seule lecture du passage était plausible ; si la correction était locale et minimale ; et si le sens, la portée et la force de l’affirmation restaient identiques. Les autres constats figurent dans `notes/A_TRANCHER_partie5.md`.

Aucune étiquette, clé de citation, formule, aucun nombre, titre, bloc `:::`, statut ni renvoi n’a été modifié. Aucun terme du registre n’a été remplacé, ajouté ou mis en gras ; deux gloses (ch. 17, E5 et E6 ; ch. 18, E4) emploient en clair des termes et notations du registre dans leur sens enregistré.

## Récapitulatif

| Fichier | Corrections appliquées | dont relevées par les deux lecteurs | dont relevées par un seul lecteur et vérifiées | dont reportées par cohérence (même expression) |
| :-- | --: | --: | --: | --: |
| `parties/partie-5.md` | 5 | 1 | 4 | 0 |
| `chapitres/17-decisions-sans-appel.md` | 8 | 5 | 3 | 0 |
| `chapitres/18-remede-trois-niveaux.md` | 9 | 3 | 3 | 3 |
| **Total** | **22** | **9** | **10** | **3** |

Corrections appliquées de la même façon dans plusieurs fichiers :
- « plafonner la production **sur** leur capacité » → « **à** leur capacité » : partie 5 (E4), ch. 18, synthèse des trois niveaux (E7) et Points clés (E8).
- « mesurer […] l’échappement **par** des erreurs injectées » → « **avec** des erreurs injectées », aligné sur le titre de la @sec:ch18-org-injection (« Mesurer la probabilité d’échappement avec des erreurs injectées ») : partie 5 (E5), ch. 18, Points clés (E9). L’expression nominale « la mesure de l’échappement par erreurs injectées » (encadré `.nuance` du ch. 18), sans ambiguïté, n’a pas été touchée.

`make verifier` après corrections : 0 erreur, 1 avertissement hors périmètre (`chapitres/01-outils-logique-probabilite.md`, tableau généré absent). Les lignes du périmètre (références candidates `savage1954`, `gneiting2007`, `sutton2018`, `sec2013knight`, `kalai2025`, `lewis2020`, `ue2015tip`, `demillo1978`) sont identiques avant et après, numéros de ligne compris (aucune coupure de paragraphe).

---

## `parties/partie-5.md`

**E1.** Paragraphe consacré au chapitre 17.
- AVANT : « Le chapitre sépare ensuite ce qui se répète dans un environnement stable, que l’on peut calibrer en confrontant les probabilités annoncées aux fréquences observées, de ce qui ne se joue qu’une fois »
- APRÈS : « Le chapitre sépare ensuite ce qui se répète dans un environnement stable et que l’on peut calibrer en confrontant les probabilités annoncées aux fréquences observées, de ce qui ne se joue qu’une fois »
- Constat : Sonnet B4 (vérifié sur le texte).
- Justification : la relative « que l’on peut calibrer » se rattachait d’abord à « environnement stable ». La coordination par « et » la rattache à « ce qui se répète », seul sens possible (on calibre des décisions répétées, cf. @sec:ch17-calibrer-verrouiller). Aucun mot de fond changé.

**E2.** Même paragraphe.
- AVANT : « Il propose enfin quatre questions qui permettent à quiconque reçoit un chiffre assuré »
- APRÈS : « Le chapitre propose enfin quatre questions qui permettent à quiconque reçoit un chiffre assuré »
- Constat : Opus B5 (vérifié : « Il » suit des phrases dont les sujets sont « le décideur », « on », « un verrou »).
- Justification : pronom au référent flou ; seul le chapitre peut « proposer quatre questions » au destinataire d’un chiffre.

**E3.** Paragraphe consacré au chapitre 18.
- AVANT : « Il donne un contenu au mot d’ordre d’un « humain dans la boucle » »
- APRÈS : « Il donne un contenu au mot d’ordre « un humain dans la boucle » »
- Constat : Opus C18 (vérifié).
- Justification : « le mot d’ordre d’un humain… » pouvait se lire « le mot d’ordre que lance un humain ». L’apposition directe nomme le mot d’ordre lui-même ; les mots cités sont conservés. (La remarque de Sonnet C2 sur « donner un contenu à » est rejetée : voir A_TRANCHER.)

**E4.** Même paragraphe.
- AVANT : « nommer les contrôleurs et plafonner la production sur leur capacité »
- APRÈS : « nommer les contrôleurs et plafonner la production à leur capacité »
- Constats : Sonnet B6 ; Opus B11.
- Justification : « plafonner sur » n’est pas idiomatique ; on plafonne une grandeur « à » une valeur. Même sens. Correction reportée au ch. 18 (E7, E8).

**E5.** Même paragraphe.
- AVANT : « et mesurer la probabilité d’échappement par des erreurs injectées »
- APRÈS : « et mesurer la probabilité d’échappement avec des erreurs injectées »
- Constat : Opus B13 (vérifié : « échappement par des erreurs » se lit d’abord comme un échappement causé par les erreurs injectées).
- Justification : la préposition reprend celle du titre de la @sec:ch18-org-injection. La glose de « probabilité d’échappement » proposée par les lecteurs n’est pas appliquée (terme du registre, ch. 6). Correction reportée au ch. 18 (E9).

---

## `chapitres/17-decisions-sans-appel.md`

**E1.** § La course à la voile revisitée (`sec:ch17-course-revisitee`), 3e paragraphe.
- AVANT : « mais qu’elle soit cachée sous le manchon d’étambrai, que M. Y n’a ni démonté ni songé à soupçonner. »
- APRÈS : « mais qu’elle soit cachée sous le manchon d’étambrai (la pièce qui entoure le mât à son passage dans le pont), que M. Y n’a ni démonté ni songé à soupçonner. »
- Constats : Sonnet B2 ; Opus C3 (première partie).
- Justification : courte glose d’un terme de marine rare (l’étambrai est l’ouverture du pont par où passe le mât). Le terme est conservé ; la glose de Sonnet a été retenue dans son principe, celle d’Opus (« pied du mât ») étant inexacte. La remarque d’Opus sur « la fiche technique » est rejetée.

**E2.** Même section, liste des quatre issues, item 3.
- AVANT : « Lorsque $p \ge p^\ast$ dès le départ, comme pour M. X, on parlera simplement de *renoncement justifié*. »
- APRÈS : « Lorsque $p \ge p^\ast$ dès l’origine, comme pour M. X, on parlera simplement de *renoncement justifié*. »
- Constat : Opus C6 (vérifié).
- Justification : dans un passage sur une course dont les issues s’appellent « départ justifié », « dès le départ » se confond avec le départ de la course. « Dès l’origine » est la formule du bloc formel M2 pour le même cas ; le sens (avant toute marge) est inchangé. La question de fond sur le nombre d’issues (Sonnet B4, Opus B4) est laissée à l’auteur.

**E3.** Encadré `.exemple-quantitatif`, légende de la @fig:ch17-decisions.
- AVANT : « Les droites d’équation $1$ séparent les quatre quadrants »
- APRÈS : « Les droites où chacun de ces rapports vaut $1$ séparent les quatre quadrants »
- Constats : Sonnet C4 ; Opus C8.
- Justification : « équation $1$ » ne désigne pas une droite. La phrase précédente de la légende nomme les deux rapports portés en abscisse et en ordonnée ; la nouvelle formulation renvoie à eux sans ajouter de formule. Le nombre $1$ est inchangé.

**E4.** Phrase de transition après l’encadré `.exemple-quantitatif`.
- AVANT : « Le tableau ravive une tentation que le @sec:ch04 avait déjà écartée »
- APRÈS : « Cet exemple ravive une tentation que le @sec:ch04 avait déjà écartée »
- Constats : Sonnet B6 ; Opus C11.
- Justification : l’encadré compte deux tableaux et une figure ; « le tableau » ne désignait aucun d’eux sans ambiguïté. Les deux lecteurs proposent « Cet exemple », qui couvre l’ensemble sans ajouter de renvoi.

**E5.** Encadré `.nuance` « Pourquoi le risque omis ne peut pas entrer dans la règle de décision », 2e paragraphe.
- AVANT : « ferait de l’incertitude ontologique du @sec:ch05 une troisième quantité mesurable. »
- APRÈS : « ferait de l’incertitude ontologique du @sec:ch05 une troisième quantité mesurable, à côté des incertitudes aléatoire et épistémique. »
- Constats : Sonnet B8 (premier tiret) ; Opus B6.
- Justification : « troisième » supposait deux quantités non nommées. Ce sont les deux termes de la loi de la variance totale du @sec:ch05 (incertitudes aléatoire et épistémique, termes du registre employés en clair) ; la phrase précédente de l’encadré invoque précisément cette décomposition. Aucune affirmation nouvelle.

**E6.** Même paragraphe, dernière phrase.
- AVANT : « il figurerait déjà dans $p$ et dans $\Theta$. »
- APRÈS : « il figurerait déjà dans $p$ et dans l’ensemble des alternatives admises $\Theta$. »
- Constats : Sonnet B8 (deuxième tiret) ; Opus B7.
- Justification : $\Theta$ n’apparaît nulle part ailleurs dans le chapitre. Le registre et le @sec:ch05 le définissent comme l’ensemble des alternatives admises, terme employé deux lignes plus haut dans le même encadré et accolé à $\Theta$ au ch. 18. Les gloses proposées par les lecteurs (« paramètres du cadre », « espace des paramètres ») n’ont pas été retenues : elles s’écartent du registre.

**E7.** § Bacs à sable et verrous (`sec:ch17-bacs-a-sable-verrous`), avant la liste des deux limites.
- AVANT : « sous la forme d’environnements cloisonnés et de séparation des privilèges. Elle a deux limites : »
- APRÈS : « sous la forme d’environnements cloisonnés et de séparation des privilèges. Cette architecture a deux limites : »
- Constat : Sonnet C8 (seconde partie ; vérifié : l’antécédent féminin le plus proche est « la séparation des privilèges »).
- Justification : les deux limites portent sur le bac à sable et sur les verrous, donc sur l’architecture à deux zones ; seule lecture plausible.

**E8.** § Recevoir un chiffre assuré (`sec:ch17-quatre-questions`), paragraphe « Lorsque le chiffre ou la recommandation sort d’un système automatisé ».
- AVANT : « Souvent, il n’existe pas non plus d’expert unique qui aurait arrêté le cadre, réparti qu’il est entre les données d’entraînement, l’orientation du modèle, les consignes et l’assemblage logiciel »
- APRÈS : « Souvent, il n’existe pas non plus d’expert unique qui aurait arrêté le cadre : celui-ci est réparti entre les données d’entraînement, l’orientation du modèle, les consignes et l’assemblage logiciel »
- Constat : Opus C18 (première partie ; vérifié : trois « il » se succèdent, un impersonnel, et « réparti qu’il est » pouvait se rattacher à « expert »).
- Justification : référent précisé ; les deux-points gardent le lien explicatif (pas d’expert unique parce que le cadre est réparti). « L’orientation du modèle » est conservée (terme du registre, « orienter (un modèle) »).

---

## `chapitres/18-remede-trois-niveaux.md`

**E1.** Chapeau.
- AVANT : « Le @sec:ch17 a montré comment trancher une décision unique quand la représentation peut omettre l’essentiel. »
- APRÈS : « Le @sec:ch17 a montré comment prendre une décision unique quand la représentation peut omettre l’essentiel. »
- Constat : Opus C2 (vérifié).
- Justification : « trancher » se construit avec une question, un débat, un différend, non avec une décision ; « prendre une décision » est la collocation de même sens (le registre définit d’ailleurs la décision unique comme une décision « prise une seule fois »).

**E2.** § Se donner une attente (`sec:ch18-attente-prealable`), 1er paragraphe.
- AVANT : « La première pratique prolonge la discipline dégagée à la @sec:ch15-bainbridge-consigne, se forger un avis avant de consulter le modèle. »
- APRÈS : « La première pratique prolonge la discipline dégagée à la @sec:ch15-bainbridge-consigne : se forger un avis avant de consulter le modèle. »
- Constat : Opus C5 (première partie ; vérifié).
- Justification : l’apposition d’un infinitif après un renvoi, séparée par une virgule, se lisait comme le début d’une énumération. Les deux-points introduisent le contenu de la discipline. Ponctuation seule ; le renvoi est inchangé.

**E3.** § Élargir à dessein l’ensemble des mondes possibles (`sec:ch18-elargir-mondes`), fin du paragraphe.
- AVANT : « la prudence prend la forme d’une marge $b$ ajoutée au risque estimé, qui relève du jugement et non d’une mesure de $z$. »
- APRÈS : « la prudence prend la forme d’une marge $b$ ajoutée au risque estimé ; cette marge relève du jugement et non d’une mesure du facteur omis $z$. »
- Constat : Sonnet B2 (relatif « qui » ; vérifié : il pouvait se rattacher à « risque estimé »).
- Justification : c’est la marge qui relève du jugement (registre : « elle relève du jugement, non de la mesure »). Le relatif est remplacé par une reprise nominale. Voir E4 pour la fin de la phrase.

**E4.** Même phrase.
- AVANT : « non d’une mesure de $z$ »
- APRÈS : « non d’une mesure du facteur omis $z$ »
- Constats : Sonnet B2 ; Opus B8.
- Justification : $z$ n’est pas présenté dans le chapitre. « Facteur omis » est la notation du registre (« $z$ : facteur omis, hors du cadre ») et l’expression du @sec:ch17 (« un facteur omis $z$ »). Les gloses des lecteurs (« la grandeur qui nous échappe », « la part du risque que le modèle ne représente pas ») n’ont pas été retenues.

**E5.** § Où : aux points de passage vers l’action (`sec:ch18-placement-ou`), 1er paragraphe.
- AVANT : « Sa place est aux points de passage où une sortie cesse d’être lue comme une ébauche que l’on discute pour être tenue pour acquise : »
- APRÈS : « Sa place est aux points de passage où une sortie cesse d’être lue comme une ébauche que l’on discute, et commence à être tenue pour acquise : »
- Constats : Sonnet B11 ; Opus B12.
- Justification : « pour être tenue » se lisait comme une finale (« que l’on discute afin qu’elle soit tenue pour acquise »). La correction reprend la formule des Points clés de ce chapitre et de la page de partie (« là où une sortie commence à être tenue pour acquise ») ; la virgule rattache « commence » au sujet « une sortie ».

**E6.** § Qui (`sec:ch18-placement-qui`), 3e paragraphe (phrase en italique).
- AVANT : « il joue une mise en scène, qui peut être pire que l’absence de contrôle »
- APRÈS : « il se livre à une mise en scène, qui peut être pire que l’absence de contrôle »
- Constats : Sonnet B14 ; Opus C11.
- Justification : « jouer une mise en scène » n’est pas idiomatique ; « se livrer à une mise en scène » garde le mot de l’auteur et le sens. L’italique est conservé.

**E7.** § Comment les trois niveaux couvrent les cinq conditions (`sec:ch18-articulation`), puce du niveau 3.
- AVANT : « en plafonnant la production sur la capacité de contrôle »
- APRÈS : « en plafonnant la production à la capacité de contrôle »
- Constat : même expression que partie 5, E4 (Sonnet B6 ; Opus B11 de la page de partie).
- Justification : préposition idiomatique, appliquée partout où l’expression revient dans le périmètre.

**E8.** Points clés, 4e puce.
- AVANT : « en nommant ses contrôleurs et en plafonnant la production sur leur capacité »
- APRÈS : « en nommant ses contrôleurs et en plafonnant la production à leur capacité »
- Constat : même expression que partie 5, E4.
- Justification : idem E7.

**E9.** Points clés, 4e puce.
- AVANT : « et en mesurant l’échappement par des erreurs injectées, venues d’un autre cadre »
- APRÈS : « et en mesurant l’échappement avec des erreurs injectées, venues d’un autre cadre »
- Constat : même expression que partie 5, E5 (Opus B13 de la page de partie).
- Justification : même ambiguïté de « par » (« échappement par des erreurs »), corrigée de la même façon et alignée sur le titre de la @sec:ch18-org-injection.
