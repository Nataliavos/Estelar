
inventario = { # creo un inventario con los productos 
        'arroz' : {'precio': 1200, 'stok': 10},
        'leche' : {'precio': 1000, 'stok': 10},
        'huevos' : {'precio': 1400, 'stok': 10},
        'carne' : {'precio': 4000, 'stok': 10},
        'jugo' : {'precio': 1100, 'stok': 10},

    }

carrito ={} # creo la variable del carrito donde se va a guardar
total=0 # variable para almacenar el  total de las compras
def actualizar(): # creo una funcion para poderla llamar mas adelante y no repetir codigo.
    total = 0
    for nombre, datos in carrito.items(): # recorro con for y doy clave y valor a los productos 
       print(f" {nombre}:{datos['cantidad']} x {datos['precio']} = {datos['subtotal']} ") # imrpimo los productos con su valor 
       total += datos['subtotal'] # imrpimo la suma del subtotal 
    print(f' Total a pagar {total}') # imprimo el total de todos los productos

while True: # creo un ciclo  para que me epreegunte los productos y cantidades
       
    producto = input('ingrese el nombre del producto y s para terminar / e para eliminar').lower() # recivo el nombre del producto
    if producto == 's': # salida del ingreso de los productos
        break

    if producto == 'e':
       eliminar = input('que producto decea eliminar?').lower()
       if eliminar in carrito:
        del carrito[eliminar]
        
       else:

        print('el producto no esta')
       actualizar()  # llamo la funcion actualizar carrito
       continue

    if producto not in inventario:  # si el producto no esta en el inventario imprimo mensaje
        print('no existe')
        continue # continua el programa

    cantidad = int(input('ingrese cantidad')) # recive la cantidad 

    if cantidad > inventario[producto]['stok']: # ealua que la cantidad no sea mayor al stok
       print('no hay suficiente stok')
       continue # continua el programa

    precio = inventario[producto]['precio'] # creo una variable precio para traer el valor del producto
    subtotal = precio * cantidad # multiplico la cantidad ingresada por el valor del producto
    
    if producto in carrito: # verificacion de si el producto exite 
        carrito[producto]['cantidad'] += cantidad # si si le sumamos la cantida ingresada
        carrito[producto]['subtotal'] = carrito[producto]['cantidad']*precio # mantenmos el mismo nobre y le aumenta el valor del producto
    else:
     carrito[producto]={ # creo un diccionario donde voy almacenar las cantidades y precio y valor total en caso de que no se haya agregado
        'cantidad': cantidad,
        'precio': precio,
        'subtotal': subtotal
     }

    actualizar() # llamo la funcion actualizar carrito
