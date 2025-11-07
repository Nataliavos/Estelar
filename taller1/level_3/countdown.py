'''Contador regresivo con while.'''

# solicitamos el número inicial al usuario
n=int(input("Ingrese un número para iniciar la cuenta regresiva: "))

# Ajustamos n para que el conteo incluya el número ingresado
n = n + 1

# Mientras n sea mayor o igual a 1, seguimos restando 1 e imprimiendo el valor
# n >= 2 para que el conteo llegue hasta 1. Para llegue hasta cero sería n >= 1
while n >= 2:
    # va restando 1 a n en cada iteración
    n -= 1

    print(n)
print("¡Despegue!")
