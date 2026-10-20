import { useEffect, useState } from "react";
import { getMeta, type Meta, type Spec } from "./api";
import { ParamPanel, type Settings } from "./components/ParamPanel";
import { ThemeContext } from "./theme";
import { SimulatorTab } from "./tabs/SimulatorTab";
import { PropagationTab } from "./tabs/PropagationTab";
import { DoeTab, type Design } from "./tabs/DoeTab";
import { SurrogateTab, type TrainedModel } from "./tabs/SurrogateTab";
import { SensitivityTab } from "./tabs/SensitivityTab";
import { RobustTab } from "./tabs/RobustTab";

export interface Common {
  meta: Meta;
  spec: Spec;
  setSpec: (s: Spec) => void;
  settings: Settings;
}

const TABS = [
  ["sim", "Simulator"],
  ["mc", "Uncertainty propagation"],
  ["doe", "Design of experiments"],
  ["sur", "Surrogate model"],
  ["sa", "Sensitivity analysis"],
  ["rob", "Robust design"],
] as const;
type TabId = (typeof TABS)[number][0];

type ThemeMode = "auto" | "light" | "dark";

export default function App() {
  const [meta, setMeta] = useState<Meta | null>(null);
  const [err, setErr] = useState<string | null>(null);
  const [spec, setSpec] = useState<Spec | null>(null);
  const [settings, setSettings] = useState<Settings>({ qoi: "range", target: 55, tol: 3, dt: 0.01 });
  const [tab, setTabState] = useState<TabId>(() => {
    const t = new URLSearchParams(window.location.search).get("tab");
    return (TABS.some(([id]) => id === t) ? t : "sim") as TabId;
  });
  const setTab = (t: TabId) => {
    setTabState(t);
    window.history.replaceState(null, "", `?tab=${t}`);
  };
  const [design, setDesign] = useState<Design | null>(null);
  const [model, setModel] = useState<TrainedModel | null>(null);
  const [themeMode, setThemeMode] = useState<ThemeMode>(() => {
    try { return (localStorage.getItem("uq-theme") as ThemeMode) || "auto"; } catch { return "auto"; }
  });
  const [themeVersion, setThemeVersion] = useState(0);

  useEffect(() => {
    getMeta().then((m) => { setMeta(m); setSpec(structuredClone(m.default_spec)); })
      .catch((e) => setErr(`Cannot reach the Python backend: ${e.message}. Start it with "uvicorn api.main:app" in uq_demo/.`));
  }, []);

  useEffect(() => {
    const root = document.documentElement;
    if (themeMode === "auto") root.removeAttribute("data-theme");
    else root.setAttribute("data-theme", themeMode);
    try { localStorage.setItem("uq-theme", themeMode); } catch { /* storage unavailable */ }
    setThemeVersion((v) => v + 1);
    const mq = window.matchMedia("(prefers-color-scheme: dark)");
    const onChange = () => setThemeVersion((v) => v + 1);
    mq.addEventListener("change", onChange);
    return () => mq.removeEventListener("change", onChange);
  }, [themeMode]);

  if (err) return <div style={{ padding: 30 }} className="error">{err}</div>;
  if (!meta || !spec) return <div style={{ padding: 30 }} className="muted">Loading…</div>;

  const common: Common = { meta, spec, setSpec, settings };

  return (
    <ThemeContext.Provider value={themeVersion}>
      <div className="app">
        <header className="topbar">
          <div className="brand">Ballistic UQ Lab<small>uncertainty quantification, hands-on</small></div>
          <nav className="tabs">
            {TABS.map(([id, label], i) => (
              <button key={id} className={`tab ${tab === id ? "active" : ""}`} onClick={() => setTab(id)}>
                <span className="num">{i + 1}</span>{label}
              </button>
            ))}
          </nav>
          <select className="inline theme-toggle" value={themeMode} aria-label="Theme"
            onChange={(e) => setThemeMode(e.target.value as ThemeMode)}>
            <option value="auto">Theme: auto</option>
            <option value="light">Theme: light</option>
            <option value="dark">Theme: dark</option>
          </select>
        </header>
        <div className="body">
          <ParamPanel meta={meta} spec={spec} setSpec={setSpec} settings={settings} setSettings={setSettings}
            showUncertainty={tab !== "sim"} />
          <main className="main">
            {tab === "sim" && <SimulatorTab {...common} />}
            {tab === "mc" && <PropagationTab {...common} />}
            {tab === "doe" && <DoeTab {...common} design={design} setDesign={setDesign}
              onUse={() => setTab("sur")} />}
            {tab === "sur" && <SurrogateTab {...common} design={design} model={model} setModel={setModel}
              onUse={() => setTab("sa")} goDoe={() => setTab("doe")} />}
            {tab === "sa" && <SensitivityTab {...common} model={model} />}
            {tab === "rob" && <RobustTab {...common} />}
          </main>
        </div>
      </div>
    </ThemeContext.Provider>
  );
}
