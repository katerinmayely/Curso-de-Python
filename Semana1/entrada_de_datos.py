# Calcular la hipotenusa (c) de un triangulo rectangulo a partir de sus 
# catetos (a y b)

# Forma larga de resolver el ejercicio
# print("Ingrese el cateto a:")
# a = input()
# a = float(a)

# print("Ingrese el cateto b:")
# b = input()
# b = float(b)

# c = (a ** 2 + b ** 2) ** 0.5 # Cálculo de la hipotenusa

# print("a = ", a, " b = ", b, " c = ", c)

# Forma más sintetizada

a = float(input("Ingrese el cateto a:")) 
b = float(input("Ingrese el cateto b:")) 

print("\nLados del triangulo \na = " + str(a) + " b = " + str(b) + " c = " + str(((a ** 2 + b ** 2) ** 0.5)) + "\n")