"""
d) Escribir una función que reciba un vector y devuelva su norma.
"""


def magnitude(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i] * x[i]
    return sum ** (1/2)
