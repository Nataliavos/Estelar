'''Validación de datos con condicionales:

    Crea un menú que pregunte al usuario qué acción desea realizar:
        Agregar producto
        Mostrar inventario
        Calcular estadísticas
        Salir
    Usa condicionales if, elif y else para procesar la opción elegida.
    Si el usuario ingresa una opción inválida, muestra un mensaje de error y pide nuevamente la entrada.
'''
inventory = []

# ------- Función Agregar Producto ------
def add_product():
    name_product = input("Ingrese nombre del producto: ")
    quantity_product = input("Ingrese cantidad: ")
    try:
        quantity_product = int(quantity_product)
    except ValueError:
        print("Ingrese un número válido.")
        return
        
    if quantity_product <= 0:
        print("Ingrese una cantidad válida.")
        
    price_product = input("Ingrese el precio: ")
    
    inventory.append({"name" : name_product, "quantity" : quantity_product, "price" : price_product})
    print("Producto ingresado con éxito.")
    
    for inv in inventory:
        print(f"Producto: {inv['name']} | Cantidad: {inv['quantity']} | Precio: {inv['price']}")
    
    #print(f"{inventory}")
    
    
    



# ------------- MENU PRINCIPAL --------------

while True:
    # mostramos el menú de opciones
    print("===== INVENTARIO =====")
    print("1) Agregar Producto\n2) Mostrar Inventario\n3) Calcular Estadísticas\n4) Reportes (aprobados/reprobados)\n5) Salir")

    # solicitamos entrada
    option=input("\nIngresa una opción ->").strip()

    # validamos que la entrada sea numérica y esté dentro del rango de opciones
    if not option.isnumeric() or option not in ["1", "2", "3", "4"]:
        print("Elija una opción válida.")
        continue # volvemos solicitar entrada

    # convertimos la entrada a entero
    option = int(option)

    # usamos match para las opciones del menú. Definimos las funciones fuera del match para mayor claridad.
    # ejecutamos la función correspondiente según la opción seleccionada
    match option:
        
        case 1:
            add_product()
        case 2:
            show_inventory()
        case 3:
            calculate_statistics()
        case 4:
            print("¡Hasta la próxima!")
            break # salimos del bucle y terminamos el programa