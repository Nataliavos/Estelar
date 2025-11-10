
#pa saberque tipo de dato ingresa el usuario

print("---tipos de datos---\n")

# pedir un dato
dato = input("escribe cualquier cosita: ")

# mostrar el tipo original
print("\ndato:", dato)
print("tipo original:", type(dato))

# convertirlos y mostrar el tipo
print("\n---conversiones de datos---")

# verificar si es número entero con int
if dato.isdigit():
    numero = int(dato)
    print("es un numero entero")
    print("valor:", numero)
    print("tipo:", type(numero))

# si es un numero decimal
elif "." in dato:
    try:
        decimal = float(dato)
        print("es un numero decimal")
        print("valor:", decimal)
        print("tipo:", type(decimal))
    except:
        print("es texto")
        print("tipo:", type(dato))

# si no es numero, es texto
else:
    print("es texto")
    print("tipo:", type(dato))