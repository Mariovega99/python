"""
c) Modificar las funciones anteriores para que tengan en cuenta el género del
destinatario, para ello, deberán recibir una tupla de tuplas, conteniendo el
nombre y el género.
"""

def campaign_3a(names):
    messages = []
    for name in names:
        messages.append("Estimad" + ("o" if name[0] == "H" else "a") +
                        " %s, vote por mí" % name[1])
    return messages


def campaign_3b(names, pos, num):
    messages = []
    for i in range(pos, pos + num):
        messages.append("Estimad" + ("o" if names[i][0] == "H" else "a") +
                        " %s, vote por mí" % names[i][1])
    return messages