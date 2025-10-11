# 1. Crea una funciÃ³n llamada "personalized_greeting" que reciba un nombre como argumento e imprima 
# "Hola, <nombre>". Si no se proporciona ningÃºn nombre, debe saludar diciendo "Hola, desconocido".

def personalized_greeting(name="desconocido"):
    print(f"Hola, {name}")

personalized_greeting()
personalized_greeting("Jeremy")

# 2. Escribe una funcion llamada "multiply" que reciba dos numeros como argumentos y 
# retorne el resultado de multiplicarlos.

def multiply(n1 , n2):
    return n1 * n2

print(multiply(6,8))

# 3. Crea una funciÃ³n llamada "is_even" que reciba un nÃºmero entero como argumento
# y retorne True si es par y False si es impar.

def is_even(n1):
    par = False
    if n1%2==0:
        par= True
    return par

print(is_even(2))

# 4. Escribe una funciÃ³n llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayÃºsculas.

def convert_to_uppercase(texts: str):
    return print(texts.upper())

convert_to_uppercase("hola")

# 5. Crea una funciÃ³n llamada "arbitrary_sum" que reciba un nÃºmero arbitrario de nÃºmeros como argumentos
# y retorne la suma de todos ellos.

def arbitrary_sum(*numbers):
    return sum(numbers)

print(arbitrary_sum(20,50,30,20))

# 6. Escribe una funciÃ³n llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido,
# y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.

def generate_full_greeting(name , subname):
    return print(f"Hola, {name} {subname}.")

# 7. Crea una funciÃ³n llamada "power" que reciba dos nÃºmeros: base y exponente, 
# y retorne el resultado de elevar la base al exponente.

def power(base , exponent):
    return pow(base,exponent)

# 8. Escribe una funciÃ³n llamada "calculate_average" que reciba tres nÃºmeros y retorne su promedio.

def calculate_average(*numbers):
    return sum(numbers) / len(numbers)

# 9. Crea una funciÃ³n llamada "count_characters" que reciba una cadena de texto y retorne el nÃºmero de caracteres que contiene.

def count_characters(texts):
    return print(len(texts))

count_characters("Hola")
# 10. Escribe una funciÃ³n llamada "display_messages" que reciba un nÃºmero indefinido de cadenas y 
# las imprima en mayÃºsculas, una por una, tal como se hizo en el archivo proporcionado.

def display_messages(*texts):
    for message in texts:
        print(message.upper())
        
display_messages("hola a todos" ,"Como estan")