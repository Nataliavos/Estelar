contactos = [
    {'nombre': 'Camilo', 'numero': 3053432456},
    {'nombre': 'Laura', 'numero': 3109876543},
    {'nombre': 'Andrés', 'numero': 3112345678},
    {'nombre': 'Valentina', 'numero': 3204567890},
    {'nombre': 'Mateo', 'numero': 3001234567}
]

print(contactos) # imprimo los contactos
while True: # creo u while para que me muestre las opciones
    agregar = input('deceas agreagr un nuevo contacto? SI/NO').lower()

    if agregar == 'si': # valido lo que ingrese la persona
        nombre =  input('escribe el nombre: ') 
        numero =  int(input('escribe el numero de telefono: '))
        nuevo_contacto={# creo un dicionario para recivir los datos 
            'nombre': nombre,
            'numero': numero,
             }
    
        contactos.append(nuevo_contacto) # agrego los daos del dicionario a lista de contactos
        print(contactos) # imprimo la lista de contactos actualizada
    elif agregar == 'no': # si dice no sale y muestra el mensaje.
     print('gracias por usar la app de agregar contactos')
     break

