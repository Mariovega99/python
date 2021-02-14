"""
1.- Escribir una función que reciba una tupla de elementos e indique si se
encuentran ordenados de menor a mayor o no.
"""

def test_sorted(tupla):
    if tupla == ():
        return -1
    previous = tupla[0]
    for item in tupla:
        if previous <= item:
            previous = item
        else:
            return False
    return True