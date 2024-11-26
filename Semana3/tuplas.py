# tupla = (elemento1, elemento2, elemento3)

# otra_tupla = elemento1, elemento2, elemento3

# import math
from math import sqrt, pow, floor

lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
otra_tupla = 1, 2, 3, 4, 5 
tupla_un_elemento = (1,)
tupla_un_elemento_2 = 1,

tupla_vacia = ()

print(lista)
print(tupla)
print(otra_tupla)
print(tupla_vacia)
print(tupla_un_elemento)
print(tupla_un_elemento_2)

print(f"Primer elemento de tupla = {tupla[0]}")
print(f"Segundo elemento de tupla = {tupla[1]}")

for elemento in tupla: # Iterando la tupla con un bucle for
    print(elemento)

print(f"Tamaño de la tupla = {len(tupla)}")

tupla_x = 6, 7, 8, 9, 10

nueva_tupla = tupla + tupla_x

print(f"Suma = {nueva_tupla}")
print(1 in tupla) # True
print(7 in tupla) # False
print(2 not in tupla) # False

# Solución de ejercicio - Cálculo de distancia entre dos puntos del plano cartesiano
print("\nEjercicio en clase")

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))

x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

punto1 = (x1, y1)
punto2 = (x2, y2)

distancia = sqrt( pow(punto2[0] - punto1[0], 2) + pow(punto2[1] - punto1[1], 2) )

print(f"Coordenadas del punto 1 = {punto1} \nCoordenadas del punto 2 = {punto2} \nDistancia = {floor(distancia)}") # Truncado a enteros con funcion piso
print(f"Coordenadas del punto 1 = {punto1} \nCoordenadas del punto 2 = {punto2} \nDistancia = {distancia: .2f}") # Truncado de decimales desde la f-string