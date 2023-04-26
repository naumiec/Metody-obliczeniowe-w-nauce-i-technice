import numpy as np
import time

def f(x):
    return np.exp(-x ** 2) * np.cos(x)

def simpson(f, a, b):
    h = b - a
    middle = (a + b) / 2

    return h * (f(a) + 4 * f(middle) + f(b)) / 6

def adaptive_quadrature(f, a, b, epsilon):
    mid = (a + b) / 2
    diff = abs(simpson(f, a, b) - simpson(f, a, mid) - simpson(f, mid, b))

    if diff < 15 * epsilon:
        return simpson(f, a, mid) + simpson(f, mid, b)
    return adaptive_quadrature(f, a, mid, epsilon / 2) + adaptive_quadrature(f, mid, b, epsilon / 2)

if __name__ == "__main__":
    a = 0
    b = 10000
    epsilon = 1e-6
    time_start = time.time()
    print("Wynik: ", adaptive_quadrature(f, a, b, epsilon))
    time_end = time.time()
    print("Czas: ", time_end - time_start)



