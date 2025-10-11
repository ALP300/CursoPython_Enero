tupla = (10,20,30,40,50)
print(tupla)

print("--- IGNORE ---")

tupla1 = (100,200,300,400,500)
print(tupla1[2])

print("--- IGNORE ---")

tupla2 = (1,2,3,3,4,5,3)
print(tupla2.count(3))

print("--- IGNORE ---")

tupla3 = ("Java", "Python", "JavaScript", "Python")
print(tupla3.index("Python"))
print("--- IGNORE ---")

tupla4 = (1,2,3)
tupla5 = (4,5,6)
tupla_suma = tupla4 + tupla5
print(tupla_suma)

print("--- IGNORE ---")

tupla6 = (10,20,30,40,50)
sub_tupla = tupla6[1:4]
print(sub_tupla)
print("--- IGNORE ---")

tupla_colores = ("rojo", "verde", "azul")
tupla_colores = list(tupla_colores)
tupla_colores.insert(1, "amarillo")
tupla_colores = tuple(tupla_colores)
print(tupla_colores)

print("--- IGNORE ---")

tupla_elemento = (100,)
print(type(tupla_elemento))  
