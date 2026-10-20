import { createContext, useContext } from "react";

// Charts read their colors from the CSS custom properties in styles.css, so
// light/dark mode is defined once. `ThemeContext` carries a counter that is
// bumped whenever the theme changes, to force charts to re-read them.
export const ThemeContext = createContext(0);
export const useThemeVersion = () => useContext(ThemeContext);

export function cssVar(name: string): string {
  return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
}

export function colors() {
  return {
    surface: cssVar("--surface-1"),
    text: cssVar("--text-primary"),
    text2: cssVar("--text-secondary"),
    muted: cssVar("--text-muted"),
    grid: cssVar("--grid"),
    baseline: cssVar("--baseline"),
    s1: cssVar("--series-1"),
    s2: cssVar("--series-2"),
    s3: cssVar("--series-3"),
    band: cssVar("--band"),
    good: cssVar("--good"),
    critical: cssVar("--critical"),
    seq: [0, 1, 2, 3, 4].map((i) => cssVar(`--seq-${i}`)),
    div: [cssVar("--div-neg"), cssVar("--div-mid"), cssVar("--div-pos")],
  };
}

export function seqScale(): [number, string][] {
  const s = colors().seq;
  return s.map((c, i) => [i / (s.length - 1), c]);
}

export function divScale(): [number, string][] {
  const d = colors().div;
  return [[0, d[0]], [0.5, d[1]], [1, d[2]]];
}

/** Fixed color per entity (never by rank). */
export const OBJECTIVE_COLOR: Record<string, "s1" | "s2" | "s3"> = {
  deterministic: "s1",
  mean_var: "s2",
  chance: "s3",
};
