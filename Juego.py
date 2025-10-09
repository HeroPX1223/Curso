fosforo = "a"
linterna = "b"
correr = "c"
quedarse_quieto = "d"
esconderse= "e"
avanzar = "f"

print("Opciones:")
print(fosforo)
print(linterna)

eleccion = input("Estás caminando por un bosque oscuro y encunetras dos objetos: un fósforo y una linterna. ¿Cuál eliges? (Escribe a para 'fósforo' o b para 'linterna'):")
if eleccion == fosforo:
    print("Coges el fósforo y lo enciendes. Por un instante, el bosque se ilumina... ¡Ves un oso grizzly, el fósofro se apaga")
    eleccion = input("¿Qué haces? (Escribe c para 'correr', d para 'quedarse quieto', e para 'esconderse'): ")
    if eleccion == correr:
         print("Decides correr, pero el oso es más rápido. Te alcanza y te come. Game over. Try again.")
    elif eleccion == quedarse_quieto:
         print("Decides quedarte quieto. El oso se acerca, te huele y se va.")
         eleccion = input("¿Qué haces ahora? (Escribe f para 'avanzar'): ")
         if eleccion == avanzar:
              print("Felicidades ganaste")
         else:
              print("No has elegido una opción válida. Game over. Try again.")
    elif eleccion == esconderse: 
         print("Decides esconderte arriba de un árbol. El oso te ve y tira el árbol, y te partes la cabeza. Game over. Try again.") 
    else:
         print("No has elegido una opción válida. Game over. Try again.")
   