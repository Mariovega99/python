"""
Ejercicio 02b
Escribir funciones que dada una cadena y un carácter:
b) Reemplace todos los espacios por el carácter. Ej: mi archivo
de texto.txt y _ debería devolver mi_archivo_de_texto.txt
"""

cad = input("Inserte una cadena: ")
caracter = input("Inserte un caracter para separar las palabras: ")

def cambiar(cad, caracter):
    salida = ""
    for letra in cad:
        if letra == " ":
            salida += caracter
        else:
            salida += letra
    return salida

print(cambiar(cad, caracter))
