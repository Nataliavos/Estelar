# contar hacia atrás desde un número hasta 0

# pedimos el numero desde que el usuarui quiera contar
inicio = int(input("desde que numero vas a contar "))

print("\ncontando regresivo:")

# usamos elwhile para contar hacia atrás
while inicio >= 0:
    print(inicio)
    # restar 1 en cada vuelta
    inicio = inicio - 1

print("fin")

