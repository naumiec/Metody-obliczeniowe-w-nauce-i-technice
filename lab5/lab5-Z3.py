import numpy as np
from math import pi


def f(x):
    return 1 / ((x ** 2) + 1)


def rectangle(a, b, h=0.1, n=10):
    array = np.linspace(a, b, num=n, endpoint=False)
    integral = sum(map(lambda x: f(x) * h, array))
    absolute_error = abs(integral - (pi / 4))

    return format(integral, '.10f'), format(absolute_error, '.10f')


def trapezoidal(a, b, h=0.1, n=10):
    array = np.linspace(a, b, num=n + 1, endpoint=True)
    integral = sum([(f(x) + f(x - h)) * h / 2 for x in array[1:]])
    absolute_error = abs(integral - (pi / 4))

    return format(integral, '.10f'), format(absolute_error, '.10f')


def simpson(a, b, h=0.1):
    n = int((b - a) / (2 * h))
    x = np.linspace(a, b, 2 * n + 1)
    y = f(x)
    integral = h / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    absolute_error = abs(integral - (pi / 4))

    return format(integral, '.10f'), format(absolute_error, '.10f')


if __name__ == "__main__":
    a = 0
    b = 1
    h = 0.1
    n = 10

    print("Rectangle method: ", rectangle(a, b, h, n))
    print("Trapezoidal method: ", trapezoidal(a, b, h, n))
    print("Simpson method: ", simpson(a, b, h))
