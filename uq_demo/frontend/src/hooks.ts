import { useCallback, useEffect, useRef, useState } from "react";
import { post } from "./api";

/** Run an API call; tracks loading / error state and cancels stale requests. */
export function useApi<T>() {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const ctrl = useRef<AbortController | null>(null);

  const run = useCallback(async (path: string, body: unknown): Promise<T | null> => {
    ctrl.current?.abort();
    const c = new AbortController();
    ctrl.current = c;
    setLoading(true);
    setError(null);
    try {
      const out = await post<T>(path, body, c.signal);
      if (!c.signal.aborted) setData(out);
      return out;
    } catch (e: any) {
      if (e?.name !== "AbortError") setError(String(e?.message ?? e));
      return null;
    } finally {
      if (ctrl.current === c) setLoading(false);
    }
  }, []);

  return { data, error, loading, run, setData };
}

/** Value that only updates after `delay` ms without change. */
export function useDebounced<T>(value: T, delay: number): T {
  const [v, setV] = useState(value);
  useEffect(() => {
    const id = setTimeout(() => setV(value), delay);
    return () => clearTimeout(id);
  }, [value, delay]);
  return v;
}
