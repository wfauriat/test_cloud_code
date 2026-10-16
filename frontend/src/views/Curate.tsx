// Curate: proposals, ops, the brief, and the preview of what staged ops would change and cost.
// PLAN §5.2, §6 (staging dock + request view), Q3/Q4/Q8.
import { useEffect, useState } from "react";
import { api, type BriefItemView, type OpView, type Preview, type ProposalView, type RenderedRequest } from "../api/client";
import { fmt, usd } from "../format";

export function Curate({ sid, version, onChanged }: { sid: string; version: number; onChanged: () => void }) {
  const [props, setProps] = useState<ProposalView[]>([]);
  const [ops, setOps] = useState<OpView[]>([]);
  const [err, setErr] = useState<string | null>(null);
  useEffect(() => {
    api.proposals(sid).then(setProps).catch((e) => setErr(String(e)));
    api.ops(sid).then(setOps).catch((e) => setErr(String(e)));
  }, [sid, version]);
  const run = (p: Promise<unknown>) => p.then(() => { setErr(null); onChanged(); }).catch((e) => setErr(String(e)));
  const live = ops.filter((o) => o.state !== "revoked");
  const saved = props.reduce((s, p) => s + p.tokens_saved, 0);

  return (
    <div className="split pad">
      <div className="stack scroll">
        {err && <div className="error">{err}</div>}
        <div className="panel">
          <div className="row"><h3 className="grow">Rule proposals ({props.length}, ~{fmt(saved)} tokens per call)</h3>
            <button disabled={!props.length} onClick={() => run(api.stageProposals(sid, null))}>Stage all</button></div>
          <table className="data">
            <thead><tr><th className="l">rule</th><th className="l">why</th><th>saves</th><th /></tr></thead>
            <tbody>
              {props.map((p) => (
                <tr key={p.id}>
                  <td className="l"><span className="badge">{p.rule}</span></td>
                  <td className="l">{p.rationale} <span className="muted mono">{String(p.targets[0]?.event_id)}#{String(p.targets[0]?.index)}</span></td>
                  <td>{fmt(p.tokens_saved)}</td>
                  <td><button onClick={() => run(api.stageProposals(sid, [p.id]))}>Stage</button></td>
                </tr>
              ))}
            </tbody>
          </table>
          {!props.length && <div className="muted">No proposals (or all staged).</div>}
        </div>
        <div className="panel">
          <h3>Ops ({live.length} active)</h3>
          <table className="data">
            <thead><tr><th className="l">verb</th><th className="l">target</th><th className="l">author</th><th className="l">state</th><th /></tr></thead>
            <tbody>
              {ops.map((o) => (
                <tr key={o.id} style={{ opacity: o.state === "revoked" ? 0.45 : 1 }}>
                  <td className="l">{o.verb}</td>
                  <td className="l mono">{o.targets.map((t) => `${String(t.event_id)}#${String(t.index)}${t.start != null ? `[${String(t.start)}:${String(t.end)}]` : ""}`).join(", ")}</td>
                  <td className="l">{o.author}<div className="muted">{o.rationale}</div></td>
                  <td className="l"><span className="badge">{o.state}</span></td>
                  <td className="row">
                    {o.state === "staged" && <button onClick={() => run(api.opAction(sid, o.id, "unstage"))}>Unstage</button>}
                    {o.state === "draft" && <button onClick={() => run(api.opAction(sid, o.id, "stage"))}>Stage</button>}
                    {o.state !== "revoked" && <button onClick={() => run(api.opAction(sid, o.id, "revoke"))}>Revoke</button>}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <Brief sid={sid} version={version} onChanged={onChanged} />
      </div>
      <PreviewPanel sid={sid} version={version} />
    </div>
  );
}

function Brief({ sid, version, onChanged }: { sid: string; version: number; onChanged: () => void }) {
  const [items, setItems] = useState<BriefItemView[]>([]);
  const [type, setType] = useState("goal");
  const [text, setText] = useState("");
  useEffect(() => { api.brief(sid).then(setItems); }, [sid, version]);
  return (
    <div className="panel stack">
      <h3>Brief <span className="muted">(written by you only; sent once per user turn as a system message, PLAN D7)</span></h3>
      {items.map((i) => (
        <div key={i.id} className="row" style={{ opacity: i.status === "active" ? 1 : 0.45 }}>
          <span className="badge">{i.type}</span><span className="grow">{i.text}</span>
          <button onClick={() => api.updateBrief(sid, i.id, { status: i.status === "active" ? "archived" : "active" }).then(onChanged)}>
            {i.status === "active" ? "Archive" : "Restore"}</button>
        </div>
      ))}
      <div className="row">
        <select value={type} onChange={(e) => setType(e.target.value)}>
          {["goal", "constraint", "decision", "fact"].map((t) => <option key={t}>{t}</option>)}
        </select>
        <input className="grow" value={text} onChange={(e) => setText(e.target.value)} placeholder="e.g. Keep the public API unchanged"
          onKeyDown={(e) => { if (e.key === "Enter" && text.trim()) api.addBrief(sid, type, text.trim()).then(() => { setText(""); onChanged(); }); }} />
        <button disabled={!text.trim()} onClick={() => api.addBrief(sid, type, text.trim()).then(() => { setText(""); onChanged(); })}>Add</button>
      </div>
    </div>
  );
}

function PreviewPanel({ sid, version }: { sid: string; version: number }) {
  const [warm, setWarm] = useState(true);
  const [ttl, setTtl] = useState("5m");
  const [brief, setBrief] = useState(false);
  const [pv, setPv] = useState<Preview | null>(null);
  const [req, setReq] = useState<RenderedRequest | null>(null);
  const [err, setErr] = useState<string | null>(null);
  useEffect(() => {
    api.preview(sid, { warm, ttl, brief }).then((p) => { setPv(p); setErr(null); }).catch((e) => setErr(String(e)));
  }, [sid, version, warm, ttl, brief]);
  const e = pv?.economics;
  return (
    <div className="stack scroll">
      <div className="panel stack">
        <div className="row">
          <h3 className="grow">What the staged edits would do</h3>
          <label><input type="checkbox" checked={warm} onChange={(x) => setWarm(x.target.checked)} /> cache warm</label>
          <select value={ttl} onChange={(x) => setTtl(x.target.value)}><option>5m</option><option>1h</option></select>
          <label><input type="checkbox" checked={brief} onChange={(x) => setBrief(x.target.checked)} /> + brief</label>
        </div>
        {err && <div className="error">{err}</div>}
        {pv && e && (
          <>
            <div><b>{pv.diff.verdict === "identical" ? "Nothing staged." : pv.diff.summary}</b></div>
            <table className="data">
              <tbody>
                <tr><td className="l">tokens per call</td><td>{fmt(e.tokens_before)} → {fmt(e.tokens_after)}</td></tr>
                <tr><td className="l">next call, input side, without the edits</td><td>{usd(e.next_call_without)}</td></tr>
                <tr><td className="l">next call, input side, with the edits</td><td>{usd(e.next_call_with)}</td></tr>
                <tr><td className="l">each later call saves</td><td>{usd(e.savings_per_call)}</td></tr>
                <tr><td className="l">pays back after</td><td>{e.pays_back_after === null ? "never" : e.pays_back_after === 0 ? "immediately" : `${Math.ceil(e.pays_back_after)} calls`}</td></tr>
                <tr><td className="l">thinking blocks lost</td><td>{e.thinking_blocks_lost}</td></tr>
              </tbody>
            </table>
            <div className="secondary">{e.summary}{pv.calibrated ? "" : " (uncalibrated estimates)"}</div>
            <Diags title="Validator (with staged edits)" items={pv.validation_staged} empty="valid" />
            <Diags title="Repairs applied" items={pv.diagnostics} empty="none" />
            {pv.validation_base.length > 0 && <Diags title="Validator (history as it is)" items={pv.validation_base} empty="valid" />}
          </>
        )}
      </div>
      <div className="panel stack">
        <div className="row"><h3 className="grow">The request as it would be sent</h3>
          <button onClick={() => api.request(sid, { staged: true, brief }).then(setReq)}>Render</button></div>
        {req && (
          <>
            <div className="muted mono">~{fmt(req.tokens_estimated)} tokens (messages only) · hash {req.hash.slice(0, 12)} · {req.source_map.length} blocks</div>
            <Diags title="Validator" items={req.validation as unknown as { code: string; message: string; where: string }[]} empty="valid" />
            {(req.request.messages as { role: string; content: Record<string, unknown>[] }[]).map((m, k) => (
              <details key={k}>
                <summary className="mono">[{k}] {m.role} · {m.content.map((b) => String(b.type)).join(", ")}</summary>
                <pre className="mono">{JSON.stringify(m.content, null, 1).slice(0, 20000)}</pre>
              </details>
            ))}
          </>
        )}
      </div>
    </div>
  );
}

function Diags({ title, items, empty }: { title: string; items: { code: string; message: string; where: string }[]; empty: string }) {
  return (
    <div>
      <span className="secondary">{title}: </span>
      {items.length === 0 ? <span className="muted">{empty}</span> : (
        <ul style={{ margin: "2px 0", paddingLeft: 18 }}>
          {items.map((d, i) => <li key={i}><span className="mono">{d.code}</span> {d.where && <span className="muted mono">{d.where}</span>} {d.message}</li>)}
        </ul>
      )}
    </div>
  );
}
