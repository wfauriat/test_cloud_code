# Lecture fraîche — chapitre 9 « Sévérité, fausses alertes et probabilité d’échappement »

Lecteur : Opus (première lecture, seul le fichier `chapitres/09-severite-echappement.md` a été lu).

## 1. Résumé de ce que j’ai compris (test de lisibilité)

1. Un test fiable sur un phénomène rare produit surtout de fausses alertes : la valeur prédictive positive (VPP) dépend du taux de base autant que de la sensibilité $s$ et du taux de fausses alertes $f$ (exemple du dépistage : VPP ≈ 15 %).
2. Un accord entre contrôleur et producteur n’est probant que si le contrôleur aurait signalé l’erreur si elle avait existé (sévérité, au sens de Mayo) ; l’accord multiplie la cote de justesse par $(1-f)/(1-s)$, et la sévérité est toujours relative à une classe d’erreurs.
3. Quand le producteur s’améliore face à un contrôleur inchangé, la VPP s’effondre et chaque vraie erreur coûte $1/\mathrm{VPP}$ examens ; la réaction aux alertes ($u$) relève du comportement (appariement des probabilités) ou d’un calcul d’utilité, pas de la règle de Bayes.
4. Le risque résiduel est le produit taux d’erreur × probabilité d’échappement ; les évaluations comparatives ne mesurent que le premier facteur. Le modèle M1 donne $s=(1-c)(1-m)$, échappement $1-su$, risque $P(E)(1-su)$, avec un plancher dû aux causes partagées.
5. Un exemple chiffré (deux scénarios × deux politiques) dégage trois leviers : précision (faible $f$), indépendance, prise en compte ($u$).

## 2. Constats classés par gravité

### Gravité A — compréhension compromise ou contresens possible

**A1. « Indépendance » reçoit trois contenus différents dans le chapitre** (sections « Le piège des fausses alertes », « Risque = … » / exemple quantitatif, « Points clés »).
- §Le piège des fausses alertes : « il ne suffit donc pas qu’il soit indépendant (sensibilité $s$ élevée) » : ici, indépendant = sensibilité élevée.
- Exemple quantitatif : le scénario « *Indépendant et précis* » « garde la même part de causes partagées ($c = 0{,}10$) » et ne baisse que $m$ ; la Lecture : « *L’indépendance élargit ce que le contrôleur peut voir.* Garder les causes partagées à 10 % et ramener l’oubli sur les autres erreurs de 20 % à 10 % » : ici, l’indépendance agit par $m$, alors que $c$ ne bouge pas.
- Points clés : « son indépendance (faible $c$, pour abaisser le plancher d’échappement) » : ici, indépendance = faible $c$.
- Gêne : le lecteur ne sait plus si l’indépendance se mesure par $c$, par $m$ ou par $s$ ; le scénario baptisé « Indépendant » ne change justement pas le paramètre que les Points clés associent à l’indépendance.
- Reformulation minimale (au choix de l’auteur, le sens bouge selon la lecture retenue) : soit renommer le levier de l’exemple (« *La sensibilité élargit ce que le contrôleur peut voir* ») et le scénario, soit aligner les Points clés sur « faible $c$ et faible $m$, c’est-à-dire $s$ élevé ». Je ne tranche pas : les deux lectures sont plausibles.

**A2. §Sévérité d’un contrôle** : « il vaut encore $1$ si le contrôleur répond sans discernement, avec autant de fausses alertes que de vraies détections ($s = f$) ».
- Gêne : $s = f$ est une égalité de *taux*, pas de *nombres* ; or tout le début du chapitre montre justement que les nombres de fausses alertes et de vraies détections diffèrent selon le taux de base. Contresens probable chez un lecteur attentif.
- Reformulation : « …s’il alerte aussi souvent sur une affirmation juste que sur une affirmation fausse ($s = f$) ». Le sens ne bouge pas.

### Gravité B — gêne réelle

**B1. §Sévérité d’un contrôle** : « un contrôle réussi ne déplace la confiance vers $\bar{E}$ que si $\Pr(A \mid E)$ est petit, c’est-à-dire si l’échec du contrôle était probable dans l’hypothèse où l’affirmation aurait été fausse ».
- Gêne : « contrôle réussi » / « échec du contrôle » est ambigu : réussi pour l’affirmation (elle passe) ou pour le contrôleur (il fait son travail) ? Plus loin, « échouer » désigne bien une défaillance du dispositif (« lorsque la comparabilité ou le recours au troisième comparateur échouent »).
- Reformulation : à la première occurrence, « un contrôle réussi (le contrôleur ne signale rien) » et « …si une alerte était probable dans l’hypothèse où l’affirmation aurait été fausse ». Le sens ne bouge pas.

