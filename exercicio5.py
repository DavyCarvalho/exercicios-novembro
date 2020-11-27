####################################################################################################

# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os
# resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um
# vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos
# dados.

####################################################################################################
from random import randrange


def lanca_dado() -> list:
    """Retorna uma lista com os resultados do lançamento aleatório de 100 dados."""
    lista_resultados = [randrange(1, 7) for _ in range(100)]

    return lista_resultados


def main() -> None:
    resultados = lanca_dado()

    print('Dados jogados:')
    for i in range(1, 7):
        quantidade = resultados.count(i)
        print(f'{i}: {quantidade}')


if __name__ == '__main__':
    main()
