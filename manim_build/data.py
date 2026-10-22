"""Toy data from spec §1.3 (illustrative numbers)."""
import math

VOCAB = 50_000

# (token label, probability); the last row is always the "others" bucket
D_TRAINED = [("mat", .46), ("floor", .19), ("sofa", .11), ("bed", .07), ("roof", .04), ("49,995 others", .13)]
D_NEXT1 = [(".", .58), (",", .14), ("and", .09), ("while", .04), ("↵", .03), ("others", .12)]
D_NEXT2 = [("The", .31), ("It", .18), ("She", .12), ("Then", .08), ("A", .06), ("others", .25)]
D_EARLY = [("mat", .02), ("floor", .03), ("sofa", .02), ("bed", .02), ("roof", .02), ("49,995 others", .89)]

# S3: tokens sampled in each iteration (row index in the shown distribution)
SAMPLES = [(D_TRAINED, 0), (D_NEXT1, 0), (D_NEXT2, 1)]   # "mat", ".", "It" (not the top token)

# S5: training progress for p(mat) and the matching losses
TRAIN_P = [0.02, 0.08, 0.21, 0.46]
TRAIN_LOSS = [3.91, 2.53, 1.56, 0.78]
EXAMPLES_SEEN = ["1,000", "1,000,000", "1,000,000,000"]

# S4 loss-meter examples
P_RIGHT, P_WRONG = 0.9, 0.01


def loss(p):
    """Cross-entropy for one position: -ln p(true token)."""
    return -math.log(p)


RANDOM_LOSS = math.log(VOCAB)   # ≈ 10.8


def loss_curve(x):
    """Schematic training curve, x in 0..1 ("training examples seen")."""
    return 2.2 + 8.6 * math.exp(-x / 0.18)


def blend(d0, d1, w):
    """Linear blend of two distributions over the same rows (keeps the sum at 1)."""
    return [(l1, (1 - w) * p0 + w * p1) for (_, p0), (l1, p1) in zip(d0, d1)]


def toward_trained(p_mat):
    """Distribution between D_EARLY and D_TRAINED in which p(mat) == p_mat."""
    return blend(D_EARLY, D_TRAINED, (p_mat - D_EARLY[0][1]) / (D_TRAINED[0][1] - D_EARLY[0][1]))


def percents(dist):
    return [round(p * 100) for _, p in dist]


# sanity: every displayed state sums to 1 and to 100 % once rounded; losses match the spec
for _d in [D_TRAINED, D_NEXT1, D_NEXT2, D_EARLY] + [toward_trained(p) for p in TRAIN_P]:
    assert abs(sum(p for _, p in _d) - 1) < 1e-9
    assert sum(percents(_d)) == 100, percents(_d)
for _p, _l in zip(TRAIN_P, TRAIN_LOSS):
    assert abs(loss(_p) - _l) < 0.01
assert round(loss(P_RIGHT), 2) == 0.11 and round(loss(P_WRONG), 2) == 4.61
assert round(RANDOM_LOSS, 1) == 10.8 and round(loss_curve(0), 1) == 10.8
