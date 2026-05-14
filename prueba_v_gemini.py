"""
Sistema de Análisis de Ventas Diarias
Unidad: Estructuras de Control en Python
Docente: Alejandro Moya
"""

# Lista de datos inicial (No modificar)
ventas = [1200, 3500, 800, 2200, 1500, 700, 4000, 950]

def ejecutar_sistema():
    while True:
        print("\n--- MENÚ DEL SISTEMA ---")
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

        match opcion:
            case "1":
                print("Listado de ventas:")
                for venta in ventas:
                    print(f"- ${venta}")

            case "2":
                print("Ventas mayores a $1000:")
                for venta in ventas:
                    if venta > 1000:
                        print(f"- ${venta}")

            case "3":
                print("Ventas menores o iguales a $1000:")
                for venta in ventas:
                    if venta <= 1000:
                        print(f"- ${venta}")

            case "4":
                total = 0
                for venta in ventas:
                    total += venta
                print(f"El total de ventas es: ${total}")

            case "5":
                total = 0
                for venta in ventas:
                    total += venta
                promedio = total / len(ventas)
                print(f"El promedio de ventas es: ${promedio:.2f}")

            case "6":
                inferior = float(input("Ingrese límite inferior: "))
                superior = float(input("Ingrese límite superior: "))
                print(f"Ventas entre ${inferior} y ${superior}:")
                for venta in ventas:
                    if venta >= inferior and venta <= superior:
                        print(f"- ${venta}")

            case "7":
                # Primero calculamos el promedio
                total = 0
                for venta in ventas:
                    total += venta
                promedio = total / len(ventas)
                
                # Luego contamos
                contador = 0
                for venta in ventas:
                    if venta > promedio:
                        contador += 1
                print(f"Cantidad de ventas mayores al promedio (${promedio:.2f}): {contador}")

            case "8":
                busqueda = float(input("Ingrese el monto a buscar: "))
                encontrado = False
                for venta in ventas:
                    if venta == busqueda:
                        encontrado = True
                        break
                
                if encontrado:
                    print("Venta encontrada")
                else:
                    print("No encontrada")

            case "0":
                print("Saliendo del sistema...")
                break

            case _:
                print("Opción inválida")

if __name__ == "__main__":
    ejecutar_sistema()