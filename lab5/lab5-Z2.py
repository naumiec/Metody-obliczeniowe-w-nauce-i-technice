from scipy.special import roots_legendre


def f(x):
    return 1 / (1 + x ** 2)


def legendre_integrate(n=8):
    x, w = roots_legendre(n)

    integral = 0
    for i in range(n):
        integral += w[i] * f(x[i])

    return format(integral, '.10f')


if __name__ == "__main__":
    n = 8
    integral = legendre_integrate(n)
    print("Wynik całkowania: ", integral)
