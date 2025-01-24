class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad

    def saludar(self):
        print(f'Hola, soy {self.nombre} ')
    
    def get_edad(self):
        return self.__edad
   
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Edad incorrecta")