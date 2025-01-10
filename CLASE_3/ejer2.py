'''
Calcular el producto de los números entre A y B
Descripción: Solicita dos números A y B (donde A < B)
y calcula el producto de todos los números en ese
rango, incluyendo A y B.
'''

a= int(input("Por favor ingresa un número a: "))
b= int(input("Por favor ingresa un número b: "))
producto=1
for i in range (a,b+1):
    producto*=i
    
print(f"El producto de los números de {a} y {b} es: {producto}")
    
    
    