# 1. Crea una lista con los nÃºmeros del 1 al 5 e imprÃ­mela.

my_list = [1,2,3,4,5]
print(my_list)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].

my_list2 = [10,20,30,40,50]
print(my_list2[2])

# 3. Agrega el nÃºmero 6 al final de la lista [1, 2, 3, 4, 5] e imprÃ­mela.

my_list.append(6)
print(my_list)

# 4. Inserta el nÃºmero 15 en la posiciÃ³n 2 de la lista [10, 20, 30, 40, 50].

my_list2.insert(2,15)
print(my_list2)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].

my_list2.remove(30)
print(my_list2)

# 6. Usa la funciÃ³n pop() para eliminar el Ãºltimo elemento de la lista [1, 2, 3, 4, 5] y almacÃ©nalo en una variable. Imprime la variable y la lista.

otro_list = my_list.pop()
print(otro_list)
print(my_list)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprÃ­mela.

my_list3 = [100,200,300,400,500]
print(my_list3[::-1])

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprÃ­mela.

my_list4 = [3,1,4,2,5]
my_list4.sort()
print(my_list4)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.

list1 = [1,2,3]
list2 = [4,5,6]
new_list = list1 + list2

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posiciÃ³n 1 hasta la 3 (sin incluir la posiciÃ³n 3).
sub_list = my_list2[1:3]
print(sub_list)
