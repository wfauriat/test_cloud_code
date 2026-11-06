"""Physical model shared by every scene (no Manim imports, so it can be tested alone).

Indexing (1-based in the text, 0-based in the code):
  * shell k = 1 .. N, from the OUTERMOST (k = 1) to the innermost (k = N);
    radii are a regular division of R: shell k spans [R (N-k)/N, R (N-k+1)/N].
  * screen row / pixel i = 1 .. N, from the TOP (i = 1) down to the axis;
    row i is a horizontal ray at height y_i = R - (i - 1/2) R / N  (one pixel per shell band).
  * Quasi-parallel beam (far source).

Doses (Beer-Lambert, material coefficient = 1):
  D_mes(i)  = D_0(i) * A_casing(i) * A_object(i),   A_object(i) = exp(-sum_k L_ik rho_k)
  D_void(i) = D_0(i) * A_casing(i)                 (calibration shot / blank virtual shot)
Step 1:  A_object(i) = D_mes(i) / D_void(i),  p_i = -ln A_object(i) = sum_k L_ik rho_k
Step 2:  recover rho from A_object (or p), given the known path lengths L_ik.
Since row i only crosses shells 1..i, L is lower-triangular.
"""
import numpy as np

N = 5
R = 1.0
SHELL_OUT = R * (N - np.arange(N)) / N      # outer radius of shell k (k = 0 is outermost)
SHELL_IN = SHELL_OUT - R / N
Y_PIX = R - (np.arange(N) + 0.5) * R / N    # row i = 0 is the top row

RHO_TRUE = np.array([0.4, 1.0, 1.4, 0.8, 0.6])   # outermost -> innermost
BRICK = 0.2                                       # density carried by one "lego brick"

CASING_WALL = 0.08          # wall thickness crossed twice by every horizontal ray
RHO_CASING = 2.0


def source_dose(y):
    """D_0: source dose reaching the screen (fan beam -> mild fall-off with height)."""
    return 1.0 - 0.15 * (np.asarray(y) / R) ** 2


def casing_factor(y):
    """A_casing: fraction of the dose let through by the two casing walls."""
    return np.exp(-RHO_CASING * 2 * CASING_WALL) * np.ones_like(np.asarray(y, dtype=float))


def half_chord(r, y):
    return np.sqrt(np.clip(r ** 2 - y ** 2, 0, None))


def chord_in_shell(k, y):
    """Total path length of a horizontal ray at height y inside shell k (0-based, 0 = outer)."""
    return 2 * (half_chord(SHELL_OUT[k], y) - half_chord(SHELL_IN[k], y))


def shell_index(r):
    """Shell index (0 = outer) for radius r, -1 outside the object."""
    r = np.asarray(r)
    k = (N - 1) - np.floor(r / R * N).astype(int)
    return np.where(r < R, k, -1)


def chord_matrix(y=Y_PIX):
    """L[i, k] = path length of row i inside shell k."""
    return np.array([[chord_in_shell(k, yi) for k in range(N)] for yi in np.atleast_1d(y)])


L = chord_matrix()


def optical_depth(rho, y=Y_PIX):
    return chord_matrix(y) @ np.asarray(rho)


def object_factor(rho, y=Y_PIX):
    """A_object(i)."""
    return np.exp(-optical_depth(rho, y))


def void_shot(y=Y_PIX):
    """D_void(i): calibration shot or simulation without the object."""
    return source_dose(y) * casing_factor(y)


def measurement(rho=RHO_TRUE, y=Y_PIX):
    """D_mes(i)."""
    return void_shot(y) * object_factor(rho, y)


A_OBS = measurement() / void_shot()       # delivered by step 1
P_OBS = -np.log(A_OBS)


def pixel_mismatch(bricks):
    """Per-pixel difference candidate - observed, in A (what the screen shows)."""
    return object_factor(np.asarray(bricks) * BRICK) - A_OBS


def misfit(bricks):
    r = pixel_mismatch(bricks)
    return float(r @ r)


def brick_fit(max_steps=200):
    """Greedy 'lego' descent: each step adds or removes the single brick that most
    reduces the mismatch. Returns the list of brick-count states."""
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
                if v < best_val - 1e-14:
                    best, best_val = c, v
        if best is None:
            break
        b = best
        history.append(b.copy())
    return history



