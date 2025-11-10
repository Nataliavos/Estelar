cuenta = [] # creo un lista vacia donde voy a guardar el dinero
while True: # creo un ciclo while para que se repita
    opciones = input('QUÉ DESEA HACER:\nrecargar dinero(r)\nsacar dinero(s)').lower() # imprimo las opciones

    if opciones == 'r': # si elije r 
       recarga =  float(input('ingrese el valor a recargar ')) # para ingresar el valor
       cuenta.append(recarga) # agrega el valor
       print({sum(cuenta)}) # suma lo que hay en la cuenta


    elif opciones == 's': # si elije la opcion s 
      if not  cuenta: # evalua que si tenga dinero o que no tenga
       print('no tienes dinero en la cuenta') # imprime mensaje de no tener dinero
       continue
       
      resta = float(input('cuanto dinero deceas sacar? '))# pregunta la cantidad de dinero que quiere sacar
      saldo= sum(cuenta)

      if resta > saldo:  # si es mamyor a saldo 
       print(f'fondos insuficientes{saldo}') # imprime no lo deja sacar
      else:
       cuenta.append(-resta) # le resta el saldo si es menor el valor a sacar
       print(f'{sum(cuenta)}') # muestra el saldo que quedo

    elif opciones == 'x': # para salir del sistema
      print('gracias por usar nuestro sistema')
      break