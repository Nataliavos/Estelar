# calculadora con las 4 operaciones basicas

# pedir 2 numeritos
num1 = float(input("primer numero: "))
num2 = float(input("segundo numero: "))

# mostrar el menu de operaciones
print("\nque operacion vas a hacer")
print("1 sumar +")
print("2 restar -")
print("3 multiplicar *")
print("4 dividir /")

# pedir la opcion
opcion = input("elige opcion: ")

# definir las operaciones de la opcion que haya pedido el usuario
if opcion == "1":
    resultado = num1 + num2
    print(num1, "+", num2, "=", resultado)

elif opcion == "2":
    resultado = num1 - num2
    print(num1, "-", num2, "=", resultado)

elif opcion == "3":
    resultado = num1 * num2
    print(num1, "*", num2, "=", resultado)

elif opcion == "4":
    # verificar que no se pueda dividir entre 0 ylisto
    if num2 == 0:
        print("error: no se puede dividir entre cero")
    else:
        resultado = num1 / num2
        print(num1, "/", num2, "=", resultado)

else:
    print("opcion invalida")