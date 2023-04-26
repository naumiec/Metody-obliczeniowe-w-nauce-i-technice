from sys import float_info
from numpy import float32, finfo



def epsilon():
    eps_double = 1.0
    while (1.0 + eps_double / 2.0) != 1.0:
        eps_double /= 2.0

    eps_float = float32(1.0)
    while (float32(1.0) + eps_float / float32(2.0)) != float32(1.0):
        eps_float /= float32(2.0)

    print("Należy pamiętać, że w języku Python nie ma typu double, a typ float działa jak double w języku C (podwójna precyzja).")
    print("Typ float (32 bitowy) można uzyskać za pomocą biblioteki numpy i funkcji float32().\n")

    print("Obliczone maszynowe epsilon dla double:", eps_double)
    print("Wartość rzeczywista (double) =", float_info.epsilon, "\n")

    print("Obliczone maszynowe epsilon dla float:", eps_float)
    print("Wartość rzeczywista (float) =", finfo(float32).eps)


if __name__ == "__main__":
    epsilon()

'''
Należy pamiętać, że w języku Python nie ma typu double, a typ float działa jak double w języku C (podwójna precyzja).
Typ float (32 bitowy) można uzyskać za pomocą biblioteki numpy i funkcji float32().

Obliczone maszynowe epsilon dla double: 2.220446049250313e-16
Wartość rzeczywista (double) = 2.220446049250313e-16
Obliczone maszynowe epsilon dla float: 1.1920929e-07
Wartość rzeczywista (float) = 1.1920929e-07
'''