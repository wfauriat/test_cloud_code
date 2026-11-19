# Lecture fraîche — Chapitre 14 « Des chaînes qui agissent »

Lecteur : Opus, première lecture. Seul le fichier `chapitres/14-chaines-qui-agissent.md` a été lu.

## 1. Résumé de ce que j'ai compris (test de lisibilité)

Les systèmes d'IA découpent les tâches complexes en *pipelines* d'étapes enchaînées. Entre ces étapes, il n'y a ni contrat écrit ni temps de relecture, contrairement à l'ingénierie classique. Un agent, qui pilote lui-même cette boucle et agit par des outils, forme une chaîne longue et auto-entretenue dont les erreurs ne sont plus lues mais exécutées : l'action précède la relecture humaine (cas Knight Capital). Un calcul illustratif sur 12 étapes montre que des contrôles croisés à chaque étape éliminent l'essentiel des erreurs indépendantes, mais pas un facteur partagé, qui finit par expliquer une grande part des échecs restants. Le texte nu qui circule entre les étapes « blanchit » les conditions, les incertitudes et les provenances, ce qui détruit la comparabilité. Enfin, donner le pouvoir d'agir à la couche la moins garantie inverse la pyramide qui rendait la pile logicielle sûre. Il faut donc séparer les espaces d'exploration sans conséquence des frontières où l'acte devient irréversible.

## 2. Constats classés par gravité

### Gravité A (compréhension compromise ou contresens possible)

**A1. Section « Autorité d'exécution et garanties inversées », § 2**
Passage : « l'absence de contrat au sommet demeurait contenue par les couches situées juste au-dessous. »
Problème : la phrase précédente attribue ce confinement au lecteur humain ou au comparateur, pas aux couches basses. Le paragraphe suivant affirme d'ailleurs que ces couches exécutent fidèlement tout ordre bien formé. Le lecteur peut donc comprendre l'inverse de l'argument.
Deux lectures plausibles, que je ne tranche pas : (a) « l'absence de contrat restait cantonnée au sommet », sans déborder sur les couches inférieures ; (b) « les couches basses servaient de garde-fou ».
Reformulation minimale, pour la lecture (a) : « l'absence de contrat restait cantonnée au sommet, sans commander directement les couches situées au-dessous. » Le sens change selon la lecture retenue.

### Gravité B (gêne réelle)

**B1. Introduction**
Passage : « Pour le dire, ce chapitre reprend deux acquis […] : une chaîne cumule les angles morts, quand un contrôle croisé n'en garde que la part commune »
Problème : « Pour le dire » ne se rattache à rien de clair. Le « quand » peut se lire de deux façons : comme opposition (« alors que ») ou comme temps (« lorsque »).
Reformulation : « Pour y répondre, […] : une chaîne cumule les angles morts, alors qu'un contrôle croisé n'en garde que la part commune ». Le choix d'« alors que » suppose la lecture adversative, qui me paraît la plus probable.

**B2. Section *Pipelines* § 2, sections « Danger structurel » et « Blanchiment » (dépendances possibles)**
Passages : « une omission de saillance (@sec:ch12) », « sa frontière en dents de scie », « un fait rare inventé au deuxième tour », « un fait rare deviné ».
Problème : ces notions ne sont jamais glosées. « Fait rare » intrigue particulièrement, car on ne voit pas pourquoi la rareté compte ici. Le lecteur qui n'a pas lu le ch. 12 ne suit pas.
Reformulation : ajouter une glose de quelques mots à la première occurrence. Par exemple : « une omission de saillance (un détail présent mais négligé, @sec:ch12) » ; « un fait rare, trop peu représenté dans les données, inventé au deuxième tour ».

**B3. Section *Pipelines*, § 3**
Passage : « On morcelle donc cette finalité floue en sous-problèmes locaux plus nets, tandis que les résultats intermédiaires circulent toujours plus vite d'un module au suivant. »
Problème : le lien logique entre les deux propositions manque, et on ne sait pas « plus vite » par rapport à quoi. Le § suivant parle pourtant de « cette accélération » comme d'une chose établie.
Reformulation : « …en sous-problèmes locaux plus nets, et les résultats intermédiaires circulent d'un module au suivant bien plus vite qu'entre deux équipes d'ingénieurs. »

