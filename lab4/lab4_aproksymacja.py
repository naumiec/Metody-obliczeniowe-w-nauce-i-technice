import numpy as np
from time import time


def pointwise_approximation(x, y):
    n = len(x)
    A = np.zeros((n, 3))
    b = y.copy()

    A[:, 0] = x ** 2
    A[:, 1] = x
    A[:, 2] = np.ones(n)

    coeffs = np.linalg.solve(A, b)

    return coeffs


if __name__ == "__main__":
    x = np.array([234, 432, 567])
    y = np.array([18364395, 62386329, 107371299])

    start = time()
    f = pointwise_approximation(x, y)
    end = time()

    a, b, c = f
    a, b, c = round(a, 5), round(b, 5), round(c, 5)
    print(f"Wielomian ma postać: {a} x^2 + {b} x + {c}")
    print(f"Time: {end - start}")

