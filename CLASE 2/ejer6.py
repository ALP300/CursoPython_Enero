#Escriba un programa que solicite al usuario tres números enteros y muestre el mayor de los tres.
numero1 = int(input("Ingrese un número1: "))
numero2 = int(input("Ingrese un número2: "))
numero3 = int(input("Ingrese un número3: "))

if numero1 >= numero2 and numero1 >= numero3:
    print(f"El número mayor es: {numero1}")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"El número mayor es: {numero2}")

else:
    print(f"El número mayor es: {numero3}")