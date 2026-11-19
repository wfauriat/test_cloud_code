# Synthèse des points à trancher (chapitres 0 à 18 et pages de partie)

Ce fichier compile les six listes `A_TRANCHER_*` (ch. 0, parties 1 à 5), produites après les relectures « à froid » (Sonnet, Opus). Chaque point a été confronté au contenu de référence (`content_spec/00_global.md`) et aux quatre sources de l'ouvrage, pour établir l'intention quand c'était possible. Aucun fichier du livre n'a été modifié.

Les sources sont du matériau interne : elles servent ici à établir ce que le texte voulait dire. Le livre ne les cite jamais, sauf l'article arXiv.

**Abréviations**
- Sources :
  - ART : l'article arXiv (`source/frame_problem_article_WF.tex`) ;
  - FD : l'essai *Failing Differently* (`source/04_failing_differently_selfcontained.md`) ;
  - ES : l'essai *Where the Guarantees End* (`source/Essay_bridge_AI_CS_final.md`) ;
  - EXP : l'exposé oral (`source/TEDLike_pitch_v2.md`) ;
  - SPEC : `content_spec/00_global.md`.
- Repères dans le livre :
  - p1… p5 : pages de partie ;
  - PC : Points clés ;
  - « ch. 5 T3 » : point T3 de la liste `A_TRANCHER` qui couvre le ch. 5.

**Les trois groupes d'action**
- **Groupe 1 : à appliquer après votre accord.** L'intention est établie par le livre lui-même (corps du texte, autre chapitre, encadré formel), par la spec ou par une source. La correction rétablit la cohérence sans changer la thèse. Je peux l'appliquer par lots, avec journal des corrections et `make verifier`.
- **Groupe 2 : arbitrage rapide.** Choix entre des options claires (terme, formulation du registre, portée), avec ma recommandation. Une fois tranché, le point passe au groupe 1.
- **Groupe 3 : à discuter avant toute modification.** Il comprend :
  - 3A : les questions de fond, qui touchent l'architecture de l'argument ;
  - 3B : les écarts notables entre le texte et ses sources ;
  - 3C : les écarts voulus avec les sources, pour mémoire.

**Marqueurs**
- ⚑ : une source tranche le point, ou s'en écarte.
- ® : touche le registre (`commun/registre_termes.md`, fichier partagé).
- ⚙ : touche un artefact généré ou `commun/parametres.py` (mainteneur).

---

## 1. Vue d'ensemble

**Volume**
- 408 points à trancher : ch. 0 : 23 ; partie 1 : 60 ; partie 2 : 109 ; partie 3 : 94 ; partie 4 : 68 ; partie 5 : 54.
- 75 points transversaux, dans les listes finales de chaque fichier. Ils se ramènent à une trentaine de familles.
- Environ 430 constats rejetés. Je les ai parcourus. Ils renforcent surtout trois familles déjà identifiées : la notation $(\dots)$, les définitions du registre et le refus des rappels de termes. Rien d'autre ne me semble à rouvrir.

