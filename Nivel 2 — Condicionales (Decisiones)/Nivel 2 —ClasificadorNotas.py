nota = int(input("Ingresa la nota (0-5): "))


if nota < 0 or nota > 5:
    print("Error: La nota debe estar entre 0 y 5.")

elif nota >= 4.5:
    print("¡Excelente!")
elif nota >= 3:
    print("Aprobado")

else:
    print("Reprobado")
