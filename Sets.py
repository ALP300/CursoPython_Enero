
# 1. Crea un set con los nÃºmeros del 1 al 5 e imprÃ­melo.

set1 = {1,2,3,4,5}
print(type(set1))
print(set1)

# 2. AÃ±ade el nÃºmero 6 al set {1, 2, 3, 4, 5} e imprÃ­melo.

set1.add(6)
print(set1)

# 3. Intenta aÃ±adir el nÃºmero 5 al set {1, 2, 3, 4, 5} nuevamente. Â¿QuÃ© sucede?



# 4. Verifica si el nÃºmero 3 estÃ¡ en el set {1, 2, 3, 4, 5} e imprime el resultado.

print( 3 in set1)

# 5. Elimina el nÃºmero 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.

set1.discard(4)
print(set1)

# 6. Usa el mÃ©todo clear() para vaciar un set y luego imprime su longitud.

set1.clear()
print(len(set1))

# 7. Convierte el set {"manzana", "naranja", "plÃ¡tano"} en una lista e imprime el primer elemento de la lista.

set_fruits = {"Manzana", "Naranja", "Platano"}
new_set = list(set_fruits)
print(new_set[0])

# 8. Realiza la uniÃ³n de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.

set1 = {1,2,3}
set2 = {4,5,6}
set_num = set1.union(set2)
print(set_num)

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.

print(set_num.difference(set2))


# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.

del set1
print(set1)