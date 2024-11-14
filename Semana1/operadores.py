# Operador de asignación (=)
numero1 = 20
numero2 = 25

# Operadores aritméticos ( + - / * % **)
suma = numero1 + numero2
resta = numero1 - numero2
division = numero1 / numero2
division_entera = numero1 // numero2
producto = numero1 * numero2
residuo = numero1 % numero2
potencia = numero1 ** numero2

print("Suma = " + str(suma) + "\n" + "Resta = " + str(resta))
print("División = " + str(division) + "\n" + "División entera = " + str(division_entera))
print("Producto = " + str(producto) + "\n" + "Residuo = " + str(residuo))
print("20 a la 25 = " + str(potencia))

# Operadores de comparación ( < > == != >= <= )

#Igualdad
var1 = True
var2 = False
print( var1 == var2 )

#Desigualdad
numero3 = 15
numero4 = 16

mayor = numero3 > numero4 # Falso
diferente = numero3 != numero4 # Verdadero

print(str(numero3) + " " + str(numero4))
print(numero3 > numero4)
print(numero3 != numero4)

# Operadores Lógicos ( and or )
print( mayor and diferente) # falso y verdadero = falso
print( mayor or diferente) # falso o verdadero = verdadero

# Operadores de tipo ( is, is not, in, not in )
lista = [ 1, 2, 3]
print(1 in lista)
print(5 in lista)