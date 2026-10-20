import { useMemo, useState } from "react";
import type { Common } from "../App";
import { fmt, pct, uncertainNames, type Spec } from "../api";
import { useApi } from "../hooks";
import { Card, Lesson, Status } from "../components/ui";
import { Plot } from "../components/Plot";
import { stdMax } from "../components/ParamPanel";
import { colors, OBJECTIVE_COLOR, seqScale, useThemeVersion } from "../theme";

interface Opt {
  x: Record<string, number>;
  objective: number;
  mean: number;
  std: number;
  nominal: number;
  p_hit: number;
  validation: { mean: number; std: number; p_hit: number; kde: { x: number[]; y: number[] } };
}
interface RobustOut {
  design: string[];
  noise: string[];
  grid: { axes: number[][]; mean: number[][] | number[]; std: any; nominal: any; p_hit: any; objective: Record<string, any> };
  optima: Record<string, Opt>;
  surrogate?: { label: string; n_train: number; test: { r2: number; rmse: number } };
  model_calls: number;
  seconds_optim: number;
}
interface TolOut { design: string[]; axes: number[][]; p_hit: any; current_std: number[] }

const DEFAULT_BOUNDS: Record<string, [number, number]> = {
  v0: [20, 45], theta: [10, 70], cd: [0.1, 0.5], cl: [-0.2, 0.3], mass: [0.2, 1.5], wind: [-10, 10],
};
type View = "p_hit" | "mean" | "std" | "nominal" | "deterministic" | "mean_var" | "chance";
const VIEW_LABEL: Record<View, string> = {
  p_hit: "P(hit target)", mean: "mean of QoI", std: "std of QoI", nominal: "QoI with nominal inputs",
  deterministic: "objective: deterministic", mean_var: "objective: mean–variance", chance: "objective: 1 − P(hit)",
};

