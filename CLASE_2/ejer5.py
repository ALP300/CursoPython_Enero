'''5. Escribe un programa que tome una calificación numérica de un
estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Menos de 60: F'''

#Se declara una variable para almacenar la nota
nota = int(input("Ingrese la califiacion del estudiante: "))

#Creamos la condicional   
if nota >= 90 and nota <= 100 :
    print("A")
elif nota >= 80 and nota <= 89:
    print("B")
elif nota >= 70 and nota <= 79:
    print("C")
elif nota >= 60 and nota <= 69:
    print("D")
elif nota <= 60:
    print("F")