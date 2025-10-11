# 1. Escribe un programa que verifique si un nÃºmero es positivo, negativo o cero.
nro = 1

if nro > 0:
    print("El numero es positivo")
else:
    print("El numero es negativo")
    
print("---------------------------------------")
# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 aÃ±os o mÃ¡s) o menor de edad.

edad = int(input("Ingrese su edad: "))

if edad >= 18 :
    print("Es mayor de edad")
else:
    print("Es menor de edad")
print("---------------------------------------")

# 3. Escribe un programa que verifique si una cadena de texto estÃ¡ vacÃ­a y muestre un mensaje en consecuencia.

cadena = ""

if cadena == "":
    print("cadena vacia")
else:
    print("cadena llena")

print("---------------------------------------")

# 4. Crea un programa que solicite dos nÃºmeros al usuario y compare cuÃ¡l es mayor. 
# Si son iguales, muestra un mensaje indicando la igualdad.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2:
    print(f'El numero {num1} es mayor.')
elif num2 > num1:
    print(f'El numero {num2} es mayor')
else:
    print("Son iguales")
print("---------------------------------------")

# 5. Escribe un programa que verifique si un nÃºmero es divisible por 3 y por 5 al mismo tiempo.

num3 = int(input("Ingrese un numero: "))

if num3 % 3 == 0 and num3 % 5 == 0:
    print(f'El numero {num3} es divisible por 3 y 5')
else:
    print("No es divisible por 3 y 5")

print("----------------------------------------")

# 6. Solicita al usuario que ingrese un nÃºmero y verifica si es par o impar.

def par_impar(numero):
    return numero%2 == 0

par = int(input("Ingrese un numero: "))

if par_impar(par):
    print("Es par")
else:
    print("Es impar")
print("---------------------------------")

# 7. Escribe un programa que determine si una persona puede votar en funciÃ³n de su edad(mayor o igual a 18).
# Si tiene 16 o 17 aÃ±os, indica que puede votar con permiso especial.

def votar(numero):
    return numero >= 18

def votar_permiso(numero):
    return numero >= 16 and numero <= 17 

edad = int(input("Ingrese su edad: "))

if votar(edad):
    print("Si puede votar")
elif votar_permiso(edad):
    print("Puede votar pero con permiso especial")
else:
    print("No puede votar")
print("-------------------------------------")

# 8. Crea un programa que solicite una contraseÃ±a al usuario y verifique si coincide con una contraseÃ±a predefinida.
# Si no coincide, muestra un mensaje de error.

def verificacion(password):
    return password == "contraseña"

password = input("Ingrese la contraseña: ")

if verificacion(password):
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

# 9. Escribe un programa que determine si un nÃºmero estÃ¡ entre 10 y 20 (ambos incluidos).



# 10. Escribe un programa que simule un semÃ¡foro: solicita al usuario que ingrese un color(rojo, amarillo, verde)
# y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.

semaforo= input("Ingrese un color(rojo, amarillo o verde): ")

if semaforo.lower() == "rojo":
    print("Detenerse")
elif semaforo.lower() == "amarillo":
    print("Alerta")
elif semaforo.lower() == "verde":
    print("Avanze")
else:
    print("Color ingresado incorrecto")