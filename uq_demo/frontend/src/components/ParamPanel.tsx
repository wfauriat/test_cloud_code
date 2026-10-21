import { useState } from "react";
import { post, uncertainNames, type Dist, type Meta, type ParamInfo, type Qoi, type Spec } from "../api";

export interface Settings {
  qoi: Qoi;
  target: number;
  tol: number;
  dt: number;
}

interface Props {
  meta: Meta;
  spec: Spec;
  setSpec: (s: Spec) => void;
  settings: Settings;
  setSettings: (s: Settings) => void;
  showUncertainty: boolean;
}

const DTS = [0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1];

/** The mean and std entered are those of X itself; show what that implies for each law. */
function lawNote(m: number, s: number, dist: Dist): string {
  if (dist === "uniform") {
    const h = Math.sqrt(3) * s;
    return `X ~ U[${(m - h).toPrecision(4)}, ${(m + h).toPrecision(4)}]`;
  }
  if (m <= 0) return "lognormal needs a positive mean";
  const sig = Math.sqrt(Math.log1p((s / m) ** 2));
  const mu = Math.log(m) - sig ** 2 / 2;
  return `ln X ~ N(μ = ${mu.toPrecision(4)}, σ = ${sig.toPrecision(3)}); median ${Math.exp(mu).toPrecision(4)}`;
}

export const stdMax = (p: ParamInfo) => (p.hi - p.lo) / (p.name === "wind" ? 6 : 8);

function Num({ value, onChange, step, min, max }: { value: number; onChange: (v: number) => void; step: number; min?: number; max?: number }) {
  return (
    <input type="number" value={Number(value.toFixed(4))} step={step} min={min} max={max}
      onChange={(e) => { const v = parseFloat(e.target.value); if (isFinite(v)) onChange(v); }} />
  );
}

export function ParamPanel({ meta, spec, setSpec, settings, setSettings, showUncertainty }: Props) {
  const [centering, setCentering] = useState(false);
  /** Mean of the QoI under the current inputs: Monte Carlo when some are uncertain, else the nominal run. */
  const meanQoi = async (qoi: Qoi): Promise<number> => {
    if (showUncertainty && uncertainNames(spec, meta).length) {
      const out = await post("propagate", { spec, dt: settings.dt, n: 1024, sampling: "sobol", n_traj: 0, qoi });
      return out.qoi[qoi].stats.mean;
    }
    const out = await post("simulate", { spec, dt: settings.dt });
    return out.qoi[qoi];
  };
  const center = async (qoi: Qoi) => {
    setCentering(true);
    try {
      const m = await meanQoi(qoi);
      setSettings({ ...settings, qoi, target: Math.round(m * 10) / 10 });
    } catch {
      setSettings({ ...settings, qoi });
    } finally {
      setCentering(false);
    }
  };
  const update = (name: string, patch: Partial<Spec[string]>) => setSpec({ ...spec, [name]: { ...spec[name], ...patch } });
  const q = meta.qois[settings.qoi];

  return (
    <aside className="sidebar">
      <div className="panel-title">Quantity of interest</div>
      <div className="toolbar">
        <label className="field">QoI
          <select value={settings.qoi} onChange={(e) => center(e.target.value as Qoi)}>
            {Object.entries(meta.qois).map(([k, v]) => <option key={k} value={k}>{v.label}</option>)}
          </select>
        </label>
        <div className="field">Target [{q.unit}]
          <div style={{ display: "flex", gap: 4 }}>
            <input type="number" value={settings.target} step={1} aria-label="Target" style={{ width: 70 }}
              onChange={(e) => setSettings({ ...settings, target: parseFloat(e.target.value) || 0 })} />
            <button className="btn small" disabled={centering} onClick={() => center(settings.qoi)}
              title="Set the target to the mean of the QoI under the current inputs (Monte Carlo if some are uncertain)">
              {centering ? "…" : "Center"}
            </button>
          </div>
        </div>
        <label className="field">± tol
          <input type="number" value={settings.tol} step={0.5} min={0.1} style={{ width: 60 }}
            onChange={(e) => setSettings({ ...settings, tol: Math.max(0.1, parseFloat(e.target.value) || 0.1) })} />
        </label>
        <label className="field">Euler dt [s]
          <select value={settings.dt} onChange={(e) => setSettings({ ...settings, dt: parseFloat(e.target.value) })}>
            {DTS.map((d) => <option key={d} value={d}>{d}</option>)}
          </select>
        </label>
      </div>

      <div className="panel-title" style={{ display: "flex", alignItems: "center" }}>
        <span style={{ flex: 1 }}>Input parameters</span>
        <button className="btn small" onClick={() => setSpec(structuredClone(meta.default_spec))}>Reset</button>
      </div>
      {meta.params.map((p) => {
        const e = spec[p.name];
        const unc = showUncertainty && e.uncertain;
        return (
          <div className="param" key={p.name}>
            <div className="param-head">
              <span className="name">{p.label}</span>
              <span className="unit">{p.unit}</span>
              {showUncertainty && (
                <button className={`toggle-unc ${e.uncertain ? "on" : ""}`} title="Treat this input as random"
                  onClick={() => update(p.name, { uncertain: !e.uncertain })}>
                  {e.uncertain ? "uncertain" : "fixed"}
                </button>
              )}
            </div>
            <div className="param-row">
              <label>{unc ? "mean" : "value"}</label>
              <input type="range" min={p.lo} max={p.hi} step={p.step} value={e.value}
                onChange={(ev) => update(p.name, { value: parseFloat(ev.target.value) })} />
              <Num value={e.value} step={p.step} min={p.lo} max={p.hi} onChange={(v) => update(p.name, { value: v })} />
            </div>
            {unc && (
              <>
                <div className="param-row">
                  <label>std</label>
                  <input type="range" min={0} max={stdMax(p)} step={p.step / 5} value={e.std}
                    onChange={(ev) => update(p.name, { std: parseFloat(ev.target.value) })} />
                  <Num value={e.std} step={p.step / 5} min={0} onChange={(v) => update(p.name, { std: Math.max(0, v) })} />
                </div>
                <div className="param-row">
                  <label>law</label>
                  <select className="dist-select" value={e.dist} onChange={(ev) => update(p.name, { dist: ev.target.value as Dist })}>
                    {meta.dists.map((d) => <option key={d} value={d} disabled={d === "lognormal" && e.value <= 0}>{d}</option>)}
                  </select>
                  <span className="muted" style={{ fontSize: 11 }}>
                    cv {e.value !== 0 ? `${((100 * e.std) / Math.abs(e.value)).toFixed(0)}%` : "–"}
                  </span>
                </div>
                {e.dist !== "normal" && <div className="law-note">{lawNote(e.value, e.std, e.dist)}</div>}
              </>
            )}
          </div>
        );
      })}
      <p className="muted" style={{ fontSize: 12, marginTop: 10 }}>
        Ball: diameter 0.22 m, air density 1.225 kg/m³. Drag and lift act through Cd/m and Cl/m, so a heavier ball
        is less affected by the air. Wind is horizontal (positive = tailwind). For every law, “mean” and “std” are the
        moments of the input itself (for a lognormal, μ and σ of ln X are derived from them).
      </p>
    </aside>
  );
}