**B2. §Sévérité d’un contrôle** : « alors $\Pr(A \mid E)$ est proche de $\Pr(A \mid \bar{E})$, ou vaut $1$ comme lui. Le rapport de vraisemblance […] est alors égal à $1$ ».
- Gêne : « proche » puis « égal à 1 » ; et « comme lui » suppose que $\Pr(A \mid \bar{E})$ vaut 1, ce qui n’a pas été dit.
- Reformulation : « …est proche de $\Pr(A \mid \bar{E})$, voire égal. Le rapport de vraisemblance […] est alors proche de $1$, ou égal à $1$ ». Le sens ne bouge pas.

**B3. §Le piège des fausses alertes** : « dont le taux d’erreur (introduit au @sec:ch06) vaut $P(E)$ ».
- Gêne : la notation passe de $\Pr(D)$, puis $\Pr(\cdot)$, à $P(E)$ sans explication ; l’équivalence $\Pr(E) = P(E)$ (et $P(\text{faux})$) n’est donnée que deux sections plus loin.
- Reformulation : déplacer ici la précision « $P(E) = \Pr(E)$, noté aussi $P(\text{faux})$ sur les graphiques ».

**B4. §Risque = … et encadré Modèle M1** : « $c$ la part des causes d’erreur que le producteur et le contrôleur partagent » ; « Une erreur n’est signalée […] que si sa cause n’est pas partagée (probabilité $1 - c$) ».
- Gêne : deux lectures plausibles : $c$ = proportion des *types de causes* (décompte) ou $c$ = probabilité qu’une *erreur donnée* relève d’une cause partagée. Le calcul $s = (1-c)(1-m)$ suppose la seconde.
- Reformulation : « la part des erreurs dues à des causes que partagent… ». Je ne tranche pas sur l’intention de l’auteur, mais le calcul s’accorde avec la seconde lecture.

**B5. Encadré Modèle M1 vs exemple quantitatif** : « les causes partagées $c$ forment un plancher qu’aucune diligence […] ne peut percer » vs « ce qui abaisse le plancher d’échappement lorsque chaque alerte est vérifiée (de 28,0 % à 19,0 %) ».
- Gêne : « plancher » désigne d’abord $c$, puis $1 - s$, alors que $c$ reste à 10 % dans les deux scénarios ; le lecteur croit à une contradiction.
- Reformulation : dans la Lecture, « ce qui abaisse l’échappement minimal atteint lorsque chaque alerte est vérifiée ($1 - s$) ». Le sens ne bouge pas.

**B6. §Le piège des fausses alertes** : « qui commet une erreur d’appréciation dans 10 % des cas, indépendamment du producteur — c’est-à-dire qu’il se trompe dans 10 % des cas aussi bien lorsqu’il juge une affirmation juste […] que lorsqu’il examine une affirmation fausse ».
- Gêne : placé juste après « indépendamment du producteur », le « c’est-à-dire » semble définir l’indépendance, alors qu’il précise la symétrie des 10 %.
- Reformulation : « …dans 10 % des cas, aussi bien lorsqu’il juge une affirmation juste (10 % de fausses alertes) que lorsqu’il examine une affirmation fausse (10 % d’oubli), et cela indépendamment du producteur ». Le sens ne bouge pas.

**B7. §Ce que l’on fait des alertes** : « un effondrement de la $\mathrm{VPP}$ pousse vers l’appariement des probabilités et l’érosion de la prise en compte ».
- Gêne : deux lectures : constat comportemental (les opérateurs dérivent) ou conclusion normative du calcul d’utilité (il devient rationnel de moins vérifier). Le paragraphe précédent insiste sur le fait que la règle de Bayes ne dicte pas $u$ ; la phrase brouille cette distinction.
- Reformulation : soit « …rend rationnel de ne plus examiner chaque alerte, et laisse le champ libre à l’appariement des probabilités », soit « …expose à l’appariement des probabilités ». Les deux lectures sont plausibles et je ne tranche pas.

**B8. §Ce que l’on fait des alertes** : « (situation où le seuil $p^\ast$ de l’@eq:ch04-seuil s’effondre vers zéro) ».
- Gêne : possible dépendance : $p^\ast$ n’est pas redéfini, et l’incise interrompt une phrase déjà longue.
- Reformulation : « (le seuil de probabilité au-delà duquel il vaut la peine d’agir, $p^\ast$ au @sec:ch04, est alors presque nul) ».

