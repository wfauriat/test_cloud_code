// Shared formatting and the category -> color mapping (color follows the category, never its rank).

export const CATEGORY_ORDER = [
  "tool_result", "thinking", "tool_use", "harness", "assistant_text", "user_text", "curator",
] as const;

const SLOT: Record<string, string> = {
  tool_result: "var(--s1)", thinking: "var(--s2)", tool_use: "var(--s3)", harness: "var(--s4)",
  assistant_text: "var(--s5)", user_text: "var(--s6)", curator: "var(--s7)",
};

export const LABEL: Record<string, string> = {
  tool_result: "tool results", thinking: "thinking", tool_use: "tool calls", harness: "harness text",
  assistant_text: "assistant text", user_text: "user text", curator: "curator",
};

export const catColor = (c: string) => SLOT[c] ?? "var(--s-other)";
export const fmt = (n: number) => n.toLocaleString("en-US");
export const kfmt = (n: number) => (n >= 10_000 ? `${Math.round(n / 1000)}k` : n >= 1000 ? `${(n / 1000).toFixed(1)}k` : `${n}`);
export const usd = (n: number) => `$${n.toFixed(n < 0.1 ? 3 : 2)}`;
