# Historia de Usuario
# Como jugador de un videojuego de rol, quiero una aplicación de consola que me permita gestionar el inventario
# de mi personaje, para poder agregar los ítems que encuentro en mis aventuras, ver el listado completo de lo
# que cargo, modificar las propiedades de un objeto cuando mejore y eliminar aquello que ya no me sirva o me
# ocupe espacio.
# Requisitos Técnicos
# Programación Orientada a Objetos
# • Clase Item: abstraer el ítem del juego con atributos de identificación y categoría, e implementar
# __str__.
# • Clase Inventario: inicializar internamente la lista de ítems y centralizar las operaciones CRUD.
# Control de Flujo e Interfaz
# • while: bucle principal infinito para mantener el programa abierto y mostrar el menú continuamente.
# • match-case: dirigir el flujo del menú según la opción de texto seleccionada por el usuario.
# • if/elif/else: validar datos (lista vacía, índice existente antes de editar/eliminar).
# • for: recorrer la lista en la función de lectura, mostrando ítems numerados con su índice.
# Operaciones CRUD sobre la Lista
# • Crear: capturar datos por teclado, instanciar el objeto e incorporarlo con .append().
# • Leer: validar con len() y recorrer con for mostrando índice y objeto.
# • Actualizar: solicitar índice, ubicar el objeto por referencia y reasignar sus propiedades.
# • Borrar: solicitar índice y remover el objeto con .pop().
# Punto Extra (opcional)
# • Implementar try-except capturando IndexError o ValueError en lugar de validaciones pasivas con
# if/else.
# • Implementar el ordenamiento (sort) por nombre y categoría.

class Item:
    def __init__(self, nombre: str, categoria: str):
        self.nombre = nombre
        self.categoria = categoria

    def __str__(self):
        return f"[{self.categoria.upper()}] {self.nombre}"

class Inventario:
    def __init__(self):
        self._items = []

    def agregar_item(self, item: Item):
        self._items.append(item)
        print(f"¡'{item.nombre}' ha sido añadido al inventario!")

    def listar_items(self):
        if not self._items:
            print("El inventario está completamente vacío.")
            return False
        
        print("\n=== INVENTARIO DE TU PERSONAJE ===")
        for indice, item in enumerate(self._items):
            print(f"{indice}. {item}")
        return True

    def actualizar_item(self, indice: int, nuevo_nombre: str, nueva_categoria: str):
        item = self._items[indice]
        item.nombre = nuevo_nombre
        item.categoria = nueva_categoria
        print(f"¡Ítem en el índice {indice} actualizado con éxito!")

    def eliminar_item(self, indice: int):
        item_eliminado = self._items.pop(indice)
        print(f"Has descartado: '{item_eliminado.nombre}'.")

    def ordenar_por_nombre(self):
        self._items.sort(key=lambda x: x.nombre.lower())
        print("Inventario ordenado por nombre alfabéticamente.")

    def ordenar_por_categoria(self):
        self._items.sort(key=lambda x: x.categoria.lower())
        print("Inventario ordenado por categoría alfabéticamente.")

def ejecutar_programa():
    inventario = Inventario()

    while True:
        print("\n" + "="*30)
        print("      GESTOR DE INVENTARIO     ")
        print("="*30)
        print("1. Agregar Ítem")
        print("2. Ver Inventario")
        print("3. Modificar Ítem")
        print("4. Eliminar Ítem")
        print("5. Ordenar por Nombre")
        print("6. Ordenar por Categoría")
        print("7. Salir de la aventura")
        
        opcion = input("\nSelecciona una opción: ").strip()

        match opcion:
            case "1":
                print("\n=== NUEVO ÍTEM ===")
                nombre = input("Nombre del ítem: ").strip()
                categoria = input("Categoría (Ej: Arma, Poción, Armadura): ").strip()
                if nombre and categoria:
                    nuevo_item = Item(nombre, categoria)
                    inventario.agregar_item(nuevo_item)
                else:
                    print("Error: El nombre y la categoría no pueden estar vacíos.")

            case "2":
                inventario.listar_items()

            case "3":
                print("\n=== MODIFICAR ÍTEM ===")
                if inventario.listar_items(): # Si hay ítems, procedemos
                    try:
                        indice = int(input("\nIntroduce el indice del ítem a modificar: "))
                        nuevo_nombre = input("Nuevo nombre: ").strip()
                        nueva_categoria = input("Nueva categoría: ").strip()
                        
                        if nuevo_nombre and nueva_categoria:
                            inventario.actualizar_item(indice, nuevo_nombre, nueva_categoria)
                        else:
                            print("Error: Los campos no pueden estar vacíos.")
                            
                    except ValueError:
                        print("Error: Debes ingresar un número entero válido para el índice.")
                    except IndexError:
                        print("Error: El índice ingresado no existe en el inventario.")

            case "4":
                print("\n=== ELIMINAR ÍTEM ===")
                if inventario.listar_items():
                    try:
                        indice = int(input("\nIntroduce el índice del ítem a eliminar: "))
                        inventario.eliminar_item(indice)
                    except ValueError:
                        print("Error: Debes ingresar un número entero válido.")
                    except IndexError:
                        print("Error: El índice ingresado no existe.")

            case "5":
                inventario.ordenar_por_nombre()
                inventario.listar_items()

            case "6":
                inventario.ordenar_por_categoria()
                inventario.listar_items()

            case "7":
                print("\n¡Gracias por jugar! Aventura terminada. ¡Vuelve Pronto!")
                break

            case _:
                print("Opción no válida. Por favor, selecciona una opción del 1 al 7.")


if __name__ == "__main__":
    ejecutar_programa()