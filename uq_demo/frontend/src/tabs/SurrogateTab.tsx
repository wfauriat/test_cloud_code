import { useEffect, useMemo, useState } from "react";
import type { Common } from "../App";
import { fmt, post, uncertainNames } from "../api";
import { useApi } from "../hooks";
import { Card, Lesson, Status, Tile } from "../components/ui";
import { Plot } from "../components/Plot";
import { colors, divScale, seqScale, useThemeVersion } from "../theme";
import { DOE_LABELS, type Design } from "./DoeTab";

export interface TrainedModel {
  id: string;
  kind: string;
  label: string;
  names: string[];
  qoi: string;
  n_train: number;
}

interface Scores { r2: number; rmse: number; mae: number; y: number[]; pred: number[] }
interface TrainOut {
  model: TrainedModel & { kernel?: string; train_time: number };
  train: Scores;
  test: Scores;
  timing: { simulator_per_1000: number; surrogate_per_1000: number; train: number };
}
interface SliceOut { x: number[]; pred: number[]; std: number[] | null; true: number[]; train_x: number[]; train_y: number[] }
interface SurfOut { x: number[]; y: number[]; pred: number[][]; true: number[][]; std: number[][] | null; error: number[][]; train_x: number[]; train_y: number[] }
interface LcOut { sizes: number[]; curves: Record<string, { label: string; r2: number[]; rmse: number[] }> }

interface Props extends Common {
  design: Design | null;
  model: TrainedModel | null;
  setModel: (m: TrainedModel) => void;
  onUse: () => void;
  goDoe: () => void;
}

const SERIES = ["s1", "s2", "s3"] as const;

