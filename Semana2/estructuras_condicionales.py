# if expresión_condicional:              # type: ignore
#     ejecutar_esto_si_cumple                  # type: ignore

# if expresión_condicional:             # type: ignore
#     ejecutar_esto_si_cumple                  # type: ignore
# else:
#     ejecutar_esto_si_no_se_cumple      # type: ignore

# if expresión_condicional:               # type: ignore
#     ejecutar_esto_si_cumple                  # type: ignore
# elif expresión_condicional:             # type: ignore
#     ejecutar_esto_si_se_cumple         # type: ignore
# else:
#     ejecutar_esto_si_no_se_cumple      # type: ignore

# Realiza la suma si y solo si ambos números son mayores a cero
numero1 = float(input("Ingrese el primer número:"))
numero2 = float(input("Ingrese el segundo numero:"))

# if-else anidados
# if numero1 > 0:
#     print("El primer número es mayor a cero.")

#     if numero2 > 0:
#         print("El segundo número es mayor a cero.")
#         suma = numero1 + numero2
#         print("Suma = " + str(suma))
#     else: 
#         print("El segundo número no es mayor a cero!!! \nNo se puede realizar la suma.")

# else: 
#     print("El primer número no es mayor a cero!!! \nNo se puede realizar la suma.")

# elif 
if numero1 == 0 and numero2 == 0:
    print("No podemos hacer la operación si hay al menos un cero!!!")
elif numero1 > 0 and numero2 > 0:
    print("Perfecto! Ambos números mayores a cero.")
    suma = numero1 + numero2
    print("Suma = " + str(suma))
else: 
    print("No podemos realizar la operación con valores que no sean mayores a cero!!!")

print("Operación finalizada.")  