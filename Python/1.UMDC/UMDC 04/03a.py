"""
a) Escribir una función que reciba una tupla con nombres, y para cada nombre
retorne una lista con un menasaje para cada nombre del tipo:
"Estimado [nombre],vote por mí".
"""

def campaign(names):
    messages = []
    for name in names:
        messages.append("Estimado %s, vote por mí" % name)
    return messages