**Ce qui ressort**
1. **Une dizaine de vrais contresens ou incohérences logiques.** Le livre ou ses sources disent clairement l'intention, si bien que la plupart se corrigent sans débat (§ 4.1).
2. **Des Points clés plus forts que le corps.** Le motif est systématique : les PC, et parfois les pages de partie, sont plus forts, plus courts ou décalés par rapport au corps du texte (une trentaine de cas). Règle proposée : le corps fait foi, et les PC s'alignent sur lui (§ 4.2).
3. **Une dizaine de définitions du registre sur lesquelles les lecteurs butent.** Elles se tranchent dans le registre, puis se répercutent dans les chapitres (§ 3.1).
4. **Deux décisions de politique éditoriale.** Ces deux décisions règlent à elles seules une quarantaine de points :
   - la notation $(\dots)$ se lit comme un trou en texte courant (une douzaine d'occurrences ; au ch. 15, les deux lecteurs y voient un reste de rédaction) ;
   - les éditeurs ont refusé par principe tout rappel d'un terme hors de son chapitre (environ 25 cas).
5. **Du vocabulaire flottant.** Environ 25 familles, souvent des calques : « devinette », « chiffre assuré », « code de règles », « trancher une décision »… (§ 3.2).
6. **Cinq questions de fond et trois écarts avec les sources méritent une discussion** (§ 2). La cinquième (D5) vient de la lecture de la conclusion.
7. **La conclusion n'a pas d'erreur de fond qui lui soit propre**, hormis D5. Elle reprend en revanche, souvent en les condensant, des formulations que cette synthèse propose de changer ailleurs ; ses deux relectures signalent surtout la densité de son tableau des statuts (§ 6).

### Les priorités

| Rang | Point | Où | Groupe |
| --: | :-- | :-- | :-- |
| 1 | Le texte du modèle M1 dit l'inverse de sa formule : « un désaccord n'apparaît que si […] le contrôleur […] échoue » | ch. 8 T1 | G1-1 |
| 2 | « Indépendance » et « plancher » : on ne sait pas s'il s'agit de $c$, $m$ ou $s$. Le plancher de 68 % est attribué à $c$ seul, et le scénario « indépendant » change $c$ et $m$ | ch. 8, 9, 16, p4 | D1 |
| 3 | Le ch. 0 rattache les « deux pièges » de la consigne au mauvais scénario | ch. 0 T3 | E2 |
| 4 | Le monde présenté comme « seule source » d'une pertinence nouvelle, contre les deux voies du ch. 7 | ch. 13 T1 | E1 |
| 5 | La définition de l'échappement exclut le cas *Challenger* (erreur contredite à temps, mais ignorée) | ch. 6 T1 ® | G1-4 |
| 6 | L'inversion des garanties : le confinement est attribué aux couches basses au lieu du lecteur ou du comparateur | ch. 14 T1 | G1-3 |
| 7 | « Un risque ignoré de moins de quatre points suffirait » : erreur logique | ch. 4 T1 | G1-2 |
| 8 | P1 couvre-t-elle l'incertitude aléatoire ? Tout dépend du sens de « désaccord » | ch. 5 T1 | G1-5 |
| 9 | « Composant spécifié » : est-ce le code ou la spécification qui est écrit ? Le contraste entre les ch. 10 et 11 en dépend | ch. 10 T1 ® | G1-6 |
| 10 | La marge $b$ semble devoir croître, puis décroître, avec les enjeux | ch. 17 T1 | G1-7 |
| 11 | Portée du blanchiment : conditions seules, ou aussi unités et provenance ? | ch. 8, 14, 16, p2 ® | D3 |
| 12 | Cadre et représentation : leurs définitions se recouvrent | ch. 2 T1 ® | D2 |
| 13 | Kalai : une borne inférieure présentée comme une égalité ; une citation sans source ; « indiscernable de l'intérieur » en tension avec la dispersion des tirages comme signal | ch. 12 T1 à T3, T8 | G1-9 à G1-11 |
| 14 | Points clés plus forts que le corps (une trentaine de cas) | partout | § 4.2 |
| 15 | Ce que « coûte » l'indépendance : le ch. 8 et la conclusion confondent les deux parties de P4 | ch. 8 T3, conclusion | D5 |

---

## 2. Groupe 3 : à discuter avant toute modification

### 3A. Questions de fond

**D1. Indépendance, plancher d'échappement, et les paramètres $c$, $m$, $s$** ⚙
*Où : ch. 8 T8 ; ch. 9 T1, T2, T6 ; ch. 16 T1 à T3 ; p4 ; listes transversales p2 n° 1-2, p4 n° 1. La formulation de P4 elle-même (ch. 8 T3) relève de D5.*

- **Le problème.**
  - Dans M1, $s = (1-c)(1-m)$. Quand chaque alerte est examinée, l'échappement vaut $1 - s = c + (1-c)\,m$.
  - Le livre appelle « indépendance » trois choses différentes :
    - un $c$ faible (PC du ch. 9, conformément à @prop:independance) ;
    - un $s$ élevé (ch. 9 : « indépendant (sensibilité $s$ élevée) ») ;
    - une baisse de $m$ (Lecture du ch. 9 : « l'indépendance élargit ce que le contrôleur peut voir », illustré en baissant $m$).
  - Le « plancher » vaut $c$ dans l'encadré M1 du ch. 9, mais $1 - s$ dans sa Lecture.
  - Au ch. 16, le plancher de 68,0 % est attribué à « la seule corrélation, à 60 % », alors qu'il vaut $1 - 0{,}40 \times 0{,}80$.
  - Le scénario *Indépendant et précis* baisse à la fois $c$ (de 60 % à 10 %) et $m$ (de 20 % à 10 %). Pourtant, la Lecture et l'intitulé « Seul un comparateur qui se trompe autrement abaisse le plancher » attribuent toute la baisse à $c$.
- **Spec et sources.**
  - Dans SPEC M1, $c$ est la part des causes partagées (toujours manquées) et $m$ l'oubli sur les autres causes.
  - FD définit la condition de « différence » ainsi : le comparateur peut « se tromper autrement ». La proposition 4 dit qu'un comparateur est utile « dans la mesure où la cause de ces erreurs l'affecte autrement ».
  - L'indépendance, au sens du livre, correspond donc à $c$.
  - Le flou vient de la spec elle-même : son préréglage *independent + precise* (§ 7) fait bouger $c$ et $m$ ensemble.
- **Une correction simple est possible.**
  - Quand chaque alerte est examinée, l'échappement ne dépend que de $c$ et de $m$, ni de $P(E)$ ni de $f$.
  - Le tableau généré du ch. 16 contient déjà la comparaison qui isole $c$ :
    - 68,0 % pour « Un modèle pour tous » ($c$ = 60 %, $m$ = 20 %) ;
    - 28,0 % pour « Contrôle entre pairs » ($c$ = 10 %, même $m$) ;
    - 19,0 % pour « Indépendant et précis », où $m$ passe en plus à 10 %.
- **Proposition.** Elle ne touche que le texte, aucun artefact :
  - au ch. 9, poser une fois que le plancher est $1 - s$ (l'échappement minimal quand chaque alerte est examinée), dont $c$ est la part incompressible ($1 - s \ge c$) ;
  - réserver « indépendance » à un $c$ faible et « sensibilité » à $s$, en disant que $s$ combine l'indépendance et la diligence ($1 - m$) ;
  - au ch. 16, attribuer les 68,0 % à $c$ et à $m$ ensemble ;
  - au ch. 16 encore, appuyer l'intitulé sur le passage de 68,0 % à 28,0 %, à $m$ égal. Le passage à 19,0 % est à porter au compte de la baisse de $m$.

  Variante plus lourde : redéfinir le scénario dans `parametres.py` pour qu'il ne change que $c$ (mainteneur).
- **À discuter.**
  - Accepter cette lecture de « indépendance ».
  - Garder ou renommer le scénario *Indépendant et précis*, qui change aussi $m$ (⚙).

**D2. Cadre et représentation : emboîtés ou disjoints ?** ®
*Où : ch. 2 T1 ; liste transversale p1 n° 7.*

- **Le problème.**
  - Les deux définitions du registre se recouvrent :
    - la représentation est faite de « mesures, catégories, équations, probabilités » ;
    - le cadre, de « variables, catégories, classe de modèles et objectif ».
  - Le § 3 du ch. 2 fait ensuite de la représentation « ce que l'on construit à l'intérieur de ce cadre » : ce serait une lecture disjointe.
  - Le premier point clé, lui, range la redéfinition d'une catégorie du côté du cadre.
- **Les sources ne tranchent pas.**
  - Côté emboîtement, ART parle d'une « constructed picture of what matters and how the matters connect » : le choix de ce qui compte, c'est-à-dire le cadre, ferait partie de la représentation.
  - Côté disjonction :
    - ART dit aussi « given a frame the agent had chosen », puis « Both are choices made within a frame that fixes which Xs are considered » ;
    - FD : « chosen before the inference runs, and the inference then runs inside it ».
- **Options.**
  - (a) Lecture emboîtée : la représentation est toute la construction, et le cadre en est la spécification finie. Il suffit de retoucher une phrase du § 3 du ch. 2 : « la représentation comprend le cadre et ce que l'on construit à l'intérieur de lui ».
  - (b) Lecture disjointe : retirer « catégories, équations » de la définition de la représentation, dans le registre, au ch. 2 et dans le PC 1.
- **Recommandation.** (a), plus fidèle à l'article et plus économe. Mais c'est le socle (étapes S1 et S2) de tout le livre : à confirmer.

**D3. Portée du « blanchiment »** ® ⚑
*Où : ch. 8 T2, T5, T17 ; ch. 14 T5 ; ch. 15 T12 ; ch. 16 T7 ; p2 T4 ; listes transversales p2 n° 3, p4 n° 2.*

- **Le problème.**
  - @def:blanchiment ne parle que de la perte des *conditions*.
  - Le PC du ch. 8 dit « conditions, unités ou provenance », et la page de la partie 2 « conditions, unités ou origine ».
  - *Mars Climate Orbiter* (une erreur d'unités) sert à la fois d'illustration du blanchiment et d'exemple d'un de ses « cousins ».
  - Le ch. 14 parle du « blanchiment des hypothèses et [des] deux proches cousins ».
  - Le ch. 16 présente l'effacement de la provenance comme déjà connu (un cousin), puis définit en gras le « blanchiment de provenance » comme une notion nouvelle.
- **Les sources ont un sens strict.**
  - ART : « Each interface converts a conditional output into an unconditional input, laundering a layer of uncertainty ».
  - FD : « Laundering is the dropping of a claim's conditions at a handoff ».
  - Les unités et la provenance sont des ajouts du livre : bienvenus, mais à situer.
  - SPEC distingue *laundering* (ch. 8) et *provenance laundering* (ch. 16).
- **Options.**
  - (a) Sens strict : blanchiment = conditions (hypothèses, domaine de validité). Les unités et la provenance sont des cousins, et MCO illustre un cousin.
  - (b) Sens intermédiaire : les « conditions » incluent les unités et les définitions, puisqu'un nombre ne vaut que dans son unité. La provenance reste le seul cousin ; le ch. 16 en fait le blanchiment de provenance.
  - (c) Sens large : le blanchiment couvre aussi la provenance. Il faut alors élargir le registre et supprimer les « cousins ».
- **Recommandation.** (b). Cette option :
  - garde MCO comme exemple central du ch. 8 ;
  - s'accorde avec la liste du ch. 14 (« hypothèses, unités, définitions et domaines de validité ») ;
  - laisse au ch. 16 un terme réellement distinct.

  Il faudrait ajuster une phrase de définition au ch. 8, réduire les « deux cousins » à un seul (la provenance), et aligner le PC du ch. 8 et la page de la partie 2.

**D4. *Challenger* lu à travers les cinq conditions** ⚑
*Où : ch. 6 T4 à T6 ; ch. 5 T13, T14 ; liste transversale p2 n° 16.*

- **Le problème.**
  - Au ch. 6, la sélection des vols endommagés sert à la fois la condition de « différence » et celle de « comparabilité ». On ne voit pas quelle cause commune fausse à la fois l'affirmation et le comparateur.
  - Pour l'« existence », on ne sait pas si le comparateur devait être disponible ou mobilisé.
  - La prise en compte comporte deux défaillances distinctes : les décideurs n'ont pas pris acte, et les ingénieurs n'avaient pas l'autorité. Le dernier paragraphe les fond en une seule.
- **Spec et sources.**
  - SPEC (écueil 1) : *Challenger* n'est pas un pur défaut de cadre, mais une mise en forme des données plus une prise en compte étouffée.
  - FD : la comparabilité exige que chaque terme énonce ses conditions ; au § 13, *Challenger* relève surtout d'un défaut de prise en compte.
  - ART en fait au contraire un défaut de cadre (« did not include, with sufficient salience… ») : le livre corrige ici son propre article, à dessein (voir § 3C).
- **La question.** C'est le cas vitrine des cinq conditions : chaque puce doit être inattaquable.
  - Faut-il garder la « différence » ? Le graphique, construit dans le même cadrage que l'affirmation, ne pouvait pas la contredire.
  - Ou faut-il ramener la sélection des vols à la seule comparabilité ?
- **Proposition minimale.**
  - Garder la puce « différence », avec une phrase de pont (Sonnet) : le comparateur est l'historique des vols, et c'est sa mise en forme, dans le cadrage même de l'affirmation, qui l'a privé de la possibilité de se tromper autrement.
  - Pour l'« existence », retenir que le comparateur était *disponible* (les relevés existaient), et traiter sous « comparabilité » le fait qu'il n'ait pas été montré.
  - Scinder la prise en compte en deux défaillances.

**D5. Ce que « coûte » l'indépendance (seconde partie de P4)**
*Où : ch. 8 T3 ; conclusion : ligne P4 du tableau, § « La tension entre coût et indépendance », PC 2 (Opus A1, Sonnet B2).*

- **Le problème.**
  - Au ch. 8, la @prop:independance dit que l'indépendance « tend à se payer en comparabilité — donc en coût de mise en correspondance ».
  - La conclusion parle d'une « tension entre coût et indépendance ». Elle donne pour exceptions des comparateurs bon marché dont « le prix se reporte sur la comparabilité ».
  - Opus objecte que ces exceptions confirment alors la proposition au lieu de la contredire. Le lecteur ne sait plus si l'indépendance s'oppose au coût (effort, délai) ou à la comparabilité.
  - Au ch. 8 s'ajoutent deux défauts :
    - « aider contre » est un calque ;
    - « une tension apparaît avec une autre des cinq conditions » : l'indépendance n'est pas l'une des cinq ; c'est « se tromper autrement ».
- **Spec et sources : elles séparent deux choses.**
  - SPEC P4 distingue :
    - la proposition : « what claim and comparator share, neither can check in the other; yet they must share something to be compared. Independence is therefore relative, and paid for in comparability » ;
    - l'hypothèse de travail : « the trade-off (cost tends to rise with independence) ». Sa note de robustesse précise : « Cheap and different comparators exist […]. Their cost lies in comparability: making the objection land. »
  - FD sépare de même la tension structurelle (« independence and comparability pull against each other ») et sa première conséquence (« the cost of a check rises with its independence »).
- **Proposition.** Distinguer partout, au ch. 8 et dans la conclusion :
  - (i) la partie structurelle : ce que l'affirmation et le comparateur partagent, aucun des deux ne peut le contrôler chez l'autre ; or il leur faut partager quelque chose pour être comparés. L'indépendance se paie donc en comparabilité ;
  - (ii) la tendance, qui est l'hypothèse de travail : le coût d'un contrôle (effort, délai, compétence) tend à croître avec son indépendance. Ses exceptions, bon marché à produire, reportent leur prix sur la mise en correspondance et sur la prise en compte, ce qui confirme (i) au lieu de le contredire.

  Dans le tableau de la conclusion, la ligne « suite » de P4 deviendrait : « le coût d'un contrôle tend à croître avec son indépendance » (hypothèse de travail). Point faible : « des comparateurs bon marché et décalés existent, mais leur prix se reporte sur la comparabilité et la prise en compte ». Au ch. 8 : « une tension apparaît entre cette condition, se tromper autrement, et une autre des cinq conditions, la comparabilité ».
- **À discuter :** c'est l'énoncé d'une proposition numérotée et la répartition de ses statuts.

### 3B. Écarts notables avec les sources

**E1. Le monde présenté comme « seule source » d'une pertinence nouvelle** ⚑
*Où : ch. 13 T1.*

- **Le texte.** « C'est la seule source capable, sous les conditions de la @prop:cause-commune, de démentir un cadre tout entier et de forcer l'entrée d'une pertinence nouvelle (@sec:ch07-deux-voies). »
- **L'écart.**
  - Le ch. 7 (§ « Comment une pertinence nouvelle entre dans un cadre ») donne deux voies : être averti, et découvrir par l'épreuve.
  - ART dit de même (« two routes… Either someone tells the agent… or… exploration of the world »), comme FD § 8 (« being told and finding out »).
  - Le ch. 13 renvoie au ch. 7 tout en le contredisant.
- **Ce que FD rend défendable.** Le monde est le seul comparateur qui ne soit pas lui-même une représentation, et donc le seul sans cadre propre. Être averti, c'est découvrir par procuration.
- **Proposition.** « C'est le seul comparateur qui ne soit pas lui-même une représentation, et donc le seul qui n'ait pas de cadre propre. Directement, ou par l'intermédiaire de celui qui nous avertit après l'avoir éprouvé (@sec:ch07-deux-voies), il est la source ultime de toute pertinence nouvelle. »
- **À discuter.** Garde-t-on une exclusivité pour « démentir » (un tiers peut signaler, seul le monde réfute) ?

**E2. Les « deux pièges » rattachés au mauvais scénario** ⚑
*Où : ch. 0 T3.*

- **Le texte du ch. 0.** « Et même lorsqu'un humain relit le brouillon du modèle, deux pièges referment le contrôle sur lui-même : la consigne […] transmet déjà son propre cadre à la machine, et l'entraînement des modèles à plaire […]. »
- **L'écart.**
  - Au ch. 15 comme dans FD § 9.2, les deux pièges valent quand on demande au *modèle* de contrôler le travail *humain* (« même dans ce sens », dit le ch. 15).
  - Quand l'humain relit le brouillon du modèle, le mécanisme est autre : sans avis propre, il « lit deux fois la même représentation » (ch. 15 ; FD : « one representation, read twice »).
  - D'où l'impossibilité, pour les deux lecteurs, de reconstituer le chaînon.
- **Proposition.** « Relire le brouillon d'un modèle sans s'être fait d'avis propre revient à lire deux fois la même représentation. Et lorsqu'on inverse les rôles, en demandant au modèle de contrôler son propre travail, deux pièges referment le contrôle sur lui-même : la consigne transmet au modèle le cadre de l'utilisateur, et l'entraînement à plaire le pousse à la complaisance plutôt qu'à la contradiction. »

**E3. Le texte « déjà rédigé » soumis au modèle** ⚑
*Où : ch. 15 T1, T2, T5 ; p4 T4.*

- **Le texte.** Seconde condition du contrôle croisé entre une personne et un modèle : soumettre « le problème nu » ; « ou, si elle doit lui présenter un texte déjà rédigé, elle lui demande […] de rechercher les failles […] sans jamais signaler la conclusion qu'elle privilégie ».
- **L'écart.**
  - FD : « A model consulted as a check should be given the problem, not the user's solution to it. »
  - L'exception du livre réintroduit ce que le premier piège dénonce, puisque le texte porte son cadre.
  - Les PC, eux, ne gardent que la règle.
- **Options.**
  - (a) Supprimer l'exception.
  - (b) La garder comme un pis-aller explicite : « à défaut, et au prix d'une neutralité moindre, puisque le texte transmet encore son cadre, … ».
  - (c) La garder telle quelle et l'ajouter aux PC.
- **Recommandation.** (b).
- **Au passage, dans le même passage :**
  - « Cette dynamique générale explique pourquoi » → « éclaire aussi pourquoi » : dans FD, l'ironie de Bainbridge est un parallèle, non la cause ;
  - « la conclusion pratique de ces deux pièges » → « de cette analyse » : la première condition découle du scénario du brouillon ;
  - le chapeau du ch. 15 et la page de la partie 4 annoncent une seule condition, alors qu'il y en a deux.

### 3C. Écarts voulus avec les sources (pour mémoire, aucune action)

Ces écarts sont des choix de la spec. Ils serviront à la conclusion, puisque le livre y applique sa méthode à lui-même.
- ***Challenger*.** ART en fait un défaut de cadre. Le livre le corrige (SPEC, écueil 1 ; FD § 13) : c'est une mise en forme des données plus une prise en compte étouffée.
- **Le signal d'incompétence.**
  - ES § 4 affirme : « nothing in the mechanism computes [an out-of-competence signal] ». Le livre le nuance (SPEC, écueil 8) : pour les erreurs de devinette, la dispersion des tirages en est un.
  - Le ch. 12 reproduit cette phrase entre guillemets, sans source, comme une confusion à éviter (voir G1-10).
- **Coût et indépendance.** FD énonce comme une conséquence que « the cost of a check rises with its independence ». Le livre en fait une hypothèse de travail, avec des contre-exemples bon marché (SPEC, P4).
- **L'attitude.** FD § 12 refuse d'en faire « le reste » et en fait la première source de comparateurs. Le livre suit FD contre ART.

---

## 3. Groupe 2 : arbitrages rapides

### 3.1 Formulations du registre ®

- **R1. « ne vaut que » (déduction, induction).**
  - *Où :* p1 T1, PC du ch. 1, chapeau du ch. 2, registre.
  - *Problème :* on peut lire « n'est valide que », ce qui est faux pour un logicien (le ch. 1 distingue d'ailleurs valide et solide).
  - *Recommandation :* « ne garantit sa conclusion que si… » ; dans le registre : « L'une et l'autre ne garantissent leur conclusion que « pourvu que »… ».
- **R2. « spécification finie », « cadre fini ».**
  - *Où :* ch. 2 T9, ch. 4 T9.
  - *Problème :* « finie » se lit « achevée », presque le contraire de l'idée.
  - *Recommandation :* garder « finie » et gloser une fois, au ch. 2 : « finie, c'est-à-dire bornée, et donc incomplète ».
- **R3. « décision unique ».**
  - *Où :* ch. 4 T4.
  - *Problème :* « prise une seule fois » est circulaire, et le dernier critère (la réponse du monde vient après l'acte) vaut pour toute décision.
  - *Recommandation :* « décision prise sans série d'essais comparables, si bien qu'une issue malheureuse ne peut être compensée par d'autres cas ». ⚑ ART : « The crossing happens once ».
- **R4. Sévérité.**
  - *Où :* p2 T8, ch. 9 T5, T9.
  - *Problème :* « contrôle réussi » se lit « bien exécuté » ou « passé sans alerte » ; et la sévérité est traitée tantôt comme une notion, tantôt comme une grandeur.
  - *Recommandation :*
    - registre : « Un contrôle passé sans alerte n'est probant que dans la mesure où il aurait donné l'alerte si l'affirmation avait été fausse » ;
    - au ch. 9, une phrase : « on la mesure par $\Pr(\bar A \mid E)$ ». ⚑ FD : « a check is worth the probability that it would have failed if the claim were wrong ».
- **R5. Comparateur : « un texte fixé à l'avance ».**
  - *Où :* p2 T5, ch. 6, ch. 13 T21, p3 T5.
  - *Problème :* l'expression est floue, et le ch. 13 dit « un énoncé fixé à l'avance ».
  - *Recommandation :* « un énoncé fixé à l'avance » partout. ⚑ FD : « a statement fixed in advance ».
- **R6. Vérification en amont.**
  - *Où :* ch. 10 T2, T3, PC.
  - *Problème :* « valable pour toutes ses exécutions futures » est trop fort pour des tests ou une relecture (Dijkstra).
  - *Recommandation :* « contrôle fait une fois, par rapport à la spécification, et qui porte sur le composant plutôt que sur chacune de ses sorties ». ⚑ FD : « never perfect, but it bears on the component » ; ES : Dijkstra « bounds how much certainty the front-loading buys ».
- **R7. Chaîne : « les angles morts s'additionnent ».**
  - *Où :* ch. 8 T18.
  - *Problème :* une réunion n'est pas une somme.
  - *Recommandation :* « se cumulent ».
- **R8. Erreur silencieuse : « que rien ne contredit ».**
  - *Où :* ch. 13 T8.
  - *Problème :* une erreur contredite après l'action est-elle signalée ?
  - *Recommandation :* « que rien ne contredit avant l'action », en accord avec l'échappement.
- **R9. Bac à sable, verrou.**
  - *Où :* ch. 17 T15 ; p5 T1 ; liste transversale p5 n° 7.
  - *Problème :* le bac à sable « interroge le monde » sans effet extérieur ; et une réponse « ne pourrait être effacée ».
  - *Recommandation :*
    - garder la définition. ⚑ FD : « the region where the world may be used freely as a comparator, because asking is cheap and reversible » ;
    - remplacer « ne pourrait être effacée » par « ne pourrait plus être défaite » ;
    - rappeler au ch. 17 qu'un bac à sable n'interroge que ce qu'il reproduit, sauf quand le monde visé est lui-même calculatoire (code, simulation).
- **R10. Affirmation et observation.**
  - *Où :* ch. 6 T9.
  - *Problème :* un « rapport de mesure » est une affirmation, si bien que les familles 1 et 3 de comparateurs se recouvrent.
  - *Recommandation :* préciser la famille 3 : « une observation du monde, et non le rapport qui en rend compte ».
- **R11. Prise en compte.**
  - *Où :* ch. 6 T5, T6.
  - *Problème :* la définition semble exiger une seule personne ; et $C_5$ dit « exerce l'autorité » au lieu de « ait l'autorité ».
  - *Recommandation :* « que le désaccord parvienne à quelqu'un qui ait l'autorité pour agir » ; « ait » dans $C_5$.

### 3.2 Vocabulaire transversal (un choix par famille, puis remplacement mécanique)

- **V1. Exact, précis, fiable.**
  - *Problème :* « précis » désigne un faible $f$ pour le contrôleur, mais aussi l'exactitude du producteur. « Dix fois plus précis » est faux pour la VPP, qui ne fait que quintupler. « 5 % de fausses alertes » se lit « 5 % des alertes sont fausses ».
  - *Où :* p2 T7, ch. 9 T18, ch. 16 T12 ; les noms de scénarios des tableaux générés ⚙.
  - *Proposition :*
    - « exact » pour le producteur ;
    - « précis » réservé au contrôleur qui émet peu de fausses alertes, glosé une fois ;
    - « émet dix fois moins de fausses alertes » ;
    - « une fausse alerte sur 5 % des affirmations correctes ».
- **V2. Statut.**
  - *Problème :* le mot a deux sens dans le livre : le statut d'une proposition (convention du livre) et le statut déclaré d'un résultat dans une organisation (ch. 18). S'y ajoute « appui ».
  - *Où :* ch. 0 T2, p2 T6, p5 T9, ch. 18.
  - *Proposition :* gloser chaque sens à sa première occurrence :
    - pour une proposition : « (définition, résultat sous hypothèses, hypothèse de travail ou constat empirique) » ;
    - pour un résultat : « (exploratoire ou établi, ce qui a été contrôlé de façon indépendante, sous quelles hypothèses principales) ». ⚑ FD § 11.3.
- **V3. Signature.**
  - *Problème :* image récurrente jugée obscure : « délivre une signature, non une preuve » ; « ajoute une signature, non une protection ».
  - *Où :* ch. 6, 8, 9, 16 à 18.
  - *Proposition :* garder le motif. ⚑ FD : « adds a signature and no evidence ». Gloser une fois au ch. 6 : « une signature au bas du dossier, qui engage sans rien prouver ».
- **V4. Couche.**
  - *Problème :* le mot a deux sens. Il désigne la couche de la pile logicielle, mais aussi un niveau de compétence (« comprendre une couche au-dessous »), avec cinq formules différentes.
  - *Où :* ch. 0 T5, p5 T8, ch. 17 T14, ch. 18 T10.
  - *Proposition :*
    - « couche » pour la pile ;
    - pour la compétence : « comprendre le niveau situé sous l'interface que l'on contrôle : le code sous le programme généré, la physique sous le nombre calculé ».

    ⚑ FD § 6, ES § 7. La lecture (b) du ch. 0 T5 est confirmée.
- **V5. Devinette.**
  - *Problème :* calque de *guess* ; en français, une devinette est une énigme. Le mot étiquette un régime d'erreur.
  - *Où :* ch. 12 T10, ch. 13, ch. 14, ch. 15 T10.
  - *Proposition :* « réponse au jugé », « erreur de conjecture »… (à choisir), puis remplacement partout.
- **V6. Invention.**
  - *Problème :* invention, fabrication, hallucination et confabulation désignent le même phénomène, sans que ce soit dit.
  - *Où :* ch. 11 T12, ch. 12 T11.
  - *Proposition :*
    - « invention » comme terme courant, avec « (ce qu'on appelle couramment une hallucination) » une fois au ch. 11 ;
    - « confabulation » seulement chez Farquhar ;
    - « modèle de récompense » plutôt que « modèle auxiliaire ».
- **V7. Orienter.**
  - *Problème :* orientation, alignement, ajustement par ou sur des préférences humaines alternent.
  - *Où :* ch. 12 T14, ch. 13 T16, ch. 15, ch. 16 T15.
  - *Proposition :*
    - « orienter » (registre) pour l'effet ;
    - « ajustement sur des préférences humaines » pour le moyen ;
    - « orientation » au lieu d'« alignement ».
- **V8. Consigne et requête.**
  - *Problème :* « requête » désigne parfois ce que le registre nomme « consigne ».
  - *Où :* ch. 10, ch. 11 T11, ch. 12.
  - *Proposition :* « consigne » ; « consigne système » glosée une fois ; garder « requête informatique » au ch. 12.
- **V9. Nom de la théorie.**
  - *Problème :* « théorie des contrôles », « générale du contrôle », « générale des contrôles » alternent.
  - *Où :* p3 T10, ch. 9 T16, ch. 10, ch. 13.
  - *Proposition :* « théorie des contrôles » partout ; le pluriel évite la confusion avec l'automatique.
- **V10. Classe d'erreurs.**
  - *Problème :* classe, famille, sous-classe et type désignent la même notion.
  - *Où :* ch. 6 T19, ch. 7 à 9.
  - *Proposition :* « classe d'erreurs », formulation de P4.
- **V11. Trancher une décision.**
  - *Problème :* collocation peu idiomatique.
  - *Où :* p4 T9, ch. 16 T19, avant-propos, ch. 18.
  - *Proposition :* « prendre une décision ».
- **V12. Arrêter son jugement.**
  - *Problème :* se lit « cesser de juger ».
  - *Où :* ch. 15, ch. 16 T16.
  - *Proposition :* « se former d'abord son propre jugement », « fixer d'abord sa propre estimation ».
- **V13. Usure des alertes.**
  - *Problème :* l'usage établi pour *alert fatigue* est « lassitude face aux alertes ».
  - *Où :* p4, ch. 16 (y compris un titre de bloc).
  - *Proposition :* changer partout, ou nulle part.
- **V14. Chiffre assuré.**
  - *Problème :* présenté avec assurance, ou garanti ?
  - *Où :* p5 T5, ch. 17 T21 (titre de section), ch. 18.
  - *Proposition :* « chiffre présenté avec assurance » dans le titre de section, ou une glose à la première occurrence.
- **V15. Code de règles.**
  - *Problème :* calque de *rulebook*.
  - *Où :* p5 T11, ch. 18 T15, ch. 17 T22, avant-propos.
  - *Proposition :* « recueil de règles », aligné sur l'avant-propos (« catalogue de recettes »).
- **V16. « Enchaîne, érode et corrèle ».**
  - *Problème :* « enchaîner » se lit aussi « entraver » ; « corréler » transitif est un calque probable. S'y rattachent, au ch. 0, les titres en « Elle… », qui perdent leur référent dans la table des matières, et « exécute les erreurs ».
  - *Où :* p5 T4, ch. 18 T21, ch. 0 T9, T22.
  - *Proposition :*
    - « met nos contrôles en série, les érode et rend leurs défaillances corrélées » ;
    - titres du ch. 0 avec un sujet explicite ;
    - « fait passer les erreurs à l'acte ».
- **V17. Exemples courants.**
  - *Problème :* calque de *running examples*.
  - *Où :* ch. 0 T19, avant-propos.
  - *Proposition :* « exemples récurrents ».
- **V18. « De l'intérieur ».**
  - *Problème :* l'intérieur du cadre, du modèle ou de la conversation, selon les cas.
  - *Où :* p3 T1, ch. 12 T3, ch. 13, ch. 16 T18.
  - *Proposition :* fixer le référent à chaque occurrence :
    - « de l'intérieur du cadre » à la page de la partie 3 et au ch. 13 ⚑ FD : « the row… cannot be inspected from inside » ;
    - au ch. 12, « à l'usage » ⚑ ES : « invisible from inside the interaction » ;
    - au ch. 16, « de l'intérieur de son propre cadre ».
- **V19. Arrière-plan.**
  - *Problème :* conditions tues, arrière-plan tu, conditions sous-entendues et arrière-plan non énoncé alternent.
  - *Où :* ch. 1 T13, ch. 1 à 3.
  - *Proposition :* « arrière-plan non énoncé » (registre des notations).
- **V20. Les cinq conditions.**
  - *Problème :* leurs noms varient (« différence » ou « capacité à se tromper autrement ») ; le ch. 17 n'en nomme que quatre ; le ch. 18 ne les énumère que dans une légende.
  - *Où :* ch. 6 T3, ch. 14 T21, ch. 17 T13, ch. 18 T6.
  - *Proposition :*
    - noms fixés : existence, différence, comparabilité, arrivée à temps, prise en compte. ⚑ FD § 3, SPEC P2 ;
    - énumérées à la première mention dans chaque chapitre qui les emploie.
- **V21. Comparabilité.**
  - *Problème :* lisibilité, comparaison fidèle et $B_{\text{cmp}}$ désignent la même chose ; « ruine la comparabilité » est ambigu.
  - *Où :* p4 T1, ch. 14 T9, ch. 16.
  - *Proposition :* « comparabilité » partout ; « l'angle mort de la comparaison, noté $B_{\text{cmp}}$ » glosé une fois par chapitre.
- **V22. Modèle.**
  - *Problème :* le mot désigne tantôt un modèle formel (M1 à M3), tantôt un modèle de langage, parfois dans la même phrase.
  - *Où :* p4 T8, ch. 16 T14.
  - *Proposition :* voir N3.
- **V23. Enjeux.**
  - *Problème :* « élevés », « asymétriques », « lourds » désignent le même rapport $L/\Delta U$.
  - *Où :* ch. 17 T1.
  - *Proposition :* « rapport des enjeux élevé » (voir G1-7).
- **V24. Divers, de faible portée.** « pertinence nouvelle » (ch. 7 T20) ; « la lecture comme jugement » (ch. 3 T11) ; « sous la prévision » (liste transversale p1 n° 12).

### 3.3 Notation et rappels (politique éditoriale)

- **N1. La notation $(\dots)$ en texte courant.**
  - *Où :* ch. 3, 4, 5, 7, 8, 14, 15, 17, 18 ; la lecture de ∩ au ch. 0 (T23).
  - *Proposition :* gloser à la première occurrence de chaque chapitre (« l'arrière-plan non énoncé, noté $(\dots)$ »). Quand $(\dots)$ est employé seul comme nom, écrire « l'arrière-plan $(\dots)$ ».
- **N2. Rappels de termes hors de leur chapitre.**
  - *Situation :* les éditeurs ont refusé toute glose, dans environ 25 cas : comparateur, adresse, blanchiment, M1 et M3, prêteur unique, omission de saillance, appariement…
  - *Proposition :* autoriser un rappel bref, une fois par chapitre, repris de la définition du registre et jamais reformulé, pour les termes introduits au moins deux parties plus tôt, et pour les chapitres d'entrée des parcours de lecture du ch. 0.
- **N3. Modèles M1 à M3.**
  - *Situation :* la série n'est présentée nulle part. M3 apparaît au ch. 7, avant M1 (ch. 8), et M2 n'arrive qu'au ch. 17. La conclusion emploie les trois.
  - *Options :*
    - (a) les renuméroter dans l'ordre d'apparition ;
    - (b) présenter la série au ch. 0 (§ Architecture) ou en annexe ;
    - (c) les nommer de façon descriptive (« le modèle de la cause commune »).
  - *Recommandation :* (b) ou (c).
- **N4. $P(E)$, $\Pr(E)$, $P(\text{faux})$.** ⚙
  - *Où :* ch. 6 T11, ch. 9 T11, ch. 16 T20.
  - *Problème :* trois notations pour une même quantité, et $c$ écrit tantôt en décimal, tantôt en pourcentage.
  - *Proposition :* poser l'équivalence dès la première occurrence, au ch. 6. $P(\text{faux})$ figure dans les tableaux générés.
- **N5. Ordre d'introduction.** Ces trois points passent au groupe 1 :
  - l'« omission de saillance » au ch. 7 : en faire une annonce explicite du ch. 12, ce que la spec prévoit (P3) ;
  - la prise en compte « égale à 1 » au ch. 8, avant la notation $u$ du ch. 9 : « chaque désaccord étant toujours pris en compte » ;
  - $p^\ast$ au ch. 0 : voir G1-22.

### 3.4 Contenu ou structure à trancher

- **S1. Ch. 18, niveau 3.** (T1 à T4) ⚑ FD § 11.3
  - *Problèmes :*
    - le titre annonce « indépendance, statut, historique et mesure », mais aucune pratique ne s'appelle « indépendance » ;
    - la synthèse attribue au niveau 3 « éviter de dépendre d'un prêteur unique » et « protéger l'autorité de celui qui alerte », qu'aucune sous-section ne développe ;
    - la 4e pratique est présentée comme documentée, puis comme une « proposition » ;
    - la 3e pratique du niveau 1 n'a pas de « limite », alors que le chapeau en promet une pour chaque pratique ;
    - le plafonnement de la production apparaît aux niveaux 2 et 3.
  - *Propositions :*
    - titre : « capacité indépendante, statut, historique et mesure » ;
    - rattacher l'autorité de celui qui alerte à la prise en compte ;
    - pour la 4e pratique : « s'appuie sur des méthodes pratiquées ailleurs ; sa transposition reste une proposition » (la conclusion en dépend) ;
    - je peux rédiger la limite manquante d'après FD § 11.1 (les mondes ajoutés ne débordent jamais le cadre de celui qui les imagine) et le ch. 3 (une liste encombrée noie l'attention).
- **S2. Ch. 6 : « cinq barrages placés l'un derrière l'autre ».** (T2)
  - *Problème :* la métaphore installe l'intuition inverse : des barrages en série sont redondants. Or la figure n'est pas encore générée ; seule la légende existe, ce qui rend la correction peu coûteuse.
  - *Options :*
    - « le signal de désaccord doit franchir les cinq conditions pour atteindre la décision ; qu'une seule manque, et il n'arrive pas » ;
    - « cinq conditions qui doivent toutes tenir ».

    Éviter « chaîne » et « verrou », termes du registre. Le mot « barrages » revient au ch. 18 (T6).
- **S3. Ch. 6 : de trois éléments à cinq conditions.** (T3)
  - *Problème :* le passage des trois éléments de @prop:comparateur aux cinq conditions n'est pas déroulé, et le PC ajoute « avant l'action ».
  - *Proposition :* dans l'encadré, « …et les cinq conditions qui en découlent » (SPEC P2), et aligner le PC. La proposition elle-même ne change pas.
- **S4. Ch. 7 : hypothèses du volet (b) de @prop:cause-commune.** (T2, T3)
  - *Problème :* M3 ne couvre que le volet (a), et aucune hypothèse n'est donnée pour (b), alors que les deux volets ont le statut de « résultat sous hypothèses ». « Partie » et « volet » alternent.
  - *Proposition :* une phrase qui liste les hypothèses de (b), tirée de FD :
    - les observations sont produites par le monde ;
    - $z$ a varié pendant la collecte ;
    - son effet n'est visible que sur les grandeurs enregistrées, y compris l'issue $Y$, comme une dispersion non attribuée.

    ⚑ FD : « only where it falls on something the frame records ». Écrire « volet » partout.
- **S5. Ch. 5 : 2008.** (T3, T16, T17)
  - *Problème :* le texte dit que le couplage « ne figurait pas dans la structure » ; l'encadré dit que les baisses régionales étaient « faiblement corrélées » et que cette quasi-indépendance était intégrée à la structure. Une corrélation faible relèverait de l'incertitude épistémique, non d'une omission.
  - *Source :* ⚑ ART : « did not produce that scenario at all ».
  - *Proposition :* réécrire l'encadré : la quasi-indépendance, estimée sur une période sans baisse nationale, était figée dans la structure, si bien qu'un couplage généralisé ne pouvait pas être engendré. Vérification factuelle à prévoir.
- **S6. Ch. 4 : la roulette russe.** (T2, T3 ; ch. 17 T7) ⚑ EXP, SPEC
  - *Problèmes :*
    - au § 3, le joueur est « à peu près certain que la chambre placée face au percuteur est vide » : il sait donc qu'une chambre est chargée ;
    - au § 5, sa conviction vient d'« un cadre où une chambre chargée n'avait pas sa place » ;
    - parmi les « deux cas » où la règle autorise à tirer, le premier supprime la condition qu'il devait illustrer.
  - *Sources :* EXP : « très fortement convaincu […] qu'il n'y a pas de balle dans le barillet […]. Ou alors que le prix à gagner est immense ». SPEC : la roulette du ch. 17 a $z = 1/6$ hors du cadre.
  - *Propositions :*
    - au § 3, « à peu près certain que le barillet ne contient aucune balle » ;
    - « Face à une mort possible, la règle de l'UES n'autorise à presser la détente que dans deux cas » ;
    - au ch. 17 : « la balle, logée dans l'une des six chambres, porte le risque réel à 16,7 % ».
- **S7. Ch. 0, points de construction.**
  - T11 : le niveau de technicité du jargon (typage, TCP, éléments finis, « modèles de fondation »…) est à fixer.
  - T12 : la phrase sur METR est mal rattachée. ⚑ ES la place après la frontière en dents de scie : « perception is not an instrument ».
  - T15, T16 : chaînons d'argument manquants.
  - T18 : « engager une architecture critique ».
  - T20 : *Challenger* est listé mais absent du chapitre ; les quatre questions (ch. 17) et les cinq questions (ch. 18) sont deux grilles distinctes. Proposition : « retrouvera ou découvrira ».
- **S8. Ch. 12 T5 : Vénus et Mercure.** Les lecteurs croient à une erreur. Faut-il une incise et une référence (`[@A-VERIFIER: …]`) ?
- **S9. Ch. 13, la typologie des comparateurs.**
  - T5 : les sources 1 et 4 se recouvrent (test automatisé, noyau de preuve).
  - T6 : la ferrure figure dans deux colonnes du tableau.
  - T7 : la vérification et la validation « recouvrent exactement » la matrice.
  - T9 : le « goulot » d'étranglement associé à un comparateur rapide et peu coûteux.
  - T14 : « contrôleur » employé au sens de *controller* (Simplex), en collision avec le terme du registre. Proposition : « loi de commande ».
  - T10 : à qui renvoie « vos propres contrôles » ? ⚑ FD : *the author's own checks*, c'est-à-dire ceux de la personne qui produit le résultat, avec ou sans outil. La page de la partie 3 devrait suivre.
- **S10. Ch. 7 T4 : rééchantillonnage et validation croisée.** ⚑ FD tranche :
  - un rééchantillonnage recalcule le résultat : c'est un comparateur calculé dans le cadre ;
  - les données tenues en réserve et la validation croisée confrontent le résultat à des issues observées, mais recueillies à une seule époque.

  Une phrase suffit.
- **S11. Ch. 2, points locaux.**
  - T7 : le jeu d'étalonnage. Lecture standard : une partie des cas ajuste le modèle, l'autre étalonne le score.
  - T10 : le jargon de l'encadré (d-séparation, do-calcul, non-conformité).
  - T11 : « habitudes de codage d'un dossier », employé avant le cas clinique.
  - T12 : « si sa barre casse » ; dans ART, c'est un incident prévu, non un facteur omis.
  - T13 : les variables retenues « par omission ».
  - T15 : la ligne 3 du tableau, peut-être voulue.
- **S12. Ch. 8, le modèle M1.**
  - T4 : un angle mort réunit les causes manquées avec une probabilité 1 ; les erreurs locales qu'un pair rattrape en sont distinctes (SPEC M1 : $m_{ik}$).
  - T11 : le vocabulaire de l'oubli et de l'erreur locale.
  - T12 : $p \times m$ ou $p^2$ ; même point au ch. 14 T11.
  - T13 : la distribution de $B_1 \cap (B_2 \cup B_{\text{cmp}})$ n'est jamais écrite ; « angle mort de la comparaison ».
  - T14 : $B$ désigne le résultat, alors que $B_i$ désigne partout un angle mort.
  - T9 : les « relectures de pairs » sont-elles des contrôles croisés ?
- **S13. Ch. 16, points du calcul.**
  - T3 : « à corrélation égale ».
  - T4 : le lien entre la borne $P(\text{faux})$ et la conclusion.
  - T6 : la « confusion fréquente » sur la règle de Bayes n'est pas énoncée (SPEC, écueil 5).
  - T18 : le récapitulatif final.
- **S14. Critère de la probabilité nulle.** (ch. 1 T1 ; ch. 3 T2, T4 ; liste transversale p1 n° 1)
  - *Problème :* « réellement » ou « logiquement » impossible ? Et comment ce critère se concilie-t-il avec le garde-fou du raisonnement à l'envers (pas de météorite) ?
  - *Recommandation :* « logiquement » (règle de Cromwell : aucune observation ne pourra rendre plausible ce qui a reçu zéro). Préciser au ch. 3 que ne pas examiner un monde n'est pas lui donner zéro (Sonnet).
- **S15. Ch. 1, l'exemple de la sonde et le score logarithmique.**
  - T2 : l'exemple ne dit pas d'où viennent les chiffres, puis dit qu'ils « ont été mesurés ». S'agit-il de leur provenance ou de leur portée ?
  - T3 : seconde sonde, ou second passage de la même ? Le dispositif conditionne l'indépendance des deux signaux : il faut le fixer dès la mise en place.
  - T4 ® : « score logarithmique » et « surprise » ; le sens de lecture n'est pas dit.

### 3.5 Points locaux de moindre importance (choix d'auteur, une décision chacun)

La plupart de ces points relèvent de « deux lectures possibles, sans effet sur l'argument ». Pour chacun, la liste `A_TRANCHER` d'origine donne les propositions des lecteurs.
- **p1 :** T2 (« ne protège de rien »), T3 (« Encore faut-il »), T4 (« la confiance se partage »).
- **p2 :** T1 (« surtout le risque réel »), T2 (« peut être défait »).
- **p3 :** T9 (« ces composants »), T11 (« frontière irrégulière » au lieu du terme du registre), T13 (« un autre raisonneur », calque).
- **p4 :** T7 (« datés »).
- **p5 :** T7 (« une part » puis « ce facteur omis »), T10 (mondes possibles élargis, ou ensemble Θ élargi).
- **Ch. 1 :** T7 (idéalisations), T8 (« Elle »), T9 (« y »), T10 (indépendance conditionnelle), T11 (« ne… plus »), T12 (« deux lignes »).
- **Ch. 3 :** T5 (« une faiblesse constante »), T6 (« donc »), T8 (« ce rôle »), T9 (la dinde : quelles « deux limites » ?), T10 (« protéger autrement »), T13 (« poids »), T14 à T18.
- **Ch. 4 :** T5 (« une consolation »), T7 (« au cas où M. X aurait vu juste »), T8 (« pourtant »).
- **Ch. 5 :** T8 (« valeur présente de $z$ »), T9 ($X$ ou $\theta$ ?), T10, T11, T15 (« représentation » au sens courant dans un titre), T18, T19 (jargon statistique), T20 (renvoyer aux hypothèses de P1), T22 (redondances).
- **Ch. 6 :** T7 (fausses alertes et échappement), T10 (accord apparent : deux défauts mêlés), T12 (« recalculer » ou « ressaisir »), T13 (doublon avec la nuance), T15, T18 (ordre des définitions).
- **Ch. 7 :** T5 (Hume : régression ou cercle), T8 à T15, T18, T19.
- **Ch. 8 :** T10 (« circulent toujours plus vite »).
- **Ch. 9 :** T4, T7, T12 à T15, T17, T19 (la prise en compte devient une proportion $u$ sans que ce soit dit), T20.
- **Ch. 10 :** T7 (l'adresse : ⚑ ES donne « the exact point where it was contradicted » ; garder « endroit »), T8, T10, T11, T13 à T20.
- **Ch. 11 :** T3, T6, T7, T9, T14 à T16.
- **Ch. 12 :** T13, T16 (Good-Turing), T18 à T22.
- **Ch. 13 :** T15, T17, T18, T19, T20 (chapeau trop dense), T22, T23.
- **Ch. 14 :** T6, T7 (annonce des bacs à sable et des verrous), T12, T13, T15 à T19, T22.
- **Ch. 15 :** T3 (décompte des mécanismes), T6 (notation de la sévérité), T9 (« posé à neuf »), T11, T13 à T16.
- **Ch. 16 :** T8 (sens de $E$), T9 à T11, T13, T17.
- **Ch. 17 :** T8, T9, T10 (« sans appel », titre du chapitre), T12, T17 à T20.
- **Ch. 18 :** T9 (« conséquence de flux »), T11 (mondes possibles et Θ), T12, T13, T14, T16, T17, T19, T20 (« l'écoute » ; ⚑ FD, question 5 : « Who has to listen »).

---

## 4. Groupe 1 : à appliquer après votre accord

### 4.1 Contresens et incohérences de fond (priorité haute)

- **G1-1. Ch. 8 T1, modèle M1, item 2.** Récrire selon Opus : « Une erreur passe au travers du contrôle croisé lorsque sa cause échappe au producteur *et* que le contrôleur ou la comparaison échoue à la faire ressortir […] ». Le sens mathématique est inchangé.
- **G1-2. Ch. 4 T1.** « il suffirait d'un risque ignoré d'à peine quatre points de pourcentage […] ; pour le joueur […], d'un peu moins d'un centième de point ». Aucun nombre nouveau.
- **G1-3. Ch. 14 T1.** « demeurait contenue par le lecteur humain ou par le comparateur placé entre ce sommet et les couches situées au-dessous ». ⚑ ES § 7 : « a wrong answer costs the time it takes to read; a wrong action executes ».
- **G1-4. Ch. 6 T1, ch. 9, registre** ®. L'échappement devient la probabilité qu'une affirmation fausse débouche sur une action « sans qu'un désaccord ait été détecté et pris en compte à temps ». Dans l'encadré : « la probabilité de l'événement contraire $\overline{D}$ ». ⚑ FD § 3 : « passes it, arrives too late, or goes unheeded ».
- **G1-5. Ch. 5 T1, P1.**
  - Au § 1, nommer le terme épistémique sans le mot « désaccord ».
  - Après la proposition : « le mot s'entend au sens large : l'écart entre les membres de l'ensemble admis, répétitions comprises ».

  ⚑ FD (sa proposition 3 sur l'incertitude), SPEC P1.
- **G1-6. Ch. 10 T1** ®. Ajouter après la définition : « Les règles dont il s'agit sont les instructions du programme elles-mêmes ; le contrat qui les énonce peut être écrit avant l'exécution, ou seulement formulé après coup. » ⚑ FD § 9 ; ES § 5 : « The expectation may never have been written; it was always *writable*. »
- **G1-7. Ch. 17 T1.** Distinguer deux grandeurs :
  - le poids du jugement de prudence, qui croît avec les enjeux, l'irréversibilité et la fragilité du cadre (⚑ ART, maxime finale, presque mot pour mot) ;
  - la marge minimale qui suffit à renverser la décision, qui décroît quand $p^\ast$ tend vers 0.

  Formules : « *Plus le rapport des enjeux est élevé, plus la marge qui suffit à renverser la décision est mince.* » ; « Ce jugement doit être d'autant plus exigeant que… ». Et « rapport des enjeux » partout.
- **G1-8. Ch. 17 T2.** Sortir « renoncement justifié » de l'item 3 et le présenter après la liste : c'est le cas $p \ge p^\ast$ dès l'origine, celui de M. X, et c'est aussi l'étiquette du tableau généré. Aligner la légende.
- **G1-9. Ch. 12 T1, T8, Kalai.**
  - Dans le corps et le PC : « à un taux au moins de l'ordre de la proportion de singletons ».
  - « il est recommandé de s'en écarter, notamment par l'abstention », au lieu de « doit être abandonnée ».

  ⚑ ES § 6 : « bounded below by roughly » ; « calibration can be deliberately broken ».
- **G1-10. Ch. 12 T2.** Retirer les guillemets de la phrase présentée comme une citation, qui ne figure nulle part dans le chapitre. Elle vient d'une source interne (ES § 4) : risque de provenance. Renvoyer au passage « aucune alarme ».
- **G1-11. Ch. 12 T3.** « *L'indiscernabilité à l'usage* » ; « Aucune alarme n'avertit l'utilisateur » ; PC : « indiscernable, à l'usage, d'une réponse juste ». Cela lève aussi la tension avec l'encadré final sur la dispersion. ⚑ ES : « indistinguishable from success at the point of use ».
- **G1-12. Ch. 13 T2, T3.**
  - « l'apport extérieur rend d'abord l'omission signalée ; c'est seulement en révisant le cadre qu'on la fait remonter ». ⚑ FD § 10.
  - PC : « le formalisme, là où il existe, déplace la colonne, jamais la ligne ».
- **G1-13. Ch. 9 T8.** « …expose à l'appariement des probabilités ». Écueil 5 de la spec : Bayes fixe la VPP, le comportement décide de la prise en compte.
- **G1-14. Ch. 9 T6.** $c$ devient « la part des erreurs du producteur dont la cause est partagée avec le contrôleur » : c'est la lecture que suppose le calcul.
- **G1-15. Ch. 0 T4.**
  - « le producteur, désormais assisté d'un modèle, […] et ceux qui le relisent consultent le même modèle » ⚑ FD § 9.3 ;
  - reprendre la tournure des PC : « se présentent avec la même aisance que ses réussites ».
- **G1-16. Ch. 0 T7.** « puisque les vraies erreurs se raréfient alors que le taux de fausses alertes du contrôleur reste le même, une part croissante… » (SPEC S9 : « a fixed checker »).
- **G1-17. Ch. 0 T6.** Aligner la condition de pression sur le ch. 2 (« à l'air libre, sous la pression atmosphérique »). L'exemple du mont Blanc fonctionne alors sans ambiguïté ⚑ EXP.
- **G1-18. Ch. 0 T13.** « la garantie préalable n'a pas été perdue… », comme le titre, les PC et SPEC S11. ES emploie indifféremment *guarantee* et *certainty*.
- **G1-19. Ch. 0 T1, p5 T3, ch. 18 PC 1.**
  - Ch. 0 : « …déborde souvent le cadre du modèle que nous consultons, même si elle ne déborde jamais le nôtre ».
  - Page de la partie 5 et PC du ch. 18 : « débordent le cadre de l'outil, jamais celui de la personne qui les forme ».

  ⚑ FD § 11.1 ; corps du ch. 18.
- **G1-20. Ch. 0 T2** (dépend de V2). « traiter la capacité d'évaluation indépendante comme une ligne budgétaire à part, et ne pas produire plus que ce qu'elle permet de vérifier » ⚑ ES § 7, FD § 11.3. Gloser « statut ».
- **G1-21. Ch. 0 T5** (dépend de V4). Des relecteurs « qui partagent l'interface avec le producteur et comprennent par eux-mêmes le niveau qui se trouve dessous ».
- **G1-22. Ch. 0 T8, T10, T14, T17 ; p5 T2 ; PC du ch. 17.**
  - « cette seconde question » ;
  - « ces thèses » ;
  - « le seuil de décision, noté $p^\ast$ (@eq:ch00-seuil) » ;
  - le lien causal : « toute action étant aussi une question posée au monde, mieux vaut la poser là où la réponse coûte peu et peut être défaite : dans un bac à sable ». ⚑ FD § 9.4.

### 4.2 Lot : Points clés et pages de partie alignés sur le corps

Dans tous ces cas, le corps du texte fait foi :
- **Ch. 3 T2 :** « que l'on ne peut raisonnablement écarter ».
- **Ch. 5 :**
  - T5 : « sans protéger contre un changement durable de ce facteur » ;
  - T6 : « élargissent ou repondèrent les alternatives, ou ménagent une marge ».
- **Ch. 6 :**
  - T3 : encadré et PC alignés sur la proposition (voir S3) ;
  - T8 : une seule force pour l'accord, sur un niveau graduel.
- **Ch. 7 T1 :** la dérive se voit dans des observations recueillies après la mise en service.
- **Ch. 8 T7 :** « augmentée des écarts que la comparaison ne sait pas exprimer ».
- **Ch. 9 T3 :** « paie lorsque les enjeux sont élevés (décision unique, perte très supérieure au coût de la contre-expertise) ».
- **Ch. 10 :**
  - T2 : « peut contrôler » ;
  - T4 : garder les cinq traits, dont « violable », mot de ES, que la glose explique ;
  - T12 : « rendent possible ».
- **Ch. 11 :**
  - T1 et p3 T4 : ce sont les consignes, l'ajustement sur des préférences et *l'optimisation des scores* aux tests de référence qui orientent le modèle. ⚑ ES § 3 range les *evaluation suites* parmi les moyens de pilotage (*steering*) ; le corps du ch. 11 dit qu'ils mesurent ;
  - T4 : « ni prévisible », à retirer ou à justifier ;
  - T5 : « prise isolément ».
- **Ch. 12 :** T1 et T3 (voir G1-9, G1-11).
- **Ch. 13 :** T3 (voir G1-12) ; T4 et page de la partie 3 : « reste liée à un apport extérieur au cadre, autre discipline ou contact avec le monde ».
- **Ch. 14 :**
  - T2 : « pèse lourd » au lieu de « domine » (42,2 %) ;
  - T3 : un facteur partagé par l'agent et ses contrôleurs.
- **Ch. 15 T8 et p4 T5 :** « la fluidité de ses sorties peut tromper jusqu'aux experts sur leur propre productivité ». ⚑ ES : « fluent output feels like progress ».
- **Ch. 16 T1 :** dépend de D1.
- **Ch. 17 :**
  - T3 : « peut protéger » ;
  - T4 : « en plus d'une marge d'humilité » ;
  - T5 : « contrôle » ou « règle », à harmoniser avec l'encadré ;
  - T6 : « le seul levier, dans ce modèle ».
- **Ch. 18 T5 :** « soutient » au lieu de « garantit ».

### 4.3 Lot : référents, renvois et précisions locales

- **Pages de partie.**
  - p2 T3 : « plus un comparateur est éloigné, plus il faut de travail pour le rendre comparable ». ⚑ FD § 6.
  - p3 :
    - T1 : « de l'intérieur du cadre » ;
    - T2 : « des erreurs d'un type nouveau » au lieu de « du type le plus délicat ». ⚑ FD § 10 : *new in kind* ;
    - T3 : « lorsqu'on l'interroge sur des faits rares dans ses données ». ⚑ FD § 10 ;
    - T5 : reprendre les intitulés des sources de comparateurs du ch. 13 ;
    - T6 : « pour peu que son respect soit vérifié mécaniquement » ;
    - T7 : « ou bien, à défaut, contrôler chaque sortie » ;
    - T8 : la cause de *Mars Climate Orbiter*, une confusion d'unités à une interface spécifiée.
  - p4 :
    - T2 : « au modèle de langage, la couche de la pile qui offre le moins de garanties ». ⚑ ES § 7 ;
    - T3 : le prêteur « de savoir et de formulation », mots du ch. 16 ;
    - T6 : « dans aucun schéma de procédure ». ⚑ FD : *process diagram*.
  - p5 :
    - T1 : « où cette réponse coûterait trop cher ou ne pourrait plus être défaite ». ⚑ FD § 9.4 ;
    - T6 : « Reste à poser ces questions au livre lui-même ».
- **Ch. 2.**
  - T2 : dans l'apologue de Dennett, la bombe est *sur* le chariot, et il s'agit de trois versions successives d'un robot.
  - T3 : PC : « au sens étroit où l'intelligence artificielle l'a posé ».
  - T4 (avec ch. 3 T3) : 5 % est le risque du voilier léger, et le choix porte sur le voilier léger ou le voilier renforcé. ⚑ EXP.
  - T5 : « et sa justification ne peut éviter le cercle ». ⚑ ART.
  - T6 : « se lit dans deux registres ». ⚑ ART : *two registers*.
- **Ch. 3.**
  - T1 (avec ch. 4 T6) : « bien calibrée ».
  - T7 : « Aucun des deux n'a raison, ni tort ». ⚑ EXP.
  - T12 : « une fois de plus ».
- **Ch. 5.**
  - T2 : « n'intervient dans aucune des alternatives de Θ ».
  - T4 : « pas, en général, ».
  - T7 : « traitement complet ».
- **Ch. 6 T14 :** « quatre sources, qui recoupent ces trois familles ».
- **Ch. 7.**
  - T6 : « ne vaut alors, par extension, que… », et annonce explicite de l'omission de saillance du ch. 12, que la spec prévoit (P3).
  - T7 : « couper mille fois le fil qui se trouve être rouge, sans rien apprendre de la couleur ». ⚑ FD § 8.
- **Ch. 8.**
  - T6 : dans la légende, « près du haut du tableau », et « (avec des exceptions : voir l'encadré) ». ⚑ FD, qui a la même non-monotonie dans son tableau.
  - T15 : « Steven Orzack et Elliott Sober » (prénoms permutés ; certain).
  - T19 : « chaque désaccord étant toujours pris en compte ».
- **Ch. 11.**
  - T2 : « et on ne les contrôle que sur des échantillons d'essai ».
  - T10 : *logit lens* : c'est une phrase à compléter, non une question. ⚑ ES § 4.
- **Ch. 12.**
  - T4 : rappeler en une phrase le volet (a) de P3.
  - T6 : « tirer 5 réponses ».
  - T7 : légende : « alerte à tort ».
  - T9 : « au moins un des tirages ».
  - T12 : « composable ». ⚑ ES : *compositional*, au sens où n'importe quel logiciel l'appelle.
- **Ch. 13.**
  - T11 : « le présent chapitre ».
  - T14 : « loi de commande » (Simplex).
- **Ch. 15.**
  - T4 : « éclaire aussi ».
  - T5 : « de cette analyse ».
  - Si l'on suit E3, adapter T1 et T2.
- **Ch. 16 T5 :** « Sous appariement, … ».
- **Ch. 18.**
  - T7, question 3 : « Les deux peuvent-ils être comparés : les conditions de l'affirmation sont-elles énoncées ? ». ⚑ FD § 11.4.
  - T18 : gloser le prêteur unique : « (le modèle commun auquel tous empruntent) ».

---

## 5. Vérifications factuelles (passe bibliographique)

- **Ch. 0 T21, *Mata v. Avianca* :** les sanctions visaient-elles les avocats, le cabinet, ou les deux ?
- **Ch. 6 T16, *Challenger* :** « la direction » désigne-t-elle la NASA ou la direction de Morton Thiokol ?
- ***Mars Climate Orbiter*.** ⚑ ES : « discrepancies it had already noticed, anomalies that went unescalated ».
  - Ch. 10 T5 : le facteur 4,45 porte sur les impulsions du fichier de petites forces, non sur la trajectoire.
  - Ch. 10 T6 et ch. 12 : des anomalies ont été vues sans être remontées. Reformuler « sans alarme décisive », par exemple en « sans qu'aucune alarme n'interrompe les opérations ».
  - Ch. 10 T9 : « bloqué avant le lancement ». Le logiciel était écrit avant le lancement, mais les fichiers fautifs ont été produits pendant le transit.
  - Ch. 8 T16 : la chaîne causale entre l'erreur d'unités et la trajectoire trop basse n'est pas dite.
- **Ch. 14 T4, Knight Capital :** un code dormant, resté sur un serveur, a été réactivé par un indicateur réutilisé. « Laissé actif » et « réactivé » sont donc vrais tous deux ; harmoniser.
- **Ch. 11 T13, ch. 12 T15, étude BCG :** environ 40 % de qualité en plus, 19 points de pourcentage de réussite en moins. Conformes à ES, à vérifier sur la source.
- **Ch. 12 T5 :** Vénus et Mercure (voir S8).
- **Ch. 2 T16 :** Shanahan, SEP. Le point T2 (Dennett) est déjà dans le § 4.3.
- **Ch. 5 :** T3 (2008, voir S5) ; T12 (« limite de l'alliage ») ; T14 (description du graphique de *Challenger*, à aligner sur le ch. 6).
- **Ch. 13 T12 :** l'autoformalisation en Lean s'entend-elle comme la traduction d'une preuve ou comme la recherche d'une preuve ?

---

## 6. La conclusion, relue à la lumière de cette synthèse

**Sources.** La conclusion (`chapitres/99-conclusion.md`) et ses deux relectures « à froid » (`LECTURE_FRAICHE_Sonnet_ch99.md`, `LECTURE_FRAICHE_Opus_ch99.md`). Ces relectures n'avaient pas été triées : il n'existe ni fichier EDITS ni fichier A_TRANCHER pour la conclusion.

**Repères.** « Opus A1 », « Sonnet B2 » renvoient à ces relectures ; « l. 25 » renvoie à une ligne du fichier.

**Bilan.** La conclusion tient le programme de la spec (`content_spec/part9_back.md`) : statuts, tensions, réfutation, comparateurs, posture. Elle n'a pas d'erreur de fond qui lui soit propre, en dehors de D5. Ses défauts sont de deux sortes :
- elle reprend, en les condensant, des formulations que cette synthèse propose de changer ailleurs (§ 6.1) ;
- son tableau des statuts est très dense, et emploie sans rappel des notations et des termes que les deux lecteurs ne retrouvent pas (§ 6.2).

### 6.1 À répercuter dans la conclusion, selon les décisions prises ailleurs

- **E1, le monde comme seule source.** À la l. 123, le monde est « le seul qui puisse contredire un cadre tout entier (@sec:ch13-le-monde) ». Il faut aligner cette phrase sur la formule retenue au ch. 13. La conclusion est d'ailleurs partagée elle-même : la l. 121 présente le domaine du lecteur comme une voie d'entrée d'une pertinence nouvelle, conformément au ch. 7.
- **D5, ce que coûte l'indépendance.** Concerne la ligne P4 du tableau (l. 22), le § « La tension entre coût et indépendance » (l. 53 à 57) et le PC 2.
- **D3, le blanchiment.** L. 24 : « Le blanchiment détruit la comparabilité aux interfaces (@def:blanchiment) ».
- **R4, la sévérité.** L. 25 : « Un contrôle réussi n'est probant que s'il aurait pu échouer ».
- **V20 et S3, les cinq conditions.** La @prop:comparateur est résumée en trois éléments (l. 18) ; le point faible invoque cinq conditions ; la dernière section les énumère avec d'autres mots (l. 142). Les deux lecteurs l'ont relevé (Opus B2, Sonnet B1). Proposition : nommer une fois les cinq conditions dans le tableau, avec leurs noms fixés.
- **G1-12, colonne et ligne.** L. 29 et l. 134 : aucun des deux lecteurs ne sait quel axe est la ligne (Opus B4, Sonnet B5). Il faut nommer les axes une fois : « la formalité change le caractère signalé ou silencieux d'une erreur (la colonne), non la place de sa cause dans ou hors du cadre (la ligne) ».
- **N3, les modèles M1 à M3.** Les trois modèles se croisent dans la conclusion (l. 49, 61, 67, 132 et la dernière ligne du tableau). Un lecteur y voit « le modèle M1 » servir à deux usages : la distance du contrôleur et les politiques d'alerte (Opus B5, C7 ; Sonnet C7).
- **V4, couche.** L. 51 : « comprenant au moins une couche au-dessous » ; l. 97 : « qu'il ne sait pas lire une couche au-dessous » (Sonnet B9).
- **V5, devinette.** L. 99.
- **V14, chiffre assuré.** L. 127 (Opus C16, Sonnet B17).
- **G1-9 et p3 T3, faits rares.** L. 28 : « la calibration générative impose d'inventer des faits rares » (Sonnet B4).
- **N1, la notation $(\dots)$.** L. 13 (Opus B1, Sonnet C1).
- **N2, les rappels.** Le tableau emploie sans rappel :
  - VPP, $p^\ast$, $B_1$, $B_2$, $B_{\text{cmp}}$, $c$, $m$, $f$ et $u$ ;
  - l'appariement des probabilités, l'adresse, orienter, la pile, l'omission structurelle.

  Voir Opus B15, C2 et Sonnet B3, B6, B11, B17. La conclusion s'adresse à qui a lu le livre, mais quelques rappels courts coûtent peu (VPP développée à sa première occurrence ; les quatre lettres glosées à la l. 132).
- **D2 et R2, cadre et représentation.** L. 13 : « une représentation construite dans un cadre fini ». La phrase convient aux deux lectures de D2 ; elle est à revoir si l'option (b) est retenue.
- **V16, les effets de l'automatisation.** L. 30 : « met les contrôles en chaîne, en retire certains et corrèle ceux qui restent ». Cette formule explicite pourrait servir de modèle pour la page de la partie 5 et le chapeau du ch. 18.

Trois points de la conclusion confirment déjà les propositions de cette synthèse :
- l. 69 : « il faut qu'un autre paramètre bouge, au premier chef la part des causes partagées $c$ ». C'est la lecture de l'indépendance proposée en D1 ;
- l. 79 : la transposition des erreurs injectées figure parmi les propositions, ce qui appuie la correction proposée pour le ch. 18 (S1) ;
- l. 45 : la lecture de *Challenger* comme pur défaut de cadre est déjà rangée parmi les lectures corrigées (§ 3C).

### 6.2 Points propres à la conclusion

**Arbitrages rapides (groupe 2)**
- **C-1. Le statut de « le monde répond à l'action ».** (l. 13, Opus B1) La seconde moitié de l'énoncé de la première ligne ne reçoit aucun statut, alors que le paragraphe précédent annonce que chaque partie reçoit le sien.
  - *Proposition :* « définition », puisque l'asymétrie découle de ce qu'est une représentation. ART parle d'« a structural observation about where the agent stands ».
- **C-2. Le rôle des constats empiriques.** (Opus A2, Sonnet B8) Trois passages ne disent pas la même chose :
  - le corps dit que l'argument « a été construit pour ne dépendre d'aucun » constat ;
  - le PC 1 dit que son poids pratique « repose » en partie sur eux ;
  - le tableau donne le statut de constat empirique à deux affirmations : le gain de portée et la frontière en dents de scie.

  *Proposition :*
  - corps : « le noyau de l'argument ne dépend d'aucun d'eux ; certaines affirmations subsidiaires en dépendent, et le tableau le signale » ;
  - PC 1 : « son poids pratique repose sur des hypothèses de travail, qu'illustrent des constats empiriques peu nombreux et datés ».
- **C-3. « Hypothèse de travail » au sens large.** (l. 138, Opus B17 ; l. 79 à 81, Opus B9)
  - *Problèmes :*
    - appliquée à tout l'échafaudage, l'expression entre en collision avec le statut défini en tête du chapitre ;
    - le tableau donne aux pratiques proposées le statut d'hypothèse de travail, alors que le § 2.6 dit qu'elles ne sont pas écrites comme des hypothèses.
  - *Proposition :*
    - « la meilleure démarche de travail », qui est le titre de la section ;
    - préciser que le statut qualifie l'appui, et le registre la forme (« Énoncés comme de simples conjectures… »).

    L'avant-propos (l. 15) dit aussi « la meilleure hypothèse de travail disponible » : à harmoniser des deux côtés.
- **C-4. « jugé sur ce qu'il énonce, et sur rien d'autre ».** (l. 134, Opus B16, Sonnet A2)
  - *Problème :* le connecteur « C'est pourquoi » enchaîne mal, et l'on ne sait pas ce que « rien d'autre » exclut.
  - *Ce que dit l'avant-propos :* il fixe le sens (l. 35) : jugé sur « la justesse de ses distinctions, la solidité de ses enchaînements et l'utilité pratique des grilles de lecture », non sur la manière dont il a été construit.
  - *Proposition :* « C'est pourquoi l'ouvrage demande, comme l'annonçait l'avant-propos, à être jugé sur ce qu'il énonce, confronté à ces comparateurs, et non sur la manière dont il a été construit. » L'avant-propos fixant l'intention, le point peut passer au groupe 1.
- **C-5. Le point faible de la ligne du ch. 11.** (Opus C5) Que des « architectures mixtes rebâtissent un contrôle mécanique autour de la tâche », est-ce une faiblesse (l'opposition entre spécifié et appris se brouille) ou une simple précision ? Choix d'auteur.
- **C-6. « dériver », « dérivation ».** (Opus C1) Calque possible de *derive* : « n'est pas dérivée », « une erreur de dérivation ». L'usage est admis en mathématiques. Si l'on change, harmoniser avec le ch. 8.
- **C-7. La liste des constats empiriques.** (l. 39) Elle omet *Challenger*, *Mata*, Knight Capital, la complaisance et l'appariement des alarmes. Ajouter « notamment », ou compléter la liste.

**À appliquer après accord (groupe 1)**
- **Tableau.**
  - Opus C2 : « valeur prédictive positive (VPP) » à la première occurrence.
  - Opus C3 : formuler le point faible de P1 comme une faiblesse.
  - Opus C4 : « Suppose une issue binaire… ».
  - Opus C7 : « pour la marge d'humilité (modèle M2) ».
  - Sonnet B4 : nommer les trois propriétés du changement de régime.
  - Opus B3, l. 19 : « la même formulation de la consigne », comme au § 2.3.
- **L. 37 et l. 99.** (Opus B6, Sonnet B7) « ne peut être prise en défaut que si la grille des cinq conditions qu'elle déplie se révèle inutile à l'usage ». Dans la liste des observations : « (ce qui ôterait à la grille son utilité sans réfuter la définition) ». Conforme à SPEC P2.
- **L. 55.** (Opus B7, Sonnet B10) Rattacher l'exemple de la corrosion à la ferrure (@sec:ch08), et supprimer la tautologie « traduire… coûte en traduction ».
- **L. 69.**
  - Opus B8 : nommer le raccourci : conclure que la seule usure des alertes suffit à rendre dangereux un producteur amélioré.
  - Sonnet B11 : remplacer « donc » par « ainsi ».
- **L. 71 et PC 2.** (Sonnet B12) « Le sens de variation du produit… », au lieu de « Le signe du produit… ». Le titre change ; l'étiquette reste la même.
- **L. 73.** (Sonnet A1, Opus C12) « Dans l'exemple illustratif du @sec:ch16, le risque […] est au contraire plus bas avec le modèle partagé… ».
- **L. 85.** (Sonnet C3) « résout » → « atténue ».
- **L. 93.** (Opus B10, Sonnet B13) « Une traversée sans incident (@sec:ch03) ne juge guère un prévisionniste ».
- **L. 97.** (Sonnet B15) « ne permettait pas de prédire la part des erreurs… ».
- **L. 99.** (Opus B11, Sonnet B14)
  - Mettre en puces les six observations.
  - Préciser l'étude de 2025 : les développeurs s'y estimaient plus rapides qu'ils ne l'étaient.
- **L. 101.** (Opus B12) « Pour que ces mesures mettent le livre à l'épreuve au lieu de reproduire son cadre ».
- **L. 107.** (Opus C15, Sonnet B19) « on la rappelle ici sans rien y ajouter ».
- **L. 111.** (Opus B13, Sonnet B19) « il ne prouve pas que la thèse soit juste, puisqu'il en partage le cadre ».
- **Titre de la l. 115.** (Sonnet B16) « D'où peuvent venir des comparateurs qui se trompent autrement ». L'étiquette reste la même.
- **L. 130.** (Opus B14) « Les observations recensées plus haut (@sec:conclusion-refutation) ».
- **L. 132.** (Opus B15, Sonnet B17) Gloser $c$, $m$, $f$ et $u$.
- **L. 140.** (Sonnet B18) « là où l'argument engage une décision unique ».
- **Dernier point clé.** (Opus A3) Couper après « ses risques nommés », car les deux-points font lire la suite comme une liste de risques.
- **Retouches de style.** Opus C8 à C11, C13, C14, C17 ; Sonnet C2, C4 à C6, C10, C11. Aucun enjeu de fond.
- **Constat écarté.** Sonnet C9 : le PC 4 (« n'en tire aucune autorité ») reprend l'avant-propos (« aucune autorité particulière ») ; le « gage réel » du corps porte sur l'article, non sur le mode d'élaboration.

### 6.3 Questions pour notre échange

1. **D5.** Acceptez-vous de distinguer la partie structurelle de P4 (l'indépendance se paie en comparabilité) et sa tendance (le coût croît avec l'indépendance), au ch. 8 comme dans la conclusion ?
2. **Le livre corrige son propre article.** Sur deux points au moins, l'ouvrage corrige l'article qu'il prolonge :
   - *Challenger* : l'article en fait un défaut de cadre ; le livre parle d'une mise en forme des données et d'une prise en compte étouffée ;
   - les défaillances lourdes : l'article les situe dans l'incertitude ontologique ; la matrice du ch. 13 les place dans la colonne silencieuse.

   La conclusion ne le dit nulle part. Ce serait pourtant l'exemple le plus concret de « la méthode appliquée à elle-même », puisque l'article est un comparateur qui partage le cadre du livre. Faut-il l'ajouter, par exemple dans « Une provenance déclarée » ? Seul l'article peut être cité ; l'origine de ces corrections ne peut pas être évoquée.
3. **Le motif des Points clés.** Dans les termes du livre, le décalage entre les PC et le corps (une trentaine de cas) est un blanchiment : les conditions tombent au passage du corps aux résumés. Une fois les corrections faites, faut-il le dire ? Le § « la tenue du texte ne prouve rien sur son fond » s'y prêterait. Ou bien est-ce une remarque à garder pour vous ?
4. **C-1 et C-3.** Quel statut donner à « le monde répond à l'action » ? Et faut-il réserver « hypothèse de travail » au statut défini en tête du chapitre, en parlant ailleurs de « démarche de travail » ?

---

## Annexe : où est passé chaque point

Repères :
- G1-n, § 4.2, § 4.3 : groupe 1 ;
- D1 à D5, E1 à E3 : groupe 3 ;
- R, V, N, S : groupe 2 (§ 3.1 à 3.4) ;
- L : § 3.5 ;
- F : § 5.

- **ch. 0 :** T1 G1-19 · T2 G1-20 · T3 E2 · T4 G1-15 · T5 G1-21 · T6 G1-17 · T7 G1-16 · T8 G1-22 · T9 V16 · T10 G1-22 · T11 S7 · T12 S7 · T13 G1-18 · T14 G1-22 · T15 S7 · T16 S7 · T17 G1-22 · T18 S7 · T19 V17 · T20 S7 · T21 F · T22 V16 · T23 N1
- **p1 :** T1 R1 · T2 à T4 L
- **ch. 1 :** T1 S14 · T2 à T4 S15 · T5 § 4.2 (« issues jugées indépendantes », comme l'encadré) · T6 V19 · T7 à T12 L · T13 V19
- **ch. 2 :** T1 D2 · T2 à T6 § 4.3 · T7, T8 S11 · T9 R2 · T10 à T15 S11 · T16 F
- **ch. 3 :** T1 § 4.3 · T2 § 4.2 · T3 § 4.3 · T4 S14 · T5, T6 L · T7 § 4.3 · T8 à T10 L · T11 V24 · T12 § 4.3 · T13 à T18 L
- **ch. 4 :** T1 G1-2 · T2, T3 S6 · T4 R3 · T5 L · T6 § 4.3 · T7, T8 L · T9 R2
- **p2 :** T1, T2 L · T3 § 4.3 · T4 D3 · T5 R5 · T6 V2 · T7 V1 · T8 R4
- **ch. 5 :** T1 G1-5 · T2 § 4.3 · T3 S5 · T4 § 4.3 · T5, T6 § 4.2 · T7 § 4.3 · T8 à T11 L · T12 F · T13, T14 D4 · T15 L · T16, T17 S5 · T18 à T20 L · T21 N1 · T22 L
- **ch. 6 :** T1 G1-4 · T2 S2 · T3 S3 · T4 à T6 D4 (T5, T6 aussi R11) · T7 L · T8 § 4.2 · T9 R10 · T10 L · T11 N4 · T12, T13 L · T14 § 4.3 · T15 L · T16 F · T17 V3 · T18 L · T19 V10
- **ch. 7 :** T1 § 4.2 · T2, T3 S4 · T4 S10 · T5 L · T6, T7 § 4.3 · T8 à T15 L · T16 N1 · T17 N3 · T18, T19 L · T20 V24
- **ch. 8 :** T1 G1-1 · T2 D3 · T3 D5 · T4 S12 · T5 D3 · T6 § 4.3 · T7 § 4.2 · T8 D1 · T9 S12 · T10 L · T11 à T14 S12 · T15 § 4.3 · T16 F · T17 D3 · T18 R7 · T19 § 4.3 · T20 V3
- **ch. 9 :** T1, T2 D1 · T3 § 4.2 · T4 L · T5 R4 · T6 G1-14 · T7 L · T8 G1-13 · T9 R4 · T10 N2 · T11 N4 · T12 à T15 L · T16 V9 · T17 L · T18 V1 · T19, T20 L
- **p3 :** T1 à T3 § 4.3 · T4 § 4.2 · T5 à T8 § 4.3 · T9 L · T10 V9 · T11 L · T12 N2 · T13 L
- **ch. 10 :** T1 G1-6 · T2, T3 R6 · T4 § 4.2 · T5, T6 F · T7, T8 L · T9 F · T10, T11 L · T12 § 4.2 · T13 à T20 L
- **ch. 11 :** T1 § 4.2 · T2 § 4.3 · T3 L · T4, T5 § 4.2 · T6, T7 L · T8 N2 · T9 L · T10 § 4.3 · T11 V8 · T12 V6 · T13 F · T14 à T16 L
- **ch. 12 :** T1 G1-9 · T2 G1-10 · T3 G1-11 · T4 § 4.3 · T5 S8 · T6, T7 § 4.3 · T8 G1-9 · T9 § 4.3 · T10 V5 · T11 V6 · T12 § 4.3 · T13 L · T14 V7 · T15 F · T16 L · T17 N2 · T18 à T22 L
- **ch. 13 :** T1 E1 · T2, T3 G1-12 · T4 § 4.2 · T5 à T7 S9 · T8 R8 · T9, T10 S9 · T11 § 4.3 · T12 F · T13 N2 · T14 § 4.3 · T15 L · T16 V7 · T17 à T20 L · T21 R5 · T22, T23 L
- **p4 :** T1 V21 · T2, T3 § 4.3 · T4 E3 · T5 § 4.2 · T6 § 4.3 · T7 L · T8 V22 · T9 V11
- **ch. 14 :** T1 G1-3 · T2, T3 § 4.2 · T4 F · T5 D3 · T6, T7 L · T8 N2 · T9 V21 · T10 N1 · T11 S12 · T12, T13 L · T14 N2 · T15 à T19 L · T20 N3 · T21 V20 · T22 L
- **ch. 15 :** T1, T2 E3 · T3 L · T4, T5 § 4.3 · T6 L · T7 N1 · T8 § 4.2 · T9 L · T10 V5 · T11 L · T12 D3 · T13 à T16 L
- **ch. 16 :** T1, T2 D1 · T3, T4 S13 · T5 § 4.3 · T6 S13 · T7 D3 · T8 à T11 L · T12 V1 · T13 L · T14 V22 · T15 V7 · T16 V12 · T17 L · T18 S13 · T19 V11 · T20 N4 · T21 N2
- **p5 :** T1 § 4.3 · T2 G1-22 · T3 G1-19 · T4 V16 · T5 V14 · T6 § 4.3 · T7 L · T8 V4 · T9 V2 · T10 L · T11 V15
- **ch. 17 :** T1 G1-7 · T2 G1-8 · T3 à T6 § 4.2 · T7 S6 · T8 à T10 L · T11 N2 · T12 L · T13 V20 · T14 V4 · T15 R9 · T16 N1 · T17 à T20 L · T21 V14 · T22 V15
- **ch. 18 :** T1 à T4 S1 · T5 § 4.2 · T6 V20 · T7 § 4.3 · T8 N1 · T9 L · T10 V4 · T11 à T14 L · T15 V15 · T16, T17 L · T18 § 4.3 · T19, T20 L · T21 V16, G1-19
