// Thin typed client. Types come from the backend's OpenAPI schema (npm run gen:api), so the
// backend's pydantic models are the single definition (PLAN §2).
import type { components } from "./schema";

type S = components["schemas"];
export type SessionSummary = S["SessionSummary"];
export type SessionDetail = S["SessionDetail"];
export type MessageView = S["MessageView"];
export type BlockView = S["BlockView"];
export type BlockDetail = S["BlockDetail"];
export type TimelineRow = S["TimelineRow"];
export type ProposalView = S["ProposalView"];
export type OpView = S["OpView"];
export type BriefItemView = S["BriefItemView"];
export type RenderedRequest = S["RenderedRequest"];
export type CallSummary = S["CallSummary"];
export type Span = { event_id: string; index: number; start?: number | null; end?: number | null };

// QUESTION: hand-typed because /preview returns a plain dict (dataclasses.asdict of PrefixDiff
// and EditEconomics). Promote to pydantic models if it stabilises.
export interface Diag { code: string; message: string; where: string }
export interface Preview {
  diff: {
    verdict: string; divergence: number | null; path_a: string | null; path_b: string | null;
    common_tokens: number; a_after_tokens: number; b_after_tokens: number;
    thinking_at_risk: string[]; thinking_lost: string[]; summary: string; safe: boolean;
  };
  economics: {
    tokens_before: number; tokens_after: number; next_call_without: number; next_call_with: number;
    extra_now: number; savings_per_call: number; pays_back_after: number | null;
    thinking_blocks_lost: number; summary: string;
  };
  calibrated: boolean;
  validation_base: Diag[];
  validation_staged: Diag[];
  diagnostics: Diag[];
  messages_base: number;
  messages_staged: number;
}

// QUESTION: hand-typed; the live view is a plain dict built in services/loop.py.
export interface ToolCard {
  id: string; name: string; input: Record<string, unknown>; policy: string; reason: string;
  input_error: string | null; effects: Record<string, unknown>;
}
export interface LiveView {
  state: string; epoch: number; frontier_seq: number; auto_continue: boolean; rebuild_pending: boolean;
  note: string | null; staged_ops: number; calls: number; model: string; workspace: string; tool_cards: ToolCard[];
  pending: null | {
    hash: string; tokens_est: number; tokens_exact: number | null; verdict: string; summary: string; new_blocks: number;
    validation: Diag[]; diagnostics: Diag[]; cost: { read_cost: number; write_cost: number; total: number };
    warm: boolean; cache_expires_in: number | null; free_ops: string[]; rebuild_pending: boolean;
  };
}

export interface ABPreview {
  arms: { arm: string; messages: number; tokens_est: number; tokens_exact: number | null; shared_with_first: number;
    validation: Diag[]; cost_est: number; betas: string[] }[];
  total_cost_est: number; brief: boolean;
}
export interface ABRun {
  id: string; total_cost: number;
  arms: { arm: string; error?: string; stop_reason?: string; model?: string; usage?: Record<string, unknown>; cost?: number;
    text?: string; tool_calls?: { name: string; input: unknown }[]; thinking_summary?: string; applied_edits?: unknown }[];
}
export interface RunRecord { id: string; created_at: string; spec: unknown; result: Omit<ABRun, "id"> | null; verdict: Record<string, unknown> | null }

async function call<T>(method: string, path: string, body?: unknown): Promise<T> {
  const res = await fetch(`/api${path}`, {
    method,
    headers: body === undefined ? undefined : { "content-type": "application/json" },
    body: body === undefined ? undefined : JSON.stringify(body),
  });
  if (!res.ok) {
    let detail = res.statusText;
    try { detail = (await res.json()).detail ?? detail; } catch { /* not json */ }
    throw new Error(`${res.status}: ${detail}`);
  }
  return res.json() as Promise<T>;
}

const q = (params: Record<string, string | number | boolean | undefined | null>) => {
  const s = new URLSearchParams();
  for (const [k, v] of Object.entries(params)) if (v !== undefined && v !== null) s.set(k, String(v));
  const out = s.toString();
  return out ? `?${out}` : "";
};

