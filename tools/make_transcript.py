"""Build a readable HTML transcript of this Claude Code session from its JSONL log."""
import base64
import html
import io
import json
import os
import re
import sys
from datetime import datetime

import markdown
from PIL import Image

SRC = sys.argv[1]
OUT = sys.argv[2]

rows = [json.loads(l) for l in open(SRC)]


def ts(o):
    t = o.get("timestamp")
    return datetime.fromisoformat(t.replace("Z", "+00:00")) if t else None


def esc(s):
    return html.escape(s or "", quote=False)


def strip_reminders(s):
    return re.sub(r"<system-reminder>.*?</system-reminder>", "", s or "", flags=re.S).strip()


MD = markdown.Markdown(extensions=["fenced_code", "tables", "sane_lists"])
MD.preprocessors.deregister("html_block")
MD.inlinePatterns.deregister("html")


def md(s):
    MD.reset()
    return MD.convert(s)


def thumb(data_b64, media, max_w=560, q=72):
    try:
        im = Image.open(io.BytesIO(base64.b64decode(data_b64)))
        im = im.convert("RGB")
        if im.width > max_w:
            im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=q, optimize=True)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    except Exception:
        return None


def trunc(s, n):
    s = s or ""
    if len(s) <= n:
        return s, False
    return s[:n], True


def fmt_dur(sec):
    sec = max(0, int(round(sec)))
    h, r = divmod(sec, 3600)
    m, s = divmod(r, 60)
    if h:
        return f"{h} h {m:02d} min"
    if m:
        return f"{m} min {s:02d} s"
    return f"{s} s"


def fmt_tok(n):
    if n >= 1e6:
        return f"{n / 1e6:.2f} M"
    if n >= 1e3:
        return f"{n / 1e3:.1f} k"
    return str(n)


# ------------------------------------------------------------------ usage per unique API message
usage = {}
msg_time = {}
for o in rows:
    if o["type"] == "assistant":
        m = o["message"]
        usage[m["id"]] = m.get("usage") or {}
        msg_time.setdefault(m["id"], ts(o))


def usage_sum(ids):
    t = dict(inp=0, cw=0, cr=0, out=0, think=0)
    for i in ids:
        u = usage.get(i, {})
        t["inp"] += u.get("input_tokens", 0)
        t["cw"] += u.get("cache_creation_input_tokens", 0)
        t["cr"] += u.get("cache_read_input_tokens", 0)
        t["out"] += u.get("output_tokens", 0)
        t["think"] += (u.get("output_tokens_details") or {}).get("thinking_tokens", 0)
    return t


# ------------------------------------------------------------------ build turns
turns = []          # each: dict(kind, start, prompt_html, events=[], msg_ids=set(), tools=0, last=ts)
tool_cards = {}     # tool_use_id -> card dict
cur = None


def new_turn(kind, o, prompt_html, label):
    global cur
    cur = dict(kind=kind, start=ts(o), last=ts(o), prompt_html=prompt_html, label=label,
               events=[], msg_ids=set(), tools=0)
    turns.append(cur)