**B9. Encadré Modèle M1, hypothèse 1** : « *Indépendance des oublis non partagés.* […] le modèle suppose en outre que les désaccords sont comparables et qu’une alerte examinée ($u$) est tranchée exactement ».
- Gêne : on parle de la comparabilité du comparateur et de l’affirmation, pas des « désaccords » ; de plus, l’intitulé n’annonce pas les deux autres hypothèses glissées ici.
- Reformulation : « …que le contrôleur et l’affirmation sont comparables » ; éventuellement, sortir ces deux hypothèses dans une quatrième rubrique.

**B10. §Ce que l’on fait des alertes** : « tout rejeter dès que le contrôleur proteste ».
- Gêne : « tout rejeter » peut se lire comme rejeter les alertes, soit l’inverse du sens voulu. Seule la suite, « gaspille […] un travail juste », lève l’ambiguïté.
- Reformulation : « rejeter le travail du producteur dès que le contrôleur proteste ». Le sens ne bouge pas.

### Gravité C — confort / style

**C1. Introduction** : « ce chapitre donne une mesure quantitative à la détection et à l’échappement ». Ce n’est pas idiomatique. Proposition : « propose une mesure quantitative de la détection et de l’échappement ». La dernière phrase de l’introduction (quatre propositions et une incise finale) gagnerait aussi à être coupée avant « — refermant ainsi ».

**C2. Introduction** : « un comparateur qui existe, se trompe autrement qu’elle, lui est comparable ». Une affirmation ne « se trompe » pas, c’est son producteur qui se trompe. Proposition : « dont les erreurs diffèrent de celles du producteur ».

**C3. §Taux de base (encadré)** : « Tant que le taux de base reste faible devant le rapport $f/s$ ». « Faible devant » suggère « négligeable », alors que la condition énoncée est une simple infériorité. Proposition : « reste inférieur au rapport $f/s$ ». Lecture d’intention à vérifier par l’auteur.

**C4. §Sévérité d’un contrôle** : « un tel accord ne prouve rien tant que le contrôleur n’avait pas réellement la possibilité ». La concordance des temps est bancale. Proposition : « …ne prouve rien si le contrôleur n’avait pas réellement la possibilité ».

**C5. §Sévérité d’un contrôle** : « multiplie la cote que l’affirmation soit juste ». C’est un calque de « the odds that ». Proposition : « multiplie la cote en faveur de la justesse de l’affirmation ».

**C6. §Sévérité d’un contrôle** : « que si $\Pr(A \mid E)$ est petit ». Petit par rapport à quoi ? Le multiplicateur dépend du rapport avec $\Pr(A \mid \bar{E})$. Proposition : « petit devant $\Pr(A \mid \bar{E})$ ».

**C7. §Le piège des fausses alertes** : « le producteur a tort et le relecteur a raison dans $0{,}01 \times (1 - 0{,}10) = 0{,}009$, soit 0,9 % ». « Dans 0,009 » n’est pas idiomatique. Proposition : « dans une proportion $0{,}01 \times … = 0{,}009$ des dossiers, soit 0,9 % ».

**C8. §Le piège des fausses alertes** : « Ce renversement crée un piège ». Le référent est flou : quel renversement ? Proposition : « Ce renversement (le désaccord accuse le plus souvent le relecteur, non le producteur) crée… ».

**C9. §Le piège des fausses alertes / Points clés** : « il doit aussi être *précis* (…$f$ doit baisser) » ; « un producteur moins précis mais mieux contrôlé ». « Précis » désigne tantôt un faible $f$ (pour le contrôleur), tantôt l’exactitude (pour le producteur). De plus, un lecteur familier du vocabulaire de la classification entend « précision » au sens de VPP (risque de faux ami). Proposition : dans les Points clés, « un producteur moins exact ».

**C10. §Ce que l’on fait des alertes** : « Devant une alerte dont on sait que neuf fois sur dix elle est fausse ». La reprise par « elle » est pléonastique. Proposition : « dont on sait qu’elle est fausse neuf fois sur dix ».

**C11. §Ce que l’on fait des alertes** : « La prise en compte (@def:prise-en-compte) — que nous noterons $u \in [0,1]$, la proportion des alertes… ». L’apposition est maladroite. Proposition : « …— que nous noterons $u \in [0,1]$ et qui désigne la proportion… ».

**C12. §Risque = …** : « tant qu’elle reste sur la table ». En français, « sur la table » signifie plutôt « en discussion ». Proposition : « tant qu’elle reste sur le papier ». Par ailleurs, « Parce que le monde répond à l’action et non à la représentation (@sec:ch02) » est une formule elliptique qui dépend du chapitre 2 (possible dépendance).

