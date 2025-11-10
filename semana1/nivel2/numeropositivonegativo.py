# verificar si un número es positivo, negativo o cero

# pedimos un número
numero = float(input("ingresa un numero: "))

# verificamos con if, elif, else
if numero > 0:
    print("el numero es positivo")
elif numero < 0:
    print("el numero es negativo")
else:
    print("el numero es cero")