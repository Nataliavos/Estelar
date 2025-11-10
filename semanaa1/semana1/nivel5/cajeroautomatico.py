# cajero automático

# empezamos con saldo inicial
saldo = 1000

# menú que se repite
while True:
    print("\n--- cajero ---")
    print("saldo actual: $", saldo)
    print("1. depositar")
    print("2. retirar")
    print("3. ver saldo")
    print("4. salir")
    
    opcion = input("elige opcion: ")
    
    # depositar dinero
    if opcion == "1":
        # pedimos cantidad y la convertimos a número
        cantidad = float(input("cuanto quieres depositar? "))
        
        # verificamos que sea positivo
        if cantidad > 0:
            # sumamos al saldo
            saldo = saldo + cantidad
            print("depositaste $", cantidad)
            print("nuevo saldo: $", saldo)
        else:
            print("cantidad invalida")
    
    # retirar dinero
    elif opcion == "2":
        cantidad = float(input("cuanto quieres retirar? "))
        
        # verificamos que tenga suficiente dinero
        if cantidad > saldo:
            print("no tienes suficiente saldo")
        elif cantidad > 0:
            # restamos del saldo
            saldo = saldo - cantidad
            print("retiraste $", cantidad)
            print("nuevo saldo: $", saldo)
        else:
            print("cantidad invalida")
    
    # solo mostrar saldo
    elif opcion == "3":
        print("tu saldo es: $", saldo)
    
    # salir
    elif opcion == "4":
        print("hasta luego")
        break