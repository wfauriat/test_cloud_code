import { useEffect, useMemo, useState } from "react";
import type { Common } from "../App";
import { fmt } from "../api";
import { useApi, useDebounced } from "../hooks";
import { Card, Lesson, Status, Tile } from "../components/ui";
import { Plot } from "../components/Plot";
import { TrajectoryView, type Limits, type Path } from "../components/TrajectoryView";
import { colors, useThemeVersion } from "../theme";

interface SimOut {
  trajectory: Path;
  qoi: Record<string, number>;
  landed: boolean;
  vacuum: Path & { range: number; max_height: number; flight_time: number };
  sweep: { theta: number[]; range: number[]; max_height: number[]; vacuum_range: number[] };
}
interface ConvOut { dt: number[]; range_error: number[]; height_error: number[]; reference_range: number }

export function SimulatorTab({ spec, settings }: Common) {
  const [scheme, setScheme] = useState<"euler" | "rk4">("euler");
  const [showVacuum, setShowVacuum] = useState(false);
  const [limits, setLimits] = useState<Limits>({});
  const [equal, setEqual] = useState(false);
  const [pins, setPins] = useState<Path[]>([]);
  const [anim, setAnim] = useState(1);
  const sim = useApi<SimOut>();
  const conv = useApi<ConvOut>();
  const theme = useThemeVersion();

  const body = useMemo(() => ({ spec, dt: settings.dt, scheme }), [spec, settings.dt, scheme]);
  const fast = useDebounced(body, 40);
  const slow = useDebounced(body, 300);
  useEffect(() => { sim.run("simulate", fast); }, [fast, sim.run]);
  useEffect(() => { conv.run("simulate/convergence", { spec: slow.spec }); }, [slow.spec, conv.run]);

  const d = sim.data;
  const theta = spec.theta.value;
  const sweepQoi = settings.qoi === "max_height" ? "max_height" : "range";

  const sweepPlot = useMemo(() => {
    if (!d) return null;
    const c = colors();
    const y = d.sweep[sweepQoi];
    const iBest = y.indexOf(Math.max(...y));
    const data: any[] = [
      { x: d.sweep.theta, y, name: "with air (drag, lift, wind)", mode: "lines", line: { color: c.s1, width: 2 },
        hovertemplate: "θ = %{x}°<br>%{y:.1f} m<extra></extra>" },
    ];
    if (sweepQoi === "range") {
      data.push({ x: d.sweep.theta, y: d.sweep.vacuum_range, name: "vacuum (exact)", mode: "lines",
        line: { color: c.muted, width: 1.5, dash: "dash" }, hovertemplate: "θ = %{x}°<br>%{y:.1f} m<extra></extra>" });
    }
    data.push({ x: [d.sweep.theta[iBest]], y: [y[iBest]], mode: "markers+text", showlegend: false,
      marker: { size: 9, color: c.s1, line: { color: c.surface, width: 2 } }, text: [`best ${d.sweep.theta[iBest]}°`],
      textposition: "top center", textfont: { color: c.text2, size: 11 }, hoverinfo: "skip" });
    return {
      data,
      layout: {
        xaxis: { title: { text: "launch angle θ [deg]" }, range: [0, 90], dtick: 15 },
        yaxis: { title: { text: sweepQoi === "range" ? "range [m]" : "max height [m]" }, rangemode: "tozero" },
        shapes: [{ type: "line", x0: theta, x1: theta, yref: "paper", y0: 0, y1: 1, line: { color: c.text2, width: 1, dash: "dot" } }],
        annotations: [{ x: theta, yref: "paper", y: 0.02, text: "current θ", showarrow: false, yanchor: "bottom", xanchor: "left", xshift: 3, font: { size: 11, color: c.text2 } }],
      },
    };
  }, [d, sweepQoi, theta, theme]);

  const convPlot = useMemo(() => {
    const cd = conv.data;
    if (!cd) return null;
    const c = colors();
    const keep = cd.dt.map((_, i) => i).filter((i) => cd.range_error[i] > 1e-9);
    const dts = keep.map((i) => cd.dt[i]);
    const err = keep.map((i) => cd.range_error[i]);
    const i0 = dts.length - 1;
    const ref = i0 >= 0 ? dts.map((t) => (err[i0] * t) / dts[i0]) : [];
    return {
      data: [
        { x: dts, y: err, name: "Euler range error", mode: "lines+markers", line: { color: c.s1, width: 2 },
          marker: { size: 8, color: c.s1, line: { color: c.surface, width: 2 } }, hovertemplate: "dt = %{x:.4f} s<br>error = %{y:.3g} m<extra></extra>" },
        { x: dts, y: ref, name: "slope 1 (first order)", mode: "lines", line: { color: c.muted, dash: "dash", width: 1.5 }, hoverinfo: "skip" },
      ],
      layout: {
        xaxis: { type: "log", dtick: 1, title: { text: "time step dt [s]" } },
        yaxis: { type: "log", dtick: 1, exponentformat: "power", title: { text: "|range − reference| [m]" } },
        shapes: [{ type: "line", x0: settings.dt, x1: settings.dt, yref: "paper", y0: 0, y1: 1, line: { color: c.text2, width: 1, dash: "dot" } }],
      },
    };
  }, [conv.data, settings.dt, theme]);

  const vac = d?.vacuum;
  return (
    <div className="grid">
      <Lesson title="Lesson 1 — a deterministic model and its numerical error" open>
        The projectile obeys Newton's law with gravity, quadratic drag (Cd), lift (Cl, e.g. backspin) and a horizontal wind.
        The ODE is integrated with the <b>explicit Euler</b> scheme: <code>v ← v + dt·a(v)</code>, <code>x ← x + dt·v</code>.
        <ul>
          <li>Move the sliders on the left: every input is a <b>fixed value</b> here. The model is deterministic.</li>
          <li>Compare with the dashed <b>vacuum parabola</b> (exact solution without air).</li>
          <li>The angle sweep shows that with drag the best angle drops below 45°, and that the curve is <b>flat near its maximum</b>, which matters later for robustness.</li>
          <li>Even a "deterministic" result has an error: the Euler error shrinks <b>linearly with dt</b> (first-order scheme).</li>
        </ul>
      </Lesson>

      <Card title="Trajectory" sub="Hover the curve to read positions. Pin a trajectory to compare with later settings."
        right={<>
          <Status loading={sim.loading} error={sim.error} />
          <label className="check"><input type="checkbox" checked={showVacuum} onChange={(e) => setShowVacuum(e.target.checked)} />vacuum</label>
          <label className="check"><input type="checkbox" checked={equal} onChange={(e) => setEqual(e.target.checked)} />true aspect</label>
          <select className="inline" value={scheme} onChange={(e) => setScheme(e.target.value as any)}>
            <option value="euler">Euler</option><option value="rk4">RK4</option>
          </select>
          <button className="btn small" onClick={() => d && setPins([...pins.slice(-5), d.trajectory])}>Pin</button>
          <button className="btn small" onClick={() => setPins([])} disabled={!pins.length}>Clear pins</button>
          <button className="btn small primary" onClick={() => setAnim(anim + 1)}>Fire ▶</button>
        </>}>
        <TrajectoryView main={d?.trajectory} vacuum={showVacuum ? vac : null} ghosts={pins} wind={spec.wind.value}
          equalAspect={equal} animateKey={anim} height={360}
          band={bandFor(settings.qoi, settings.target, settings.tol)} bandAxis={settings.qoi === "max_height" ? "y" : "x"}
          limits={limits} />
        <AxisLimits limits={limits} setLimits={setLimits} />
        <div className="legend">
          <span><span className="line" style={{ borderColor: "var(--series-1)" }} />current trajectory</span>
          {showVacuum && <span><span className="line" style={{ borderColor: "var(--text-muted)", borderTopStyle: "dashed" }} />vacuum parabola</span>}
          {pins.length > 0 && <span><span className="line" style={{ borderColor: "var(--text-muted)", opacity: 0.55 }} />pinned</span>}
          {bandFor(settings.qoi, settings.target, settings.tol) && <span><span className="swatch" style={{ background: "var(--band)" }} />target ± tol</span>}
        </div>
      </Card>

      <section className="card">
        <div className="tiles">
          <Tile label="Range" value={`${fmt(d?.qoi.range, 1)} m`} note={vac && `vacuum: ${fmt(vac.range, 1)} m`} />
          <Tile label="Max height" value={`${fmt(d?.qoi.max_height, 1)} m`} note={vac && `vacuum: ${fmt(vac.max_height, 1)} m`} />
          <Tile label="Flight time" value={`${fmt(d?.qoi.flight_time, 2)} s`} note={vac && `vacuum: ${fmt(vac.flight_time, 2)} s`} />
          <Tile label="Impact speed" value={`${fmt(d?.qoi.impact_speed, 1)} m/s`} note={`launch: ${fmt(spec.v0.value, 1)} m/s`} />
          {d && (() => {
            const gap = d.qoi[settings.qoi] - settings.target;
            return <Tile label="Distance to target" value={`${gap >= 0 ? "+" : ""}${fmt(gap, 1)}`}
              note={Math.abs(gap) <= settings.tol ? "✓ within tolerance" : "✗ outside tolerance"} />;
          })()}
        </div>
      </section>

      <Card span={6} collapsible defaultOpen={false} title={`${sweepQoi === "range" ? "Range" : "Max height"} vs launch angle`} sub="All other inputs at their current values.">
        {sweepPlot && <Plot data={sweepPlot.data} layout={sweepPlot.layout} height={300} />}
      </Card>
      <Card span={6} collapsible defaultOpen={false} title="Euler convergence" sub={`Error of the range against a fine RK4 reference (${fmt(conv.data?.reference_range, 2)} m). The dotted line is the dt used everywhere in the app.`}
        right={<Status loading={conv.loading} error={conv.error} />}>
        {convPlot && <Plot data={convPlot.data} layout={convPlot.layout} height={300} />}
      </Card>
    </div>
  );
}

/** Target band shown on the trajectory: on the ground for the range, in height for the max height. */
export function bandFor(qoi: string, target: number, tol: number): [number, number] | null {
  return qoi === "range" || qoi === "max_height" ? [target - tol, target + tol] : null;
}

/** Optional fixed axis limits for the trajectory view; an empty box means automatic. */
export function AxisLimits({ limits, setLimits }: { limits: Limits; setLimits: (l: Limits) => void }) {
  const box = (key: keyof Limits, placeholder: string) => (
    <input type="number" style={{ width: 64 }} placeholder={placeholder} value={limits[key] ?? ""}
      onChange={(e) => { const v = parseFloat(e.target.value); setLimits({ ...limits, [key]: isFinite(v) ? v : null }); }} />
  );
  const any = Object.values(limits).some((v) => typeof v === "number");
  return (
    <div className="toolbar" style={{ marginTop: 6, alignItems: "center", fontSize: 12 }}>
      <span className="muted">Axis limits (empty = auto):</span>
      <span>x {box("xmin", "0")} – {box("xmax", "auto")}</span>
      <span>y {box("ymin", "0")} – {box("ymax", "auto")}</span>
      {any && <button className="btn small" onClick={() => setLimits({})}>Auto</button>}
    </div>
  );
}
