# Definición
def saludo(nombre):
    print(f"Hola, {nombre}.")
    return "Saludado"

def suma(a, b):
    return a + b

nombre = input("Ingrese su nombre: ")

for i in range(11):
    # Llamado
    se_saludo = saludo("Marlon Díaz")

print(f"Estado = {se_saludo}")
print(suma(1,2))