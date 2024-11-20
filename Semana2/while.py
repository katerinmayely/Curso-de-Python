# while expresion_condicional:              # type: ignore
#    instrucciones...                      # type: ignore

# while(True):
#     print("Estoy atrapado en un bucle")

contador = 1
while contador != 11:
    print(contador)
    contador = contador + 1

print("Estoy fuera del bucle")

# Recibe una secuencia de números y determina cuántos son pares y cuántos son impares.

# Crear las variables que almacenen las cantidades de pares e impares 
contador_pares = 0
contador_impares = 0

# Solicitar un numero entero al usuario
numero = int(input("Ingrese un numero:"))

# bucle se detiene si ingreso el cero
while numero != 0:
    if numero % 2 == 0:
        contador_pares += 1 # contador_pares = contador_pares + 1
    else:
        contador_impares += 1

    numero = int(input("Ingrese un numero:"))

print(f"Pares: {contador_pares} \nImpares: {contador_impares}")