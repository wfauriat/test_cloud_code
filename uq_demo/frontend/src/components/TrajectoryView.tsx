import { useEffect, useRef, useState } from "react";
import * as d3 from "d3";
import { colors, useThemeVersion } from "../theme";

export interface Path {
  x: number[];
  y: number[];
}

interface Props {
  main?: Path | null; // highlighted trajectory (with hover read-out)
  vacuum?: Path | null; // drag-free parabola
  ghosts?: Path[]; // pinned earlier trajectories
  spaghetti?: (Path & { value: number })[]; // Monte Carlo sample paths, colored by `value`
  valueLabel?: string;
  impacts?: number[]; // impact positions (rug on the ground)
  band?: [number, number] | null; // target band on the ground
  wind?: number;
  height?: number;
  equalAspect?: boolean;
  animateKey?: number; // change it to replay the drawing animation of `main`
}

const M = { top: 18, right: 18, bottom: 34, left: 46 };

/** D3 view of trajectories in the (x, y) plane. */
export function TrajectoryView(props: Props) {
  const { main, vacuum, ghosts = [], spaghetti = [], impacts = [], band, wind = 0, height = 340,
    equalAspect = false, animateKey = 0, valueLabel = "" } = props;
  const wrap = useRef<HTMLDivElement>(null);
  const svgRef = useRef<SVGSVGElement>(null);
  const [width, setWidth] = useState(700);
  const [tip, setTip] = useState<{ left: number; top: number; text: string } | null>(null);
  const theme = useThemeVersion();
  const lastAnim = useRef(animateKey);

  useEffect(() => {
    const el = wrap.current;
    if (!el) return;
    const ro = new ResizeObserver(([e]) => setWidth(Math.max(280, e.contentRect.width)));
    ro.observe(el);
    return () => ro.disconnect();
  }, []);

  useEffect(() => {
    const svg = d3.select(svgRef.current!);
    svg.selectAll("*").remove();
    const c = colors();
    const W = width - M.left - M.right;
    const H = height - M.top - M.bottom;

    const all: Path[] = [...(main ? [main] : []), ...(vacuum ? [vacuum] : []), ...ghosts, ...spaghetti];
    let xMax = d3.max(all, (p) => d3.max(p.x)) ?? 10;
    let yMax = d3.max(all, (p) => d3.max(p.y)) ?? 5;
    if (band) xMax = Math.max(xMax, band[1]);
    xMax = Math.max(xMax * 1.05, 1);
    yMax = Math.max(yMax * 1.15, 1);
    if (equalAspect) {
      const k = Math.max(xMax / W, yMax / H); // metres per pixel, same on both axes
      xMax = k * W;
      yMax = k * H;
    }
    const x = d3.scaleLinear().domain([0, xMax]).range([0, W]);
    const y = d3.scaleLinear().domain([0, yMax]).range([H, 0]);
    if (!equalAspect) { x.nice(); y.nice(); }

    const g = svg.append("g").attr("transform", `translate(${M.left},${M.top})`);
    g.append("g").attr("class", "gridline").attr("transform", `translate(0,${H})`)
      .call(d3.axisBottom(x).ticks(8).tickSize(-H).tickFormat(() => ""));
    g.append("g").attr("class", "gridline").call(d3.axisLeft(y).ticks(5).tickSize(-W).tickFormat(() => ""));
    g.append("g").attr("class", "axis").attr("transform", `translate(0,${H})`).call(d3.axisBottom(x).ticks(8));
    g.append("g").attr("class", "axis").call(d3.axisLeft(y).ticks(5));
    g.append("text").attr("class", "label").attr("x", W).attr("y", H + 30).attr("text-anchor", "end").text("distance x [m]");
    g.append("text").attr("class", "label").attr("x", -2).attr("y", -6).text("height y [m]");

    if (band) {
      const [b0, b1] = band;
      g.append("rect").attr("class", "band").attr("x", x(b0)).attr("width", Math.max(1, x(b1) - x(b0)))
        .attr("y", 0).attr("height", H);
      g.append("text").attr("class", "band-label").attr("x", (x(b0) + x(b1)) / 2).attr("y", 12)
        .attr("text-anchor", "middle").text("target ± tol");
    }

    const line = d3.line<[number, number]>().x((d) => x(d[0])).y((d) => y(d[1]));
    const pts = (p: Path) => p.x.map((v, i) => [v, p.y[i]] as [number, number]);

    if (spaghetti.length) {
      const vals = spaghetti.map((s) => s.value);
      const [lo, hi] = d3.extent(vals) as [number, number];
      const color = d3.scaleSequential(d3.interpolateRgbBasis(c.seq.slice(1))).domain([lo, hi === lo ? lo + 1 : hi]);
      const alpha = spaghetti.length > 150 ? 0.35 : 0.6;
      g.append("g").selectAll("path").data(spaghetti).join("path").attr("class", "spag")
        .attr("d", (p) => line(pts(p))).attr("stroke", (p) => color(p.value)).attr("opacity", alpha);
      // gradient legend
      const lg = svg.append("g").attr("transform", `translate(${M.left + 14},${M.top + 4})`);
      const gid = `grad-${Math.random().toString(36).slice(2)}`;
      const grad = svg.append("defs").append("linearGradient").attr("id", gid);
      d3.range(0, 1.01, 0.25).forEach((t) =>
        grad.append("stop").attr("offset", `${t * 100}%`).attr("stop-color", color(lo + t * (hi - lo))));
      lg.append("rect").attr("width", 150).attr("height", 8).attr("rx", 2).attr("fill", `url(#${gid})`);
      lg.append("text").attr("class", "label").attr("y", 20).text(d3.format(".3~s")(lo));
      lg.append("text").attr("class", "label").attr("x", 150).attr("y", 20).attr("text-anchor", "end").text(d3.format(".3~s")(hi));
      lg.append("text").attr("class", "label").attr("x", 75).attr("y", 20).attr("text-anchor", "middle").text(valueLabel);
    }

    if (impacts.length) {
      g.append("g").selectAll("rect").data(impacts.slice(0, 3000)).join("rect").attr("class", "impact")
        .attr("x", (d) => x(d) - 0.5).attr("y", H - 7).attr("width", 1).attr("height", 7);
    }

    ghosts.forEach((p) => g.append("path").attr("class", "ghost").attr("d", line(pts(p))));
    if (vacuum) g.append("path").attr("class", "vacuum").attr("d", line(pts(vacuum)));

    g.append("line").attr("class", "ground").attr("x1", 0).attr("x2", W).attr("y1", H).attr("y2", H);

    if (main && main.x.length > 1) {
      const path = g.append("path").attr("class", "main").attr("d", line(pts(main)));
      if (animateKey !== lastAnim.current) {
        lastAnim.current = animateKey;
        const L = (path.node() as SVGPathElement).getTotalLength();
        path.attr("stroke-dasharray", `${L} ${L}`).attr("stroke-dashoffset", L)
          .transition().duration(1100).ease(d3.easeQuadOut).attr("stroke-dashoffset", 0)
          .on("end", () => path.attr("stroke-dasharray", null));
      }
      const iApex = d3.maxIndex(main.y);
      g.append("circle").attr("class", "apex").attr("r", 4).attr("cx", x(main.x[iApex])).attr("cy", y(main.y[iApex]));

      // hover read-out along the main trajectory
      const cross = g.append("g").style("display", "none");
      cross.append("line").attr("class", "cross").attr("y1", 0).attr("y2", H);
      cross.append("circle").attr("r", 5).attr("fill", c.s1).attr("stroke", c.surface).attr("stroke-width", 2);
      const bis = d3.bisector((d: number) => d).center;
      g.append("rect").attr("width", W).attr("height", H).attr("fill", "transparent")
        .on("mousemove", (ev) => {
          const [mx] = d3.pointer(ev);
          const i = bis(main.x, x.invert(mx));
          const px = x(main.x[i]);
          const py = y(main.y[i]);
          cross.style("display", null);
          cross.select("line").attr("x1", px).attr("x2", px);
          cross.select("circle").attr("cx", px).attr("cy", py);
          setTip({ left: px + M.left + 12, top: py + M.top - 10, text: `x = ${main.x[i].toFixed(1)} m, y = ${main.y[i].toFixed(1)} m` });
        })
        .on("mouseleave", () => { cross.style("display", "none"); setTip(null); });
    }

    if (Math.abs(wind) > 0.05) {
      // wind arrow, length proportional to speed
      const len = Math.min(90, 8 + Math.abs(wind) * 5);
      const dir = Math.sign(wind);
      const x0 = 14 + (dir < 0 ? len : 0);
      const wg = g.append("g").attr("transform", `translate(${x0},${spaghetti.length ? 58 : 24})`);
      wg.append("line").attr("class", "wind").attr("x1", 0).attr("x2", dir * len).attr("y1", 0).attr("y2", 0);
      wg.append("path").attr("class", "wind-head")
        .attr("d", `M${dir * len},0 l${-dir * 8},-5 l0,10 z`);
      wg.append("text").attr("class", "wind-label").attr("x", dir * len / 2).attr("y", -8).attr("text-anchor", "middle")
        .text(`wind ${wind > 0 ? "+" : ""}${wind.toFixed(1)} m/s`);
    }
  }, [main, vacuum, ghosts, spaghetti, impacts, band, wind, width, height, equalAspect, animateKey, theme, valueLabel]);

  return (
    <div ref={wrap} style={{ position: "relative" }}>
      <svg ref={svgRef} className="traj" width={width} height={height} role="img" aria-label="Trajectory plot" />
      {tip && <div className="traj-tip" style={{ left: tip.left, top: tip.top }}>{tip.text}</div>}
    </div>
  );
}
