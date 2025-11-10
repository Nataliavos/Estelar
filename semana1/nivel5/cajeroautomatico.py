# simulador de cajero automático

# empezamos con un saldo inicial
saldo = 1000

# el programa se repite hasta que el usuario salga
while True:
    print("\n--- cajero automático ---")
    print(f"saldo actual: ${saldo}")
    print("1. depositar")
    print("2. retirar")
    print("3. consultar saldo")
    print("4. salir")
    
    opcion = input("elige una opción: ")
    
    # opción 1: agregar dinero a la cuenta
    if opcion == "1":
        cantidad = float(input("¿cuánto quieres depositar? $"))
        # verificamos que sea un número positivo
        if cantidad > 0:
            saldo += cantidad
            print(f"✓ depositaste ${cantidad}. nuevo saldo: ${saldo}")
        else:
            print("✗ cantidad inválida")
    
    # opción 2: sacar dinero
    elif opcion == "2":
        cantidad = float(input("¿cuánto quieres retirar? $"))
        # verificamos que tenga suficiente dinero
        if cantidad > saldo:
            print("✗ saldo insuficiente")
        elif cantidad > 0:
            saldo -= cantidad
            print(f"✓ retiraste ${cantidad}. nuevo saldo: ${saldo}")
        else:
            print("✗ cantidad inválida")
    
    # opción 3: solo mostrar cuánto dinero tiene
    elif opcion == "3":
        print(f"tu saldo es: ${saldo}")
    
    # opción 4: terminar el programa
    elif opcion == "4":
        print("¡hasta luego!")
        break