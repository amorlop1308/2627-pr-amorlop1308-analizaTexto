def analizar_texto(frase: str) -> tuple[int, int]:
    """
    Analiza una frase y calcula el número de vocales y de palabras que contiene.

    :param frase: Frase de texto a analizar
    :return: Tupla con dos enteros (número de vocales, número de palabras)
    """
    frase = frase.lower()

    vocales: int = 0
    for caracter in frase:
        if caracter in "aeiouáéíóúü":
            vocales += 1

    lista_palabras: list[str] = frase.split()
    palabras: int = len(lista_palabras)

    return vocales, palabras


def main() -> None:
    frase: str = input()

    resultado: tuple[int, int] = analizar_texto(frase)

    print(f"Vocales: {resultado[0]}")
    print(f"Palabras: {resultado[1]}")


if __name__ == "__main__":
    main()