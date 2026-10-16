"""SQLite store. Every query is in this file, in plain SQL.  PLAN §3.

Tables are append-only except for two mutable fields, both noted where they change:
`sessions.head` (current leaf of the event tree) and `ops.state` (draft → staged → applied |
revoked; each change is also written to `observations`).
Blocks are content-addressed: a block shared by hundreds of requests is stored once.
"""

from __future__ import annotations

import json
import sqlite3
import threading
import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from ..core.model import Block, Event, Op, Preamble, Span
from ..core.wire import block_hash, dumps

SCHEMA = """
CREATE TABLE IF NOT EXISTS sessions (
    id TEXT PRIMARY KEY, title TEXT, source TEXT, created_at TEXT,
    config TEXT NOT NULL DEFAULT '{}', preamble TEXT NOT NULL DEFAULT '{}', head TEXT
);
CREATE TABLE IF NOT EXISTS blocks (hash TEXT PRIMARY KEY, json TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS events (
    id TEXT PRIMARY KEY, session_id TEXT NOT NULL, parent_id TEXT, seq INTEGER NOT NULL,
    kind TEXT NOT NULL, role TEXT, meta TEXT NOT NULL DEFAULT '{}', created_at TEXT
);
CREATE INDEX IF NOT EXISTS events_by_session ON events(session_id, seq);
CREATE TABLE IF NOT EXISTS event_blocks (
    event_id TEXT NOT NULL, idx INTEGER NOT NULL, hash TEXT NOT NULL, origin TEXT NOT NULL,
    PRIMARY KEY (event_id, idx)
);
CREATE TABLE IF NOT EXISTS ops (
    id TEXT PRIMARY KEY, session_id TEXT NOT NULL, grp TEXT, verb TEXT NOT NULL,
    targets TEXT NOT NULL, payload TEXT NOT NULL, author TEXT NOT NULL, rationale TEXT,
    state TEXT NOT NULL, seq INTEGER NOT NULL, created_at TEXT
);
CREATE TABLE IF NOT EXISTS calls (
    id TEXT PRIMARY KEY, session_id TEXT NOT NULL, epoch INTEGER NOT NULL, request TEXT NOT NULL,
    response TEXT, usage TEXT, cost REAL, latency_ms INTEGER, model TEXT, stop_reason TEXT,
    error TEXT, created_at TEXT
);
CREATE TABLE IF NOT EXISTS brief_items (
    id TEXT PRIMARY KEY, session_id TEXT NOT NULL, type TEXT NOT NULL, text TEXT NOT NULL,
    status TEXT NOT NULL, author TEXT NOT NULL, seq INTEGER NOT NULL, created_at TEXT
);
CREATE TABLE IF NOT EXISTS runs (
    id TEXT PRIMARY KEY, session_id TEXT NOT NULL, kind TEXT NOT NULL, spec TEXT NOT NULL,
    result TEXT, verdict TEXT, created_at TEXT
);
CREATE TABLE IF NOT EXISTS observations (
    id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT NOT NULL, session_id TEXT, kind TEXT NOT NULL,
    payload TEXT NOT NULL
);
"""


def now() -> str:
    return datetime.now(UTC).isoformat(timespec="milliseconds")


def new_id() -> str:
    return uuid.uuid4().hex[:12]


