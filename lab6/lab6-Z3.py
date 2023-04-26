from math import cos
import time
import numpy as np



def f(x):
    return cos(x)


def gauss_hermite_integration(n, test=True):
    x, w = np.polynomial.hermite.hermgauss(n)
    if not test:
        print("weights:", *w)
        print("roots:", *x)

    return sum([w[i] * f(x[i]) for i in range(n)])


if __name__ == "__main__":
    for n in [4, 8, 16, 32, 64]:
        start_time = time.time()
        result = gauss_hermite_integration(n, True)
        end_time = time.time()
        print("n =", n, "\n", "result =", result, "\n", "time =", end_time - start_time, "seconds")