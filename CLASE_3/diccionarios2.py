#TEORIA PART 1

#AGREGAR
'''
persona={"nombre":"Juan", "edad":25, "ciudad":"Lima","correo":"Thuleitomaznapatinomas@gmail.com"}

persona["telefono"]="976783049"
print(persona)
'''
#ELIMINAR

'''persona={"nombre":"Juan", "edad":25, "ciudad":"Lima","correo":"Thuleitomaznapatinomas@gmail.com"}
del persona["correo"]
print(persona)'''

#ITERAR
for clave,valor in persona.items():
    print(f"{clave}:{valor}")