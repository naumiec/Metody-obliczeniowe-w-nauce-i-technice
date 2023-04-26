# iteracja metoda iteracji newtona do rozwiazywania równań niliniwohc

def newton(f, df, x0, eps, maxiter):
    x = x0
    for i in range(maxiter):
        x1 = x - f(x)/df(x)
        if abs(x1 - x) < eps:
            return x1
        x = x1
    return None

if __name__ == "__main__":
    print(newton(lambda x: x**2 - 2, lambda x: 2*x, 1, 1e-6, 1000))


