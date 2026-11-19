# Chapitre d’essai de la chaîne de production {#sec:ch00 .corps}

Ce fichier vérifie chaque convention : blocs, énoncés, renvois, équations, figures, tableaux générés, marqueurs « à vérifier » et typographie française. Il ne fait pas partie du livre.

## Renvois et typographie {#sec:ch00-renvois}

Le seuil est donné par @eq:ch00-seuil ; la @prop:essai en tire une conséquence, et la @def:essai-seuil fixe le vocabulaire. La figure [-@fig:ch00-seuil] et le @tbl:ch00-seuils montrent les mêmes nombres. Voir aussi la @sec:ch00-blocs et l’annexe [-@sec:annexe-essai].

Typographie : « guillemets », deux-points : point-virgule ; exclamation ! interrogation ? et pourcentage 5 % ou 0,1 %.

Une référence à confirmer [@A-VERIFIER: Savage 1954, chapitre sur l’utilité] et une étiquette inconnue @fig:ch00-inexistante pour tester l’alerte.

Citations : une référence vérifiée [@fauriat2026frame], une référence candidate [@savage1954], et une clé inconnue [@inconnu2099] pour tester l’alerte.

$$ p^\ast = \frac{\Delta U}{\Delta U + L} = \frac{1}{1 + L/\Delta U} $$ {#eq:ch00-seuil}

::: {.definition #def:essai-seuil titre="Seuil de décision"}
Le **seuil p∗** est la probabilité d’échec au-delà de laquelle l’option risquée cesse d’être payante.
:::

::: {.proposition #prop:essai titre="Le seuil s’effondre quand l’enjeu croît" statut="résultat sous hypothèses"}
Quand le rapport $L/\Delta U$ tend vers l’infini, le seuil $p^\ast$ tend vers $0$.
:::

## Les six blocs {#sec:ch00-blocs}

::: {.outils titre="L’utilité espérée subjective"}
On choisit l’acte dont l’utilité espérée, calculée avec ses propres probabilités, est la plus élevée.
:::

::: {.formel titre="Dérivation du seuil"}
On part si et seulement si $(1-p)\,U_{\text{gain}} + p\,U_{\text{casse}} > U_{\text{sûr}}$.
:::

::: {.exemple-quantitatif titre="Le seuil en fonction de l’enjeu"}
**Mise en place.** Trois rapports des enjeux : 25, 100 et 10 000.

![Seuil p∗ en fonction du rapport des enjeux, avec M. X et M. Y.](tests/figures/essai-seuil.pdf){#fig:ch00-seuil width=85%}

**Calcul.**

::: {.inclure fichier="tests/tableaux/essai-seuil.md"}
:::

**Lecture.** Pour un rapport de 25, le seuil vaut 3,85 % ; pour 10 000, il tombe à 0,0100 %.
:::

::: {.cas titre="Mars Climate Orbiter" date="1999"}
Une erreur d’unité à une interface [@A-VERIFIER: rapport de la commission d’enquête, 1999].
:::

::: {.nuance titre="Ce que le seuil ne dit pas"}
Le seuil se rapporte à ce que croit le décideur, non au risque réel.
:::

::: {.question}
Pour votre prochain déploiement irréversible, quel est le rapport $L/\Delta U$ ?
:::

![Figure volontairement absente.](figures/ch00-absente.pdf){#fig:ch00-absente}

## Points clés {.points-cles}

- La chaîne produit le PDF et le HTML à partir d’une seule source.
- Les renvois, énoncés et blocs sont numérotés de la même manière dans les deux sorties.

# Annexe d’essai {#sec:annexe-essai .annexes}

Une annexe est numérotée par une lettre.
