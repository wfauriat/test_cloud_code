"""Token estimates and their calibration.  PLAN §4 step 2.

Every number from this module is an *estimate*. Exact counts come only from the API
(`count_tokens`, or `usage` on a response). The UI marks the difference.

# QUESTION: CHARS_PER_TOKEN is a rough prior for the current tokenizer; calibrate() replaces it
# per session when reported usage is available (imports carry it on every assistant message).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any

CHARS_PER_TOKEN = 3.2
BLOCK_OVERHEAD = 4  # role/type framing per block
IMAGE_TOKENS = 1600  # QUESTION: flat guess; images are rare in coding sessions


def estimate_text(s: str, ratio: float = CHARS_PER_TOKEN) -> int:
    return math.ceil(len(s) / ratio) if s else 0


def estimate_raw(raw: dict[str, Any], ratio: float = CHARS_PER_TOKEN, hint: int | None = None) -> int:
    """Estimate one block. `hint` overrides the content-based guess (e.g. thinking tokens
    reported in usage, which the visible text cannot give: under display "omitted" the
    thinking text is empty and only the signature remains)."""
    from .segment import text_of
    from .wire import dumps

    if hint is not None:
        return hint + BLOCK_OVERHEAD
    t = raw.get("type")
    if t in ("thinking", "redacted_thinking"):
        text = raw.get("thinking", "")
        if text:
            return estimate_text(text, ratio) + BLOCK_OVERHEAD
        # QUESTION: the signature carries the encrypted reasoning; its size is a weak proxy.
        sig = raw.get("signature") or raw.get("data") or ""
        return estimate_text(sig, ratio * 2) + BLOCK_OVERHEAD
    if t == "image":
        return IMAGE_TOKENS
    if t == "tool_use":
        return estimate_text(raw.get("name", "") + dumps(raw.get("input", {})), ratio) + BLOCK_OVERHEAD
    if t in ("text", "tool_result"):
        return estimate_text(text_of(raw), ratio) + BLOCK_OVERHEAD
    return estimate_text(dumps(raw), ratio) + BLOCK_OVERHEAD


@dataclass(frozen=True)
class Calibration:
    """reported_input ≈ preamble_tokens + scale × estimated_messages, fitted over calls.

    `preamble_tokens` estimates what the log does not contain (system prompt + tool
    definitions); `scale` corrects the chars-per-token prior.
    """

    scale: float
    preamble_tokens: float
    r2: float
    n: int


def calibrate(points: list[tuple[int, int]]) -> Calibration | None:
    """Least squares over (estimated tokens before the call, reported total input of the call)."""
    pts = [(float(e), float(r)) for e, r in points if r > 0]
    n = len(pts)
    if n < 3:
        return None
    mx = sum(e for e, _ in pts) / n
    my = sum(r for _, r in pts) / n
    sxx = sum((e - mx) ** 2 for e, _ in pts)
    if sxx == 0:
        return None
    sxy = sum((e - mx) * (r - my) for e, r in pts)
    b = sxy / sxx
    a = my - b * mx
    ss_tot = sum((r - my) ** 2 for _, r in pts)
    ss_res = sum((r - (a + b * e)) ** 2 for e, r in pts)
    r2 = 1 - ss_res / ss_tot if ss_tot else 1.0
    return Calibration(scale=b, preamble_tokens=a, r2=r2, n=n)
