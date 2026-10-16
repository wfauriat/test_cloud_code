// Look: outline | context map | document | inspector.  PLAN §6.
// Keyboard: j/k move between blocks, d drop, p pin, r replace, i insert a note after, u revoke.
import { useVirtualizer } from "@tanstack/react-virtual";
import { useCallback, useEffect, useLayoutEffect, useMemo, useRef, useState } from "react";
import { api, type BlockDetail, type BlockView, type MessageView, type Span } from "../api/client";
import { CATEGORY_ORDER, LABEL, catColor, fmt, kfmt } from "../format";

type Flat = { m: number; b: number; key: string; eid: string; block: BlockView; start: number; siblings: number[] };
const msgBlocks = (f: Flat): Span[] => f.siblings.map((index) => ({ event_id: f.eid, index }));
const keyOf = (eid: string, index: number) => `${eid}#${index}`;
const HEAD_LINES = 12;
const TAIL_LINES = 6;

export function Look({ sid, version, onChanged }: { sid: string; version: number; onChanged: () => void }) {
  const [msgs, setMsgs] = useState<MessageView[]>([]);
  const [sel, setSel] = useState<string | null>(null);
  const [err, setErr] = useState<string | null>(null);
  const docRef = useRef<HTMLDivElement>(null);

  useEffect(() => { api.messages(sid).then(setMsgs).catch((e) => setErr(String(e))); }, [sid, version]);

  const flat: Flat[] = useMemo(() => {
    const out: Flat[] = [];
    let start = 0;
    msgs.forEach((msg, m) => msg.blocks.forEach((block, b) => {
      out.push({ m, b, key: keyOf(msg.event_id, block.index), eid: msg.event_id, block, start,
        siblings: msg.blocks.map((x) => x.index) });
      start += block.tokens;
    }));
    return out;
  }, [msgs]);
  const byKey = useMemo(() => new Map(flat.map((f) => [f.key, f])), [flat]);
  const current = sel ? byKey.get(sel) ?? null : null;

  const virt = useVirtualizer({
    count: msgs.length,
    getScrollElement: () => docRef.current,
    // Estimate from the real line counts (collapsed bodies included): a poor estimate makes the list
    // jump when rows are measured while scrolling.
    estimateSize: (i) => estimateMessageHeight(msgs[i]),
    overscan: 6,
  });

  const select = useCallback((key: string, scroll = true) => {
    setSel(key);
    const f = byKey.get(key);
    if (f && scroll) virt.scrollToIndex(f.m, { align: "center" });
  }, [byKey, virt]);

  const act = useCallback(async (verb: string, targets: Span[], payload: Record<string, unknown> = {}, rationale = "") => {
    try { await api.createOp(sid, { verb, targets, payload, rationale }); setErr(null); onChanged(); }
    catch (e) { setErr(String(e)); }
  }, [sid, onChanged]);

  const revokeAll = useCallback(async (f: Flat) => {
    for (const id of f.block.status.op_ids) await api.opAction(sid, id, "revoke").catch(() => undefined);
    onChanged();
  }, [sid, onChanged]);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      const t = e.target as HTMLElement;
      if (t.closest("input, textarea, select") || e.metaKey || e.ctrlKey) return;
      const i = current ? flat.indexOf(current) : -1;
      if (e.key === "j" && flat.length) select(flat[Math.min(i + 1, flat.length - 1)].key);
      else if (e.key === "k" && flat.length) select(flat[Math.max(i - 1, 0)].key);
      else if (!current) return;
      else if (e.key === "d") act("drop", [{ event_id: current.eid, index: current.block.index }]);
      else if (e.key === "p") act("pin", [{ event_id: current.eid, index: current.block.index }]);
      else if (e.key === "u") revokeAll(current);
      else if (e.key === "r") {
        const text = window.prompt("Replace the whole block with:", "");
        if (text !== null) act("replace", [{ event_id: current.eid, index: current.block.index }], { text });
      } else if (e.key === "i") {
        const text = window.prompt("Insert a note after this block:", "");
        if (text) act("insert", [{ event_id: current.eid, index: current.block.index }], { text });
      } else return;
      e.preventDefault();
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [current, flat, select, act, revokeAll]);

  return (
    <div className="look">
      <Outline msgs={msgs} sel={current} onPick={(m) => select(keyOf(msgs[m].event_id, msgs[m].blocks[0]?.index ?? 0))} />
      <ContextMap flat={flat} sel={sel} onPick={select} />
      <div className="doc scroll" ref={docRef}>
        {err && <div className="pad error">{err}</div>}
        <div style={{ height: virt.getTotalSize(), position: "relative" }}>
          {virt.getVirtualItems().map((vi) => (
            <div key={vi.key} data-index={vi.index} ref={virt.measureElement}
              style={{ position: "absolute", top: 0, left: 0, right: 0, transform: `translateY(${vi.start}px)` }}>
              <Message msg={msgs[vi.index]} sel={sel} onPick={(k) => select(k, false)} />
            </div>
          ))}
        </div>
      </div>
      <Inspector sid={sid} f={current} version={version} act={act} revokeAll={revokeAll} onChanged={onChanged} />
    </div>
  );
}

