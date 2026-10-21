import { useState, type ReactNode } from "react";

interface CardProps {
  title: string;
  sub?: ReactNode;
  span?: number;
  right?: ReactNode;
  children: ReactNode;
  collapsible?: boolean; // click the title to fold / unfold
  defaultOpen?: boolean;
}

export function Card({ title, sub, span = 12, right, children, collapsible = false, defaultOpen = true }: CardProps) {
  const [open, setOpen] = useState(defaultOpen);
  const shown = !collapsible || open;
  return (
    <section className={`card ${span < 12 ? `span-${span}` : ""} ${shown ? "" : "folded"}`}>
      <div className="card-head">
        <h3>
          {collapsible ? (
            <button className="fold" aria-expanded={open} onClick={() => setOpen(!open)}>
              <span className="caret">{open ? "▾" : "▸"}</span>{title}
            </button>
          ) : title}
        </h3>
        <span className="spacer" />
        {shown && right}
      </div>
      {sub && <p className="sub">{sub}</p>}
      {/* folded content is not rendered at all, so charts are drawn at their real size on opening */}
      {shown && children}
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
