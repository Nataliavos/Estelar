inventario=[] # creo una lista donde se van almacenar los productos
while True: # creo un ciclo while para que se repita los mensajes

     try: # verifica que los datos ingresados correpsondan al tipo de dato 
      
         nombre = str(input('ingrese el nombre del producto: '))
         if nombre.strip() == '' or nombre.isdigit() or nombre.startswith(('+','-')):
              
              raise ValueError('error')
         break 
     except ValueError: # si no coiciden me tira error
         print(f'ingrese dato valido')

#-------------------------------------------------ex
while True:# verifica que los datos ingresados correpsondan al tipo de dato 
     
     try:
          precio = float(input('Ingrese el precio del producto: '))
          if precio < 0: # evalua que no se menor 0
           raise ValueError('error')
          break
     except ValueError: # si no coiciden me tira error
          
          print('ingrese dato valido')

#-------------------------------------------------

while True:
     try:# verifica que los datos ingresados correpsondan al tipo de dato 
          cantidad = int(input(' ingrese cantidad del producto: '))
          if cantidad < 0:
     
           raise ValueError('error')
          break
     except ValueError: # si no coiciden me tira error
          print('Ingrese dato valido')

costo_total = precio * cantidad # realiza la operacion 
print(f'{nombre} / {precio} / {cantidad} / {costo_total}') # imprime los datos ingresados por la persona

print('------------------------INVENTARIO ACTUALIZADO--------------------------') 
#Agregamos los productos
inventario.append(f' Producto: {nombre}  | Catidad: {cantidad}  | Valor unitario: {precio} | Total: {costo_total}')
#imprimimos el inventario actualizado
print(inventario)
print('------------------------------------------------------------------------')