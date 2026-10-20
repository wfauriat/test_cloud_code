import { useEffect, useMemo, useState } from "react";
import type { Common } from "../App";
import { fmt, uncertainNames } from "../api";
import { useApi } from "../hooks";
import { Card, Lesson, Status, Tile } from "../components/ui";
import { Plot } from "../components/Plot";
import { colors, useThemeVersion } from "../theme";
import type { TrainedModel } from "./SurrogateTab";

interface Cost { evaluations: number; seconds: number }
interface OatOut { base: number; rows: { name: string; x_lo: number; x_hi: number; y_lo: number; y_hi: number; swing: number }[]; cost: Cost; model: string }
interface MorrisOut { rows: { name: string; mu: number; mu_star: number; sigma: number }[]; cost: Cost; model: string }
interface SobolOut { rows: { name: string; S1: number; ST: number; S1_ci: [number, number]; ST_ci: [number, number] }[]; sum_S1: number; cost: Cost; model: string; n_base: number }

const RUN_COST: [string, number][] = [["actual (vectorized Euler)", 0], ["1 s / run", 1], ["1 min / run (CFD-like)", 60], ["1 h / run (large FE model)", 3600]];

function duration(s: number): string {
  if (s < 1) return `${(s * 1000).toFixed(0)} ms`;
  if (s < 120) return `${s.toFixed(1)} s`;
  if (s < 7200) return `${(s / 60).toFixed(0)} min`;
  if (s < 2 * 86400) return `${(s / 3600).toFixed(1)} h`;
  if (s < 2 * 365 * 86400) return `${(s / 86400).toFixed(0)} days`;
  return `${(s / (365 * 86400)).toFixed(1)} years`;
}

interface Props extends Common { model: TrainedModel | null }

