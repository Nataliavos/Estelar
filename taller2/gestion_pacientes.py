
# ------------ DATOS DE PRUEBA ------------
# pacientes = [{
#      "id": 1234,
#      "nombre": "Natalia",
#      "apellido": "Vargas",
#      "edad": "27",
#      "genero": "femenino",
#      "diagnostico": "migraña",
#      "historial": ["asma", "ansiedad"]
#      },
#      {
#      "id": 3456,
#      "nombre": "Jesus",
#      "apellido": "Perez",
#      "edad": "61",
#      "genero": "masculino",
#      "diagnostico": "calculos renales",
#      "historial": ["hipertensión", "diabetes"]
#      }
#      ]
pacientes = [] 

# ------- FUNCIÓN 4: ELIMINAR PACIENTES -------
def eliminar_pacientes():
    # si no hay pacientes registrados, regresar al menú principal
    if not pacientes:
        print("No hay pacientes registrados.")
        return 
    # mostrar la lista de pacientes registrados
    print("Lista actual de pacientes:")
    print("--------------------------")
    for pac in pacientes:
        print(f"\n{pac['id']} - {pac['nombre']} {pac['apellido']}")
        for clave, valor in pac.items():
            print(f"   {clave}: {valor}")

    # pedir el ID del paciente a eliminar, con manejo de error si no es numérico
    try:
        eliminar_id = int(input("Ingrese el ID del paciente que desea eliminar: "))
    except ValueError:
        print("El ID debe ser un número, intente de nuevo\n.")
        return
    
    # buscar paciente por ID en los diccionarios de la lista pacientes
    paciente_encontrado = None
    for pac in pacientes:
        if pac["id"] == eliminar_id:
            paciente_encontrado = pac
            break
    # si no se encuentra el paciente,regresar al menú principal
    if paciente_encontrado is None:
        print(f"No se encontró ningún paciente con ID {eliminar_id}")
        return

    # confirmar eliminación
    print(f"\n¿Seguro que desea eliminar el paciente {paciente_encontrado['id']} - {paciente_encontrado['nombre']} {paciente_encontrado['apellido']}?")
    confirmar = input("Escriba 'si' para confirmar o 'no' para cancelar: ").strip().lower()

    # si el usuario ingresa "si", eliminar el paciente de la lista
    if confirmar == "si":
        pacientes.remove(paciente_encontrado)
        print(f"\nPaciente {paciente_encontrado['id']} - {paciente_encontrado['nombre']} {paciente_encontrado['apellido']} ha sido eliminado.")
        
        # si quedan pacientes, mostrar la lista actualizada
        if pacientes:
            print("\nLista actualizada de pacientes: ")
            print("---------------------------------")
            for pac in pacientes:
                print(f"\n{pac['id']} - {pac['nombre']} {pac['apellido']}")
                for clave, valor in pac.items():
                    print(f"   {clave}: {valor}")
        else:
            print("\nNo quedan pacientes en la lista.")
    # si el usuario ingresa "no", cancelar la eliminación
    elif confirmar == "no":
        print("\nEliminación cancelada.")
    # si el usuario ingresa otra cosa, mostrar mensaje y cancelar la eliminación
    else:
        print("\nOpción no válida. Eliminación cancelada.")


    

    
# ------------ MENÚ PRINCIPAL ------------
while True:
    # mostramos el menú de opciones
    print("------- GESTIÓN DE PACIENTES -------")
    print("1) Agregar Paciente\n2) Buscar Pacientes\n3) Actualizar Datos\n4) Eliminar Pacientes \n5) Reportes \n6) Salir")

    # solicitamos la opción al usuario
    option=input("\nIngresa una opción ->").strip()

    # validamos que la entrada sea numérica y esté dentro del rango de opciones
    if not option.isnumeric() or option not in ["1", "2", "3", "4", "5", "6"]:
        print("Por favor ingrese una opción válida.")
        continue # volvemos a pedir el dato

    # convertimos la entrada a entero
    option = int(option)

    # usamos match para las opciones del menú. Definimos las funciones fuera del match para mayor claridad.
    # ejecutamos la función correspondiente según la opción seleccionada
    match option:
        
        case 1:
            agregar_pacientes() #Camilo
        case 2:
            buscar_pacientes() #Lucas
        case 3:
            actualizar_datos() #Vero
        case 4:
            eliminar_pacientes() #Natalia
        case 5:
            generar_reportes() # 
        case 6:
            print("¡Hasta la próxima!")
            break # salimos del bucle y terminamos el programa