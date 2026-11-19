# Content Spec — Global (read this before any Part file)

**Status:** v1.0 (derived from `course_outline.md` v0.1 and spec §13).
**Language:** English, for precision. The monograph itself is written in idiomatic French (spec §13.6).
**Precedence when documents disagree:**
1. `authoring_conventions.md` (how to write);
2. this content spec (what to say);
3. `course_outline.md` (where it goes);
4. `content_spec/source_threads_en.md` (raw material; never cited).

**Files:**
- `00_global.md`: argument line, statements, formal models, terminology, notation, parameters, references, pitfalls;
- `part0_front.md`: preface and Chapter 0;
- `part1.md` … `part5.md`: Parts I–V;
- `part9_back.md`: conclusion and appendices;
- `source_threads_en.md`: raw material keyed by map thread id.

---

## 1. The Argument Line (what the whole book establishes)

Every chapter serves one step of this line. A builder must know which step their chapter carries and which steps it relies on.

| Step | Claim | Established in |
| :-- | :-- | :-- |
| S1 | We act on a finite **picture** of the world; the world answers the action, not the picture. Decisions are made on beliefs, and they shape outcomes. | ch. 2, 4 |
| S2 | Every usable rule hides an open background `(…)`; choosing what to state is choosing a **frame**. Rigour inside a frame (deduction as much as induction) never certifies the frame. | ch. 2 |
| S3 | Probability is best read as judgment over possible worlds. One outcome barely grades a forecaster; only repetition (calibration) can. | ch. 3 |
| S4 | Under SEU, the risky one-shot option pays only below p∗ = ΔU/(ΔU+L), which tends to 0 as stakes grow. The world does not consult our belief. | ch. 4 |
| S5 | Quantified uncertainty is disagreement within an admitted set (**P1**). What the frame omits produces no disagreement, hence no error bar. | ch. 5 |
| S6 | An error is detected only by a comparator that exists, can fail differently, is comparable, arrives in time, and is heeded (**P2**). Otherwise the error escapes. | ch. 6 |
| S7 | The frame is a common cause of all checks computed from it (**P3a**). Observations can reveal an omitted factor only if it varied, and only through recorded variables (**P3b**). No meta-procedure escapes the regress; new relevance enters only from outside. | ch. 7 |
| S8 | Independence is relative to a class of errors and paid for in comparability (**P4**). Chains unite blind spots; cross-checks intersect them (**P5**). Laundering at handoffs turns compositions into chains. | ch. 8 |
| S9 | A passing check is evidence only if it could have failed (severity). As errors become rare, a fixed checker's alarms become mostly false. Risk = error rate × escape probability, and benchmarks measure only the first factor. | ch. 9 |
| S10 | Classical software earned the right to be forgotten: written contracts allow verification once, in advance, and failures have an address. | ch. 10 |
| S11 | Machine learning moves the specification into data. It gains reach and spends the guarantee and legibility. Fluent falsehood breaks no contract. Steering is not specifying. | ch. 11 |
| S12 | At the top of the stack three properties flip together (promise, failure presentation, post-mortem). Verification must move to outputs. Competence is jagged. Calibrated generation must invent rare facts; re-asking catches guessing errors, not consistent ones. | ch. 12 |
| S13 | Synthesis: errors sort on two axes, where the cause lies and whether a comparator disagrees. Learned components crowd the inside-and-silent cell. Comparators come from four sources, and automation reshapes each. | ch. 13 |
| S14 | Automation chains checks (agents: errors execute), removes them (lost friction, lost tell, collapsed signals, prompt traps) and correlates them (shared models raise escape probability, provenance laundering, throughput squeeze). | ch. 14–16 |
| S15 | Practice: decide one-shot acts with a deliberate humility buffer and a gate, explore in sandboxes, and ask for the conditions of any confident number. Organize checks on three levels: attitude, placement, organization (with measured escape). | ch. 17–18 |
| S16 | The method applies to the book itself. Its statements carry statuses, its tensions are listed, and it stands as a working approach. | Conclusion |

---

## 2. Stance (applies to every chapter)

