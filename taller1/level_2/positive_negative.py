#Número positivo, negativo o cero.

num = int(input("Ingrese un número: "))

if num > 0 :
    print(f"El número ({num}) es positivo.")
elif num < 0 :
    print(f"El número ({num}) es negativo.")
elif num == 0 :
    print(f"El número ({num}) es cero.")