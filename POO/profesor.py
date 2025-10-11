from persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def ensenar(self):
        print(f'{self.nombre} está enseñando {self.materia}')
    
    