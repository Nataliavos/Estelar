#Calculadora básica con +, -, *, /.

print("=== CALCULADORA ===")

# Inicializamos result para evitar errores si no se genera un resultado
result = None #Evita errores si no se genera resultado

# Mostramos el menú y pedimos opción
option = int(input("Elija la operación que desea realizar: \n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir"))

# Opción salir
if option == 5 :
    print("¡Hasta la próxima!")

# Operaciones: suma, resta, multiplicación
elif option >= 1 and option <= 3 :

    while True:
        try:
            num1 = int(input("Ingrese un número:" ))
            break  # Si no hay error, salimos del ciclo
        except ValueError:
            print("Error. Ingrese un número válido.")

    while True:
        try:
            num2 = int(input("Ingrese otro número:" ))
            break  # Si no hay error, salimos del ciclo
        except ValueError:
            print("Error. Ingrese un número válido.")

# División
elif option == 4 :

    while True:
        try:
            num1 = int(input("Ingrese un número:" ))
            break  # Si no hay error, salimos del ciclo
        except ValueError:
            print("Error. Ingrese un número válido.")

    while True:
        try:
            num2 = int(input("Ingrese otro número:" ))
            if num2 != 0 :
                break  # Solo salimos del ciclo si NO es cero
            else:
                print("Error. No se puede dividir entre cero")
                
        except ValueError:
            print("Error. Ingrese un número válido.")
else:
    print("La opción ingresada no es válida.")
 
# Operaiones matemáticas según la opción elegida
if option == 1 :
        result = num1 + num2
elif option == 2 :
    result = num1 - num2
elif option == 3 :
    result = num1 * num2
elif option == 4 :
    result = num1 / num2

# Mostrar el resultado solo si existe
if result is not None :
    print(f"El resultado es: {result}")