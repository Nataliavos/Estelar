iterador = 0

while iterador < 3:
    #  La solicitud de entrada se repite en cada ciclo
    try:
        numero = float(input(f"Por favor ingresa el número {iterador + 1} de 3: "))
        
        if numero > 0:
            print("El número ingresado es positivo.")
        elif numero < 0:
            print("El número ingresado es negativo.")
        else:
            print("El número ingresado es cero.")
            
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un valor numérico.")
        # Opcional: Podrías usar 'continue' aquí para no incrementar el iterador si la entrada es inválida.

    # Es crucial incrementar el iterador para evitar un bucle infinito
    iterador = iterador + 1

print("\nProceso terminado. Se ingresaron 3 números.")