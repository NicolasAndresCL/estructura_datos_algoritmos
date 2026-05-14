""" 1. HISTORIA DE USUARIO
"Como melómano, quiero una aplicación de consola que me permita gestionar mi lista de
canciones favoritas, para poder agregar temas nuevos, visualizarlos ordenadamente,
corregir errores en sus datos y eliminar aquellos que ya no me gustan, asegurando que el
programa no se cierre si cometo un error al ingresar datos." 
El estudiante deberá desarrollar un programa en Python que cumpla con:
• Clase Cancion: Con atributos titulo y artista. Debe incluir el método __str__ para
facilitar la visualización.
• Clase Playlist: Que contenga una lista de objetos y los métodos necesarios para el
CRUD (Crear, Leer, Actualizar, Borrar).
• Interfaz de Consola: Menú interactivo usando la estructura match-case.
• Robustez: Implementación obligatoria de try-except para evitar caídas del sistema.
Deberás aplicar obligatoriamente los siguientes conceptos:
• append(): Para añadir nuevas canciones al final de la lista.
• pop(): Para eliminar canciones seleccionándolas por su número de índice.
• Referencia de Objetos (Edición): Para modificar una canción, se debe acceder al
objeto mediante su índice (lista[posicion]) y reasignar sus atributos.
• sort(key=callback): Para ordenar la lista alfabéticamente
Para el ordenamiento, se debe implementar una función Callback. Esta funciona como un
"ayudante" que le dice al método .sort() qué atributo del objeto debe comparar.
Ejemplo de estructura de ordenamiento:
Python
def ordenar(self):
def criterio(c):
return c.titulo # Extrae el título para comparar
self.canciones.sort(key=criterio)
Es obligatorio proteger el programa en las opciones de Eliminar y Editar contra los
siguientes errores:
• IndexError: Ocurre cuando el usuario ingresa un índice que no existe (ej: borrar la
canción 10 cuando solo hay 3).
• ValueError: Ocurre cuando el usuario ingresa texto (letras) en lugar de un número
entero para el índice.
"""
# ============================================================
#  GESTIÓN DE PLAYLIST  |  Historia de Usuario - Melómano
# ============================================================

class Cancion:
    """Representa una canción con título y artista."""

    def __init__(self, titulo: str, artista: str):
        self.titulo = titulo
        self.artista = artista

    def __str__(self) -> str:
        return f'"{self.titulo}" - {self.artista}'


class Playlist:
    """Gestiona una colección de objetos Cancion (CRUD completo)."""

    def __init__(self):
        self.canciones: list[Cancion] = []

    # ── CREATE ──────────────────────────────────────────────
    def agregar(self, titulo: str, artista: str) -> None:
        nueva = Cancion(titulo, artista)
        self.canciones.append(nueva)           # append() obligatorio
        print(f"\n  ✔ Canción agregada: {nueva}")

    # ── READ ────────────────────────────────────────────────
    def mostrar(self) -> None:
        if not self.canciones:
            print("\n  La playlist está vacía.")
            return
        print("\n  ── Tu Playlist ──────────────────────────")
        for i, cancion in enumerate(self.canciones):
            print(f"  [{i}] {cancion}")
        print(f"  Total: {len(self.canciones)} canción(es)")
        print("  ─────────────────────────────────────────")

    # ── UPDATE ──────────────────────────────────────────────
    def editar(self, indice: int, nuevo_titulo: str, nuevo_artista: str) -> None:
        cancion = self.canciones[indice]       # referencia al objeto por índice
        cancion.titulo = nuevo_titulo          # reasignación de atributos
        cancion.artista = nuevo_artista
        print(f"\n  ✔ Canción actualizada: {cancion}")

    # ── DELETE ──────────────────────────────────────────────
    def eliminar(self, indice: int) -> None:
        eliminada = self.canciones.pop(indice) # pop() obligatorio
        print(f"\n  ✔ Eliminada: {eliminada}")

    # ── SORT ────────────────────────────────────────────────
    def ordenar(self) -> None:
        def criterio(c: Cancion) -> str:       # función callback
            return c.titulo.lower()            # comparación insensible a mayúsculas

        self.canciones.sort(key=criterio)      # sort(key=callback) obligatorio
        print("\n  ✔ Playlist ordenada alfabéticamente.")
        self.mostrar()

    def __len__(self) -> int:
        return len(self.canciones)


