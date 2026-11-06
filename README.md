# tomo-vizu – uniaxial tomography, explained with animations

A short animated explainer (about 3 min 30 s, 8 scenes) about **uniaxial X-ray tomography**: how the density of
concentric shells inside a closed casing can be recovered from a single row of screen pixels. The figures are
simple shapes driven by one small mathematical model, so every bar, colour and number on screen is computed
rather than drawn by hand. The same model also powers an interactive page you can play with in a browser.

Everything here was built in one Claude Code session; the full transcript is in
[`docs/session_transcript.html`](docs/session_transcript.html).

## What the explainer shows

**Set-up.** An X-ray source, a confinement casing, an object made of concentric shells (only half a slice is
needed thanks to symmetry) and a screen with one pixel per row. Rows *i* and shells *k* are numbered from the
outside; row *i* only crosses shells 1 … *i*.

**Model (Beer–Lambert, material coefficient μ):**

```
D_mes(i)  = D_0(i) · A_casing(i) · A_object(i)
A_object(i) = exp( − Σ_k L_ik · μ_k · ρ_k )          L_ik = length of row i inside shell k (geometry)
```

| Scene | Title | Message |
|---|---|---|
| S1 | Uniaxial X-ray tomography | The experiment, the doses D and the absorption fractions A; the densities ρ_k are the unknowns. |
| S2 | Phase 1: accounting | A blank shot (calibration, or a simulation without the object) gives D_void; D_mes / D_void = A_object isolates the object. |
| S3 | Phase 2: inverting – what each pixel row sees | One equation per row: A = exp(−L ρ), with a lower-triangular L. |
| S4 | Phase 2: optimization by stacking bricks | Add the brick that best lowers the mismatch Σ Δ_i², one step downhill, until the screens match. |
| S5 | Phase 2: why gradients help | On the mismatch landscape, a step walk probes neighbours brick by brick; the gradient ∂A/∂ρ = −L e^(−Lρ) points downhill for all shells at once. |
| S6 | Going further 1 – noise | 5 % noise on the screen, 10 shells: without regularization the inner shells are unreliable. |
| S7 | Going further 2 – two materials | If the inner shells can be either of two materials, several objects give exactly the same screen. |
| S8 | Going further 3 – a biased blank | A wrong source or casing estimate biases the densities, mostly the outer shell. |

"Step" is kept for literal optimization steps; the two stages of the method are called *phases*.

## Repository layout

```
manim_build/
  model.py      the physics: geometry, chord matrix L, doses, noise, brick walk, Gauss–Newton, …
  theme.py      look and layout (Inter font, colours from the original sketch), drawing helpers
  scenes.py     the 8 Manim scenes (S1_Setup … S8_BlankBias)
  i18n.py       French text for every label, caption and title (equations unchanged)
  render.sh     renders all scenes and joins them into one video
  manim.cfg     white background
  preflight.py  smoke test of the Manim + LaTeX install
interactive/
  tomo_lab.html hands-on page (single file, plain JavaScript, no build)
docs/
  session_transcript.html   transcript of the session that produced all of this
tools/
  make_transcript.py        builds that transcript from a Claude Code session log
```

Rendered videos are not committed (`manim_build/media/`, `manim_build/media_fr/` are ignored); they are
reproduced from the code.

## Rendering the videos

Requirements: Python 3.10+, [Manim Community](https://www.manim.community/) 0.19+, a LaTeX install
(`latex`, `dvisvgm`, packages `standalone`, `sansmath`), ffmpeg, Pango/Cairo development files and the
[Inter](https://rsms.me/inter/) font. On Debian/Ubuntu, for example:

```bash
sudo apt-get install -y ffmpeg libcairo2-dev libpango1.0-dev texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-science dvisvgm
python3 -m venv .venv && .venv/bin/pip install manim
```

Then, from `manim_build/`:

```bash
./render.sh l                    # quick 480p draft of every scene
./render.sh h                    # final 1080p60 → media/tomography_explainer_1080p60.mp4
./render.sh m S5_Gradient        # one scene only, 720p
TOMO_LANG=fr ./render.sh h       # French version → media_fr/tomography_explainer_1080p60_fr.mp4
```

Qualities: `l` 480p15, `m` 720p30, `h` 1080p60, `k` 2160p60. The final 1080p video is about 3 min 28 s and
16 MB. Set `MANIM=/path/to/manim` if Manim is not on your `PATH`.

**French version.** Both languages come from the same code. `TOMO_LANG=fr` swaps every visible text through
`i18n.py`; equations and notations (D_mes, D_void, A_object, L_ik, ρ_k …) are kept as they are. Setting
`TOMO_I18N_LOG=missing.txt` lists any text that has no translation yet.

## The interactive page

Open `interactive/tomo_lab.html` in a browser (no server, no install). It uses the same model as the videos:

- **Phase 1** – measured dose with adjustable noise and true casing density; the blank comes from a calibration
  shot or a simulation (assumed casing density, source error), giving A_obs = D_mes / D_void. The true object
  is hidden until you reveal it, and can be edited.
- **Phase 2** – build a candidate object: click shells to add bricks (Shift-click or right-click removes,
  scroll for fine steps), drag the stacks, or use the sliders; switch each shell between material 1 and
  material 2; 5 or 10 shells.
- **Comparison** – per row, measured vs candidate dose, A_obs vs A_cand and Δ_i, the total mismatch and its
  history; buttons for an exact inversion, Gauss–Newton gradient steps and a brick walk.

## Model in numbers

5 shells of equal thickness in a unit radius, true densities (outer → inner) 0.4, 1.0, 1.4, 0.8, 0.6;
one brick = 0.2; material 2 absorbs half as much as material 1 (μ₂ = μ₁ / 2); casing walls of thickness 0.08
and density 2; source dose 1 − 0.15 y². With these values the brick walk recovers the densities in 21 steps,
Gauss–Newton in 4–5.
