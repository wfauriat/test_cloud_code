import { useEffect, useMemo, useState } from "react";
import type { Common } from "../App";
import { fmt, pct, type Qoi } from "../api";
import { useApi, useDebounced } from "../hooks";
import { Card, Lesson, Status, Tile } from "../components/ui";
import { Plot } from "../components/Plot";
import { colors, seqScale, useThemeVersion } from "../theme";

interface Experiment {
  names: string[];
  truth: Record<string, number>;
  theta: number[];
  noise: number;
  gust_std: number;
  obs: Partial<Record<Qoi, number[]>>;
  true_curve: { theta: number[] } & Partial<Record<Qoi, number[]>>;
}
interface Kde { x: number[]; y: number[] }
interface SummaryRow {
  name: string; prior_mean: number; prior_std: number; prior_ci: [number, number];
  post_mean: number; post_std: number; post_ci: [number, number]; map: number;
  prior_kde: Kde; post_kde: Kde; truth?: number; truth_in_ci?: boolean;
}
interface Band { p05: number[]; p50: number[]; p95: number[] }
interface CalOut {
  names: string[];
  method: "grid" | "mcmc";
  grid?: { axes: number[][]; marginals: number[][]; pairs: { i: number; j: number; density: number[][] }[]; n_points: number };
  mcmc?: { acceptance: number; burn: number; n_walkers: number; n_iter: number; traces: number[][][] };
  emulator?: { n_train: number; scores: Record<string, { r2: number; rmse: number }> };
  samples: { prior: number[][]; posterior: number[][] };
  summary: SummaryRow[];
  correlation: number[][];
  predictive_curve: { theta: number[]; qoi: Qoi; prior: Band; posterior: Band };
  prediction: { theta: number; qoi: Qoi; prior: { std: number; mean: number; kde: Kde }; posterior: { std: number; mean: number; kde: Kde }; truth?: number };
  seconds: number;
  model_runs: number;
  simulator_runs: number;
}

type ObsMode = "range" | "max_height" | "both";

