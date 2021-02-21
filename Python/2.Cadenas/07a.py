"""
Ejercicio 7a
Escribir funciones que dadas dos cadenas de caracteres:
a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo,
"cadena" es una subcadena de "subcadena".
"""

cad = 'subcadena'
subcad = 'cadena'

def subcadena(cad, subcad):
    return cad.find(subcad) != -1

print(subcadena(cad, subcad))
