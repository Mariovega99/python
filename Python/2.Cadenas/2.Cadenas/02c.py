"""
Ejercicio 02c
Escribir funciones que dada una cadena y un carácter:
c) Reemplace todos los dígitos en la cadena por el carácter "X".
Ej: su clave es: 1540 y X debería devolver su clave es: XXXX
"""

clave = input("Inserte una clave: ")

def cambiar_x(clave):
    salida = ""
    digitos = "0123456789"
    for letra in clave:
        if letra in digitos:
            salida += "X"
        else:
            salida += letra
    return salida

print(cambiar_x(clave))
