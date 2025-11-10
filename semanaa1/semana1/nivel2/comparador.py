# encontrar el mayor y menor de tres números y pedimos tres numeritos

num1 = float(input("numero 1 "))
num2 = float(input("numero 2 "))
num3 = float(input("numero 3 "))

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


# creamos una lista y la ordenamos
numeros = [num1, num2, num3]
numeros.sort()

print("ordenados:", numeros)
print("menor:", numeros[0])
print("medio:", numeros[1])
print("mayor:", numeros[2])