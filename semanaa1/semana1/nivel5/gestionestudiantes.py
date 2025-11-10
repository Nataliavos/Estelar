# mini base de datos de estudiantes

# listas para guardar la información
nombres = []
edades = []
carreras = []

while True:
    print("\n--- estudiantes ---")
    print("1. agregar estudiante")
    print("2. ver estudiantes")
    print("3. buscar estudiante")
    print("4. eliminar estudiante")
    print("5. salir")
    
    opcion = input("elige opcion: ")
    
    # agregar estudiante
    if opcion == "1":
        nombre = input("nombre: ")
        edad = int(input("edad: "))
        carrera = input("carrera: ")
        
        # agregamos a cada lista
        nombres.append(nombre)
        edades.append(edad)
        carreras.append(carrera)
        
        print("estudiante agregado")
    
    # ver todos los estudiantes
    elif opcion == "2":
        print("\n--- lista de estudiantes ---")
        
        # verificamos si hay estudiantes
        if len(nombres) == 0:
            print("no hay estudiantes")
        else:
            # recorremos con for
            for i in range(len(nombres)):
                print("nombre:", nombres[i])
                print("edad:", edades[i])
                print("carrera:", carreras[i])
                print("---")
    
    # buscar estudiante
    elif opcion == "3":
        buscar = input("nombre a buscar: ")
        encontrado = False
        
        # buscamos en la lista de nombres
        for i in range(len(nombres)):
            # si el nombre coincide
            if nombres[i] == buscar:
                print("\nestudiante encontrado:")
                print("nombre:", nombres[i])
                print("edad:", edades[i])
                print("carrera:", carreras[i])
                encontrado = True
                break  # salimos del for
        
        # si no lo encontramos
        if encontrado == False:
            print("no encontrado")
    
    # eliminar estudiante
    elif opcion == "4":
        buscar = input("nombre a eliminar: ")
        encontrado = False
        
        # buscamos el estudiante
        for i in range(len(nombres)):
            if nombres[i] == buscar:
                # eliminamos de todas las listas usando pop()
                # pop(i) elimina el elemento en la posición i
                nombres.pop(i)
                edades.pop(i)
                carreras.pop(i)
                
                print("estudiante eliminado")
                encontrado = True
                break
        
        if encontrado == False:
            print("no encontrado")
    
    # salir
    elif opcion == "5":
        print("adios")
        break