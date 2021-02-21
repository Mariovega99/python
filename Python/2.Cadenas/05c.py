"""
Ejercicio 5c
Escribir una función que dada una cadena de caracteres, devuelva:
c) Las palabras que comiencen con la letra A. Por ejemplo, si recibe "Antes de
ayer" debe devolver "Antes ayer".
"""

cad = input("Introduce una frase: ")
def aes(cad):
    palabras = cad.split()
    salida = ''
    for palabra in palabras:
        if palabra[0] in 'aAáÁ':
            salida += ' ' + palabra
    return salida[1:]

print(aes(cad))
