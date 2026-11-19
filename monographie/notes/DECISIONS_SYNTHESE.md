# Décisions sur les arbitrages de la synthèse

Journal des décisions prises sur les points du groupe 2 de `notes/SYNTHESE_A_TRANCHER.md`, au fil d'une revue interactive avec l'auteur. Pour chaque point : la décision et sa portée. Un point « ouvert » est réservé à une discussion ultérieure. Un point « bloquant » doit être tranché avant toute application, parce qu'il touche de nombreux fichiers.

Aucune décision n'est encore appliquée au texte.

## Politiques éditoriales (§ 3.3)

- **N1. La notation $(\dots)$ en texte courant.** *Adopté*, après discussion. L'auteur juge la notation, reprise de la perspective de Pearl, trop proche de l'exposé oral d'origine. « Le reste » et « non-spécifié » ont été écartés (collisions avec le « remainder » de l'article et avec « composant spécifié »). La règle retenue :
  - dans les formules affichées, $A \cap (\dots) \rightarrow B$ ne change pas : les points de suspension montrent que la liste est ouverte ;
  - au ch. 1, une phrase nomme la parenthèse et donne la lettre : « l'**arrière-plan tacite**, noté aussi $\mathcal{T}$ dans le texte » ;
  - en prose, « l'arrière-plan tacite $\mathcal{T}$ » à la première mention de chaque chapitre, puis le nom seul. La lettre seule n'apparaît que là où une phrase manipule l'arrière-plan (« une variation de $\mathcal{T}$ »). Jamais de « $(\dots)$ » nu en prose ;
  - « arrière-plan tacite » devient un terme du registre, introduit en gras au ch. 1, et la ligne des notations est mise à jour ;
  - V19 est réglé du même coup : « arrière-plan tacite » et « conditions tacites » remplacent « conditions tues », « arrière-plan tu », « conditions sous-entendues » et « arrière-plan non énoncé ».

  Portée : le registre et une quinzaine de passages répartis dans 13 fichiers. À surveiller : au ch. 2, l'encadré causal emploie $T$ pour la variable d'intervention ($\mathrm{do}(T = t)$), dont la forme est proche de $\mathcal{T}$. On pourrait la renommer, sans urgence.

## Formulations du registre (§ 3.1)

- **R1. « ne vaut que » (déduction, induction).** *Adopté.* « ne garantit sa conclusion que si… » sur la page de la partie 1 ; « ne garantissent leur conclusion que « pourvu que »… » dans le registre, les PC du ch. 1 et le chapeau du ch. 2.
- **R2. « spécification finie ».** *Adopté.* Le terme est gardé, avec une glose unique à la définition du ch. 2 : « finie, c'est-à-dire bornée et donc incomplète ».
- **R4. Sévérité.** *Adopté.*
  - Le registre, la page de la partie 2, le ch. 9 et la conclusion disent : « Un contrôle passé sans alerte n'est probant que dans la mesure où il aurait donné l'alerte si l'affirmation avait été fausse (Mayo) ».
  - Au ch. 9, une phrase est ajoutée après la définition : « On la mesure par $\Pr(\bar A \mid E)$, la probabilité que le contrôle donne l'alerte quand l'affirmation est fausse. »
- **R5. Comparateur : « un texte fixé à l'avance ».** *Ouvert*, réservé à la discussion. Non bloquant.
- **R6. Vérification en amont.** *Adopté.* Dans le registre et au ch. 10 : « Contrôle d'un composant fait une fois, par rapport à sa spécification, et qui porte sur le composant plutôt que sur chacune de ses sorties : ce qu'il établit vaut pour toutes ses exécutions futures. » Dans les PC du ch. 10 : « peut contrôler le composant une fois pour toutes ».
- **R3. « décision unique ».** *Adopté.* Nouvelle définition, dans le registre et au ch. 4 : « décision prise sans série d'essais comparables, si bien qu'une issue malheureuse ne peut être compensée par d'autres cas : la réponse du monde n'arrive qu'après l'acte, trop tard pour le corriger ».
- **N2. Rappels de termes hors de leur chapitre.** *Adopté.* Un rappel bref par chapitre est autorisé, repris mot pour mot de la définition du registre, sans gras. Il concerne les termes introduits au moins deux parties plus tôt, et les chapitres d'entrée des parcours de lecture du ch. 0. Environ 25 points deviennent applicables.
- **N3. Modèles M1 à M3.** *Adopté.* On garde la numérotation de la spec. La série est présentée une fois au ch. 0 (§ Architecture), et chaque première mention dans un chapitre est accompagnée de quelques mots de description (« le modèle M1, des angles morts et de l'échappement, @sec:ch08 »). Huit fichiers.
- **N4. $P(E)$, $\Pr(E)$, $P(\text{faux})$.** *Adopté.* Les trois notations sont gardées. L'équivalence est posée à la première occurrence aux ch. 6, 9 et 16. En prose, $c$ s'écrit en pourcentage, comme dans les tableaux.
