lista= [2,4,2,6,1,7,9,2,5,4,5] # creo lista con duplicados
eliminar= [] # variable dobde se almacena la nueva lista sin duplicados

for i in lista: # recorro la lista 
    if i not in eliminar: # evaluo 
        eliminar.append(i) # agrego a la lista

print(eliminar) # imprimo la lista