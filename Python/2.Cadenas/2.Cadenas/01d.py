"""
Ejercicio 01d
Escribir funciones que dada una cadena de caracteres:
cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
d) Retorne dicha cadena en sentido inverso.
Ej.: '¡Hola mundo!' debe imprimir '!odnum aloH¡'
"""

cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"

def inversa(cad):
    salida = ""
    for i in range(len(cad)-1, -1, -1):
        salida += cad[i]
    return(salida)


def inversa_2(cad):
    return(cad[::-1])

print(inversa(cad))
print(inversa_2(cad))
