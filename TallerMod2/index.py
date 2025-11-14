# Funcion para agregar producto
inventario =[] # Creamos un lista vacia para almacenar el inventario


print('-------------------------APLICACIÓN DE INVENTARIO-------------------------------------------')
def agregar_producto(): #------------------FUNCION PARA AGREGAR PRODUCTOS---------------------------#

    print('---------------AGREGAR PRODUCTO-------------------')
   
    nombre = input('INGRESA NOMBRE: ') # pedimos el nombre del producto
    while True: # ciclo while para validar que el valor ingresado sea un numero
        try:# validar que el valor ingresado sea numerico
         valor = int(input('INGRESA VALOR: '))# pedimos el valor del producto  
         break # detenemos si cuple la condicion
        except ValueError: # si no cumple la condicion
          print('ERROR: INGRESE UN VALOR NUMERICO VALIDO') # imprime mensaje de error
    while True: #  ciclo while para validar que el valor ingresado sea un numero
       try:# validar que el valor ingresado sea numerico
        cantidad = int(input('AGREGAR CANTIDAD: ')) # pedimos la cantidad del producto
        break# detenemos si cuple la condicion
       except ValueError: # si no cumple la condicion
            print('ERROR: INGRESE UN VALOR NUMERICO VALIDO') # imprime mensaje de error

    salir = input('PRECIONE (S) SI DECEA SALIR O (ENTER) PARA CONTINUAR AGREGANDO').lower() # opcion para salir o continuar agregando productos
    
    total = valor * cantidad # calculamos el total del producto (valor * cantidad)
  
  
    agregar ={              # creamos un diciionario para almacenar los valores ingresados para  luego mostrarlos
            'nombre':nombre,
            'valor': valor,
            'cantidad': cantidad,
            'total': total
        }
   
    

    inventario.append(agregar) # agregamos los productos a la lista (EL INVENTARIO)
    

    if salir == 's': # condicion para salir o continuar agregando productos
            menu()
    else:
         agregar_producto()
        # Detenemos el ciclo while para evitar que siga pidiendo productos

#-------------------- FUNCION PARA MOSTRARA INVENTARIO --------------------------#
def mostrar_inventario():
    print('------------------Mostrar Inventario.--------------------')
    if inventario == []: # verificamos si la lista del inventario esta vacia
       print('NO HAY PRODUCTOS EN EL INVENTARIO') # mensaje si no hay productos en el inventario
    else:
     for invent in inventario: # recorremos la lista del inventario para mostrar los productos agregados
      print(f'|NOMBRE: {invent["nombre"]}|VALOR: ${invent["valor"]}|CANTIDAD: {invent["cantidad"]}|TOTAL: {invent["total"]}|')  # mostramos los productos agregados de la lista de manera ordenada
      print('--------------------------------------------------------------------------')
    salida= input('PARA VOLVER AL MENU PRECIONA (S)').lower() # opcion para volver al menu
    if salida == 's': # condicion para volver al menu
     menu() # llamamos a la funcion menu para volver a ver el principal
    

# -------------------FUNCION PARA CALCULAR LAS ESTADISTICAS----------------------#
def calcular_estadisticas():
    print('--------------------ESTADISTICAS------------------------')
    if inventario == []:
       print('[NO HAY PRODUCTOS EN EL INVENTARIO') # mensaje si no hay productos en el inventario
    else:
     for item in inventario: # recorremos la lista del inventario para mostrar los productos agregados
        print(f'|EL TOTAL: {item["nombre"]} = {item["total"]} |') # mostramos el total de cada producto agregado

    totalidad = sum(item["total"] for item in inventario) # calculamos la suma total del inventario
    print(f'|SUMA TOTAL DEL INVENTARIO ${totalidad}|')# mostramos la suma total del inventario
    cantidad_productos = sum(item["cantidad"]for item in inventario)
    print(f'CANTIDAD TOTAL DE PRODUCTO: {cantidad_productos}')# mostramos la cantidad total de productos en el inventario
      
    print('----------------------------------------------------')
       
    salir = input('PARA VOLVER ATRAS PRESION (S)').lower() # opcion para volver al menu
    if salir == 's': # condicion para volver al menu
       menu() # llamamos a la funcion



def menu(): #--------------FUNCION PARA MOSTRAR EL MENU--------------------------#

    while True: # creamos  un ciclo while para mostrar el menu de opciones
        try:
            print('1:AGREGAR PRODUCTO.')
            print('----------------------------')
            print('2:MOSTRAR INVENTARIO.')
            print('----------------------------')
            print('3:CALCULAR ESTADISTICAS.')
            print('----------------------------')
            print('4:SALIR') # creamos una variable para salir
            print('----------------------------')
            opcion = int(input('INGRESE LA OPCIION QUE DECEA REALIZAR:'))
            break # Detenemos para evitar el bucle
        except ValueError:    
            print('Error Ingrese dato valido') # mensaje de error


    if opcion == 1: 
        agregar_producto() #-----------------LLAMAMOS A LA FUNCION PARA AGREGAR PRODUCTOS------------------#
        
    if opcion == 2:
        mostrar_inventario() #-----------------LLAMAMOS A LA FUNCION PARA MOSTRAR INVENTARIO------------------#

    if opcion == 3:
       calcular_estadisticas()#-----------------LLAMAMOS A LA FUNCION PARA CALCULAR ESTADISTICAS------------------#
    
    if opcion == 4:
        print('--------GRACIAS POR USAR NUESTRO INVENTARIO----------') # mensaje de despedida
        

menu()#-----------------LLAMAMOS A LA FUNCION MENU PARA INICIAR LA APLICACION DE INVENTARIO------------------#

