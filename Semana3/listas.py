# lista = [elemento1, elemento2, elemento3]   # type: ignore

lista = [1, 'string', True, 2, 'string2', False]
print(lista) # Imprimir la lista completa

lista[1] = 'cadena' # Cambiar valor de un elemento
print(lista)

lista[4] = lista[1] # Copiar el valor de un elemento a otro
print(lista)

print(f"Numero {lista[3]}") # Acceder a elemento de la lista por separado

# Conocer el tamaño de la lista "len()"
print(f"Tamaño actual de la lista = {len(lista)}")

# Agregar elementos nuevos a la lista. Métodos -> append() insert()
lista.append("elemento al final") # Insertar elemento al final
print(lista)

lista.insert(1, "Valor específicamente en la segunda posición") # Insertar elemento en posición especificada
print(lista)

print(f"Tamaño actual de la lista = {len(lista)}")

# Eliminar elementos de la lista
del lista[0] # Elimina el elemento que se encuentre en la posición indicada
print(lista)

lista.remove('cadena') # Elimina la primera coincidencia del valor que se le envía cómo argumento
print(lista)

print(f"Tamaño actual de la lista = {len(lista)}")

lista_vacia = [] # Crear una lista
print(lista_vacia)

for i in range(10):
    lista_vacia.append(i + 1)

print(lista_vacia)

for elemento in lista: # Iterar los elementos de una lista
    print(elemento)

# Sumar todos los elementos de lista_vacia
total = 0
for numero in lista_vacia:
    total += numero

print(f"Suma = {total}")