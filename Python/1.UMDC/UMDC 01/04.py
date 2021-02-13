"""
Ejercicio 04
Utilice el programa anterior para generar una tabla de conversión de
temperaturas, desde 0º F hasta 120º F, de 10 en 10.
"""

def conversion(f):
    return (f - 32) * 5/9

print("Grados Fahrenheit     Grados Celsius")
print("=================     ==============")

for f in range(0, 121, 10):
    print(f, "                   ", conversion(f))