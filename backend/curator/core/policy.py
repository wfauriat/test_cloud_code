"""Gate policy: one function decides auto / review / deny for any action.  PLAN D8.

Among matching rules the most restrictive wins (deny > review > auto), so an allow rule can
never hide a deny. When no rule matches, the answer is "review".
"""

from __future__ import annotations

from dataclasses import dataclass

ORDER = {"auto": 0, "review": 1, "deny": 2}


@dataclass(frozen=True)
class PolicyRule:
    decision: str  # "auto" | "review" | "deny"
    kind: str = "*"  # "prompt" | "tool_call" | "proposal" | "*"
    tool: str = "*"
    reason: str = ""

    def matches(self, kind: str, tool: str | None) -> bool:
        return self.kind in ("*", kind) and self.tool in ("*", tool or "")


# v1: review everything, plus read-only tools inside the workspace.
DEFAULT_RULES: tuple[PolicyRule, ...] = (
    PolicyRule("auto", "tool_call", "read_file", "read-only, confined to the workspace"),
    PolicyRule("auto", "tool_call", "list_dir", "read-only, confined to the workspace"),
    PolicyRule("auto", "tool_call", "grep", "read-only, confined to the workspace"),
    PolicyRule("review", "tool_call", "run_command", "commands always need a human"),
)


@dataclass(frozen=True)
class Decision:
    decision: str
    reason: str


def evaluate(kind: str, tool: str | None = None,
             rules: tuple[PolicyRule, ...] = DEFAULT_RULES) -> Decision:
    hits = [r for r in rules if r.matches(kind, tool)]
    if not hits:
        return Decision("review", "default: review everything")
    worst = max(hits, key=lambda r: ORDER[r.decision])
    return Decision(worst.decision, worst.reason)
