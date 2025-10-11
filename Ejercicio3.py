"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

numGanador = []
for i in range(5):
    usuario = int(input("Ingrese los numeros ganadores de la loteria: "))
    numGanador.append(usuario)

numGanador.sort()
print(numGanador)

"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""
listCursos = ["Matematica" , "Fisica", "Quimica", "Historia" , "Lengua"]

notas = list()

for cursos in listCursos:
    nota = int(input(f'Introduce la nota del curso {cursos}: '))
    notas.append(nota)
        
for cursos,notas in zip(listCursos,notas):
        print(f'En {cursos} has sacado {notas}')

if notas in         

