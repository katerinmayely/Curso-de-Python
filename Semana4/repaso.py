# Calculadora de descuentos
# Solicitar al usuario el precio del producto y el porcentaje de descuento
# Validar que solo ingrese numeror positivos y en el rango
# Mostral el precio final
from funciones import saludo

def calcular_precio_con_descuento(precio_producto, porcentaje_descuento):
    descuento = precio_producto * (porcentaje_descuento / 100)
    total_pagar = precio_producto - descuento
    return total_pagar

try:
    precio = float(input("Ingrese el precio del producto: "))
    descuento = float(input("Ingrese el descuento: "))

    if precio < 0 or descuento < 0 or descuento > 100:
        print("Ingrese valores positivos o dentro del rango")
        
    precio_final = calcular_precio_con_descuento(precio, descuento)

    saludo("Nombre")

    print(f"El precio a pagar es: {precio_final} lempiras.")
except ValueError:
    print("Solo se permiten valores númericos")
except:
    print("Ocurrió un error")