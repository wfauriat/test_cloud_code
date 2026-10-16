"""Text of blocks, and a deterministic segmenter.  PLAN §4 step 1.

Offsets are Python string indices, i.e. Unicode code points, so spans stay valid for any
future non-Python component that counts the same way.

Segments are a UI and citation unit only. Ops store spans, never segment ids, so changing
the segmenter (bump SEGMENTER_VERSION) never orphans an op.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from .wire import dumps

SEGMENTER_VERSION = 1
TOOL_OUTPUT_CHUNK_LINES = 40


def text_of(raw: dict[str, Any]) -> str:
    """The human-readable text of a block. For tool_use it is the input JSON (read-only)."""
    t = raw.get("type")
    if t == "text":
        return raw.get("text", "")
    if t == "thinking":
        return raw.get("thinking", "")
    if t == "tool_use":
        return dumps(raw.get("input", {}))
    if t == "tool_result":
        c = raw.get("content")
        if c is None:
            return ""
        if isinstance(c, str):
            return c
        return "\n".join(p.get("text", "") for p in c if isinstance(p, dict) and p.get("type") == "text")
    return ""


def editable(raw: dict[str, Any]) -> bool:
    """Span edits are allowed on text blocks and on tool results made only of text."""
    t = raw.get("type")
    if t == "text":
        return True
    if t == "tool_result":
        c = raw.get("content")
        return c is None or isinstance(c, str) or all(
            isinstance(p, dict) and p.get("type") == "text" for p in c)
    return False


@dataclass(frozen=True)
class Segment:
    start: int
    end: int
    kind: str  # "paragraph" | "code" | "lines"


_FENCE = re.compile(r"^```.*?^```[^\n]*$", re.M | re.S)
_BLANK = re.compile(r"\n[ \t]*\n")


def segments(text: str, *, tool_output: bool = False) -> list[Segment]:
    if not text:
        return []
    if tool_output:
        return _line_chunks(text, 0, len(text))
    out: list[Segment] = []
    pos = 0
    for m in _FENCE.finditer(text):
        out += _paragraphs(text, pos, m.start())
        out.append(Segment(m.start(), m.end(), "code"))
        pos = m.end()
    out += _paragraphs(text, pos, len(text))
    return out


def _paragraphs(text: str, start: int, end: int) -> list[Segment]:
    out, pos = [], start
    for m in _BLANK.finditer(text, start, end):
        if text[pos:m.start()].strip():
            out.append(Segment(pos, m.start(), "paragraph"))
        pos = m.end()
    if text[pos:end].strip():
        out.append(Segment(pos, end, "paragraph"))
    return out


def _line_chunks(text: str, start: int, end: int) -> list[Segment]:
    out, pos, count, chunk_start = [], start, 0, start
    while pos < end:
        nl = text.find("\n", pos, end)
        pos = end if nl == -1 else nl + 1
        count += 1
        if count == TOOL_OUTPUT_CHUNK_LINES:
            out.append(Segment(chunk_start, pos, "lines"))
            chunk_start, count = pos, 0
    if chunk_start < end:
        out.append(Segment(chunk_start, end, "lines"))
    return out
