
# Crear un conjunto
mi_conjunto = {1, 2, 3, 4}   
otro_conjunto = set([1, 2, 3, 4])

print(mi_conjunto)
print(otro_conjunto)

# Agregar elementos al conjunto
mi_conjunto.add(5)
print(mi_conjunto)

# Eliminar elementos
mi_conjunto.remove(1)
print(mi_conjunto)

A = {1, 2, 3, 4}
B = {4, 5, 6, 7, 8}

# Unión
C = A | B
print(C)

# Intersección
D = A & B
print(D)

# Diferencia
E = B - A
print(E)