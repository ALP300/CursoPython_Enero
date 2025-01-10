#TEORIA PART 1

persona={"nombre":"Juan", "edad":25, "ciudad":"Lima","correo":"Thuleitomaznapatinomas@gmail.com"}

print("Nombre: ",persona["nombre"])
print("Edad: ",persona["edad"])
print("Ciudad: ",persona["ciudad"])

if "telefono" in persona:
    print("La clave se encuentra :D")
else:
    print("No se encuentra la clave")