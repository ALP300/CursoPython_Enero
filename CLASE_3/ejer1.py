'''
Imprimir números impares de N a 1
Descripción: Escribe un programa que solicite 
un número N al usuario e imprima todos los 
números impares desde N hasta 1 en orden descendente.

'''

n= int(input("Por favor ingresa un número: "))


for i in range(n,0,-1):
    if i%2 !=0:
        print(i)