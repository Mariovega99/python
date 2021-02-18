"""
Ejercicio 02d
Escribir funciones que dada una cadena y un carácter:
d) Inserte el carácter cada 3 dígitos en la cadena.
Ej. 2552552550 y . debería devolver 255.255.255.0
"""

cad = "2552552550"

def puntitos(cad):
    salida = ""
    puntos = len(cad) // 3
    for veces in range(puntos):
        for trio in range(3):
            salida += cad[veces * 3 + trio]
        salida += "."
    salida += cad[puntos * 3]
    if salida[-1] == ".":
        salida = salida[:-1]
    return salida

print(puntitos(cad))
