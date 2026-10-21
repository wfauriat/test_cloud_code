import { useEffect, useMemo, useState } from "react";
import type { Common } from "../App";
import { fmt, uncertainNames } from "../api";
import { useApi, useDebounced } from "../hooks";
import { Card, Lesson, Status } from "../components/ui";
import { Plot } from "../components/Plot";
import { colors, useThemeVersion } from "../theme";

export interface Design {
  names: string[];
  box: [number, number][];
  X: number[][];
  method: string;
}

interface DoeOut {
  names: string[];
  box: [number, number][];
  U: number[][];
  X: number[][];
  metrics: { min_distance: number; discrepancy: number; n: number };
  compare: Record<string, { min_distance: number; discrepancy: number }>;
}

export const DOE_LABELS: Record<string, string> = {
  random: "Random (MC)", lhs: "Latin hypercube", lhs_opt: "LHS, optimized", sobol: "Sobol", halton: "Halton", factorial: "Full factorial",
};

interface Props extends Common {
  design: Design | null;
  setDesign: (d: Design) => void;
  onUse: () => void;
}

export function DoeTab({ meta, spec, settings, setDesign, onUse }: Props) {
  // Default design inputs: the uncertain ones, except the wind (a nuisance input, opt in with its checkbox).
  const unc = uncertainNames(spec, meta).filter((nm) => nm !== "wind");
  const [names, setNames] = useState<string[]>(unc.length ? unc : ["v0", "theta"]);
  const [method, setMethod] = useState("lhs");
  const [n, setN] = useState(50);
  const [k, setK] = useState(3);
  const [seed, setSeed] = useState(0);
  const [override, setOverride] = useState<Record<string, [number, number]>>({});
  const doe = useApi<DoeOut>();
  const theme = useThemeVersion();
  const info = (nm: string) => meta.params.find((p) => p.name === nm)!;

  const ordered = meta.params.map((p) => p.name).filter((nm) => names.includes(nm));
  const body = useMemo(() => ({ spec, dt: settings.dt, names: ordered, method, n, k, seed,
    box_override: Object.fromEntries(Object.entries(override).filter(([nm]) => ordered.includes(nm))) }),
  [spec, settings.dt, ordered.join(","), method, n, k, seed, override]);
  const deb = useDebounced(body, 150);
  useEffect(() => { if (deb.names.length) doe.run("doe", deb); }, [deb, doe.run]);

  const d = doe.data;
  const levels = Math.max(2, Math.round(n ** (1 / Math.max(1, ordered.length))));

  // Lower-triangular matrix of pairwise scatter plots (plain SVG traces, no WebGL needed).
  const splom = useMemo(() => {
    if (!d) return null;
    const c = colors();
    const k = d.names.length;
    const col = (j: number) => d.X.map((r) => r[j]);
    const marker = { size: 6, color: c.s1, line: { color: c.surface, width: 1 } };
    const title = (nm: string) => ({ text: `${nm} [${info(nm).unit}]`, font: { size: 11 } });
    if (k === 1) {
      return { data: [{ x: col(0), y: col(0).map(() => 0), mode: "markers", marker, hovertemplate: "%{x:.3f}<extra></extra>" }],
        layout: { xaxis: { title: title(d.names[0]) }, yaxis: { visible: false }, showlegend: false }, height: 160 };
    }
    const m = k - 1;
    const gap = 0.035;
    const data: any[] = [];
    const layout: any = { showlegend: false, margin: { l: 60, r: 10, t: 10, b: 50 } };
    for (let row = 0; row < m; row++) {
      for (let cl = 0; cl <= row; cl++) {
        const i = cl;
        const j = row + 1;
        const idx = row * m + cl + 1;
        const ax = idx === 1 ? "" : String(idx);
        data.push({ x: col(i), y: col(j), mode: "markers", marker, xaxis: `x${ax}`, yaxis: `y${ax}`,
          hovertemplate: `${d.names[i]} = %{x:.3f}<br>${d.names[j]} = %{y:.3f}<extra></extra>` });
        layout[`xaxis${ax}`] = { domain: [cl / m + gap, (cl + 1) / m - gap], anchor: `y${ax}`, range: d.box[i],
          title: row === m - 1 ? title(d.names[i]) : undefined, showticklabels: row === m - 1, tickfont: { size: 10 } };
        layout[`yaxis${ax}`] = { domain: [1 - (row + 1) / m + gap, 1 - row / m - gap], anchor: `x${ax}`, range: d.box[j],
          title: cl === 0 ? title(d.names[j]) : undefined, showticklabels: cl === 0, tickfont: { size: 10 } };
      }
    }
    return { data, layout, height: Math.max(320, 170 * m) };
  }, [d, theme]);

  const compare = useMemo(() => {
    if (!d) return null;
    const c = colors();
    const ms = Object.keys(d.compare);
    const col = ms.map((m) => (m === method ? c.s1 : c.muted));
    const bars = (key: "min_distance" | "discrepancy", ax: string) => ({
      type: "bar", orientation: "h", y: ms.map((m) => DOE_LABELS[m]), x: ms.map((m) => d.compare[m][key]),
      marker: { color: col }, xaxis: `x${ax}`, yaxis: `y${ax}`, hovertemplate: "%{y}: %{x:.4f}<extra></extra>",
    });
    return {
      data: [bars("min_distance", ""), bars("discrepancy", "2")],
      layout: {
        grid: { rows: 1, columns: 2, pattern: "independent", xgap: 0.35 }, showlegend: false, bargap: 0.35,
        xaxis: { title: { text: "min. distance between points (higher = better)" } },
        xaxis2: { title: { text: "discrepancy (lower = better)" } },
        yaxis: { autorange: "reversed" }, yaxis2: { autorange: "reversed", showticklabels: false },
        margin: { l: 110, t: 8 },
      },
    };
  }, [d, method, theme]);

  const toggle = (nm: string) => setNames(names.includes(nm) ? names.filter((x) => x !== nm) : [...names, nm]);

  return (
    <div className="grid">
      <Lesson title="Lesson 3 — design of experiments: where to run the simulator" open>
        A surrogate model learns from a <b>training set</b>: a few well-chosen simulator runs inside a box of the input space.
        With a limited budget, the points should <b>fill the space</b> evenly.
        <ul>
          <li><b>Random</b> sampling leaves holes and clusters. <b>Latin hypercube</b> puts one point per row and per column of a grid, in every 1D projection.</li>
          <li><b>Sobol/Halton</b> are low-discrepancy sequences: they spread evenly and can be extended point by point.</li>
          <li>A <b>full factorial</b> grid needs levels<sup>d</sup> runs: it explodes with the dimension (curse of dimensionality), and its 1D projections collapse onto a few levels.</li>
          <li>Compare methods with the <b>min. distance</b> (avoid near-duplicates) and the <b>discrepancy</b> (gap to a perfectly uniform spread).</li>
        </ul>
      </Lesson>

      <section className="card">
        <div className="toolbar">
          <div className="field">Inputs of the design
            <div>{meta.params.map((p) => (
              <label key={p.name} className="check" style={{ marginRight: 10 }}>
                <input type="checkbox" checked={names.includes(p.name)} onChange={() => toggle(p.name)} />{p.name}
              </label>
            ))}</div>
          </div>
          <label className="field">Method
            <select value={method} onChange={(e) => setMethod(e.target.value)}>
              {meta.doe_methods.map((m) => <option key={m} value={m}>{DOE_LABELS[m] ?? m}</option>)}
            </select>
          </label>
          <label className="field">Points n
            <input type="number" min={2} max={2000} value={n} onChange={(e) => setN(Math.max(2, parseInt(e.target.value) || 2))} />
          </label>
          <label className="field">Box = mean ± k·σ, k =
            <input type="number" min={0.5} max={6} step={0.5} value={k} onChange={(e) => setK(parseFloat(e.target.value) || 3)} />
          </label>
          <label className="field">Seed <input type="number" value={seed} onChange={(e) => setSeed(parseInt(e.target.value) || 0)} /></label>
          <button className="btn primary" disabled={!d} onClick={() => { if (d) { setDesign({ names: d.names, box: d.box, X: d.X, method }); onUse(); } }}>
            Train a surrogate on this design →
          </button>
          <Status loading={doe.loading} error={doe.error} />
        </div>
        {method === "factorial" && <p className="muted" style={{ margin: "6px 0 0" }}>Full factorial: {levels} levels per input → {levels ** ordered.length} runs (n is rounded to levels^d).</p>}
        {!ordered.length && <p className="error">Select at least one input.</p>}
      </section>

      <Card span={7} title="Design points (pairwise projections)" sub="Every pair of inputs, in physical units, over the full box: look for holes and clusters.">
        {splom && <Plot data={splom.data} layout={splom.layout} height={splom.height} />}
      </Card>
      <Card span={5} title="Input box" sub="Bounds of the training domain. Edit a bound to override the mean ± k·σ default.">
        {d && (
          <table className="data">
            <thead><tr><th>input</th><th>lower</th><th>upper</th><th /></tr></thead>
            <tbody>
              {d.names.map((nm, j) => (
                <tr key={nm}>
                  <td>{info(nm).label} <span className="muted">[{info(nm).unit}]</span></td>
                  {[0, 1].map((side) => (
                    <td key={side}>
                      <input type="number" style={{ width: 80 }} step={info(nm).step} value={Number(d.box[j][side].toFixed(4))}
                        onChange={(e) => {
                          const v = parseFloat(e.target.value);
                          if (!isFinite(v)) return;
                          const b: [number, number] = [...d.box[j]] as [number, number];
                          b[side] = v;
                          setOverride({ ...override, [nm]: b });
                        }} />
                    </td>
                  ))}
                  <td>{override[nm] && <button className="btn small" onClick={() => { const o = { ...override }; delete o[nm]; setOverride(o); }}>reset</button>}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
        {d && <p className="muted" style={{ fontSize: 12 }}>
          This design: min. distance {fmt(d.metrics.min_distance, 4)}, discrepancy {fmt(d.metrics.discrepancy, 5)} (unit-cube scale), {d.metrics.n} points.
        </p>}
      </Card>
      <Card title={`Space-filling quality at n = ${n}`} sub="Same number of points and dimension for every method; the selected method is highlighted.">
        {compare && <Plot data={compare.data} layout={compare.layout} height={230} />}
      </Card>
    </div>
  );
}
