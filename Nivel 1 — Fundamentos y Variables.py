# 1. Hola usuario

nombre = input("Por favor, introduce tu nombre: ")
print("¡Hola, " + nombre + "!")

edad = input("Por favor, introduce tu edad: ")
print("Tienes " + edad + " años.")

print("Hola " + nombre + ", tienes " + edad + " años.")

print("---------------------------------")

# 2. Suma de dos números.

print("\n--- Suma de dos números ---")

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
suma = num1 + num2

print(f"La suma de {num1} y {num2} es: {suma}")

print("---------------------------------")


# 3. Área del triángulo.

print("\n--- Área del triángulo ---")

base = float(input("Introduce la base del triángulo: "))
altura = float(input("Introduce la altura del triángulo: "))
area = (base * altura) / 2

print(f"Un triángulo con base {base} y altura {altura} tiene un área de: {area}")

print("---------------------------------")

# 4. Conversión de grados Celsius a Fahrenheit.

celsius = float(input("Introduce la temperatura en grados Celsius (°C): "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C es igual a {fahrenheit}°F.")
