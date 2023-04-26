import numpy as np
from math import log


def f(x):
    return 1 / (1 + x)


def rectangle(a, b, n):
    h = (b - a) / n
    integral = 0

    for i in range(n):
        xi = a + i * h
        integral += f(xi) * h

    absolute_error = abs(integral - log(2))
    relative_error = absolute_error / log(2)

    return format(integral, '.10f'), format(absolute_error, '.10f'), format(relative_error, '.10f')


def trapezoidal(a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2

    for i in range(1, n):
        xi = a + i * h
        integral += f(xi)
    integral *= h

    absolute_error = abs(integral - log(2))
    relative_error = absolute_error / log(2)

    return format(integral, '.10f'), format(absolute_error, '.10f'), format(relative_error, '.10f')


def simpson1(a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]
    integral = y[0] + y[-1]

    for i in range(1, n, 2):
        integral += 4 * y[i]
    for i in range(2, n - 1, 2):
        integral += 2 * y[i]

    integral *= h / 3

    absolute_error = abs(integral - log(2))
    relative_error = absolute_error / log(2)

    return format(integral, '.10f'), format(absolute_error, '.10f'), format(relative_error, '.10f')


def simpson2(a, b, n, eps=1e-8):
    m = n // 2
    dx = (b - a) / n
    x = a + dx
    sum1 = 0
    sum2 = 0

    for i in range(1, m + 1):
        sum1 += f(x)
        x += 2 * dx
    x = a + 2 * dx
    for i in range(1, m):
        sum2 += f(x)
        x += 2 * dx
    integral = dx * (f(a) + 4 * sum1 + 2 * sum2 + f(b)) / 3

    err = eps + 1
    while err > eps:
        old_integral = integral
        n *= 2
        m *= 2
        dx /= 2
        x = a + dx
        sum1 = 0
        sum2 = 0

        for i in range(1, m + 1):
            sum1 += f(x)
            x += 2 * dx
        x = a + 2 * dx
        for i in range(1, m):
            sum2 += f(x)
            x += 2 * dx

        integral = dx * (f(a) + 4 * sum1 + 2 * sum2 + f(b)) / 3
        err = abs(integral - old_integral) / 15

    absolute_error = abs(integral - log(2))
    relative_error = absolute_error / log(2)

    return format(integral, '.10f'), format(absolute_error, '.10f'), format(relative_error, '.10f')


if __name__ == "__main__":
    a = 0
    b = 1
    h = 0.1
    n = 10


    print("Rectangle method: ", rectangle(a, b, n))
    print("Trapezoidal method: ", trapezoidal(a, b, n))
    print("Simpson method: ", simpson1(a, b, n))
    print("Composite Simpson method: ", simpson2(a, b, n))