export function SurrogateTab({ meta, spec, settings, design, setModel, onUse, goDoe }: Props) {
  const [kind, setKind] = useState("gp");
  const [localDesign, setLocalDesign] = useState<Design | null>(design);
  const [sliceParam, setSliceParam] = useState<string>("");
  const [px, setPx] = useState("");
  const [py, setPy] = useState("");
  const [view, setView] = useState<"pred" | "true" | "error" | "std">("pred");
  const [lcKinds, setLcKinds] = useState<string[]>(["poly2", "gp", "rf"]);
  const train = useApi<TrainOut>();
  const slice = useApi<SliceOut>();
  const surf = useApi<SurfOut>();
  const lc = useApi<LcOut>();
  const theme = useThemeVersion();
  const q = meta.qois[settings.qoi];
  const info = (nm: string) => meta.params.find((p) => p.name === nm)!;
  const axisTitle = (nm: string) => `${info(nm).label} [${info(nm).unit}]`;

  useEffect(() => { if (design) setLocalDesign(design); }, [design]);

  const quickDesign = async () => {
    const names = uncertainNames(spec, meta);
    const out = await post("doe", { spec, names: names.length ? names : ["v0", "theta"], method: "lhs_opt", n: 40 });
    setLocalDesign({ names: out.names, box: out.box, X: out.X, method: "lhs_opt" });
  };

  const d = localDesign;
  useEffect(() => {
    if (!d) return;
    train.run("surrogate/train", { spec, dt: settings.dt, names: d.names, box: d.box, X: d.X, kind, qoi: settings.qoi })
      .then((out) => { if (out) setModel(out.model); });
    // retrain when the design, the model type or the QoI changes
  }, [d, kind, settings.qoi]); // eslint-disable-line react-hooks/exhaustive-deps

  const m = train.data?.model;
  useEffect(() => {
    if (!d) return;
    if (!d.names.includes(sliceParam)) setSliceParam(d.names[0]);
    if (!d.names.includes(px)) setPx(d.names[0]);
    if (!d.names.includes(py) || py === d.names[0]) setPy(d.names[Math.min(1, d.names.length - 1)]);
  }, [d]); // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => { if (m && sliceParam && m.names.includes(sliceParam)) slice.run("surrogate/slice", { model_id: m.id, param: sliceParam }); }, [m, sliceParam, slice.run]);
  useEffect(() => {
    if (m && px && py && px !== py && m.names.includes(px) && m.names.includes(py)) surf.run("surrogate/surface", { model_id: m.id, px, py, n_grid: 40 });
  }, [m, px, py, surf.run]);

  const parity = useMemo(() => {
    const t = train.data;
    if (!t) return null;
    const c = colors();
    const all = [...t.train.y, ...t.test.y];
    const lo = Math.min(...all);
    const hi = Math.max(...all);
    return {
      data: [
        { x: [lo, hi], y: [lo, hi], mode: "lines", line: { color: c.muted, dash: "dash", width: 1.5 }, name: "perfect prediction", hoverinfo: "skip" },
        { x: t.test.y, y: t.test.pred, mode: "markers", name: `test (${t.test.y.length} new runs)`,
          marker: { size: 6, color: c.s2, opacity: 0.6 }, hovertemplate: "true %{x:.2f}<br>pred %{y:.2f}<extra>test</extra>" },
        { x: t.train.y, y: t.train.pred, mode: "markers", name: `training (${t.train.y.length})`,
          marker: { size: 8, color: c.s1, line: { color: c.surface, width: 1.5 } }, hovertemplate: "true %{x:.2f}<br>pred %{y:.2f}<extra>train</extra>" },
      ],
      layout: { xaxis: { title: { text: `simulator ${q.label.toLowerCase()} [${q.unit}]` } }, yaxis: { title: { text: `surrogate [${q.unit}]` } } },
    };
  }, [train.data, theme]);

  const slicePlot = useMemo(() => {
    const s = slice.data;
    if (!s) return null;
    const c = colors();
    const data: any[] = [];
    if (s.std) {
      data.push({ x: s.x, y: s.pred.map((v, i) => v + 2 * s.std![i]), mode: "lines", line: { width: 0 }, showlegend: false, hoverinfo: "skip" });
      data.push({ x: s.x, y: s.pred.map((v, i) => v - 2 * s.std![i]), mode: "lines", line: { width: 0 }, fill: "tonexty",
        fillcolor: c.band, name: kind === "gp" ? "GP ±2σ" : "spread of trees ±2σ", hoverinfo: "skip" });
    }
    data.push({ x: s.x, y: s.true, mode: "lines", name: "simulator (truth)", line: { color: c.text, width: 2 }, hovertemplate: "%{y:.2f}<extra>truth</extra>" });
    data.push({ x: s.x, y: s.pred, mode: "lines", name: "surrogate", line: { color: c.s1, width: 2, dash: "dash" }, hovertemplate: "%{y:.2f}<extra>surrogate</extra>" });
    data.push({ x: s.train_x, y: s.train_y, mode: "markers", name: "training points (projected)", marker: { size: 6, color: c.muted, opacity: 0.6 }, hoverinfo: "skip" });
    return { data, layout: { xaxis: { title: { text: axisTitle(sliceParam) } }, yaxis: { title: { text: `${q.label} [${q.unit}]` } } } };
  }, [slice.data, theme]);

  const surfPlot = useMemo(() => {
    const s = surf.data;
    if (!s) return null;
    const c = colors();
    const z = view === "std" ? s.std : s[view];
    if (!z) return null;
    const isErr = view === "error";
    const zmax = isErr ? Math.max(...z.flat().map(Math.abs)) : undefined;
    const title = { pred: `surrogate ${q.label.toLowerCase()}`, true: `simulator ${q.label.toLowerCase()}`, error: "surrogate − simulator", std: "GP standard deviation" }[view];
    return {
      data: [
        { type: "contour", x: s.x, y: s.y, z, colorscale: isErr ? divScale() : seqScale(), zmin: isErr ? -zmax! : undefined, zmax,
          contours: { coloring: "heatmap", showlabels: true, labelfont: { size: 10, color: c.text } }, line: { width: 0.5, color: c.surface },
          colorbar: { title: { text: `${title} [${q.unit}]`, side: "right", font: { size: 11 } }, thickness: 12, outlinewidth: 0, tickfont: { color: c.muted } },
          hovertemplate: `${px} = %{x:.2f}<br>${py} = %{y:.2f}<br>%{z:.3f}<extra></extra>` },
        { x: s.train_x, y: s.train_y, mode: "markers", name: "training points", marker: { size: 7, color: c.surface, line: { color: c.text, width: 1.5 } }, hoverinfo: "skip" },
      ],
      layout: { xaxis: { title: { text: axisTitle(px) } }, yaxis: { title: { text: axisTitle(py) } }, showlegend: false, margin: { r: 10 } },
    };
  }, [surf.data, view, theme]);

  const lcPlot = useMemo(() => {
    const l = lc.data;
    if (!l) return null;
    const c = colors() as any;
    return {
      data: Object.entries(l.curves).map(([kd, cv], i) => ({
        x: l.sizes, y: cv.r2.map((v) => Math.max(v, -0.2)), name: cv.label, mode: "lines+markers",
        line: { color: c[SERIES[i % 3]], width: 2 }, marker: { size: 8, color: c[SERIES[i % 3]], line: { color: c.surface, width: 2 } },
        hovertemplate: `${kd}: n = %{x}, Q² = %{y:.4f}<extra></extra>`,
      })),
      layout: { xaxis: { type: "log", tickvals: l.sizes, title: { text: "training-set size n" } }, yaxis: { title: { text: "Q² on test set" }, range: [-0.2, 1.02] } },
    };
  }, [lc.data, theme]);

  if (!d) {
    return (
      <div className="grid">
        <section className="card">
          <h3>No training design yet</h3>
          <p>Build one in the <b>Design of experiments</b> tab, or start from a quick default (optimized LHS, 40 points on the uncertain inputs).</p>
          <div className="toolbar"><button className="btn" onClick={goDoe}>Go to DoE</button><button className="btn primary" onClick={quickDesign}>Use quick default</button></div>
        </section>
      </div>
    );
  }

  const t = train.data;
  return (
    <div className="grid">
      <Lesson title="Lesson 4 — surrogate models: a cheap stand-in for the simulator" open>
        A surrogate (metamodel) is a regression <b>f̂(x) ≈ f(x)</b> fitted on the DoE runs. Once trained it costs microseconds,
        so it can replace the simulator in the tens of thousands of runs that Monte Carlo, Sobol or optimization need.
        <ul>
          <li>Judge it on <b>new</b> points: Q² (R² on a test set) close to 1 and a small RMSE. A perfect fit on the training points proves nothing (random forests overfit).</li>
          <li>The <b>Gaussian process</b> (kriging) interpolates the data and also returns its own uncertainty (±2σ band), which grows away from the training points.</li>
          <li>The <b>learning curve</b> shows how many runs each model needs: compare polynomials, GP and forest.</li>
          <li>Try a small n (10), a wide box (k = 5), or the max height QoI to see models fail.</li>
        </ul>
      </Lesson>

      <section className="card">
        <div className="toolbar">
          <label className="field">Model
            <select value={kind} onChange={(e) => setKind(e.target.value)}>
              {Object.entries(meta.surrogates).map(([k, v]) => <option key={k} value={k}>{v}</option>)}
            </select>
          </label>
          <div className="field">Training design
            <span>{DOE_LABELS[d.method] ?? d.method}, {d.X.length} runs on {d.names.join(", ")} — QoI: {q.label}</span>
          </div>
          <button className="btn" onClick={goDoe}>Change design</button>
          <button className="btn primary" disabled={!m} onClick={onUse}>Use for sensitivity analysis →</button>
          <Status loading={train.loading} error={train.error} />
        </div>
      </section>

      {t && (
        <section className="card">
          <div className="tiles">
            <Tile label="Q² (test)" value={fmt(t.test.r2, 4)} note={`R² on training: ${fmt(t.train.r2, 4)}`} />
            <Tile label="RMSE (test)" value={`${fmt(t.test.rmse, 3)} ${q.unit}`} note={`MAE ${fmt(t.test.mae, 3)}`} />
            <Tile label="Simulator cost" value={`${fmt(t.timing.simulator_per_1000 * 1000, 1)} ms`} note="per 1000 runs (vectorized Euler)" />
            <Tile label="Surrogate cost" value={`${fmt(t.timing.surrogate_per_1000 * 1000, 1)} ms`} note={`per 1000 predictions; fit in ${fmt(t.timing.train * 1000, 0)} ms`} />
          </div>
          {t.model.kernel && <p className="muted" style={{ fontSize: 12, margin: "8px 0 0" }}>Fitted GP kernel (inputs scaled to [0,1]): <code>{t.model.kernel}</code></p>}
        </section>
      )}

      <Card span={5} title="Parity plot" sub="Predicted vs true QoI. Points on the diagonal are perfect predictions.">
        {parity && <Plot data={parity.data} layout={parity.layout} height={330} />}
      </Card>
      <Card span={7} title="1D slice" sub="One input varies; the others stay at their nominal values (clipped into the box)."
        right={<><Status loading={slice.loading} error={slice.error} />
          <select className="inline" value={sliceParam} onChange={(e) => setSliceParam(e.target.value)}>
            {d.names.map((nm) => <option key={nm} value={nm}>{info(nm).label}</option>)}
          </select></>}>
        {slicePlot && <Plot data={slicePlot.data} layout={slicePlot.layout} height={330} />}
      </Card>
      {d.names.length >= 2 && (
        <Card span={7} title="2D response surface" sub="Two inputs vary on a grid; the others stay at their nominal values. Circles are the training points."
          right={<><Status loading={surf.loading} error={surf.error} />
            <select className="inline" value={px} onChange={(e) => setPx(e.target.value)}>{d.names.map((nm) => <option key={nm} value={nm}>x: {nm}</option>)}</select>
            <select className="inline" value={py} onChange={(e) => setPy(e.target.value)}>{d.names.map((nm) => <option key={nm} value={nm}>y: {nm}</option>)}</select>
            <select className="inline" value={view} onChange={(e) => setView(e.target.value as any)}>
              <option value="pred">surrogate</option><option value="true">simulator</option><option value="error">error</option>
              {surf.data?.std && <option value="std">GP std</option>}
            </select></>}>
          {px === py ? <p className="muted">Pick two different inputs.</p> : surfPlot && <Plot data={surfPlot.data} layout={surfPlot.layout} height={380} />}
        </Card>
      )}
      <Card span={d.names.length >= 2 ? 5 : 12} title="Learning curve" sub="Test Q² vs number of training runs (same DoE method and box)."
        right={<><Status loading={lc.loading} error={lc.error} />
          <button className="btn small primary" onClick={() => lc.run("surrogate/learning_curve", { spec, dt: settings.dt, names: d.names, box: d.box, kinds: lcKinds, sizes: [8, 16, 32, 64, 128, 256], method: d.method === "factorial" ? "lhs" : d.method, qoi: settings.qoi })}>Compute</button></>}>
        <div style={{ marginBottom: 6 }}>
          {Object.entries(meta.surrogates).map(([k, v]) => (
            <label key={k} className="check" style={{ marginRight: 10, fontSize: 12 }}>
              <input type="checkbox" checked={lcKinds.includes(k)} disabled={!lcKinds.includes(k) && lcKinds.length >= 3}
                onChange={() => setLcKinds(lcKinds.includes(k) ? lcKinds.filter((x) => x !== k) : [...lcKinds, k])} />{v}
            </label>
          ))}
          <span className="muted" style={{ fontSize: 11 }}>(up to 3)</span>
        </div>
        {lcPlot ? <Plot data={lcPlot.data} layout={lcPlot.layout} height={300} /> : <p className="muted">Press “Compute” (it trains 6 models of each type).</p>}
      </Card>
    </div>
  );
}
