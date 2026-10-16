"""Render + repair + validate. Each test is also an example of one rule (PLAN §4 steps 4-6)."""

import json

from factories import call, coding_session, ev, result, text, thinking

from curator.core.model import Op, Preamble, Request, Span
from curator.core.render import render
from curator.core.validate import validate

PARAMS = {"model": "claude-opus-5-5", "max_tokens": 1000}


def go(events, ops=(), **kw):
    res = render(events, list(ops), preamble=Preamble(), params=PARAMS, **kw)
    problems = validate(res.request, thinking_had=res.thinking_had, thinking_kept=res.thinking_kept)
    return res, problems


def op(verb, *targets, **payload):
    go.n = getattr(go, "n", 0) + 1
    return Op(f"o{go.n}", verb, list(targets), payload, rationale=payload.pop("why", ""), seq=go.n)


def test_untouched_session_renders_valid_and_byte_identical_twice():
    a, problems = go(coding_session())
    b, _ = go(coding_session())
    assert problems == []
    assert json.dumps(a.request.to_api()) == json.dumps(b.request.to_api())
    assert a.thinking_had == a.thinking_kept == [1, 3, 7]


def test_drop_tool_result_leaves_placeholder_inside_and_keeps_the_pair():
    res, problems = go(coding_session(), [op("drop", Span("u2", 0), why="stale")])
    assert problems == []
    stub = res.request.messages[2]["content"][0]
    assert stub["type"] == "tool_result" and stub["tool_use_id"] == "t1"
    assert stub["content"].startswith("[curator: removed the output of Read(a.py)") and "stale" in stub["content"]


def test_drop_tool_use_removes_its_result_and_leaves_a_note():
    res, problems = go(coding_session(), [op("drop", Span("a1", 2))])  # the Bash call
    assert problems == []
    a1 = res.request.messages[1]["content"]
    assert [b["type"] for b in a1] == ["thinking", "tool_use", "text"]
    assert [b["tool_use_id"] for b in res.request.messages[2]["content"]] == ["t1"]
    assert any(d.code == "repair.orphan_results" for d in res.diagnostics)


def test_span_replace_and_insert():
    events = [ev("u1", "user", text("keep this. DROP THIS. keep that."))]
    res, problems = go(events, [op("replace", Span("u1", 0, 11, 21), text="[cut]"),
                                op("insert", Span("u1", 0), text="note from curator")])
    assert problems == []
    assert [b["text"] for b in res.request.messages[0]["content"]] == \
        ["keep this. [cut] keep that.", "note from curator"]


def test_strip_all_thinking_for_imports():
    res, problems = go(coding_session(), thinking="strip_all")
    assert problems == []
    assert res.thinking_kept == []
    assert any(d.code == "render.thinking_stripped" for d in res.diagnostics)


def test_dropping_middle_thinking_is_a_gap():
    _, problems = go(coding_session(), [op("drop", Span("a2", 0))])
    assert [p.code for p in problems] == ["V09.thinking_gap"]


def test_dropping_thinking_from_the_back_is_fine():
    _, problems = go(coding_session(), [op("drop", Span("a4", 0)), op("drop", Span("a2", 0))])
    assert problems == []


def test_brief_is_a_system_message_after_the_last_user_message():
    res, problems = go(coding_session(), brief="Goal: fix a.py")
    assert problems == []
    assert res.request.messages[-1] == {"role": "system", "content": [{"type": "text", "text": "Goal: fix a.py"}]}


def test_misplaced_system_message_is_folded_into_the_next_user_message():
    events = [ev("u1", "user", text("hi")), ev("a1", "assistant", text("hello")),
              ev("s1", "system", text("<reminder>")), ev("u2", "user", text("next"))]
    res, problems = go(events)
    assert problems == []
    assert [b["text"] for b in res.request.messages[-1]["content"]] == ["<reminder>", "next"]


def test_interleaved_results_are_merged_and_put_first():
    events = [ev("u1", "user", text("go")),
              ev("a1", "assistant", call("t1", "Read", file_path="x"), call("t2", "Read", file_path="y")),
              ev("u2", "user", result("t1", "x")), ev("h1", "user", text("<beside>"), origin="harness"),
              ev("u3", "user", result("t2", "y"))]
    res, problems = go(events)
    assert problems == []
    assert [b["type"] for b in res.request.messages[2]["content"]] == ["tool_result", "tool_result", "text"]


def test_validator_catches_structural_errors():
    bad = Request(PARAMS, [], [], [
        {"role": "system", "content": [text("first")]},
        {"role": "user", "content": [text("go"), result("t9", "orphan")]},
        {"role": "assistant", "content": [call("t1", "Read")]},
        {"role": "user", "content": [text(" ")]},
        {"role": "assistant", "content": [text("prefill")]},
    ])
    codes = {d.code for d in validate(bad)}
    assert {"V02.first", "V04.system_after", "V07.orphan_result", "V08.results_first",
            "V07.missing_result", "V06.empty_text", "V05.prefill"} <= codes


def test_validator_checks_the_frozen_preamble():
    pre = Preamble(system=[text("You are X.")], tools=[{"name": "read_file"}])
    res = render([ev("u1", "user", text("hi"))], [], preamble=pre, params=PARAMS)
    assert validate(res.request, preamble=pre) == []
    res.request.system = [text("You are Y.")]
    assert [d.code for d in validate(res.request, preamble=pre)] == ["V10.preamble_system"]


def test_thinking_blocks_must_match_the_log():
    res, _ = go([ev("u1", "user", text("hi")), ev("a1", "assistant", thinking("s"), text("ok")),
                 ev("u2", "user", text("more"))])
    res.request.messages[1]["content"][0] = thinking("tampered")
    assert [d.code for d in validate(res.request, known_hashes=set())] == ["V11.opaque_changed"]
