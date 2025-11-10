
# mostrar los datos del produc

print("--- registro de producto ---\n")


# pedimos los datos
nombre = input("nombre del producto: ")
precio = float(input("precio: "))
cantidad = int(input("cantidad: "))


# calcular todo el costo de la operacion
costo_total = precio * cantidad


# mostrar el resultado con barritas 
print("\n--- resultado ---")
print("Producto:", nombre, "| Precio:", precio, "| Cantidad:", cantidad, "| Total:", costo_total)