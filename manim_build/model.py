"""Physical model shared by every scene (no Manim imports here, so it can be tested alone).

Geometry (one vertical slice through the object, beam along +x):
  * Object = N concentric circular shells, radii r_k = k R / N (regular division).
  * Screen = N pixels; pixel j sits at height y_j = (j - 1/2) R / N (centre of band j).
  * Quasi-parallel beam (far source): ray j is horizontal at height y_j.

Beer-Lambert, material coefficient = 1:
  I_meas(y) = I0(y) * T_casing(y) * T_obj(y),   T_obj(y) = exp(-sum_k rho_k L_k(y))
Step 1 (calibration shot, no object) gives I_cal(y) = I0(y) * T_casing(y), so
  p(y) := -ln(I_meas / I_cal) = sum_k L_k(y) rho_k      (linear in the densities)
Step 2 (tomography) recovers rho from p, given the known chord matrix L.
"""
import numpy as np

N = 4                     # number of shells = number of screen pixels
R = 1.0                   # object radius (model units)
RADII = np.linspace(0, R, N + 1)          # r_0 = 0 ... r_N = R
Y_PIX = (np.arange(N) + 0.5) * R / N      # ray heights, one per screen pixel

RHO_TRUE = np.array([0.6, 1.4, 1.0, 0.4])  # densities, innermost -> outermost
BRICK = 0.2                                 # density carried by one "lego brick"

CASING_WALL = 0.08         # wall thickness crossed twice by every horizontal ray
RHO_CASING = 2.0


def source_profile(y):
    """Source intensity on the screen (fan beam -> mild fall-off with height)."""
    return 1.0 - 0.15 * (np.asarray(y) / R) ** 2


def casing_transmission(y):
    return np.exp(-RHO_CASING * 2 * CASING_WALL) * np.ones_like(np.asarray(y, dtype=float))


def half_chord(r, y):
    """Half-length of the chord of a circle of radius r at height y (0 if missed)."""
    return np.sqrt(np.clip(r ** 2 - y ** 2, 0, None))


def chord_in_shell(k, y):
    """Total path length of a horizontal ray at height y inside shell k (0-based)."""
    return 2 * (half_chord(RADII[k + 1], y) - half_chord(RADII[k], y))


def chord_matrix(y=Y_PIX):
    """L[j, k] = path length of ray j inside shell k  (upper-triangular for band-centred rays)."""
    return np.array([[chord_in_shell(k, yj) for k in range(N)] for yj in np.atleast_1d(y)])


L = chord_matrix()


def optical_depth(rho, y=Y_PIX):
    return chord_matrix(y) @ np.asarray(rho)


def object_transmission(rho, y=Y_PIX):
    return np.exp(-optical_depth(rho, y))


def calibration_shot(y=Y_PIX):
    return source_profile(y) * casing_transmission(y)


def measurement(rho=RHO_TRUE, y=Y_PIX):
    return calibration_shot(y) * object_transmission(rho, y)


P_OBS = -np.log(measurement() / calibration_shot())   # what step 1 delivers


def misfit(bricks):
    r = optical_depth(np.asarray(bricks) * BRICK) - P_OBS
    return float(r @ r)


def brick_fit(max_steps=200):
    """Greedy 'lego' optimisation: each step adds or removes the single brick that
    best reduces the screen mismatch. Returns the list of brick-count states."""
    b = np.zeros(N, dtype=int)
    history = [b.copy()]
    for _ in range(max_steps):
        best, best_val = None, misfit(b)
        for k in range(N):
            for d in (+1, -1):
                c = b.copy(); c[k] += d
                if c[k] < 0:
                    continue
                v = misfit(c)
                if v < best_val - 1e-12:
                    best, best_val = c, v
        if best is None:
            break
        b = best
        history.append(b.copy())
    return history


if __name__ == "__main__":
    np.set_printoptions(precision=3, suppress=True)
    print("chord matrix L (rows = rays bottom->top, cols = shells inner->outer):\n", L)
    print("calibration I_cal :", calibration_shot())
    print("measurement I_meas:", measurement())
    print("object transmission:", measurement() / calibration_shot())
    print("optical depth p   :", P_OBS)
    print("exact inversion   :", np.linalg.solve(L, P_OBS))
    h = brick_fit()
    print(f"brick fit: {len(h) - 1} moves, final bricks {h[-1]} -> rho {h[-1] * BRICK}, misfit {misfit(h[-1]):.2e}")
    print("moves:", [int(np.flatnonzero(h[i + 1] - h[i])[0]) for i in range(len(h) - 1)])
