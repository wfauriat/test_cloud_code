import { useCallback, useEffect, useState } from "react";
import { api, type SessionDetail, type SessionSummary } from "./api/client";
import { fmt } from "./format";
import { Curate } from "./views/Curate";
import { Experiments } from "./views/Experiments";
import { Live } from "./views/Live";
import { CategoryLegend, Look } from "./views/Look";
import { Timeline } from "./views/Timeline";

const TABS = ["Look", "Timeline", "Curate", "A/B", "Live"] as const;
type Tab = (typeof TABS)[number];

export function App() {
  const [sessions, setSessions] = useState<SessionSummary[]>([]);
  const [sid, setSid] = useState<string | null>(() => localStorageGet("sid"));
  const [tab, setTab] = useState<Tab>(() => (localStorageGet("tab") as Tab) || "Look");
  const [detail, setDetail] = useState<SessionDetail | null>(null);
  const [version, setVersion] = useState(0);
  const [path, setPath] = useState("");
  const [err, setErr] = useState<string | null>(null);
  const changed = useCallback(() => setVersion((v) => v + 1), []);

  useEffect(() => { api.sessions().then((s) => { setSessions(s); if (!sid && s[0]) setSid(s[0].id); }).catch((e) => setErr(String(e))); }, [version]); // eslint-disable-line react-hooks/exhaustive-deps
  useEffect(() => { if (sid) { localStorageSet("sid", sid); api.session(sid).then(setDetail).catch((e) => setErr(String(e))); } }, [sid, version]);
  useEffect(() => localStorageSet("tab", tab), [tab]);

  const doImport = async () => {
    try { const s = await api.importSession(path.trim()); setSid(s.id); setPath(""); setErr(null); changed(); }
    catch (e) { setErr(String(e)); }
  };

  return (
    <div className="app">
      <div className="topbar">
        <h1>Context Curator</h1>
        <select value={sid ?? ""} onChange={(e) => setSid(e.target.value)} style={{ maxWidth: 360 }}>
          {sessions.map((s) => <option key={s.id} value={s.id}>{s.title.slice(0, 60)} ({s.messages})</option>)}
        </select>
        <div className="tabs">{TABS.map((t) => <button key={t} className={t === tab ? "on" : ""} onClick={() => setTab(t)}>{t}</button>)}</div>
        {detail && (
          <span className="muted">
            {detail.source} · {detail.messages} messages · {detail.calls} calls · {detail.ops} ops
            {detail.calibration && ` · hidden preamble ≈ ${fmt(Math.round(detail.calibration.preamble_tokens))} tok`}
          </span>
        )}
        <span className="grow" />
        <input value={path} onChange={(e) => setPath(e.target.value)} placeholder="~/.claude/projects/…/session.jsonl" style={{ width: 300 }}
          onKeyDown={(e) => e.key === "Enter" && path.trim() && doImport()} />
        <button disabled={!path.trim()} onClick={doImport}>Import</button>
      </div>
      <div className="main">
        <div style={{ padding: "4px 12px", borderBottom: "1px solid var(--border)" }}>
          {err && <span className="error">{err} </span>}
          {detail && <CategoryLegend composition={detail.composition} />}
        </div>
        <div className="content">
          {tab === "Live" && <Live sid={sid} source={detail?.source ?? null} version={version} onChanged={changed}
            onCreated={(s) => { setSid(s); changed(); }} />}
          {!sid && tab !== "Live" && <div className="pad muted">Import a Claude Code session to start (path to a .jsonl under ~/.claude/projects).</div>}
          {sid && tab === "Look" && <Look sid={sid} version={version} onChanged={changed} />}
          {sid && tab === "Timeline" && <Timeline sid={sid} />}
          {sid && tab === "Curate" && <Curate sid={sid} version={version} onChanged={changed} />}
          {sid && tab === "A/B" && <Experiments sid={sid} />}
        </div>
      </div>
    </div>
  );
}

// Per-viewer conveniences only (last session, last tab); the page works without them.
function localStorageGet(k: string): string | null {
  try { return window.localStorage.getItem(`curator.${k}`); } catch { return null; }
}
function localStorageSet(k: string, v: string) {
  try { window.localStorage.setItem(`curator.${k}`, v); } catch { /* ignore */ }
}
