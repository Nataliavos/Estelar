marcascarros = []

print("Por favor, ingresa 3 marcas de carros:")


for i in range(3):
    
    marca = input(f"Marca de carro #{i + 1}: ")
    
    marcascarros.append(marca)


print("\nLas marcas de carros que ingresaste son:")


print(marcascarros)


print("\n¿Deseas quitar alguna marca de la lista?")
marcaeliminar = input("Ingresa el nombre exacto de la marca a quitar (o presiona Enter para omitir): ")

if marcaeliminar in marcascarros:
    marcascarros.remove(marcaeliminar)
    print(f"'{marcaeliminar}' eliminada.")
    print("Nueva lista:", marcascarros)
elif marcaeliminar == "":
    print("No se eliminó ninguna marca.")
else:
    print(f"'{marcaeliminar}' no se encontró en la lista.")
    
    
    
sdsdasdad