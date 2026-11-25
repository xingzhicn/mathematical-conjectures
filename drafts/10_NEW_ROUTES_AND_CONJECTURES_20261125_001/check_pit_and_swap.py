"""Exact finite examples for the opposite-pair queries and the coherent square."""

from collections import Counter
from itertools import product
from math import isqrt


def check_matrix_tests():
    # All nonzero rank-one 3-by-3 matrices up to a nonzero scalar on each side.
    p, n, alpha = 7, 3, 3
    points = [tuple(pow(t, i, p) for i in range(n)) for t in range(2 * n - 1)]
    lines = [
        v for v in product(range(p), repeat=n) if next((x for x in v if x), 0) == 1
    ]
    assert len(lines) == 57
    for a, b in product(lines, repeat=2):
        assert any(
            sum(x * y for x, y in zip(a, v)) * sum(x * y for x, y in zip(b, v)) % p
            for v in points
        )

    # The anti-diagonal linear systems used for ranks 1, 2 and 3 are Vandermonde.
    nodes = [pow(alpha, i, p) for i in range(n)]
    for i, node in enumerate(nodes):
        assert all((node - previous) % p for previous in nodes[:i])


def check_square(q):
    s = isqrt(q - 1) + 1
    w = s * s
    table = Counter()
    # Edges in cyclic order are 12, 23, 34 and 41. The first three carry tags.
    for top, right, bottom, left in product(range(w + 1), range(w + q), range(w + 1), range(w)):
        tags = [top >= w, right >= w, bottom >= w]
        # Agreement at vertices 2 and 3 connects the entire tagged tree.
        if tags[0] != tags[1] or tags[1] != tags[2]:
            continue
        if tags[0]:
            if left < q:
                table[left, right - w, right - w, left] += 2
            continue
        (a_top, b_top), (a_right, b_right), (a_bottom, b_bottom), (a_left, b_left) = (
            divmod(label, s) for label in (top, right, bottom, left)
        )
        if b_top != b_left or a_top != a_right or b_right != b_bottom or a_bottom != a_left:
            continue
        outputs = (s*a_top+a_left, s*b_top+b_right, s*a_right+a_bottom, s*b_left+b_bottom)
        if max(outputs) < q:
            table[outputs] += 1
    for i, j, k, l in product(range(q), repeat=4):
        assert table[i, j, k, l] == int(i == k and j == l) + 2 * int(i == l and j == k)


def check_capacities(q, horizontal, vertical, outputs):
    d = q // 2
    w = (isqrt(q - 1) + 1) ** 2
    assert outputs % 2 == 0
    assert d**horizontal >= (w + 1)**outputs
    assert d**vertical >= (w * (w + q))**(outputs // 2)


if __name__ == "__main__":
    check_matrix_tests()
    for dimension in (2, 3, 4, 5):
        check_square(dimension)
    check_capacities(64, 8, 8, 6)
    check_capacities(256, 5, 5, 4)
    print("Matrix queries: 3249 projective rank-one pairs over F7.")
    print("Coherent square: exact output at every coefficient for q = 2, 3, 4, 5.")
    print("Wire capacities: 16 to 6 at q = 64 and 10 to 4 at q = 256.")
