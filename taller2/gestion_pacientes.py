
# pacientes = [{
#       "id": 1234,
#       "nombre": "Natalia",
#       "apellido": "Vargas",
#       "edad": "27",
#       "genero": "femenino",
#       "diagnostico": "migraña",
#       "historial": ["asma", "ansiedad"]
#       },
#       {
#       "id": 3456,
#       "nombre": "Jesus",
#       "apellido": "Perez",
#       "edad": "61",
#       "genero": "masculino",
#       "diagnostico": "calculos renales",
#       "historial": ["hipertensión", "diabetes"]
#       }
#       ]


# ------- Función actualizar_datos -------
def actualizar_datos():
    """
    Permite actualizar cualquiera de los 7 campos de un paciente,
    identificado por su ID.
    """
    print("\n---  ACTUALIZAR DATOS DEL PACIENTE ---")

    
    # Manejo de errores para asegurar que el ID es un número
    try:
        id_actualizar = int(input("Ingrese el ID del paciente a actualizar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return

    # 1. Buscar el paciente (usando la función auxiliar)
   
    paciente_encontrado = None

    for pac in pacientes:
        if pac["id"] == id_actualizar:
            paciente_encontrado = pac
            break
        
    # si no se encuentra el paciente,regresar al menú principal
    if paciente_encontrado is None:
        print(f"No se encontró ningún paciente con ID {id_actualizar}")
        return
    
    # 2. Mostrar datos actuales y opciones de actualización
    print("\n Paciente Encontrado. Datos Actuales:")
    print(f"ID: {paciente_encontrado['id']}")
    for clave, valor in paciente_encontrado.items():
        print(f"   {clave}: {valor}")

    print("\n¿Qué Dato deseas Actualizar?")
    print("1) Edad")
    print("2) Diagnóstico")
    print("3) Historial (Añadir evento)")
    print("0) Cancelar")
   
    opcion_actualizar = input("Seleccione una opción (0-3): ").strip()

    if opcion_actualizar == '0':
        print("Actualización cancelada.")
        return
    
    elif opcion_actualizar == '1':
        # --- Actualizar Edad ---
        try:
            nueva_edad = int(input(f"Edad actual: {paciente_encontrado['edad']}. Ingrese la nueva edad: "))
            paciente_encontrado['edad'] = nueva_edad 
        except ValueError:
            print("Error: La edad debe ser un número entero.")

        print("Edad actualizada correctamente.")
        for clave, valor in paciente_encontrado.items():
            print(f"   {clave}: {valor}")

    elif opcion_actualizar == '2':
        # --- Actualizar diagnóstico ---
        nuevo_diag = (input(f"Diagnóstico actual: {paciente_encontrado['diagnostico']}. Ingrese el nuevo diagnóstico: "))
        paciente_encontrado['diagnostico'] = nuevo_diag
        print("Diagnóstico actualizado correctamente.")
        for clave, valor in paciente_encontrado.items():
            print(f"   {clave}: {valor}")
           
    elif opcion_actualizar == '3':
        # --- Añadir Historial (no reemplaza, sino que añade) ---
        nuevo_historial = input("Ingrese el nuevo evento para el historial: ").strip()
         # Aseguramos que el historial sea una lista
        paciente_encontrado["historial"].append(nuevo_historial)
        print("Evento añadido al historial.")
        for clave, valor in paciente_encontrado.items():
            print(f"   {clave}: {valor}")
       
    else:
        print("opción no válida. Intente de nuevo.")


while True:
    # mostramos el menú de opciones
    print("===== GESTIÓN DE PACIENTES =====")
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