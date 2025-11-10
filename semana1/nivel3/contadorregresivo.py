# contar hacia atrás desde un número hasta 0

# pedimos desde qué número empezar
inicio = int(input("desde que numero quieres contar? "))

print("\ncontando regresivo:")

# usamos while para contar hacia atrás
while inicio >= 0:
    print(inicio)
    # restamos 1 en cada vuelta
    inicio = inicio - 1

print("despegue!")

# otra versión con for
print("\n--- con for ---")
inicio = int(input("desde que numero? "))

# range con paso negativo
for i in range(inicio, -1, -1):
    print(i)

print("despegue!")