def candidates_tested(bricks):
    """Simulations needed by one step-walk step from this state: every valid +/-1 brick is tried."""
    return int(N + np.count_nonzero(np.asarray(bricks) > 0))


def jacobian(rho):
    """dA_i/drho_k = -L_ik A_i : the derivative of exp(-L rho)."""
    return -object_factor(rho)[:, None] * L


def gauss_newton(n_iter=6):
    """Gradient-based fit (Gauss-Newton): each iteration = one simulation + its derivative.
    Returns the list of density vectors, starting from zero."""
    rho = np.zeros(N)
    out = [rho.copy()]
    for _ in range(n_iter):
        J = jacobian(rho)
        r = object_factor(rho) - A_OBS
        rho = rho - np.linalg.solve(J.T @ J, J.T @ r)
        out.append(rho.copy())
    return out


def rho_misfit(rho):
    r = object_factor(rho) - A_OBS
    return float(r @ r)



# ============================================================ going further
def geometry(n):
    """Chord matrix and mid radii for the same object split into n regular shells."""
    out = R * (n - np.arange(n)) / n
    inn = out - R / n
    y = R - (np.arange(n) + 0.5) * R / n
    Lm = np.array([[2 * (half_chord(out[k], yi) - half_chord(inn[k], yi)) for k in range(n)] for yi in y])
    return Lm, (out + inn) / 2


def true_rho(n):
    """Same physical object on n shells (n a multiple of N): each band of the 5-shell object is split."""
    return RHO_TRUE[np.arange(n) * N // n]


NOISE = 0.05          # relative noise on the measured dose (hence on A_object)


def noisy_fits(n=N, draws=6, seed=0, many=3000):
    """Direct inversion (no regularisation) of noisy screens.
    Returns true rho, a few (noisy A, estimated rho) draws, and the std of the estimate per shell."""
    Lm, _ = geometry(n)
    rho = true_rho(n)
    A = np.exp(-Lm @ rho)
    rng = np.random.default_rng(seed)

    def one():
        a = A * (1 + NOISE * rng.standard_normal(n))
        return a, np.linalg.solve(Lm, -np.log(a))
    shows = [one() for _ in range(draws)]
    spread = np.array([one()[1] for _ in range(many)]).std(axis=0)
    return rho, A, shows, spread


MU = {1: 1.0, 2: 0.5}   # material 1 (outer shells) absorbs more than material 2: mu1 > mu2
# material patterns (shell 1 .. 5) that all give exactly the observed screen
# shells 1-3 are known to be material 1; only the two inner shells (4, 5) may be either material
MATERIAL_SOLUTIONS = [(1, 1, 1, 1, 1), (1, 1, 1, 2, 1), (1, 1, 1, 1, 2), (1, 1, 1, 2, 2)]


def densities_for(materials):
    """Only mu * rho is observable: density needed in each shell for a given material pattern."""
    return np.array([RHO_TRUE[k] / MU[m] for k, m in enumerate(materials)])


def screen_for(materials, rho):
    mu = np.array([MU[m] for m in materials])
    return object_factor(mu * rho)


def biased_fit(bias):
    """Inversion with a blank misestimated by a factor (1 + bias): A_est = A_obj / (1 + bias)."""
    return np.linalg.solve(L, -np.log(A_OBS / (1 + bias)))

if __name__ == "__main__":
    np.set_printoptions(precision=3, suppress=True)
    print("L (rows i = top -> bottom, cols k = outer -> inner):\n", L)
    print("D_void :", void_shot())
    print("D_mes  :", measurement())
    print("A_obj  :", A_OBS)
    print("p      :", P_OBS)
    print("exact inversion:", np.linalg.solve(L, P_OBS))
    h = brick_fit()
    print(f"brick fit: {len(h) - 1} moves -> rho {h[-1] * BRICK}, misfit {misfit(h[-1]):.2e}")
    print("moves (shell, +/-):", [(int(np.flatnonzero(h[i + 1] - h[i])[0]) + 1, int((h[i + 1] - h[i]).sum()))
                                  for i in range(len(h) - 1)])
    print("misfit path:", [f"{misfit(s):.1e}" for s in h])
