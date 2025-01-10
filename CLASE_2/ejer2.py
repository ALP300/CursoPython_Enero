'''
Escribe un programa que solicite al usuario dos números y muestre su
suma, resta, multiplicación, división, división entera y residuo (módulo).
'''
num1= float(input("Por favor ingresa el primer número: "))
num2= float(input("Por favor ingresa el segundo número: "))
suma= num1+num2
resta= num1-num2
multiplicacion= num1*num2
div= num1/num2   
divEntera= num1//num2   
modulo= num1%num2
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {div}")
print(f"División Entera: {divEntera}")
print(f"Módulo: {modulo}")