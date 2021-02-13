"""
Ejercicio 02
Escribir un programa que le pregunte al usuario una cantidad de euros, una
tasa de interés y un número de años y muestre como resultado el monto final a
obtener. La fórmula a utilizar es (interés compuesto):
Cf = Ci * (1 + i/100) ^ n
Donde Ci es el capital inicial, i es la tasa de interés y n es el número de
años a calcular.
"""

def interes_compuesto(ci, i, n):
    return ci * (1 + i / 100) ** n

leyendo = True
while leyendo:
    try:
        dinero_inicial = float(input("Introduce el dinero inicial: "))
        anhos = float(input("Introduce los años: "))
        interes = float(input("Introduce el interés (%): "))
        leyendo = False
    except ValueError:
        print("Error en la introduccion de datos\n")

print("Total a pagar: ", interes_compuesto(
    dinero_inicial, interes, anhos), "euros")