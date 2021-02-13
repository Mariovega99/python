"""
Ejercicio 03
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
Celsius. Recordar que la fórmula para la conversión es: F = 9/5 * C + 32.
"""

def conversion(f):
    return (f - 32) * 5/9

leyendo = True
while leyendo:
    try:
        fh = float(input("Introduce una temperatura en Farenheit: "))
        leyendo = False
    except ValueError:
        print("Introduce un valor numérico\n")

print("La temperatura equivalente en Celsius es: ", conversion(fh))