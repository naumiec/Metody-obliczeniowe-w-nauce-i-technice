import math
import numpy as np
import time

def f(x):
    if x == 0:
        return 0
    return math.cos(x) * math.exp(x ** -2)

def rectangle(a, b, n):
    time_start = time.time()

    dx = (b - a) / n
    suma = 0
    for i in range(n):
        x = a + i * dx
        suma += f(x)

    time_stop = time.time()

    return dx * suma, time_stop - time_start

def trapezoidal(a, b, n):
    time_start = time.time()

    dx = (b - a) / n
    suma = 0
    for i in range(n):
        x1 = a + i * dx
        x2 = a + (i + 1) * dx
        suma += (f(x1) + f(x2)) / 2

    time_stop = time.time()

    return dx * suma, time_stop - time_start

def simpson(a, b, n):
    time_start = time.time()

    dx = (b - a) / n
    suma = 0
    for i in range(n):
        x1 = a + i * dx
        x2 = a + (i + 1) * dx
        xm = (x1 + x2) / 2
        suma += (f(x1) + 4 * f(xm) + f(x2)) / 6

    time_stop = time.time()

    return dx * suma, time_stop - time_start

if __name__ == "__main__":
    a = 0
    b = 1000

    n = 1000
    rectangle_result, rectangle_time = rectangle(a, b, n)
    print("Metoda prostokątów: ", rectangle_result, rectangle_time)
    trapezoidal_result, trapezoidal_time = trapezoidal(a, b, n)
    print("Metoda trapezów: ", trapezoidal_result, trapezoidal_time)

    n = 100
    simpson_result, simpson_time = simpson(a, b, n)
    print("Metoda Simpsona: ", simpson_result, simpson_time)
