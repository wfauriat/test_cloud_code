# Lecture fraîche — chapitre 7 « Le cadre, cause commune de nos contrôles »

Lecteur : Opus (première lecture, seul fichier lu : `chapitres/07-cadre-cause-commune.md`).

## 1. Résumé de ce que j'ai compris (test de lisibilité)

1. Comme deux pompes de secours branchées sur la même alimentation, des contrôles redondants qui partagent une cause amont tombent en panne ensemble : c'est la défaillance de mode commun.
2. Tous les contrôles calculés à l'intérieur d'un cadre (relecture, contre-calcul, rééchantillonnage) partagent le cadre comme cause commune. Face à un facteur omis $z$, leur accord n'apporte aucune information (rapport de vraisemblance égal à 1, modèle M3).
3. Les observations du monde peuvent révéler $z$, mais seulement si $z$ a varié pendant la collecte, et seulement sous la forme d'une dispersion inexpliquée des grandeurs que le cadre enregistre. Sinon, on obtient une « dérive de distribution » une fois le système en service (cas de Google Flu Trends).
4. Toute méta-procédure qui juge un cadre adopte elle-même un cadre, d'où une régression à l'infini (théorèmes *no free lunch*, Hume, Goodman).
5. Une pertinence nouvelle n'entre donc que de l'extérieur : soit quelqu'un d'autre nous avertit, soit on la découvre par l'épreuve du monde. Cette seconde voie a un coût, d'où la règle d'explorer là où l'essai est peu coûteux et réversible.

Le fil d'ensemble se suit bien ; les points ci-dessous gênent localement.

## 2. Constats classés par gravité

### Gravité A (compréhension compromise ou contresens possible)

**A1 — Points clés, 3e puce (incohérence avec le corps du texte)**
« elles le montrent alors comme une dispersion inexpliquée, ou par une dérive de distribution lorsqu'il bouge après coup. »
- **Ce qui gêne :** dans le corps du texte (§ « Quand les observations… »), la dérive de distribution est justement le cas où $z$ est resté constant pendant la collecte. Les contrôles fondés sur ces données « ne pouvaient pas le voir ». Or la puce semble dire que les observations collectées révèlent le facteur « par une dérive de distribution ».
- **Deux lectures plausibles :**
  - (i) Ce sont les observations recueillies *après* la mise en service qui le révèlent, à travers la dérive.
  - (ii) La dérive serait l'une des façons dont les données de collecte le montrent. Cette lecture contredit le corps du texte.
- Je ne tranche pas.
- **Reformulation minimale, selon la lecture (i) :** « … elles le montrent alors comme une dispersion inexpliquée ; s'il n'a pas varié pendant la collecte et ne bouge qu'après coup, on parle de dérive de distribution, invisible aux contrôles fondés sur ces données. » Le sens change si l'auteur visait autre chose.

### Gravité B (gêne réelle)

**B1 — § Le cadre comme cause commune, l. 41**
« Dès que $x$ est fixé, l'accord ou le désaccord entre $f_1(x)$ et $f_2(x)$ est déjà arrêté — tout au plus à des tirages internes sans lien avec $z$. »
- **Ce qui gêne :** la phrase est agrammaticale. Il manque visiblement « près » (« à … près »).
- **Proposition :** « … est déjà arrêté, aux tirages internes près, qui n'ont aucun lien avec $z$. » Le sens ne bouge pas.

