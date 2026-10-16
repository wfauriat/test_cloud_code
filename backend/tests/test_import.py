"""Claude Code import on a synthetic log that reproduces the format's quirks (docs/quirks.md)."""

from factories import claude_code_jsonl

from curator.adapters.importers import claude_code
from curator.adapters.store import Store
from curator.core.validate import validate
from curator.services import sessions as S
from curator.services import staging


def test_parse_rejoins_parallel_calls_and_keeps_side_branch_results():
    parsed = claude_code.parse(claude_code_jsonl())
    asst = [e for e in parsed.events if e.role == "assistant"]
    assert [b.type for b in asst[0].blocks] == ["thinking", "tool_use", "tool_use"]
    results = [b.raw["tool_use_id"] for e in parsed.events if e.role == "user" for b in e.blocks
               if b.type == "tool_result"]
    assert results == ["t1", "t2", "t3"]
    assert parsed.stats["side_entries"] == 1
    assert parsed.stats["attachments_unrendered"] == 1
    assert parsed.preamble.known is False and [b["text"] for b in parsed.preamble.system] == \
        ["You are a coding agent.", "Be brief."]


def test_imported_session_renders_valid_and_has_a_usage_timeline(tmp_path):
    path = tmp_path / "s.jsonl"
    path.write_text("\n".join(claude_code_jsonl()))
    store = Store(":memory:")
    sid = S.import_claude_code(store, path)
    view = S.load(store, sid)
    res = S.render_view(view)
    assert validate(res.request, thinking_had=res.thinking_had, thinking_kept=res.thinking_kept) == []
    assert res.thinking_kept == []  # PLAN D12: imports never replay thinking
    assert [m["role"] for m in res.request.messages] == ["user", "system", "assistant", "user", "assistant", "user"]
    rows = S.usage_timeline(view)
    assert len(rows) == 3 and not any(r["cache_break"] for r in rows)
    kinds = [o["kind"] for o in store.observations(sid)]
    assert kinds == ["import", "rules"]


def test_cache_break_is_detected(tmp_path):
    path = tmp_path / "s.jsonl"
    path.write_text("\n".join(claude_code_jsonl(cache_break=True)))
    store = Store(":memory:")
    view = S.load(store, S.import_claude_code(store, path))
    rows = S.usage_timeline(view)
    assert rows[1]["cache_break"] and rows[1]["lost"] == 4000


def test_staged_rule_proposals_preview_with_economics(tmp_path):
    path = tmp_path / "s.jsonl"
    path.write_text("\n".join(claude_code_jsonl()))
    store = Store(":memory:")
    sid = S.import_claude_code(store, path)
    view = S.load(store, sid)
    [p] = [p for p in S.proposals(view) if p.rule == "R2"]
    staging.create_op(store, sid, verb=p.op.verb, targets=[t.to_dict() for t in p.op.targets],
                      author=p.op.author, rationale=p.rationale)
    out = staging.preview(S.load(store, sid))
    assert out["diff"]["verdict"] == "diverge" and out["validation_staged"] == []
    assert out["economics"]["tokens_after"] < out["economics"]["tokens_before"]
