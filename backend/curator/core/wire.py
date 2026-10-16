"""Wire helpers: hashing, comparison keys, and the flattened view of a request.  PLAN D3.

Rule: blocks are stored and replayed as the JSON objects we received. Nothing here rebuilds
a block; these functions only *look* at blocks.

# QUESTION: comparison keys keep key order (no sort_keys). A key-order change is reported as a
# change. That is the conservative choice: it may flag a change the server would not see, but it
# never hides one.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Any

from .model import Request

# Request params that change the messages cache when they change (prompt-caching invalidation
# hierarchy: model > tools > system > thinking/effort > messages).
CACHE_RELEVANT_PARAMS = ("thinking", "output_config")


def dumps(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def block_hash(raw: dict[str, Any]) -> str:
    return hashlib.sha256(dumps(raw).encode()).hexdigest()


def without_cache_control(raw: Any) -> Any:
    """Moving cache markers does not change the prompt, so comparisons ignore them."""
    if isinstance(raw, dict):
        return {k: without_cache_control(v) for k, v in raw.items() if k != "cache_control"}
    if isinstance(raw, list):
        return [without_cache_control(v) for v in raw]
    return raw


def compare_key(raw: Any) -> str:
    return dumps(without_cache_control(raw))


def request_hash(req: Request) -> str:
    """Hash of everything sent. Gate approvals are tied to it (PLAN D8)."""
    return hashlib.sha256(dumps(req.to_api()).encode()).hexdigest()


@dataclass(frozen=True)
class Position:
    """One position of a request in cache order: model, tools, system, params, then messages.

    `kind` is the block type for content positions, or "model" / "tool" / "system" / "params" /
    "role" for the structural ones. A "role" position marks the start of each message, so two
    requests that group the same blocks differently do not compare equal.
    """

    path: str
    kind: str
    key: str
    tokens: int = 0


def positions(req: Request, estimate=None) -> list[Position]:
    from .tokens import estimate_raw  # local import: tokens imports nothing from here

    est = estimate or estimate_raw
    out = [Position("model", "model", str(req.params.get("model")))]
    out += [Position(f"tools[{i}]", "tool", compare_key(t), est({"type": "text", "text": dumps(t)}))
            for i, t in enumerate(req.tools)]
    out += [Position(f"system[{i}]", "system", compare_key(b), est(b))
            for i, b in enumerate(req.system)]
    params = {k: req.params.get(k) for k in CACHE_RELEVANT_PARAMS}
    out.append(Position("params", "params", dumps(params)))
    for k, msg in enumerate(req.messages):
        out.append(Position(f"messages[{k}]", "role", msg["role"]))
        content = msg["content"]
        if isinstance(content, str):
            content = [{"type": "text", "text": content}]
        for j, b in enumerate(content):
            out.append(Position(f"messages[{k}].content[{j}]", b.get("type", "unknown"),
                                compare_key(b), est(b)))
    return out
