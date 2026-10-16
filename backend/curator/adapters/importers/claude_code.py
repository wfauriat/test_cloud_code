"""Claude Code session logs -> events (approximate wire).  PLAN §3 "import mapping", §5.1.

The JSONL format is internal to Claude Code and changes between versions; this importer reads
only what it needs and counts everything it skips (see `stats`). What we get:
- the main chain of entries (user / assistant / attachment / system), linked by parentUuid;
- assistant messages split one content block per line, re-joined here by message.id;
- per-call `usage`, i.e. the exact input size Claude Code sent at each call;
- harness text ("attachments": reminders, environment, skills listings...) with how it was
  rendered (`renderedRole` system or user);
- sometimes a `prompt_snapshot` with the system prompt, and `deferred_tools_record` with some
  tool definitions. Never the full tool list.  # QUIRK: so imported wire is approximate.
"""

from __future__ import annotations

import json
from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Any

from ...core.model import Block, Preamble
from ...core.wire import block_hash

CONTEXT_TYPES = ("user", "assistant", "attachment", "system")
SYSTEM_PROMPT_BOUNDARY = "__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__"


@dataclass
class ImportedEvent:
    kind: str  # "message" | "import_meta"
    role: str | None
    blocks: list[Block]
    meta: dict[str, Any]


@dataclass
class ImportedSession:
    title: str
    events: list[ImportedEvent]
    preamble: Preamble
    model: str | None
    stats: dict[str, int] = field(default_factory=dict)


