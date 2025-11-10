# clasificar una nota segun lo que se haya sacado

# pedir la nota
nota = float(input("ingresa tu nota de 1 a 100: "))

# clasificar la nota
if nota >= 90:
    print("muy teso")
elif nota >= 80:
    print("muy bien")
elif nota >= 6:
    print("pasó")
else:
    print("ono perdiste")