for o in rows:
    t = o["type"]
    if t == "user":
        origin = (o.get("origin") or {}).get("kind")
        c = o["message"]["content"]
        if origin == "human":
            parts, label = [], ""
            blocks = c if isinstance(c, list) else [{"type": "text", "text": c}]
            for b in blocks:
                if b.get("type") == "text":
                    txt = strip_reminders(b.get("text"))
                    if txt:
                        parts.append(f'<div class="ptext">{esc(txt)}</div>')
                        label = label or txt
                elif b.get("type") == "image":
                    src = (b.get("source") or {})
                    uri = thumb(src.get("data", ""), src.get("media_type"), max_w=900, q=80)
                    if uri:
                        parts.append(f'<img class="uimg" src="{uri}" alt="image attached by the user">')
            new_turn("human", o, "".join(parts), label)
            continue
        if origin == "task-notification":
            txt = c if isinstance(c, str) else " ".join(b.get("text", "") for b in c if b.get("type") == "text")
            m = re.search(r"<summary>(.*?)</summary>", txt, re.S)
            new_turn("notify", o, "", (m.group(1) if m else "Background task finished"))
            continue
        if cur is None:
            continue
        cur["last"] = ts(o) or cur["last"]
        if isinstance(c, str):
            s = strip_reminders(c)
            if s.startswith("Stop hook feedback"):
                cur["events"].append(("system", s))
            elif "[Request interrupted by user" in s:
                cur["events"].append(("system", "Request interrupted by the user."))
            continue
        for b in c:
            if b.get("type") == "tool_result":
                card = tool_cards.get(b.get("tool_use_id"))
                if card is None:
                    continue
                card["end"] = ts(o)
                card["error"] = bool(b.get("is_error"))
                content = b.get("content")
                texts, imgs = [], []
                if isinstance(content, str):
                    texts.append(content)
                elif isinstance(content, list):
                    for cb in content:
                        if cb.get("type") == "text":
                            texts.append(cb.get("text", ""))
                        elif cb.get("type") == "image":
                            src = cb.get("source") or {}
                            uri = thumb(src.get("data", ""), src.get("media_type"))
                            if uri:
                                imgs.append(uri)
                card["result"] = strip_reminders("\n".join(texts))
                card["images"] = imgs
            elif b.get("type") == "text":
                s = strip_reminders(b.get("text"))
                if "[Request interrupted by user" in s:
                    cur["events"].append(("system", "Request interrupted by the user."))
    elif t == "assistant" and cur is not None:
        m = o["message"]
        cur["msg_ids"].add(m["id"])
        cur["last"] = ts(o) or cur["last"]
        for b in m.get("content", []):
            if b.get("type") == "text" and b.get("text", "").strip():
                cur["events"].append(("text", b["text"]))
            elif b.get("type") == "tool_use":
                card = dict(name=b["name"], input=b.get("input") or {}, start=ts(o), end=None,
                            result=None, images=[], error=False)
                tool_cards[b["id"]] = card
                cur["events"].append(("tool", card))
                cur["tools"] += 1
    elif t == "attachment" and cur is not None:
        a = o["attachment"]
        if a.get("type") == "queued_command" and (a.get("origin") or {}).get("kind") == "human":
            cur["events"].append(("midturn", a.get("prompt", ""), ts(o)))
        cur["last"] = ts(o) or cur["last"]

# ------------------------------------------------------------------ tool rendering
def short(name):
    return name.replace("mcp__claude-code-remote__", "").replace("mcp__github__", "github.")


def tool_label(card):
    n, i = card["name"], card["input"]
    if n == "Bash":
        return i.get("description") or (i.get("command", "").splitlines() or [""])[0][:90]
    if n in ("Read", "Write", "Edit"):
        return os.path.basename(i.get("file_path", ""))
    if n == "Grep":
        return f"/{i.get('pattern', '')}/"
    if n == "Glob":
        return i.get("pattern", "")
    if n == "SendUserFile":
        return i.get("caption") or ", ".join(os.path.basename(f) for f in i.get("files", []))
    if n == "AskUserQuestion":
        qs = i.get("questions") or []
        return qs[0].get("question", "")[:90] if qs else ""
    if n == "ToolSearch":
        return i.get("query", "")
    if n == "Artifact":
        return i.get("action", "publish")
    return ""


def pre(s, cls="", limit=6000):
    body, cut = trunc(s, limit)
    note = f'<div class="cut">… trimmed ({len(s):,} characters in total)</div>' if cut else ""
    return f'<pre class="{cls}">{esc(body)}</pre>{note}'


def tool_input_html(card):
    n, i = card["name"], card["input"]
    if n == "Bash":
        bg = ' <span class="tag">background</span>' if i.get("run_in_background") else ""
        return f'<div class="lbl">command{bg}</div>' + pre(i.get("command", ""), "cmd", 5000)
    if n == "Write":
        return (f'<div class="lbl">write <code>{esc(i.get("file_path", ""))}</code></div>'
                + pre(i.get("content", ""), "", 7000))
    if n == "Edit":
        return (f'<div class="lbl">edit <code>{esc(i.get("file_path", ""))}</code></div>'
                f'<div class="lbl sm">old</div>' + pre(i.get("old_string", ""), "old", 3000)
                + f'<div class="lbl sm">new</div>' + pre(i.get("new_string", ""), "new", 3000))
    if n == "Read":
        extra = ", ".join(f"{k}={v}" for k, v in i.items() if k != "file_path")
        return f'<div class="lbl">read <code>{esc(i.get("file_path", ""))}</code> {esc(extra)}</div>'
    return '<div class="lbl">input</div>' + pre(json.dumps(i, indent=2, ensure_ascii=False), "", 4000)


