# sumar todos los números del 1 hasta un número que diga el usuario

print("\n--- sumar igualando a ceroo")
n = int(input("ingresa un numero: "))
suma = 0

for i in range(1, n + 1):
    suma = suma + i

print("la suma es:", suma)