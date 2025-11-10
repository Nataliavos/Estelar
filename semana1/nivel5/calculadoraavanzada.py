# calculadora usando funciones (cada operación es una función)

# función para sumar
def sumar(a, b):
    return a + b

# función para restar
def restar(a, b):
    return a - b

# función para multiplicar
def multiplicar(a, b):
    return a * b

# función para dividir
def dividir(a, b):
    # verificamos que no divida entre cero
    if b == 0:
        return "error: no se puede dividir entre cero"
    return a / b

# función para calcular potencia
def potencia(a, b):
    return a ** b

# programa principal
while True:
    print("\n--- calculadora ---")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. potencia")
    print("6. salir")
    
    opcion = input("elige una opción: ")
    
    # si elige salir, terminamos el programa
    if opcion == "6":
        print("¡adiós!")
        break
    
    # para las demás opciones, pedimos dos números
    if opcion in ["1", "2", "3", "4", "5"]:
        num1 = float(input("primer número: "))
        num2 = float(input("segundo número: "))
        
        # según la opción, llamamos a la función correspondiente
        if opcion == "1":
            resultado = sumar(num1, num2)
            print(f"resultado: {num1} + {num2} = {resultado}")
        
        elif opcion == "2":
            resultado = restar(num1, num2)
            print(f"resultado: {num1} - {num2} = {resultado}")
        
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
            print(f"resultado: {num1} × {num2} = {resultado}")
        
        elif opcion == "4":
            resultado = dividir(num1, num2)
            print(f"resultado: {num1} ÷ {num2} = {resultado}")
        
        elif opcion == "5":
            resultado = potencia(num1, num2)
            print(f"resultado: {num1} ^ {num2} = {resultado}")