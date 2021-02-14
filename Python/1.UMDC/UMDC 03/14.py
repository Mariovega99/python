"""
Ejercicio 14
Escribir una función que dada la cantidad de ejercicios de un examen, y el
porcentaje necesario de ejercicios bien resueltos necesario para aprobar
dicho examen, revise un grupo de examenes. Para ello, en cada paso debe
preguntar la cantidad de ejercicios resueltos por el alumno, indicando con un
valor centinela que no hay más examenes a revisar. Debe mostrar por pantalla
el porcentaje correspondiente a la cantidad de ejercicios resueltos respecto
a la cantidad de ejercicios del examen y una leyenda que indique si aprobó o
no.
"""

numEj = int(input("Ejercicios totales: "))
porcentaje = int(input("Valor por ejercicio en %: "))

def examen(numEj, porcentaje):
    while True:
        leyendo = True
        while leyendo:
            resueltos = int(input("Numero de ejercicios resueltos (-1 para salir): "))
            leyendo = False
        if resueltos == -1:
            return
        else:
            nota = (100/numEj)*resueltos
            print("El % de ejercicios resueltos es", nota)
            if nota < porcentaje:
                print("Suspenso")
            else:
                print("Aprobado")

print(examen(numEj, porcentaje))