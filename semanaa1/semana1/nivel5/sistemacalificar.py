# programa para calcular promedio de notas preguntamos cuántas notas va a ingresar
cantidad = int(input("¿cuántas notas vas a ingres "))

# creamos una lista vacía para guardar las notas
notas = []

# usamos for para pedir cada nota
for i in range(cantidad):
    # pedimos la nota y la convertimos a número decimal
    nota = float(input("ingresa una nota: "))
    # agregamos la nota a la lista
    notas.append(nota)

# calculamos el promedio
# sum() suma todos los números de la lista
# len() cuenta cuántos elementos hay
promedio = sum(notas) / len(notas)

# mostramos el promedio
print("tu promedio es:", promedio)

# verificamos si aprobó
if promedio >= 70:
    print("aprobaste")
else:
    print("reprobaste")

# mostramos todas las notas
print("tus notas fueron:", notas)