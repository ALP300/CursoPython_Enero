# 1. Usa un bucle while para imprimir los nÃºmeros del 1 al 10.

i = 0

while i <= 10:
    print(i)
    i+=1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada nÃºmero.

num = [10, 20, 30, 40, 50]
for i in num:
    print(i)

# 3. Escribe un programa que use un bucle while para sumar los nÃºmeros del 1 al 100 e imprime el resultado.

num1 = 0
suma = 0
while num1 <= 100:
    suma += num1
    print(suma)
    num1 +=1

# 4. Escribe un bucle for que imprima cada carÃ¡cter de la cadena "Python".

word = "Python Backend"
for letter in word:
    print(letter)

# 5. Usa un bucle while para encontrar el primer nÃºmero divisible por 7 entre 1 y 50.

i = 1 
while i <= 50:
    if i % 7 == 0:
        print(f"El numero {i} es divisible por 7")
    i +=1
# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.

dict = {"name": "Brais", "age": 37, "country": "Galicia"}

for clave in dict:
    print(clave)

# 7. Escribe un programa que use un bucle while para imprimir los nÃºmeros pares entre 1 y 20.

i=0
while i <= 20:
    if i % 2== 0:
        print(f"El numero {i} es par")
    i+=1
print("Se acabo el diccionario")

# 8. Usa un bucle for con la funciÃ³n range() para imprimir los nÃºmeros del 1 al 10 en orden inverso.

i=0

for i in range(11,0,-1):
    print(i)
    
# 9. Escribe un programa que use un bucle for para contar cuÃ¡ntas veces aparece el nÃºmero 30 
# en la lista[30, 10, 30, 20, 30, 40].

numeros = [30, 10, 30, 20, 30, 40]

contador = 0

for num in numeros:
    if num == 30:
        contador += 1

print("El número 30 aparece", contador, "veces en la lista.")


# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".

name = ["Jose","Danna","Angel","Brais","Brais"]
i=0
for names in name:
    if names == "Brais":
        i+=1
print(f"El nombre Brais se repite {i}")