# guardar solo los numeros pares de la cantidad de numeros que quiera agrefgar el usuario

# crearnos una lista con varios números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("lista original:", numeros)

# hacer una lista vacia para pares
pares = []

# recorremos todos los números
for num in numeros:
    # verificamos si es par
    # los numeros son pares si al dividirlos entre 2 el residuo es 0
    # usamos % para obtener el residuo
    if num % 2 == 0:
        # si es par, lo agregamos a la lista de pares
        pares.append(num)

print("numeros pares:", pares)

# ahora con los numeros que meta el usuario
print("\nahora ingresa tus numeros:")
misnumeros = []
mispares = []

cantidad = int(input("cuantos numeros vas a ingresar? "))

for i in range(cantidad):
    num = int(input("ingresa un numero: "))
    misnumeros.append(num)
    
    # verificamos si es par mientras lo ingresamos y ya
    if num % 2 == 0:
        mispares.append(num)

print("\ntus numeros:", misnumeros)
print("los pares son:", mispares)
print("hay", len(mispares), "numeros pares")