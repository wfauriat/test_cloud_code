"""Command line: look at the backend without the UI.  PLAN §8.

    curator import ~/.claude/projects/<project>/<session>.jsonl
    curator sessions
    curator show <sid>
    curator timeline <sid>
    curator rules <sid> [--stage]
    curator render <sid> [--call N] [--out request.json]
    curator diff <sid> --call N --call M      # two reconstructed requests
    curator diff <sid> --staged [--cold]      # history as it is vs. with staged ops
    curator cost --before 300000 --after 200000 --prefix 0 [--cold] [--ttl 1h]
    curator export [<sid>]                    # observations as JSONL
    curator export-session <sid> [--out f]    # everything: events, ops, calls (exact requests), observations
    curator wire <sid> [--call N] [--out f]   # the exact request sent for call N (default: last), live sessions

The database defaults to workspace/curator.db (override with --db or CURATOR_DB).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict
from pathlib import Path

from .adapters.store import Store
from .core.costs import DROP_COST_REFERENCE, edit_economics
from .core.prefix import diff
from .core.validate import validate
from .services import sessions as S
from .services import staging

DEFAULT_DB = os.environ.get("CURATOR_DB", str(Path(__file__).resolve().parents[2] / "workspace" / "curator.db"))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="curator", description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--db", default=DEFAULT_DB)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("import")
    p.add_argument("paths", nargs="+")
    sub.add_parser("sessions")
    for name in ("show", "timeline"):
        sub.add_parser(name).add_argument("sid")
    p = sub.add_parser("rules")
    p.add_argument("sid")
    p.add_argument("--stage", action="store_true", help="stage every proposal as an op")
    p.add_argument("--limit", type=int, default=30)
    p = sub.add_parser("render")
    p.add_argument("sid")
    p.add_argument("--call", type=int, help="reconstruct the request of the n-th call (0-based)")
    p.add_argument("--out")
    p = sub.add_parser("diff")
    p.add_argument("sid")
    p.add_argument("--call", type=int, action="append", default=[])
    p.add_argument("--staged", action="store_true")
    p.add_argument("--cold", action="store_true")
    p = sub.add_parser("cost")
    p.add_argument("--model", default="claude-opus-5-5")
    p.add_argument("--before", type=int, required=True)
    p.add_argument("--after", type=int, required=True)
    p.add_argument("--prefix", type=int, default=0, help="tokens before the first change")
    p.add_argument("--cold", action="store_true")
    p.add_argument("--ttl", default="5m", choices=["5m", "1h"])
    p = sub.add_parser("export")
    p.add_argument("sid", nargs="?")
    p = sub.add_parser("export-session")
    p.add_argument("sid")
    p.add_argument("--out")
    p = sub.add_parser("wire")
    p.add_argument("sid")
    p.add_argument("--call", type=int, help="0-based call index (default: last)")
    p.add_argument("--response", action="store_true", help="print the raw response too")
    p.add_argument("--out")
    a = ap.parse_args(argv)

    if a.cmd == "cost":
        e = edit_economics(a.model, tokens_before=a.before, tokens_after=a.after, divergence_tokens=a.prefix,
                           warm=not a.cold, ttl=a.ttl)
        _print_json(asdict(e))
        print(e.summary())
        return 0

    store = Store(a.db)
    if a.cmd == "import":
        for path in a.paths:
            sid = S.import_claude_code(store, path)
            print(f"{sid}  {store.session(sid)['title']}")
    elif a.cmd == "sessions":
        for s in store.sessions():
            print(f"{s['id']}  {s['source']:<20} {s['messages']:>5} msgs  {s['title']}")
    elif a.cmd == "show":
        v = S.load(store, a.sid)
        print(f"{v.info['title']}  [{v.source}]  {len(v.messages)} messages, {len(v.ops)} ops")
        print(f"preamble: {v.preamble.note or ('frozen' if v.preamble.known else 'unknown')}")
        print("composition (estimated tokens):")
        comp = S.composition(v)
        total = sum(comp.values()) or 1
        for k, n in comp.items():
            print(f"  {k:<16} {n:>9,}  {100 * n / total:5.1f}%")
        cal = S.calibration(v)
        if cal:
            print(f"calibration over {cal.n} calls: reported ≈ {cal.preamble_tokens:,.0f} + "
                  f"{cal.scale:.2f} × estimated  (r²={cal.r2:.3f})")
        obs = [o for o in store.observations(a.sid) if o["kind"] == "import"]
        if obs:
            print("import stats:", json.dumps(obs[-1]["payload"]["stats"]))
    elif a.cmd == "timeline":
        v = S.load(store, a.sid)
        print(f"{'n':>4} {'total in':>9} {'read':>9} {'write':>8} {'uncached':>8} {'out':>6}  ttl  note")
        for r in S.usage_timeline(v):
            note = f"BREAK -{r['lost']:,} ({r['reason']})" if r["cache_break"] else ""
            print(f"{r['n']:>4} {r['total_input']:>9,} {r['cache_read']:>9,} {r['cache_write']:>8,} "
                  f"{r['uncached']:>8,} {r['output']:>6,}  {r['ttl']:<4} {note}")
    elif a.cmd == "rules":
        v = S.load(store, a.sid)
        props = S.proposals(v)
        for p in props[: a.limit]:
            print(f"{p.rule}  -{p.tokens_saved:>7,} tok  {p.op.targets[0].event_id}#{p.op.targets[0].index}  "
                  f"{p.rationale}")
        print(f"{len(props)} proposals, ~{sum(p.tokens_saved for p in props):,} tokens per call")
        if a.stage:
            for p in props:
                staging.create_op(store, a.sid, verb=p.op.verb, targets=[t.to_dict() for t in p.op.targets],
                                  payload=p.op.payload, author=p.op.author, rationale=p.rationale)
            print(f"staged {len(props)} ops")
    elif a.cmd == "render":
        v = S.load(store, a.sid)
        events = S.cut(v, call_n=a.call)
        res = S.render_view(v, events=events)
        problems = validate(res.request, thinking_had=res.thinking_had, thinking_kept=res.thinking_kept)
        print(f"{len(res.request.messages)} messages; diagnostics:")
        for d in res.diagnostics:
            print(f"  {d.code}: {d.message}")
        print("validator:", "ok" if not problems else "")
        for d in problems:
            print(f"  {d.code} {d.where}: {d.message}")
        if a.out:
            Path(a.out).write_text(json.dumps(res.request.to_api(), ensure_ascii=False, indent=1))
            print(f"wrote {a.out}")
    elif a.cmd == "diff":
        v = S.load(store, a.sid)
        if a.staged:
            out = staging.preview(v, warm=not a.cold)
            print(out["diff"]["summary"])
            print(out["economics"]["summary"])
            if out["economics"]["thinking_blocks_lost"]:
                print(DROP_COST_REFERENCE)
            for d in out["validation_staged"]:
                print(f"  {d['code']} {d['where']}: {d['message']}")
        else:
            if len(a.call) != 2:
                print("give --call twice, or --staged", file=sys.stderr)
                return 2
            r1, r2 = (S.render_view(v, events=S.cut(v, call_n=n)).request for n in a.call)
            print(diff(r1, r2).summary())
    elif a.cmd == "export-session":
        from .services.export import export_jsonl
        text = export_jsonl(store, a.sid)
        if a.out:
            Path(a.out).write_text(text)
            print(f"wrote {a.out} ({text.count(chr(10))} lines)")
        else:
            sys.stdout.write(text)
    elif a.cmd == "wire":
        from .services.export import call_detail
        calls = store.calls(a.sid)
        if not calls:
            print("no calls (wire requests exist for live sessions; for imports use `curator render`)", file=sys.stderr)
            return 1
        d = call_detail(store, a.sid, calls[a.call]["id"] if a.call is not None else None)
        out = {"request": d["request"], **({"response": d["response"]} if a.response else {})}
        text = json.dumps(out if a.response else d["request"], ensure_ascii=False, indent=1)
        if a.out:
            Path(a.out).write_text(text)
            print(f"wrote {a.out}: call {d['n']}, {len(d['request']['messages'])} messages")
        else:
            print(text)
    elif a.cmd == "export":
        for o in store.observations(a.sid):
            print(json.dumps(o, ensure_ascii=False))
    return 0


def _print_json(obj) -> None:
    print(json.dumps(obj, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    raise SystemExit(main())
