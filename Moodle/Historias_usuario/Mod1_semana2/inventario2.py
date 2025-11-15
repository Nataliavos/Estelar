'''
Este programa implementa un sistema sencillo de gestión de inventario en consola.
Permite agregar productos con validación de datos, mostrar el inventario registrado
y generar un reporte con estadísticas como el valor total por producto y del inventario.
El menú principal guía al usuario a través de las diferentes opciones disponibles.
'''

# Lista para almacenar los productos del inventario
inventory = []

# Variables para diseño de la tabla
azul = "\033[34m" # color azul
reset = "\033[0m" # reset color
header = f"{azul}{'\nID':<15}{'PRODUCTO':<15}{'PRECIO':<15}{'CANTIDAD':<15}{reset}" # encabezado de tabla
line = f"{'-' * len(header)}" # línea separadora

# ------- AGREGAR PRODUCTO ------
def add_product():

    # Asignamos un ID automático a cada producto
    id_product = len(inventory) + 1

    # Solicitamos nombre del producto y validamos que no esté vacío
    name = input("Ingrese nombre del producto: ")
    while name == "":
        name = input("Ingrese un nombre válido: ")

    # Solicitamos precio y validamos que sea numérico, mayor o igual a 0 y no esté vacío
    price = input("Ingrese precio: ")

    while not price.replace('.', '', 1).isnumeric() or float(price) < 0 or price == "":
        price = input("Ingrese un precio válido: ")
    # Si es válido convertimos a float
    price = float(price)

    # Solicitamos cantidad y validamos que sea numérico, mayor a 0 y no esté vacío
    quantity = input("Ingrese cantidad: ")

    while not quantity.isnumeric() or int(quantity) <= 0 or quantity == "":
        quantity = input("Ingrese una cantidad válida: ")
    # Si es válido convertimos a int
    quantity = int(quantity)

    # Agregamos el producto al inventario
    inventory.append({"id_product" : id_product, "name" : name, "price" : price, "quantity" : quantity})

    # Imprimimos confirmación y encabezado de tabla
    print("\nProducto ingresado con éxito.")
    print(f"{azul}{header}")
    print(line)

    last_product = inventory[-1] # obtenemos el último producto agregado
    # Imprimimos el último producto agregado
    print(f'{last_product["id_product"]:<15}{last_product["name"]:<15}{last_product["price"]:<15}{last_product["quantity"]:<15}\n')


# ------- MOSTRAR INVENTARIO ------
def show_inventory():

    # Verificamos si el inventario está vacío
    if len(inventory) == 0:
        print("No hay productos en el inventario.\n")
        return
    
    # Imprimimos encabezado de tabla y línea separadora
    print(f"{azul}{header}")
    print(line)

    # Recorremos el inventario e imprimimos cada producto
    for inv in inventory:
       print(f'{inv["id_product"]:<15}{inv["name"]:<15}{inv["price"]:<15}{inv["quantity"]:<15}') 


# ------- CALCULAR ESTADÍSTICAS -------
def calculate_statistics():
    # Verificamos si el inventario está vacío
    if len(inventory) == 0:
        print("No hay productos en el inventario.\n")
        return
    
    print(f"{azul}{'\nPRODUCTO':<20}{'VALOR TOTAL':<20}{reset}")
    print('-' * 40)

    # Calculamos valor total del inventario
    total_value = 0  # Inicializamos acumulador
    # Multiplica precio por cantidad y el resultado se suma al acumulador (total_value) en cada iteración
    for inv in inventory: 
        total_value += inv["price"] * inv["quantity"] 

    # Imprimimos resultados
    for inv in inventory:
        value_per_product = inv["price"] * inv["quantity"]
        print(f'{inv["name"]:<20}{value_per_product:<20.2f}')

    print(f"\nCantidad total de productos: {len(inventory)}")
    print(f"Valor total del inventario: {total_value:.2f}\n") # mostramos valor total con 2 decimales
    

# ------- MENU PRINCIPAL -------
while True:
    # mostramos el menú de opciones
    print("\n======== MENÚ PRINCIPAL ========")
    print("1) Agregar Producto\n2) Mostrar Inventario\n3) Mostrar reporte\n4) Salir")

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
            print("Saliendo del programa...")
            break # salimos del bucle y terminamos el programa