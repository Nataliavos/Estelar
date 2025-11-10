pares = [] # lista de numeros pares 
impares = [] # lista de numeros impares
for i in range(1,50,1): # imprime una lisat de numeros iniciando en 1 hasta 50 y va de 1 en 1
   if i % 2 == 0: # los numero con residual 0 en este caso pares
     print(f'{i}, par') # imprime los numeros pares
     pares.append(i) # Los agrega a la lista pares mediannte el append
   if i % 2 != 0: # los numeros no divisibles por 2 es decir impares 
        print(f'{i},impar') # imprime los impares 
        impares.append(i) # Agrega a la lisat mediante el append

print(pares) # Imprime la lista
print(impares) # imprime la lista