**B2 — § Le cadre comme cause commune, l. 69**
« Cet argument formel appelle trois précisions sur son champ d'application réel : conditionner nettement sur $x$ reste une idéalisation, et l'impuissance d'un contrôle interne face à $z$ ne retire rien à son utilité […] »
- **Ce qui gêne :** la phrase annonce trois précisions mais n'en énumère que deux après les deux-points. La deuxième nuance de l'encadré (l'omission de saillance) n'y figure pas. Le lecteur cherche la troisième.
- **Proposition :** « … conditionner nettement sur $x$ reste une idéalisation, un facteur peut être représenté sans être mobilisé, et l'impuissance d'un contrôle interne… » Autre solution : supprimer l'énumération et garder seulement « appelle trois précisions ».

**B3 — Proposition @prop:cause-commune, l. 38, et modèle M3**
« Les deux parties de cet énoncé sont des résultats sous hypothèses ; la partie (b) est illustrée ci-dessous par des constats empiriques. »
- **Ce qui gêne :** les hypothèses ne sont énoncées que plus loin, dans M3, et M3 ne couvre que le volet (a). Pour (b), le lecteur ne trouve aucune liste d'hypothèses et se demande lesquelles sont visées.
- **Proposition :** « … sont des résultats sous hypothèses (explicitées pour (a) dans le modèle M3 ci-dessous) ; la partie (b)… » Le sens peut bouger si l'auteur pense à d'autres hypothèses pour (b).

**B4 — Modèle M3, « Limite », l. 66**
« ni $f_1$ ni $f_2$ ne dépendent d'observations réelles où $Z$ aurait varié […] mesures issues de $g(X, Z)$ »
- **Ce qui gêne :** la notation passe sans prévenir de $z$ minuscule (partout ailleurs) à $Z$ majuscule. Le lecteur ne sait pas s'il s'agit du même objet. Ce serait la variable aléatoire correspondante, par analogie avec $X$ et $x$, mais rien ne le dit.
- **Proposition :** ajouter une incise à la première occurrence : « où $Z$ (le facteur omis considéré comme variable, dont $z$ est une valeur) aurait varié ».

**B5 — Modèle M3, hypothèse 2, l. 53**
« aucune variable retenue dans $X$ ne varie avec $z$ au-delà de ce que $x$ fixe déjà. »
- **Ce qui gêne :** une fois $X = x$ fixé, aucune variable de $X$ ne varie plus, et la clause paraît donc tautologique. Le lecteur ne voit pas ce qu'elle exclut.
- **Lecture probable :** aucune variable de $X$ ne sert d'indicateur indirect de $z$. Elle n'est pas certaine.
- **Proposition, sous cette lecture :** « aucune variable retenue dans $X$ ne porte d'information sur $z$ au-delà de ce que la valeur $x$ fixe déjà ». À valider par l'auteur, car le sens peut bouger.

**B6 — Modèle M3, l. 48 et l. 56**
« au sens d'une tolérance convenue » / « dépasse une tolérance fixée »
- **Ce qui gêne :** le même mot désigne deux seuils distincts : celui de la concordance $A$ entre $f_1$ et $f_2$, et celui de l'ampleur de l'erreur $e$. Un lecteur peut croire qu'il s'agit du même.
- **Proposition :** « (à une tolérance d'accord convenue près) » et « dépasse un seuil d'erreur fixé ». Le sens ne bouge pas.

**B7 — Modèle M3, l. 48**
« Soit une grandeur réelle $Y = g(x, z)$ »
- **Ce qui gêne :** « réelle » a deux lectures plausibles. Soit « à valeurs réelles » (sens mathématique), soit « du monde réel » (en écho à « l'issue réelle produite par le monde », l. 41). Je ne tranche pas.
- **Proposition :** « Soit la grandeur effectivement observée dans le monde, $Y = g(x, z)$ » (lecture 2), ou « une grandeur à valeurs réelles » (lecture 1).

**B8 — § Le cadre comme cause commune, l. 27**
« (avec le même coefficient de sécurité de 1,8 qu'au @sec:ch05) »
- **Ce qui gêne :** la parenthèse n'est pas exploitée. On ne sait pas pourquoi ce coefficient est rappelé ici ; on devine qu'il ne couvre pas la corrosion, mais rien ne le dit. Possible dépendance au chapitre 5.
- **Proposition :** « (avec le même coefficient de sécurité de 1,8 qu'au @sec:ch05, qui ne couvre pas ce mécanisme) ». Le sens peut bouger si le rappel a une autre fonction.

**B9 — Encadré « Portée réelle… », 2e puce, l. 75**
« Le volet (a) de la @prop:cause-commune ne s'applique alors qu'aux contrôles qui réutilisent les mêmes paramètres ajustés et la même formulation de la question »
- **Ce qui gêne :** ici le facteur figure dans l'entrée, donc dans $x$. Le lecteur ne voit pas comment le volet (a), formulé pour un facteur *absent* de $x$, s'applique encore, même restreint. Le lien est elliptique.
- **Proposition :** « Le volet (a) ne vaut alors, par extension, que pour les contrôles qui réutilisent… ». Signalé sans trancher : l'auteur peut vouloir dire autre chose qu'une extension.

**B10 — § Quand les observations…, l. 91**
« il peut couper le fil rouge au fil de mille essais simulés sans jamais rien apprendre de la couleur. »
- **Ce qui gêne, sur le sens :** le « fil rouge » n'a pas été introduit. On ne sait pas s'il est le fil dangereux ou un fil sans danger.
- **Ce qui gêne, sur le style :** la répétition « fil… au fil » est maladroite.
- **Proposition :** « il peut, au cours de mille essais simulés, couper le bon fil sans jamais rien apprendre de la couleur ». Le sens bouge si « rouge » avait un rôle voulu (par exemple, le rouge serait toujours le fil dangereux).

**B11 — § Quand les observations…, l. 101**
« L'épisode illustre les deux volets de la @prop:cause-commune. […] Dès que cet arrière-plan a bougé, le modèle n'a cédé que face à des données indépendantes du moteur de recherche. »
- **Ce qui gêne, sur la correspondance :** le texte ne dit pas quelle phrase illustre quel volet ; le lecteur doit faire la correspondance seul.
- **Ce qui gêne, sur le verbe :** « céder » est ambigu. Il peut vouloir dire « s'est dégradé » ou « a été pris en défaut ».
- **Proposition :** « Tant que […], aucune analyse des seules requêtes ne signalait la fragilité du lien (volet (b) : $z$ ne variait pas). Dès que cet arrière-plan a bougé, seul un comparateur indépendant du moteur de recherche a pu révéler l'écart (volet (a)). » Ce découpage est mon interprétation et l'auteur doit le valider.

**B12 — § Comment une pertinence nouvelle…, l. 126**
« l'information neuve franchit la frontière du cadre parce qu'elle n'en a pas été calculée. »
- **Ce qui gêne :** « en » est à la fois flou et peu idiomatique (« calculée du cadre »).
- **Proposition :** « … parce qu'elle n'a pas été calculée à partir de lui. » Le sens ne bouge pas.

**B13 — § Comment une pertinence nouvelle…, l. 119**
« ou les changements de comportement d'usage au suivi d'un indicateur en ligne. »
- **Ce qui gêne :** cet « indicateur en ligne » n'apparaît nulle part ailleurs dans le chapitre, contrairement aux deux autres exemples. On ne sait pas s'il renvoie à Google Flu Trends ou à un exemple d'un chapitre antérieur (possible dépendance). « Comportement d'usage » est en outre lourd.
- **Proposition, si l'exemple renvoie à Google Flu Trends :** « ou l'évolution des habitudes de recherche au suivi de la grippe par les requêtes en ligne ». Sinon, il faut un renvoi au chapitre concerné.

**B14 — Introduction, l. 3**
« laissant le reste dans un arrière-plan $(\dots)$ »
- **Ce qui gêne :** la notation $(\dots)$ est opaque pour qui n'a pas le chapitre 2 en tête (possible dépendance). On peut la prendre pour une coupure de citation.
- **Proposition :** « laissant le reste dans un arrière-plan, noté $(\dots)$ au @sec:ch02 ».

### Gravité C (confort / style)

**C1 — § Le cadre comme cause commune, l. 29**
« La proposition suivante réunit cette clôture interne et les conditions… »
- **Ce qui gêne :** « clôture interne » apparaît sans avoir été introduite.
- **Proposition :** « … réunit cette impuissance des contrôles internes et les conditions… »

**C2 — Encadré « Redondance et cause commune », l. 14**
« ajouter une troisième protection indépendante le réduit encore d'un ordre de grandeur »
- **Ce qui gêne :** le gain n'est d'un ordre de grandeur que si chaque probabilité vaut environ 0,1. La formulation paraît générale.
- **Proposition :** « … le réduit encore, par exemple d'un ordre de grandeur si chaque protection échoue une fois sur dix ». Le calcul reste inchangé.

**C3 — § La défaillance de mode commun, l. 11**
« elles ne forment qu'un double câblage sous une vulnérabilité unique. »
- **Ce qui gêne :** l'image est peu claire, surtout « double câblage sous ».
- **Proposition :** « elles ne forment qu'une protection dédoublée exposée à une vulnérabilité unique ».

**C4 — § Le cadre comme cause commune, l. 25**
« reprenant la lettre esquissée au @sec:ch05 »
- **Ce qui gêne :** « esquisser » une lettre sonne étrange.
- **Proposition :** « reprenant la lettre introduite de façon informelle au @sec:ch05 ».

**C5 — Ensemble du chapitre (l. 41, 69, 74)**
« conditionner sur $x$ », « conditionnent rarement sur le vecteur $x$ »
- **Ce qui gêne :** calque de *condition on*.
- **Proposition :** « raisonner conditionnellement à $x$ ». Cela reste acceptable dans un jargon statistique ; à harmoniser seulement si l'auteur le souhaite.

**C6 — § Le cadre comme cause commune, l. 41, et M3, l. 48**
« l'issue réelle $g(x, z)$ » / « une grandeur réelle $Y$ »
- **Ce qui gêne :** le même objet porte deux noms (« issue » est par ailleurs proche de *outcome*).
- **Proposition :** harmoniser, par exemple « la grandeur réelle » dans les deux passages.

**C7 — § Le cadre comme cause commune, l. 41**
« Le rapport de vraisemblance de cet accord, conditionnellement à $x$, vaut exactement $1$ »
- **Ce qui gêne :** le texte ne précise pas encore quelles hypothèses sont comparées (« grande » contre « petite » erreur ; la précision n'arrive que dans M3). « Cote préalable » est une possible dépendance au chapitre 1.
- **Proposition :** « Le rapport de vraisemblance de cet accord (erreur importante contre erreur faible), conditionnellement à $x$, … »

**C8 — Proposition, l. 36-38 ; suite du texte, l. 41 et 83**
« partie (b) » / « volet (a) », « volet (b) »
- **Ce qui gêne :** les deux termes alternent pour désigner la même chose.
- **Proposition :** uniformiser sur « volet ».

**C9 — § Quand les observations…, l. 83-87**
« deux limites rigoureuses » puis « La première condition… La seconde condition »
- **Ce qui gêne :** « limites » et « conditions » alternent, et « rigoureuses » est impropre au sens de « strictes ». De plus, la « seconde condition » est formulée comme une restriction (« ne peuvent apparaître qu'à travers »), et non comme une condition. Les Points clés la formulent, eux, comme une condition (« que ses effets modifient des grandeurs enregistrées »).
- **Proposition :** « deux conditions strictes », puis « La seconde condition est que ses effets touchent des grandeurs que le cadre enregistre ; et même alors… ».

**C10 — § Quand les observations…, l. 91**
« un automate d'essais et d'erreurs »
- **Ce qui gêne :** calque de *trial-and-error*.
- **Proposition :** « un automate qui apprend par essais-erreurs » (ou « par tâtonnement »).

**C11 — § La régression à l'infini, l. 109**
« tous obtiennent exactement la même performance moyenne, y compris face à une recherche aléatoire aveugle. »
- **Ce qui gêne :** « face à » est mal choisi, puisque la recherche aléatoire fait partie des algorithmes comparés.
- **Proposition :** « … la même performance moyenne, recherche aléatoire aveugle comprise ».

**C12 — § La régression à l'infini, l. 109**
« elle confirme le propos au lieu de le lever »
- **Ce qui gêne :** on lève une objection, pas un propos.
- **Proposition :** « elle confirme le propos au lieu de l'affaiblir ».

**C13 — § La régression à l'infini, l. 113**
« « vleu » » puis « *vleue* », « « *vleu* » »
- **Ce qui gêne :** l'italique n'est pas homogène.
- **Proposition :** mettre toutes les occurrences en italique (ou aucune).

**C14 — § La régression à l'infini, l. 113**
« précède l'inférence et ne peut jamais être tiré de rien. »
- **Ce qui gêne :** « tiré de rien » est flou. Deux lectures sont possibles : « ne peut pas être déduit des seules données », ou « ne surgit jamais *ex nihilo* ». Je ne tranche pas.
- **Proposition, selon la lecture 1 :** « … précède l'inférence et ne peut être tiré des seules données ».

**C15 — § Le cadre comme cause commune, l. 19**
« partage la même origine amont »
- **Ce qui gêne :** légère redondance.
- **Proposition :** « partage une origine amont avec l'affirmation… ».

**C16 — § Comment une pertinence nouvelle…, l. 130**
« il convient d'explorer activement le monde là où […] et de recourir à des comparateurs extérieurs avant d'agir dès que […] »
- **Ce qui gêne :** la phrase est longue, avec deux branches symétriques chargées chacune de trois qualificatifs.
- **Proposition :** couper en deux phrases (« Il convient d'explorer activement… à apprendre. À l'inverse, dès que la réponse du monde coûterait trop cher… »).

## 3. Appréciation globale

- **Sections les plus accessibles :**
  - « La défaillance de mode commun » : l'exemple des pompes est d'une grande clarté.
  - « La régression à l'infini » : l'argument est bien progressif, de la méta-procédure à *no free lunch*, Hume puis Goodman, et l'exemple de « vleu » est bien amené.
  - « Comment une pertinence nouvelle entre » : les deux voies sont nettes, la règle de prudence est utile.
- **Section la moins accessible :** le cœur formel de « Le cadre comme cause commune ».
  - Le modèle M3 est solide, mais ses notations gênent : $z$ devient $Z$, « tolérance » désigne deux seuils, et l'hypothèse 2 est opaque.
  - L'annonce des « trois précisions » est incomplète.
  - La proposition renvoie à des hypothèses qui ne sont explicitées que pour son volet (a).
- **Section intermédiaire :** « Quand les observations… ». Elle se suit, mais le flottement entre « limites » et « conditions », l'exemple du fil rouge et le paragraphe de rattachement de Google Flu Trends aux deux volets demandent un effort.
- **Points clés :** la 3e puce présente la dérive de distribution d'une manière qui peut contredire le corps du texte (A1).
