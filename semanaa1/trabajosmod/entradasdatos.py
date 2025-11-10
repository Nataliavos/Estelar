

# programa para registrar productos con validacion de datos



print("---registro de producto en el inventario---\n")


# pedimos el nombre del producto con letras
nombre = input("nombre del producto: ")

# pedimos el precio y validamos que sea un numerito
while True:
    preciotexto = input("precio del producto: ")
    
    # convertir los numeros a decimal
    # verificamos que tenga solo números y punto decimal
    if preciotexto.replace(".", "", 1).isdigit():
        precio = float(preciotexto)
        
        # mirar bien que sea positivo
        if precio > 0:
            break  
        else:
            print("error: el precio debe ser mayor a cero\n")
    else:
        print("error: ingresa un precio valido con numeros\n")

# pedir cantidad y ver q sea un numero entero
while True:
    cantidadtexto = input("cantidad en stock: ")
    
    # verificamos que sea solo números
    if cantidadtexto.isdigit():
        cantidad = int(cantidadtexto)
        
        # verificamos que sea positivo
        if cantidad > 0:
            break  
        else:
            print("la cantidad debe ser mayor a 0\n")
    else:
        print("ingresa un numero entero valido\n")

# calculamos el costo total del inventario
costototal = precio * cantidad
# mostramos los datos registrados
print("\n---producto registrado corretamente---")
print("nombre:", nombre)
print("precio: $", precio)
print("cantidad:", cantidad, "unidades")
print("costo total en inventario: $", costototal)