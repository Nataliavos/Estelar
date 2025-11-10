# mostrar la tabla de multiplicar de un número

# pedir el numero
numero = int(input("de que numero quieres ver la tabla de multimplicar"))

print("\ntabla del", numero, ":")

# multiplicamos del 1 al 10
for i in range(1, 11):
    # calculamos el resultado
    resultado = numero * i
    # mostramos la operación
    print(numero, "x", i, "=", resultado)

