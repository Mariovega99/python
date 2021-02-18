"""
Ejercicio 01c
Escribir funciones que dada una cadena de caracteres:
cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
c) Retorne dicha cadena cada dos caracteres. Ej.: "recta" imprime "rca"
"""

cad = 'En un lugar de la Mancha de cuyo nombre no quiero acordarme'

def cada_dos(cad):
    cadena = ""
    for i in range(0, len(cad), 2):
        cadena += cad[i]
    return(cadena)


def cada_dos_2(cad):
    return(cad[::2])


print(cada_dos(cad))
print(cada_dos_2(cad))
