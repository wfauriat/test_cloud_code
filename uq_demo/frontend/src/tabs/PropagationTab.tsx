import { useEffect, useMemo, useState } from "react";
import type { Common } from "../App";
import { fmt, pct, uncertainNames } from "../api";
import { useApi, useDebounced } from "../hooks";
import { Card, Lesson, Status, Tile } from "../components/ui";
import { Plot } from "../components/Plot";
import { TrajectoryView, type Path } from "../components/TrajectoryView";
import { colors, useThemeVersion } from "../theme";

interface Stats { mean: number; std: number; min: number; max: number; p05: number; p50: number; p95: number }
interface McOut {
  n: number;
  uncertain: string[];
  qoi: Record<string, { values: number[]; stats: Stats; kde: { x: number[]; y: number[] } }>;
  convergence: { n: number[]; mean: number[]; lo: number[]; hi: number[] };
  fosm: { mean: number; std: number; contrib: Record<string, number> };
  trajectories: Path[];
  inputs: Record<string, number[]>;
  not_landed: number;
  risk?: { p_miss: number; p_miss_ci: [number, number]; p_short: number; p_long: number };
}

const NS = [100, 500, 1000, 2000, 5000, 10000, 20000];

export function PropagationTab({ meta, spec, settings }: Common) {
  const [n, setN] = useState(2000);
  const [sampling, setSampling] = useState<"random" | "lhs" | "sobol">("random");
  const [seed, setSeed] = useState(0);
  const [nTraj, setNTraj] = useState(80);
  const [auto, setAuto] = useState(true);
  const mc = useApi<McOut>();
  const theme = useThemeVersion();
  const names = uncertainNames(spec, meta);
  const q = settings.qoi;
  const qInfo = meta.qois[q];
  const label = (nm: string) => meta.params.find((p) => p.name === nm)!;

  const body = useMemo(() => ({ spec, dt: settings.dt, n, sampling, seed, n_traj: nTraj, qoi: q,
    target: settings.target, tol: settings.tol }), [spec, settings, n, sampling, seed, nTraj, q]);
  const debounced = useDebounced(body, 250);
  const run = () => mc.run("propagate", body);
  useEffect(() => { if (auto) mc.run("propagate", debounced); }, [debounced, auto, mc.run]);

  const d = mc.data;
  const s = d?.qoi[q]?.stats;
  const values = d?.qoi[q]?.values;

  const spaghetti = useMemo(() => d ? d.trajectories.map((t, i) => ({ ...t, value: d.qoi[q].values[i] })) : [],
    [d, q]);
  const impacts = useMemo(() => d?.qoi.range.values ?? [], [d]);

  const hist = useMemo(() => {
    if (!d || !s || !values) return null;
    const c = colors();
    const kd = d.qoi[q].kde;
    const xs = kd.x;
    const fm = d.fosm;
    const normal = xs.map((x) => fm.std > 0 ? Math.exp(-0.5 * ((x - fm.mean) / fm.std) ** 2) / (fm.std * Math.sqrt(2 * Math.PI)) : 0);
    const vline = (x: number, dash: string, color: string) => ({ type: "line", x0: x, x1: x, yref: "paper", y0: 0, y1: 1, line: { color, width: 1.5, dash } });
    return {
      data: [
        { x: values, type: "histogram", histnorm: "probability density", name: "Monte Carlo samples", nbinsx: Math.min(80, Math.max(15, Math.round(Math.sqrt(values.length)))),
          marker: { color: c.s1, opacity: 0.55, line: { color: c.surface, width: 1 } }, hovertemplate: "%{x}<br>density %{y:.3g}<extra></extra>" },
        { x: xs, y: kd.y, name: "kernel density", mode: "lines", line: { color: c.s1, width: 2 }, hoverinfo: "skip" },
        ...(fm.std > 0 ? [{ x: xs, y: normal, name: "first-order (FOSM) normal", mode: "lines", line: { color: c.s2, width: 2, dash: "dash" }, hoverinfo: "skip" }] : []),
      ],
      layout: {
        barmode: "overlay",
        xaxis: { title: { text: `${qInfo.label} [${qInfo.unit}]` } },
        yaxis: { title: { text: "probability density" } },
        shapes: [
          { type: "rect", x0: settings.target - settings.tol, x1: settings.target + settings.tol, yref: "paper", y0: 0, y1: 1, fillcolor: c.band, line: { width: 0 }, layer: "below" },
          vline(s.mean, "solid", c.text), vline(s.p05, "dot", c.text2), vline(s.p95, "dot", c.text2),
        ],
        annotations: [
          { x: s.mean, yref: "paper", y: 0.99, text: "mean", showarrow: false, yanchor: "top", xanchor: "left", xshift: 3, font: { size: 11, color: c.text2 } },
          { x: s.p05, yref: "paper", y: 0.99, text: "5%", showarrow: false, yanchor: "top", xanchor: "left", xshift: 3, font: { size: 11, color: c.text2 } },
          { x: s.p95, yref: "paper", y: 0.99, text: "95%", showarrow: false, yanchor: "top", xanchor: "left", xshift: 3, font: { size: 11, color: c.text2 } },
          { x: settings.target, yref: "paper", y: 0.01, yanchor: "bottom", text: "target", showarrow: false, font: { size: 11, color: c.text2 }, bgcolor: c.surface },
        ],
      },
    };
  }, [d, q, s, values, settings.target, settings.tol, theme]);

  const convPlot = useMemo(() => {
    if (!d) return null;
    const c = colors();
    const cv = d.convergence;
    return {
      data: [
        { x: cv.n, y: cv.hi, mode: "lines", line: { width: 0 }, showlegend: false, hoverinfo: "skip" },
        { x: cv.n, y: cv.lo, mode: "lines", line: { width: 0 }, fill: "tonexty", fillcolor: c.band, name: "95% confidence interval", hoverinfo: "skip" },
        { x: cv.n, y: cv.mean, mode: "lines", line: { color: c.s1, width: 2 }, name: "running mean", hovertemplate: "n = %{x}<br>mean = %{y:.2f}<extra></extra>" },
      ],
      layout: { xaxis: { type: "log", dtick: 1, title: { text: "number of samples n" } }, yaxis: { title: { text: `mean ${qInfo.label.toLowerCase()} [${qInfo.unit}]` } } },
    };
  }, [d, theme, qInfo]);

  const scatter = useMemo(() => {
    if (!d || !d.uncertain.length) return null;
    const c = colors();
    const k = d.uncertain.length;
    const cols = Math.min(k, 3);
    const rows = Math.ceil(k / cols);
    const yv = d.qoi[q].values;
    const data: any[] = [];
    const layout: any = { grid: { rows, columns: cols, pattern: "independent", xgap: 0.12, ygap: 0.3 }, showlegend: false, margin: { t: 10, b: 40 } };
    d.uncertain.forEach((nm, i) => {
      const xs = d.inputs[nm];
      const ax = i === 0 ? "" : String(i + 1);
      data.push({ x: xs, y: yv.slice(0, xs.length), mode: "markers", type: "scatter", xaxis: `x${ax}`, yaxis: `y${ax}`,
        marker: { size: 4, color: c.s1, opacity: 0.35 }, hovertemplate: `${nm} = %{x:.3f}<br>${q} = %{y:.2f}<extra></extra>` });
      const p = label(nm);
      layout[`xaxis${ax}`] = { title: { text: `${p.label} [${p.unit}]`, font: { size: 11 } } };
      layout[`yaxis${ax}`] = { title: { text: i % cols === 0 ? qInfo.label : "" } };
    });
    return { data, layout, height: 230 * rows };
  }, [d, q, theme]);

  return (
    <div className="grid">
      <Lesson title="Lesson 2 — propagate input uncertainty with Monte Carlo" open>
        Switch inputs to <b>uncertain</b> in the left panel and give them a mean, a standard deviation and a law.
        Each Monte Carlo sample draws every uncertain input, runs the simulator, and records the QoI.
        <ul>
          <li>The spaghetti plot shows the samples; the histogram shows the <b>output distribution</b>: mean, spread, 5–95% interval.</li>
          <li><b>Risk</b> is the probability of landing outside the target ± tolerance.</li>
          <li>The Monte Carlo error decreases as <b>1/√n</b>: 4× more samples halve the confidence interval. Try LHS or Sobol sampling: they converge faster.</li>
          <li>The dashed curve is the <b>first-order (FOSM)</b> approximation, which linearises the model at the mean. It is cheap, and fine while uncertainties are small. Increase a std to see it break down.</li>
        </ul>
      </Lesson>

      <section className="card">
        <div className="toolbar">
          <label className="field">Samples n
            <select value={n} onChange={(e) => setN(+e.target.value)}>{NS.map((v) => <option key={v} value={v}>{v}</option>)}</select>
          </label>
          <label className="field">Sampling
            <select value={sampling} onChange={(e) => setSampling(e.target.value as any)}>
              <option value="random">random (plain MC)</option><option value="lhs">Latin hypercube</option><option value="sobol">Sobol (quasi-MC)</option>
            </select>
          </label>
          <label className="field">Trajectories drawn
            <select value={nTraj} onChange={(e) => setNTraj(+e.target.value)}>{[0, 30, 80, 200, 400].map((v) => <option key={v} value={v}>{v}</option>)}</select>
          </label>
          <label className="field">Seed <input type="number" value={seed} onChange={(e) => setSeed(parseInt(e.target.value) || 0)} /></label>
          <button className="btn" onClick={() => setSeed(seed + 1)}>New seed</button>
          <label className="check"><input type="checkbox" checked={auto} onChange={(e) => setAuto(e.target.checked)} />auto-run</label>
          {!auto && <button className="btn primary" onClick={run}>Run Monte Carlo</button>}
          <Status loading={mc.loading} error={mc.error} />
        </div>
        <div style={{ marginTop: 6 }}>
          {names.length ? names.map((nm) => <span className="chip" key={nm}>{label(nm).label}: {spec[nm].dist} σ={spec[nm].std}</span>)
            : <span className="error">No uncertain input: toggle "fixed" → "uncertain" in the left panel.</span>}
        </div>
      </section>

      {d && s && (
        <section className="card">
          <div className="tiles">
            <Tile label={`Mean ${qInfo.label.toLowerCase()}`} value={`${fmt(s.mean, 2)} ${qInfo.unit}`} note={`FOSM: ${fmt(d.fosm.mean, 2)}`} />
            <Tile label="Std. deviation" value={`${fmt(s.std, 2)} ${qInfo.unit}`} note={`FOSM: ${fmt(d.fosm.std, 2)}`} />
            <Tile label="90% interval" value={`${fmt(s.p05, 1)} – ${fmt(s.p95, 1)}`} note="5% and 95% quantiles" />
            {d.risk && <Tile label="P(miss target)" value={pct(d.risk.p_miss)}
              note={`95% CI ${pct(d.risk.p_miss_ci[0])}–${pct(d.risk.p_miss_ci[1])}; short ${pct(d.risk.p_short)}, long ${pct(d.risk.p_long)}`} />}
            <Tile label="Simulator runs" value={d.n.toLocaleString()} note={d.not_landed ? `${d.not_landed} did not land` : `${sampling} sampling`} />
          </div>
        </section>
      )}

      <Card span={7} title="Sampled trajectories" sub={`Colored by ${qInfo.label.toLowerCase()}; ticks on the ground mark impact points.`}>
        <TrajectoryView spaghetti={spaghetti} valueLabel={`${qInfo.label} [${qInfo.unit}]`} impacts={impacts}
          band={q === "range" ? [settings.target - settings.tol, settings.target + settings.tol] : null}
          wind={spec.wind.value} height={340} />
      </Card>
      <Card span={5} title={`Distribution of ${qInfo.label.toLowerCase()}`} sub="Histogram, kernel density and first-order approximation. The shaded band is target ± tol.">
        {hist && <Plot data={hist.data} layout={hist.layout} height={340} />}
      </Card>
      <Card span={5} title="Monte Carlo convergence" sub="Running estimate of the mean and its 95% confidence interval.">
        {convPlot && <Plot data={convPlot.data} layout={convPlot.layout} height={280} />}
      </Card>
      <Card span={7} title="Output vs each input" sub="A clear trend means an influential input; a flat cloud means a negligible one. This previews sensitivity analysis.">
        {scatter && <Plot data={scatter.data} layout={scatter.layout} height={scatter.height} />}
      </Card>
    </div>
  );
}
