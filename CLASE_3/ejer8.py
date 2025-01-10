'''
Ejercicio 
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, 
correo, preferente), donde preferente tendrá el valor `True` si se trata de un cliente 
preferente. El programa debe preguntar al usuario por una opción del siguiente menú: 
(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los 
clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción 
elegida el programa tendrá que hacer lo siguiente:

1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
3. Preguntar por el NIF del cliente y mostrar sus datos.
4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
6. Terminar el programa.


'''

'''persona={"nombre":"Juan", "edad":25, "ciudad":"Lima","correo":"Thuleitomaznapatinomas@gmail.com"}
     del persona["correo"]'''
clientes={}
opcion= ' '
while opcion!='6':
    if opcion=='1':
        nif= input("Introduce NIF del cliente: ")
        nombre= input("Introduce nombre del cliente: ")
        dirección= input("Introduce dirección del cliente: ")
        telefono= input("Introduce teléfono del cliente: ")
        correo= input("Introduce correo del cliente: ")
        preferente= input("¿El cliente es preferente (S/N): ")
        cliente={'nombre':nombre,'dirección':dirección,'teléfono':telefono,'correo':correo,'preferente':preferente=='S'}
        clientes[nif]=cliente
        #persona["telefono"]="976783049"
        
    if opcion=='2':
        nif= input("Introduce NIF del cliente: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print("No existe cliente con el nif: ", nif)
    
    if opcion=='3':
        nif= input("Introduce NIF del cliente: ")
        if nif in clientes:
            for clave, valor in clientes[nif].items():
                print(clave.title()+' : ',valor)
        else:
            print("No existe cliente con el nif: ", nif)
        
    if opcion=='4':
        print('LA LISTA DE CLIENTES ES: ')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])
    
    if opcion=='5':
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'])
        
        
    opcion=input('Menú de opciones:  \n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Listar cliente\n(4) Lista de cliente\n(5)Listar preferente\n(6) Salir \nElige una opción: ')