def tool_html(card):
    dur = (card["end"] - card["start"]).total_seconds() if card["end"] and card["start"] else None
    d = f'<span class="dur">{fmt_dur(dur) if dur is not None and dur >= 1 else "&lt;1 s"}</span>' if dur is not None else ""
    err = " err" if card["error"] else ""
    res = ""
    if card["result"]:
        res += '<div class="lbl">output</div>' + pre(card["result"], "out", 4000)
    if card["images"]:
        res += '<div class="lbl">image(s) returned</div>' + "".join(f'<img class="timg" src="{u}" alt="tool output image">'
                                                                  for u in card["images"])
    if not res:
        res = '<div class="lbl">(no output)</div>'
    return (f'<details class="tool{err}"><summary><span class="tname">{esc(short(card["name"]))}</span>'
            f'<span class="tdesc">{esc(tool_label(card))}</span>{d}</summary>'
            f'<div class="tbody">{tool_input_html(card)}{res}</div></details>')


# ------------------------------------------------------------------ overview numbers
all_ids = set(usage)
U = usage_sum(all_ids)
cost = [o for o in rows if o["type"] == "cost-state"]
cost = cost[-1] if cost else {}
times = [ts(o) for o in rows if o.get("timestamp")]
t0, t1 = min(times), max(times)
active = sum((tn["last"] - tn["start"]).total_seconds() for tn in turns)
tool_counts = {}
for c in tool_cards.values():
    tool_counts[short(c["name"])] = tool_counts.get(short(c["name"]), 0) + 1
n_human = sum(1 for tn in turns if tn["kind"] == "human")
n_mid = sum(1 for tn in turns for e in tn["events"] if e[0] == "midturn")

