pacientes = []
"""datos_paciente = {
    "id": "",
    "nombre": "",
    "apellido": "",
    "edad": "",
    "genero": "",
    "diagnostico": "",
    "historial": []
    }
"""



def agregar_pacientes():
    print('---------- Agregar Pacientes ----------')
    while True: # validacion de datos numericos y de texto para el id reciva solo numeros
            try:
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
                

        
    genero = input('iINGRESE GENERO: ').lower().strip() # ingresamos datos

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
    for paciente in pacientes:
        print(f'{paciente["id"]}|{paciente["nombre"]}|{paciente["apellido"]}|{paciente["edad"]}|{paciente["genero"]}|{paciente["diagnostico"]}|{paciente["historial"]}')

agregar_pacientes()



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
          