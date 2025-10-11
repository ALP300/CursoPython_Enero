# 1. Crea una funciÃ³n que intente dividir dos nÃºmeros proporcionados por el usuario.
# Usa try-except para capturar cualquier error de divisiÃ³n (por ejemplo, divisiÃ³n por cero).

number1 = 12
number2 = 0

try:
    print(number1/number2)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

# 2. Crea una funciÃ³n que tome una cadena e intente convertirla en un nÃºmero entero. 
# Usa try-except para capturar cualquier error en la conversiÃ³n.

def convert_integer(texts):
    print(int(texts))
    
chain = "Hola"

try:
    convert_integer(chain)
    print("Conversion exitosa")
except:
    print("Conversion fallida")

# 3. Crea una funciÃ³n que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado).
# Usa try-except para gestionar las operaciones de archivos de forma segura.



# 4. Crea una funciÃ³n que realice mÃºltiples operaciones (suma, resta, divisiÃ³n, multiplicaciÃ³n) 
# con dos nÃºmeros. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final,
# independientemente de los errores.

def  multiple_operations(number1 , number2):
    print(number1 +number2)
    print(number1 - number2)
    print(number1 * number2)
    print(number1/number2)

try:
    multiple_operations(12,2)
    print("Operacion cumplida")
except:
    print("Operacion fallida")
finally:
    print("La ejecucion sigue")


# 5. Crea una funciÃ³n que le pida al usuario su edad y lance un ValueError si la entrada no es un nÃºmero entero positivo.
# Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.

def enter_age():
    try:
        age= int(input("Ingresa un numero: "))
        print(age)
        print("Se realizo correctamente")
    except:
        print("Error")
    finally:
        print("La ejecucion sigue")


# 6. Crea una funciÃ³n que intente acceder a un elemento de una lista por Ã­ndice. 
# Usa try-except para manejar el caso donde el Ã­ndice estÃ© fuera de rango.

def list(i):
    
    names = [1,2,3,4,5]
    
    try:
        print(f"{names}")
    except:

# 7. Crea una funciÃ³n que use try-except para manejar mÃºltiples excepciones: ZeroDivisionError, ValueError y TypeError.

        def handle_multiple_exceptions(num1,num2):
            try:
                div = num1 / num2 
                print(div)
            except ZeroDivisionError:
                print("No se puede dividir entre ceros")
            except ValueError:
                print("Valor invalido")
            except TypeError:
                print("Tipo de dato incorrecto")
            

# 8. Crea una funciÃ³n que simule una transacciÃ³n. Lanza una excepciÃ³n personalizada llamada 
# InsufficientFundsError si el saldo es menor que la cantidad a retirar.

class InsufficientFundsError(Exception):
    pass


def simulate_transaction(balance, withdrawal_amount):
    try:
        if withdrawal_amount > balance:
            raise InsufficientFundsError(
                "Saldo insuficiente para la transacciÃ³n.")
        balance -= withdrawal_amount
        print(f"TransacciÃ³n realizada correctamente. Nuevo saldo: {balance}")
    except InsufficientFundsError as e:
        print(f"Error: {e}")
# 9. Crea una funciÃ³n que intente convertir una lista de cadenas en enteros. 
# Maneja cualquier error que surja cuando una cadena no pueda convertirse.

def convert_string_to_integer(*string_list):
    integers = []
    try:
        for string in string_list :
            integers.append(int(string))
            print(integers)
    except TypeError as e:
        print(e)
    

# 10. Crea una función que calcule la raíz cuadrada de un número.
# Lanza un ValueError si el número es negativo.

import math

def calculate_root(num):
    try:
        if num < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        resultado = math.sqrt(num)
        print(f"La raíz cuadrada de {num} es {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
