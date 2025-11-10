# agenda para guardar contactos

# lista de diccionarios (cada contacto es un diccionario)
contactos = []

while True:
    print("\n--- agenda de contactos ---")
    print("1. agregar contacto")
    print("2. ver todos los contactos")
    print("3. buscar contacto")
    print("4. eliminar contacto")
    print("5. salir")
    
    opcion = input("elige una opción: ")
    
    # opción 1: agregar nuevo contacto
    if opcion == "1":
        nombre = input("nombre: ")
        telefono = input("teléfono: ")
        email = input("email: ")
        
        # creamos el contacto como diccionario
        contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "email": email
        }
        
        contactos.append(contacto)
        print("✓ contacto agregado")
    
    # opción 2: mostrar todos los contactos
    elif opcion == "2":
        print("\n--- todos los contactos ---")
        if len(contactos) == 0:
            print("no hay contactos guardados")
        else:
            for i, c in enumerate(contactos, 1):
                print(f"\n{i}. {c['nombre']}")
                print(f"   teléfono: {c['telefono']}")
                print(f"   email: {c['email']}")
    
    # opción 3: buscar un contacto por nombre
    elif opcion == "3":
        buscar = input("nombre a buscar: ")
        encontrado = False
        
        for c in contactos:
            if c['nombre'].lower() == buscar.lower():
                print(f"\n✓ contacto encontrado:")
                print(f"nombre: {c['nombre']}")
                print(f"teléfono: {c['telefono']}")
                print(f"email: {c['email']}")
                encontrado = True
                break
        
        if not encontrado:
            print("✗ contacto no encontrado")
    
    # opción 4: eliminar un contacto
    elif opcion == "4":
        buscar = input("nombre del contacto a eliminar: ")
        encontrado = False
        
        # buscamos el contacto en la lista
        for i, c in enumerate(contactos):
            if c['nombre'].lower() == buscar.lower():
                # lo eliminamos usando remove
                contactos.remove(c)
                print("✓ contacto eliminado")
                encontrado = True
                break
        
        if not encontrado:
            print("✗ contacto no encontrado")
    
    # opción 5: salir
    elif opcion == "5":
        print("¡hasta luego!")
        break