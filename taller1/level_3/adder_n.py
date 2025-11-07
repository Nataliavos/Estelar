'''Sumatoria del 1 al n.'''

n = int(input("Ingrese un número: "))

cont = 0

for i in range (1, n+1) :
    cont += i

print(f"La sumatoria de 1 a {n} es igual a {cont}")