const LINE_PX = 17;
function estimateMessageHeight(msg: MessageView): number {
  let h = 34;
  for (const b of msg.blocks) {
    const lines = b.text ? b.text.split("\n").length : 0;
    const shown = lines > HEAD_LINES + TAIL_LINES + 4 ? HEAD_LINES + TAIL_LINES + 2 : lines;
    const wrapped = b.text ? Math.ceil(b.text.length / 140) : 0; // long lines wrap
    h += 26 + LINE_PX * Math.min(Math.max(shown, Math.min(wrapped, HEAD_LINES + TAIL_LINES + 2)), 40);
  }
  return h;
}

function Outline({ msgs, sel, onPick }: { msgs: MessageView[]; sel: Flat | null; onPick: (m: number) => void }) {
  return (
    <div className="outline scroll">
      <div className="pad muted" style={{ paddingBottom: 4 }}>{msgs.length} messages</div>
      {msgs.map((msg, m) => (
        <div key={msg.event_id} className={`item ${sel?.m === m ? "on" : ""}`} onClick={() => onPick(m)}
          title={msg.blocks.map((b) => b.gist).join("\n")}>
          <span className="mono muted" style={{ width: 26 }}>{msg.call_n ?? ""}</span>
          <span className="gist"><b style={{ fontWeight: 500 }}>{msg.label}</b> <span className="muted">{msg.blocks[0]?.gist}</span></span>
          <span className="mono muted">{kfmt(msg.tokens)}</span>
        </div>
      ))}
    </div>
  );
}

function Message({ msg, sel, onPick }: { msg: MessageView; sel: string | null; onPick: (key: string) => void }) {
  return (
    <div className="msg">
      <div className="msg-head">
        <b>{msg.label}</b>
        {msg.call_n !== null && msg.call_n !== undefined && <span className="badge">call {msg.call_n}</span>}
        <span className="grow" />
        <span className="mono">{fmt(msg.tokens)} tok</span>
        <span className="muted mono">{msg.timestamp?.slice(11, 19)}</span>
      </div>
      {msg.blocks.map((b) => <Block key={b.index} eid={msg.event_id} b={b} on={sel === keyOf(msg.event_id, b.index)} onPick={onPick} />)}
    </div>
  );
}

