# Quirks log

API and format behaviour met while building. Each entry: what we saw, where it is handled, and what it may mean for the spec revision. Code sites carry a `# QUIRK:` marker.

## Claude Code session logs (import)

1. **Parallel tool calls branch the parent tree.** With two calls in one assistant message, the log goes `call 1 → call 2 → result 2 → …` on the main path, while `result 1` hangs off `call 1` as a side branch. Walking back from the leaf loses `result 1`.
   - Handled in `importers/claude_code.py`: side entries hanging off the path (results-only user entries, and attachments under them) are kept in file order.
   - For the spec: "the transcript is a tree" holds in Claude Code too, but its branches mix two meanings: parallelism and real alternatives (rewinds).
2. **One line per content block.** An assistant message is split over several lines sharing `message.id`, with the results of parallel calls interleaved between them.
   - Handled: blocks are re-joined by message id; `repair.py` merges the results into one user message.
   - The first version of the importer split calls and produced false "cache breaks" in the timeline: a cheap check that the re-join works.
3. **Harness text is first-class.** `attachment` entries carry the text Claude Code injected (environment, reminders, skills and tool listings, token counters) and how it was rendered: `renderedRole` `system` or `user`, sometimes `renderedBesideToolResult`.
   - On a 31-call session this harness text was ~23% of the estimated tokens.
   - Some system-rendered attachments sit where a mid-conversation system message is not allowed. `repair.py` folds them into the next user message, so the imported wire is approximate there.
4. **The preamble is partly there.** A `prompt_snapshot` attachment carries the system prompt (sometimes more than once), and `deferred_tools_record` carries the definitions of deferred tools only. The full tool list is never logged. Imported preambles are marked `known: false`.
5. **The hidden preamble can be measured anyway.** Per-call `usage` gives the exact input size of every call. Fitting `reported ≈ a + b × estimated` over the calls gives `a` ≈ the size of what the log does not contain (system prompt + tools). On this planning session: a ≈ 49k tokens, b ≈ 1.17, r² = 1.000. So the `chars / 3.2` prior undercounts by ~17%.
6. **Thinking text is empty, thinking tokens are not.** Under the default display `omitted`, thinking blocks carry only a signature, so their size can't be estimated from text. Usage reports `output_tokens_details.thinking_tokens` per message, split evenly over the message's thinking blocks. On the planning session, thinking was the largest category (~32% of estimated tokens).
7. **Bash-first reading.** With Claude Code's "bash-first" steer, files are often read with `cat`/`sed` through Bash, which the stale-read rule (R2, keyed on `Read`) cannot see. R3 still catches exact re-runs.

## Curation economics

8. **Placeholders can cost more than they save.** A stub `[curator: removed … · why · how]` is ~30 tokens; stubbing a small tool output increases the prompt.
   - Rules skip proposals that save nothing.
   - For the spec: the stub convention needs a minimum size.
9. **First real number (Q4).** On this planning session, staging the 3 rule proposals (~19k tokens/call) gave: warm cache, costs $0.56 more on the next call and pays back after ~125 calls; cold cache, saves $0.11 right away. This matches the critique's point that pruning a warm cache rarely pays in dollars.
