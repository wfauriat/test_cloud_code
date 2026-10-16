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
  brief: (sid: string) => call<BriefItemView[]>("GET", `/sessions/${sid}/brief`),
  addBrief: (sid: string, type: string, text: string) => call<BriefItemView>("POST", `/sessions/${sid}/brief`, { type, text }),
  updateBrief: (sid: string, bid: string, body: { text?: string; status?: string }) =>
    call<BriefItemView>("PATCH", `/sessions/${sid}/brief/${bid}`, body),
};
