"""Ops fold, prefix diff, costs, rules, tokens, policy."""

from factories import call, coding_session, ev, result, text

from curator.core import costs, policy, rules, tokens
from curator.core.model import Block, Op, Preamble, Span
from curator.core.ops import check_op, fold
from curator.core.prefix import diff
from curator.core.render import render

PARAMS = {"model": "claude-opus-5-5", "max_tokens": 1000}


def req(events, ops=(), thinking="keep"):
    return render(events, list(ops), preamble=Preamble(), params=PARAMS, thinking=thinking).request


# -- ops ------------------------------------------------------------------------------------
def test_later_op_wins_on_overlap_and_fully_covered_ops_are_shadowed():
    b = Block(text("0123456789"))
    ops = [Op("a", "replace", [Span("e", 0, 2, 5)], {"text": "X"}, seq=1),
           Op("b", "drop", [Span("e", 0, 1, 8)], seq=2)]
    plan = fold(ops, lambda s: b)[("e", 0)]
    assert plan.action == "rewrite" and plan.text == "089"
    assert plan.shadowed == ["a"]


def test_check_op_refuses_span_edits_on_calls_and_machine_ops_on_pins():
    blocks = {("a1", 1): Block(call("t1", "Read", file_path="a.py"), "model"),
              ("u2", 0): Block(result("t1", "body"), "tool")}
    get = lambda s: blocks.get(s.address)  # noqa: E731
    assert check_op(Op("x", "drop", [Span("a1", 1, 0, 3)]), get, set())
    assert check_op(Op("y", "replace", [Span("a1", 1)], {"text": "z"}), get, set())
    assert check_op(Op("z", "drop", [Span("u2", 0)], author="rule:R2@1"), get, {("u2", 0)})
    assert check_op(Op("w", "drop", [Span("u2", 0)]), get, {("u2", 0)}) == []  # humans may override pins


# -- prefix diff ----------------------------------------------------------------------------
def test_next_step_is_append_only_and_rewind_is_a_prefix():
    s = coding_session()
    a, b = req(s[:3]), req(s[:5])
    assert diff(a, b).verdict == "append_only"
    assert diff(b, a).verdict == "rewind" and diff(b, a).safe


def test_editing_early_content_puts_later_thinking_at_risk():
    s = coding_session()
    edited = req(s, [Op("o", "replace", [Span("u1", 0)], {"text": "Fix the bug in b.py"}, seq=1)])
    d = diff(req(s), edited)
    assert d.verdict == "diverge" and d.path_b == "messages[0].content[0]"
    assert len(d.thinking_at_risk) == 3 and not d.safe


def test_stripping_after_the_edit_trades_risk_for_lost_reasoning():
    s = coding_session()
    ops = [Op("o", "drop", [Span("u4", 0)], seq=1), Op("s", "drop", [Span("a4", 0)], author="assembler", seq=2)]
    d = diff(req(s), req(s, ops))
    assert d.thinking_at_risk == [] and len(d.thinking_lost) == 1 and d.safe


# -- costs: the spec's worked example (specs_claude.md §8.4) ---------------------------------
def test_edit_economics_matches_the_worked_example():
    warm = costs.edit_economics("claude-opus-5-5", tokens_before=300_000, tokens_after=200_000,
                                divergence_tokens=0, warm=True)
    assert round(warm.next_call_without, 2) == 0.06 and round(warm.next_call_with, 2) == 1.00
    assert round(warm.savings_per_call, 2) == 0.02 and round(warm.pays_back_after) == 47
    cold = costs.edit_economics("claude-opus-5-5", tokens_before=300_000, tokens_after=200_000,
                                divergence_tokens=0, warm=False)
    assert round(-cold.extra_now, 2) == 0.50 and cold.pays_back_after == 0


def test_usage_cost_prices_each_bucket():
    u = {"input_tokens": 1_000_000, "output_tokens": 1_000_000, "cache_read_input_tokens": 1_000_000,
         "cache_creation_input_tokens": 2_000_000,
         "cache_creation": {"ephemeral_5m_input_tokens": 1_000_000, "ephemeral_1h_input_tokens": 1_000_000}}
    assert costs.usage_cost("claude-opus-5-5", u) == 4 + 20 + 0.2 + 5 + 8


# -- rules ----------------------------------------------------------------------------------
def test_rules_find_stale_reads_reruns_and_duplicates():
    props = rules.propose(coding_session())
    found = {(p.rule, p.op.targets[0].address) for p in props}
    assert ("R2", ("u2", 0)) in found  # a.py read, then edited
    assert ("R3", ("u2", 1)) in found  # `ls` ran again later
    assert all(p.op.state == "draft" and p.op.author.startswith("rule:") for p in props)


def test_rules_skip_pinned_and_bound_oversized_output():
    big = "\n".join(f"line {i} " + "x" * 60 for i in range(400))
    s = [ev("u1", "user", text("go")), ev("a1", "assistant", call("t1", "Bash", command="cat big")),
         ev("u2", "user", result("t1", big))]
    [p] = rules.propose(s)
    assert p.rule == "R1" and p.op.verb == "replace" and "[curator: removed 370 lines" in p.op.payload["text"]
    assert rules.propose(s, pinned={("u2", 0)}) == []


# -- tokens ---------------------------------------------------------------------------------
def test_calibration_recovers_preamble_and_scale():
    pts = [(e, int(50_000 + 1.2 * e)) for e in range(1000, 200_000, 7000)]
    cal = tokens.calibrate(pts)
    assert abs(cal.preamble_tokens - 50_000) < 5 and abs(cal.scale - 1.2) < 1e-3 and cal.r2 > 0.999


# -- policy ---------------------------------------------------------------------------------
def test_policy_defaults_to_review_and_most_restrictive_wins():
    assert policy.evaluate("tool_call", "read_file").decision == "auto"
    assert policy.evaluate("tool_call", "write_file").decision == "review"
    rules_ = policy.DEFAULT_RULES + (policy.PolicyRule("deny", "tool_call", "read_file", "test"),)
    assert policy.evaluate("tool_call", "read_file", rules_).decision == "deny"
