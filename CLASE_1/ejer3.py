import random

colores =["rojo","negro"]
numeros = range(0,37)

numero_usuario = int(input("elige el numero: "))
color_usuario = input("elige un color:  ")

if numero_usuario not in numeros or color_usuario.lower() not in colores:
    print("EROR,DATOS NO VALIDOS")
    quit()

color_ganador = random.choice(colores)
numero_ganador = random.choice(numeros)

print(f"Ha tocado...El {numero_ganador} {color_ganador} ")

if numero_ganador == numero_usuario and color_ganador == color_usuario:
    print("HAS GANADO")

elif numero_ganador == numero_usuario:
    print("HAS ACERTADO EL NUMERO".lower())
elif color_ganador == color_usuario:
    print("HAS ACERTADO EL COLOR".lower())

else:
    print("HAS PERDIDO!!")