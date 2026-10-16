"""Prices, call costs, and the economics of an edit.  PLAN §4 step 8.

Simplified cache model (automatic caching on the whole prompt):
- warm cache: the shared prefix is read, the rest is written;
- cold cache: everything is written.
It ignores the minimum cacheable size and the 20-block lookback; good enough to see the shape.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

MTOK = 1_000_000


@dataclass(frozen=True)
class Price:
    """$ per million tokens."""

    input: float
    output: float
    cache_read: float
    write_5m: float
    write_1h: float


PRICES: dict[str, Price] = {
    # From the bundled Claude API reference (cached 2026-10-06). Writes are 1.25x (5 min) / 2x (1 h).
    "claude-opus-5-5": Price(4.00, 20.00, 0.20, 5.00, 8.00),
    "claude-sonnet-5-5": Price(2.00, 10.00, 0.20, 2.50, 4.00),
    "claude-fable-5-1": Price(10.00, 50.00, 0.25, 12.50, 20.00),
    # QUESTION: verify Haiku 5.5 cache prices; 0.1x read assumed. Prompts over 100k tokens cost more.
    "claude-haiku-5-5": Price(0.10, 0.50, 0.01, 0.125, 0.20),
}
DEFAULT_MODEL = "claude-opus-5-5"

DROP_COST_REFERENCE = (
    "Anthropic's figures (multi-turn coding benchmark): dropping thinking once per session adds "
    "+2.5/3.9/4.5/20.1% output tokens (low/medium/high/max effort); every turn, "
    "+4.6/9.7/10.3/67.1%. Wide error bars; a reference, not a prediction.")


def price(model: str | None) -> Price:
    return PRICES.get(model or DEFAULT_MODEL, PRICES[DEFAULT_MODEL])


def usage_cost(model: str | None, usage: dict[str, Any]) -> float:
    """Cost of one response from its reported usage."""
    p = price(model)
    cc = usage.get("cache_creation") or {}
    w5 = cc.get("ephemeral_5m_input_tokens")
    w1 = cc.get("ephemeral_1h_input_tokens", 0)
    if w5 is None:  # older shape: one total, assume 5-minute writes
        w5 = usage.get("cache_creation_input_tokens", 0) - w1
    return (usage.get("input_tokens", 0) * p.input + usage.get("output_tokens", 0) * p.output
            + usage.get("cache_read_input_tokens", 0) * p.cache_read
            + w5 * p.write_5m + w1 * p.write_1h) / MTOK


@dataclass(frozen=True)
class CallEstimate:
    read_tokens: int
    write_tokens: int
    output_tokens: int
    read_cost: float
    write_cost: float
    output_cost: float

    @property
    def total(self) -> float:
        return self.read_cost + self.write_cost + self.output_cost


def estimate_call(model: str | None, total_tokens: int, cached_prefix_tokens: int, *,
                  warm: bool, ttl: str = "5m", output_tokens: int = 0) -> CallEstimate:
    p = price(model)
    read = min(cached_prefix_tokens, total_tokens) if warm else 0
    write = total_tokens - read
    wp = p.write_1h if ttl == "1h" else p.write_5m
    return CallEstimate(read, write, output_tokens, read * p.cache_read / MTOK, write * wp / MTOK,
                        output_tokens * p.output / MTOK)


@dataclass(frozen=True)
class EditEconomics:
    tokens_before: int
    tokens_after: int
    next_call_without: float  # $ input side of the next call if the edit is not applied
    next_call_with: float  # $ input side of the next call if it is
    extra_now: float  # with - without (negative = the edit saves money right away)
    savings_per_call: float  # on each later call, warm cache assumed
    pays_back_after: float | None  # calls; None if it never does, 0 if it saves now
    thinking_blocks_lost: int
    thinking_tokens_lost: int

    def summary(self) -> str:
        if self.extra_now <= 0:
            head = f"saves ${-self.extra_now:.2f} on the next call"
        elif self.pays_back_after is None:
            head = f"costs ${self.extra_now:.2f} more and never pays back"
        else:
            head = f"costs ${self.extra_now:.2f} more now, pays back after {self.pays_back_after:.0f} calls"
        tail = (f"; reasoning lost: {self.thinking_blocks_lost} thinking block(s)"
                if self.thinking_blocks_lost else "")
        return head + tail


def edit_economics(model: str | None, *, tokens_before: int, tokens_after: int,
                   divergence_tokens: int, warm: bool, ttl: str = "5m",
                   thinking_blocks_lost: int = 0, thinking_tokens_lost: int = 0) -> EditEconomics:
    """`divergence_tokens`: tokens before the first changed position (still cacheable)."""
    without = estimate_call(model, tokens_before, tokens_before, warm=warm, ttl=ttl).total
    with_ = estimate_call(model, tokens_after, divergence_tokens, warm=warm, ttl=ttl).total
    extra = with_ - without
    savings = max(tokens_before - tokens_after, 0) * price(model).cache_read / MTOK
    if extra <= 0:
        pays_back: float | None = 0
    elif savings > 0:
        pays_back = extra / savings
    else:
        pays_back = None
    return EditEconomics(tokens_before, tokens_after, without, with_, extra, savings, pays_back,
                         thinking_blocks_lost, thinking_tokens_lost)
