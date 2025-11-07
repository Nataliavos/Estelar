'''Sumatoria del 1 al n.'''
# solicitamos datos y pasamso a tipo entero
n = int(input("Ingrese un número: "))

# inicializamos el contador
cont = 0

# recorremos los números del 1 al n y los vamos sumando
for i in range (1, n+1) :
    cont += i

# imprimimos el resultado
print(f"La sumatoria de 1 a {n} es igual a {cont}")

