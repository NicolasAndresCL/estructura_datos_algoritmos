def calcular_precio(edad, es_estudiante):
    """Calcula el precio de entrada según edad y estado de estudiante."""
    precio_base = 5000
    
    if edad < 12:
        descuento = 1.0
    elif edad >= 60:
        descuento = 0.5
    elif es_estudiante:
        descuento = 0.2
    else:
        descuento = 0.0
    
    return precio_base * (1 - descuento)


def mostrar_ticket(nombre, precio):
    """Muestra el ticket de compra."""
    print(f"--- TICKET PARA {nombre} ---")
    print(f"Total a pagar: ${precio}")


def obtener_menu_items():
    """Retorna los menús de comida y bebida."""
    menu_comida = {
        "1": ("Hamburguesa", 3000),
        "2": ("Completo", 3500),
        "3": ("Cabritas", 2500)
    }
    
    menu_bebida = {
        "1": ("Coca-Cola Zero", 1500),
        "2": ("Agua", 1000),
        "3": ("Energetica", 3000)
    }
    
    return menu_comida, menu_bebida


def mostrar_menu(titulo, menu):
    """Muestra un menú y retorna la selección."""
    print(f"\n--- {titulo} ---")
    for key, (item, precio) in menu.items():
        print(f"{key}. {item} - ${precio}")
    
    return input("Seleccione una opción (o presione Enter para omitir): ")


def agregar_comida_bebida():
    """Permite seleccionar comida y bebida, retorna el total adicional."""
    menu_comida, menu_bebida = obtener_menu_items()
    
    comida = mostrar_menu("Menú de Comida", menu_comida)
    bebida = mostrar_menu("Menú de Bebida", menu_bebida)
    
    total_adicional = 0
    if comida in menu_comida:
        total_adicional += menu_comida[comida][1]
    if bebida in menu_bebida:
        total_adicional += menu_bebida[bebida][1]
    
    return total_adicional


def procesar_asistente(numero, total_general):
    """Procesa la compra de un asistente."""
    print(f"\nDatos del asistente {numero}:")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    es_estudiante = input("¿Es estudiante? (si/no): ").lower() == "si"
    
    precio_entrada = calcular_precio(edad, es_estudiante)
    mostrar_ticket(nombre, precio_entrada)
    
    adicional = agregar_comida_bebida()
    total = precio_entrada + adicional
    
    if adicional > 0:
        print(f"Total adicional: ${adicional}")
        print(f"Total a pagar: ${total}")
    
    return total, total_general + total


def main():
    """Programa principal."""
    continuar = True
    
    while continuar:
        cantidad = int(input("¿Cuántas entradas desea comprar?: "))
        total_general = 0
        
        for i in range(cantidad):
            total, total_general = procesar_asistente(i + 1, total_general)
            print(f"Total general hasta ahora: ${total_general}")
        
        opcion = input("\n¿Desea atender a otro grupo? (s/n): ")
        continuar = opcion.lower() != 'n'
    
    print("Sistema cerrado. ¡Buen día!")


if __name__ == "__main__":
    main()
