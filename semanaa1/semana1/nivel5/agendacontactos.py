# agenda simple de contactos

# listas para guardar la información
nombres = []
telefonos = []
emails = []

while True:
    print("\n--- agenda ---")
    print("1. agregar contacto")
    print("2. ver contactos")
    print("3. buscar contacto")
    print("4. eliminar contacto")
    print("5. salir")
    
    opcion = input("elige opcion: ")
    
    # agregar contacto
    if opcion == "1":
        nombre = input("nombre: ")
        telefono = input("telefono: ")
        email = input("email: ")
        
        # agregamos a cada lista usando append()
        nombres.append(nombre)
        telefonos.append(telefono)
        emails.append(email)
        
        print("contacto agregado")
    
    # ver todos los contactos
    elif opcion == "2":
        print("\n--- todos los contactos ---")
        
        # verificamos si hay contactos
        if len(nombres) == 0:
            print("no hay contactos")
        else:
            # recorremos con for
            for i in range(len(nombres)):
                print("\ncontacto", i + 1)
                print("nombre:", nombres[i])
                print("telefono:", telefonos[i])
                print("email:", emails[i])
    
    # buscar contacto
    elif opcion == "3":
        buscar = input("nombre a buscar: ")
        encontrado = False
        
        # buscamos en la lista
        for i in range(len(nombres)):
            if nombres[i] == buscar:
                print("\ncontacto encontrado:")
                print("nombre:", nombres[i])
                print("telefono:", telefonos[i])
                print("email:", emails[i])
                encontrado = True
                break
        
        if encontrado == False:
            print("contacto no encontrado")
    
    # eliminar contacto
    elif opcion == "4":
        buscar = input("nombre a eliminar: ")
        encontrado = False
        
        # buscamos el contacto
        for i in range(len(nombres)):
            if nombres[i] == buscar:
                # eliminamos usando pop()
                nombres.pop(i)
                telefonos.pop(i)
                emails.pop(i)
                
                print("contacto eliminado")
                encontrado = True
                break
        
        if encontrado == False:
            print("contacto no encontrado")
    
    # salir
    elif opcion == "5":
        print("adios")
        break