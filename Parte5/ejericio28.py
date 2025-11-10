estudiantes = [ # Creo una lista de estudiantes para poder agregar más
    {'nombre': 'Camilo', 'edad': 20, 'id': 1020467}, 
    {'nombre': 'Laura', 'edad': 22, 'id': 1020468},
    {'nombre': 'Andrés', 'edad': 19, 'id': 1020469},
    {'nombre': 'Valentina', 'edad': 21, 'id': 1020470},
    {'nombre': 'Mateo', 'edad': 23, 'id': 1020471}
]
print(estudiantes) # los imprimo

while True: # creo un while para los mensajes Y AGREGAR a los estudiantes
  agregar =  input('Deseas AGREGUE A UN ESTUDIANTE SI/NO').lower()
  if agregar == 'si': # Si marca si pide los siguientes datos
        nombre = input('cual es el nombre?')
        edad = int(input('cuale es la edad'))
        identificacion = int(input('cual es la identificación'))

        nuevo={ # creo un dicionario donde voy almacenar esos datos
       'nombre': nombre,
        'edad': edad,
        'id': identificacion
        }

        estudiantes.append(nuevo) # Agrego los datos a la lista mediante append
        print(estudiantes)# Imprimo los datos actualizados
  elif agregar == 'no':# en caso de que ponga no sale del programa
      print('Saliste, Gracias por usar el programa')
      break


