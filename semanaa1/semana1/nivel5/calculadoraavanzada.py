# calculadora con varias operaciones

while True:
    print("\n--- calculadora ---")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. potencia")
    print("6. salir")
    
    opcion = input("elige operacion: ")
    
    # si elige salir
    if opcion == "6":
        print("adios")
        break
    
    # para las otras opciones pedimos dos números
    # pedimos primer número
    num1 = float(input("primer numero: "))
    # pedimos segundo número
    num2 = float(input("segundo numero: "))
    
    # sumar
    if opcion == "1":
        resultado = num1 + num2
        print("resultado:", num1, "+", num2, "=", resultado)
    
    # restar
    elif opcion == "2":
        resultado = num1 - num2
        print("resultado:", num1, "-", num2, "=", resultado)
    
    # multiplicar
    elif opcion == "3":
        resultado = num1 * num2
        print("resultado:", num1, "x", num2, "=", resultado)
    
    # dividir
    elif opcion == "4":
        # verificamos que no divida entre cero
        if num2 == 0:
            print("no se puede dividir entre cero")
        else:
            resultado = num1 / num2
            print("resultado:", num1, "/", num2, "=", resultado)
    
    # potencia (num1 elevado a num2)
    elif opcion == "5":
        # usamos ** para potencia
        resultado = num1 ** num2
        print("resultado:", num1, "^", num2, "=", resultado)