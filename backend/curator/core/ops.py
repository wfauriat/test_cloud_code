"""Folding ops over blocks.  PLAN §4 step 3, D5.

`fold` turns the active ops into one BlockPlan per touched block: keep, drop, or rewrite with
new text. Overlaps: the later op (by seq) wins; ops that end up winning nowhere are reported as
shadowed so the UI can flag them.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field

from .model import Block, Op, Span
from .segment import editable, text_of

BlockOf = Callable[[Span], Block | None]


@dataclass
class BlockPlan:
    action: str = "keep"  # "keep" | "drop" | "rewrite"
    text: str | None = None  # new text when action == "rewrite"
    op_ids: list[str] = field(default_factory=list)
    pinned: bool = False
    shadowed: list[str] = field(default_factory=list)


def active_ops(ops: list[Op], include_staged: bool = True) -> list[Op]:
    """Applied ops are on the wire. Staged ops count only in previews (include_staged)."""
    states = ("staged", "applied") if include_staged else ("applied",)
    return sorted((o for o in ops if o.state in states), key=lambda o: o.seq)


def pinned_addresses(ops: list[Op]) -> set[tuple[str, int]]:
    return {s.address for o in ops if o.verb == "pin" and o.state in ("staged", "applied")
            for s in o.targets}


def check_op(op: Op, block_of: BlockOf, pinned: set[tuple[str, int]]) -> list[str]:
    """Reasons to refuse an op at creation time (empty list = accepted)."""
    errors: list[str] = []
    if op.verb in ("replace", "insert") and not isinstance(op.payload.get("text"), str):
        errors.append(f"{op.verb} needs payload.text")
    if op.verb == "insert" and len(op.targets) != 1:
        errors.append("insert needs exactly one anchor block")
    if not op.targets:
        errors.append("no target")
    for span in op.targets:
        b = block_of(span)
        if b is None:
            errors.append(f"unknown block {span.address}")
            continue
        if op.verb in ("drop", "replace"):
            if not span.whole and not editable(b.raw):
                errors.append(f"{b.type} block {span.address} can only be targeted whole")
            if op.verb == "replace" and (b.opaque or b.type == "tool_use"):
                # QUESTION: rewriting the model's own tool call would misreport what it did.
                errors.append(f"{b.type} block {span.address} can be dropped, not rewritten")
            if op.machine and span.address in pinned:
                errors.append(f"block {span.address} is pinned; machine ops may not touch it")
        if not span.whole:
            n = len(text_of(b.raw))
            if not (0 <= (span.start or 0) < (span.end or 0) <= n):
                errors.append(f"span [{span.start}, {span.end}) outside block text (len {n})")
    return errors


def fold(ops: list[Op], block_of: BlockOf) -> dict[tuple[str, int], BlockPlan]:
    """`ops` must already be the active ops in seq order (see active_ops)."""
    edits: dict[tuple[str, int], list[tuple[Op, int, int]]] = {}
    for op in ops:
        if op.verb not in ("drop", "replace"):
            continue
        for span in op.targets:
            b = block_of(span)
            if b is None:
                continue
            n = len(text_of(b.raw))
            s, e = (0, n) if span.whole else (span.start or 0, span.end or n)
            edits.setdefault(span.address, []).append((op, s, e))

    plans: dict[tuple[str, int], BlockPlan] = {}
    for addr, items in edits.items():
        b = block_of(Span(*addr))
        assert b is not None
        plan = BlockPlan(op_ids=[op.id for op, _, _ in items])
        if not editable(b.raw):
            # Whole-only blocks (thinking, tool_use, images, unknown): any active drop removes them.
            plan.action = "drop" if any(op.verb == "drop" for op, _, _ in items) else "keep"
        else:
            plan.action, plan.text, plan.shadowed = _paint(text_of(b.raw), items)
        plans[addr] = plan

    for addr in pinned_addresses(ops):
        plans.setdefault(addr, BlockPlan()).pinned = True
    return plans


def _paint(text: str, items: list[tuple[Op, int, int]]) -> tuple[str, str | None, list[str]]:
    """Paint op intervals over the text; the last op covering a piece wins that piece."""
    points = sorted({0, len(text), *(s for _, s, _ in items), *(e for _, _, e in items)})
    pieces: list[tuple[int, int, Op | None]] = []
    for p, q in zip(points, points[1:], strict=False):
        winner = next((op for op, s, e in reversed(items) if s <= p and q <= e), None)
        pieces.append((p, q, winner))
    winners = {w.id for _, _, w in pieces if w is not None}
    shadowed = [op.id for op, _, _ in items if op.id not in winners]

    if not text:  # empty block: only a whole drop/replace can apply
        last = items[-1][0]
        if last.verb == "replace":
            return "rewrite", last.payload.get("text", ""), shadowed
        return "drop", None, shadowed

    out: list[str] = []
    emitted: set[str] = set()
    for p, q, w in pieces:
        if w is None:
            out.append(text[p:q])
        elif w.verb == "replace" and w.id not in emitted:
            out.append(w.payload.get("text", ""))
            emitted.add(w.id)
    new = "".join(out)
    if not emitted and not new:
        return "drop", None, shadowed
    return "rewrite", new, shadowed


def inserts_by_anchor(ops: list[Op]) -> dict[tuple[str, int], list[Op]]:
    out: dict[tuple[str, int], list[Op]] = {}
    for op in ops:
        if op.verb == "insert" and op.targets:
            out.setdefault(op.targets[0].address, []).append(op)
    return out
