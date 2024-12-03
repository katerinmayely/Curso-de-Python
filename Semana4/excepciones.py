def division(a, b):
    resultado = a / b
    return resultado

print("División")
num1 = float(input("Ingrese un número:"))
num2 = float(input("Ingrese otro número:"))

try:
    print(f"El total es {division(num1, num2)}")
except ZeroDivisionError:
    print("Cuidado! Está intentando dividir entre cero...")
except:
    print("Ocurrió un error")
