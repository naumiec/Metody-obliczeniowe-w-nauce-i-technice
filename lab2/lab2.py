import math



def e_to_x_power_1(x=1, epsilon=0.000001):
    e_to_x_power = 0
    i = 0

    while True:
        e_to_x_power += (x ** i) / math.factorial(i)
        if abs(x ** (i + 1) / math.factorial(i + 1)) < epsilon:
            break
        i += 1

    return e_to_x_power


def e_to_x_power_2(x=1, n=100):
    e_to_x_power = 0

    for i in range(n):
        e_to_x_power += (x ** i) / math.factorial(i)

    return e_to_x_power


if __name__ == '__main__':
    powers = [1, -1, 5, -5, 10, -10]
    values = [2.71828182845904523536,
              0.36787944117144232159,
              148.41315910257660342111,
              0.00673794699908546709,
              22026.46579480671651695790,
              0.00004539992976248485]

    for power, value in zip(powers, values):
        print("Przybliżona wartość e do potęgi {} wynosi: {}".format(power, value))

        e1 = e_to_x_power_1(power)
        print("WERSJA 1. (epsilon) Wyliczona wartość e do potęgi {} wynosi: {}".format(power, e1))
        print("WERSJA 1. (epsilon) Błąd względny 1: {}".format(abs(value - e1) / value))

        e2 = e_to_x_power_2(power)
        print("WERSJA 2. (n iteracji) Wyliczona wartość e do potęgi {} wynosi: {}".format(power, e2))
        print("WERSJA 2. (n iteracji) Błąd względny 1: {}\n".format(abs(value - e2) / value))
