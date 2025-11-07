num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operador = input("Ingresa el operador (+, -, *, /): ")
resultado = 0

if operador == '+':
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
elif operador == '-':
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
elif operador == '*':
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operador == '/':
    
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("¡Error! No se puede dividir por cero.")
else:
    print("Operador no válido. Por favor, usa +, -, *, o /.")