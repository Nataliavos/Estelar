# carrito de compras simple

# listas para guardar nombres y precios
productos = []
precios = []

# usamos while True para repetir el menú
while True:
    print("\n--- menu ---")
    print("1. agregar producto")
    print("2. ver carrito")
    print("3. calcular total")
    print("4. salir")
    
    # pedimos que elija una opción
    opcion = input("elige opcion: ")
    
    # si elige 1, agregamos producto
    if opcion == "1":
        nombre = input("nombre del producto: ")
        precio = float(input("precio: "))
        
        # agregamos a las listas usando append()
        productos.append(nombre)
        precios.append(precio)
        
        print("producto agregado")
    
    # si elige 2, mostramos el carrito
    elif opcion == "2":
        print("\n--- tu carrito ---")
        
        # verificamos si hay productos
        if len(productos) == 0:
            print("carrito vacio")
        else:
            # usamos for para recorrer las listas
            for i in range(len(productos)):
                # mostramos cada producto con su precio
                print(productos[i], "- $", precios[i])
    
    # si elige 3, sumamos todo
    elif opcion == "3":
        # creamos variable para sumar
        total = 0
        
        # recorremos los precios y los sumamos
        for precio in precios:
            total = total + precio
        
        print("total a pagar: $", total)
    
    # si elige 4, salimos del programa
    elif opcion == "4":
        print("adios")
        break  # esto termina el while