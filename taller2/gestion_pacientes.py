

pacientes = []

contador = 0
def contador_pacientes():
    global contador
    contador += 1


# ------- FUNCIÓN AGREGAR PACIENTES -------

def agregar_pacientes():
    print('---------- Agregar Pacientes ----------')
    while True: 
            
            try:#validacion de datos numericos y de texto para el id reciva solo numeros
                identificacion = int(input('INGRESE EL NUMERO DE IDENTIFICACIO DEL PACIENTE: '))
                break # salimos del bucle si la entrada es valida
            except ValueError:
                print('Error, ingrese un numero valido') #print mensaje de error

           # Validacion de datos numericos y de texto
    nombre = input("INGRESE EL NOMBRE DEL PACIENTE: ").lower().strip()
    apellido = input("INGRESE EL APELLIDO DEL PACIENTE: ").lower().strip()

    while True: # validacion de datos numericos y de texto para el id reciva solo numeros
            try:
                edad = int(input('INGRESE LA EDAD: ')) # ingresamos datos
                break # salimos del bucle si la entrada es valida
            except ValueError:
               print('Error, ingrese un numero valido') #imprimimos mensaje de error
                
        
    genero = input('INGRESE GENERO: ').lower().strip() # ingresamos datos

    diagnostico = input('INGRESE EL DIAGNOSTICO: ').lower().strip() # ingresamos datos

    historial = input('INGRESE EL HISTORIAL: ').lower().strip() # ingresamos datos
   
    
    datos_paciente ={
                    'id': identificacion, # identificacion del paciente
                    'nombre': nombre, # nombre del paciente
                    'apellido': apellido,# apellido del paciente
                    'edad': edad, # edad del paciente
                    'genero': genero,# genero del paciente
                    'diagnostico': diagnostico, # diagnostico del paciente
                    'historial': historial # historial del paciente
                 }
                 
    pacientes.append(datos_paciente)
    print('------------------PACIENTE AGREGADO EXITOSAMENTE-------------------')
    azul = "\033[34m" # color azul
    reset = "\033[0m" # reset color
    # recorro la lista de pacientes y muestro sus datos
    print(f'{azul}{"ID":<15}{"NOMBRE":<15}{"APELLIDO":<15}{"EDAD":<15}{"GENERO":<15}{"DIAGNOSTICO":<15}{"HISTORIAL":<15}{reset}')  # Completar con los campos necesarios# imprimo los datos de cada paciente
    for paciente in pacientes:
        print(f'{paciente["id"]:<15}{paciente["nombre"]:<15}{paciente["apellido"]:<15}{paciente["edad"]:<15}{paciente["genero"]:<15}{paciente["diagnostico"]:<15}{paciente["historial"]:<15}')
        contador_pacientes() # llamo a la funcion contador pacientes para contar los pacientes agregados



# ------- FUNCIÓN BUSCAR PACIENTE -------
def buscar_paciente(criterio, valor):
    """Busca pacientes según criterio"""
    return [p for p in pacientes if valor.lower() in str(p.get(criterio, "")).lower()]


def buscar_pacientes():
    
    if not pacientes:
        print("\n no hay pacientes registrados\n")
        return
    
    print("\n===== BUSCAR PACIENTES =====")
    print("1) Buscar por ID")
    print("2) Buscar por Nombre") 
    print("3) Buscar por Diagnóstico")
    
    opcion = input("\nseleccione: ").strip()
    
    if opcion not in ["1", "2", "3"]:
        print("opcion invalida.")
        return
    
    valor = input("ingrese valor a buscar: ").strip()
    
    criterios = {"1": "id", "2": "nombre", "3": "diagnostico"}
    resultados = buscar_paciente(criterios[opcion], valor)
    
    if resultados:
        print(f"\n✓ encontrados {len(resultados)} paciente(s):\n")
        for p in resultados:
            print(f"  ID: {p.get('id')}")
            print(f"  Nombre: {p.get('nombre')} {p.get('apellido')}")
            print(f"  Edad: {p.get('edad')}")
            print(f"  Género: {p.get('genero')}")
            print(f"  Diagnóstico: {p.get('diagnostico')}")
            print(f"  Historial: {p.get('historial')}")
            print("-" * 40)
    else:
        print("\n✗ No se encontró ningún paciente.\n")