export function RobustTab({ meta, spec, setSpec, settings }: Common) {
  const [design, setDesign] = useState<string[]>(["v0", "theta"]);
  const [bounds, setBounds] = useState<Record<string, [number, number]>>(DEFAULT_BOUNDS);
  const [lam, setLam] = useState(1);
  const [nMc, setNMc] = useState(256);
  const [useSur, setUseSur] = useState(true);
  const [surKind, setSurKind] = useState("gp");
  const [view, setView] = useState<View>("p_hit");
  const [tolAt, setTolAt] = useState("chance");
  const rob = useApi<RobustOut>();
  const tol = useApi<TolOut>();
  const theme = useThemeVersion();
  const q = meta.qois[settings.qoi];
  const info = (nm: string) => meta.params.find((p) => p.name === nm)!;
  const axisTitle = (nm: string) => `mean ${info(nm).label.toLowerCase()} [${info(nm).unit}]`;
  const noise = uncertainNames(spec, meta);

  const run = () => rob.run("robust", {
    spec, dt: settings.dt, design, bounds: design.map((d) => bounds[d]), qoi: settings.qoi, target: settings.target,
    tol: settings.tol, lam, n_mc: nMc, grid: 31, use_surrogate: useSur, surrogate_kind: surKind, n_train: 200,
  });

  const specAt = (o: Opt): Spec => {
    const s = structuredClone(spec);
    for (const [k, v] of Object.entries(o.x)) s[k].value = v;
    return s;
  };

  const runTol = () => {
    const o = rob.data?.optima[tolAt];
    if (!o) return;
    const dv = rob.data!.design;
    tol.run("robust/tolerance", {
      spec: specAt(o), dt: settings.dt, design: dv, qoi: settings.qoi, target: settings.target, tol: settings.tol,
      std_max: dv.map((d) => Math.max(3 * (spec[d].uncertain ? spec[d].std : 0), stdMax(info(d)) / 4)), grid: 15, n_mc: 400,
    });
  };

  const r = rob.data;
  const landscape = useMemo(() => {
    if (!r) return null;
    const c = colors() as any;
    const z = view in r.grid.objective ? r.grid.objective[view] : (r.grid as any)[view];
    const markers = Object.entries(r.optima).map(([k, o]) => ({
      x: [o.x[r.design[0]]], y: r.design.length === 2 ? [o.x[r.design[1]]] : [view in r.grid.objective ? o.objective : (o as any)[view]],
      mode: "markers", name: meta.objectives[k], marker: { size: 13, color: c[OBJECTIVE_COLOR[k]], line: { color: c.surface, width: 2.5 }, symbol: "circle" },
      hovertemplate: `${meta.objectives[k]}<br>%{x:.2f}, %{y:.2f}<extra></extra>`,
    }));
    if (r.design.length === 2) {
      const [ax, ay] = r.grid.axes;
      const cur = { x: [spec[r.design[0]].value], y: [spec[r.design[1]].value], mode: "markers", name: "current design",
        marker: { size: 11, symbol: "x-thin", color: c.text, line: { width: 2.5, color: c.text } }, hoverinfo: "skip" };
      return {
        data: [
          { type: "contour", x: ax, y: ay, z, colorscale: seqScale(), reversescale: view.startsWith("d") || view === "mean_var" || view === "chance" || view === "std",
            contours: { coloring: "heatmap", showlabels: true, labelfont: { size: 10, color: c.text } }, line: { width: 0.5, color: c.surface },
            colorbar: { title: { text: VIEW_LABEL[view], side: "right", font: { size: 11 } }, thickness: 12, outlinewidth: 0, tickfont: { color: c.muted } },
            hovertemplate: `${r.design[0]} = %{x:.2f}<br>${r.design[1]} = %{y:.2f}<br>%{z:.3f}<extra></extra>`, showlegend: false },
          { type: "contour", x: ax, y: ay, z: r.grid.nominal, showscale: false, contours: { coloring: "none", start: settings.target, end: settings.target, size: 1 },
            line: { color: c.text, width: 2, dash: "dash" }, name: "nominal QoI = target", showlegend: true, hoverinfo: "skip" },
          cur, ...markers,
        ],
        layout: { xaxis: { title: { text: axisTitle(r.design[0]) } }, yaxis: { title: { text: axisTitle(r.design[1]) } } },
      };
    }
    const ax = r.grid.axes[0];
    const data: any[] = [];
    if (view === "mean") {
      const m = r.grid.mean as number[];
      const s = r.grid.std as number[];
      data.push({ x: ax, y: m.map((v, i) => v + s[i]), mode: "lines", line: { width: 0 }, showlegend: false, hoverinfo: "skip" });
      data.push({ x: ax, y: m.map((v, i) => v - s[i]), mode: "lines", line: { width: 0 }, fill: "tonexty", fillcolor: c.band, name: "mean ± 1 std", hoverinfo: "skip" });
    }
    data.push({ x: ax, y: z, mode: "lines", line: { color: c.text, width: 2 }, name: VIEW_LABEL[view], hovertemplate: "%{x:.2f}: %{y:.3f}<extra></extra>" });
    return {
      data: [...data, ...markers],
      layout: { xaxis: { title: { text: axisTitle(r.design[0]) } }, yaxis: { title: { text: VIEW_LABEL[view] } },
        shapes: view === "mean" || view === "nominal" ? [{ type: "rect", xref: "paper", x0: 0, x1: 1, y0: settings.target - settings.tol, y1: settings.target + settings.tol, fillcolor: c.band, line: { width: 0 }, layer: "below" }] : [] },
    };
  }, [r, view, theme, spec]);

  const validation = useMemo(() => {
    if (!r) return null;
    const c = colors() as any;
    return {
      data: Object.entries(r.optima).map(([k, o]) => ({
        x: o.validation.kde.x, y: o.validation.kde.y, mode: "lines", name: `${meta.objectives[k]} (P = ${pct(o.validation.p_hit)})`,
        line: { color: c[OBJECTIVE_COLOR[k]], width: 2.5 }, hovertemplate: "%{x:.1f}: %{y:.3f}<extra></extra>",
      })),
      layout: {
        xaxis: { title: { text: `${q.label} [${q.unit}] — simulator, fresh samples` } }, yaxis: { title: { text: "probability density" } },
        shapes: [{ type: "rect", x0: settings.target - settings.tol, x1: settings.target + settings.tol, yref: "paper", y0: 0, y1: 1, fillcolor: c.band, line: { width: 0 }, layer: "below" }],
      },
    };
  }, [r, theme]);

  const tolPlot = useMemo(() => {
    const t = tol.data;
    if (!t) return null;
    const c = colors();
    const cur = t.current_std;
    if (t.design.length === 2) {
      return {
        data: [
          { type: "contour", x: t.axes[0], y: t.axes[1], z: t.p_hit, colorscale: seqScale(), zmin: 0, zmax: 1,
            contours: { coloring: "heatmap", showlabels: true, start: 0.1, end: 0.9, size: 0.1, labelfont: { size: 10, color: c.text } },
            line: { width: 0.6, color: c.surface }, colorbar: { title: { text: "P(hit)", side: "right" }, thickness: 12, outlinewidth: 0, tickfont: { color: c.muted } },
            hovertemplate: `σ ${t.design[0]} = %{x:.3f}<br>σ ${t.design[1]} = %{y:.3f}<br>P(hit) = %{z:.3f}<extra></extra>` },
          { x: [cur[0]], y: [cur[1]], mode: "markers+text", text: ["current σ"], textposition: "top right", textfont: { color: c.text, size: 11 },
            marker: { size: 11, symbol: "x-thin", line: { width: 2.5, color: c.text } }, hoverinfo: "skip", showlegend: false },
        ],
        layout: { xaxis: { title: { text: `std of ${info(t.design[0]).label.toLowerCase()} [${info(t.design[0]).unit}]` } },
          yaxis: { title: { text: `std of ${info(t.design[1]).label.toLowerCase()} [${info(t.design[1]).unit}]` } } },
      };
    }
    return {
      data: [{ x: t.axes[0], y: t.p_hit, mode: "lines+markers", line: { color: c.s1, width: 2 }, marker: { size: 7, color: c.s1 }, name: "P(hit)" }],
      layout: { xaxis: { title: { text: `std of ${info(t.design[0]).label.toLowerCase()}` } }, yaxis: { title: { text: "P(hit)" }, range: [0, 1.02] },
        shapes: [{ type: "line", x0: cur[0], x1: cur[0], yref: "paper", y0: 0, y1: 1, line: { color: c.text2, dash: "dot" } }] },
    };
  }, [tol.data, theme]);

  const toggle = (nm: string) => {
    if (design.includes(nm)) setDesign(design.filter((d) => d !== nm));
    else setDesign([...design, nm].slice(-2));
  };

  return (
    <div className="grid">
      <Lesson title="Lesson 6 — robust design: hit the target despite uncertainty" open>
        You control the <b>means</b> of one or two design variables (e.g. launch speed and angle). Their std in the left panel is the
        <b> implementation tolerance</b>. The other uncertain inputs (<b>wind</b>, Cd…) are <b>nuisance parameters</b> you cannot control.
        <ul>
          <li><b>Deterministic</b> design: make the nominal trajectory land on the target (dashed curve). Infinitely many designs do this, and they are not equally robust!</li>
          <li><b>Mean–variance</b>: minimize (E[QoI] − target)² + λ·Var[QoI]. λ trades bias against spread.</li>
          <li><b>Chance</b>: maximize the probability of landing within target ± tol.</li>
          <li>Every candidate design is evaluated with the same random samples (common random numbers) on a surrogate. Each optimum is then <b>checked on the real simulator</b>.</li>
          <li>Finally, <b>tolerance allocation</b>: how precise must the speed and the angle be to reach a given hit probability?</li>
        </ul>
      </Lesson>

      <section className="card">
        <div className="toolbar">
          <div className="field">Design variables (pick 1 or 2)
            <div>{meta.params.map((p) => (
              <label key={p.name} className="check" style={{ marginRight: 10 }}>
                <input type="checkbox" checked={design.includes(p.name)} onChange={() => toggle(p.name)} />{p.name}
              </label>
            ))}</div>
          </div>
          {design.map((d) => (
            <div className="field" key={d}>bounds of mean {d}
              <div style={{ display: "flex", gap: 4 }}>
                {[0, 1].map((i) => (
                  <input key={i} type="number" style={{ width: 70 }} step={info(d).step} value={bounds[d][i]}
                    onChange={(e) => { const b: [number, number] = [...bounds[d]] as [number, number]; b[i] = parseFloat(e.target.value) || 0; setBounds({ ...bounds, [d]: b }); }} />
                ))}
              </div>
            </div>
          ))}
          <label className="field">λ (mean–variance)
            <input type="number" min={0} step={0.5} value={lam} onChange={(e) => setLam(Math.max(0, parseFloat(e.target.value) || 0))} />
          </label>
          <label className="field">MC samples / design
            <select value={nMc} onChange={(e) => setNMc(+e.target.value)}>{[64, 128, 256, 512, 1024].map((v) => <option key={v} value={v}>{v}</option>)}</select>
          </label>
          <label className="field">Model
            <select value={useSur ? surKind : "sim"} onChange={(e) => { if (e.target.value === "sim") setUseSur(false); else { setUseSur(true); setSurKind(e.target.value); } }}>
              <option value="gp">GP surrogate (200 runs)</option><option value="poly3">cubic surrogate (200 runs)</option><option value="sim">simulator (slow)</option>
            </select>
          </label>
          <button className="btn primary" onClick={run} disabled={!design.length || rob.loading}>Optimize</button>
          <Status loading={rob.loading} error={rob.error} />
        </div>
        <div style={{ marginTop: 6, fontSize: 13 }}>
          <span className="muted">Target: {q.label.toLowerCase()} = {settings.target} ± {settings.tol} {q.unit}. Uncertain inputs: </span>
          {noise.map((nm) => <span className="chip" key={nm}>{nm} σ={spec[nm].std}{design.includes(nm) ? " (tolerance)" : " (nuisance)"}</span>)}
          {!noise.includes("wind") && <span className="muted"> Tip: make the wind uncertain; it is the typical nuisance parameter.</span>}
        </div>
        {r?.surrogate && <p className="muted" style={{ fontSize: 12, margin: "6px 0 0" }}>
          Surrogate: {r.surrogate.label} on {r.surrogate.n_train} simulator runs, test Q² = {fmt(r.surrogate.test.r2, 4)}, RMSE = {fmt(r.surrogate.test.rmse, 3)} {q.unit}.
          {" "}{r.model_calls.toLocaleString()} surrogate evaluations in {fmt(r.seconds_optim, 1)} s.</p>}
      </section>

      {r && <>
        <Card span={7} title="Design landscape" sub={r.design.length === 2 ? "Each point is a candidate design (means); dots are the optima, × the current design. Along the dashed curve the nominal QoI equals the target." : "Each x is a candidate design (mean); dots are the optima."}
          right={<select className="inline" value={view} onChange={(e) => setView(e.target.value as View)}>
            {(Object.keys(VIEW_LABEL) as View[]).map((v) => <option key={v} value={v}>{VIEW_LABEL[v]}</option>)}</select>}>
          {landscape && <Plot data={landscape.data} layout={landscape.layout} height={420} />}
        </Card>
        <Card span={5} title="Check on the simulator" sub="Output distribution at each optimum: fresh Monte Carlo samples on the true simulator (not the surrogate).">
          {validation && <Plot data={validation.data} layout={validation.layout} height={420} />}
        </Card>
        <Card title="Optimal designs" sub="‘P(hit) est.’ comes from the optimizer (surrogate, common random numbers); ‘P(hit) check’ from 4000 fresh simulator runs.">
          <table className="data">
            <thead><tr><th>objective</th>{r.design.map((d) => <th key={d}>mean {d}</th>)}<th>nominal QoI</th><th>mean</th><th>std</th><th>P(hit) est.</th><th>P(hit) check</th><th /></tr></thead>
            <tbody>
              {Object.entries(r.optima).map(([k, o]) => (
                <tr key={k}>
                  <td><span className="swatch" style={{ background: `var(--series-${OBJECTIVE_COLOR[k].slice(1)})` }} />{meta.objectives[k]}</td>
                  {r.design.map((d) => <td key={d}>{fmt(o.x[d], 2)}</td>)}
                  <td>{fmt(o.nominal, 2)}</td><td>{fmt(o.validation.mean, 2)}</td><td>{fmt(o.validation.std, 2)}</td>
                  <td>{pct(o.p_hit)}</td><td><b>{pct(o.validation.p_hit)}</b></td>
                  <td><button className="btn small" onClick={() => setSpec(specAt(o))}>Apply to inputs</button></td>
                </tr>
              ))}
            </tbody>
          </table>
        </Card>
        <Card title="Tolerance allocation" sub="Hit probability as a function of the std of the design variables (normal tolerances), at the chosen optimum and with the nuisance inputs unchanged. Simulator runs."
          right={<><Status loading={tol.loading} error={tol.error} />
            <select className="inline" value={tolAt} onChange={(e) => setTolAt(e.target.value)}>
              {Object.keys(r.optima).map((k) => <option key={k} value={k}>at {meta.objectives[k].toLowerCase()} optimum</option>)}
            </select>
            <button className="btn small primary" onClick={runTol}>Compute</button></>}>
          {tolPlot ? <Plot data={tolPlot.data} layout={tolPlot.layout} height={380} />
            : <p className="muted">Press “Compute”: tighter tolerances raise P(hit), but the nuisance inputs (wind) cap it. Read off the tolerances needed for, e.g., P(hit) ≥ 0.8.</p>}
        </Card>
      </>}
    </div>
  );
}
