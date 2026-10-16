"""Core data model: plain dataclasses, no I/O.  PLAN §3.

Vocabulary
- Block: one API content block, kept as the exact JSON object received or sent (`raw`).
  Its identity is the hash of that JSON (wire.block_hash). `origin` says who produced it;
  it is metadata, never sent.
- Event: an immutable entry in a session's tree. Kind "message" carries a role and blocks;
  the other kinds (tool_exec, gate, import_meta, error) are records, never rendered.
- Span: an address. (event_id, index) points at one block; start/end narrow it to
  [start, end) code points of the block's text (segment.text_of). start=None = whole block.
- Op: an edit. Ops never modify events; the renderer folds them over the events.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

Role = Literal["user", "assistant", "system"]
Origin = Literal["user", "model", "tool", "harness", "curator"]
Verb = Literal["drop", "replace", "pin", "insert"]
OpState = Literal["draft", "staged", "applied", "revoked"]

THINKING_TYPES = frozenset({"thinking", "redacted_thinking"})
# Block types whose text we know how to read. Anything else is treated as opaque:
# kept byte for byte, addressable only as a whole (spec principle "opaque pass-through").
KNOWN_TYPES = frozenset({"text", "tool_use", "tool_result", "image", "document"}) | THINKING_TYPES


@dataclass(frozen=True)
class Block:
    raw: dict[str, Any]
    origin: Origin = "user"

    @property
    def type(self) -> str:
        return self.raw.get("type", "unknown")

    @property
    def is_thinking(self) -> bool:
        return self.type in THINKING_TYPES

    @property
    def opaque(self) -> bool:
        """Whole-only: no span edits, no rewriting. Thinking is signed; unknown types are unknown."""
        return self.is_thinking or self.type not in KNOWN_TYPES


@dataclass
class Event:
    id: str
    seq: int
    kind: str  # "message" | "tool_exec" | "gate" | "import_meta" | "error"
    role: Role | None = None
    blocks: list[Block] = field(default_factory=list)
    parent_id: str | None = None
    meta: dict[str, Any] = field(default_factory=dict)  # usage, model, timestamps, source refs

    @property
    def is_message(self) -> bool:
        return self.kind == "message"


@dataclass(frozen=True)
class Span:
    event_id: str
    index: int
    start: int | None = None
    end: int | None = None

    @property
    def whole(self) -> bool:
        return self.start is None

    @property
    def address(self) -> tuple[str, int]:
        return (self.event_id, self.index)

    def to_dict(self) -> dict[str, Any]:
        return {"event_id": self.event_id, "index": self.index, "start": self.start, "end": self.end}

    @staticmethod
    def from_dict(d: dict[str, Any]) -> Span:
        return Span(d["event_id"], int(d["index"]), d.get("start"), d.get("end"))


@dataclass
class Op:
    """An edit. Payload by verb:
    - drop:    {}
    - replace: {"text": str}           replacement for the targeted span(s)
    - pin:     {"repeat_in_brief": bool}
    - insert:  {"text": str}           a curator text block placed after the target block
    """

    id: str
    verb: Verb
    targets: list[Span]
    payload: dict[str, Any] = field(default_factory=dict)
    author: str = "human"  # "human" | "rule:<id>@<ver>" | "llm:<call>" | "assembler"
    rationale: str = ""
    state: OpState = "staged"
    group: str | None = None
    seq: int = 0

    @property
    def machine(self) -> bool:
        return self.author != "human"


@dataclass
class Preamble:
    """System prompt and tool definitions, frozen at session start (PLAN D11).

    For imports `known` is False: Claude Code logs carry at most a snapshot of the system
    prompt and the definitions of deferred tools, so what we hold is partial.
    """

    system: list[dict[str, Any]] = field(default_factory=list)
    tools: list[dict[str, Any]] = field(default_factory=list)
    known: bool = True
    note: str = ""


@dataclass
class Request:
    params: dict[str, Any]  # model, max_tokens, thinking, output_config, ...
    system: list[dict[str, Any]]
    tools: list[dict[str, Any]]
    messages: list[dict[str, Any]]  # {"role": ..., "content": [raw blocks]}

    def to_api(self) -> dict[str, Any]:
        body: dict[str, Any] = dict(self.params)
        if self.system:
            body["system"] = self.system
        if self.tools:
            body["tools"] = self.tools
        body["messages"] = self.messages
        return body


@dataclass(frozen=True)
class Source:
    """Where one block of a rendered request came from (one entry of the source map)."""

    kind: str  # "event" | "edited" | "placeholder" | "note" | "inserted" | "brief"
    event_id: str | None = None
    index: int | None = None
    op_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class Diagnostic:
    code: str
    message: str
    where: str = ""


@dataclass
class RenderResult:
    request: Request
    # (message index, content index) -> Source
    source_map: dict[tuple[int, int], Source]
    diagnostics: list[Diagnostic]
    # Indices (in request.messages) of assistant messages whose source had thinking / still has it.
    thinking_had: list[int] = field(default_factory=list)
    thinking_kept: list[int] = field(default_factory=list)
