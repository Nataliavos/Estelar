

pacientes = [{
    "id": 1234,
    "nombre": "Natalia",
    "apellido": "Vargas",
    "edad": "27",
    "genero": "femenino",
    "diagnostico": "migraña",
    "historial": ["asma", "ansiedad"]
    },
    {
        "id": 1234,
    "nombre": "Natalia",
    "apellido": "Vargas",
    "edad": "27",
    "genero": "femenino",
    "diagnostico": "migraña",
    "historial": ["asma", "ansiedad"]
    }
    ]

def eliminar_pacientes():
    print(f"{pacientes}")
    eliminar_id = ((f"Ingrese el ID del paciente que desea eliminar"))
    dicc_eliminar = {"id" : eliminar_id}
    print(f"dicc_eliminar")
    confirmar = (f"¿Está seguro de eliminar el paciente: ID {eliminar_id("id", "nombre", "apellido")}? si/no").lower()
    if confirmar == "si":
        pacientes.remove(dicc_eliminar)
    

    

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