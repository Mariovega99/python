"""
4.- Vectores
a) Escribir una función que reciba dos vectores y devuelva su
producto escalar.
"""

def scalar(x, y):
    p = list()
    for i in range(len(x)):
        p.append(x[i]*y[i])
    return sum(p)