function Block({ eid, b, on, onPick }: { eid: string; b: BlockView; on: boolean; onPick: (key: string) => void }) {
  const [open, setOpen] = useState(false);
  const key = keyOf(eid, b.index);
  const st = b.status;
  const lines = b.text.split("\n");
  const long = lines.length > HEAD_LINES + TAIL_LINES + 4 && !open;
  const head = long ? lines.slice(0, HEAD_LINES).join("\n") + "\n" : b.text;
  const tail = long ? lines.slice(-TAIL_LINES).join("\n") : "";
  return (
    <div className={`blk ${st.state} ${on ? "on" : ""}`} style={{ borderLeftColor: catColor(b.category) }}
      onClick={() => onPick(key)}>
      <div className="blk-head">
        <span className="mono muted">{b.type}</span>
        <span className="gist">{b.gist}</span>
        {st.pinned && <span className="badge">pinned</span>}
        {st.state !== "kept" && <span className={`badge ${st.state} ${st.pending ? "pending" : ""}`}>{st.state}{st.pending ? " (staged)" : ""}</span>}
        {b.is_error && <span className="badge dropped">error</span>}
        <span className="mono muted">{fmt(b.tokens)}</span>
      </div>
      {b.type === "thinking" || b.type === "redacted_thinking" ? (
        !b.text && <div className="gap-note">reasoning not visible (display "omitted"); ~{fmt(b.tokens)} tokens</div>
      ) : null}
      {b.text && (
        <div className={`body ${b.type === "tool_use" ? "secondary" : ""}`} data-key={key}>
          <pre data-offset={0}>{head}</pre>
          {long && (
            <>
              <div className="gap-note">
                … {lines.length - HEAD_LINES - TAIL_LINES} lines hidden{" "}
                <button onClick={(e) => { e.stopPropagation(); setOpen(true); }}>expand</button>
              </div>
              <pre data-offset={b.text.length - tail.length}>{tail}</pre>
            </>
          )}
        </div>
      )}
    </div>
  );
}

/** The selected text inside one block, as a code-point span (PLAN §3 addressing). */
function selectionSpan(key: string): { start: number; end: number } | null {
  const s = window.getSelection();
  if (!s || s.isCollapsed || s.rangeCount === 0) return null;
  const r = s.getRangeAt(0);
  const pos = (node: Node, off: number) => {
    const pre = (node.nodeType === Node.TEXT_NODE ? node.parentElement : (node as Element))?.closest("pre[data-offset]");
    const body = pre?.closest(`[data-key="${CSS.escape(key)}"]`);
    if (!pre || !body) return null;
    // DOM offsets are UTF-16 units; convert the text before the caret to code points.
    const before = (pre.textContent ?? "").slice(0, off);
    return Number(pre.getAttribute("data-offset")) + [...before].length;
  };
  const a = pos(r.startContainer, r.startOffset);
  const b = pos(r.endContainer, r.endOffset);
  return a === null || b === null || a === b ? null : { start: Math.min(a, b), end: Math.max(a, b) };
}

