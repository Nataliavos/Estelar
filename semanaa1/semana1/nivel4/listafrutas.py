#hacer una lista de frutas y mostrarselas al usuarui

# creamos una lista con fruticas
frutas = ["manzana", "pera", "uva", "sandia"]

# mostramos la lista completa de las fruytas
print("mi lista de frutas:", frutas)

# mostrar cuantas frutas tenemos
print("tengo", len(frutas), "frutas")

# mostrar una fruta en cada linea distinta
print("\nrecorrer la lista:")
for fruta in frutas:
    print("- ", fruta)

# accedemos a frutas por posición
print("\nla primera fruta es:", frutas[0])
print("la última fruta es:", frutas[-1])