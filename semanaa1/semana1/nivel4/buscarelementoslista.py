# buscar las fruta en la lista

# crear una lista de frutas
frutas = ["manzana", "pera", "uva", "sandia", "naranja"]

print("mis frutas:", frutas)

# pedimos al usuario que f ruta quierebuscar
buscar = input("\nque fruta queres buscar ")

# buscamos con if y in
# in es pa mirar si un objeto esta en una lista
if buscar in frutas:
    print("si tengo", buscar)
else:
    print("no tengo", buscar)

