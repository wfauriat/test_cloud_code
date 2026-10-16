// Usage timeline (imports): per-call input split into cache read / cache write / uncached,
// with cache breaks marked. Answers Q2 and shows the real cost of each call.  PLAN §6.
import { useEffect, useLayoutEffect, useRef, useState } from "react";
import { api, type TimelineRow } from "../api/client";
import { fmt, kfmt, usd } from "../format";

const SERIES = [
  { key: "cache_read", label: "cache read", color: "var(--s1)" },
  { key: "cache_write", label: "cache write", color: "var(--s2)" },
  { key: "uncached", label: "uncached input", color: "var(--s3)" },
] as const;

export function Timeline({ sid }: { sid: string }) {
  const [rows, setRows] = useState<TimelineRow[]>([]);
  const [tip, setTip] = useState<{ x: number; y: number; r: TimelineRow } | null>(null);
  const ref = useRef<HTMLDivElement>(null);
  const [w, setW] = useState(900);
  useEffect(() => { api.timeline(sid).then(setRows); }, [sid]);
  useLayoutEffect(() => {
    const el = ref.current;
    if (!el) return;
    const ro = new ResizeObserver(() => setW(el.clientWidth));
    ro.observe(el);
    return () => ro.disconnect();
  }, []);

  if (!rows.length) return <div className="pad muted">No calls with usage in this session.</div>;
  const H = 260, L = 48, B = 22, T = 18;
  const max = Math.max(...rows.map((r) => r.total_input)) || 1;
  const slot = (w - L - 8) / rows.length;
  const bw = Math.max(Math.min(slot - 2, 28), 1);
  const yv = (v: number) => ((H - B - T) * v) / max;
  const ticks = [0, max / 2, max];
  const cost = rows.reduce((s, r) => s + r.cost, 0);
  const breaks = rows.filter((r) => r.cache_break);

  return (
    <div className="pad stack scroll">
      <div className="row">
        <b>Input per call</b>
        <span className="muted">{rows.length} calls · {usd(cost)} at list price · {breaks.length} cache break{breaks.length === 1 ? "" : "s"}</span>
        <span className="grow" />
        <div className="legend">
          {SERIES.map((s) => <span key={s.key}><span className="swatch" style={{ background: s.color }} />{s.label}</span>)}
          <span><span style={{ color: "var(--critical)" }}>▲</span> cache break</span>
        </div>
      </div>
      <div ref={ref} className="panel" style={{ position: "relative" }} onMouseLeave={() => setTip(null)}>
        <svg width={w - 22} height={H} role="img" aria-label="Stacked input tokens per call">
          {ticks.map((t) => (
            <g key={t}>
              <line x1={L} x2={w} y1={H - B - yv(t)} y2={H - B - yv(t)} stroke="var(--grid)" />
              <text x={L - 6} y={H - B - yv(t) + 4} textAnchor="end" fontSize={11} fill="var(--text-muted)">{kfmt(Math.round(t))}</text>
            </g>
          ))}
          {rows.map((r, i) => {
            const x = L + i * slot + (slot - bw) / 2;
            let acc = 0;
            return (
              <g key={r.n} onMouseMove={(e) => setTip({ x: e.clientX, y: e.clientY, r })}>
                <rect x={L + i * slot} y={T} width={slot} height={H - B - T} fill="transparent" />
                {SERIES.map((s) => {
                  const v = r[s.key];
                  const hgt = yv(v);
                  const y0 = H - B - yv(acc) - hgt;
                  acc += v;
                  return hgt > 0 ? <rect key={s.key} x={x} y={y0 + (hgt > 4 ? 1 : 0)} width={bw}
                    height={Math.max(hgt - (hgt > 4 ? 2 : 0), 0.5)} fill={s.color} rx={bw > 6 ? 1.5 : 0} /> : null;
                })}
                {r.cache_break && <text x={x + bw / 2} y={H - B - yv(r.total_input) - 4} textAnchor="middle" fontSize={11} fill="var(--critical)">▲</text>}
                {(rows.length <= 40 || i % Math.ceil(rows.length / 40) === 0) &&
                  <text x={x + bw / 2} y={H - 6} textAnchor="middle" fontSize={10} fill="var(--text-muted)">{r.n}</text>}
              </g>
            );
          })}
          <line x1={L} x2={w} y1={H - B} y2={H - B} stroke="var(--baseline)" />
        </svg>
        {tip && (
          <div className="tooltip" style={{ left: tip.x + 14, top: tip.y + 8 }}>
            <b>call {tip.r.n}</b> <span className="muted">{tip.r.timestamp?.slice(11, 19)}</span>
            {SERIES.map((s) => <div key={s.key} className="row"><span className="swatch" style={{ background: s.color }} />{s.label}: {fmt(tip.r[s.key])}</div>)}
            <div>output: {fmt(tip.r.output)} · {usd(tip.r.cost)}</div>
            {tip.r.cache_break && <div className="error">▲ break: −{fmt(tip.r.lost)} cached tokens ({tip.r.reason})</div>}
          </div>
        )}
      </div>
      <div className="panel scroll" style={{ maxHeight: 360 }}>
        <table className="data">
          <thead><tr><th>call</th><th className="l">time</th><th>total input</th><th>read</th><th>write</th><th>uncached</th><th>output</th><th className="l">ttl</th><th>cost</th><th className="l">note</th></tr></thead>
          <tbody>
            {rows.map((r) => (
              <tr key={r.n}>
                <td>{r.n}</td><td className="l mono">{r.timestamp?.slice(11, 19)}</td><td>{fmt(r.total_input)}</td>
                <td>{fmt(r.cache_read)}</td><td>{fmt(r.cache_write)}</td><td>{fmt(r.uncached)}</td><td>{fmt(r.output)}</td>
                <td className="l">{r.ttl}</td><td>{usd(r.cost)}</td>
                <td className="l">{r.cache_break ? <span className="error">▲ −{fmt(r.lost)} ({r.reason})</span> : ""}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