export function CalibrationTab({ meta, spec, setSpec, settings }: Common) {
  const calibratable = meta.calibratable;
  const [names, setNames] = useState<string[]>(["cd"]);
  const [truth, setTruth] = useState<Record<string, number>>({});
  const [nObs, setNObs] = useState(8);
  const [thLo, setThLo] = useState(15);
  const [thHi, setThHi] = useState(65);
  const [obsMode, setObsMode] = useState<ObsMode>("range");
  const [noise, setNoise] = useState(1.0);
  const [gust, setGust] = useState(0);
  const [seed, setSeed] = useState(0);
  const [sigma, setSigma] = useState<number | null>(null); // null = same as the true noise
  const [method, setMethod] = useState<"grid" | "mcmc">("grid");
  const [useEmu, setUseEmu] = useState(true);
  const [walkers, setWalkers] = useState(32);
  const [iters, setIters] = useState(300);
  const [burn, setBurn] = useState(100);
  const [thetaNew, setThetaNew] = useState(45);
  const [reveal, setReveal] = useState(true);
  const exp = useApi<Experiment>();
  const cal = useApi<CalOut>();
  const theme = useThemeVersion();
  const info = (nm: string) => meta.params.find((p) => p.name === nm)!;
  const unitOf = (nm: string) => info(nm).unit;
  const qois: Qoi[] = obsMode === "both" ? ["range", "max_height"] : [obsMode];
  const predQoi: Qoi = qois.includes(settings.qoi) ? settings.qoi : qois[0];
  const qInfo = meta.qois[predQoi];
  const sig = sigma ?? noise;

  // Default "true" values: a bit more than one prior std above the prior mean.
  const truthOf = (nm: string) => truth[nm] ?? Number((spec[nm].value + 1.2 * Math.max(spec[nm].std, info(nm).step)).toFixed(4));
  const truthAll = Object.fromEntries(names.map((n) => [n, truthOf(n)]));

  const toggle = (nm: string) => {
    const next = names.includes(nm) ? names.filter((x) => x !== nm) : [...names, nm].slice(-3);
    setNames(meta.params.map((p) => p.name).filter((n) => next.includes(n)));
    // the prior is the law of the parameter in the left panel: make sure it is shown and non-degenerate
    if (!names.includes(nm) && (!spec[nm].uncertain || spec[nm].std <= 0)) {
      setSpec({ ...spec, [nm]: { ...spec[nm], uncertain: true, std: spec[nm].std > 0 ? spec[nm].std : info(nm).step * 4 } });
    }
  };

  const expBody = useMemo(() => ({ spec, dt: settings.dt, names, truth: truthAll, n_obs: nObs, theta_range: [thLo, thHi],
    noise, gust_std: gust, qois, seed }), [spec, settings.dt, names.join(), JSON.stringify(truthAll), nObs, thLo, thHi, noise, gust, obsMode, seed]);
  const expDeb = useDebounced(expBody, 200);
  useEffect(() => { if (names.length) exp.run("calibration/experiment", expDeb); }, [expDeb, exp.run]);

  const e = exp.data;
  const runCal = () => {
    if (!e) return;
    cal.run("calibration/run", { spec, dt: settings.dt, names: e.names, theta: e.theta, obs: e.obs, sigma: sig, method,
      use_emulator: useEmu, n_walkers: walkers, n_iter: iters, burn, theta_range: [thLo, thHi], theta_new: thetaNew,
      pred_qoi: predQoi, truth: e.truth, seed });
  };
  // Grid inference on 1-2 parameters is fast: rerun it automatically when the data change.
  const auto = method === "grid" && names.length <= 2;
  useEffect(() => { if (auto && e) runCal(); }, [e, auto, sig, thetaNew, predQoi]); // eslint-disable-line react-hooks/exhaustive-deps

  const c0 = cal.data;
  const d = c0 && c0.names.join() === names.join() ? c0 : null; // ignore stale results after changing parameters

  const dataPlot = useMemo(() => {
    if (!e) return null;
    const c = colors();
    const data: any[] = [];
    const pc = d?.predictive_curve;
    if (pc && pc.qoi === predQoi) {
      const band = (b: Band, name: string, fill: string, line: string, dash?: string) => [
        { x: pc.theta, y: b.p95, mode: "lines", line: { width: 0 }, showlegend: false, hoverinfo: "skip" },
        { x: pc.theta, y: b.p05, mode: "lines", line: { width: 0 }, fill: "tonexty", fillcolor: fill, name: `${name} 90% band`, hoverinfo: "skip" },
        { x: pc.theta, y: b.p50, mode: "lines", line: { color: line, width: 2, dash }, name: `${name} median`, hovertemplate: "θ = %{x}°: %{y:.2f}<extra></extra>" },
      ];
      data.push(...band(pc.prior, "prior", c.band, c.muted, "dot"));
      data.push(...band(pc.posterior, "posterior", hexAlpha(c.s1, 0.25), c.s1));
    }
    const tc = e.true_curve[predQoi];
    if (reveal && tc) data.push({ x: e.true_curve.theta, y: tc, mode: "lines", name: "truth (hidden)", line: { color: c.text, width: 1.5, dash: "dash" }, hoverinfo: "skip" });
    const ob = e.obs[predQoi];
    if (ob) {
      data.push({ x: e.theta, y: ob, mode: "markers", name: `observations (±${fmt(e.noise, 1)} noise)`,
        error_y: { type: "constant", value: e.noise, color: c.s2, thickness: 1.2, width: 4 },
        marker: { size: 9, color: c.s2, line: { color: c.surface, width: 2 } }, hovertemplate: "θ = %{x:.1f}°<br>obs = %{y:.2f}<extra></extra>" });
    }
    return {
      data,
      layout: {
        xaxis: { title: { text: "launch angle θ [deg]" }, range: [0, 90], dtick: 15 },
        yaxis: { title: { text: `${qInfo.label} [${qInfo.unit}]` } },
        shapes: [{ type: "line", x0: thetaNew, x1: thetaNew, yref: "paper", y0: 0, y1: 1, line: { color: c.text2, width: 1, dash: "dot" } }],
        annotations: [{ x: thetaNew, yref: "paper", y: 0.02, yanchor: "bottom", xanchor: "left", xshift: 3, text: "prediction", showarrow: false, font: { size: 11, color: c.text2 } }],
      },
    };
  }, [e, d, predQoi, reveal, thetaNew, theme]);

  const margPlot = useMemo(() => {
    if (!d) return null;
    const c = colors();
    const k = d.summary.length;
    const data: any[] = [];
    const layout: any = { grid: { rows: k, columns: 1, pattern: "independent", ygap: 0.45 }, margin: { t: 30 } };
    d.summary.forEach((r, i) => {
      const ax = i === 0 ? "" : String(i + 1);
      const show = i === 0;
      data.push({ x: r.prior_kde.x, y: r.prior_kde.y, mode: "lines", name: "prior", legendgroup: "prior", showlegend: show,
        line: { color: c.muted, width: 2, dash: "dash" }, xaxis: `x${ax}`, yaxis: `y${ax}`, hoverinfo: "skip" });
      data.push({ x: r.post_kde.x, y: r.post_kde.y, mode: "lines", name: "posterior", legendgroup: "post", showlegend: show,
        line: { color: c.s1, width: 2 }, fill: "tozeroy", fillcolor: hexAlpha(c.s1, 0.18), xaxis: `x${ax}`, yaxis: `y${ax}`,
        hovertemplate: `${r.name} = %{x:.4f}<extra>posterior</extra>` });
      if (reveal && r.truth !== undefined) {
        data.push({ x: [r.truth, r.truth], y: [0, Math.max(...r.post_kde.y) * 1.05], mode: "lines", name: "truth", legendgroup: "truth", showlegend: show,
          line: { color: c.text, width: 1.5, dash: "dot" }, xaxis: `x${ax}`, yaxis: `y${ax}`, hoverinfo: "skip" });
      }
      const lo = Math.min(r.prior_ci[0], r.post_ci[0], r.truth ?? Infinity);
      const hi = Math.max(r.prior_ci[1], r.post_ci[1], r.truth ?? -Infinity);
      const pad = 0.15 * (hi - lo);
      layout[`xaxis${ax}`] = { title: { text: `${info(r.name).label} [${unitOf(r.name)}]`, font: { size: 11 } }, range: [lo - pad, hi + pad] };
      layout[`yaxis${ax}`] = { showticklabels: false, title: { text: "density", font: { size: 11 } }, rangemode: "tozero" };
    });
    return { data, layout, height: 120 + 170 * k };
  }, [d, reveal, theme]);

  const pairPlot = useMemo(() => {
    if (!d || d.names.length < 2) return null;
    const c = colors();
    const pairs: [number, number][] = d.names.length === 2 ? [[0, 1]] : [[0, 1], [0, 2], [1, 2]];
    const data: any[] = [];
    const layout: any = { grid: { rows: 1, columns: pairs.length, pattern: "independent", xgap: 0.12 }, showlegend: false };
    pairs.forEach(([i, j], p) => {
      const ax = p === 0 ? "" : String(p + 1);
      const xa = `x${ax}`, ya = `y${ax}`;
      const g = d.grid?.pairs.find((q) => q.i === i && q.j === j);
      if (g && d.grid) {
        data.push({ type: "contour", x: d.grid.axes[i], y: d.grid.axes[j], z: g.density, colorscale: seqScale(), showscale: false,
          contours: { coloring: "heatmap" }, line: { width: 0.4, color: c.surface }, xaxis: xa, yaxis: ya, hoverinfo: "skip" });
      } else {
        const ps = d.samples.prior, qs = d.samples.posterior;
        data.push({ x: ps.map((s) => s[i]), y: ps.map((s) => s[j]), mode: "markers", marker: { size: 3, color: c.muted, opacity: 0.25 }, xaxis: xa, yaxis: ya, hoverinfo: "skip" });
        data.push({ x: qs.map((s) => s[i]), y: qs.map((s) => s[j]), mode: "markers", marker: { size: 3, color: c.s1, opacity: 0.35 }, xaxis: xa, yaxis: ya, hoverinfo: "skip" });
      }
      const ti = d.summary[i].truth, tj = d.summary[j].truth;
      if (reveal && ti !== undefined && tj !== undefined) {
        data.push({ x: [ti], y: [tj], mode: "markers", marker: { size: 12, symbol: "x-thin", line: { width: 2.5, color: c.text } }, xaxis: xa, yaxis: ya, hoverinfo: "skip" });
      }
      // On the grid, zoom on the posterior (the grid itself spans the whole prior box).
      const zoom = (k: number) => {
        const r = d.summary[k];
        const lo = Math.min(r.post_ci[0], r.truth ?? Infinity), hi = Math.max(r.post_ci[1], r.truth ?? -Infinity);
        const pad = 0.6 * (hi - lo);
        return g ? [lo - pad, hi + pad] : undefined;
      };
      layout[`xaxis${p === 0 ? "" : p + 1}`] = { title: { text: d.names[i], font: { size: 11 } }, range: zoom(i) };
      layout[`yaxis${p === 0 ? "" : p + 1}`] = { title: { text: d.names[j], font: { size: 11 } }, range: zoom(j) };
    });
    return { data, layout };
  }, [d, reveal, theme]);

  const tracePlot = useMemo(() => {
    if (!d?.mcmc) return null;
    const c = colors();
    const m = d.mcmc;
    const k = d.names.length;
    const data: any[] = [];
    const layout: any = { grid: { rows: k, columns: 1, pattern: "independent", ygap: 0.3 }, showlegend: false, shapes: [] };
    d.names.forEach((nm, i) => {
      const ax = i === 0 ? "" : String(i + 1);
      m.traces[i].forEach((w) => data.push({ y: w, mode: "lines", line: { width: 1, color: c.s1 }, opacity: 0.5, xaxis: `x${ax}`, yaxis: `y${ax}`, hoverinfo: "skip" }));
      layout[`yaxis${ax}`] = { title: { text: nm, font: { size: 11 } } };
      layout[`xaxis${ax}`] = { title: i === k - 1 ? { text: "iteration" } : undefined, showticklabels: i === k - 1 };
      layout.shapes.push({ type: "rect", xref: `x${ax}`, yref: `y${ax} domain`, x0: 0, x1: m.burn, y0: 0, y1: 1, fillcolor: c.band, line: { width: 0 }, layer: "below" });
    });
    return { data, layout, height: 90 + 120 * k };
  }, [d, theme]);

  const predPlot = useMemo(() => {
    if (!d) return null;
    const c = colors();
    const p = d.prediction;
    const data: any[] = [
      { x: p.prior.kde.x, y: p.prior.kde.y, mode: "lines", name: `prior predictive (σ = ${fmt(p.prior.std, 2)})`, line: { color: c.muted, width: 2, dash: "dash" }, hoverinfo: "skip" },
      { x: p.posterior.kde.x, y: p.posterior.kde.y, mode: "lines", name: `posterior predictive (σ = ${fmt(p.posterior.std, 2)})`, line: { color: c.s1, width: 2 },
        fill: "tozeroy", fillcolor: hexAlpha(c.s1, 0.18), hoverinfo: "skip" },
    ];
    const shapes: any[] = [];
    if (reveal && p.truth !== undefined) shapes.push({ type: "line", x0: p.truth, x1: p.truth, yref: "paper", y0: 0, y1: 1, line: { color: c.text, width: 1.5, dash: "dot" } });
    return { data, layout: { xaxis: { title: { text: `${meta.qois[p.qoi].label} at θ = ${p.theta}° [${meta.qois[p.qoi].unit}]` } }, yaxis: { title: { text: "density" }, rangemode: "tozero" }, shapes } };
  }, [d, reveal, theme]);

  return (
    <div className="grid">
      <Lesson title="Lesson 7 — Bayesian calibration: learn the parameters from measurements" open>
        Some inputs, like the drag coefficient, can't be measured directly, but their effect can. Fire a few shots at known angles, measure
        the range, and update your knowledge with <b>Bayes' rule</b>: posterior ∝ likelihood × prior.
        <ul>
          <li>The <b>prior</b> is the law of each parameter in the left panel. The <b>likelihood</b> says how well the simulator, run with those parameters, reproduces the noisy observations.</li>
          <li>More shots and less noise give a narrower posterior. The <b>posterior predictive</b> band then shrinks around the data, and so does the prediction at a new angle.</li>
          <li><b>Identifiability</b>: calibrate Cd and mass together. Only Cd/m enters the equations, so the data pin down a ridge, not a point (strong correlation). Widen the mass prior (std 0.1 kg) to see it clearly.</li>
          <li><b>Model error</b>: add unmodelled wind gusts. The model ignores them, so the posterior becomes over-confident and can miss the truth, unless you inflate the assumed noise σ.</li>
          <li>The <b>grid</b> method computes the exact posterior (fine for 1–3 parameters). <b>MCMC</b> samples it and scales to more parameters. It needs thousands of model runs, hence the GP <b>emulator</b>.</li>
        </ul>
      </Lesson>

      <section className="card">
        <div className="card-head"><h3>1 · Synthetic experiment</h3><span className="spacer" /><Status loading={exp.loading} error={exp.error} /></div>
        <div className="toolbar">
          <div className="field">Parameters to calibrate (1–3)
            <div>{calibratable.map((nm) => (
              <label key={nm} className="check" style={{ marginRight: 10 }}>
                <input type="checkbox" checked={names.includes(nm)} onChange={() => toggle(nm)} />{nm}
              </label>
            ))}</div>
          </div>
          {names.map((nm) => (
            <label className="field" key={nm}>true {nm} (hidden)
              <input type="number" step={info(nm).step / 5} value={truthOf(nm)}
                onChange={(ev) => { const v = parseFloat(ev.target.value); if (isFinite(v)) setTruth({ ...truth, [nm]: v }); }} />
            </label>
          ))}
          <label className="field">Shots
            <input type="number" min={1} max={60} value={nObs} onChange={(ev) => setNObs(Math.min(60, Math.max(1, parseInt(ev.target.value) || 1)))} />
          </label>
          <label className="field">Angles from–to [deg]
            <div style={{ display: "flex", gap: 4 }}>
              <input type="number" style={{ width: 60 }} value={thLo} onChange={(ev) => setThLo(parseFloat(ev.target.value) || 1)} />
              <input type="number" style={{ width: 60 }} value={thHi} onChange={(ev) => setThHi(parseFloat(ev.target.value) || 1)} />
            </div>
          </label>
          <label className="field">Measured
            <select value={obsMode} onChange={(ev) => setObsMode(ev.target.value as ObsMode)}>
              <option value="range">range</option><option value="max_height">max height</option><option value="both">both</option>
            </select>
          </label>
          <label className="field">Noise σ [m]
            <input type="number" min={0.05} step={0.1} value={noise} onChange={(ev) => setNoise(Math.max(0.05, parseFloat(ev.target.value) || 0.05))} />
          </label>
          <label className="field">Unmodelled gusts σ [m/s]
            <input type="number" min={0} step={0.5} value={gust} onChange={(ev) => setGust(Math.max(0, parseFloat(ev.target.value) || 0))} />
          </label>
          <button className="btn" onClick={() => setSeed(seed + 1)}>New data</button>
        </div>
        <p className="muted" style={{ fontSize: 12, margin: "6px 0 0" }}>
          Shots use the nominal values of the other inputs (left panel); the launch speed is {fmt(spec.v0.value, 1)} m/s unless v0 is calibrated.
          Priors: {names.map((nm) => `${nm} ~ ${spec[nm].dist}(${spec[nm].value}, σ=${spec[nm].std})`).join(", ")}.
        </p>
      </section>

      <section className="card">
        <div className="card-head"><h3>2 · Inference</h3><span className="spacer" /><Status loading={cal.loading} error={cal.error} /></div>
        <div className="toolbar">
          <label className="field">Method
            <select value={method} onChange={(ev) => setMethod(ev.target.value as any)}>
              <option value="grid">exact grid</option><option value="mcmc">MCMC (ensemble sampler)</option>
            </select>
          </label>
          {method === "mcmc" && <>
            <label className="field">Likelihood model
              <select value={useEmu ? "emu" : "sim"} onChange={(ev) => setUseEmu(ev.target.value === "emu")}>
                <option value="emu">GP emulator (fast)</option><option value="sim">simulator (slow)</option>
              </select>
            </label>
            <label className="field">Walkers <input type="number" min={4} max={256} step={2} value={walkers} onChange={(ev) => setWalkers(parseInt(ev.target.value) || 32)} /></label>
            <label className="field">Iterations <input type="number" min={20} max={5000} value={iters} onChange={(ev) => setIters(parseInt(ev.target.value) || 300)} /></label>
            <label className="field">Burn-in <input type="number" min={0} value={burn} onChange={(ev) => setBurn(parseInt(ev.target.value) || 0)} /></label>
          </>}
          <label className="field">Assumed noise σ
            <input type="number" min={0.05} step={0.1} value={sig} onChange={(ev) => setSigma(Math.max(0.05, parseFloat(ev.target.value) || 0.05))} />
          </label>
          {sigma !== null && <button className="btn small" onClick={() => setSigma(null)}>= true noise</button>}
          <label className="field">Predict at θ [deg]
            <input type="number" min={1} max={89} value={thetaNew} onChange={(ev) => setThetaNew(Math.min(89, Math.max(1, parseFloat(ev.target.value) || 45)))} />
          </label>
          <label className="check"><input type="checkbox" checked={reveal} onChange={(ev) => setReveal(ev.target.checked)} />reveal truth</label>
          <button className="btn primary" onClick={runCal} disabled={!e || cal.loading}>{auto ? "Re-run" : "Run inference"}</button>
        </div>
        {auto && <p className="muted" style={{ fontSize: 12, margin: "6px 0 0" }}>Exact grid with ≤ 2 parameters: updates automatically when the data change.</p>}
        {method === "mcmc" && !useEmu && <p className="muted" style={{ fontSize: 12, margin: "6px 0 0" }}>Each iteration runs walkers × shots simulations: expect several seconds.</p>}
      </section>

      {d && (
        <section className="card">
          <div className="tiles">
            {d.summary.map((r) => (
              <Tile key={r.name} label={`${r.name}: posterior mean ± std`} value={`${fmt(r.post_mean, 4)} ± ${fmt(r.post_std, 4)}`}
                note={<>prior {fmt(r.prior_mean, 3)} ± {fmt(r.prior_std, 3)}; std ÷ {fmt(r.prior_std / r.post_std, 1)}
                  {reveal && r.truth !== undefined && <> · truth {fmt(r.truth, 3)} {r.truth_in_ci ? "✓ in 95% CI" : "✗ outside 95% CI"}</>}</>} />
            ))}
            <Tile label="Model evaluations" value={d.model_runs.toLocaleString()}
              note={d.emulator ? `on the emulator; ${d.simulator_runs} simulator runs to train it` : `simulator runs, ${fmt(d.seconds, 1)} s`} />
            {d.mcmc && <Tile label="MCMC acceptance" value={pct(d.mcmc.acceptance, 0)} note={`${d.mcmc.n_walkers} walkers × ${d.mcmc.n_iter} it., burn-in ${d.mcmc.burn}`} />}
            {d.emulator && Object.entries(d.emulator.scores).map(([q, s]) => (
              <Tile key={q} label={`Emulator Q² (${q})`} value={fmt(s.r2, 4)} note={`RMSE ${fmt(s.rmse, 3)}`} />
            ))}
          </div>
        </section>
      )}

      <Card span={7} title="Data and predictions" sub={`Observed ${qInfo.label.toLowerCase()} per shot, with the 90% bands of the model predictions under the prior and under the posterior.`}>
        {dataPlot && <Plot data={dataPlot.data} layout={dataPlot.layout} height={400} />}
      </Card>
      <Card span={5} title="Prior → posterior" sub="Marginal density of each calibrated parameter.">
        {margPlot ? <Plot data={margPlot.data} layout={margPlot.layout} height={margPlot.height} /> : <p className="muted">Run the inference.</p>}
      </Card>
      {d && pairPlot && (
        <Card span={7} title="Joint posterior" sub={<>
          {d.grid ? "Exact posterior density on the grid" : "MCMC samples (blue) over prior samples (grey)"}; × marks the truth.
          Correlation: {d.names.flatMap((a, i) => d.names.slice(i + 1).map((b, k) => `${a}–${b} ${fmt(d.correlation[i][i + 1 + k], 2)}`)).join(", ")}.</>}>
          <Plot data={pairPlot.data} layout={pairPlot.layout} height={340} />
        </Card>
      )}
      {d && tracePlot && (
        <Card span={d.names.length >= 2 ? 5 : 7} title="MCMC traces" sub="Eight walkers. The shaded burn-in is discarded. Well-mixed chains look like stationary noise.">
          <Plot data={tracePlot.data} layout={tracePlot.layout} height={tracePlot.height} />
        </Card>
      )}
      {d && predPlot && (
        <Card span={d.names.length >= 2 || d.mcmc ? 12 : 5} title={`Prediction of a new shot at θ = ${d.prediction.theta}°`}
          sub={`Uncertainty on the ${meta.qois[d.prediction.qoi].label.toLowerCase()} from the parameter uncertainty only: std ÷ ${fmt(d.prediction.prior.std / d.prediction.posterior.std, 1)} after calibration.`}>
          <Plot data={predPlot.data} layout={predPlot.layout} height={300} />
        </Card>
      )}
    </div>
  );
}

/** "#rrggbb" + alpha -> "rgba(...)" (Plotly fills need explicit transparency). */
function hexAlpha(hex: string, a: number): string {
  const h = hex.replace("#", "");
  if (h.length !== 6) return hex;
  const n = parseInt(h, 16);
  return `rgba(${(n >> 16) & 255},${(n >> 8) & 255},${n & 255},${a})`;
}
