"""
Ejercicio 4
Escribir una función que reciba una cadena que contiene un largo número entero
y devuelva una cadena con el número y las separaciones de miles. Por ejemplo,
si recibe 1234567890, debe devolver 1.234.567.890
"""

cad = "1234567890"

def puntua(cad):
    long = len(cad)
    primeros = long % 3
    if primeros > 0:
        salida = cad[0:primeros]+"."
    else:
        salida = ""
    for i in range(0, (long//3)*3, 3):
        salida = salida + cad[primeros + i:primeros + i + 3] + "."
    return salida[:-1]

print(puntua(cad))
