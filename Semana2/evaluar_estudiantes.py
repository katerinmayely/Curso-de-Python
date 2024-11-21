numero_estudiantes = int(input("Ingrese la cantidad de estudiantes que va a evaluar:"))

reprobados = 0
aprobados = 0
suma_calificaciones = 0

for i in range(1, numero_estudiantes + 1):
    nota = float(input(f"Ingrese la nota del estudiante {i}:"))

    # Evaluarlo Pasó o no pasó
    if nota >= 70:
        aprobados += 1
    else:
        reprobados += 1

    suma_calificaciones += nota

    # if i == numero_estudiantes:
    #     promedio = suma_calificaciones / numero_estudiantes
    
promedio = suma_calificaciones / numero_estudiantes

print(f"\nTotal de estudiantes evaluados = {numero_estudiantes}")
print(f"Promedio = {promedio}")
print(f"Cantidad de reprobados = {reprobados}")
print(f"Cantidad de aprobados = {aprobados}")