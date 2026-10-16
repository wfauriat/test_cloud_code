"""Model provider port: one narrow interface (send, count_tokens), the real Anthropic client, and
two fakes (scripted for tests, echo for trying the UI without an API key).  PLAN §5.3.

Wire fidelity (PLAN D3): the reply's content is kept exactly as `Message.to_dict()` returns it
(unset fields excluded) and replayed as stored.
# QUESTION: verify on live calls that to_dict() of a streamed final message round-trips byte for
# byte (the per-call prefix verifier in services/loop.py would flag the first mismatch).
"""

from __future__ import annotations

import os
import time
from dataclasses import dataclass, field
from typing import Any, Protocol

# Request fields passed as typed keyword arguments; everything else goes through extra_body so
# that fields newer than the installed SDK (fallbacks, context_management, cache_control, ...)
# reach the API unchanged.
CORE_FIELDS = ("model", "max_tokens", "messages")


@dataclass
class Reply:
    content: list[dict[str, Any]]
    usage: dict[str, Any]
    stop_reason: str | None
    model: str | None
    stop_details: dict[str, Any] | None = None
    raw: dict[str, Any] = field(default_factory=dict)
    latency_ms: int = 0


class Provider(Protocol):
    name: str

    def send(self, body: dict[str, Any], *, betas: list[str] = ()) -> Reply: ...

    def count_tokens(self, body: dict[str, Any], *, betas: list[str] = ()) -> int | None: ...


class AnthropicProvider:
    name = "anthropic"

    def __init__(self) -> None:
        import anthropic

        self.client = anthropic.Anthropic()

    def send(self, body: dict[str, Any], *, betas: list[str] = ()) -> Reply:
        core = {k: body[k] for k in CORE_FIELDS}
        extra = {k: v for k, v in body.items() if k not in CORE_FIELDS}
        headers = {"anthropic-beta": ",".join(betas)} if betas else None
        t0 = time.monotonic()
        with self.client.messages.stream(**core, extra_body=extra, extra_headers=headers) as stream:
            msg = stream.get_final_message()
        d = msg.to_dict()
        return Reply(d.get("content", []), d.get("usage", {}), d.get("stop_reason"), d.get("model"),
                     d.get("stop_details"), d, int(1000 * (time.monotonic() - t0)))

    def count_tokens(self, body: dict[str, Any], *, betas: list[str] = ()) -> int | None:
        keep = {k: body[k] for k in ("model", "messages") if k in body}
        extra = {k: body[k] for k in ("system", "tools", "thinking", "context_management") if k in body}
        headers = {"anthropic-beta": ",".join(betas)} if betas else None
        r = self.client.messages.count_tokens(**keep, extra_body=extra, extra_headers=headers)
        return r.input_tokens


class ScriptedProvider:
    """Replies from a list, in order. Records every request (tests)."""

    name = "scripted"

    def __init__(self, replies: list[dict[str, Any]]):
        self.replies = list(replies)
        self.requests: list[dict[str, Any]] = []
        self.betas: list[list[str]] = []

    def send(self, body: dict[str, Any], *, betas: list[str] = ()) -> Reply:
        self.requests.append(body)
        self.betas.append(list(betas))
        r = self.replies.pop(0)
        usage = r.get("usage") or {"input_tokens": 10, "output_tokens": 5, "cache_read_input_tokens": 0,
                                   "cache_creation_input_tokens": 0}
        return Reply(r["content"], usage, r.get("stop_reason", "end_turn"), body.get("model"), None, r, 1)

    def count_tokens(self, body: dict[str, Any], *, betas: list[str] = ()) -> int | None:
        return None


class EchoProvider(ScriptedProvider):
    """No API key needed: answers with a short text, and lists the workspace when asked to "ls".
    Lets the gates and the loop be tried end to end in the UI (CURATOR_PROVIDER=echo)."""

    name = "echo"

    def __init__(self) -> None:
        super().__init__([])
        self.n = 0

    def send(self, body: dict[str, Any], *, betas: list[str] = ()) -> Reply:
        self.n += 1
        last = body["messages"][-1]
        texts = [b.get("text", "") for b in last["content"] if b.get("type") == "text"] \
            if last["role"] in ("user", "system") else []
        has_results = any(b.get("type") == "tool_result" for b in last.get("content", []))
        if any("ls" in t.split() for t in texts) and not has_results:
            content = [{"type": "text", "text": "Listing the workspace."},
                       {"type": "tool_use", "id": f"toolu_echo_{self.n}", "name": "list_dir", "input": {"path": "."}}]
            stop = "tool_use"
        else:
            content = [{"type": "text", "text": f"[echo provider] {len(body['messages'])} messages received."}]
            stop = "end_turn"
        self.replies = [{"content": content, "stop_reason": stop}]
        return super().send(body, betas=betas)


def default_provider() -> Provider:
    kind = os.environ.get("CURATOR_PROVIDER", "anthropic")
    return EchoProvider() if kind == "echo" else AnthropicProvider()
