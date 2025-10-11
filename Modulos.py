# 1. Crea un mÃ³dulo llamado "calculator" que contenga funciones para sumar, restar, 
# multiplicar y dividir dos nÃºmeros. Importa este mÃ³dulo en otro archivo y usa sus funciones.

### MODULO calculator.py  ###
def add(a,b):
    print(a+b)
    
def subtract(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def divide(a,b):
    if b > 0 :
        print(a/b)
    
# 2. Crea un mÃ³dulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius
# y Fahrenheit. Escribe un programa que importe este mÃ³dulo y realice conversiones.

### MODULO converter

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)

def fahrenheit_to_celsius(Fahrenheit):
    celsius = (Fahrenheit - 32 ) * 5/9 

# 3. Crea un mÃ³dulo que contenga una lista de nombres de estudiantes y una funciÃ³n
# que imprima todos los nombres. Importa este mÃ³dulo en otro archivo y usa la funciÃ³n para mostrar la lista.



# 4. Crea un mÃ³dulo llamado "geometry" que tenga una funciÃ³n para calcular el Ã¡rea de un cÃ­rculo y un cuadrado. Usa este mÃ³dulo en otro archivo para calcular Ã¡reas.

# 5. Escribe un mÃ³dulo que contenga una funciÃ³n que acepte cualquier nÃºmero de argumentos y devuelva su suma. Importa y usa la funciÃ³n en otro archivo.

# 6. Crea un mÃ³dulo que defina una clase llamada "Car" con propiedades como marca, modelo y aÃ±o. Importa este mÃ³dulo en otro archivo y crea una instancia de la clase "Car".

# 7. Escribe un mÃ³dulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.

# 8. Crea un mÃ³dulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de nÃºmeros. Usa este mÃ³dulo para calcular estos valores en una lista dada.

# 9. Crea un mÃ³dulo que contenga una funciÃ³n para contar cuÃ¡ntas veces aparece una palabra en un texto. Escribe un programa que importe el mÃ³dulo y lo use para contar palabras en una cadena.

# 10 Crea un mÃ³dulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este mÃ³dulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas especÃ­ficas.