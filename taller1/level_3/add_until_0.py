'''Sumar hasta que el usuario escriba 0.'''

# inicializamos la suma en 0
suma = 0

print("=== SUMA DE NÚMEROS ===")

while True:
    # pedimos al usuario que ingrese un número
    numero = input("Ingresa un número (0 para terminar) --> ")

    # si el usuario ingresa 0, salimos del bucle
    if numero == "0":
        break

    # validamos que la entrada sea un número
    if not numero.isnumeric():
        print("Por favor, ingresa un número válido.")
        continue

    # convertimos la entrada a entero y la sumamos
    suma += int(numero)

# mostramos el resultado
print(f"La suma de los números ingresados es --> {suma}")
