"""
Ejercicio 5a
Escribir una función que dada una cadena de caracteres, devuelva:
a) La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial
Bus debe devolver USB.
"""

cad = input("Introduce una frase y te devolveré sus siglas: ")

def siglas(cad):
    palabras = cad.split()
    sig = ""
    for palabras in palabras:
        sig = sig + palabras[0]
    return sig.upper()

print(siglas(cad))