**B4. Section *Pipelines*, § 4**
Passage : « Dans un *pipeline* logiciel alimenté par des composants appris, l'effet s'accuse encore »
Problème : « l'effet » n'a pas d'antécédent net. On comprend après coup qu'il s'agit de l'incapacité de chaque poste à juger l'ensemble.
Reformulation : « …cette myopie des postes s'accuse encore ».

**B5. Section « Danger opérationnel », § 3**
Passage : « Pour qu'un humain exerce une prise en compte (@def:prise-en-compte) avant le dommage, l'alerte doit arriver avant que l'acte… »
Problème : « exercer une prise en compte » n'est pas idiomatique. Par ailleurs, « l'alerte » arrive sans avoir été introduite.
Reformulation : « Pour qu'un humain puisse prendre en compte une alerte (@def:prise-en-compte) avant le dommage, celle-ci doit lui parvenir avant que l'acte… »

**B6. Section « Danger opérationnel », après l'encadré, et section « Autorité », § 3**
Passages : « des programmes dont quelqu'un avait écrit les règles et où un écart conservait une adresse » ; « dont les erreurs fluides n'ont pas d'adresse de défaillance ».
Problème : ce sont des métaphores techniques héritées d'un chapitre antérieur, opaques sans définition. « Erreurs fluides » n'apparaît nulle part ailleurs dans ce chapitre.
Reformulation : « …où un écart pouvait être rattaché à une ligne de code précise » ; « dont les erreurs, plausibles en surface, ne se rattachent à aucun point de défaillance localisable ».

**B7. Section « Chiffrer une trajectoire longue », § 1, et l'encadré**
Passage : « le modèle M1 avait déjà chiffré l'effet d'une composition en série »
Problème : M1 est une dépendance que le chapitre ne présente pas. On reconstitue son contenu à partir des formules, mais seulement après coup.
Reformulation : « le modèle M1 (erreurs locales indépendantes, contrôles croisés, facteur commun) avait déjà chiffré… »

**B8. Encadré quantitatif, « Mise en place », dernier §**
Passage : « On ajoute enfin un facteur omis partagé, de probabilité $q$ »
Problème : on ne sait pas de quoi le facteur est « omis ». « Partagé » renvoie ici au producteur et à son contrôleur, mais la phrase dit aussi qu'il frappe l'ensemble de la trajectoire, ce qui laisse deux lectures. « Producteur » apparaît ici pour la première fois, à la place d'« agent ».
Reformulation : « un facteur omis partagé — une cause d'erreur que ni l'agent ni son contrôleur ne prennent en compte —, de probabilité $q$, qui pèse sur l'ensemble de la trajectoire ».

**B9. Section « Blanchiment », § 1**
Passage : « qui ne valait que sous des hypothèses explicites $A$ et dans les limites de $(\dots)$ »
Problème : à l'affichage, « $(\dots)$ » ressemble à un trou dans le texte ou à un espace réservé oublié. Quant à $A$, cette notation n'est jamais réutilisée.
Reformulation : « qui ne valait que sous certaines hypothèses et dans un certain domaine de validité ». Si la notation reprend celle du ch. 8, il faut la compléter.

**B10. Section « Blanchiment », § 2, et Points clés, puce 3**
Passages : « des *chaînes de caractères nues* » ; « circulent sous forme de chaînes de caractères nues […] transforme un *pipeline* […] en une chaîne aveugle ».
Problème : dans un chapitre dont le mot-clé est « chaîne » au sens de suite de maillons, « chaîne de caractères » (au sens de texte brut) crée une collision lexicale. Dans les Points clés, les deux sens se côtoient dans la même phrase.
Reformulation : « sous forme de texte brut » ou « de simples suites de caractères ». Garder « chaîne » pour la suite de maillons.

