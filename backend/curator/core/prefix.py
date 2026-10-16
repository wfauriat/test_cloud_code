"""Compare two requests the way the cache and thinking binding see them.  PLAN §4 step 7.

The question it answers: if `b` is sent after `a`, where does `b` stop being `a`?
Everything after that point is a cache write instead of a read, and any thinking block from
`a`'s history that sits after it was produced on a prefix that no longer exists.

Verdicts
- identical
- append_only: a is a strict prefix of b (the normal step inside an epoch)
- rewind:      b is a strict prefix of a (trailing turns dropped: cache reusable, thinking valid)
- diverge:     they differ at position `divergence`
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .model import THINKING_TYPES, Request
from .wire import Position, positions


@dataclass
class PrefixDiff:
    verdict: str
    divergence: int | None
    path_a: str | None
    path_b: str | None
    common_tokens: int
    a_after_tokens: int
    b_after_tokens: int
    # thinking from a's history placed after the divergence in b: 400, or dropped under drop_block
    thinking_at_risk: list[str] = field(default_factory=list)
    # thinking in a after the divergence that b no longer carries: reasoning the model loses
    thinking_lost: list[str] = field(default_factory=list)

    @property
    def safe(self) -> bool:
        """True when sending b after a keeps the cache prefix and every replayed thinking block."""
        return self.verdict in ("identical", "append_only", "rewind") or not self.thinking_at_risk

    def summary(self) -> str:
        if self.verdict == "identical":
            return "identical"
        if self.verdict == "append_only":
            return f"append-only: +{self.b_after_tokens:,} tokens after {self.common_tokens:,} shared"
        if self.verdict == "rewind":
            return f"rewind: drops {self.a_after_tokens:,} trailing tokens"
        return (f"diverges at {self.path_b or self.path_a} after {self.common_tokens:,} shared tokens; "
                f"{self.b_after_tokens:,} tokens rewritten; thinking at risk {len(self.thinking_at_risk)}, "
                f"lost {len(self.thinking_lost)}")


def diff(a: Request, b: Request, estimate=None) -> PrefixDiff:
    pa, pb = positions(a, estimate), positions(b, estimate)
    return diff_positions(pa, pb)


def diff_positions(pa: list[Position], pb: list[Position]) -> PrefixDiff:
    n = min(len(pa), len(pb))
    d = next((i for i in range(n) if pa[i].key != pb[i].key or pa[i].kind != pb[i].kind), n)
    if d == len(pa) == len(pb):
        verdict = "identical"
    elif d == len(pa):
        verdict = "append_only"
    elif d == len(pb):
        verdict = "rewind"
    else:
        verdict = "diverge"
    # Conservative: in a linear history every replayed thinking block after the divergence was
    # produced on a prefix that went through the changed position. (A branch can carry thinking
    # produced on its own prefix; the exact per-producer check is services/loop._invalid_thinking.)
    b_thinking = {p.key for p in pb if p.kind in THINKING_TYPES}
    return PrefixDiff(
        verdict=verdict,
        divergence=None if verdict == "identical" else d,
        path_a=pa[d].path if d < len(pa) else None,
        path_b=pb[d].path if d < len(pb) else None,
        common_tokens=sum(p.tokens for p in pa[:d]),
        a_after_tokens=sum(p.tokens for p in pa[d:]),
        b_after_tokens=sum(p.tokens for p in pb[d:]),
        thinking_at_risk=[p.path for p in pb[d:] if p.kind in THINKING_TYPES],
        thinking_lost=[p.path for p in pa[d:] if p.kind in THINKING_TYPES and p.key not in b_thinking],
    )
