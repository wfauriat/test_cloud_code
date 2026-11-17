# The Language Machine

An explorable "infinite canvas" about AI and language models, made for mixed, non-specialist audiences.
It is one self-contained HTML file with plain JavaScript and no build step. Open `index.html` in any modern browser.
It needs a network connection only for the Google Fonts, and falls back to system fonts without one.

## What is on the map

The centre card branches into four territories, with three angles each:

| Territory | Angles |
|---|---|
| The machine | What it is · Where it works and fails · Why this wave is different (language as substrate) |
| In your life | Already everywhere (chosen / embedded / connected) · Learning and thinking · Using it well |
| At work | Jobs are bundles of tasks · From answers to errands (agents) · Expertise and trust |
| Society | Who decides · Hype, fear and incentives · What it says about us |

Each angle opens 3 to 5 **threads**, 43 in all. Each thread shows two levels of detail:

1. a title and a one-line gist,
2. a short explanation, with chips that open optional extras: **Analogy**, **Example**, **The catch**, **Ask the room** (a discussion prompt) and, on one card, **Try it** (a next-word sampling toy with a temperature slider).

Links inside the text (↗) jump to related cards elsewhere on the map.

## Ways to explore

- **Free roaming**: drag to pan; scroll, pinch or use `+`/`−` to zoom; `F` fits the map. When you zoom far out, cards switch to large labels so the map stays readable.
- **Guided paths** (Guide button): five short routes for different starting points (*New to all this*, *Worried about it*, *Skeptical of the hype*, *Already a heavy user*, *Not really my thing*). Use `←`/`→` to step through. They follow the digest's point that anxious, enthusiastic, skeptical and disengaged listeners each need a different way in.
- **Jump to an angle** from the Guide panel, or link straight to a card with a hash, e.g. `index.html#jagged`.
- **Overview** folds everything back. **Show all threads** opens every angle at once.
- The camera follows what you open. You can turn this off in the Guide panel.

## Source

The content is adapted from the digest *AI and LLMs for a lay audience: angles and usage digest* (Nov 2026).
That digest compiles public surveys (Pew, Reuters Institute, Gallup), vendor usage reports (OpenAI, Anthropic, Microsoft, Google) and education studies (OECD, randomized trials).
Numbers are kept few and rounded on purpose. The analogies, examples and discussion prompts were added for conversation and are not findings.
Check figures against the original sources before quoting them.

## Code layout (inside `index.html`)

- `DATA` / `PATHS`: all the content, as plain JS objects. Edit text here. `{{id|label}}` makes a cross-link and `*text*` makes emphasis.
- Layout: an outline-style tidy tree with left and right sides. Card heights are measured from the DOM. Each re-layout is anchored on the card you clicked, so that card stays still and its neighbours move around it.
- Rendering: DOM cards in a single transformed "world" layer, with SVG edges and territory zones, and a canvas minimap. A single `requestAnimationFrame` loop eases the cards and camera.
