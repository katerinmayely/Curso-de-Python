from funciones import mostrar_menu, sumar, restar, multiplicar, dividir, mostrar_historial

operaciones_realizadas = 0
historial = [] # [ '3+4=7', '3-1=2' ]

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la operación que desea realizar: ").strip()

    if opcion == "6":
        print(f"\n¡Gracias por usar la calculadora! \nTotal de operaciones realizadas: {operaciones_realizadas}")
        mostrar_historial(historial)
        break

    if opcion == "5":
        mostrar_historial(historial)
        continue

    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
        continue

    try:
        if opcion == "1":
            resultado = sumar(num1, num2)
            operacion = f"{num1}+{num2}={resultado}"
        elif opcion == "2":
            resultado = restar(num1, num2)
            operacion = f"{num1}-{num2}={resultado}"
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
            operacion = f"{num1}*{num2}={resultado}"
        elif opcion == "4":
            resultado = dividir(num1, num2)
            operacion = f"{num1}/{num2}={resultado}"
        elif opcion == "5":
            mostrar_historial(historial)
        else:
            print("Opción no válida. Intente de nuevo.")
            continue

        print(f"El resultado de la operación es: {resultado}")
        operaciones_realizadas += 1
        historial.append(operacion)
    except:
        print("Ocurrió un error al realizar la operación.")