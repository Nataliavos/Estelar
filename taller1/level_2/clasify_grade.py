'''Clasificador de notas (Excelente, Aprobado, Reprobado).'''

#Solicitamos el dato (nota) al usuario y lo pasamos a tipo float
grade = float(input("Ingrese su nota: "))

status = None #Evita errores si no se genera resultado

# Validación para asegurar que se ingresen notas entre 0 - 5
if grade >= 0 and grade <= 5:

    # Asignamos una clasificación según la nota ingresada
    if grade > 4.5 :
        status = "Excelente"    
    elif grade >= 3.0 and grade <= 4.5 :
        status = "Aprobado"
    elif grade < 3 :
        status = "Reprobado"

# Imprimir mensaje de error si no se cumple la condición (0 - 5)
else :
    print("Ingrese una nota válida.")

# Si la variable status no está vacía, imprimimos la clasificación
if status is not None:
    print(f"Su calificación es: ({grade}) {status}")

    