**C13. §Ce que l’on fait des alertes / §Risque = …** : « alertes effectivement examinées et suivies d’effet » puis « une affirmation […] fausse et suivie d’effet ». La même expression sert pour deux objets distincts. Proposition, pour l’affirmation : « fausse et passée dans l’action ».

**C14. §Risque = …** : « la probabilité que le contrôleur oublie une erreur sur les autres causes ($1 - c$) ». La parenthèse peut se lire comme une valeur de $m$. Proposition : « sur les autres causes (fraction $1 - c$) ».

**C15. §Risque = … puis encadré M1** : le paragraphe qui précède l’encadré en donne déjà presque tout le contenu ($c$, $m$, $s$, $u$, $1 - su$, risque). Cette redondance alourdit la lecture. Proposition : réduire ce paragraphe à l’annonce de l’encadré.

**C16. Encadré M1** : « ($B_{\text{cmp}} = \emptyset$ dans l’@eq:ch08-croise-angle-mort) ». C’est une notation non rappelée (possible dépendance). Proposition : ajouter « (aucune erreur due à la comparaison elle-même) ».

**C17. Exemple quantitatif, Mise en place** : « lorsque le taux d’erreur du producteur diminue sur plusieurs ordres de grandeur, face à l’absence de contrôleur ». La fin de phrase est obscure. Proposition : « …, comparés au cas sans contrôleur ».

**C18. Exemple quantitatif, Lecture** : « la courbe bleue ($u = 1$) reste horizontale à 28,0 % ». Cela n’est vrai que sur le panneau de gauche, que la phrase ne précise qu’ensuite. Proposition : « sur le panneau de gauche, la courbe bleue… ».

**C19. Encadré Nuance** : « sans devenir supérieur au risque sans contrôleur ni croître à lui seul » ; « sous l’effet d’une amélioration apparente ». Le référent de « à lui seul » est flou (le risque ? le contrôleur ?). « Apparente » peut se lire comme « illusoire » ou comme « visible ». Proposition : « ni croître du seul fait de la baisse de $P(E)$ » ; « sous l’effet d’une baisse de $P(E)$ ». Deux lectures sont possibles pour « apparente », je ne tranche pas.

**C20. Conclusion de partie** : « une théorie générale du contrôle des représentations finies, édifiée hors de l’informatique récente ». Le jargon (« représentations finies ») n’est pas rappelé, et « édifiée hors de » est ambigu (sans recours à ? en dehors du champ de ?). Le récapitulatif « Des trois incertitudes et de la mesure d’une barre d’erreur… » enchaîne aussi des notions non présentées dans ce chapitre (possibles dépendances). Proposition : « …édifiée sans recourir à l’informatique récente ».

**C21. Points clés** : « une décision d’utilité espérée qui paie presque toujours devant des enjeux élevés et irréversibles ». « Presque toujours » et « irréversibles » n’apparaissent pas dans le corps du texte, qui dit « justifie amplement » pour une « décision unique aux enjeux élevés ». Proposition : aligner la formulation sur celle du corps.

**C22. Encadré M1 et passim** : « le contrôleur oublie tout de même une erreur », « taux d’oubli ». « Oublier » pour « ne pas détecter » est légèrement impropre. Proposition (facultative) : « laisse passer » / « taux de manqués ». C’est un choix de voix, que l’auteur peut garder.

## 3. Appréciation globale

Les sections les plus accessibles sont « Taux de base et valeur prédictive positive » (exemple des mille personnes, très clair, calculs vérifiés et justes) et « Le piège des fausses alertes » (calcul des désaccords limpide). La décomposition « Risque = taux d’erreur × échappement », avec ses deux systèmes chiffrés, est également très efficace. Tous les chiffres de l’exemple quantitatif (VPP 61,5 % et 76,8 %, échappements 55,7 / 28,0 / 37,8 / 19,0 %) se recalculent correctement.

Les sections les moins accessibles sont « Sévérité d’un contrôle » (ambiguïté réussi/échec, passage $s = f$ formulé en nombres) et surtout l’ensemble formé par l’encadré M1, l’exemple quantitatif et les Points clés. C’est là que le vocabulaire flotte : « indépendance », « plancher », « précis » et le sens exact de $c$ y reçoivent des contenus différents, et le paragraphe d’annonce double l’encadré. Le défaut principal du chapitre est l’incohérence terminologique autour de l’indépendance (A1), plus que la langue, qui reste globalement idiomatique.
