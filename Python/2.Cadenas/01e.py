"""
Ejercicio 01e
Escribir funciones que dada una cadena de caracteres:
e) Imprima la cadena en un sentido y en sentido inverso.
Ej: reflejo imprime reflejoojelfer.
"""

cad = 'reflejo'

def reflejo(cad):
    salida = cad
    for i in range(len(cad)-1, -1, -1):
        salida += cad[i]
    return(salida)


def reflejo_2(cad):
    return(cad + cad[::-1])

print(reflejo(cad))
print(reflejo_2(cad))
