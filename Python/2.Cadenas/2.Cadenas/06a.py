"""
Ejercicio 6a
Escribir funciones que dada una cadena de caracteres:
a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe
'Algoritmos o logaritmos' debe devolver 'lgrtms  lgrtms'.
"""

cad = input("Introduce una frase y te devolveré las consonantes: ")

def consonantes(cad):
    consonante = ""
    for letra in cad:
        if letra not in "aeiouAEIOU":
            consonante += letra
    return consonante

print(consonantes(cad))
