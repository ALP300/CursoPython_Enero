'''
Contar múltiplos de 7 en un rango
Descripción: Solicita dos números X y Y (donde X < Y) y 
cuenta cuántos números en ese rango son múltiplos de 7.
'''
x= int(input("Por favor ingresa un número a: "))
y= int(input("Por favor ingresa un número b: "))
multiplos=0
for i in range (x,y+1):
    if i%7==0:
        multiplos+=1
    
    
print(f"Hay {multiplos} múltiplos entre {x} y {y} ")