function Inspector({ sid, f, version, act, revokeAll, onChanged }: {
  sid: string; f: Flat | null; version: number; onChanged: () => void;
  act: (verb: string, targets: Span[], payload?: Record<string, unknown>, rationale?: string) => Promise<void>;
  revokeAll: (f: Flat) => Promise<void>;
}) {
  const [detail, setDetail] = useState<BlockDetail | null>(null);
  const [summary, setSummary] = useState<{ draft: string; call: string; model: string; cost: number; targets: Span[] } | null>(null);
  useEffect(() => {
    setDetail(null);
    if (f) api.block(sid, f.eid, f.block.index).then(setDetail).catch(() => setDetail(null));
  }, [sid, f?.key, version]); // eslint-disable-line react-hooks/exhaustive-deps
  if (!f) return <div className="inspector pad muted">Select a block (click, or j/k).</div>;
  const b = f.block;
  const target = { event_id: f.eid, index: b.index };
  const withSelection = (verb: "drop" | "replace") => {
    const span = selectionSpan(f.key);
    if (!span) return window.alert("Select some text inside this block first.");
    const payload = verb === "replace" ? { text: window.prompt("Replace the selection with:", "") ?? "" } : {};
    act(verb, [{ ...target, ...span }], payload);
  };
  const editable = b.type === "text" || b.type === "tool_result";
  const draft = async (whole: boolean) => {
    const targets = whole && f ? msgBlocks(f) : [target];
    try { const d = await api.summarize(sid, targets); setSummary({ ...d, targets }); }
    catch (e) { window.alert(String(e)); }
  };
  return (
    <div className="inspector scroll pad stack">
      <div className="kv">
        <span className="k">address</span><span className="mono">{f.eid}#{b.index}</span>
        <span className="k">type</span><span>{b.type} · {b.origin}</span>
        <span className="k">category</span><span className="row"><span className="swatch" style={{ background: catColor(b.category) }} />{LABEL[b.category] ?? b.category}</span>
        <span className="k">tokens</span><span>{fmt(b.tokens)} <span className="muted">(estimated)</span></span>
        <span className="k">status</span><span>{b.status.state}{b.status.pending ? " (staged)" : ""}{b.status.pinned ? ", pinned" : ""}</span>
        {b.tool_name && <><span className="k">tool</span><span className="mono">{b.tool_name} {b.tool_use_id}</span></>}
      </div>
      <div className="row">
        <button onClick={() => act("drop", [target])} title="d">Drop</button>
        <button onClick={() => act("pin", [target])} title="p">Pin</button>
        {editable && <button onClick={() => { const t = window.prompt("Replace the whole block with:", ""); if (t !== null) act("replace", [target], { text: t }); }} title="r">Replace…</button>}
        <button onClick={() => { const t = window.prompt("Insert a note after this block:", ""); if (t) act("insert", [target], { text: t }); }} title="i">Note after…</button>
        {b.status.op_ids.length > 0 && <button onClick={() => revokeAll(f)} title="u">Revoke ops</button>}
      </div>
      {editable && (
        <div className="row">
          <span className="muted">Selection:</span>
          <button onClick={() => withSelection("drop")}>Drop selection</button>
          <button onClick={() => withSelection("replace")}>Replace selection…</button>
        </div>
      )}
      <div className="row">
        <span className="muted">LLM draft summary:</span>
        <button onClick={() => draft(false)}>this block</button>
        <button onClick={() => draft(true)}>this message</button>
      </div>
      {summary && (
        <div className="panel stack">
          <h3>Draft from {summary.model} ({summary.cost.toFixed(4)} $), not applied yet</h3>
          <textarea rows={6} value={summary.draft} onChange={(e) => setSummary({ ...summary, draft: e.target.value })} />
          <div className="row">
            <button className="primary" onClick={() => api.acceptSummary(sid, summary.targets, summary.draft, summary.call)
              .then(() => { setSummary(null); onChanged(); }).catch((e) => window.alert(String(e)))}>Accept as staged edit</button>
            <button onClick={() => setSummary(null)}>Discard</button>
          </div>
        </div>
      )}
      {detail && detail.proposals.length > 0 && (
        <div className="panel">
          <h3>Rule proposals</h3>
          {detail.proposals.map((p) => (
            <div key={String(p.id)} className="row">
              <span className="badge">{String(p.rule)}</span><span className="grow">{String(p.rationale)}</span>
              <span className="mono">−{fmt(Number(p.tokens_saved))}</span>
              <button onClick={() => api.stageProposals(sid, [String(p.id)]).then(onChanged)}>Stage</button>
            </div>
          ))}
        </div>
      )}
      {detail && detail.ops.length > 0 && (
        <div className="panel">
          <h3>Ops on this block</h3>
          {detail.ops.map((o) => (
            <div key={String(o.id)} className="row mono">
              <span>{String(o.verb)}</span><span className="badge">{String(o.state)}</span>
              <span className="muted grow">{String(o.author)} {String(o.rationale ?? "")}</span>
            </div>
          ))}
        </div>
      )}
      {b.status.shadowed.length > 0 && <div className="muted">Shadowed ops (overridden by later ones): {b.status.shadowed.join(", ")}</div>}
      {detail && (
        <details>
          <summary>Raw block JSON (as stored and replayed)</summary>
          <pre className="mono">{JSON.stringify(detail.raw, null, 1)}</pre>
        </details>
      )}
    </div>
  );
}

