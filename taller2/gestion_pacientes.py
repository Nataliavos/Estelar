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
    while True:
    
            # Validacion de datos numericos y de texto
            identificacion = (input('ingresar numero de identificacion: '))
            while not identificacion.isnumeric():
                print('Error, ingrese un numero valido')
                identificacion = input('ingresar numero de identificacion: ')
            identificacion = int(identificacion)    


           # Validacion de datos numericos y de texto

            nombre = input("Ingrese el nombre del paciente: ").lower().strip()
            apellido = input("Ingrese el apellido del paciente: ").lower().strip()

                
            edad =input('ingresar edad: ')
            while not edad.isnumeric():
                print('Error, ingrese un numero valido')
                edad = input('ingresar edad: ')
            edad = int(edad)
        

            genero = input('ingresar genero: ').lower().strip() # ingresamos datos
            diagnostico = input('ingresar diagnostico: ').lower().strip() # ingresamos datos
            historial = input('ingresar historial medico: ').lower().strip() # ingresamos datos
            break

           
    
    datos_paciente = {
                        'id': identificacion,
                        'nombre': nombre,
                        'apellido': apellido,
                        'edad': edad,
                        'genero': genero,
                        'diagnostico': diagnostico,
                        'historial': historial
                    }
    pacientes.append(datos_paciente)

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
          