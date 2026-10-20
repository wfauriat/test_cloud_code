import type { ReactNode } from "react";

export function Card({ title, sub, span = 12, right, children }: { title: string; sub?: ReactNode; span?: number; right?: ReactNode; children: ReactNode }) {
  return (
    <section className={`card ${span < 12 ? `span-${span}` : ""}`}>
      <div className="card-head">
        <h3>{title}</h3>
        <span className="spacer" />
        {right}
      </div>
      {sub && <p className="sub">{sub}</p>}
      {children}
    </section>
  );
}

export function Lesson({ title, children, open = false }: { title: string; children: ReactNode; open?: boolean }) {
  return (
    <details className="lesson" open={open}>
      <summary>{title}</summary>
      {children}
    </details>
  );
}

export function Tile({ label, value, note }: { label: string; value: ReactNode; note?: ReactNode }) {
  return (
    <div className="tile">
      <div className="label">{label}</div>
      <div className="value">{value}</div>
      {note && <div className="note">{note}</div>}
    </div>
  );
}

export function Status({ loading, error }: { loading?: boolean; error?: string | null }) {
  return (
    <>
      {loading && <span className="busy">computing…</span>}
      {error && <div className="error">⚠ {error}</div>}
    </>
  );
}
