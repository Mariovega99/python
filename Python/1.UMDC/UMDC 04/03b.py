"""
b) Escribir una función que reciba una tupla con nombres, una posición
de origen p y una cantidad n, e imprima el mensaje anterior para los n
nombres que se encuentran a partir de la posición p.
"""

def campaign(names, pos, num):
    messages = []
    for i in range(pos, pos + num):
        messages.append("Estimado %s, vote por mí" % names[i])
    return messages
