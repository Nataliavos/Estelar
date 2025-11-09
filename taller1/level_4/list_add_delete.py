'''Agregar y eliminar frutas.'''

# creamos una lista con frutas
fruits = ["mandarina", "fresa", "piña", "mango"]

# usamos un ciclo para mostrar el menú hasta que el usuario decida salir
while True:
    # mostramos el menú, solicitamos al usuario elegir una opcion y la guardamos en la variable "action"
    action = input("¿Qué quieres hacer?\n1) Buscar una fruta \n2) Agregar una fruta \n3) Eliminar una fruta \n4) Salir").strip()

    # validamos la entrada: que sea un número y que esté entre las opciones válidas
    if not action.isnumeric() or action not in ["1", "2", "3", "4"]:
        print("Opción no válida. Intenta de nuevo.")
        continue

    # convertimos la entrada a entero para usar en el match
    action = int(action)

    # usamos match para las opciones del menú
    match action:
        # buscar fruta
        case 1:
            search_fruit = input("Ingresa el nombre de la fruta a buscar -->").lower().strip()
            # verificamos si la fruta está e imprimimos la respuesta (si está o no)
            if search_fruit in fruits:
                print(f"La fruta '{search_fruit}' está en la lista.")
            else:
                print(f"La fruta '{search_fruit}' no está en la lista.")
        # agregar fruta
        case 2:
            new_fruit = input("Ingresa el nombre de la fruta --> ").lower().strip()
            # agregamos la fruta a la lista
            fruits.append(new_fruit)
            # mostramos mensaje de confirmación y lista actualizada
            print(f"Fruta '{new_fruit}' agregada. Frutas disponibles: {fruits}")
        # eliminar fruta
        case 3:
            # si la lista está vacía, no permite eliminar
            if not fruits:
                print("No hay frutas para eliminar.")
            # si la lista no está vacía, solicitamos el nombre de la fruta a eliminar
            else:
                delete_fruit = input("Ingrese la fruta a eliminar -->").lower().strip()
                # si la fruta está en la lista, la eliminamos
                if delete_fruit in fruits:
                    fruits.remove(delete_fruit)
                    print(f"Fruta '{delete_fruit}' eliminada. Frutas disponibles: {fruits}")
                else :
                    print(f"La fruta '{delete_fruit}' no está en la lista.")
        # salir del programa
        case 4:
            print("¡Hasta la próxima!")
            break # salimos del ciclo y terminamos el programa
