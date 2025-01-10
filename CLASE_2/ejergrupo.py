"""Escribe un programa que tome una calificación numérica de un
estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Menos de 60: F"""

num_cal = int(input("Ingrese un número del 1 al 100: "))

if 90 <= num_cal <= 100:
    print("Tu calificación está en el rango A.")
elif 80 <= num_cal <= 89:
    print("Tu calificación está en el rango B.")
elif 70 <= num_cal <= 79:
    print("Tu calificación está en el rango C.")
elif 60 <= num_cal <= 69:
    print("Tu calificación está en el rango D.")
elif 0 <= num_cal < 60:
    print("Tu calificación está en el rango F.")
else:
    print("El número ingresado no está en el rango válido (1-100).")