function ContextMap({ flat, sel, onPick }: { flat: Flat[]; sel: string | null; onPick: (key: string) => void }) {
  const ref = useRef<HTMLDivElement>(null);
  const [h, setH] = useState(600);
  const [tip, setTip] = useState<{ x: number; y: number; f: Flat } | null>(null);
  useLayoutEffect(() => {
    const el = ref.current;
    if (!el) return;
    const ro = new ResizeObserver(() => setH(el.clientHeight));
    ro.observe(el);
    return () => ro.disconnect();
  }, []);
  const total = flat.reduce((s, f) => s + f.block.tokens, 0) || 1;
  const W = 30;
  const y = (t: number) => (t / total) * (h - 2);
  return (
    <div className="map" ref={ref} style={{ position: "relative" }} onMouseLeave={() => setTip(null)}>
      <svg width={W} height={h} role="img" aria-label="Context map: the request as sent, height proportional to tokens">
        <defs>
          <pattern id="hatch-drop" width="4" height="4" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
            <rect width="4" height="4" fill="var(--surface-1)" opacity="0.65" /><line x1="0" y1="0" x2="0" y2="4" stroke="var(--critical)" strokeWidth="1.5" />
          </pattern>
          <pattern id="hatch-edit" width="4" height="4" patternUnits="userSpaceOnUse" patternTransform="rotate(135)">
            <line x1="0" y1="0" x2="0" y2="4" stroke="var(--surface-1)" strokeWidth="1.5" />
          </pattern>
        </defs>
        {flat.map((f) => {
          const top = y(f.start) + 1;
          const hh = Math.max(y(f.block.tokens) - (y(f.block.tokens) > 6 ? 2 : 0), 0.6);
          const st = f.block.status;
          return (
            <g key={f.key} onClick={() => onPick(f.key)} style={{ cursor: "pointer" }}
              onMouseMove={(e) => setTip({ x: e.clientX, y: e.clientY, f })}>
              <rect x={3} y={top} width={W - 9} height={hh} rx={hh > 6 ? 2 : 0} fill={catColor(f.block.category)} />
              {st.state === "dropped" && <rect x={3} y={top} width={W - 9} height={hh} fill="url(#hatch-drop)" />}
              {st.state === "edited" && <rect x={3} y={top} width={W - 9} height={hh} fill="url(#hatch-edit)" />}
              {st.pinned && <rect x={W - 5} y={top} width={3} height={Math.max(hh, 2)} fill="var(--text-primary)" />}
              {sel === f.key && <rect x={1} y={top - 1} width={W - 5} height={hh + 2} fill="none" stroke="var(--accent)" strokeWidth={2} />}
            </g>
          );
        })}
      </svg>
      {tip && (
        <div className="tooltip" style={{ left: tip.x + 14, top: tip.y + 8 }}>
          <div className="row"><span className="swatch" style={{ background: catColor(tip.f.block.category) }} /><b>{LABEL[tip.f.block.category] ?? tip.f.block.category}</b></div>
          <div>{fmt(tip.f.block.tokens)} tokens · {tip.f.block.status.state}{tip.f.block.status.pinned ? " · pinned" : ""}</div>
          <div className="muted">{tip.f.block.gist}</div>
        </div>
      )}
    </div>
  );
}

export function CategoryLegend({ composition }: { composition: Record<string, number> }) {
  const total = Object.values(composition).reduce((a, b) => a + b, 0) || 1;
  const cats = [...CATEGORY_ORDER.filter((c) => c in composition), ...Object.keys(composition).filter((c) => !(CATEGORY_ORDER as readonly string[]).includes(c))];
  return (
    <div className="legend">
      {cats.map((c) => (
        <span key={c}><span className="swatch" style={{ background: catColor(c) }} />{LABEL[c] ?? c} {Math.round((100 * composition[c]) / total)}%</span>
      ))}
      <span className="muted">hatched red = dropped · hatched = edited · bar at right = pinned</span>
    </div>
  );
}
