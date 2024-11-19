# for i in range(rango):          # type: ignore
#    cualquier_cosa()
#    pass

# formated strings literals
variable = "Python"
print(f"Estoy aprendiendo {variable}")
# Salida: Estoy aprendiendo Python

# Conteo de números del 1 al 10 con un parámetro en la función range
for i in range(10): # lista [1, 2, 3, 4]
    print(i + 1)

print("\n")

# Conteo de números del 1 al 10 con dos parámetros en la función range
for i in range(1, 11): # lista [1, 2, 3, 4]
    print(i)

print("\n")

# Conteo de números impares del 1 al 10 
for i in range(1, 11, 2):
    print(i)

# Iteración de una cadena
# Saber cuántas vocales hay dentro de una cadena (palabra, oración, etc)

frase = input("Ingrese una cadena:")
contador_vocales = 0
vocales = "aeiouAEIOU"

for caracter in frase:
    if caracter in vocales:
        contador_vocales = contador_vocales + 1

print(f"La frase ingresada tiene {contador_vocales} vocales.")