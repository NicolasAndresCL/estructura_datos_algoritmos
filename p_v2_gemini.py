# Lista inicial de ventas proporcionada por el caso
ventas = [1200, 3500, 800, 2200, 1500, 700, 4000, 950]

continuar = True

while continuar:
    # 1. Mostrar Menú
    print("\n--- SISTEMA DE ANÁLISIS DE VENTAS ---")
    print("1: Mostrar todas las ventas")
    print("2: Mostrar ventas mayores a $1000")
    print("3: Mostrar ventas menores o iguales a $1000")
    print("4: Calcular total de ventas")
    print("5: Calcular promedio")
    print("6: Mostrar ventas dentro de un rango")
    print("7: Contar cuántas ventas son mayores al promedio")
    print("8: Buscar un monto de venta")
    print("0: Salir")
    
    opcion = input("\nSeleccione una opción: ")

    # 2. Estructura Match para el control del menú
    match opcion:
        case "1":
            print("Listado de ventas:")
            for v in ventas:
                print(f"${v}")
        
        case "2":
            print("Ventas mayores a $1000:")
            for v in ventas:
                if v > 1000:
                    print(f"${v}")
        
        case "3":
            print("Ventas menores o iguales a $1000:")
            for v in ventas:
                if v <= 1000:
                    print(f"${v}")
        
        case "4":
            total = sum(ventas)
            print(f"El total de ventas del día es: ${total}")
        
        case "5":
            promedio = sum(ventas) / len(ventas)
            print(f"El promedio de ventas es: ${promedio:.2f}")
            
        case "6":
            inf = int(input("Ingrese límite inferior: "))
            sup = int(input("Ingrese límite superior: "))
            print(f"Ventas entre ${inf} y ${sup}:")
            for v in ventas:
                if v >= inf and v <= sup:
                    print(f"${v}")
        
        case "7":
            promedio = sum(ventas) / len(ventas)
            contador = 0
            for v in ventas:
                if v > promedio:
                    contador += 1
            print(f"Cantidad de ventas sobre el promedio (${promedio:.2f}): {contador}")
            
        case "8":
            busqueda = int(input("Ingrese el monto a buscar: "))
            encontrado = False
            for v in ventas:
                if v == busqueda:
                    encontrado = True
                    break
            
            if encontrado:
                print("Venta encontrada")
            else:
                print("No encontrada")
                
        case "0":
            print("Saliendo del sistema...")
            continuar = False
            
        case _:
            print("Opción inválida")