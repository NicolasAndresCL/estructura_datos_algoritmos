"""cálculo de números pares"""

from typing import List


def pares_en_lista(numeros: List[int]) -> List[int]:
    """Devuelve los números pares de la lista de entrada."""
    return [x for x in numeros if x % 2 == 0]


def contar_pares(numeros: List[int]) -> int:
    """Devuelve la cantidad de números pares en la lista de entrada."""
    return len(pares_en_lista(numeros))


def main() -> None:
    entrada = input("Ingresa números separados por espacios: ").strip()
    if not entrada:
        print("No ingresaste ningún número.")
        return

    try:
        numeros = [int(x) for x in entrada.split()]
    except ValueError:
        print("Entrada inválida. Introduce solo números enteros.")
        return

    pares = pares_en_lista(numeros)
    print(f"Números pares: {pares}")
    print(f"Cantidad de pares: {contar_pares(numeros)}")


if __name__ == "__main__":
    main()
