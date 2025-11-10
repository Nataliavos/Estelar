nombres = ['Camilo', 'Carlos','yonathan', 'Camila', 'Natalia'] # creo la lista
   
print(nombres) # imprimo la lista

Encuentra = input('que nombre quieres enconta: ') 

for i , nombre in enumerate(nombres): # verifica que si exita el nombre
     if nombre == Encuentra:
      print(f' {i}, {nombre}') # me devuelve la poscion y el nombre
      break
else:
        print(f'{Encuentra}, no esta en la lista') # si no esta imprime no se encuentra
 
for nombre in nombres:
    print(nombre) # imprime el nombre