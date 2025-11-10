lista = [];
total=0; # creo una variable vacia
cantidad = int(input('Agregue cantidad de notas: ')) # se agrega las cantidades

for i in range(cantidad): # el rago va adepender de la cantidad que ingrese
     notas = float(input(f'Agregue notas {i+1}:'))
     lista.append(notas) # agrego las notas
     print(lista)
   
     total = sum(lista) # suma el total
     print(total) # muestro el total

     print('-------------------------------')
     resultado = total / cantidad   # saco el promedio
     print(resultado) # imprimo el resultado

