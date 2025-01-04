
#Mi primer juego (Tim4do)


import random as rn

print('Comienza el juego')
print('-Piedra(1)\n-Papel(2)\n-Tijera(3)\n-Salir(0)')


eleccion = int(input('\nElige una opcion: '))


opcion=['piedra','papel','tijera']





while eleccion != 0 :
     

     aleatorio = rn.choice(opcion)



     if eleccion == 1:
         
         print('\nLa computadora elige: '+aleatorio)

         if aleatorio == 'piedra':
              
              print('Intenta de nuevo!!')

         elif aleatorio == 'papel':
              print('Gana la computadora :c')

         elif aleatorio == 'tijera':
              
              print('Felicidades a ganado!!')

     elif eleccion == 2:
         
         print('\nLa computadora elige: '+aleatorio)

         if aleatorio == 'papel':
              
              print('Intenta de nuevo!!')

         elif aleatorio == 'tijera':
              print('Gana la computadora :c')

         elif aleatorio == 'piedra':
              
              print('Felicidades a ganado!!')

     elif eleccion == 3:
         
         print('\nLa computadora elige: '+aleatorio)

         if aleatorio == 'tijera':
              
              print('Intenta de nuevo!!')

         elif aleatorio == 'piedra':
              print('Gana la computadora :c')

         elif aleatorio == 'papel':
              
              print('Felicidades `a ganado!!')

     print('\n-Piedra(1)\n-Papel(2)\n-Tijera(3)\n-Salir(0)')
     eleccion = int(input('\nElige una opcion: '))


print("Gracias por jugar. ¡Hasta luego!")