# ------------------------------------------------------------------ page
H = []
H.append(f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Session Transcript</title>
<style>
:root {{ --ink:#1f1f1f; --muted:#6b6b6b; --line:#e3e3e3; --bg:#f6f6f3; --card:#fff; --user:#eef4fb; --user-b:#9cbbe0;
        --mid:#fff6e5; --mid-b:#e0b860; --tool:#fafafa; --err:#c00000; --accent:#2E7D32; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--ink); font:15px/1.55 Inter, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }}
.wrap {{ max-width: 980px; margin: 0 auto; padding: 24px 16px 60px; }}
h1 {{ font-size: 24px; margin: 0 0 4px; }}
h2 {{ font-size: 17px; margin: 28px 0 10px; }}
.sub {{ color: var(--muted); margin: 0 0 18px; }}
.grid {{ display:grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 10px; }}
.stat {{ background: var(--card); border:1px solid var(--line); border-radius: 10px; padding: 10px 12px; }}
.stat b {{ display:block; font-size: 20px; font-variant-numeric: tabular-nums; }}
.stat span {{ color: var(--muted); font-size: 12.5px; }}
table {{ width:100%; border-collapse: collapse; background: var(--card); border:1px solid var(--line); border-radius: 10px; overflow:hidden; font-size: 13.5px; }}
th, td {{ text-align:left; padding: 6px 10px; border-top: 1px solid var(--line); vertical-align: top; }}
th {{ background:#f0f0ec; border-top:0; font-weight:600; }}
td.num, div.num {{ text-align:right; font-variant-numeric: tabular-nums; white-space:nowrap; }}
div.num {{ text-align:left; }}
.bar {{ height: 8px; background: #8fb3d9; border-radius: 4px; min-width: 2px; }}
a {{ color: #1f5fa8; text-decoration: none; }} a:hover {{ text-decoration: underline; }}
.turn {{ margin: 26px 0 0; }}
.turnhead {{ display:flex; gap: 10px; align-items: baseline; flex-wrap: wrap; color: var(--muted); font-size: 13px; margin-bottom: 6px; }}
.turnhead .n {{ font-weight: 650; color: var(--ink); font-size: 14px; }}
.prompt {{ background: var(--user); border-left: 4px solid var(--user-b); border-radius: 8px; padding: 10px 14px; }}
.prompt .who, .mid .who {{ font-size: 12px; font-weight: 650; color: #3b6ea8; text-transform: uppercase; letter-spacing: .04em; }}
.ptext {{ white-space: pre-wrap; }}
.uimg {{ max-width: 100%; border:1px solid var(--line); border-radius: 6px; margin-top: 8px; }}
.mid {{ background: var(--mid); border-left: 4px solid var(--mid-b); border-radius: 8px; padding: 8px 12px; margin: 10px 0; }}
.mid .who {{ color: #9a6b00; }}
.notify {{ color: var(--muted); font-size: 13.5px; border:1px dashed #cfcfcf; border-radius: 8px; padding: 8px 12px; background:#fbfbf9; }}
.sys {{ color: var(--muted); font-size: 13px; border-left: 3px solid #cfcfcf; padding: 4px 10px; margin: 8px 0; white-space: pre-wrap; }}
.assist {{ background: var(--card); border:1px solid var(--line); border-radius: 8px; padding: 2px 16px; margin: 10px 0; }}
.assist p, .assist ul, .assist ol, .assist table {{ margin: 10px 0; }}
.assist table {{ font-size: 13px; }}
.assist pre {{ background:#f3f3f0; padding: 8px 10px; border-radius: 6px; overflow:auto; font-size: 12.5px; }}
.assist code {{ font: 12.5px ui-monospace, SFMono-Regular, Menlo, monospace; background:#f3f3f0; padding: 1px 4px; border-radius: 4px; }}
.assist pre code {{ background: none; padding: 0; }}
.tools {{ margin: 6px 0; }}
details.tool {{ background: var(--tool); border:1px solid var(--line); border-radius: 7px; margin: 4px 0; }}
details.tool.err {{ border-color: #e8a0a0; }}
details.tool summary {{ cursor:pointer; padding: 5px 10px; display:flex; gap: 10px; align-items: baseline; font-size: 13px; list-style: none; }}
details.tool summary::-webkit-details-marker {{ display:none; }}
details.tool summary::before {{ content: "▸"; color: var(--muted); }}
details.tool[open] summary::before {{ content: "▾"; }}
.tname {{ font: 600 12px ui-monospace, Menlo, monospace; color: #4a4a4a; background:#ececec; padding: 1px 6px; border-radius: 4px; white-space: nowrap; }}
details.tool.err .tname {{ background:#f6dcdc; color: var(--err); }}
.tdesc {{ flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: #333; }}
.dur {{ color: var(--muted); font-size: 12px; white-space: nowrap; font-variant-numeric: tabular-nums; }}
.tbody {{ padding: 4px 12px 10px; border-top: 1px solid var(--line); }}
.tbody pre {{ background:#fff; border:1px solid var(--line); border-radius: 6px; padding: 8px 10px; overflow:auto; max-height: 420px;
             font: 12px/1.45 ui-monospace, SFMono-Regular, Menlo, monospace; white-space: pre-wrap; word-break: break-word; margin: 4px 0; }}
.tbody pre.cmd {{ background:#1f2430; color:#e8e8e8; border-color:#1f2430; }}
.tbody pre.old {{ background:#fff3f3; }} .tbody pre.new {{ background:#f2fbf2; }}
.lbl {{ font-size: 11.5px; color: var(--muted); text-transform: uppercase; letter-spacing: .04em; margin-top: 8px; }}
.lbl.sm {{ margin-top: 4px; }}
.lbl code {{ text-transform: none; letter-spacing: 0; font-size: 12px; }}
.tag {{ text-transform:none; background:#e8eefc; color:#3b5bb5; border-radius: 4px; padding: 0 5px; }}
.cut {{ font-size: 12px; color: var(--muted); font-style: italic; }}
.timg {{ max-width: 100%; border:1px solid var(--line); border-radius: 6px; margin: 4px 0; display:block; }}
.meta {{ font-size: 12.5px; color: var(--muted); margin-top: 6px; }}
.toolbar {{ position: sticky; top: 0; z-index: 5; background: rgba(246,246,243,.94); backdrop-filter: blur(4px);
            padding: 8px 0; border-bottom: 1px solid var(--line); display:flex; gap: 8px; align-items:center; flex-wrap: wrap; }}
.toolbar button {{ font: inherit; font-size: 13px; padding: 4px 10px; border:1px solid #c9c9c9; border-radius: 6px; background:#fff; cursor:pointer; }}
.note {{ font-size: 12.5px; color: var(--muted); }}
@media (max-width: 640px) {{ .tdesc {{ white-space: normal; }} th:nth-child(4), td:nth-child(4) {{ display:none; }} }}
</style></head><body><div class="wrap">""")

H.append(f"""<h1>Session transcript – uniaxial tomography explainer</h1>
<p class="sub">Claude Code cloud session · repository <code>wfauriat/test_cloud_code</code> · {t0:%Y-%m-%d} ·
{n_human} prompts from you (+{n_mid} sent while I was working) · generated from the session log at {t1:%H:%M} UTC.</p>""")

out_total = U["out"]
ctx_total = U["inp"] + U["cw"] + U["cr"]
H.append('<div class="grid">')
for big, small in [
    (fmt_dur((t1 - t0).total_seconds()), f"session span ({t0:%H:%M} → {t1:%H:%M} UTC)"),
    (fmt_dur(active), "active time (prompt → last reply, summed over turns)"),
    (fmt_dur(cost.get("totalAPIDuration", 0) / 1000), "model time (API calls)"),
    (fmt_dur(cost.get("totalToolDuration", 0) / 1000), "tool time (commands, renders, …)"),
    (fmt_tok(out_total), f"output tokens (incl. {fmt_tok(U['think'])} reasoning)"),
    (fmt_tok(ctx_total), f"input tokens processed ({fmt_tok(U['cr'])} from cache)"),
    (str(len(all_ids)), "model calls"),
    (str(len(tool_cards)), "tool calls"),
]:
    H.append(f'<div class="stat"><b>{big}</b><span>{small}</span></div>')
H.append("</div>")
if cost.get("totalCostUSD"):
    H.append(f'<p class="note">Cost estimate reported by Claude Code at list prices: '
             f'<b>${cost["totalCostUSD"]:.2f}</b>. Input tokens are mostly re-read conversation context served from the '
             f'prompt cache, which is billed at a fraction of the normal input price. Figures cover the session up to the '
             f'moment this page was generated.</p>')
H.append('<p class="note">Tool calls: ' + ", ".join(f"{k} × {v}" for k, v in sorted(tool_counts.items(), key=lambda kv: -kv[1])) + "</p>")

# turns table
H.append("<h2>Turns</h2><table><tr><th>#</th><th>started</th><th>request</th><th>duration</th><th>tools</th><th>output tok.</th></tr>")
maxd = max((tn["last"] - tn["start"]).total_seconds() for tn in turns) or 1
for k, tn in enumerate(turns, 1):
    d = (tn["last"] - tn["start"]).total_seconds()
    us = usage_sum(tn["msg_ids"])
    lab = tn["label"].replace("\n", " ")
    lab = (lab[:110] + "…") if len(lab) > 110 else lab
    if tn["kind"] == "notify":
        lab = "⚙ " + lab
    H.append(f'<tr><td class="num"><a href="#t{k}">{k}</a></td><td class="num">{tn["start"]:%H:%M}</td>'
             f'<td><a href="#t{k}">{esc(lab)}</a></td>'
             f'<td><div class="num">{fmt_dur(d)}</div><div class="bar" style="width:{max(d / maxd * 100, 1):.1f}%"></div></td>'
             f'<td class="num">{tn["tools"]}</td><td class="num">{fmt_tok(us["out"])}</td></tr>')
H.append("</table>")

H.append('<h2>Conversation</h2><div class="toolbar"><button onclick="tog(true)">Expand all tool calls</button>'
         '<button onclick="tog(false)">Collapse all</button><span class="note">Tool calls are collapsed; click one to see '
         'its input and output. My hidden reasoning is not included (only its token count above).</span></div>')

for k, tn in enumerate(turns, 1):
    d = (tn["last"] - tn["start"]).total_seconds()
    us = usage_sum(tn["msg_ids"])
    H.append(f'<div class="turn" id="t{k}"><div class="turnhead"><span class="n">Turn {k}</span>'
             f'<span>{tn["start"]:%H:%M:%S} UTC</span><span>· {fmt_dur(d)}</span><span>· {tn["tools"]} tool calls</span>'
             f'<span>· {fmt_tok(us["out"])} output tokens</span></div>')
    if tn["kind"] == "human":
        H.append(f'<div class="prompt"><div class="who">You</div>{tn["prompt_html"]}</div>')
    else:
        H.append(f'<div class="notify">⚙ Background notification: {esc(tn["label"])}</div>')
    tool_buf = []

    def flush():
        if tool_buf:
            H.append('<div class="tools">' + "".join(tool_buf) + "</div>")
            tool_buf.clear()

    for e in tn["events"]:
        if e[0] == "tool":
            tool_buf.append(tool_html(e[1]))
            continue
        flush()
        if e[0] == "text":
            H.append(f'<div class="assist">{md(e[1])}</div>')
        elif e[0] == "midturn":
            H.append(f'<div class="mid"><div class="who">You, while I was working · {e[2]:%H:%M:%S}</div>'
                     f'<div class="ptext">{esc(e[1])}</div></div>')
        elif e[0] == "system":
            H.append(f'<div class="sys">{esc(e[1])}</div>')
    flush()
    H.append("</div>")

H.append("""<script>
function tog(open){ document.querySelectorAll('details.tool').forEach(d => d.open = open); }
</script></div></body></html>""")

with open(OUT, "w") as fh:
    fh.write("".join(H))
print("turns", len(turns), "tool cards", len(tool_cards), "bytes", os.path.getsize(OUT))
