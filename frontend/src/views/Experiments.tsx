// Next-step A/B: same cut point, different contexts; compare what the model proposes next.
// PLAN §5.4, Q5 (curated vs. as-is vs. the server baseline), Q8 (+ brief). Preview the cost first.
import { useEffect, useState } from "react";
import { api, type ABPreview, type ABRun, type RunRecord, type TimelineRow } from "../api/client";
import { fmt, usd } from "../format";

const ARMS = ["as_is", "curated", "server_clear", "curated_brief"];
const ARM_LABEL: Record<string, string> = {
  as_is: "as is", curated: "curated (staged ops)", server_clear: "server clear_tool_uses", curated_brief: "curated + brief",
};

export function Experiments({ sid }: { sid: string }) {
  const [rows, setRows] = useState<TimelineRow[]>([]);
  const [spec, setSpec] = useState({ call_n: null as number | null, arms: ARMS, keep_n: 3, model: "claude-opus-5-5", effort: "medium", system_text: "" });
  const [pv, setPv] = useState<ABPreview | null>(null);
  const [run, setRun] = useState<ABRun | null>(null);
  const [runs, setRuns] = useState<RunRecord[]>([]);
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string | null>(null);
  const [verdict, setVerdict] = useState({ preferred: "", notes: "" });
  useEffect(() => { api.timeline(sid).then(setRows); api.abRuns(sid).then(setRuns); setPv(null); setRun(null); }, [sid]);
  const body = { ...spec, system_text: spec.system_text || null };
  const go = async <T,>(p: Promise<T>, then: (x: T) => void) => {
    setBusy(true);
    try { then(await p); setErr(null); } catch (e) { setErr(String(e)); } finally { setBusy(false); }
  };

  return (
    <div className="split pad">
      <div className="stack scroll">
        <div className="panel stack">
          <h3>Next-step A/B</h3>
          <div className="muted">Replays one cut point under several contexts. Tools are declared, never run; thinking is stripped in every arm (PLAN D12). Costs real money on your key: preview first.</div>
          <label className="row">cut before call
            <select value={spec.call_n ?? ""} onChange={(e) => setSpec({ ...spec, call_n: e.target.value === "" ? null : Number(e.target.value) })}>
              <option value="">end of session</option>
              {rows.map((r) => <option key={r.n} value={r.n}>call {r.n} ({fmt(r.total_input)} tok)</option>)}
            </select></label>
          <div className="row">{ARMS.map((a) => (
            <label key={a}><input type="checkbox" checked={spec.arms.includes(a)}
              onChange={(e) => setSpec({ ...spec, arms: e.target.checked ? [...spec.arms, a] : spec.arms.filter((x) => x !== a) })} /> {ARM_LABEL[a]}</label>
          ))}</div>
          <div className="row">
            <label>keep N tool results (server arm) <input type="number" min={0} value={spec.keep_n} style={{ width: 60 }} onChange={(e) => setSpec({ ...spec, keep_n: Number(e.target.value) })} /></label>
            <label>model <select value={spec.model} onChange={(e) => setSpec({ ...spec, model: e.target.value })}>
              {["claude-opus-5-5", "claude-sonnet-5-5", "claude-haiku-5-5", "claude-fable-5-1"].map((m) => <option key={m}>{m}</option>)}</select></label>
            <label>effort <select value={spec.effort} onChange={(e) => setSpec({ ...spec, effort: e.target.value })}>
              {["low", "medium", "high", "xhigh", "max"].map((m) => <option key={m}>{m}</option>)}</select></label>
          </div>
          <textarea rows={2} placeholder="System prompt override (default: the logged snapshot, or a stand-in)" value={spec.system_text}
            onChange={(e) => setSpec({ ...spec, system_text: e.target.value })} />
          <div className="row">
            <button disabled={busy || !spec.arms.length} onClick={() => go(api.abPreview(sid, body), setPv)}>Preview cost</button>
            <button className="primary" disabled={busy || !pv} onClick={() => go(api.abRun(sid, body), (r) => { setRun(r); api.abRuns(sid).then(setRuns); })}>
              {busy ? "Running…" : `Run${pv ? ` (~${usd(pv.total_cost_est)})` : ""}`}</button>
          </div>
          {err && <div className="error">{err}</div>}
        </div>
        {pv && (
          <div className="panel">
            <table className="data">
              <thead><tr><th className="l">arm</th><th>messages</th><th>tokens</th><th>shared with arm 1</th><th>est. cost</th><th className="l">validator</th></tr></thead>
              <tbody>{pv.arms.map((a) => (
                <tr key={a.arm}><td className="l">{ARM_LABEL[a.arm]}</td><td>{a.messages}</td>
                  <td>{a.tokens_exact != null ? `${fmt(a.tokens_exact)} exact` : `~${fmt(a.tokens_est)}`}</td><td>{fmt(a.shared_with_first)}</td>
                  <td>{usd(a.cost_est)}</td><td className="l">{a.validation.length ? <span className="error">{a.validation.map((d) => d.code).join(", ")}</span> : "ok"}</td></tr>
              ))}</tbody>
            </table>
            {!pv.brief && <div className="muted">No brief items: the "+ brief" arm is skipped.</div>}
          </div>
        )}
        <div className="panel">
          <h3>Past runs</h3>
          {runs.map((r) => (
            <div key={r.id} className="row">
              <button onClick={() => setRun(r.result ? { id: r.id, ...r.result } : null)}>open</button>
              <span className="mono muted">{r.created_at.slice(0, 19)}</span>
              <span>{r.verdict ? `preferred: ${String(r.verdict.preferred)}` : "no verdict"}</span>
            </div>
          ))}
        </div>
      </div>
      <div className="stack scroll">
        {run && (
          <>
            <div className="row" style={{ alignItems: "stretch" }}>
              {run.arms.map((a) => (
                <div key={a.arm} className="panel stack" style={{ flex: 1, minWidth: 0 }}>
                  <h3>{ARM_LABEL[a.arm]}</h3>
                  {a.error ? <div className="error">{a.error}</div> : (
                    <>
                      <div className="muted">{a.stop_reason} · {usd(a.cost ?? 0)} · read {fmt(Number(a.usage?.cache_read_input_tokens ?? 0))}</div>
                      {a.applied_edits && <div className="muted mono">server: {JSON.stringify(a.applied_edits)}</div>}
                      <pre>{(a.text ?? "").slice(0, 3000)}</pre>
                      {(a.tool_calls ?? []).map((t, i) => <pre key={i} className="mono secondary">→ {t.name}({JSON.stringify(t.input).slice(0, 400)})</pre>)}
                    </>
                  )}
                </div>
              ))}
            </div>
            <div className="panel row">
              <span>Verdict:</span>
              {run.arms.map((a) => <label key={a.arm}><input type="radio" checked={verdict.preferred === a.arm} onChange={() => setVerdict({ ...verdict, preferred: a.arm })} /> {ARM_LABEL[a.arm]}</label>)}
              <label><input type="radio" checked={verdict.preferred === "same"} onChange={() => setVerdict({ ...verdict, preferred: "same" })} /> no real difference</label>
              <input className="grow" placeholder="notes" value={verdict.notes} onChange={(e) => setVerdict({ ...verdict, notes: e.target.value })} />
              <button disabled={!verdict.preferred} onClick={() => api.abVerdict(sid, run.id, verdict).then(() => api.abRuns(sid).then(setRuns))}>Save</button>
            </div>
          </>
        )}
      </div>
    </div>
  );
}
