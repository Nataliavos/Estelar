var_texto = "Hola, soy Veronica"
print(f"La variable '{var_texto}' es de tipo: {type(var_texto)}")

# 2. Número Entero (Integer)
# Números sin decimales.
var_entero = 50
print(f"La variable '{var_entero}' es de tipo: {type(var_entero)}")

# 3. Número Decimal (Float)

var_decimal = 19.99
print(f"La variable '{var_decimal}' es de tipo: {type(var_decimal)}")

# 4. Booleano (Boolean)
# Solo puede ser Verdadero (True) o Falso (False).
var_booleana = True
print(f"La variable '{var_booleana}' es de tipo: {type(var_booleana)}")

print("---")

# 5. El caso de tu ejercicio (input)
# input() SIEMPRE devuelve un string ('str')
edad_como_texto = input("Escribe un número (ej. 25): ")
print(f"El dato '{edad_como_texto}' que escribiste es de tipo: {type(edad_como_texto)}")

# Convertimos ese texto a un entero
edad_como_numero = int(edad_como_texto)
print(f"El dato '{edad_como_numero}'(después de convertir) es de tipo: {type(edad_como_numero)}")