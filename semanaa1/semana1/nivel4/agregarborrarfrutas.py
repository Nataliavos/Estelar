# practicar agregar y eliminar elementos de una lista

# una lista vacia
frutas = []

# agregar las frutas con un append()
print("agregando frutas...")
frutas.append("manzana")
print("agregué manzana:", frutas)

frutas.append("pera")
print("agregué pera:", frutas)

frutas.append("uva")
print("agregué uva:", frutas)

frutas.append("sandia")
print("agregué sandia:", frutas)

print("\nlista completa:", frutas)
print("total de frutas:", len(frutas))

# eliminamos una fruta con remove()
# remove() elimina el elemento por su nombre
print("\neliminando pera...")
frutas.remove("pera")
print("lista actual:", frutas)

# eliminamos con pop()
# pop() elimina el último elemento
print("\neliminando el último elemento...")
fruta_eliminada = frutas.pop()
print("eliminé:", fruta_eliminada)
print("lista actual:", frutas)

# eliminamos por posición con pop(posicion)
print("\neliminando la primera fruta...")
frutas.pop(0)
print("lista final:", frutas)