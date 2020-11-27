####################################################################################################

# Faça um programa que gera uma lista dos números primos existentes entre 1 e
# um número inteiro informado pelo usuário.

####################################################################################################
def numeros_primos_in_range(stop: int) -> list:
    """
    Obtém uma lista com os números primos de um até o valor do stop.

    Args:
         stop: Valor de parada.

    Returns:
        Lista com números primos.
    """
    lista_primos = [2]
    for i in range(2, stop + 1):
        if i % 2 == 1:
            lista_primos.append(i)

    return lista_primos


def main() -> None:
    stop = int(input('Digite um valor de parada: '))
    numeros_primos = numeros_primos_in_range(stop)
    print(*numeros_primos)


if __name__ == '__main__':
    main()
