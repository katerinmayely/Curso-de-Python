# Definición
def saludo(nombre):
    return f"Hola {nombre}"

def suma(a, b):
    return a + b

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")

    for i in range(11):
        # Llamado
        se_saludo = saludo("Marlon Díaz")

    print(f"Estado = {se_saludo}")
    print(suma(1,2))

    #Invocación
    print( saludo("Elias") )