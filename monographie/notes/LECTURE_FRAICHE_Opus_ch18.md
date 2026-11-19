# Lecture fraîche — chapitre 18, « Un remède à trois niveaux »

Lecteur : Opus, première lecture, sans autre fichier que `chapitres/18-remede-trois-niveaux.md`.

## 1. Ce que j'ai compris (test de lisibilité)

1. Le chapitre ne propose pas de règlement : il rassemble des pratiques pour organiser les contrôles, réparties sur trois niveaux (attitude, placement, organisation).
2. Niveau 1, l'attitude : se donner soi-même des comparateurs (attente écrite à l'avance, pré-mortem, scénarios élargis). C'est nécessaire, mais cela reste prisonnier du cadre de la personne et des incitations.
3. Niveau 2, le placement : décider où contrôler (aux points de passage vers l'action), qui contrôle (quelqu'un qui partage l'interface et lit « une couche au-dessous »), quoi contrôler (la sortie, mais aussi la représentation) et avec quel effort (proportionné aux enjeux, la production étant plafonnée par la capacité de contrôle). Le RAG sert d'exemple d'outil de placement.
4. Niveau 3, l'organisation : budgéter la capacité d'évaluation, exiger un statut pour chaque affirmation, tenir un historique, mesurer l'échappement par erreurs injectées (sur le modèle de la TIP en aviation et du test par mutation).
5. Aucun niveau ne couvre seul les cinq conditions de détection ; le chapitre se clôt sur cinq questions à poser au dispositif de contrôle avant d'agir.

Le fil général se suit bien. Les difficultés tiennent surtout à des notations et à des termes techniques hérités des chapitres antérieurs, et à quelques flottements de vocabulaire (conditions/barrages, contrôleur humain/automatique).

## 2. Constats classés par gravité

### Gravité A

**A1. Section « Cinq questions avant d'agir », question 3 (liste et encadré)**
« *Les conditions sont-elles énoncées de sorte que les deux puissent être comparés ?* »
Ce qui gêne : dans tout le chapitre, « les conditions » désigne les cinq conditions de détection ; ici, le mot renvoie aux hypothèses et aux limites de validité de l'affirmation. Dans l'encadré, sans le développement qui suit, une lecture erronée est probable (« les cinq conditions sont-elles énoncées ? »). « Les deux » (comparateur et affirmation) n'a pas non plus d'antécédent dans l'encadré.
Reformulation minimale : « Les hypothèses et les conditions de validité sont-elles énoncées de sorte que l'affirmation et le comparateur puissent être comparés ? »
Le sens ne bouge pas si la lecture « hypothèses de l'affirmation » est la bonne, ce que suggère le développement (« a-t-elle gardé ses hypothèses, ses unités… »). À confirmer par l'auteur.

### Gravité B

**B1. Introduction**
« ni méta-procédure qui garantirait son propre cadre (@sec:ch07-regression) »
Ce qui gêne : l'idée reste elliptique pour qui n'a pas en tête le chapitre 7 (il s'agit vraisemblablement de la régression d'un contrôle qui devrait contrôler son propre cadre). C'est une possible dépendance.
Reformulation : « ni méta-procédure censée garantir elle-même la validité de son propre cadre, ce qui mènerait à une régression (@sec:ch07-regression) ». Cette version suppose une lecture précise ; à valider.

**B2. Introduction, et section « Élargir à dessein… »**
« en précisant pour chacune sa raison d'être, ses limites et son appui »
Ce qui gêne : l'introduction annonce, pour chaque pratique, ses limites. La troisième pratique du niveau 1 (élargir les mondes possibles) n'en a pourtant aucune, alors que les deux autres ont chacune leur phrase « La limite… ». Le lecteur cherche cette limite.
Reformulation : ajouter une phrase de limite à cette sous-section, ou alléger l'annonce (« en précisant, le cas échéant, ses limites »). Cette correction touche au contenu : c'est à l'auteur de décider.

**B3. Niveau 1, premier paragraphe**
« L'argument de ce livre conduit à renverser cet ordre. »
Ce qui gêne : la phrase précédente décrit deux conceptions de l'humilité (politesse ajoutée après coup, vertu paralysante), pas un « ordre ». Seule la première suppose implicitement une séquence (le calcul d'abord, l'humilité ensuite).
Reformulation : « L'argument de ce livre conduit à renverser cette hiérarchie : l'humilité vient d'abord. » Ou « …à renverser cet ordre, qui place l'humilité après le calcul. »

**B4. Niveau 1, deuxième paragraphe**
« la génération instantanée efface la friction qui les fabriquait sans qu'on y pense »
Ce qui gêne : deux lectures sont plausibles. Soit la friction fabriquait les comparateurs sans qu'on y pense, soit la génération efface cette friction sans qu'on s'en aperçoive.
Reformulation, première lecture : « efface la friction qui, sans qu'on y pense, les fabriquait ». Seconde lecture : « efface, sans qu'on y prenne garde, la friction qui les fabriquait ». Je ne tranche pas entre les deux.

**B5. Tout le chapitre (dès « Se donner une attente… », puis « Qui », « Où », etc.)**
« Ce geste agit sur deux des cinq conditions (@sec:ch06-cinq-conditions). »
Ce qui gêne : les cinq conditions structurent tout le chapitre (« deuxième condition », « quatrième condition », tableau de synthèse, cinq questions), mais elles ne sont énumérées que dans la légende de la figure, vers la fin. Avant cela, le lecteur doit les reconstituer morceau par morceau. C'est une possible dépendance.
Reformulation : dès la première mention, ajouter une incise qui les rappelle : « (existence d'un comparateur, capacité à se tromper autrement, comparabilité, arrivée à temps, prise en compte) ».

**B6. Pré-mortem, second paragraphe**
« quelle variation de l'arrière-plan $(\dots)$ (@eq:ch01-regle) »
Ce qui gêne : la notation $(\dots)$ s'affiche comme des points de suspension entre parenthèses ; elle est opaque sans l'équation du chapitre 1. C'est une possible dépendance.
Reformulation : « quelle variation des conditions d'arrière-plan laissées implicites dans la règle (@eq:ch01-regle) ».

**B7. « Élargir à dessein l'ensemble des mondes possibles »**
« Pour le raisonnement, cette branche prend la forme de trois questions […]. Pour l'acte, elle rejoint la marge d'humilité »
Ce qui gêne : « cette branche » et « elle » renvoient soit à la seule branche « et si quelque chose nous échappait ? », soit à toute la pratique d'élargissement. S'y ajoute un flottement de termes : le titre parle de « mondes possibles », le texte d'« alternatives admises $\Theta$ ».
Reformulation : « Pour le raisonnement, cette question prend la forme… ; pour l'acte, elle rejoint… ». Si c'est la pratique entière qui est visée : « Pour le raisonnement, cet élargissement prend la forme… ». Je ne tranche pas. Pour le titre, on peut écrire « l'ensemble des mondes possibles, c'est-à-dire des alternatives admises $\Theta$ ».

**B8. Même sous-section**
« une marge $b$ ajoutée au risque estimé, qui relève du jugement et non d'une mesure de $z$ »
Ce qui gêne : $z$ n'est pas défini dans le chapitre. Le lecteur ne sait pas ce qu'on ne mesure pas. C'est une possible dépendance.
Reformulation : « …et non d'une mesure de $z$, la part du risque que le modèle ne représente pas » (à ajuster selon la définition réelle de $z$).

**B9. Niveau 1, « Limite structurelle… », et Niveau 3, « statut »**
« l'équilibre mélangeant du @sec:ch15 »
Ce qui gêne : ce terme de théorie des jeux (en anglais, *pooling equilibrium*) n'est pas transparent pour un lecteur cultivé. C'est une possible dépendance.
Reformulation, à la première occurrence : « l'équilibre mélangeant du @sec:ch15, où réponses contrôlées et non contrôlées deviennent indiscernables ».

**B10. Niveau 2, premier paragraphe**
« Là où s'arrête la garantie préalable, parce que des composants appris occupent le sommet de la pile (…) ou parce que des modules spécifiés conduisent à une décision dont le cadre reste ouvert (…), le contrôle ne peut plus porter sur la couche prise en bloc »
Ce qui gêne : la phrase d'ouverture du niveau est longue et accumule « garantie préalable », « sommet de la pile » et « couche prise en bloc » sans les expliciter.
Reformulation : couper en deux phrases. « La garantie préalable s'arrête dans deux cas : quand des composants appris occupent le sommet de la pile (…), ou quand des modules spécifiés conduisent à une décision dont le cadre reste ouvert (…). Le contrôle ne peut plus alors porter sur l'ensemble de la couche : il faut le placer… »

**B11. Niveau 2, deuxième paragraphe**
« celui qui ne lit plus qu'une alerte sur deux d'un contrôleur dont presque toutes les alertes sont fausses »
Ce qui gêne : partout ailleurs, « contrôleur » désigne la personne qui contrôle. Ici, il s'agit d'un dispositif automatique d'alerte. Le lecteur hésite.
Reformulation : « …d'un système d'alerte dont presque toutes les alertes sont fausses ».

**B12. « Où : aux points de passage vers l'action »**
« où une sortie cesse d'être lue comme une ébauche que l'on discute pour être tenue pour acquise »
Ce qui gêne : « pour » peut se lire comme un but (« afin d'être tenue pour acquise »), ce qui fausse le sens. Le point clé dit bien « là où une sortie commence à être tenue pour acquise ».
Reformulation : « où une sortie cesse d'être lue comme une ébauche que l'on discute et commence à être tenue pour acquise ».

**B13. « Quoi », dernier paragraphe**
« ne fait pas sortir du cercle du prêteur unique (@sec:ch16-meme-preteur) »
Ce qui gêne : la métaphore du « prêteur unique » apparaît ici sans glose. Elle ne s'éclaire qu'à la question 2 (« le prêteur unique auquel toute la profession emprunte »). C'est une possible dépendance.
Reformulation : « …du cercle du prêteur unique, cette source commune à laquelle tous empruntent (@sec:ch16-meme-preteur) ».

**B14. « Combien », premier paragraphe**
« comme le rapport des enjeux $L/\Delta U$ fixe le seuil $p^\ast$ aux chapitres [-@sec:ch04] et [-@sec:ch17] »
Ce qui gêne : $\Delta U$ et $p^\ast$ ne sont pas définis dans le chapitre. Seul $L$ est glosé ensuite (« la perte $L$ »). C'est une possible dépendance.
Reformulation : « comme le rapport entre la perte en cas d'erreur $L$ et le gain de l'action $\Delta U$ fixe le seuil de décision $p^\ast$… » (à ajuster selon les définitions réelles).

**B15. « Un outil de placement : RAG », dernier paragraphe**
« le lien devient un décor qui augmente la confiance apparente sans réduire l'échappement »
Ce qui gêne : « échappement » est un terme technique. Il n'est défini (renvoi @def:echappement et formule) que dans la section sur les erreurs injectées, plus loin. C'est une possible dépendance, utilisée avant son explicitation dans le chapitre.
Reformulation : « …sans réduire l'échappement, c'est-à-dire la part des erreurs qui franchissent le contrôle ».

**B16. « Combien » (niveau 2) et « Dimensionner la production » (niveau 3) ; points clés 2 et 4 ; synthèse du niveau 3**
« c'est la *capacité de contrôle disponible qui plafonne la production admise jusqu'à l'action* » (niveau 2) / « plafonner le flux d'affirmations promues vers l'action à ce que cette capacité peut absorber » (niveau 3)
Ce qui gêne : la même pratique est présentée deux fois, à deux niveaux, et attribuée tantôt au placement (point clé 2), tantôt à l'organisation (point clé 4 et synthèse). Le lecteur ne sait plus de quel niveau elle relève.
Reformulation : au niveau 2, annoncer le renvoi : « …qui plafonne la production admise jusqu'à l'action ; le niveau 3 en tire une règle budgétaire (@sec:ch18-org-capacite) ». Le contenu reste inchangé.

**B17. « Comment les trois niveaux… », puce Niveau 3**
« en évitant de dépendre d'un prêteur unique » ; « en protégeant l'autorité de celui qui alerte »
Ce qui gêne : aucune des sous-sections du niveau 3 ne développe ces deux éléments. Le plus proche est l'« arbitrage explicite de la direction » dans « Dimensionner ». La synthèse attribue donc au niveau 3 des pratiques que le corps du texte ne présente pas.
Reformulation : soit rattacher explicitement (« …en protégeant, par l'arbitrage de la direction, l'autorité de celui qui alerte »), soit retirer de la synthèse. C'est à l'auteur de décider ; le contenu est concerné.

**B18. Encadré « Ce que mesurent… », point 1**
« Dans la revue structurelle de la ferrure (@sec:ch05, @sec:ch08, @sec:ch13) »
Ce qui gêne : « la ferrure » est un exemple suivi d'autres chapitres, jamais présenté ici. L'article défini suppose que le lecteur le connaît. Le chapitre l'évoque pourtant sans le nommer (« calcul de structure par éléments finis », « brouillard salin »). C'est une possible dépendance.
Reformulation : « Dans l'exemple récurrent de la ferrure, cette pièce métallique dont le calcul par éléments finis ignorait la corrosion (@sec:ch05…) » (à ajuster selon l'exemple réel).

**B19. « Comment les trois niveaux… » et points clés**
« les cinq barrages du @sec:ch06 »
Ce qui gêne : après tout un chapitre qui parle de « conditions », le mot « barrages » surgit (légende, synthèse, point clé 5) sans qu'on dise qu'il s'agit des mêmes choses.
Reformulation : « les cinq conditions du @sec:ch06, qui sont autant de barrages (@fig:ch06-cinq-conditions) ».

### Gravité C

**C1. Introduction.** « alors que l'automatisation les enchaîne, les érode et les corrèle » : « enchaîne » se lit aussi comme « entrave ». Proposition : « les met en série, les érode et les corrèle ». Le sens bouge si « entraver » était voulu.

**C2. Introduction.** « comment trancher une décision unique » : la collocation est peu idiomatique (on tranche une question). Proposition : « comment prendre une décision unique ».

**C3. Introduction.** « et son appui : dispositif documenté ou proposition » : « appui » est vague. Proposition : « et son statut : dispositif documenté ou simple proposition ».

**C4. Niveau 1, deuxième paragraphe.** « si on ne les entretient pas délibérément, ils disparaissent les premiers » : « les premiers » appelle un « parmi quoi ? ». Proposition : « ils sont les premiers à disparaître ».

**C5. « Se donner une attente… », premier paragraphe.** « prolonge la discipline dégagée à la @sec:…, se forger un avis avant de consulter le modèle » : l'apposition infinitive est abrupte. Proposition : « …la discipline dégagée à la @sec:… : se forger un avis… ». Par ailleurs, « la flèche » (déformation d'une poutre) est un terme technique ; on peut écrire « la flèche (la déformation) ».

**C6. « Se donner une attente… », second paragraphe.** « Une attente écrite à l'avance change cette lecture passive en confrontation » : proposition « transforme cette lecture passive en confrontation ». Plus loin, « l'attente peut être arbitraire. Elle ne sert donc pas à défendre… » : le « donc » ne découle pas clairement de l'arbitraire. Proposition : « C'est pourquoi elle ne sert pas… ».

**C7. Pré-mortem.** « chacun parcourt les variables déjà représentées » : « représentées » est du jargon (« prises en compte dans le modèle »). Proposition : « les variables déjà prises en compte dans le plan ».

**C8. Pré-mortem.** « La limite tient au contexte » : la limite décrite tient plutôt à l'usage ritualisé. Proposition : « La limite tient à l'usage ». Aussi : « sans prise en compte (@def:prise-en-compte) » se lit comme une locution ordinaire, alors que c'est un terme défini (la cinquième condition). « Verrous » y est employé avant d'être rappelé (section « Où »).

**C9. Section « Qui » et suivantes.** « une couche au-dessous » / « la couche au-dessous » / « la couche inférieure » / « la couche sous-jacente » / « la couche située sous l'interface » : cinq formulations pour une même notion clé. Ce n'est pas faux, mais un lecteur peut se demander s'il s'agit de la même chose. On peut fixer « une couche au-dessous (de l'interface) » à la première occurrence. Sur le plan idiomatique, « une couche en dessous » est plus courant que « une couche au-dessous ».

**C10. « Qui », premier paragraphe.** « ses objections ne trouvent pas prise, faute de comparabilité : c'est l'angle mort de la comparaison, $B_{\text{cmp}}$ » : la notation $B_{\text{cmp}}$ est introduite puis jamais réutilisée, et l'on dit plutôt « n'ont pas de prise ». Proposition : « ses objections n'ont pas de prise, faute de comparabilité ». La notation peut être supprimée ou rattachée à son renvoi d'origine.

**C11. « Qui », dernier paragraphe.** « il joue une mise en scène » : la tournure est peu idiomatique. Proposition : « il se livre à une mise en scène ».

**C12. « Où ».** « La première question répond d'abord à la quatrième condition » : ce « d'abord » annonce d'autres conditions, qui ne viennent pas. Proposition : supprimer « d'abord ».

**C13. « Quoi ».** « (omission structurelle, omission de saillance) » et « la frontière en dents de scie » : ce sont des termes d'autres chapitres, sans glose (possible dépendance). L'ordre des parenthèses (absent → structurelle, non mobilisé → saillance) est implicite. Proposition : « un facteur absent de la représentation (omission structurelle), ou présent mais non mobilisé (omission de saillance) ».

**C14. « Combien ».** « à mesure que […] le retour en arrière se ferme » : proposition « devient impossible ». Également : « une conséquence de flux » (calque ; proposition « une conséquence sur les flux ») ; « alertes de faible valeur prédictive positive » (jargon statistique, possible dépendance ; proposition « alertes dont la plupart sont fausses ») ; « la production admise jusqu'à l'action » (elliptique ; proposition « la production autorisée à aller jusqu'à l'action »).

**C15. « Dimensionner la production ».** « qui dimensionne le volume de production mis en service » : « mis en service » convient mal à un volume. Proposition : « le volume de production admis vers l'action ».

**C16. « Exiger que toute affirmation porte son statut ».** « toute note, tout chiffre, tout extrait de code ou toute synthèse […] s'il s'agit d'une exploration provisoire ou d'une affirmation établie, de quelles sources […] elle provient » : le référent de « elle » est flottant (la liste mêle des masculins et des féminins). Proposition : « de quelles sources ou de quels modèles l'élément provient ».

**C17. « Mesurer la probabilité d'échappement ».** « $P(E)$ » puis « $\Pr(\bar{C} \mid E)$ » : la notation des probabilités n'est pas homogène dans une même phrase. À uniformiser si ce n'est pas voulu.

**C18. Paragraphe avant l'encadré « nuance », et l'encadré lui-même.** « L'encadré suivant examine ces trois limites » / « expose à trois illusions » : le même objet est appelé « limites » puis « illusions ». De plus, le paragraphe annonce les trois points presque mot pour mot, ce qui fait doublon avec l'encadré. Proposition : « L'encadré suivant les détaille », et alléger l'énumération qui précède.

**C19. Légende de la figure.** « Chaque niveau consolide plusieurs barrages et laisse les autres à la charge des deux autres niveaux » : la répétition « autres… autres » gêne. Proposition : « …et laisse les barrages restants aux deux autres niveaux ».

**C20. Synthèse niveau 1 et question 5.** « n'a pas de prise sur l'écoute de l'institution » ; « a-t-elle le temps, l'écoute et l'autorité nécessaires » : « l'écoute » remplace « la prise en compte » sans prévenir, et « avoir l'écoute » est peu idiomatique. Proposition : « n'a pas de prise sur la prise en compte par l'institution » ; « a-t-elle le temps, la disponibilité et l'autorité nécessaires ».

## 3. Appréciation globale

Le chapitre est bien construit. L'annonce en trois niveaux, les quatre questions du placement, la synthèse finale et les cinq questions donnent au lecteur des repères solides, et les exemples concrets (brouillard salin, opérateur qui clique sur *Accepter*, TIP, mutants) sont très parlants.

- **Sections les plus accessibles** : le pré-mortem ; « Où » et « Qui » ; « Exiger un statut » ; l'encadré TIP et test par mutation ; les cinq questions finales (à l'ambiguïté de la question 3 près).
- **Sections les moins accessibles** : « Élargir à dessein l'ensemble des mondes possibles » (notations $\Theta$, $b$, $z$, référents flous, aucune limite énoncée) ; l'ouverture du niveau 2 (phrase longue et jargonneuse) ; « Combien » (notations $L/\Delta U$, $p^\ast$, valeur prédictive positive).
- **Point transversal** : les cinq conditions ne sont jamais énumérées avant la figure finale, et sont ensuite rebaptisées « barrages ». Un rappel en une ligne dès la première mention réglerait une bonne partie des gênes.
