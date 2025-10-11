"""
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla.
"""
listCursos = ["Matematica" , "Fisica", "Quimica", "Historia" , "Lengua"]

print(listCursos)

"""
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura>
es cada una de las asignaturas de la lista.
"""

for cursos in listCursos:
    print(f'Yo estudio {cursos}')
    

"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje
En <asignatura> has sacado <nota> donde <asignatura>
es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""
notas = list()

for cursos in listCursos:
    nota = int(input(f'Introduce la nota del curso {cursos}: '))
    notas.append(nota)
        
for cursos,notas in zip(listCursos,notas):
        print(f'En {cursos} has sacado {notas}')

print("-------------------")
        