export const api = {
  sessions: () => call<SessionSummary[]>("GET", "/sessions"),
  importSession: (path: string) => call<SessionSummary>("POST", "/sessions/import", { path }),
  session: (sid: string) => call<SessionDetail>("GET", `/sessions/${sid}`),
  messages: (sid: string) => call<MessageView[]>("GET", `/sessions/${sid}/messages`),
  block: (sid: string, eid: string, idx: number) => call<BlockDetail>("GET", `/sessions/${sid}/blocks/${eid}/${idx}`),
  timeline: (sid: string) => call<TimelineRow[]>("GET", `/sessions/${sid}/timeline`),
  proposals: (sid: string) => call<ProposalView[]>("GET", `/sessions/${sid}/proposals`),
  stageProposals: (sid: string, ids: string[] | null) =>
    call<OpView[]>("POST", `/sessions/${sid}/proposals/stage`, { ids }),
  ops: (sid: string) => call<OpView[]>("GET", `/sessions/${sid}/ops`),
  createOp: (sid: string, body: { verb: string; targets: Span[]; payload?: Record<string, unknown>; rationale?: string }) =>
    call<OpView>("POST", `/sessions/${sid}/ops`, body),
  opAction: (sid: string, opId: string, action: "revoke" | "stage" | "unstage") =>
    call<OpView>("POST", `/sessions/${sid}/ops/${opId}/${action}`),
  preview: (sid: string, p: { warm: boolean; ttl: string; call?: number | null; brief?: boolean }) =>
    call<Preview>("GET", `/sessions/${sid}/preview${q(p)}`),
  request: (sid: string, p: { call?: number | null; staged?: boolean; brief?: boolean }) =>
    call<RenderedRequest>("GET", `/sessions/${sid}/request${q(p)}`),
  createLive: (body: Record<string, unknown>) => call<SessionSummary>("POST", "/live", body),
  live: (sid: string) => call<LiveView>("GET", `/sessions/${sid}/live`),
  liveMessage: (sid: string, text: string) => call<LiveView>("POST", `/sessions/${sid}/live/message`, { text }),
  liveApprove: (sid: string, hash: string) => call<LiveView>("POST", `/sessions/${sid}/live/approve`, { hash }),
  liveReject: (sid: string, reason: string) => call<LiveView>("POST", `/sessions/${sid}/live/reject`, { reason }),
  liveTools: (sid: string, decisions: Record<string, Record<string, unknown>>) =>
    call<LiveView>("POST", `/sessions/${sid}/live/tools`, { decisions }),
  liveReset: (sid: string) => call<LiveView>("POST", `/sessions/${sid}/live/reset`),
  liveApply: (sid: string) => call<LiveView>("POST", `/sessions/${sid}/live/apply-edits`),
  liveSettings: (sid: string, auto_continue: boolean) => call<LiveView>("POST", `/sessions/${sid}/live/settings`, { auto_continue }),
  callDetail: (sid: string, cid: string) =>
    call<{ id: string; n: number; request: Record<string, unknown>; response: Record<string, unknown> | null; error: string | null }>(
      "GET", `/sessions/${sid}/calls/${cid}`),
  pendingRequest: (sid: string) =>
    call<{ hash: string; request: Record<string, unknown>; validation: Diag[] }>("GET", `/sessions/${sid}/live/pending-request`),
  exportUrl: (sid: string) => `/api/sessions/${sid}/export.jsonl`,
  calls: (sid: string) => call<CallSummary[]>("GET", `/sessions/${sid}/calls`),
  abPreview: (sid: string, spec: Record<string, unknown>) => call<ABPreview>("POST", `/sessions/${sid}/ab/preview`, spec),
  abRun: (sid: string, spec: Record<string, unknown>) => call<ABRun>("POST", `/sessions/${sid}/ab/run`, spec),
  abRuns: (sid: string) => call<RunRecord[]>("GET", `/sessions/${sid}/ab/runs`),
  abVerdict: (sid: string, rid: string, v: { preferred: string; notes: string }) =>
    call<{ ok: boolean }>("POST", `/sessions/${sid}/ab/runs/${rid}/verdict`, v),
  summarize: (sid: string, targets: Span[]) =>
    call<{ draft: string; call: string; model: string; cost: number }>("POST", `/sessions/${sid}/summarize`, { targets }),
  acceptSummary: (sid: string, targets: Span[], text: string, call_id: string) =>
    call<OpView[]>("POST", `/sessions/${sid}/summarize/accept`, { targets, text, call_id }),
  brief: (sid: string) => call<BriefItemView[]>("GET", `/sessions/${sid}/brief`),
  addBrief: (sid: string, type: string, text: string) => call<BriefItemView>("POST", `/sessions/${sid}/brief`, { type, text }),
  updateBrief: (sid: string, bid: string, body: { text?: string; status?: string }) =>
    call<BriefItemView>("PATCH", `/sessions/${sid}/brief/${bid}`, body),
};