class Store:
    """One connection per thread (the API serves sync routes from a thread pool, and a sqlite
    connection must not be shared across threads). In-memory stores keep a single connection."""

    def __init__(self, path: str | Path = ":memory:"):
        self.path = str(path)
        self._local = threading.local()
        self._shared = None
        if self.path == ":memory:":
            self._shared = self._connect()
        else:
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            self.db.execute("PRAGMA journal_mode=WAL")

    def _connect(self) -> sqlite3.Connection:
        con = sqlite3.connect(self.path, check_same_thread=False, timeout=10)
        con.row_factory = sqlite3.Row
        con.executescript(SCHEMA)
        return con

    @property
    def db(self) -> sqlite3.Connection:
        if self._shared is not None:
            return self._shared
        con = getattr(self._local, "con", None)
        if con is None:
            con = self._local.con = self._connect()
        return con

    # -- sessions -------------------------------------------------------------------------
    def create_session(self, title: str, source: str, *, config: dict | None = None,
                       preamble: Preamble | None = None) -> str:
        sid = new_id()
        p = preamble or Preamble()
        self.db.execute(
            "INSERT INTO sessions (id, title, source, created_at, config, preamble) VALUES (?,?,?,?,?,?)",
            (sid, title, source, now(), dumps(config or {}),
             dumps({"system": p.system, "tools": p.tools, "known": p.known, "note": p.note})))
        self.db.commit()
        return sid

    def sessions(self) -> list[dict[str, Any]]:
        rows = self.db.execute(
            "SELECT s.id, s.title, s.source, s.created_at, "
            "(SELECT COUNT(*) FROM events e WHERE e.session_id = s.id AND e.kind = 'message') AS messages "
            "FROM sessions s ORDER BY s.created_at DESC").fetchall()
        return [dict(r) for r in rows]

    def session(self, sid: str) -> dict[str, Any]:
        r = self.db.execute("SELECT * FROM sessions WHERE id = ?", (sid,)).fetchone()
        if r is None:
            raise KeyError(sid)
        d = dict(r)
        d["config"] = json.loads(d["config"])
        d["preamble"] = json.loads(d["preamble"])
        return d

    def preamble(self, sid: str) -> Preamble:
        p = self.session(sid)["preamble"]
        return Preamble(p.get("system", []), p.get("tools", []), p.get("known", True), p.get("note", ""))

    def set_head(self, sid: str, event_id: str) -> None:  # mutable field: current leaf
        self.db.execute("UPDATE sessions SET head = ? WHERE id = ?", (event_id, sid))
        self.db.commit()

    def update_config(self, sid: str, config: dict) -> None:
        self.db.execute("UPDATE sessions SET config = ? WHERE id = ?", (dumps(config), sid))
        self.db.commit()

    # -- events ---------------------------------------------------------------------------
    def add_event(self, sid: str, kind: str, *, role: str | None = None, blocks: list[Block] = (),
                  parent_id: str | None = None, meta: dict | None = None, commit: bool = True,
                  set_head: bool = True) -> Event:
        eid = new_id()
        seq = self.db.execute("SELECT COALESCE(MAX(seq), 0) + 1 FROM events WHERE session_id = ?",
                              (sid,)).fetchone()[0]
        self.db.execute(
            "INSERT INTO events (id, session_id, parent_id, seq, kind, role, meta, created_at) "
            "VALUES (?,?,?,?,?,?,?,?)", (eid, sid, parent_id, seq, kind, role, dumps(meta or {}), now()))
        for i, b in enumerate(blocks):
            h = block_hash(b.raw)
            self.db.execute("INSERT OR IGNORE INTO blocks (hash, json) VALUES (?, ?)", (h, dumps(b.raw)))
            self.db.execute("INSERT INTO event_blocks (event_id, idx, hash, origin) VALUES (?,?,?,?)",
                            (eid, i, h, b.origin))
        if set_head:
            self.db.execute("UPDATE sessions SET head = ? WHERE id = ?", (eid, sid))
        if commit:
            self.db.commit()
        return Event(eid, seq, kind, role, list(blocks), parent_id, meta or {})

    def commit(self) -> None:
        self.db.commit()

    def events(self, sid: str) -> list[Event]:
        rows = self.db.execute("SELECT * FROM events WHERE session_id = ? ORDER BY seq", (sid,)).fetchall()
        blocks: dict[str, list[Block]] = {}
        for r in self.db.execute(
                "SELECT eb.event_id, eb.idx, eb.origin, b.json FROM event_blocks eb "
                "JOIN blocks b ON b.hash = eb.hash JOIN events e ON e.id = eb.event_id "
                "WHERE e.session_id = ? ORDER BY e.seq, eb.idx", (sid,)):
            blocks.setdefault(r["event_id"], []).append(Block(json.loads(r["json"]), r["origin"]))
        return [Event(r["id"], r["seq"], r["kind"], r["role"], blocks.get(r["id"], []), r["parent_id"],
                      json.loads(r["meta"])) for r in rows]

    def chain(self, sid: str, leaf: str | None = None) -> list[Event]:
        """Events from the root to `leaf` (default: the session head), following parent ids."""
        evs = self.events(sid)
        by_id = {e.id: e for e in evs}
        cur = leaf or self.session(sid)["head"]
        out = []
        while cur and cur in by_id:
            out.append(by_id[cur])
            cur = by_id[cur].parent_id
        return list(reversed(out))

    def put_block(self, raw: dict) -> str:
        h = block_hash(raw)
        self.db.execute("INSERT OR IGNORE INTO blocks (hash, json) VALUES (?, ?)", (h, dumps(raw)))
        return h

    def get_blocks(self, hashes: list[str]) -> dict[str, dict]:
        out: dict[str, dict] = {}
        for i in range(0, len(hashes), 500):
            chunk = hashes[i:i + 500]
            q = f"SELECT hash, json FROM blocks WHERE hash IN ({','.join('?' * len(chunk))})"
            out.update({r[0]: json.loads(r[1]) for r in self.db.execute(q, chunk)})
        return out

    def known_block_hashes(self, sid: str) -> set[str]:
        rows = self.db.execute("SELECT eb.hash FROM event_blocks eb JOIN events e ON e.id = eb.event_id "
                               "WHERE e.session_id = ?", (sid,))
        return {r[0] for r in rows}

    # -- ops ------------------------------------------------------------------------------
    def add_op(self, sid: str, op: Op) -> Op:
        op.seq = self.db.execute("SELECT COALESCE(MAX(seq), 0) + 1 FROM ops WHERE session_id = ?",
                                 (sid,)).fetchone()[0]
        self.db.execute(
            "INSERT INTO ops (id, session_id, grp, verb, targets, payload, author, rationale, state, seq, "
            "created_at) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (op.id, sid, op.group, op.verb, dumps([t.to_dict() for t in op.targets]), dumps(op.payload),
             op.author, op.rationale, op.state, op.seq, now()))
        self.db.commit()
        return op

    def ops(self, sid: str) -> list[Op]:
        rows = self.db.execute("SELECT * FROM ops WHERE session_id = ? ORDER BY seq", (sid,)).fetchall()
        return [Op(r["id"], r["verb"], [Span.from_dict(t) for t in json.loads(r["targets"])],
                   json.loads(r["payload"]), r["author"], r["rationale"] or "", r["state"], r["grp"], r["seq"])
                for r in rows]

    def set_op_state(self, sid: str, op_id: str, state: str) -> None:  # mutable field, logged
        self.db.execute("UPDATE ops SET state = ? WHERE id = ? AND session_id = ?", (state, op_id, sid))
        self.observe(sid, "op_state", {"op": op_id, "state": state}, commit=False)
        self.db.commit()

    # -- calls (wire log, live sessions) ---------------------------------------------------
    def add_call(self, sid: str, *, epoch: int, request: dict, response: dict | None, usage: dict | None,
                 cost: float | None, latency_ms: int | None, model: str | None, stop_reason: str | None,
                 error: str | None = None) -> str:
        cid = new_id()
        self.db.execute(
            "INSERT INTO calls (id, session_id, epoch, request, response, usage, cost, latency_ms, model, "
            "stop_reason, error, created_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            (cid, sid, epoch, dumps(request), dumps(response) if response is not None else None,
             dumps(usage) if usage is not None else None, cost, latency_ms, model, stop_reason, error, now()))
        self.db.commit()
        return cid

    def calls(self, sid: str) -> list[dict[str, Any]]:
        rows = self.db.execute("SELECT * FROM calls WHERE session_id = ? ORDER BY created_at, rowid",
                               (sid,)).fetchall()
        out = []
        for r in rows:
            d = dict(r)
            for k in ("request", "response", "usage"):
                d[k] = json.loads(d[k]) if d[k] else None
            out.append(d)
        return out

    # -- brief ----------------------------------------------------------------------------
    def add_brief_item(self, sid: str, type_: str, text: str, author: str = "human") -> str:
        bid = new_id()
        seq = self.db.execute("SELECT COALESCE(MAX(seq), 0) + 1 FROM brief_items WHERE session_id = ?",
                              (sid,)).fetchone()[0]
        self.db.execute("INSERT INTO brief_items (id, session_id, type, text, status, author, seq, created_at) "
                        "VALUES (?,?,?,?,?,?,?,?)", (bid, sid, type_, text, "active", author, seq, now()))
        self.db.commit()
        return bid

    def brief_items(self, sid: str) -> list[dict[str, Any]]:
        rows = self.db.execute("SELECT * FROM brief_items WHERE session_id = ? ORDER BY seq", (sid,))
        return [dict(r) for r in rows]

    def update_brief_item(self, sid: str, bid: str, *, text: str | None = None, status: str | None = None) -> None:
        if text is not None:
            self.db.execute("UPDATE brief_items SET text = ? WHERE id = ? AND session_id = ?", (text, bid, sid))
        if status is not None:
            self.db.execute("UPDATE brief_items SET status = ? WHERE id = ? AND session_id = ?", (status, bid, sid))
        self.db.commit()

    # -- runs (experiments) ----------------------------------------------------------------
    def add_run(self, sid: str, kind: str, spec: dict, result: dict | None = None) -> str:
        rid = new_id()
        self.db.execute("INSERT INTO runs (id, session_id, kind, spec, result, created_at) VALUES (?,?,?,?,?,?)",
                        (rid, sid, kind, dumps(spec), dumps(result) if result is not None else None, now()))
        self.db.commit()
        return rid

    def set_run(self, rid: str, *, result: dict | None = None, verdict: dict | None = None) -> None:
        if result is not None:
            self.db.execute("UPDATE runs SET result = ? WHERE id = ?", (dumps(result), rid))
        if verdict is not None:
            self.db.execute("UPDATE runs SET verdict = ? WHERE id = ?", (dumps(verdict), rid))
        self.db.commit()

    def runs(self, sid: str) -> list[dict[str, Any]]:
        rows = self.db.execute("SELECT * FROM runs WHERE session_id = ? ORDER BY created_at", (sid,))
        out = []
        for r in rows:
            d = dict(r)
            for k in ("spec", "result", "verdict"):
                d[k] = json.loads(d[k]) if d[k] else None
            out.append(d)
        return out

    # -- observations ---------------------------------------------------------------------
    def observe(self, sid: str | None, kind: str, payload: dict, commit: bool = True) -> None:
        self.db.execute("INSERT INTO observations (ts, session_id, kind, payload) VALUES (?,?,?,?)",
                        (now(), sid, kind, dumps(payload)))
        if commit:
            self.db.commit()

    def observations(self, sid: str | None = None) -> list[dict[str, Any]]:
        q = "SELECT * FROM observations" + (" WHERE session_id = ?" if sid else "") + " ORDER BY id"
        rows = self.db.execute(q, (sid,) if sid else ())
        return [{**dict(r), "payload": json.loads(r["payload"])} for r in rows]
