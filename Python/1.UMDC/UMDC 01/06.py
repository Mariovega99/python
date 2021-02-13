"""
Ejercicio 06
Escribir un programa que reciba un número n por parámetro e imprima los
primeros números triangulares, junto con su índice.
Los números triangulares se obtienen mediante la suma de los números naturales
desde 1 hasta n. Es decir, si se piden los primeros 5 números triangulares, el
programa debe imprimir:
1 - 1
2 - 3
3 - 6
4 - 10
5 - 15
Nota: hacerlo usando y sin usar la ecuación n * (n + 1) / 2. ¿Cuál realiza más
operaciones? (Respuesta: triangularIterativo con diferencia)
"""

def triangular(n):
    triangular2 = 0
    for i in range(1, n+1):
        triangular2 += i
    return triangular2


n = int(input("introduza un valor "))

for i in range(1, n+1):
    print(i, " - ", triangular(i))
    triangular(i)