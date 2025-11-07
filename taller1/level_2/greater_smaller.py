'''Comparador de tres números: mayor y menor.'''

# Solicitamos al usuario que ingrese los datos (números) y guardamos cada uno en una variable
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
num3 = int(input("Ingrese el otro número: "))

# Creamos variables para almacenar el mayor y el menor y las igualamos al primer número ingresado
greater = num1
smaller = num1

# COmparamos cada número que ingrese con el valor guardado en la variable (mayor o menor)
if num2 > greater :
    greater = num2
if num3 > greater :
    greater = num3
    
if num2 < smaller :
    smaller = num2
if num3 < smaller :
    smaller = num3

# Imprimimos el valor final de las variables (mayor y menor)
print(f"El número mayor es: {greater}")
print(f"El número menor es: {smaller}")