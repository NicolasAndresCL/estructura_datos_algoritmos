""" Ejercicio Breve de Clases en Python
Enunciado
Cree una clase llamada Libro.
La clase debe tener:
Atributos
• título
• autor
• páginas
Métodos
1. Mostrar información del libro.
2. Indicar si el libro tiene más de 300 páginas.
En el programa principal debe:
1. Crear un objeto con datos ingresados por usted.
2. Mostrar la información.
3. Ejecutar el método que indica si es largo o corto. """

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")

    def largo(self):
        if self.paginas > 300:
            print("El libro es largo.")
        else:
            print("El libro es corto.")
            
# Programa principal
if __name__ == "__main__":
    # Crear un objeto con datos ingresados por el usuario
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    paginas = int(input("Ingrese el número de páginas del libro: "))

    libro = Libro(titulo, autor, paginas)

    # Mostrar la información del libro
    libro.mostrar_informacion()

    # Indicar si el libro es largo o corto
    libro.largo()