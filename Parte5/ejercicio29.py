def suma(a , b): # Creo una funcion para la suma
    return a + b
def resta(a, b): # creo una funcion para la resta
    return a - b 
def multiplicacion(a, b):# creo una funcion para la multiplicación
    return a * b
def division(a , b):# creo una funcion para la división
    if b == 0: # si es 0 retorna error
     return 'no es valido'
    return a / b

def calculadora():# creo una funcion llamada calculadora
 while True: # creo un while para que se me repita las opciones
        print("\nOperaciones disponibles:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
      

        opcion= input( 'seleciones una opcion') # input donde se ingresa el valor
        if opcion == '5': # si es 5 sale del programa
            print('saliste')
            break
        if opcion in ['1','2','3','4']: 
              try: # valido que sean numeros los que se ingresan
                  numeroUno= float(input('ingresa numero '))
                  numeroDos= float(input('ingresa numero '))
              except ValueError: # en dado caso que no me muestra el mensaje
               print('ingrese un dato valido')
               continue
              if opcion == '1': # Si selciono 1
                   print(f'La suma es: {suma(numeroUno, numeroDos)}')# suma los dos valores
                   
              elif opcion == '2': # Si selciono 2
                   print(f'La resta es:{resta(numeroUno, numeroDos)}')# resta los dos valores
                   
              elif opcion == '3': # Si selciono 3
                   print(f'La multiplicación es: {multiplicacion(numeroUno, numeroDos)}')  # multiplica los dos valores
                   
              elif opcion == '4':# si seleciono 4
                   print(f' La división es: {division(numeroUno, numeroDos)}')   # divide los dos valores
                      
              else:
                   print('Opcion no valida')


calculadora() # llamo la funcion para que se ejecute.