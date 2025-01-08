#ver si una roca es un peligro inminente
roca = input("el valor de la roca que se aserque es de: ",)
roca_f = float(roca)

print(f" ojo:el valor de la roca esta medida a travez de m^3 y sera comparado a un valor de una roca promedio para ver si la roca es peligrosa o no")

roca_P = input("insertar el valor de la roca promedio: ",)
roca_P_f = float(roca_P)

print(f"necesitamos el valor de la proximidad de velocidad de la roca")

proximidad = input(f"el valor de proximidad es de: ",)
proximidad_f = float(proximidad)

if roca_f<roca_P_f:
    print(str(" la roca es menor que la roca promedio de tamaño " + roca_P + " no necesita observación"))
    if proximidad_f>100:
        print(str(" la roca va a una velocidad muy peligrosa a pesar de su tamaño de " + roca + " afectara a la nave sera necesario hacer maniobras evasivas"))
    elif proximidad_f == 100:
        print(str(" la roca va a una velocidad promedio a pesar de su tamaño de " + roca + " puede afectar a la nave sera necesario hacer maniobras evasivas"))
    elif proximidad_f == 0:
        print("no tiene velocidad, no es amenaza alguna")
    else:
        print(str(" la roca va a muy poca velocidad no es amenaza alguna"))

elif roca==roca_P:
    print(str(" la roca es igual a la roca promedio de tamaño " + roca_P + " no necesita observación"))
    if proximidad_f > 100:
        print(str(" la roca va a una velocidad muy peligrosa a pesar de su tamaño de " + roca + " afectara a la nave sera necesario hacer maniobras evasivas"))
    elif proximidad_f == 100:
        print(str(" la roca va a una velocidad promedio a pesar de su tamaño de " + roca + " puede afectar a la nave sera necesario hacer maniobras evasivas"))
    elif proximidad_f == 0:
        print("no tiene velocidad, no es amenaza alguna")
    else:
        print(str(" la roca va a muy poca velocidad no es amenaza alguna"))

else:
    print(str("la roca es mayor que la roca promedio de valor "+ roca_P + " necesita observación constante es un peligro inminente"))
    if proximidad_f > 100:
        print(str("la roca de tamaño " + roca + " es demasiado grande y con la velocidad de aproximación de " + proximidad + " que se aserca es imposible evadir el choque"))
    elif proximidad_f == 100:
        print(str("la roca de tamaño " + roca + " es demasiado grande y con la velocidad de aproximación de " + proximidad + " que se aserca hay posibilidad de hacer maniobras evasivas y sobrevivir"))
    elif proximidad_f == 0:
        print("no tiene velocidad, no es amenaza alguna")
    else:
        print(str("la roca de tamaño " + roca + " es grande pero con la velocidad de aproximación de " + proximidad + " sera muy facil de evadirla"))
