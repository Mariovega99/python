"""
Ejercicio 6c
Escribir funciones que dada una cadena de caracteres:
c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe
'vestuario' debe devolver 'vistaerou'.
"""

cad = 'vestuario'

def revocaliza(cad):
    cambio=""
    vocales="aeiouaAEIOUA"
    for caracter in cad:
        if caracter in vocales:
            cambio += vocales[vocales.find(caracter) + 1]
        else:
            cambio += caracter
    return cambio

print(revocaliza(cad))
