"""The brief: user-authored items rendered into one short text.  PLAN D7.

Only human-written or human-accepted items go in, because the brief is sent with system
authority. It is delivered once per user turn, right after the user's message.
"""

from __future__ import annotations

from typing import Any

ORDER = ("goal", "constraint", "decision", "fact")
TITLES = {"goal": "Goals", "constraint": "Constraints", "decision": "Decisions", "fact": "Facts"}


def render_brief(items: list[dict[str, Any]]) -> str | None:
    active = [i for i in items if i["status"] == "active"]
    if not active:
        return None
    lines = ["Session brief, maintained by the user. It takes precedence over older context."]
    for kind in ORDER:
        group = [i for i in active if i["type"] == kind]
        if group:
            lines.append(f"{TITLES[kind]}:")
            lines += [f"- {i['text']}" for i in group]
    return "\n".join(lines)