**B11. Section « Blanchiment », phrase précédant la liste à puces**
Passage : « le blanchiment des hypothèses et les deux proches cousins que la @sec:ch08-blanchiment en avait distingués : »
Problème : on annonce trois phénomènes (le blanchiment plus deux cousins), mais la liste n'a que deux puces. La première puce semble fondre le blanchiment et un cousin.
Deux lectures possibles, que je ne tranche pas : (a) les cousins sont « unités, définitions, domaines » et « provenance », et la première puce regroupe deux phénomènes ; (b) seuls les deux items de la liste comptent, et « le blanchiment des hypothèses » est de trop.
Reformulation pour la lecture (a) : scinder la première puce en deux. Pour la lecture (b) : « …on retrouve les deux formes du blanchiment que la @sec:ch08-blanchiment avait distinguées : ».

**B12. Section « Blanchiment », avant-dernier §**
Passage : « Au regard de la grille des cinq conditions de détection (@sec:ch06-cinq-conditions), le diagnostic est celui de la @sec:ch08-blanchiment »
Problème : le diagnostic n'est pas énoncé. On ne découvre qu'au § suivant que c'est la comparabilité qui est atteinte.
Reformulation : « …le diagnostic est celui de la @sec:ch08-blanchiment, c'est la comparabilité qui tombe, aggravé par… »

**B13. Section « Autorité », avant-dernier §**
Passage : « Le @sec:ch17 formalisera ces deux dispositifs complémentaires »
Problème : la phrase précédente énonce un seul principe (dissocier les espaces), pas deux dispositifs. Le référent de « ces deux dispositifs » reste à deviner : les espaces d'exploration et les frontières contrôlées ?
Reformulation : « Le @sec:ch17 formalisera ces deux régimes, le bac à sable et le point de contrôle avant l'acte, et montrera… ». C'est à vérifier par l'auteur, car le sens dépend de ce qu'il vise.

