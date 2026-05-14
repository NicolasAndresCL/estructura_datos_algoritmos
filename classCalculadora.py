class Calculadora:
    """Clase que encapsula operaciones aritméticas básicas."""

    OPERACIONES = {
        "1": ("Suma", "sumar"),
        "2": ("Resta", "restar"),
        "3": ("Multiplicación", "multiplicar"),
        "4": ("División", "dividir"),
    }

    def sumar(self, num1: float, num2: float) -> float:
        return num1 + num2

    def restar(self, num1: float, num2: float) -> float:
        return num1 - num2

    def multiplicar(self, num1: float, num2: float) -> float:
        return num1 * num2

    def dividir(self, num1: float, num2: float) -> float:
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        return num1 / num2

    def ejecutar(self, opcion: str, num1: float, num2: float) -> float:
        if opcion not in self.OPERACIONES:
            raise ValueError("Opción no válida. Seleccione entre 1 y 4.")
        _, nombre_metodo = self.OPERACIONES[opcion]
        metodo = getattr(self, nombre_metodo)
        return metodo(num1, num2)


def pedir_numero(mensaje: str) -> float:
    """Solicita un número al usuario con validación."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("  ✗ Entrada inválida. Ingrese un número válido.")


def mostrar_menu(operaciones: dict) -> None:
    """Imprime el menú de operaciones disponibles."""
    print("\n── Seleccione una operación ──")
    for clave, (nombre, _) in operaciones.items():
        print(f"  {clave}. {nombre}")


def main() -> None:
    calc = Calculadora()

    print("=" * 34)
    print("        CALCULADORA")
    print("=" * 34)

    num1 = pedir_numero("Ingrese el primer número:  ")
    num2 = pedir_numero("Ingrese el segundo número: ")

    mostrar_menu(calc.OPERACIONES)
    opcion = input("\nOpción: ").strip()

    try:
        resultado = calc.ejecutar(opcion, num1, num2)
        nombre_op = calc.OPERACIONES[opcion][0]
        print(f"\nNombre operación {nombre_op} el resultado = {resultado}")
    except (ZeroDivisionError, ValueError) as e:
        print(f"\n   Error: {e}")


if __name__ == "__main__":
    main()