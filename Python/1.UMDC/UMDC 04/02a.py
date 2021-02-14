"""
a) Escribir una función que indique si dos fichas de dominó encajan o no.
Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4).
"""

def domino(token_1, token_2):
    return (token_1[0] == token_2[0] or token_1[0] == token_2[1]
            or token_1[1] == token_2[0] or token_1[1] == token_2[1])