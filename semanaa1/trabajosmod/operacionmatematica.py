# para calcular el costo total del inventario


print("---calculo de costo total---\n")
# pedimos los datos del producto
nombre = input("nombre del producto: ")
precio = float(input("precio: "))
cantidad = int(input("cantidad: "))
# creamos la variable del costo total el producto

# hacer la variable y definirla con una operacion para imprimirla al final 
costototal = precio * cantidad

# mostramos el resultado
print("\n---resultado---")
print("producto:", nombre)
print("precio: $", precio)
print("cantidad:", cantidad)
print("costo total: $", costototal)