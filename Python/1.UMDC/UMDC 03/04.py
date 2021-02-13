"""
Ejercicio 04
Escribir una función que reciba un número entero k e imprima su
descomposición en factores primos.
"""

def fact_primos(n):
    if n < 2:
        print(1)
    else:
        i = 2
        print(1)
        while (n/2 + 1) > i:
            if n % i == 0:
                print(i)
                n //= i
            else:
                i += 1
        print(n)