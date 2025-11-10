lista = [] # creo una lista para almacenar una variable
contador = 0 # creo una varible contador donde se van almacenar las vueltas para posteriormente ser utilizadas para sacar el promedio

while True:  # creo un ciclo wile para que se repita siempre
        numeros = int(input('ingresa cantidad de numeros')) # creo variable para ingresa valores
        if numeros == 0:  # si el numero ingresado e sigual a 0 se detiene
         print(f'el resultado es:, {resultado}')   # imprime luego de detener
         break # detienee el blucle
            
       
        lista.append(numeros) # agrega los numero ingresados en la variable numeros a la lista Lista
        contador += 1 # contador incrementa en uno con cada iteracion
        
        print(lista) # imprime la lista
        resultado = sum(lista) / contador # imprime el resulatdo final