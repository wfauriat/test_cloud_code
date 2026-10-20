"""Ballistic model: point mass with drag, lift and horizontal wind.

State (x, y, vx, vy). With k = 0.5 * rho * S and relative velocity u = v - w
(w = horizontal wind, positive = tailwind):

    a = -g * y_hat - (k * Cd / m) * |u| * u + (k * Cl / m) * |u| * perp(u)

where perp(u) = (-u_y, u_x) is u rotated by +90 deg, so a positive Cl
(backspin) lifts the projectile while it travels forward.

All functions are vectorised: every input may be a scalar or an array of
shape (N,), and N trajectories are advanced together in one numpy loop.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

G = 9.81  # gravity [m/s^2]
RHO = 1.225  # air density [kg/m^3]
DIAMETER = 0.22  # ball diameter [m] (football-sized)
AREA = np.pi * DIAMETER**2 / 4  # reference area [m^2]
K_AERO = 0.5 * RHO * AREA

T_MAX = 60.0  # safety cap on flight time [s]


@dataclass
class SimResult:
    range: np.ndarray  # horizontal distance at impact [m]
    max_height: np.ndarray  # apex height [m]
    flight_time: np.ndarray  # time of flight [s]
    impact_speed: np.ndarray  # ground speed at impact [m/s]
    landed: np.ndarray  # False if the projectile did not land before T_MAX
    trajectories: list[np.ndarray] | None = None  # list of (n_pts, 2) arrays

    def qoi(self, name: str) -> np.ndarray:
        return {
            "range": self.range,
            "max_height": self.max_height,
            "flight_time": self.flight_time,
            "impact_speed": self.impact_speed,
        }[name]


def _acceleration(vx, vy, cd, cl, mass, wind):
    ux = vx - wind
    uy = vy
    speed = np.sqrt(ux * ux + uy * uy)
    kd = K_AERO * cd / mass * speed
    kl = K_AERO * cl / mass * speed
    ax = -kd * ux - kl * uy
    ay = -G - kd * uy + kl * ux
    return ax, ay


def simulate(
    v0,
    theta_deg,
    cd=0.0,
    cl=0.0,
    mass=1.0,
    wind=0.0,
    dt=0.01,
    scheme: str = "euler",
    record: int = 0,
    max_points: int = 200,
) -> SimResult:
    """Integrate N trajectories until each one hits the ground (y = 0).

    `dt` may itself be an array (one step size per trajectory), which is how
    the dt-convergence study is vectorised. `record` is the number of
    trajectories (the first ones) whose path is stored, downsampled to at
    most `max_points` points.
    """
    v0, theta, cd, cl, mass, wind, dt = np.broadcast_arrays(
        *(np.atleast_1d(np.asarray(a, dtype=float)) for a in (v0, theta_deg, cd, cl, mass, wind, dt))
    )
    n = v0.shape[0]
    th = np.radians(theta)
    x = np.zeros(n)
    y = np.zeros(n)
    vx = v0 * np.cos(th)
    vy = v0 * np.sin(th)
    t = np.zeros(n)

    active = np.ones(n, dtype=bool)
    rng_out = np.full(n, np.nan)
    tof = np.full(n, np.nan)
    v_imp = np.full(n, np.nan)
    ymax = np.zeros(n)

    record = min(record, n)
    hist_x = [x[:record].copy()]
    hist_y = [y[:record].copy()]
    nsteps = np.zeros(n, dtype=int)  # number of in-flight steps per trajectory

    max_steps = int(np.ceil(T_MAX / dt.min()))
    for _ in range(max_steps):
        if scheme == "rk4":
            def f(s):
                ax_, ay_ = _acceleration(s[2], s[3], cd, cl, mass, wind)
                return np.array([s[2], s[3], ax_, ay_])
            s = np.array([x, y, vx, vy])
            k1 = f(s)
            k2 = f(s + 0.5 * dt * k1)
            k3 = f(s + 0.5 * dt * k2)
            k4 = f(s + dt * k3)
            xn, yn, vxn, vyn = s + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        else:  # explicit Euler
            ax, ay = _acceleration(vx, vy, cd, cl, mass, wind)
            xn = x + dt * vx
            yn = y + dt * vy
            vxn = vx + dt * ax
            vyn = vy + dt * ay

        # Trajectories crossing the ground during this step: interpolate linearly.
        hit = active & (yn < 0.0)
        if hit.any():
            frac = y[hit] / (y[hit] - yn[hit])
            rng_out[hit] = x[hit] + frac * (xn[hit] - x[hit])
            tof[hit] = t[hit] + frac * dt[hit]
            vxi = vx[hit] + frac * (vxn[hit] - vx[hit])
            vyi = vy[hit] + frac * (vyn[hit] - vy[hit])
            v_imp[hit] = np.hypot(vxi, vyi)
            active &= ~hit

        x = np.where(active, xn, x)
        y = np.where(active, yn, y)
        vx = np.where(active, vxn, vx)
        vy = np.where(active, vyn, vy)
        t = np.where(active, t + dt, t)
        ymax = np.maximum(ymax, np.where(active, y, 0.0))
        nsteps += active
        if record:
            hist_x.append(x[:record].copy())
            hist_y.append(y[:record].copy())
        if not active.any():
            break

    landed = ~active
    # Projectiles still flying at T_MAX: report their current position.
    rng_out = np.where(landed, rng_out, x)
    tof = np.where(landed, tof, t)
    v_imp = np.where(landed, v_imp, np.hypot(vx, vy))

    trajectories = None
    if record:
        hx, hy = np.array(hist_x), np.array(hist_y)
        trajectories = []
        for i in range(record):
            k = nsteps[i] + 1
            arr = np.column_stack([hx[:k, i], hy[:k, i]])
            if landed[i]:
                arr = np.vstack([arr, [rng_out[i], 0.0]])
            if len(arr) > max_points:
                idx = np.unique(np.r_[np.linspace(0, len(arr) - 1, max_points).astype(int), len(arr) - 1])
                arr = arr[idx]
            trajectories.append(arr)

    return SimResult(rng_out, ymax, tof, v_imp, landed, trajectories)


def vacuum_trajectory(v0: float, theta_deg: float, n_points: int = 100) -> dict:
    """Closed-form drag-free parabola (the reference solution)."""
    th = np.radians(theta_deg)
    vx, vy = v0 * np.cos(th), v0 * np.sin(th)
    tof = 2 * vy / G
    t = np.linspace(0, tof, n_points)
    return {
        "x": (vx * t).tolist(),
        "y": (vy * t - 0.5 * G * t**2).tolist(),
        "range": float(v0**2 * np.sin(2 * th) / G),
        "max_height": float(vy**2 / (2 * G)),
        "flight_time": float(tof),
    }
