# pa verificar si un numero es par o impar

# pedimos un número
numero = int(input("ingresa un numero: "))

# usamos % para saber el residuo cuando dividimos entre 2
# si el residuo es 0 es par
# si el residuo es 1 es impar
if numero % 2 == 0:
    print("el numero", numero, "es par")
else:
    print("el numero", numero, "es impar")