# Lecture fraîche, chapitre 6 (« Détecter une erreur : comparateurs et cinq conditions »)

Lecteur : Sonnet 5.5, première lecture, texte seul.

## 1. Ce que j'ai compris (test de lisibilité)

1. Une affirmation (calcul, prévision, mesure) ne porte pas sa justesse en elle ; on ne la contrôle qu'en la confrontant à un comparateur : une autre affirmation, un texte fixé à l'avance ou une observation du monde.
2. Un contrôle n'arrête une erreur que si cinq conditions sont réunies : un comparateur existe, il peut se tromper autrement que l'affirmation, les deux sont comparables, le désaccord arrive avant l'action, et quelqu'un l'enregistre et a l'autorité d'agir.
3. Si l'une des cinq manque pour une famille d'erreurs, la probabilité d'échappement de ces erreurs vaut 1 devant ce contrôle, quel que soit le taux d'erreur P(E). Le cas intermédiaire est renvoyé au ch. 9.
4. *Challenger* : les données ont été mal mises en forme (vols sans dommage omis, pas d'axe de température commun) et les objections des ingénieurs n'ont pas arrêté la décision. Les deux défaillances sont combinées.
5. Un désaccord prouve qu'au moins un des deux termes est faux, sans dire lequel. Un accord ne vaut que si le comparateur aurait pu contredire une affirmation fausse.

## 2. Constats classés par gravité

### Gravité A

**A1. §4 (Challenger), points « Différence » et « Comparabilité »**
Passages : « En n'affichant que les vols affectés de dommages, le graphique a sélectionné un sous-ensemble qui ne pouvait plus contredire clairement la confiance affichée » (Différence) et « L'absence des vols sans dommage [...] ôtaient le contraste indispensable » (Comparabilité).
Problème : le même fait (l'omission des vols sans dommage) sert aux deux conditions. Or, telles que le §2 les définit, la « différence » porte sur une cause d'erreur partagée par l'affirmation et le comparateur. La « comparabilité » porte sur la grandeur, les unités, les définitions et les conditions de validité. Un lecteur ne voit pas pourquoi un biais de sélection relève de l'une plutôt que de l'autre. Il peut en conclure que les définitions du §2 sont lâches, ou ne pas comprendre l'attribution. Le « graphique » est aussi traité tantôt comme le comparateur, tantôt comme le vecteur de présentation du comparateur, sans que ce statut soit dit.
Proposition minimale : ajouter une phrase de pont avant la liste, par exemple « Ici, le comparateur est l'historique des vols passés ; c'est sa mise en forme, et non les vols eux-mêmes, qui est en cause », puis, dans « Différence », « [...] le graphique ne pouvait plus se tromper autrement que la confiance affichée, puisqu'il ne contenait que des cas qui la confortaient ».
Deux lectures sont plausibles. Si l'auteur tient les deux défaillances pour distinctes, il faut dire en quoi. S'il les tient pour une seule, il faut le dire (« défaillance conjointe »). Je ne tranche pas.

### Gravité B

**B1. §1, définitions « affirmation » et « comparateur »**
Passages : « un énoncé portant sur un fait : la réponse d'un modèle, une prévision ou un rapport de mesure » et « une observation du monde ».
Problème : un « rapport de mesure » est une affirmation par la définition. Les familles 1 (une autre affirmation) et 3 (observation du monde) se recouvrent donc, par exemple quand on confronte une prévision à une mesure consignée. Le lecteur ne sait pas où ranger le cas.
Proposition : en 3, « une observation directe du monde (et non un énoncé qui en rend compte) », ou retirer « rapport de mesure » de la définition d'affirmation.
Le sens bouge selon que l'auteur veut séparer l'observation de son compte rendu (lecture 1) ou accepter le recouvrement (lecture 2).

**B2. §2, la proposition et les cinq conditions**
Passages : « Une erreur n'est détectée que lorsqu'une affirmation est confrontée à un comparateur [...], que cette comparaison fait apparaître un désaccord et que quelqu'un en prend acte » et « Dès qu'on déroule ce qu'elle exige en pratique, elle fait apparaître cinq conditions ».
Problème : la proposition énonce trois éléments. Elle ne dit ni « avant l'action », ni « autorité pour agir », ni « se tromper autrement », ni « comparable ». Le passage de trois à cinq n'est pas déroulé. Pourtant l'encadré formel dit « D'après la prop., une détection suivie d'effet exige la réunion des cinq conditions », et les points clés ajoutent « avant l'action ». Le lecteur pense que la proposition est plus riche qu'elle ne l'est, ou que quelque chose manque.
Proposition : « [...] elle se décompose en pratique en cinq conditions, dont deux (différence, comparabilité) précisent ce que « confronter » suppose, et deux (arrivée à temps, autorité) précisent ce que « prendre acte » exige ». Ou ajouter « à temps » et « avec autorité pour agir » dans l'énoncé.
Cela ne change pas l'argument. Cela change seulement ce qui est attribué à la proposition.

**B3. §2, figure des « cinq barrages » et paragraphe qui la commente**
Passages : « cinq barrages successifs entre l'affirmation et l'action » et « si un seul barrage manque ou cède [...], toute erreur de ce type traverse le contrôle ».
Problème : dans l'image habituelle, des barrages en série arrêtent ce qui passe, et il suffit qu'un seul tienne. Ici c'est l'inverse, car il faut que les cinq tiennent pour arrêter l'erreur. L'image peut être lue à contresens. Le lecteur ne sait pas non plus si c'est l'erreur ou le signal de désaccord qui doit franchir les barrages.
Proposition : remplacer « barrages » par « maillons d'une même chaîne » ou « verrous qui doivent tous tenir », dans le texte et dans la légende. Ou préciser « le signal de désaccord doit passer les cinq barrages pour atteindre la décision ».
Deux lectures sont possibles (le signal franchit les barrages, ou l'erreur les franchit). Elles ne donnent pas la même métaphore. Je ne tranche pas.

**B4. §3, définition de la probabilité d'échappement et §2**
Passage : « sans avoir été contredite à temps » ; dans l'encadré, « l'événement contraire D̄, atteindre l'action sans avoir été contredite à temps ».
Problème : D est défini comme « détectée **et prise en compte** avant l'action ». Son contraire inclut donc une erreur contredite à temps mais ignorée (cinquième condition). La formulation « contredite à temps » est plus étroite que l'événement réellement visé, et la condition 5 devient invisible dans la définition.
Proposition : « sans avoir été détectée et prise en compte à temps ».
Cela ne change pas le contenu mathématique. Cela aligne seulement le libellé.

**B5. §4, Existence « remplie » et formulation de la condition**
Passages : « La première condition était remplie » ; § 2 : « existe et soit disponible au moment du contrôle » ; encadré formel : « existe et est mobilisé ».
Problème : trois libellés pour une même condition (disponible, mobilisé, existe). Pour *Challenger*, les relevés existaient mais n'ont pas été montrés. Si « mobilisé » est le critère, la condition 1 est en partie en défaut, ce qui contredit « remplie ». Le lecteur hésite.
Proposition : harmoniser (par exemple « existe et est accessible à ceux qui contrôlent ») et, pour *Challenger*, « existait, mais n'a pas été mis sous les yeux des décideurs sous une forme exploitable ».
Cela touche à l'argument seulement si l'auteur tient « mobilisé » pour essentiel. À trancher par lui.

**B6. §4, condition « Comparabilité », dernière phrase**
Passage : « Les graphiques ne rapprochaient pas dans une forme lisible ce que les vols antérieurs montraient de la température prévue pour le lendemain. »
Problème : phrase elliptique. « ce que les vols antérieurs montraient de la température » est incompréhensible au premier passage. Le lecteur ne voit pas ce qui était à rapprocher de quoi.
Proposition : « Les graphiques ne mettaient pas en regard, sous une forme lisible, l'état des joints lors des vols antérieurs et la température annoncée pour le lendemain. »

**B7. §5, exemple de l'accord apparent**
Passage : « si un contrôle compare des nombres privés de leurs conditions de validité et accepte à peu près n'importe quel ordre de grandeur, la conformité apparente ne renseigne pas ».
Problème : deux défauts sont mêlés. L'un est la perte des conditions de validité (comparabilité). L'autre est une tolérance excessive, qui ne correspond à aucune des cinq conditions telles que définies. Le rattachement à la grille est flou.
Proposition : scinder en deux exemples et nommer la condition, ou écrire « [...] (comparabilité), ou si sa tolérance est telle qu'il aurait accepté à peu près n'importe quel résultat (le comparateur ne pouvait alors pas contredire) ».

**B8. §5, force de la conclusion sur l'accord**
Passages : « *il ne prouve rien*, à moins que le comparateur n'ait eu une véritable possibilité de contredire » ; « n'apporte un véritable appui [...] que dans la mesure où le contrôle courait réellement le risque d'échouer » ; points clés : « n'apporte aucune preuve si le comparateur n'avait aucune possibilité ».
Problème : trois niveaux (rien / appui graduel / aucune preuve si aucune possibilité). Le premier est absolu et tombe sous la condition, le second est graduel, le troisième ne vise que le cas extrême. Le lecteur ne sait pas si l'accord prouve, appuie ou rien.
Proposition : uniformiser le verbe et le seuil, par exemple « apporte un appui dans la mesure où le comparateur aurait pu contredire une affirmation fausse ».
La force exacte voulue (preuve ou appui) reste à choisir par l'auteur. Je ne tranche pas.

**B9. §3, « mondes possibles »**
Passage : « un poids de jugement accordé aux mondes possibles où l'affirmation considérée ne correspond pas aux faits ».
Problème : formule technique, renvoyée au ch. 3 (possible dépendance). Un lecteur qui n'a pas le ch. 3 en tête ne comprend pas ce que serait un « poids de jugement ».
Proposition : « un degré de confiance (jugement) dans le fait que l'affirmation soit fausse ».
Le sens ne bouge pas si le ch. 3 définit bien l'interprétation subjectiviste.

### Gravité C

**C1. §1, définitions « contrôle » et « comparateur »**
Passages : « Un contrôle est la confrontation d'une affirmation à un comparateur censé concorder » et « Un comparateur est ce à quoi l'on confronte une affirmation ».
Problème : définitions circulaires l'une par l'autre ; « censé concorder » n'apparaît que dans la première.
Proposition : définir le comparateur par ce qu'il est (« élément indépendant qu'on tient pour devoir concorder avec l'affirmation »).

**C2. §1, tripartition annoncée puis reprise en quatre**
Passage : « la détaillera en quatre sources distinctes de comparateurs ».
Problème : trois familles ici, quatre sources au ch. 13. Le passage de l'une aux autres n'est pas précisé.
Proposition : « en détaillera quatre sources, qui recoupent ces trois familles ».

**C3. §2, deux paragraphes redondants**
Passages : « Disons-le sans détour : prise isolément, la prop. est presque définitionnelle [...] » et l'encadré « Une proposition presque définitionnelle [...] ».
Problème : le même propos est dit deux fois, dans un paragraphe puis dans un encadré, presque avec les mêmes mots (« presque définitionnelle », « grille d'examen », « thèse audacieuse » / « résultat surprenant »). La dernière phrase de l'encadré, avec les trois exemples d'organisation, est seule nouvelle. L'étiquette « statut=définition » côtoie « presque définitionnelle » sans que l'écart soit expliqué.
Proposition : couper le paragraphe ou l'encadré. L'encadré peut commencer à « Sa fécondité pratique ».

**C4. §2, « Or chacune de ces cinq conditions obéit »**
Problème : « Or » suggère une opposition qui n'existe pas.
Proposition : « Chacune de ces cinq conditions obéit en outre à des mécanismes qui lui sont propres ».

**C5. §2, encadré, « Aucune expérience empirique ne saurait la démentir »**
Problème : pléonasme. Et « retard d'exécution » (liste des cinq défaillances) ne correspond pas à « arrivée à temps » : c'est le désaccord qui est en retard, pas l'exécution.
Proposition : « Aucune expérience ne saurait la démentir » ; « retard du désaccord ».

**C6. §2, « Prise en compte »**
Passages : « Les deux volets de cette définition comptent également » ; la proposition ne parle que de « prendre acte ».
Problème : « également » est ambigu (aussi, ou autant). L'autorité est ajoutée ici sans avoir été annoncée plus haut.
Proposition : « comptent autant l'un que l'autre ».

**C7. §3, « expose moins »**
Passage : « un outil sujet à des erreurs fréquentes [...] expose moins qu'un outil plus exact ».
Problème : « exposer » sans complément est elliptique.
Proposition : « expose à moins de risque ».

**C8. §3, notation de l'encadré**
Passage : « P(E) = Pr(E) ».
Problème : deux notations pour la même quantité (P et Pr), ce qui surprend dans une ligne si brève.
Proposition : en garder une.

**C9. §3, phrase sur les cas intermédiaires**
Passage : « produit parfois des désaccords injustifiés sur des affirmations exactes ».
Problème : introduit sans transition les fausses alarmes, qui ne sont pas liées à l'échappement. « Désaccords injustifiés » s'accorde mal avec le §5, selon lequel tout désaccord comparable prouve qu'un terme est faux.
Proposition : « produit parfois de fausses alertes (un désaccord causé par une erreur du comparateur) ». Ou supprimer.

**C10. §4, phrase de Tufte trop longue**
Passage : « Privées de ce groupe de comparaison et présentées sans aligner [...] que révèle au contraire l'ensemble des 23 vols antérieurs documentés [...] ».
Problème : phrase longue (environ 70 mots) à subordonnées empilées. Le « 23 » apparaît sans annonce.
Proposition : couper après « température commun », puis « Une telle mise en forme [...] ».

**C11. §4, « tranché aisément sur la foi d'un dossier mutilé »**
Problème : le dernier paragraphe est dense. « Tranché » et « mutilé » sont forts et peu clairs (qui tranche ? en quel sens ?). Les deux hypothèses sont à retourner mentalement.
Proposition : « Réduire l'épisode à l'un de ces deux versants laisserait croire soit qu'un meilleur graphique aurait suffi malgré une hiérarchie décidée à lancer, soit qu'une organisation plus attentive aurait su décider avec un dossier tronqué ».

**C12. §4, prise en compte**
Passage : « a bien été prononcé, mais il n'a pas été retenu [...] et ceux qui le portaient ne détenaient pas l'autorité finale ».
Problème : la défaillance de la condition 5 est décrite de deux façons. Les managers qui avaient l'autorité n'ont pas pris acte, et les ingénieurs n'avaient pas l'autorité. Le lecteur ne sait quelle est la cause principale.
Proposition : indiquer que les deux ont joué, ou choisir.

**C13. §5, « délivre une signature, non une preuve »**
Problème : métaphore peu claire (une signature de quoi ?).
Proposition : « délivre un simple visa, non une preuve ».

**C14. §5, ouverture**
Passage : « pour éviter une dernière confusion ».
Problème : la confusion n'est pas nommée avant la fin du paragraphe suivant.
Proposition : « pour éviter de confondre accord et preuve, et désaccord et condamnation de l'affirmation ».

**C15. Terminologie « famille / classe / sous-classe » d'erreurs**
Passages : « famille d'erreurs » (§3), « sous-classe » (encadré), « classe d'erreurs » (points clés).
Problème : trois mots pour la même notion.
Proposition : harmoniser.

**C16. §1, jargon technique**
Passages : « calcul par éléments finis », « formulaire de résistance des matériaux », « idéalisations géométriques ».
Problème : un lecteur cultivé non ingénieur ne saisit pas tout. Le sens général reste accessible par le contexte.
Proposition : une glose brève à la première occurrence (« calcul numérique de contraintes par éléments finis »). Dépendance probable vers le ch. 5 pour « éléments finis ».

**C17. Points clés, puce 4**
Passage : « a privé l'analyse de différence et de comparabilité ».
Problème : « privé l'analyse de différence » est difficile à lire (on lit « différence » comme un nom commun).
Proposition : « a fait défaillir les conditions de différence et de comparabilité ».

**C18. Définition d'« affirmation »**
Problème : « prévision » est à peine un énoncé « portant sur un fait » (le fait n'existe pas encore).
Proposition : « portant sur un fait, passé, présent ou à venir ».

## 3. Appréciation globale

Chapitre dans l'ensemble clair et bien construit : les définitions sont en général posées avant leur emploi et les exemples du quotidien aident beaucoup. Les sections les plus accessibles sont le §1 (affirmation, contrôle, comparateur et trois familles d'exemples) et le §5 (désaccord / accord, ton très net). Le §2 est bon pour les cinq conditions, avec des exemples concrets pour chacune. Les passages les moins accessibles sont l'application de *Challenger* (§4), où la correspondance entre faits et conditions est inégale (voir A1, B5, B6), et l'encadré formel du §3. Les principaux défauts de fond sont des décalages de libellé entre la proposition, les cinq conditions, la définition de l'échappement et les points clés.

Décompte : A = 1 ; B = 9 ; C = 18.
