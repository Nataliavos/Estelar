a = int(input("Ingresa el primer número (A): "))
b = int(input("Ingresa el segundo número (B): "))
c = int(input("Ingresa el tercer número (C): "))

# CÓDIGO PARA ENCONTRAR EL MAYOR

if a >= b and a >= c:
    mayor = a
elif b >= a and b >= c:
    mayor = b
else: 
    mayor = c

# CÓDIGO PARA ENCONTRAR EL MENOR

if a <= b and a <= c:
    menor = a
elif b <= a and b <= c:
    menor = b
else: 
    menor = c

print(f"\nEl número mayor es: {mayor}")
print(f"El número menor es: {menor}")