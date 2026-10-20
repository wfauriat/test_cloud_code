import { useEffect, useRef } from "react";
import Plotly from "plotly.js-dist-min";
import { colors, useThemeVersion } from "../theme";

interface Props {
  data: any[];
  layout?: Record<string, any>;
  height?: number;
  onClick?: (ev: any) => void;
}

function deepMerge(a: any, b: any): any {
  const out: any = { ...a };
  for (const [k, v] of Object.entries(b ?? {})) {
    out[k] = v && typeof v === "object" && !Array.isArray(v) && a?.[k] && typeof a[k] === "object" ? deepMerge(a[k], v) : v;
  }
  return out;
}

export function baseLayout(): Record<string, any> {
  const c = colors();
  const axis = {
    gridcolor: c.grid, linecolor: c.baseline, zerolinecolor: c.baseline, tickcolor: c.baseline,
    tickfont: { color: c.muted, size: 11 }, title: { font: { color: c.text2, size: 12 } }, automargin: true,
  };
  return {
    paper_bgcolor: c.surface, plot_bgcolor: c.surface,
    font: { family: 'system-ui, -apple-system, "Segoe UI", sans-serif', color: c.text2, size: 12 },
    margin: { l: 56, r: 16, t: 12, b: 44 },
    xaxis: axis, yaxis: axis,
    legend: { orientation: "h", x: 0, xanchor: "left", y: 1.02, yanchor: "bottom", font: { size: 12, color: c.text2 } },
    hoverlabel: { bgcolor: c.surface, bordercolor: c.baseline, font: { color: c.text, size: 12 } },
    hovermode: "closest",
  };
}

/** Plotly chart that re-renders on data / layout / theme change. */
export function Plot({ data, layout, height = 320, onClick }: Props) {
  const ref = useRef<HTMLDivElement>(null);
  const theme = useThemeVersion();

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const base = baseLayout();
    // Axes named in `layout` (xaxis2, yaxis3...) inherit the themed axis style.
    for (const k of Object.keys(layout ?? {})) {
      if (/^[xy]axis\d+$/.test(k)) base[k] = base[k.slice(0, 5)];
    }
    Plotly.react(el, data, { ...deepMerge(base, layout), height, autosize: true },
      { responsive: true, displaylogo: false, displayModeBar: false });
  }, [data, layout, height, theme]);

  useEffect(() => {
    const el = ref.current as any;
    if (!el || !onClick) return;
    el.on?.("plotly_click", onClick);
    return () => el.removeAllListeners?.("plotly_click");
  }, [onClick]);

  useEffect(() => {
    const el = ref.current;
    return () => { if (el) Plotly.purge(el); };
  }, []);

  return <div ref={ref} style={{ width: "100%", minHeight: height }} />;
}
