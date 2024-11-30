# classificador.py

def classificar_numeros(numeros):
    """
    Classifica os números em pares e ímpares.

    Args:
        numeros (list): Lista de números inteiros.

    Returns:
        tuple: Duas listas - (pares, ímpares)
    """
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]
    return pares, impares