export function SensitivityTab({ meta, spec, settings, model }: Props) {
  const names = uncertainNames(spec, meta);
  const surOk = !!model && model.qoi === settings.qoi && names.every((n) => model.names.includes(n));
  const [useSur, setUseSur] = useState(surOk);
  const [r, setR] = useState(20);
  const [levels, setLevels] = useState(4);
  const [nBase, setNBase] = useState(1024);
  const [runCost, setRunCost] = useState(60);
  const oat = useApi<OatOut>();
  const mor = useApi<MorrisOut>();
  const sob = useApi<SobolOut>();
  const theme = useThemeVersion();
  const q = meta.qois[settings.qoi];
  const label = (nm: string) => meta.params.find((p) => p.name === nm)!.label;

  const base = { spec, dt: settings.dt, qoi: settings.qoi, model_id: useSur && surOk ? model!.id : null };
  const runOat = () => oat.run("sensitivity", { ...base, method: "oat" });
  const runMorris = () => mor.run("sensitivity", { ...base, method: "morris", r, levels });
  const runSobol = () => sob.run("sensitivity", { ...base, method: "sobol", n_base: nBase });
  const runAll = () => { runOat(); runMorris(); runSobol(); };
  useEffect(() => { if (names.length) runAll(); }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const tornado = useMemo(() => {
    const o = oat.data;
    if (!o) return null;
    const c = colors();
    const ys = o.rows.map((rw) => label(rw.name));
    return {
      data: [
        { type: "bar", orientation: "h", y: ys, x: o.rows.map((rw) => rw.y_lo - o.base), base: o.base, name: "input at its 5% quantile",
          marker: { color: c.s1 }, customdata: o.rows.map((rw) => [rw.x_lo, rw.y_lo]), hovertemplate: "input = %{customdata[0]:.3f}<br>QoI = %{customdata[1]:.2f}<extra>5%</extra>" },
        { type: "bar", orientation: "h", y: ys, x: o.rows.map((rw) => rw.y_hi - o.base), base: o.base, name: "input at its 95% quantile",
          marker: { color: c.s2 }, customdata: o.rows.map((rw) => [rw.x_hi, rw.y_hi]), hovertemplate: "input = %{customdata[0]:.3f}<br>QoI = %{customdata[1]:.2f}<extra>95%</extra>" },
      ],
      layout: {
        barmode: "overlay", bargap: 0.35, yaxis: { autorange: "reversed" },
        xaxis: { title: { text: `${q.label} [${q.unit}]` } },
        shapes: [{ type: "line", x0: o.base, x1: o.base, yref: "paper", y0: 0, y1: 1, line: { color: c.text, width: 1.5 } }],
        margin: { l: 130 },
      },
    };
  }, [oat.data, theme]);

  const morrisPlot = useMemo(() => {
    const m = mor.data;
    if (!m) return null;
    const c = colors();
    const mx = Math.max(...m.rows.map((rw) => Math.max(rw.mu_star, rw.sigma))) * 1.15 || 1;
    return {
      data: [
        { x: [0, mx], y: [0, mx], mode: "lines", line: { color: c.muted, dash: "dash", width: 1 }, name: "σ = μ*", hoverinfo: "skip" },
        { x: m.rows.map((rw) => rw.mu_star), y: m.rows.map((rw) => rw.sigma), text: m.rows.map((rw) => rw.name), mode: "markers+text",
          textposition: "top right", textfont: { color: c.text2, size: 12 }, name: "inputs",
          marker: { size: 11, color: c.s1, line: { color: c.surface, width: 2 } }, hovertemplate: "%{text}<br>μ* = %{x:.3f}<br>σ = %{y:.3f}<extra></extra>" },
      ],
      layout: {
        xaxis: { title: { text: `μ* — mean |elementary effect| [${q.unit}]` }, range: [0, mx] },
        yaxis: { title: { text: "σ — non-linearity / interactions" }, range: [0, mx] }, showlegend: false,
        annotations: [{ x: mx * 0.25, y: mx * 0.92, text: "above the diagonal: non-linear or interacting", showarrow: false, font: { size: 11, color: c.muted } }],
      },
    };
  }, [mor.data, theme]);

  const sobolPlot = useMemo(() => {
    const s = sob.data;
    if (!s) return null;
    const c = colors();
    const ys = s.rows.map((rw) => label(rw.name));
    const err = (key: "S1" | "ST", ci: "S1_ci" | "ST_ci") => ({
      type: "data", symmetric: false, array: s.rows.map((rw) => rw[ci][1] - rw[key]), arrayminus: s.rows.map((rw) => rw[key] - rw[ci][0]),
      color: c.text2, thickness: 1.2, width: 4,
    });
    return {
      data: [
        { type: "bar", x: ys, y: s.rows.map((rw) => rw.S1), name: "first order S₁ (alone)", marker: { color: c.s1 }, error_y: err("S1", "S1_ci"),
          hovertemplate: "%{x}<br>S₁ = %{y:.3f}<extra></extra>" },
        { type: "bar", x: ys, y: s.rows.map((rw) => rw.ST), name: "total S_T (incl. interactions)", marker: { color: c.s2 }, error_y: err("ST", "ST_ci"),
          hovertemplate: "%{x}<br>S_T = %{y:.3f}<extra></extra>" },
      ],
      layout: { barmode: "group", bargap: 0.3, bargroupgap: 0.08, yaxis: { title: { text: "share of output variance" }, range: [0, 1.05] } },
    };
  }, [sob.data, theme]);

  const costs = [["One-at-a-time", oat.data], ["Morris", mor.data], ["Sobol", sob.data]] as [string, { cost: Cost; model: string } | null][];

  return (
    <div className="grid">
      <Lesson title="Lesson 5 — which inputs drive the output uncertainty?" open>
        Sensitivity analysis ranks the uncertain inputs, so you know where to reduce uncertainty, and which inputs can be fixed.
        <ul>
          <li><b>One-at-a-time (tornado)</b>: move each input to its 5% and 95% quantiles, the others staying at nominal. It is cheap (2d+1 runs) but local, and blind to interactions.</li>
          <li><b>Morris screening</b>: r random one-at-a-time paths. μ* ranks importance, σ flags non-linearity or interactions. It costs r(d+1) runs.</li>
          <li><b>Sobol indices</b> split the output variance: S₁ is the share explained by an input alone, S_T includes its interactions. The gap S_T − S₁ measures interactions. It costs N(d+2) runs, which is why a <b>surrogate</b> is used.</li>
        </ul>
      </Lesson>

      <section className="card">
        <div className="toolbar">
          <div className="field">Model evaluated
            <div>
              <label className="check" style={{ marginRight: 12 }}><input type="radio" checked={!useSur || !surOk} onChange={() => setUseSur(false)} />simulator</label>
              <label className="check"><input type="radio" checked={useSur && surOk} disabled={!surOk} onChange={() => setUseSur(true)} />
                surrogate {model ? `(${model.label}, ${model.n_train} runs)` : "(train one first)"}</label>
            </div>
          </div>
          <button className="btn primary" onClick={runAll} disabled={!names.length}>Run all three</button>
        </div>
        {model && !surOk && <p className="muted" style={{ fontSize: 12, margin: "6px 0 0" }}>The trained surrogate does not match: it must predict {q.label.toLowerCase()} and cover every uncertain input ({names.join(", ")}). Retrain it in tab 4.</p>}
        {!names.length && <p className="error">No uncertain input: toggle some parameters to "uncertain" in the left panel.</p>}
      </section>

      <Card span={6} title="One-at-a-time (tornado)" sub="Output when each input sits at its 5% or 95% quantile; the vertical line is the nominal output."
        right={<><Status loading={oat.loading} error={oat.error} /><button className="btn small" onClick={runOat}>Run</button></>}>
        {tornado && <Plot data={tornado.data} layout={tornado.layout} height={300} />}
      </Card>
      <Card span={6} title="Morris screening" sub="Important inputs sit to the right; inputs above the diagonal act non-linearly or interact."
        right={<><Status loading={mor.loading} error={mor.error} />
          <label className="field" style={{ flexDirection: "row", alignItems: "center" }}>r <input type="number" value={r} min={2} max={500} style={{ width: 60 }} onChange={(e) => setR(parseInt(e.target.value) || 20)} /></label>
          <label className="field" style={{ flexDirection: "row", alignItems: "center" }}>levels <input type="number" value={levels} min={2} max={10} style={{ width: 50 }} onChange={(e) => setLevels(parseInt(e.target.value) || 4)} /></label>
          <button className="btn small" onClick={runMorris}>Run</button></>}>
        {morrisPlot && <Plot data={morrisPlot.data} layout={morrisPlot.layout} height={300} />}
      </Card>
      <Card span={8} title="Sobol indices" sub="Error bars are 95% bootstrap confidence intervals. Increase N to tighten them."
        right={<><Status loading={sob.loading} error={sob.error} />
          <select className="inline" value={nBase} onChange={(e) => setNBase(+e.target.value)}>
            {[128, 256, 512, 1024, 2048, 4096, 8192].map((v) => <option key={v} value={v}>N = {v}</option>)}
          </select>
          <button className="btn small" onClick={runSobol}>Run</button></>}>
        {sobolPlot && <Plot data={sobolPlot.data} layout={sobolPlot.layout} height={300} />}
        {sob.data && (
          <div className="tiles" style={{ marginTop: 8 }}>
            <Tile label="Σ S₁" value={fmt(sob.data.sum_S1, 3)} note="1 means a purely additive model" />
            <Tile label="Interaction share" value={fmt(Math.max(0, 1 - sob.data.sum_S1), 3)} note="1 − Σ S₁" />
            <Tile label="Most influential" value={label(sob.data.rows.reduce((a, b) => (b.ST > a.ST ? b : a)).name)} note="largest S_T" />
          </div>
        )}
      </Card>
      <Card span={4} title="Computational budget" sub="Model runs used by each method, and what they would cost with an expensive simulator."
        right={<select className="inline" value={runCost} onChange={(e) => setRunCost(+e.target.value)}>
          {RUN_COST.map(([l, v]) => <option key={v} value={v}>{l}</option>)}</select>}>
        <table className="data">
          <thead><tr><th>method</th><th>runs</th><th>time</th></tr></thead>
          <tbody>
            {costs.map(([nm, out]) => (
              <tr key={nm}><td>{nm} <span className="muted">{out ? `(${out.model})` : ""}</span></td>
                <td>{out ? out.cost.evaluations.toLocaleString() : "–"}</td>
                <td>{!out ? "–" : runCost === 0 || out.model === "surrogate" ? duration(out.cost.seconds) : duration(out.cost.evaluations * runCost)}</td></tr>
            ))}
            {useSur && surOk && model && (
              <tr><td>surrogate training</td><td>{model.n_train}</td><td>{runCost === 0 ? "–" : duration(model.n_train * runCost)}</td></tr>
            )}
          </tbody>
        </table>
        <p className="muted" style={{ fontSize: 12 }}>
          {useSur && surOk ? "On the surrogate, only its training runs call the real simulator; every other evaluation is a cheap prediction."
            : "Every evaluation above is a real simulator run. Switch to the surrogate to compare."}
        </p>
      </Card>
    </div>
  );
}
