'''
Escribe un programa que solicite al usuario un número entero y calcule
su cuadrado y su cubo.
'''
import math
num1= int(input("Por favor ingresa el primer número: "))
cuadrado2= num1**2
cubo3= num1**3
cuadrado= math.pow(num1,2)
cubo= math.pow(num1,3)
print(f"El cuadrado del número es: {cuadrado}")
print(f"El cubo del número es: {cubo}")