# verificar si un número es par o impar

# pedimos un número
numero = int(input("ingresa un numero: "))

# usamos % para saber el residuo de dividir entre 2
# si el residuo es 0, es par
# si el residuo es 1, es impar
if numero % 2 == 0:
    print("el numero", numero, "es par")
else:
    print("el numero", numero, "es impar")