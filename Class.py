# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y 
# un mÃ©todo "make_sound" que imprima un sonido genÃ©rico.

class Anima:
    
    def __init__(self,species):
        self.species= species

    def make_sound(self,sound):
        print("aaaaaaaaaaaaaaaa")

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacÃ©nala en una propiedad pÃºblica.ç
# AÃ±ade el mÃ©todo "make_sound" que imprima un sonido dependiendo de la especie.

class Animal:
    def __init__(self,species):
        self.species = species

    def make_sound(self):
        if self.make_sound == "perro":
            print("GUAU-GUAU")
        elif self.make_sound == "gato":
            print("MIAU-MIAU")
        else:
            print("Sonido generico")

# 3. Crea una clase llamada "Car" con las propiedades pÃºblicas "brand" y "model". 
# AdemÃ¡s, debe tener una propiedad privada "_speed" que inicialmente serÃ¡ 0.

class Car:
    def __init__(self,brand,model,speed = 0):
        self.brand = brand
        self.model = model
        self.__speed = speed #Privada

# 4. AÃ±ade a la clase "Car" un mÃ©todo llamado "accelerate" que aumente la velocidad en 10 unidades. 
# añade tambiÃ©n un mÃ©todo "brake" que reduzca la velocidad en 10 unidades. AsegÃºrate de que la velocidad no sea negativa.

    def accelerate(self):
        self.__speed +=10
    
    def brake(self):
        self.__speed = max(0, self.__speed - 10)

# 5. Crea una clase "Book" que tenga propiedades como "title" (pÃºblico) y "author" (privado). 
# AÃ±ade un mÃ©todo para obtener el autor y otro para cambiar el tÃ­tulo del libro.

class Book:
    def __init__(self,title,author):
        self.title = title
        self.__author = author

    def get_author(self):
        return self.__author
    
    def change_title(self,new_title):
        self.title = new_title

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. 
# AÃ±ade un mÃ©todo para calcular y devolver la nota media del estudiante.

class Estudiante:
    def __init__(self,name,subname,*notes):
        self.name = name
        self.subname = subname
        self.notes = notes
    
    def calculate_average(self):
        average = sum(self.notes)/len(self.notes)
        print(f"El estudiante {self.name} {self.subname} tiene de promedio {average}")

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". 
# AÃ±ade mÃ©todos para depositar y retirar dinero, asegurÃ¡ndote de que no se pueda retirar mÃ¡s de lo que hay en la cuenta.

class BankAccount:
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Depósito exitoso. Saldo actual: {self.balance}")
        else:
            print("El monto a depositar debe ser positivo.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Retiro exitoso. Saldo restante: {self.balance}")
        else:
            print("Fondos insuficientes o monto inválido.")


# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". 
# AÃ±ade un mÃ©todo que calcule la distancia entre dos puntos.

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked".
# AÃ±ade un mÃ©todo que calcule el pago total basado en las horas trabajadas y el salario por hora.

class Employee:
    def __init__(self,name,hourly_wage,hours_worked):
        self.name = name 
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
    
    def calculate_payment(self,hourly_wage,hours_worked):
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        salary = hours_worked * hourly_wage
        print(f"Tu salario es {salary}")
        

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). ç
# AÃ±ade un mÃ©todo para agregar un producto al inventario y otro para mostrar todos los productos disponibles.

class Store:
    def __init__(self):
        self.inventory = []  # empezamos con lista vacía
    
    def add_product(self, new_product):
        self.inventory.append(new_product)
        print(f"Producto '{new_product}' agregado al inventario.")
    
    def show_products(self):
        if self.inventory:
            print("Productos disponibles:")
            for product in self.inventory:
                print(f"- {product}")
        else:
            print("No hay productos en el inventario.")
