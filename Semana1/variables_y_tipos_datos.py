# CONSIDERACIONES AL CREAR NOMBRES DE VARIABLES Y FUNCIONES 
# 1 - Nombres de variables puedden contener mayúsculas, minúsculas, dígitos (números) 
# y carácter Guión Bajo.

# 2 - Debe comenzar con una letra.

# 3 - Las mayúsculas y minúsculas se tratan de forma distinta.

# 4 - Utilizar nombres QUE ME DEN A ENTENDER LA LA FUNCIÓN DE ESA VARIABLE.

# 5 - No utilizar como nombre palabras reservadas.

# 6 - El carácter Guión bajo es considerado, por Python, como una letra.

nombre_estudiante = 'Kattherine'

# Ejemplo de caso incorrecto
#print = "Hola mundo"
#print(print)

print(nombre_estudiante)

_21nombre = "Kattherine"
print(_21nombre)

_21nombre = False
print(_21nombre)

_21nombre = 12
print(_21nombre)

# True, if, for, while... ejemplos de palabras reservadas.

# print(apellido) -Caso incorrecto: No podemos utilizar variables que no hemos creado.

# Conversión de variables. Funciones de conversión -> float() int() str()
hora = 3
print("Hola Kattherine son las " + str(hora))