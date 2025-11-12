pacientes = []
datos_paciente = {
    "id": "",
    "nombre": "",
    "apellido": "",
    "edad": "",
    "genero": "",
    "diagnostico": "",
    "historial": []
    }

actualizar_datos = ()

print("\n-actualizar_datos-")

paciente_id = int(input("Ingrese el id del paciente a actualizar"))

paciente_encontrado = None 
for p in pacientes:
    if p.get("id") == paciente_id:
        paciente_encontrado = p
        break

    if not paciente_encontrado:
        print(f"paciente no id {paciente_id} no encontrado")
        
     return
    
print("\n paciente encontrado.")
print(f"id:{paciente_encontrado["id"]}")
print(f"nombre:{paciente_encontrado["nombre"]}")
print(f"apellido:{paciente_encontrado["apellido"]}")
print(f"edad: {paciente_encontrado["edad"]}")
print(f"genero: {paciente_encontrado["genero"]}")
print(f"diagnostico: {paciente_encontrado["diagnostico"]}")
print(f"historial: {paciente_encontrado["historial"]}")

print("\n¿Que Dato deseas Actualizar")
print("1) id")
print("2) nombre")
print("3) apellido")
print("4) edad")
print("5) genero")
print("6) diagnostico")
print("7) historial")

opcion_actualizar = input("Selecciones una opcion (0-7):").strip()

nuevo_id = int(input(f"Ingrese el nuevo id(actual:{paciente_encontrado})"))
while True:
    # mostramos el menú de opciones
    print("===== GESTIÓN DE PACIENTES =====")
    print("1) Agregar Paciente\n2) Buscar Pacientes\n3) Actualizar Datos\n4) Eliminar Pacientes \n5) Reportes \n6) Salir")

    # solicitamos la opción al usuario
    option=input("\nIngresa una opción ->").strip()

    # validamos que la entrada sea numérica y esté dentro del rango de opciones
    if not option.isnumeric() or option not in ["1", "2", "3", "4", "5","6"]:
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