**B14. Points clés, puce 2, et encadré quantitatif**
Passage : « ils laissent intact tout facteur omis partagé par l'ensemble des maillons »
Problème : dans le corps, « partagé » signifie surtout « commun au producteur et à son contrôleur » (« l'angle mort commun du producteur et de son contrôleur »). La puce le définit plutôt comme commun à tous les maillons. Les deux formulations du même critère divergent.
Reformulation : « tout facteur omis que partagent l'agent et ses contrôleurs, et qui pèse sur toute la trajectoire ».

### Gravité C (confort, style)

**C1. Introduction**
Passage : « contrôle reporté sur chaque sortie au sommet de la pile »
Problème : « reporté » peut se lire comme « différé » ou comme « transféré ».
Reformulation : « contrôle déplacé sur chaque sortie… ».

**C2. Section *Pipelines*, § 4**
Passage : « répond aux conditions réelles de la route qu'il va emprunter »
Problème : le texte suppose sans le dire qu'il s'agit d'une ligne automobile.
Reformulation : « Sur une ligne d'assemblage automobile, … ».

**C3. Section *Pipelines*, puce 1**
Passage : « grammaticalement et syntaxiquement bien formé »
Problème : le doublon est quasi redondant.
Reformulation : « tant qu'il paraît bien formé ».

**C4. Introduction et section « Agents », § 1**
Passages : « des agents, dont les erreurs ne sont plus lues mais exécutées » (avant la définition en gras) ; « un simple maillon d'un graphe fixe ».
Problème : l'emploi en annonce est acceptable. « Graphe » est en revanche du jargon.
Reformulation : « d'un enchaînement fixe ».

**C5. Sections « Danger structurel » et « Blanchiment »**
Passages : « un fait rare inventé » / « un fait rare deviné ».
Problème : il s'agit de deux verbes pour le même phénomène, et le lecteur se demande s'ils désignent la même chose.
Reformulation : unifier les deux verbes.

**C6. Encadré Knight Capital**
Passages : « laissa actif en production un code dormant » / « le code dormant réactivé ».
Problème : on ne sait pas si le code était resté actif ou s'il a été réactivé.
Reformulation : harmoniser, par exemple « un code dormant que la mise à jour réactiva ».

**C7. Encadré quantitatif**
Passages : « manque chaque erreur locale avec la probabilité $m$ », « probabilité d'oubli indépendant », « laisse passer » (légende), « étourderies locales » ; « est $p^2 = 0{,}06^2$ ».
Problème : quatre mots désignent la même grandeur ou les mêmes erreurs. Par ailleurs, la formule écrit $p^2$ là où le raisonnement porte sur $p \cdot m$.
Reformulation : garder « manque » et « erreurs locales », et écrire « $p\,m = p^2 = 0{,}06^2$ ».

**C8. Encadré, « Lecture », puce 1**
Passage : « une fiabilité locale apparemment honorable à chaque pas ($p = 6\,\%$) »
Problème : on parle de fiabilité, mais on cite un taux d'erreur.
Reformulation : « un taux d'erreur local apparemment modeste ($p = 6\,\%$) ».

**C9. Paragraphe après l'encadré**
Passages : « de 21,9 % à 52,4 % » ; « C'est justement cette lisibilité que détruit ce qui transite aux interfaces ».
Problème : les pourcentages sont en texte brut, alors qu'ils sont en mode mathématique ailleurs, ce qui donne une typographie hétérogène. Par ailleurs, c'est la manière de transmettre qui détruit la lisibilité, plus que le contenu transmis.
Reformulation : « …que détruit la façon dont les résultats transitent aux interfaces… ».

**C10. Section « Autorité », § 1**
Passage : « Rassemblons maintenant la vue d'ensemble […] et ce que l'enchaînement […] vient y déplacer. »
Problème : le verbe régit deux compléments hétérogènes.
Reformulation : « Reprenons la vue d'ensemble […] pour voir ce que l'enchaînement […] vient y déplacer. »

**C11. Section « Autorité », § 4**
Passage : « croiser le diagnostic avec les quatre sources de comparateurs »
Problème : on annonce quatre sources, mais seulement deux cas suivent, ce qui crée une légère attente déçue.
Reformulation : « …en particulier avec la distinction… », en laissant tomber le croisement avec les quatre sources, ou bien en les nommer.

**C12. Section « Autorité », puce 1**
Passages : « Même une chaîne de douze tentatives » ; « avant qu'aucun changement n'atteigne ».
Problème : « tentatives » ne correspond pas aux « étapes » du calcul. Le tour « avant qu'aucun » est rare, et la plupart des lecteurs le jugeront fautif.
Reformulation : « …sans qu'aucun changement n'atteigne la production ».

**C13. Section « Autorité », puce 2**
Passage : « une série de décisions uniques à fort coût (@sec:ch04-decision-unique) »
Problème : c'est une dépendance non glosée.
Reformulation : « décisions uniques (qu'on ne peut pas rejouer pour apprendre) à fort coût ».

**C14. Section « Danger opérationnel », § après l'encadré**
Passage : « du moins n'y frappait-elle que des programmes »
Problème : la vitesse ne « frappe » pas des programmes.
Reformulation : « du moins ne concernait-elle que des programmes ».

**C15. Section « Blanchiment », § 1**
Passage : « effaçant l'écart entre livres-force-secondes et newton-secondes »
Problème : ce n'est pas l'écart qui est effacé, mais la distinction entre les deux unités.
Reformulation : « effaçant la distinction entre… ».

## 3. Appréciation globale

Les sections les plus accessibles sont « Danger opérationnel » (réponses et actions, cas Knight Capital), très claire et bien illustrée, et le parcours en quatre temps de la section « Blanchiment », qui est concret et convaincant.

L'encadré quantitatif est juste : j'ai vérifié les calculs, qui sont cohérents (52,4 %, 53,8 %, 4,24 %, 7,11 %, 42,2 %, 21,9 %). Il est toutefois alourdi par des dépendances (M1, $B_{\text{cmp}}$, « facteur omis ») et par un vocabulaire flottant pour une même grandeur.

Les sections les moins accessibles sont l'introduction (dense, faite de renvois en chaîne) et la section « Autorité et garanties inversées ». Cette dernière s'appuie sur des métaphores héritées (« adresse », « erreurs fluides », « décisions uniques ») et contient la phrase ambiguë signalée en A1, qui touche le cœur de l'argument sur l'inversion.
