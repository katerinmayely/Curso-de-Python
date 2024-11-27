
# diccionario = {
#     clave1: valor1,   # type: ignore
#     clave2: valor2,   # type: ignore
#     clave3: valor3,   # type: ignore
# }

diccionario_es_en = {
    "anaranjado": "orange",
    "rojo": "red",
    "verde": "green",
    "amarillo": "yellow",
    "blanco": "white"
}

print(diccionario_es_en) # Mostrar en consola un diccionario

print(diccionario_es_en["verde"]) # Buscar un valor por su clave 

# keys() - Retorna una lista [] con todas las claves
print(diccionario_es_en.keys())

print("\nDiccionario es-en iterado con el método keys()")
for key in diccionario_es_en.keys():
    print(f"{key} -> {diccionario_es_en[key]}")

# items() - Retorna una lista de tuplas () con todos los pares del diccionario
print("\nDiccionario es-en iterado con el método items()")
for es, en in diccionario_es_en.items():
    print(f"{es} -> {en}")

# Modificar un elemento del diccionario
diccionario_es_en["rojo"] = "redcito"

print("\n")
print(diccionario_es_en["rojo"])

# Agregar una nueva clave al diccionario
diccionario_es_en["negro"] = "black"

print("\n")
print(diccionario_es_en)

# Eliminar una clave del diccionario
del diccionario_es_en["rojo"]

print("\n")
print(diccionario_es_en)

diccionario_es_en.popitem() # Eliminar la última clave del diccionario

print("\n")
print(diccionario_es_en)

key = input("\n¡Bienvenido al diccionario \"súper\" básico! \nIngrese un color que quiera traducir (Ingrese 'no' si desea terminar): ")

while( key != "no" ):
    if key in diccionario_es_en.keys():
        print(f"{key} -> {diccionario_es_en[key]}")
    else:
        print("Aún no hemos registrado esa palabra en nuestro diccionario.")

    key = input("Ingrese un color que quiera traducir (Ingrese 'no' si desea terminar): ")