pacientes = []

contador = 0
def contador_pacientes():
    global contador
    contador += 1



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
    for paciente in pacientes:
        print(f'{azul}{"ID":<15}{"NOMBRE":<15}{"APELLIDO":<15}{"EDAD":<15}{"GENERO":<15}{"DIAGNOSTICO":<15}{"HISTORIAL":<15}{reset}')  # Completar con los campos necesarios
        # imprimo los datos de cada paciente
        print(f'{paciente["id"]:<15}{paciente["nombre"]:<15}{paciente["apellido"]:<15}{paciente["edad"]:<15}{paciente["genero"]:<15}{paciente["diagnostico"]:<15}{paciente["historial"]:<15}')
    contador_pacientes() # llamo a la funcion contador pacientes para contar los pacientes agregados

agregar_pacientes() # llamo a la funcion agregar pacientes para iniciar el programa

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
    info = input("SELECIONE EL NUMERO DE LA OPCION QUE DECEA HACER: ")
        

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

        print(f'el total de pacientes es: {contador}') # imprimo el total de pacientes registrados
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