# ============================================================
#  INTERFAZ DE CONSOLA
# ============================================================

def pedir_indice(playlist: Playlist, accion: str) -> int:
    """
    Solicita un índice al usuario con manejo de errores.
    Lanza ValueError o IndexError según corresponda para que
    el llamador los capture con try-except.
    """
    playlist.mostrar()
    if len(playlist) == 0:
        raise IndexError("La playlist está vacía, no hay nada que " + accion)
    texto = input(f"\n  Ingresa el número de la canción a {accion}: ")
    indice = int(texto)           # ValueError si no es número
    if indice < 0 or indice >= len(playlist):
        raise IndexError(f"Índice {indice} fuera de rango (0 a {len(playlist)-1})")
    return indice


def menu() -> None:
    playlist = Playlist()

    MENU_TEXTO = """
  ╔══════════════════════════════╗
  ║      🎵  MI PLAYLIST         ║
  ╠══════════════════════════════╣
  ║  1. Agregar canción          ║
  ║  2. Mostrar canciones        ║
  ║  3. Editar canción           ║
  ║  4. Eliminar canción         ║
  ║  5. Ordenar alfabéticamente  ║
  ║  6. Salir                    ║
  ╚══════════════════════════════╝"""

    while True:
        print(MENU_TEXTO)
        opcion = input("  Elige una opción: ").strip()

        match opcion:

            case "1":  # ── AGREGAR ─────────────────────────
                try:
                    titulo  = input("  Título  : ").strip()
                    artista = input("  Artista : ").strip()
                    if not titulo or not artista:
                        raise ValueError("El título y el artista no pueden estar vacíos.")
                    playlist.agregar(titulo, artista)
                except ValueError as e:
                    print(f"\n  ⚠ Error de valor: {e}")

            case "2":  # ── MOSTRAR ─────────────────────────
                playlist.mostrar()

            case "3":  # ── EDITAR ──────────────────────────
                try:
                    indice = pedir_indice(playlist, "editar")
                    print(f"\n  Editando: {playlist.canciones[indice]}")
                    nuevo_titulo  = input("  Nuevo título  : ").strip()
                    nuevo_artista = input("  Nuevo artista : ").strip()
                    if not nuevo_titulo or not nuevo_artista:
                        raise ValueError("Los campos no pueden estar vacíos.")
                    playlist.editar(indice, nuevo_titulo, nuevo_artista)
                except ValueError as e:
                    print(f"\n  ⚠ Error de valor: {e}")
                except IndexError as e:
                    print(f"\n  ⚠ Error de índice: {e}")

            case "4":  # ── ELIMINAR ────────────────────────
                try:
                    indice = pedir_indice(playlist, "eliminar")
                    playlist.eliminar(indice)
                except ValueError as e:
                    print(f"\n  ⚠ Error de valor: {e}")
                except IndexError as e:
                    print(f"\n  ⚠ Error de índice: {e}")

            case "5":  # ── ORDENAR ─────────────────────────
                playlist.ordenar()

            case "6":  # ── SALIR ───────────────────────────
                print("\n  ¡Hasta luego! 🎶\n")
                break

            case _:    # ── OPCIÓN INVÁLIDA ─────────────────
                print("\n  ⚠ Opción no válida. Elige entre 1 y 6.")


# ── PUNTO DE ENTRADA ────────────────────────────────────────
if __name__ == "__main__":
    menu()








    