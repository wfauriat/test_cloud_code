// Live: the agent loop with its two gates.  PLAN §5.3, Q6 (gate timings are logged by the backend).
// Keys at a gate: a = approve (prompt gate: send; tool gate: submit decisions).
import { useCallback, useEffect, useState } from "react";
import { api, type CallSummary, type LiveView, type MessageView, type ToolCard } from "../api/client";
import { fmt, usd } from "../format";

export function Live({ sid, source, version, onChanged, onCreated }: {
  sid: string | null; source: string | null; version: number; onChanged: () => void; onCreated: (sid: string) => void;
}) {
  const [creating, setCreating] = useState(false);
  if (!sid || source !== "live" || creating) {
    return <CreateLive onCreated={(s) => { setCreating(false); onCreated(s); }} onCancel={creating ? () => setCreating(false) : undefined} />;
  }
  return <LivePanel sid={sid} version={version} onChanged={onChanged} onNew={() => setCreating(true)} />;
}

function CreateLive({ onCreated, onCancel }: { onCreated: (sid: string) => void; onCancel?: () => void }) {
  const [f, setF] = useState({ title: "live session", workspace: "~/curator-sandbox", model: "claude-opus-5-5",
    effort: "medium", ttl: "5m", allow_commands: false, fallbacks: true });
  const [err, setErr] = useState<string | null>(null);
  const set = (k: string, v: unknown) => setF((x) => ({ ...x, [k]: v }));
  return (
    <div className="pad"><div className="panel stack" style={{ maxWidth: 560 }}>
      <h3>New live session</h3>
      <div className="muted">System prompt and tools are frozen when the session is created (PLAN D11). Tools work inside the workspace folder only.</div>
      <label className="row">title <input className="grow" value={f.title} onChange={(e) => set("title", e.target.value)} /></label>
      <label className="row">workspace <input className="grow mono" value={f.workspace} onChange={(e) => set("workspace", e.target.value)} /></label>
      <div className="row">
        <label>model <select value={f.model} onChange={(e) => set("model", e.target.value)}>
          {["claude-opus-5-5", "claude-sonnet-5-5", "claude-haiku-5-5", "claude-fable-5-1"].map((m) => <option key={m}>{m}</option>)}</select></label>
        <label>effort <select value={f.effort} onChange={(e) => set("effort", e.target.value)}>
          {["low", "medium", "high", "xhigh", "max"].map((m) => <option key={m}>{m}</option>)}</select></label>
        <label>cache TTL <select value={f.ttl} onChange={(e) => set("ttl", e.target.value)}><option>5m</option><option>1h</option></select></label>
      </div>
      <label><input type="checkbox" checked={f.allow_commands} onChange={(e) => set("allow_commands", e.target.checked)} /> declare run_command (always reviewed; runs on this machine)</label>
      <label><input type="checkbox" checked={f.fallbacks} onChange={(e) => set("fallbacks", e.target.checked)} /> server-side refusal fallback (the UI says when another model answered)</label>
      {err && <div className="error">{err}</div>}
      <div className="row"><button className="primary" onClick={() => api.createLive(f).then((s) => onCreated(s.id)).catch((e) => setErr(String(e)))}>Create</button>
        {onCancel && <button onClick={onCancel}>Cancel</button>}</div>
    </div></div>
  );
}

