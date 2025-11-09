'''Lista de números y promedio.'''

numbers = []

while True :
    # solicitamos la cantidad de números a ingresar
    num_count = input("¿Cuántos números deseas ingresar? ").strip()

    # primero valido que la entrada sea numérica
    if not num_count.isnumeric() :
        print("Por favor ingrese un número válido.")
        continue # volvemos a pedir el dato
    
    # convertimos la entrada a entero
    num_count = int(num_count)

    # ahora validamos que la entrada sea mayor que cero
    if num_count <= 0:
        print("El número debe ser mayor que cero.")
        continue # volvemos a pedir el dato
    
    # si pasa todas las validaciones, salimos del ciclo
    break 

# mientras el numero de elementos en la lista sea menor a la cantidad solicitada
while len(numbers) < num_count :
    # solicitamos el número
    num = input(f"Ingrese un número -->").strip()

    # validamos que la entrada sea numérica
    if not num.isnumeric() :
        print("Por favor ingrese un número válido.")
        continue # volvemos a pedir el dato
    
    # convertimos la entrada a entero
    num = int(num)

    # ahora validamos que la entrada sea mayor o igual a cero
    if num < 0:
        print("El número debe ser positivo.")
        continue # volvemos a pedir el dato

    # si pasa todas las validaciones, agregamos el número a la lista
    numbers.append(num)

# calculamos el promedio. Con round() redondeamos el resultado a 2 decimales 
average = round(sum(numbers) / num_count, 2)

# mostramos el resultado
print(f"El promedio de los números {numbers} es --> {average}")