- **Practical first.** The aim is the right approach to acting on the world through a picture. Formality serves rigour and consistency; it is never an end.
- **Working stance.** Claims are best working assumptions in the Bayesian sense (*faute de mieux*), with their tensions and risks named. Exposing unavoidable tensions is a goal, not a weakness.
- **Self-consistency.** The book applies its principles to itself. It never claims validation from its design process, and it marks the status of its statements.
- **Register.** Explanatory and precise; neither popular-science hype nor dry formalism. Gist first, formal second (spec §1.2).

---

## 3. Statements (canonical wording, status, justification, robustness)

French titles are proposals; the content must be preserved. Slugs are fixed (authoring conventions §5).

### P1 `prop:desaccord` (ch. 5)
- **EN:** A quantitative statement of uncertainty summarizes how far the members of a specified set of alternatives disagree. An alternative that was never admitted contributes no disagreement.
- **FR title (proposal):** « L'incertitude n'est qu'un désaccord mesuré »
- **Status:** *résultat sous hypothèses*.
- **Justification:** every quantified uncertainty is computed from spread within an admitted ensemble (replicates; posterior draws, ensemble members, bootstrap fits). The law of total variance over Θ makes this explicit: both terms are averages over the admitted set.
- **Robustness note:** a factor that varied unrecorded during data collection *is* in the bars, as scatter attributed to chance. "Silent" means unattributed, not always absent. Only a factor that stayed constant leaves no trace.

### P2 `prop:comparateur` (ch. 6)
- **EN:** An error is detected only when a claim is compared with something expected to agree with it (a comparator), the comparison shows a disagreement, and someone registers it.
- **FR title:** « Pas de détection sans comparateur »
- **Status:** *définition* (close to a tautology). Its usefulness comes from the five conditions it unfolds into: existence, difference, comparability, timeliness, uptake.
- **Robustness note:** say plainly that the statement is near-definitional, and that the substance lies in the conditions and in their independent failure modes.

### P3 `prop:cause-commune` (ch. 7)
- **EN:**
  - (a) A comparator computed from the frame's own content cannot detect an error caused by a factor the frame omits.
  - (b) Observations can, but only if that factor varied while they were taken, and only through what the frame records.
- **FR title:** « Le cadre est une cause commune »
- **Status:** (a) *résultat sous hypothèses*; (b) *résultat sous hypothèses*, illustrated by *constats empiriques* (Google Flu Trends; lab vs field).
- **Justification (a):** model M3 (§4).
- **Robustness note:**
  - (a) holds conditional on the represented variables x. Real comparators rarely condition that cleanly.
  - For learned models, a factor may be represented but not mobilized ("salience omission", ch. 12). There (a) holds only for comparators that reuse the same weights and prompt.
  - Self-checks remain useful against slips; P3a is about omitted factors only.

### P4 `prop:independance` (ch. 8)
- **EN:** A comparator helps against a class of errors to the extent that their cause affects it differently. What claim and comparator share, neither can check in the other; yet they must share something to be compared. Independence is therefore relative, and paid for in comparability.
- **FR title:** « L'indépendance est relative, et se paie en comparabilité »
- **Status:** first sentence *définition*; the trade-off (cost tends to rise with independence) *hypothèse de travail*.
- **Robustness note:** "cost rises with independence" is a strong tendency, not a law. Cheap and different comparators exist: a naive outsider's question, an order of magnitude, a conservation law, a model from another family. Their cost lies in comparability: making the objection land.

### P5 `prop:chaines` (ch. 8)
- **EN:** In a chain, the blind spot contains every component's blind spot plus the errors born at interfaces. In a cross-check, it shrinks to what both components share, under perfect comparison and uptake.
- **FR title:** « Une chaîne cumule les angles morts ; un contrôle croisé ne garde que ceux qui sont communs »
- **Status:** *résultat sous hypothèses* (independence of misses; perfect comparison and uptake).
- **Formal statement:** model M1.
- **Robustness note:**
  - With an imperfect comparison, the correct form is `B₁ ∩ (B₂ ∪ B_cmp)`, not `(B₁ ∩ B₂) ∪ B_cmp`.
  - The trade-off (the shared blind spot shrinks with distance while the comparison blind spot grows) *suggests* an optimal reviewer distance but does not derive one. Say so.

---

## 4. Formal Models (where formality carries the argument; spec §13.2)

Builders of the named chapters must state these models with explicit assumptions. Elsewhere, formal sketches suffice.

