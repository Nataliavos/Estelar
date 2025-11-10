# encontrar el mayor y menor de tres números

# pedimos tres números
num1 = float(input("primer numero: "))
num2 = float(input("segundo numero: "))
num3 = float(input("tercer numero: "))

# encontramos el mayor
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

# encontramos el menor
if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print("\nel numero mayor es:", mayor)
print("el numero menor es:", menor)

# forma más fácil usando max() y min()
print("\n--- forma facil ---")
num1 = float(input("numero 1: "))
num2 = float(input("numero 2: "))
num3 = float(input("numero 3: "))

mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)

print("mayor:", mayor)
print("menor:", menor)

# versión que también ordena los tres
print("\n--- ordenados de menor a mayor ---")
num1 = float(input("numero 1: "))
num2 = float(input("numero 2: "))
num3 = float(input("numero 3: "))

# creamos una lista y la ordenamos
numeros = [num1, num2, num3]
numeros.sort()

print("ordenados:", numeros)
print("menor:", numeros[0])
print("medio:", numeros[1])
print("mayor:", numeros[2])