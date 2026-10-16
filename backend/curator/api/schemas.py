"""API shapes. They are the contract with the UI: the TS types are generated from them
(`npm run gen:api` in frontend/), so nothing is typed twice by hand.  PLAN §2.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class SessionSummary(BaseModel):
    id: str
    title: str
    source: str
    created_at: str
    messages: int


class ImportRequest(BaseModel):
    path: str


class CalibrationView(BaseModel):
    scale: float
    preamble_tokens: float
    r2: float
    n: int


class SessionDetail(BaseModel):
    id: str
    title: str
    source: str
    config: dict[str, Any]
    preamble_note: str
    preamble_known: bool
    preamble_system_tokens: int
    preamble_tools: int
    composition: dict[str, int]
    calibration: CalibrationView | None
    messages: int
    calls: int
    ops: int
    import_stats: dict[str, Any] | None


class BlockStatus(BaseModel):
    state: str  # "kept" | "dropped" | "edited"
    pending: bool  # the change is staged, not yet applied
    pinned: bool
    op_ids: list[str]
    shadowed: list[str]


class BlockView(BaseModel):
    index: int
    type: str
    origin: str
    category: str
    tokens: int
    text: str
    gist: str
    tool_name: str | None = None
    tool_use_id: str | None = None
    is_error: bool = False
    status: BlockStatus


class MessageView(BaseModel):
    event_id: str
    seq: int
    role: str
    label: str  # "user" | "assistant" | "harness: <type>" | "tool results"
    timestamp: str | None
    call_n: int | None  # for assistant messages carrying usage: index in the timeline
    tokens: int
    blocks: list[BlockView]


class BlockDetail(BaseModel):
    event_id: str
    index: int
    raw: dict[str, Any]
    segments: list[dict[str, Any]]
    ops: list[dict[str, Any]]
    proposals: list[dict[str, Any]]


class TimelineRow(BaseModel):
    n: int
    event_id: str
    seq: int
    timestamp: str | None
    uncached: int
    cache_read: int
    cache_write: int
    output: int
    total_input: int
    ttl: str
    est_messages_before: int
    cache_break: bool
    lost: int
    reason: str | None
    cost: float


class ProposalView(BaseModel):
    id: str
    rule: str
    rationale: str
    verb: str
    targets: list[dict[str, Any]]
    payload: dict[str, Any]
    tokens_before: int
    tokens_after: int
    tokens_saved: int


class OpView(BaseModel):
    id: str
    verb: str
    targets: list[dict[str, Any]]
    payload: dict[str, Any]
    author: str
    rationale: str
    state: str
    seq: int


class OpCreate(BaseModel):
    verb: str
    targets: list[dict[str, Any]]
    payload: dict[str, Any] = {}
    rationale: str = ""
    author: str = "human"


class StageProposals(BaseModel):
    ids: list[str] | None = None  # None = all current proposals


class BriefItemView(BaseModel):
    id: str
    type: str
    text: str
    status: str
    author: str


class BriefItemCreate(BaseModel):
    type: str  # goal | decision | constraint | fact
    text: str


class BriefItemUpdate(BaseModel):
    text: str | None = None
    status: str | None = None


class RenderedRequest(BaseModel):
    request: dict[str, Any]
    source_map: list[dict[str, Any]]
    diagnostics: list[dict[str, Any]]
    validation: list[dict[str, Any]]
    tokens_estimated: int
    hash: str


class Observation(BaseModel):
    id: int
    ts: str
    session_id: str | None
    kind: str
    payload: dict[str, Any]


class LiveCreate(BaseModel):
    title: str
    workspace: str
    model: str = "claude-opus-5-5"
    effort: str = "medium"
    allow_commands: bool = False
    ttl: str = "5m"
    fallbacks: bool = True


class LiveMessage(BaseModel):
    text: str


class LiveApprove(BaseModel):
    hash: str


class LiveReject(BaseModel):
    reason: str = ""


class LiveTools(BaseModel):
    decisions: dict[str, dict[str, Any]]


class LiveSettings(BaseModel):
    auto_continue: bool


class CallSummary(BaseModel):
    id: str
    epoch: int
    model: str | None
    stop_reason: str | None
    usage: dict[str, Any] | None
    cost: float | None
    latency_ms: int | None
    error: str | None
    created_at: str


class ABSpec(BaseModel):
    call_n: int | None = None
    arms: list[str] = ["as_is", "curated", "server_clear", "curated_brief"]
    keep_n: int = 3
    model: str = "claude-opus-5-5"
    effort: str = "medium"
    max_tokens: int = 4096
    system_text: str | None = None


class ABVerdict(BaseModel):
    preferred: str | None = None
    notes: str = ""


class SummaryRequest(BaseModel):
    targets: list[dict[str, Any]]
    model: str = "claude-haiku-5-5"


class SummaryAccept(BaseModel):
    targets: list[dict[str, Any]]
    text: str
    call_id: str
