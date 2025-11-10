# crear una lista de frutas y mostrarla

# creamos una lista con algunas frutas
frutas = ["manzana", "pera", "uva", "sandia"]

# mostramos la lista completa
print("mi lista de frutas:", frutas)

# mostramos cuántas frutas hay
print("tengo", len(frutas), "frutas")

# mostramos cada fruta en una línea diferente
print("\nrecorriendo la lista:")
for fruta in frutas:
    print("- ", fruta)

# accedemos a frutas por posición
print("\nla primera fruta es:", frutas[0])
print("la última fruta es:", frutas[-1])