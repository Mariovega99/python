"""
Ejercicio 02a
Escribir funciones que dada una cadena y un carácter:
a) Inserte el carácter entre cada letra de la cadena. Ej: separar y , debería
devolver s,e,p,a,r,a,r
"""

cad = str(input("Introducir palabra: "))

def separar(cad):
    salida = ""
    for letra in cad:
        salida += letra + ","
    return salida[:-1]

print(separar(cad))
