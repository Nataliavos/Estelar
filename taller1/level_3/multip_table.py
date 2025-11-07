'''Tabla de multiplicar.'''

# Solicitamos el número al usuario
num = int(input("Ingrese un número para ver su tabla de multiplicar: "))

# Inicializamos el iterador
i = 0

# con un for aseguramos que se repita la acción (multiplicar) 10 veces
for i in range (0, 10):
    # El iterador sumaŕa 1 cada vez que se repita el ciclo
    i += 1
    # Realizamos la multiplicación
    result = num * i
    
    # Imprimimos el resultado
    print(f"{num} x {i} = {result}")