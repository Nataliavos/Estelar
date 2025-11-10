# pedir números y calcular el promedio de alguienb
numeros = []
# creamos una lista vacía

# pedimos cuantos numeros va a meter
cantidad = int(input("cuantos numeros vas a ingresar"))

# usamos for para pedir cada número
for i in range(cantidad):
    # pedimos el numero
    num = float(input("ingresa un numero: "))
    # ylo agregamos a la lista
    numeros.append(num)

# mostramos la lista
print("\ntus numeros:", numeros)

# calaculamos el promedio
# sum() suma los numeros, todos
# len() cuenta cuantos numeros es que hay
suma = sum(numeros)
promedio = suma / len(numeros)

print("la suma es:", suma)
print("el promedio es:", promedio)

# ver el mayor y e menor
mayor = max(numeros)
menor = min(numeros)

print("el numero mayor es:", mayor)
print("el numero menor es:", menor)