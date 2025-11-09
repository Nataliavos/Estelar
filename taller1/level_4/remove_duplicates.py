'''Eliminar duplicados.'''

print("====== FORMA 1 USANDO UN SET ======") 
# creamo una lista con elementos duplicados
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 8, 5]
# convertimos la lista a un set para eliminar duplicados
unique_numbers = set(numbers)
# convertimos el set de nuevo a una lista
unique_numbers = list(unique_numbers)
# mostramos la lista sin duplicados
print(f"Lista inicial --> {numbers}\nLista sin duplicados --> {unique_numbers}")


print("====== FORMA 2 USANDO UN CICLO ======")
# creamo una lista con elementos duplicados
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 8, 5]
# creamos una lista vacía para guardar los elementos únicos
unique_numbers = []
# recorremos cada número en la lista original
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

# mostramos la lista sin duplicados
print(f"Lista inicial --> {numbers}\nLista sin duplicados --> {unique_numbers}")