# ------- FUNCIÓN ACTUALIZAR DATOS -------
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


# ------- FUNCIÓN ELIMINAR PACIENTES -------
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


# ------- 5. FUNCIÓN PARA GENERAR REPORTES
def generar_reportes(): # creamos la funcion generar reportes
    print('------------------Reporte de pacientes:-------------------')
    azul = "\033[34m" # color azul
    reset = "\033[0m" # reset color
    #imprrimo encabezado de la tabla
    print(f'{azul}{"ID":<10}{"NOMBRE":<15}{"APELLIDO":<15}{"EDAD":<10}{"GENERO":<15}{"DIAGNOSTICO":<15}{"HISTORIAL":<15}{reset}')  # Completar con los campos necesarios
    
    print(f"{azul}{'-'*90}{reset}") # linea extra de separacion

    for paciente in pacientes: # recorro la lista de pacientes  
        # imprimo los datos de cada paciente
     print(f'{paciente["id"]:<10}{paciente["nombre"]:<15}{paciente["apellido"]:<15}{paciente["edad"]:<10}{paciente["genero"]:<15}{paciente["diagnostico"]:<15}{paciente["historial"]:<15}')  # Completar con los campos necesarios

    # creo las ociones de reporte   
    print("-------------------------------opciones de reporte----------------------------")
    print("1: PACIENTES MAYORES DE 60 AÑOS.")
    print("2: PACIENTES CON DIAGNOSTICO ESPECIFICO. ")
    print("3: PACIENTES POR GENERO. ")
    print('4: TOTAL DE PACIENTES REGISTRADOS.')
    print("5: volver. ")
    info = input("SELECIONE UNA OPCIÓN: ")
        

    if info == "1":
        print("PACIENTES MAYORES DE 60 AÑOS:")
        for paciente in pacientes: # recorro la lista de pacientes
            if paciente["edad"]>60: # Valido si la edad es mayor a 60
             # imprimo el encabezado de la tabla
             print("\033[34m" + f'{"ID":<10}{"NOMBRE":<15}{"APELLIDO":<15}{"EDAD":<10}{"GENERO":<15}{"DIAGNOSTICO":<15}{"HISTORIAL":<15}' + "\033[0m")  # Completar con los campos necesarios
           # imprimo los datos de cada paciente que cumple la condicion
             print(f'{paciente["id"]:<10}{paciente["nombre"]:<15}{paciente["apellido"]:<15}{paciente["edad"]:<10}{paciente["genero"]:<15}{paciente["diagnostico"]:<15}{paciente["historial"]:<15}')  # Completar con los campos necesarios
    
    if info == "4": # opcion 4 total de pacientes registrados
        print('-----------------------------TOTAL DE PACIENTES REGISTRADOS:------------------------')

        print(f'el total de pacientes es: {len(pacientes)}') # imprimo el total de pacientes registrados
        volver = input("Presione S para VOLVER...") # pausa para volver al menu principal
        if volver.lower() == "s":
            generar_reportes() # vuelvo a seccion generar reportes

    if info == "2":
        diagnostico = input('ingrese el diagnostico que desea buscar: ').lower().strip()
        print(f'pacientes con diaagnostico de {diagnostico}:')
        for paciente in pacientes:
            if paciente["diagnostico"] == diagnostico:
             print("\033[34m" + f'{"ID":<10}{"NOMBRE":<15}{"APELLIDO":<15}{"EDAD":<10}{"GENERO":<15}{"DIAGNOSTICO":<15}{"HISTORIAL":<15}' + "\033[0m")  # Completar con los campos necesarios
             print(f'{paciente["id"]:<10}{paciente["nombre"]:<15}{paciente["apellido"]:<15}{paciente["edad"]:<10}{paciente["genero"]:<15}{paciente["diagnostico"]:<15}{paciente["historial"]:<15}')  # Completar con los campos necesarios

    if info == "5":
     agregar_pacientes()
    

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
