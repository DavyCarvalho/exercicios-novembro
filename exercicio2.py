####################################################################################################

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
# área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é
# vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3
#     situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de
#     folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
#

####################################################################################################
from math import ceil


def calcula_quantidade_litros(area_pintada: float) -> float:
    """
    Calcula a quantidade de litros de tinta necessários para pintar uma área informada.

    Args:
         area_pintada: Tamanho da área em m2.

    Returns:
        Quantidade de litros.
    """
    # Calculando a quantidade de litros necessários.
    quantidade_litros = area_pintada / 6

    # Acrescentando os 10% de folga
    quantidade_litros *= 1.1

    return round(quantidade_litros, 2)


def calculo_quantidade_latas(quantidade_litros: float) -> int:
    """
    Calcula a quantidade de latas necessárias para pintar a área informada.

    Args:
        quantidade_litros: Quantidade de litros de tinta necessários.

    Returns:
         A quantidade de latas necessárias.
    """
    quantidade_latas = ceil(quantidade_litros / 18)

    return quantidade_latas


def calculo_quantidade_galoes(quantidade_litros: float) -> int:
    """
    Calcula a quantidade de galões necessários para pintar a área informada.

    Args:
        quantidade_litros: Quantidade de litros de tinta necessários.

    Returns:
         A quantidade de galões necessárias.
    """
    quantidade_galoes = ceil(quantidade_litros / 3.6)

    return quantidade_galoes


def calculo_quantidade_latas_galoes(quantidade_litros: float) -> (int, int):
    """
    Calcula a quantidade de latas/galões necessárias para pintar a área informada com
    o mínimo de desperdício.

     Args:
         quantidade_litros: Quantidade de litros necessários para pintar aquela área.

    Return:
        Uma tupla com a quantidade de galões e tintas necessárias com o mínimo de desperdício.
    """
    # Calculando a quantidade de latas e o resto
    quantidade_latas, resto = divmod(quantidade_litros, 18)

    # Calculando a quantidade de galões
    quantidade_galoes = calculo_quantidade_galoes(resto)

    return int(quantidade_galoes), quantidade_galoes


def calculo_preco_latas(quantidade_latas: int) -> float:
    """
    Calcula o preço total de acordo com a quantidade de latas fornecidas.

    Args:
        quantidade_latas: Quantidade de latas.

    Returns:
        Preço total.
    """
    return round(quantidade_latas * 80, 2)


def calculo_preco_galoes(quantidade_galoes: int) -> float:
    """
    Calcula o preço total de acordo com a quantidade de galões fornecidas.

    Args:
        quantidade_galoes: Quantidade de galões.

    Returns:
        Preço total.
    """
    return round(quantidade_galoes * 25, 2)


def main() -> None:
    # Input do usuário
    area_pintada = float(input('Digite o tamanho da área a ser pintada (m2): '))

    quantidade_litros = calcula_quantidade_litros(area_pintada)

    # Opção 1
    quantidade_latas = calculo_quantidade_latas(quantidade_litros)
    preco_latas = calculo_preco_latas(quantidade_latas)
    # Opção 2
    quantidade_galoes = calculo_quantidade_galoes(quantidade_litros)
    preco_galoes = calculo_preco_galoes(quantidade_galoes)
    # Opção 3
    quantidade_latas_minimo, quantidade_galoes_minimo = calculo_quantidade_latas_galoes(quantidade_litros)
    preco_latas_minimo = calculo_preco_latas(quantidade_latas_minimo)
    preco_galoes_minimo = calculo_preco_galoes(quantidade_galoes_minimo)
    preco_total = preco_galoes_minimo + preco_latas_minimo

    print(f'Opção 1)\n'
          f'Quantidade de latas: {quantidade_latas}\n'
          f'Preço total das latas: R$ {preco_latas}\n'
          f'Opção 2)\n'
          f'Quantidade de galões: {quantidade_galoes}\n'
          f'Preço total dos galões: R$ {preco_galoes}\n'
          f'Opção 3)\n'
          f'Quantidade de latas: {quantidade_latas_minimo}\n'
          f'Quantidade de galões: {quantidade_galoes_minimo}\n'
          f'Preço total: R$ {preco_total}')


if __name__ == '__main__':
    main()