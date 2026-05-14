ventas = [1200, 3500, 800, 2200, 1500, 700, 4000, 950]

while True:
    print("\n------------Menú del sistema------------")
    print("1: Mostrar todas las ventas")
    print("2: Mostrar ventas mayores a $1000")
    print("3: Mostrar ventas menores o iguales a $1000")
    print("4: Calcular total de ventas")
    print("5: Calcular promedio")
    print("6: Mostrar ventas dentro de un rango")
    print("7: Contar cuántas ventas son mayores al promedio")
    print("8: Buscar un monto de venta")
    print("0: Salir\n")

    opcion = input("\nSelecciona una opción:  ").strip()
    match opcion: # Match para evaluar la opción seleccionada por el usuario y ejecutar la acción correspondiente
        case "1":
            print(f"\nTodas las ventas: {ventas}\n")
        case "2":
            mayores_1000 = [v for v in ventas if v > 1000]   # For e if para filtrar las ventas mayores a $1000
            print(f"\nVentas mayores a $1000: {mayores_1000}\n")
        case "3":
            menores_igual_1000 = [v for v in ventas if v <= 1000]  # For e if para filtrar las ventas menores o iguales a $1000
            print(f"\nVentas menores o iguales a $1000: {menores_igual_1000}\n")
        case "4":
            total = sum(ventas) #sum para calcular el total de ventas
            print(f"\nTotal de ventas: ${total}\n")
        case "5":
            promedio = sum(ventas) / len(ventas) #sum y len para calcular el promedio de ventas
            print(f"\nPromedio de ventas: ${promedio:.2f}\n")
        case "6": # Pedir dos valores:  límite inferior o límite superior
            limite_inferior = int(input("Ingresa el límite inferior: ").strip())
            limite_superior = int(input("Ingresa el límite superior: ").strip())

            ventas_rango = [v for v in ventas if limite_inferior <= v <= limite_superior] # For e if para filtrar las ventas dentro del rango especificado por el usuario
            print(f"\nVentas dentro del rango ${limite_inferior} - ${limite_superior}: {ventas_rango}\n")
        case "7":
            promedio = sum(ventas) / len(ventas)
            mayores_al_promedio = [v for v in ventas if v > promedio]
            cantidad = len([v for v in ventas if v > promedio])
            print(f"\nVentas mayores al promedio (${promedio:.2f}): {mayores_al_promedio} (Cantidad: {cantidad})\n")
        case "8":
            monto_buscar = int(input("Ingresa el monto de venta a buscar: ").strip())
            if monto_buscar in ventas:
                print("\nVenta encontrada\n")
            else:
                print("\nNo encontrada\n")
        case "0":
            print("\nSaliendo del sistema. ¡Hasta pronto!\n")
            break
        case _:
            print("\nOpción inválida\n")