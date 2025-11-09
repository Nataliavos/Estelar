'''Números pares: guardar solo los pares.'''

even_numbers = []

while True:
    # solicitamos el número al usuario
    num = input("Ingrese el número que desea guardar. Para salir ingrese 0 -->").strip()

    # validamos que la entrada sea numérica
    if not num.isnumeric() :
        print("Por favor ingrese un número válido.")
        continue # volvemos a pedir el dato

    # convertimos la entrada a entero
    num = int(num)

    # si el usuario ingresa 0, salimos del ciclo
    if num == 0:
        break
    elif num % 2 == 0:
        even_numbers.append(num)

# mostramos los números pares guardados
print(f"Números pares guardados: {even_numbers}")
