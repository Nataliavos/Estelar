''' Adivina el número (usar random). '''

# importamos la librería random para generar un número aleatorio
import random

# generamos un número secreto entre 1 y 10
secret_num = random.randint(1, 10)

print("======= ADIVINA EL NÚMERO SECRETO =======")
print("Tienes 3 intentos para adivinar un número entre 1 y 10.")

# variable para saber si ya adiviné o no, la inicializamos en False
guessed = False
# contador de intentos, lo inicializamos en 0
attempts = 0

# mientras tenga menos de 3 intentos y no haya adivinado, sigo jugando
while attempts < 3 and not guessed :
    # pedimos al usuario que ingrese un número
    assumption = input(f"Intento {attempts +1}/3 -->").strip()

    # si el usuario no ingresa un número, mostramos error y volvemos a pedirlo
    if not assumption.isnumeric():
        print("Dato inválido, ingresa números solamente.")
        assumption = input("Ingresa un número ente 1 y 10. Tienes 3 intentos --> ").strip()

    # convertimos el número ingresado a entero
    assumption = int(assumption)

    # si el número está por fuera del rango, mostramos error y volvemos a pedirlo (no cuenta como intento)
    if assumption < 1 or assumption > 10 :
        print("El número debe estar entre 1 y 10. Intenta de nuevo.")
        # reiniciamos el intento actual
        continue
    
    # incrementamos el contador de intentos
    attempts += 1

    # comparamos el número ingresado con el número secreto
    if assumption == secret_num :
        print(f"¡Adivinaste! El número secreto es --> {secret_num}")
        guessed = True
    elif assumption > secret_num :
        print(f"El número secreto es menor que {assumption}.")
    else :
        print(f"El número secreto es mayor que {assumption}.")

# si el usuario no adivinó después de 3 intentos, mostramos el número secreto
if not guessed :
    print(f"Lo siento, no adivinaste. El número secreto era --> {secret_num}")
