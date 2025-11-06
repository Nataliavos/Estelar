'''Conversor de grados Celsius a Fahrenheit.'''
'''°F = °C × (9/5) + 32'''
print("Conversor de grados Celsius a Fahrenheit")
degrees_c = float(input("Ingrese los grados Celsius:"))
conversion_f = degrees_c * (9/5) + 32

print(f"{degrees_c} °C equivalen a {conversion_f} °F")
