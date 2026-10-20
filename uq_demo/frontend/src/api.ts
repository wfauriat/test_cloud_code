// Thin typed client for the FastAPI backend (see uq_demo/api/main.py).

export type Dist = "normal" | "uniform" | "lognormal";
export type Qoi = "range" | "max_height" | "flight_time" | "impact_speed";

export interface ParamEntry {
  value: number;
  std: number;
  dist: Dist;
  uncertain: boolean;
}
export type Spec = Record<string, ParamEntry>;

export interface ParamInfo {
  name: string;
  label: string;
  unit: string;
  lo: number;
  hi: number;
  value: number;
  std: number;
  uncertain: boolean;
  step: number;
}

export interface Meta {
  params: ParamInfo[];
  qois: Record<Qoi, { label: string; unit: string }>;
  dists: Dist[];
  doe_methods: string[];
  surrogates: Record<string, string>;
  objectives: Record<string, string>;
  calibratable: string[];
  default_spec: Spec;
}

export interface Curve {
  x: number[];
  y: number[];
}

export class ApiError extends Error {}

export async function post<T = any>(path: string, body: unknown, signal?: AbortSignal): Promise<T> {
  const res = await fetch(`/api/${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
    signal,
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    const detail = Array.isArray(data.detail)
      ? data.detail.map((d: any) => `${(d.loc || []).join(".")}: ${d.msg}`).join("; ")
      : data.detail;
    throw new ApiError(detail || `HTTP ${res.status}`);
  }
  return data as T;
}

export async function getMeta(): Promise<Meta> {
  const res = await fetch("/api/meta");
  if (!res.ok) throw new ApiError(`backend not reachable (HTTP ${res.status})`);
  return res.json();
}

export function uncertainNames(spec: Spec, meta: Meta): string[] {
  return meta.params.map((p) => p.name).filter((n) => spec[n].uncertain && spec[n].std > 0);
}

export const fmt = (v: number | null | undefined, digits = 2): string =>
  v === null || v === undefined || !isFinite(v) ? "–" : v.toFixed(digits);

export const pct = (v: number | null | undefined, digits = 1): string =>
  v === null || v === undefined || !isFinite(v) ? "–" : `${(100 * v).toFixed(digits)}%`;