function LivePanel({ sid, version, onChanged, onNew }: { sid: string; version: number; onChanged: () => void; onNew: () => void }) {
  const [v, setV] = useState<LiveView | null>(null);
  const [calls, setCalls] = useState<CallSummary[]>([]);
  const [msgs, setMsgs] = useState<MessageView[]>([]);
  const [text, setText] = useState("");
  const [wire, setWire] = useState<{ title: string; body: unknown } | null>(null);
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState<string | null>(null);
  useEffect(() => {
    api.live(sid).then(setV).catch((e) => setErr(String(e)));
    api.calls(sid).then(setCalls);
    api.messages(sid).then(setMsgs);
  }, [sid, version]);
  const run = useCallback(async (p: Promise<LiveView>) => {
    setBusy(true);
    try { setV(await p); setErr(null); } catch (e) { setErr(String(e)); } finally { setBusy(false); onChanged(); }
  }, [onChanged]);

  if (!v) return <div className="pad muted">{err ?? "loading…"}</div>;
  const canSend = v.state === "idle" || v.state === "blocked";
  return (
    <div className="split pad">
      <div className="stack scroll">
        <div className="panel row">
          <span className={`badge ${v.state === "blocked" ? "dropped" : ""}`}>{v.state}</span>
          <span className="muted">epoch {v.epoch} · {v.calls} calls · {v.model} · {v.workspace}</span>
          <span className="grow" />
          <label><input type="checkbox" checked={v.auto_continue} onChange={(e) => run(api.liveSettings(sid, e.target.checked))} /> auto-send after tool results</label>
          <button disabled={busy || v.state === "idle"} onClick={() => run(api.liveReset(sid))}
            title="Back to idle, keeping the history (calls waiting at the tool gate are marked cancelled)">Reset gate</button>
          <button onClick={onNew}>New live session</button>
          <a href={api.exportUrl(sid)} download><button>Export session</button></a>
          <button disabled={!v.staged_ops || busy} onClick={() => run(api.liveApply(sid))}
            title="Apply staged edits to sent history (rebuild): costs a cache rewrite and the thinking after the first change">
            Apply {v.staged_ops} staged edit{v.staged_ops === 1 ? "" : "s"} to history</button>
        </div>
        {v.note && <div className="panel secondary">{v.note}</div>}
        {err && <div className="panel error">{err}</div>}
        {(v.state === "prompt_gate" || v.state === "blocked") && v.pending && <PromptGate v={v} busy={busy}
          approve={() => run(api.liveApprove(sid, v.pending!.hash))} reject={() => run(api.liveReject(sid, ""))}
          view={() => api.pendingRequest(sid).then((r) => setWire({ title: "Waiting request (exactly what Approve would send)", body: r.request }))} />}
        {v.state === "tool_gate" && <ToolGate cards={v.tool_cards} busy={busy} submit={(d) => run(api.liveTools(sid, d))} />}
        <div className="panel stack">
          <textarea rows={3} value={text} onChange={(e) => setText(e.target.value)} disabled={!canSend}
            placeholder={canSend ? "Message (Ctrl+Enter to send). The brief, if any, is appended after it." : "waiting at a gate…"}
            onKeyDown={(e) => { if (e.key === "Enter" && e.ctrlKey && text.trim()) { run(api.liveMessage(sid, text)); setText(""); } }} />
          <div><button className="primary" disabled={!canSend || !text.trim() || busy}
            onClick={() => { run(api.liveMessage(sid, text)); setText(""); }}>Send</button></div>
        </div>
        <div className="panel stack">
          <h3>Last messages <span className="muted">(full view in Look; edits there are staged)</span></h3>
          {msgs.slice(-8).map((m) => (
            <div key={m.event_id}><b>{m.label}</b> <span className="muted">{fmt(m.tokens)} tok</span>
              {m.blocks.map((b) => <div key={b.index} className="secondary" style={{ marginLeft: 10 }}>{b.type === "text" ? b.text.slice(0, 400) : b.gist}</div>)}
            </div>
          ))}
        </div>
      </div>
      <div className="stack scroll">
        <div className="panel">
          <h3>Calls (wire log)</h3>
          <table className="data">
            <thead><tr><th>#</th><th>epoch</th><th className="l">model</th><th className="l">stop</th><th>read</th><th>write</th><th>uncached</th><th>out</th><th>cost</th><th>ms</th></tr></thead>
            <tbody>
              {calls.map((c, i) => {
                const u = (c.usage ?? {}) as Record<string, number>;
                return (
                  <tr key={c.id} style={{ cursor: "pointer" }} title="show the exact request and the raw response"
                    onClick={() => api.callDetail(sid, c.id).then((d) => setWire({ title: `Call ${i}: exact request and raw response`, body: { request: d.request, response: d.response, error: d.error } }))}>
                    <td>{i}</td><td>{c.epoch}</td><td className="l">{c.model}</td>
                    <td className="l">{c.error ? <span className="error" title={c.error}>error</span> : c.stop_reason}</td>
                    <td>{fmt(u.cache_read_input_tokens ?? 0)}</td><td>{fmt(u.cache_creation_input_tokens ?? 0)}</td>
                    <td>{fmt(u.input_tokens ?? 0)}</td><td>{fmt(u.output_tokens ?? 0)}</td>
                    <td>{c.cost != null ? usd(c.cost) : ""}</td><td>{c.latency_ms ?? ""}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
          <div className="muted">Click a row for the exact request sent and the raw response.</div>
        </div>
        {wire && (
          <div className="panel stack">
            <div className="row"><h3 className="grow">{wire.title}</h3>
              <button onClick={() => navigator.clipboard?.writeText(JSON.stringify(wire.body, null, 1))}>Copy</button>
              <button onClick={() => setWire(null)}>Close</button></div>
            <pre className="mono">{JSON.stringify(wire.body, null, 1)}</pre>
          </div>
        )}
      </div>
    </div>
  );
}

function PromptGate({ v, busy, approve, reject, view }: { v: LiveView; busy: boolean; approve: () => void; reject: () => void; view: () => void }) {
  const p = v.pending!;
  const [left, setLeft] = useState<number | null>(p.cache_expires_in);
  useEffect(() => {
    setLeft(p.cache_expires_in);
    const t = setInterval(() => setLeft((x) => (x == null ? x : Math.max(x - 1, 0))), 1000);
    return () => clearInterval(t);
  }, [p.hash, p.cache_expires_in]);
  useEffect(() => {
    const k = (e: KeyboardEvent) => { if (e.key === "a" && !(e.target as HTMLElement).closest("input,textarea") && v.state === "prompt_gate") approve(); };
    window.addEventListener("keydown", k);
    return () => window.removeEventListener("keydown", k);
  }, [approve, v.state]);
  return (
    <div className="panel stack" style={{ borderColor: "var(--accent)" }}>
      <h3>Prompt gate: the next request</h3>
      <div><b>{p.summary}</b></div>
      <div className="kv">
        <span className="k">tokens</span><span>~{fmt(p.tokens_est)} estimated{p.tokens_exact != null ? ` · ${fmt(p.tokens_exact)} exact` : ""}</span>
        <span className="k">cost (input)</span><span>{usd(p.cost.read_cost)} read + {usd(p.cost.write_cost)} write = {usd(p.cost.total)}</span>
        <span className="k">cache</span><span>{p.warm ? `warm, expires in ${fmtTime(left)}` : "cold (full write)"}</span>
        {p.free_ops.length > 0 && <><span className="k">free edits</span><span>{p.free_ops.length} staged op(s) on unsent content go out now</span></>}
        {p.rebuild_pending && <><span className="k">rebuild</span><span>this request applies your edits to history (new epoch)</span></>}
      </div>
      {p.validation.length > 0 && <div className="error">Validator: {p.validation.map((d) => `${d.code} ${d.where} ${d.message}`).join("; ")}</div>}
      {p.diagnostics.length > 0 && <div className="muted">Repairs: {p.diagnostics.map((d) => d.message).join("; ")}</div>}
      <div className="row">
        <button className="primary" disabled={busy || v.state !== "prompt_gate"} onClick={approve} title="a">{busy ? "Sending…" : "Approve and send"}</button>
        <button disabled={busy} onClick={reject}>Reject</button>
        <button onClick={view}>View request JSON</button>
      </div>
    </div>
  );
}

function ToolGate({ cards, busy, submit }: { cards: ToolCard[]; busy: boolean; submit: (d: Record<string, Record<string, unknown>>) => void }) {
  const [dec, setDec] = useState<Record<string, { action: string; reason?: string; input?: string }>>(() =>
    Object.fromEntries(cards.map((c) => [c.id, { action: c.policy === "deny" || c.input_error ? "deny" : "approve", input: JSON.stringify(c.input, null, 1) }])));
  const send = () => {
    const out: Record<string, Record<string, unknown>> = {};
    for (const c of cards) {
      const d = dec[c.id];
      out[c.id] = d.action === "modify" ? { action: "modify", input: JSON.parse(d.input ?? "{}") } : { action: d.action, reason: d.reason };
    }
    submit(out);
  };
  return (
    <div className="panel stack" style={{ borderColor: "var(--accent)" }}>
      <h3>Tool gate: {cards.length} call{cards.length === 1 ? "" : "s"}</h3>
      {cards.map((c) => {
        const d = dec[c.id];
        const e = c.effects as Record<string, unknown>;
        const set = (patch: Partial<typeof d>) => setDec((x) => ({ ...x, [c.id]: { ...x[c.id], ...patch } }));
        return (
          <div key={c.id} className="panel stack">
            <div className="row"><b className="mono">{c.name}</b><span className="badge">{c.policy}</span><span className="muted">{c.reason}</span></div>
            {c.input_error && <div className="error">{c.input_error}</div>}
            <div className="muted">
              {e.writes ? "writes" : "read-only"}{Array.isArray(e.paths) && e.paths.length ? ` · paths: ${(e.paths as string[]).join(", ")}` : ""}
              {e.network ? ` · network: ${String(e.network)}` : ""}{e.creates ? " · creates the file" : ""}
              {e.matches !== undefined ? ` · matches: ${String(e.matches)}` : ""}
            </div>
            {Array.isArray(e.unknowns) && (e.unknowns as string[]).map((u) => <div key={u} className="error">{u}</div>)}
            {typeof e.diff === "string" && e.diff && <pre className="mono panel">{e.diff.slice(0, 6000)}</pre>}
            <div className="row">
              {["approve", "deny", "modify"].map((a) => (
                <label key={a}><input type="radio" checked={d.action === a} onChange={() => set({ action: a })} /> {a}</label>
              ))}
              {d.action === "deny" && <input className="grow" placeholder="reason (sent to the model)" value={d.reason ?? ""} onChange={(x) => set({ reason: x.target.value })} />}
            </div>
            {d.action === "modify"
              ? <textarea rows={4} className="mono" value={d.input} onChange={(x) => set({ input: x.target.value })} />
              : <pre className="mono secondary">{JSON.stringify(c.input, null, 1).slice(0, 3000)}</pre>}
          </div>
        );
      })}
      <div><button className="primary" disabled={busy} onClick={send}>Submit decisions and run</button></div>
    </div>
  );
}

function fmtTime(s: number | null) {
  if (s == null) return "?";
  const m = Math.floor(s / 60);
  return `${m}:${String(Math.floor(s % 60)).padStart(2, "0")}`;
}
