"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y
el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""

hrs_trabajadas = int(input("Ingrese el numero de horas trabajadas: "))
costo_hr = float(input("Ingrese el costo por hora trabajada: "))
total = hrs_trabajadas * costo_hr

print(f"El total pagado fue {total}")
print("----------------------------------------------------")


"""
Escribir un programa que lea un entero positivo, 
, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
. La suma de los 
primeros enteros positivos puede ser calculada de la siguiente forma:
"""
n = int(input("Introduce un numero entero positivo: "))

suma = (n*(n+1))/2

print("La suma es " + str(suma))