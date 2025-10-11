from estudiante import Estudiante
from profesor import Profesor

estudiante = Estudiante('Juan', 20, 'Ingeniería en Sistemas')
profesor= Profesor('Carlos', 30, 'Matemáticas')

estudiante.saludar()
estudiante.estudiar()
profesor.ensenar()
profesor.saludar()
print(f"Edad de {estudiante.nombre} es: {estudiante.get_edad()}")
estudiante.set_edad(25)
print(f"Edad de {estudiante.nombre} es: {estudiante.get_edad()}")