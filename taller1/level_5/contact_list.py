'''Agenda de contactos (lista de diccionarios).'''

# Creamos un diccionario vacío para almacenar los contactos
contact_list = {}


# ===== Función para crear un nuevo contacto =====
def createContact():
    print("Módulo Crear contacto")

    # Pedimos al usuario el número del contacto
    num = input("Ingrese número-->")

    # Validamos que el número sea solo numérico
    while not num.isnumeric():
        print("Dato inválido. Ingresa solo número")
        num = input("Ingrese número->")

    # Solicitamos nombre y apellido
    name = input("Ingresa el nombre-->")
    lastname = input("Ingrese Apellido->")

    # Guardamos el contacto en el diccionario principal
    # Usamos el número como clave
    contact_list[num] = {
        "name": name,
        "lastname": lastname
    }

    # Confirmamos la creación del contacto
    print("Contacto registrado con éxito")
    print(contact_list)  # Mostramos la agenda actualizada


# ===== Función para buscar un contacto =====
def searchContact():
    print("Módulo Buscar contacto")

    # Si no hay contactos, mostramos un mensaje
    if not contact_list:
        print("No hay contactos")
        return
    
    print("Buscar contacto por número")

    # Pedimos el número a buscar
    num = input("Ingresa número a buscar-->")

    # Validamos que sea un número válido
    while not num.isnumeric():
        print("Dato inválido. Ingresa solo número")
        num = input("Ingresa número a buscar-->")

    # Si el número está en la agenda, lo mostramos
    if num in contact_list:
        numSearched = contact_list[num]
        print(f"Número -> {num} | Nombre -> {numSearched['name']} | Apellido -> {numSearched['lastname']}")
    else:
        # Si no existe, mostramos mensaje
        print("El contacto no existe")


# ===== Función para actualizar datos de un contacto =====
def updateContact():
    print("Módulo Actualizar")

    # Si la agenda está vacía, mostramos mensaje
    if not contact_list:
        print("No hay contactos")
        return
    
    # Pedimos el número del contacto a actualizar
    num = input("Ingrese número-->")

    # Validamos que el número sea numérico
    while not num.isnumeric():
        print("Dato inválido")
        num = input("Ingrese número-->")

    # Si el número existe, entramos al módulo de actualización
    if num in contact_list:
        update = contact_list[num]  # Guardamos los datos actuales del contacto
        print(update)  # Mostramos la información antes de editar

        print("¿Qué deseas actualizar del contacto?")
        print("1) Actualizar número\n2) Actualizar nombre\n3) Actualizar apellido")

        # Solicitamos una opción
        option = input("Ingrese una opción-->")

        # Usamos match para decidir qué actualizar
        match option:
            case "1":
                print("Modificar número")
                new_num = input("Ingrese nuevo número->").strip()
                # validamos que sea numérico
                while not new_num.isnumeric():
                    print("Dato inválido. Ingresa solo números.")
                    new_num = input("Ingrese nuevo número->").strip()
                
                # validamos no exista ya en la agenda
                if new_num in contact_list:
                    print("Ese número ya existe en la agenda. No se puede duplicar.")
                    return
                # Movemos el contacto a la nueva clave y borramos la vieja
                contact_list[new_num] = contact_list.pop(num)
                
                # mostramos confirmación e imprimimos la agenda actualizada
                print("Número actualizado con éxito")
                print(contact_list)
              
            case "2":
                print("Modificar nombre")
                update['name'] = input("Nuevo nombre->")
                print(contact_list)
            case "3":
                print("Modificar apellido")
                update['lastname'] = input("Ingrese nuevo apellido->")
                print(contact_list)
            case _:
                print("Opción inválida")


# ===== Función para eliminar un contacto =====
def deleteContact():
    print("Módulo Eliminar")

    # Si la agenda está vacía, mostramos mensaje
    if not contact_list:
        print("Agenda vacía")
        return
    
    # Pedimos el número a eliminar
    num = input("Ingrese contacto a eliminar->")

    # Validamos que el número sea numérico
    while not num.isnumeric():
        print("Dato inválido")
        num = input("Ingrese contacto a eliminar->")

    # Si el número existe, lo eliminamos
    if num in contact_list:
        contact_list.pop(num)  # Eliminamos el contacto del diccionario
        print("Se eliminó con éxito")
        print(contact_list)
    else:
        # Si el número no existe, mostramos mensaje
        print("Ese contacto no existe")


# ===== Menú principal =====
while True:
    # Mostramos el menú con las opciones
    print("Bienvenido a la agenda")
    print("1) Crear contacto\n2) Buscar contacto\n3) Actualizar contacto\n4) Eliminar contacto\n5) Salir de agenda")

    # Solicitamos una opción al usuario
    option = input("Ingresa opción->")

    # Usamos match para ejecutar la función correspondiente
    match option:
        case "1":
            createContact()
        case "2":
            searchContact()
        case "3":
            updateContact()
        case "4":
            deleteContact()
        case "5":
            break  # Terminamos el programa