**M1. Blind spots and escape (ch. 8–9; reused in ch. 14, 16).**
- **Setup:** error causes form a set. Component i misses errors of cause k with probability m_{ik}. A claim is wrong with probability P(E).
- **Chain:** an error escapes if it escapes any link; interface errors belong to no link.
- **Cross-check:** an error escapes only if all checkers miss it, or if the comparison cannot express it.
- **Independent misses:** P(escape) = Π m_i. For a cause shared by all checkers, P(escape) = 1 whatever their number.
- **Checker model of ch. 9:**
  - a fraction c of the producer's error causes is shared with the checker (always missed);
  - on the other errors the checker misses with probability m;
  - false-alarm rate f;
  - sensitivity s = (1 − c)(1 − m);
  - PPV = P(E)s / [P(E)s + (1 − P(E))f];
  - uptake u = PPV under probability matching, u = 1 if every flag is investigated;
  - escape = 1 − s·u; risk = P(E)·escape.
- **Assumptions to state:** independence of the non-shared misses, a stationary error rate, uptake modelled as probability matching (a behavioural assumption, cited, not derived from Bayes).

**M2. Deciding with an unrepresented variable (ch. 4 baseline; ch. 17 full).**
- **Baseline (ch. 4):** SEU with the reinforced boat as a sure baseline. Go iff (1 − p)U_win + pU_fail > U_safe, i.e. p < p∗ = ΔU/(ΔU + L) = 1/(1 + L/ΔU).
- **Extension (ch. 17):** the world adds an omitted failure chance z, independent of p, so the world's probability is p_w = 1 − (1 − p)(1 − z).
  - The decider decides on p + b, where b is a deliberate buffer.
  - The decider cannot condition on z, which is outside the picture.
  - Four cases: correct go, silent trap (go while p_w ≥ p∗), saved by the buffer, over-caution (the buffer's price when z = 0).
- **Key point to state:** b is a judgment, not an estimate of z. Turning z into a readable dial would contradict P1/P3.

**M3. The frame as common cause (ch. 7).**
- **Setup:** the outcome is g(x, z), with x represented and z omitted. Claim f₁(x) and comparator f₂(x) are both computed in the frame.
- **Argument:** agreement between f₁ and f₂ is a function of x alone. Given x, the likelihood ratio of "agree" for "error large" vs "error small" equals 1.
- **Assumptions to state:** both claim and comparator are functions of the recorded variables only; z is not recorded.
- **Limit to state:** if z varied during data collection, it enters as unexplained scatter (P3b).

---

## 5. Terminology Register (origin)

**Superseded by `monographie/commun/registre_termes.md`.** That file is the French register and the source of truth: fixed French terms, definitions in French, chapter of introduction, notation. The table below is kept as the English origin of that register.

One French term per concept. **First** = the chapter where the term is introduced in bold and defined. No synonyms for the technical sense.

| EN concept | FR term (fixed) | Short definition | First | Label |
| :-- | :-- | :-- | :-- | :-- |
| picture | représentation | the constructed representation an agent acts on | 2 | `def:representation` |
| frame | cadre | the finite specification inference works within (variables, categories, model class, objective) | 2 | `def:cadre` |
| frame problem | problème du cadre | (historical AI sense, McCarthy–Hayes; broader sense used here) | 2 | |
| deduction / induction | déduction / induction | | 1 | |
| possible worlds | mondes possibles | situations compatible with what is known | 3 | |
| reasoning in reverse | raisonner à l'envers | asking which hidden variation would flip a conclusion | 3 | |
| likelihood ratio | rapport de vraisemblance | | 1 | |
| logarithmic score | score logarithmique | surprise, −ln Pr(outcome) | 1 | |
| calibration (confidence sense) | calibration | stated probabilities match observed frequencies | 3 | |
| generative calibration | calibration générative | model's distribution over statements matches training distribution | 12 | |
| subjective expected utility | utilité espérée subjective (UES) | | 4 | |
| threshold p∗ | seuil p∗ | | 4 | `eq:ch04-seuil` |
| stakes ratio L/ΔU | rapport des enjeux L/ΔU | | 4 | |
| one-shot decision | décision unique | | 4 | |
| aleatory / epistemic / ontological uncertainty | incertitude aléatoire / épistémique / ontologique | | 5 | |
| admitted set (of alternatives) | ensemble des alternatives admises | | 5 | |
| claim | affirmation | asserts a matter of fact (model output, forecast, measurement report) | 6 | `def:affirmation` |
| check | contrôle | comparison of a claim with a comparator expected to agree | 6 | `def:controle` |
| comparator | comparateur | what a claim is compared with: another claim, a statement fixed in advance, an observation | 6 | `def:comparateur` |
| fail differently | se tromper autrement | for a given cause, the cause does not make both wrong the same way | 6 | |
| uptake | prise en compte | someone registers a disagreement and has the standing to act | 6 | `def:prise-en-compte` |
| error rate | taux d'erreur | P(claim wrong) | 6 | |
| escape probability | probabilité d'échappement | P(wrong claim reaches action uncontradicted) | 6 | `def:echappement` |
| common-mode failure | défaillance de mode commun | | 7 | |
| distribution shift | dérive de distribution | | 7 | |
| structural / salience omission | omission structurelle / omission de saillance | | 12 | |
| blind spot | angle mort | set of error causes a component cannot register | 8 | `def:angle-mort` |
| chain / cross-check | chaîne / contrôle croisé | series / parallel composition of checks | 8 | |
| laundering | blanchiment | dropping a claim's conditions at a handoff | 8 | `def:blanchiment` |
| provenance laundering | blanchiment de provenance | | 16 | |
| producer / checker | producteur / contrôleur | (producer: whoever produces the claim; *auteur* acceptable in plain prose) | 8 | |
| severity | sévérité | a pass is evidence only if the check could have failed (Mayo) | 9 | `def:severite` |
| base rate | taux de base | | 9 | |
| sensitivity / false-alarm rate | sensibilité / taux de fausses alertes | | 9 | |
| positive predictive value | valeur prédictive positive (VPP) | share of alarms that are real errors | 9 | |
| probability matching | appariement des probabilités | | 9 | |
| specified component (map: "stated") | composant spécifié | rules written, checkable specification (contract) | 10 | `def:composant-specifie` |
| learned component | composant appris | rules fitted to examples, existing only as parameters | 11 | `def:composant-appris` |
| contract; pre-/postcondition | contrat ; précondition / postcondition | | 10 | |
| front-loaded verification | vérification en amont | check once against the statement, covering all runs | 10 | |
| address (of a failure) | adresse (d'une défaillance) | | 10 | |
| prompt | consigne (*prompt* glossed once) | | 11 | |
| benchmark | test de référence (*benchmark* glossed once) | | 11 | |
| steering | orienter (un modèle) | | 11 | |
| regime flip / regime boundary | changement de régime / frontière de régime | | 12 | |
| jagged frontier | frontière en dents de scie | | 12 | |
| signalled / silent error | erreur signalée / silencieuse | | 13 | |
| verification / validation | vérification / validation | solving the stated problem right / stating the right problem | 13 | |
| agent | agent | | 14 | |
| tell | signe révélateur | visible sign of a producer's uncertainty | 15 | |
| costly signal; pooling equilibrium | signal coûteux ; équilibre mélangeant | | 15 | |
| seeded errors | erreurs injectées | | 18 | |
| track record | historique | | 3 (first use), 18 | |
| humility buffer | marge d'humilité | | 17 | |
| sandbox / gate | bac à sable / verrou | | 17 | `def:bac-a-sable`, `def:verrou` |
| pre-mortem | pré-mortem | | 18 | |

---

## 6. Notation (to be copied into Appendix C)

| Symbol | Meaning | First |
| :-- | :-- | :-- |
| Pr(·), Pr(B \| A) | probability, conditional probability | 1 |
| X, x | represented variables / their values | 2 |
| z | omitted factor (outside the frame) | 5 (informal), 7 (M3) |
| Θ, θ | admitted set of hypotheses / one hypothesis | 5 |
| p | believed failure probability | 4 |
| L, ΔU | loss if failure, gain if success (vs. safe option) | 4 |
| p∗ | decision threshold ΔU/(ΔU+L) | 4 |
| b | humility buffer | 17 |
| p_w | the world's failure probability 1 − (1 − p)(1 − z) | 17 |
| P(E) | error rate | 6, 9 |
| c, m, f, s | shared-cause share, miss rate on other errors, false-alarm rate, sensitivity | 9 |
| u | uptake | 9 |
| B_i, B_cmp | blind spot of component i, of the comparison | 8 |
| N, q | number of chain steps, shared omitted factor (chain example) | 8 |

Decimal comma in the French text (`0{,}05` in math).

---

## 7. Canonical Parameters and Values (to be frozen in `commun/parametres.py`; reproduced in Appendix D)

All values were computed from the formulas in §4 and checked against the interactive labs. Figures and tables must reproduce them exactly.

**log-score (ch. 3):**
- p_X = 5 %, p_Y = 0.1 %.
- Boat breaks: −ln p = 3.00 (X) and 6.91 (Y); likelihood ratio 50 in favour of X.
- Boat holds: −ln(1 − p) = 0.051 (X) and 0.001 (Y); ratio 0.95 / 0.999 = 0.951.

**seu-a (ch. 4) and seu-b (ch. 17):** L/ΔU = 25, so p∗ = 1/26 = 3.85 %.

| Scenario | L/ΔU | p | b | z | p + b | Decision | p_w | Outcome |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Mr Y | 25 | 0.1 % | 0 | 0 | 0.1 % | go | 0.1 % | correct go |
| Mr X | 25 | 5 % | 0 | 0 | 5 % | no-go | 5 % | no-go on own estimate |
| Mr Y + unseen crack | 25 | 0.1 % | 0 | 8 % | 0.1 % | go | 8.09 % | **silent trap** |
| … plus buffer | 25 | 0.1 % | 4 % | 8 % | 4.1 % | no-go | 8.09 % | saved by the buffer |
| Russian roulette | 10 000 | 0.001 % | 0 | 1/6 | 0.001 % | go | 16.7 % | silent trap; p∗ = 0.0100 % |

- seu-a uses the rows without z or b.
- seu-b adds an over-caution row: z = 0, b = 4 %, so p + b = 4.1 % ≥ p∗: no-go, and the buffer's price is the forgone gain.

**chain-a (ch. 8) and chain-b (ch. 14):** per-step error p = 6 %; the peer misses with probability p.

| N | q | Unchecked chain | Cross-checked | Independent part (unchecked → checked) | Share of residual failures involving q |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 4 | 0 | 21.9 % | 1.43 % | 21.9 % → 1.43 % | — |
| 4 | 3 % | 24.3 % | 4.39 % | 21.9 % → 1.43 % | 68.3 % |
| 12 | 0 | 52.4 % | 4.24 % | 52.4 % → 4.24 % | — |
| 12 | 3 % | 53.8 % | 7.11 % | 52.4 % → 4.24 % | 42.2 % |

**escape-a (ch. 9) and escape-b (ch. 16):** "PPV" = flags heeded at the PPV rate; "all" = every flag investigated.

| Preset | P(E) | c | m | f | s | PPV | Escape (PPV / all) | Risk (PPV / all) vs P(E) | 1/PPV |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| peers | 10 % | 10 % | 20 % | 5 % | 72 % | 61.5 % | 55.7 % / 28.0 % | 5.57 % / 2.80 % vs 10 % | 1.6 |
| shared model | 2 % | 60 % | 20 % | 5 % | 32 % | 11.6 % | 96.3 % / 68.0 % | 1.93 % / 1.36 % vs 2 % | 8.7 |
| shared + precise | 2 % | 60 % | 20 % | 0.5 % | 32 % | 56.6 % | 81.9 % / 68.0 % | 1.64 % / 1.36 % vs 2 % | 1.8 |
| independent + precise | 2 % | 10 % | 10 % | 0.5 % | 81 % | 76.8 % | 37.8 % / 19.0 % | 0.76 % / 0.38 % vs 2 % | 1.3 |

- escape-a uses *peers*, with *independent + precise* for contrast.
- escape-b uses *shared model* and *shared + precise* to separate the correlation effect from the false-alarm effect.

**plausibility (ch. 12):** five samples per question; answer distributions as in the lab.

| Mode | Distribution (✓ = right) | P(one answer wrong) | Severity (if wrong, P(5 answers disagree)) | P(flag \| right) |
| :-- | :-- | :-- | :-- | :-- |
| known fact (Eiffel Tower) | Paris ✓ 97, Lyon 2, Marseille 1 | 3 % | ≈ 100 % | 11.5 % |
| arbitrary rare fact (birth date) | 22, 20, 18 ✓, 16, 14, 10 (six dates) | 82 % | 99.9 % | 99.9 % |
| popular misconception (closest planet on average) | Venus 88, Mercury ✓ 9, Mars 3 | 91 % | 42.0 % | ≈ 100 % |

**Plain-arithmetic examples:**
- *Teaser (ch. 0, 9):* 1 % error × 90 % escape = 0.9 %, vs 10 % × 1 % = 0.1 %, a factor of nine.
- *Screening (ch. 9):* prevalence 1 %, sensitivity 90 %, false-positive rate 5 %, so PPV = 15.4 %.
- *Producer/reviewer (ch. 9):* producer wrong 1 %, reviewer wrong 10 %, independent; 91.7 % of their disagreements are cases where the producer was right.

**Generated artefacts (in `monographie/`, produced by `make figures`).**
- **Paths and labels:** include each figure as `figures/<name>.pdf` with the label `#fig:<name>`. Include each table with `::: {.inclure fichier="tableaux/<name>.md"}` `:::`; its label `tbl:<name>` is already set inside the generated file.
- **Display precision:** the generated tables are authoritative. Copy numbers from them; they may carry one more significant digit than the summaries above (e.g. 0,756 % for 0.76 %).

| Example | Chapter | Figure | Table(s) |
| :-- | :-- | :-- | :-- |
| log-score | 3 | `ch03-score-log`: surprise of each forecast under both outcomes | `ch03-score-log` |
| seu-a | 4 | `ch04-seuil`: threshold p∗ vs L/ΔU, Mr X, Mr Y, roulette | `ch04-seuil` |
| chain-a | 8 | `ch08-chaine`: failure probability vs N (1–8), unchecked vs cross-checked, q = 0 / 3 % | `ch08-chaine` |
| escape-a | 9 | `ch09-echappement`: escape and risk vs P(faux), fixed peer checker, both uptake policies | `ch09-echappement` (transposed: one column per scenario); also `ch09-depistage`, `ch09-desaccords`, `ch09-taux-echappement` (plain-arithmetic examples, the last one also serves the ch. 0 teaser) |
| plausibility | 12 | `ch12-plausibilite`: the three answer distributions, right answer highlighted | `ch12-plausibilite` |
| chain-b | 14 | `ch14-chaine-agent`: same curves to N = 12 | `ch14-chaine-agent` |
| escape-b | 16 | `ch16-modele-partage`: escape and risk for four scenarios (horizontal bars) | `ch16-modele-partage` (transposed) |
| seu-b | 17 | `ch17-decisions`: the four outcomes, axes scaled to p∗, buffer shown as an arrow | `ch17-scenarios` (inputs), `ch17-decisions` (outcomes) |

---

## 8. References Register (all "to verify" except the arXiv article)

Most of these references are now entries of `monographie/commun/biblio_a_verifier.bib`, citable by key (e.g. `mco1999`, `dellacqua2023`, `kalai2024`, `becker2025`). Each entry's `averifier` field repeats the points to check. Builders cite the keys, which render with « ? » until verified. The *Check* column lists the specific points to confirm against the primary source.

| Ref | Used in | Check |
| :-- | :-- | :-- |
| Author, *The frame problem in quantitative practice: ontological uncertainty and epistemic humility in an age of automated inference*, arXiv:2605.23614 (22 May 2026), doi:10.48550/arXiv.2605.23614 | 0, 2, 5, 7, 18, preface | ✔ in `biblio.bib` as `fauriat2026frame` (source: `source/frame_problem_article_WF.tex`) |
| McCarthy & Hayes (1969); Dennett (1984) "Cognitive wheels" | 2, 12 | robot and bomb-on-wagon example |
| Korzybski (1933) | 2 | quotation form |
| Pearl (1988; 2009) | 2 | minefield analogy wording |
| Vovk et al. (2005) / Angelopoulos & Bates (conformal prediction) | 2 | |
| Russell & Norvig, *AIMA* | 3 | possible-worlds framing |
| de Finetti; Savage (1954); Jaynes (2003); Lindley | 3, 4 | |
| Gneiting & Raftery (2007) (proper scoring rules) | 3 | suggested addition |
| Wynne (1992); Walker et al. (2003); Lempert et al. (2003); Knight (1921) | 5 | |
| Russell (1912), *The Problems of Philosophy* (chicken) | 5 | chapter and wording |
| Rogers Commission (1986); Tufte (1997) | 5, 6 | chart content (flights shown), engineers' objection |
| Hume (1748); Goodman (1955) | 7 | |
| Wolpert & Macready (1997) | 7 | |
| Sutton & Barto (2018) | 7 | |
| Lazer et al. (2014), *Science* | 7 | Google Flu Trends claims |
| Knight & Leveson (1986) | 8 | 27 versions; correlated failures |
| Levins (1966); Orzack & Sober (1993); Wimsatt (1981) | 8 | quotation "intersection of independent lies" |
| Mayo (1996; 2018) | 9 | severity definition |
| Bliss, Gilson & Deaton (1995) | 9 | probability matching to alarm reliability |
| Meyer (1992); Hoare (1969); Dijkstra (1970/72) | 10 | Dijkstra quotation source |
| Mars Climate Orbiter Mishap Investigation Board (1999) | 0, 8, 10 | SM_FORCES file, lbf·s vs N·s, factor ≈ 4.45, 23 Sept 1999 |
| Sculley et al. (2015) | 11 | |
| Dell'Acqua et al. (2023) | 11, 12 | 758 consultants; +12.2 % tasks, 25.1 % faster, ≈ 40 % quality; −19 points outside frontier |
| logit lens (nostalgebraist, 2020) | 11 | web source: acceptability |
| *Mata v. Avianca* (S.D.N.Y. 2023) | 0, 11 | |
| *Moffatt v. Air Canada* (2024 BCCRT 149) | 11 | absence of technology evidence; later statement that the chatbot predated generative AI (source?) |
| Goodhart (1975); Strathern (1997) | 11 | |
| Christiano et al. (2017) / Ouyang et al. (2022) (RLHF) | 11 | |
| Kalai & Vempala (2024); Kalai, Nachum, Vempala & Zhang (2025) | 12 | bound statement; evaluation scoring claim |
| Farquhar et al. (2024), *Nature* | 12 | semantic entropy scope |
| Bainbridge (1983) | 15 | |
| Becker et al. (2025) (METR) | 0, 15 | −19 % measured, +20 % estimated after; tool vintage |
| Spence (1973); Akerlof (1970) | 15 | |
| Sharma et al. (2023) or equivalent (sycophancy) | 15 | suggested addition |
| Shumailov et al. (2024), *Nature* | 16 | |
| SEC (2013), Knight Capital order | 14 | ≈ 45 min; > $460M |
| Sha (2001) (Simplex) | 13 | |
| de Moura & Ullrich (2021) (Lean 4) | 13 | |
| Threat image projection: EU Implementing Regulation (EU) 2015/1998 | 18 | TIP requirement; link to screener training |
| DeMillo, Lipton & Sayward (1978) (mutation testing) | 18 | |
| Lewis et al. (2020) (RAG) | 18 | |

---

## 9. Global Pitfalls (claims the book must not make)

1. Do not present *Challenger* as a pure frame failure (it was data framing plus suppressed uptake).
2. Do not present *Moffatt v. Air Canada* as evidence about LLM hallucination.
3. Do not say classical software keeps the inside-and-silent cell empty. It *can empty it in advance*.
4. Do not say "below, errors are loud". Classical errors are *definable*, not loud.
5. Do not say falling error rates erode uptake "by Bayes alone". Bayes fixes PPV; behaviour decides uptake.
6. Do not claim an optimal reviewer distance is derived.
7. Do not treat the omitted risk z as something the decider can estimate or read.
8. Do not mix the two senses of calibration. Do not claim that nothing in a model computes an out-of-competence signal (sample spread does, for guessing errors).
9. Do not let any argument depend on a specific model generation. Dated figures go in dated `.cas` blocks.
10. Do not claim that the book's statements are proven or validated by its design process.
11. Never mention internal documents, source tags, map ids, or "amendments" (hard constraint).
