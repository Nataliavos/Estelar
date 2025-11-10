import random # importamos el numero 

numero_secret = random.randint(1,10) # damos el rango



verd = False # bandera inicializada en false

while not verd:
    numero = int(input('digita un numero'))

    if numero < numero_secret: # evalua el numero ingresado
        print('el numero que dijitaste es menor')
    elif numero > numero_secret: # evalua el numero ingresado
        print('el numero que dijitaste es mayor')
    else:
        print('adivinaste') # imprime si adivina
        verd = True

