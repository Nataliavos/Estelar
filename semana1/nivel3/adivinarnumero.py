# juego de adivinar un número

# importamos random para generar números aleatorios
import random

# generamos un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

print("adivina el numero entre 1 y 10")

# el juego se repite hasta que adivine
while True:
    # pedimos un intento
    intento = int(input("tu numero: "))
    
    # verificamos si adivinó
    if intento == numero_secreto:
        print("felicidades! adivinaste!")
        break  # salimos del while
    elif intento < numero_secreto:
        print("muy bajo, intenta de nuevo")
    else:
        print("muy alto, intenta de nuevo")

# versión con intentos limitados
print("\n--- con 5 intentos ---")
numero_secreto = random.randint(1, 20)
intentos = 5

print("adivina el numero entre 1 y 20")
print("tienes", intentos, "intentos")

for i in range(intentos):
    intento = int(input("\nintento: "))
    
    if intento == numero_secreto:
        print("ganaste!")
        break
    elif intento < numero_secreto:
        print("muy bajo")
    else:
        print("muy alto")
    
    # mostramos cuántos intentos quedan
    quedan = intentos - i - 1
    if quedan > 0:
        print("te quedan", quedan, "intentos")

# si terminó el for sin adivinar
if intento != numero_secreto:
    print("\nperdiste! el numero era:", numero_secreto)