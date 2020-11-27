####################################################################################################

# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada
# posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado
# mágico de lado 3, com números de 1 a 9:

#     8  3  4
#     1  5  9
#     6  7  2

#     Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as
#     características acima. Dica: produza todas as combinações possíveis e verifique a soma quando
#     completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz
#     3x3.

####################################################################################################
from itertools import permutations
from typing import Iterator


def transforma_em_matriz(vetores: Iterator) -> list:
    """
    Transforma uma lista de vetores em matrizes 3x3.

    Args:
        vetores: Lista de vetores com 9 posições.

    Returns:
        Uma lista de matrizes.
    """
    lista_matrizes = []
    for vetor in vetores:
        indice = 0
        matriz = []
        for _ in range(3):
            linha = []
            for _ in range(3):
                linha.append(vetor[indice])
                indice += 1
            matriz.append(linha)
        lista_matrizes.append(matriz)

    return lista_matrizes


def print_quadrados_magicos(quadrados_magicos: list) -> None:
    """
    Printa os quadrados_magicos no console em forma de matriz.

    Args:
        quadrados_magicos: lista com os quadrados mágicos.
    """
    for quadrado_magico in quadrados_magicos:
        for linha in quadrado_magico:
            print(*linha, sep=' ')
        print()


def eh_quadrado_magico(lista_matrizes: list) -> list:
    """
    Verifica quais elementos na lista de matrizes são quadrados mágicos.

    Args:
        lista_matrizes: Lista com todas as matrizes 3x3.

    Returns:
        Uma lista com as matrizes que são quadrados mágicos.
    """

    lista_quadrados_magicos = []
    for matriz in lista_matrizes:
        # Verificando se a soma da diagonal secundária é igual a 15
        soma_diagonal_secundaria = matriz[0][2] + matriz[1][1] + matriz[2][0]
        if soma_diagonal_secundaria != 15:
            continue

        # Verificando se a soma da diagonal principal é igual a 15
        soma_diagonal_principal = matriz[0][0] + matriz[1][1] + matriz[2][2]
        if soma_diagonal_principal != 15:
            continue

        flag = False

        # Verificando se a soma da linha é igual a 15
        for linha in matriz:
            if sum(linha) != 15:
                flag = True
                break
        if flag:
            continue

        # Verificando se a soma da coluna é igual a 15
        for coluna, _ in enumerate(matriz):
            soma_coluna = 0
            for linha, _ in enumerate(matriz):
                soma_coluna += matriz[linha][coluna]
            if soma_coluna != 15:
                flag = True
                break
        if flag:
            continue

        # Se passou nas validações é adicionado na lista de quadrados mágicos
        lista_quadrados_magicos.append(matriz)

    return lista_quadrados_magicos


def main() -> None:
    # Gerando vetores.
    vetores = permutations(range(1, 10), 9)

    # Transformando os vetores em matrizes
    lista_matrizes = transforma_em_matriz(vetores)

    # Obtendo uma lista com os quadrados mágicos
    quadrados_magicos = eh_quadrado_magico(lista_matrizes)

    # Printar os quadrados mágicos na tela em forma de matriz.
    print_quadrados_magicos(quadrados_magicos)


if __name__ == '__main__':
    main()