def parse(lines: Iterable[str], *, name: str = "session") -> ImportedSession:
    stats: Counter[str] = Counter()
    entries: list[dict[str, Any]] = []
    for line in lines:
        stats["lines"] += 1
        try:
            d = json.loads(line)
        except ValueError:
            stats["bad_lines"] += 1
            continue
        stats[f"type.{d.get('type')}"] += 1
        entries.append(d)

    by_uuid = {d["uuid"]: d for d in entries if d.get("uuid")}
    main = [d for d in entries if d.get("uuid") and d.get("type") in CONTEXT_TYPES]
    stats["sidechain_skipped"] = sum(1 for d in main if d.get("isSidechain"))
    main = [d for d in main if not d.get("isSidechain")]
    chain: list[dict[str, Any]] = []
    cur = main[-1] if main else None
    seen: set[str] = set()
    while cur is not None and cur["uuid"] not in seen:
        seen.add(cur["uuid"])
        chain.append(cur)
        cur = by_uuid.get(cur.get("parentUuid"))
    on_path = {d["uuid"] for d in chain}
    # QUIRK: parallel tool calls branch the parentUuid tree: result 1 is a child of call 1 while
    # the path to the leaf runs through call 2 and result 2. Side entries hanging off the path
    # (tool results, and attachments under them) are part of the context, so they are kept,
    # in file order. Other branches (rewinds, abandoned edits) are not.
    included: set[str] = set()
    side: set[str] = set()
    chain = []
    for d in main:
        if d["uuid"] in on_path:
            chain.append(d)
            included.add(d["uuid"])
        elif d.get("parentUuid") in included and (_is_results_only(d) or (
                d.get("type") == "attachment" and d.get("parentUuid") in side)):
            chain.append(d)
            included.add(d["uuid"])
            side.add(d["uuid"])
    stats["side_entries"] = len(side)
    stats["off_chain"] = len(main) - len(chain)

    events: list[ImportedEvent] = []
    system_snapshots: list[list[dict[str, Any]]] = []
    tools: dict[str, dict[str, Any]] = {}
    assistant_by_id: dict[str, ImportedEvent] = {}
    model = None
    title = None

    for d in chain:
        t = d.get("type")
        if t == "assistant":
            msg = d.get("message") or {}
            model = model or msg.get("model")
            # QUIRK: parallel tool calls are logged interleaved with their results
            # (call 1, result 1, call 2, ...). On the wire they are one assistant message, so
            # blocks re-join their message by id; the results land after it and repair.py
            # merges them into one user message.
            prior = assistant_by_id.get(msg.get("id"))
            if prior is not None:
                _extend_assistant(prior, d, msg)
            else:
                ev = ImportedEvent("message", "assistant", [], {
                    "message_id": msg.get("id"), "model": msg.get("model"), "timestamp": d.get("timestamp"),
                    "uuids": [], "block_indexes": []})
                _extend_assistant(ev, d, msg)
                events.append(ev)
                assistant_by_id[msg.get("id")] = ev
                stats["assistant_messages"] += 1
        elif t == "user":
            msg = d.get("message") or {}
            content = msg.get("content")
            raws = [{"type": "text", "text": content}] if isinstance(content, str) else list(content or [])
            blocks = [Block(r, _user_origin(r, d)) for r in raws if isinstance(r, dict)]
            if not blocks:
                stats["empty_user_skipped"] += 1
                continue
            if title is None and not d.get("isMeta") and blocks[0].type == "text":
                first = blocks[0].raw.get("text", "").strip()
                title = first.splitlines()[0][:80] if first else None
            events.append(ImportedEvent("message", "user", blocks, {
                "timestamp": d.get("timestamp"), "uuid": d.get("uuid"), "is_meta": bool(d.get("isMeta"))}))
        elif t == "attachment":
            att = d.get("attachment") or {}
            atype = att.get("type")
            if atype == "prompt_snapshot" and att.get("systemPrompt"):
                parts = [s for s in att["systemPrompt"] if isinstance(s, str) and s != SYSTEM_PROMPT_BOUNDARY]
                system = [{"type": "text", "text": s} for s in parts]
                system_snapshots.append(system)
                events.append(ImportedEvent("import_meta", None, [], {
                    "attachment_type": atype, "timestamp": d.get("timestamp"),
                    "system_hash": block_hash({"system": system})}))
                continue
            if atype == "deferred_tools_record":
                for entry in att.get("entries") or []:
                    if isinstance(entry, dict) and entry.get("name"):
                        tools[entry["name"]] = entry
            rendered = d.get("rendered")
            if not rendered:
                stats["attachments_unrendered"] += 1
                continue
            role = "system" if d.get("renderedRole") == "system" else "user"
            blocks = []
            for item in rendered:
                c = item.get("content") if isinstance(item, dict) else item
                if isinstance(c, str) and c.strip():
                    blocks.append(Block({"type": "text", "text": c}, "harness"))
                elif isinstance(c, list):
                    blocks += [Block(r, "harness") for r in c if isinstance(r, dict)]
            if blocks:
                stats["attachments_rendered"] += 1
                events.append(ImportedEvent("message", role, blocks, {
                    "attachment_type": atype, "timestamp": d.get("timestamp"), "uuid": d.get("uuid"),
                    "beside_tool_result": bool(d.get("renderedBesideToolResult"))}))
        else:  # "system" entries: hook summaries and the like, not part of the prompt
            stats["system_entries_skipped"] += 1

    for ev in events:  # in-memory bookkeeping only
        ev.meta.pop("block_indexes", None)
    stats["prompt_snapshots"] = len(system_snapshots)
    stats["distinct_system_prompts"] = len({block_hash({"s": s}) for s in system_snapshots})
    preamble = Preamble(
        system=system_snapshots[0] if system_snapshots else [],
        tools=list(tools.values()),
        known=False,
        note=("partial: system prompt from Claude Code's first prompt_snapshot; tools only from "
              "deferred_tools_record entries" if system_snapshots else "unknown: no prompt snapshot in the log"))
    return ImportedSession(title or name, events, preamble, model, dict(stats))


def _extend_assistant(ev: ImportedEvent, d: dict[str, Any], msg: dict[str, Any]) -> None:
    ev.meta["uuids"].append(d.get("uuid"))
    usage = msg.get("usage")
    if usage and usage.get("output_tokens", 0) >= (ev.meta.get("usage") or {}).get("output_tokens", -1):
        ev.meta["usage"] = usage
        ev.meta["stop_reason"] = msg.get("stop_reason")
    idx = d.get("apiBlockIndex")
    for j, raw in enumerate(msg.get("content") or []):
        key = (idx if idx is not None else None, j)
        if idx is not None and key in ev.meta["block_indexes"]:
            continue  # the same block logged twice
        ev.meta["block_indexes"].append(key)
        ev.blocks.append(Block(raw, "model"))


def _is_results_only(d: dict[str, Any]) -> bool:
    content = (d.get("message") or {}).get("content")
    return d.get("type") == "user" and isinstance(content, list) and bool(content) and all(
        isinstance(b, dict) and b.get("type") == "tool_result" for b in content)


def _user_origin(raw: dict[str, Any], d: dict[str, Any]) -> str:
    if raw.get("type") == "tool_result":
        return "tool"
    return "harness" if d.get("isMeta") else "user"
