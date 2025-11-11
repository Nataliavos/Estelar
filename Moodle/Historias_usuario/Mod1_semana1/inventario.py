
# solicitamos al usuario nombre del producto
name_product = input("Ingrese nombre del producto: ").lower()

# solicitamos al usuario cantidad del producto
quantity = input("Ingrese cantidad: ")

# Validamos que cantidad sea numérico
while not quantity.isnumeric():
    print("Ingrese un número válido para la cantidad.")
    quantity = input("Ingrese cantidad: ")
# convertimos a entero la cantidad
quantity = int(quantity)

# solicitamos al usuario precio del producto
price = input("Ingrese precio del producto: ")

# Validamos que precio sea numérico, permitiendo decimales
while not price.replace('.', '', 1).isnumeric():
    print("Ingrese un número válido para el precio.")
    price = input("Ingrese precio del producto: ")

# convertimos a flotante el precio
price = float(price)

# calculamos el valor total y lo almacenamos en una variable
total_value = quantity * price

# mostramos el inventario ingresado
print(f"Producto: {name_product} | Cantidad: {quantity} | Precio unitario: ${price:.2f} | Valor total: ${total_value:.2f}")