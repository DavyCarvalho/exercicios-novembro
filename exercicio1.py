# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
# o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo:
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$

####################################################################################################


def formata_percentual(aliquota: float) -> float:
    """
    Função que formata uma aliquota em valor percentual.

    Args:
        aliquota: Valor da aliquota a ser formatado.

    Returns:
        O valor da aliquota formatado para percentual.
    """
    percentual = round(aliquota * 100, 2)

    return percentual


def calcula_desconto_inss(salario_bruto: float) -> (float, float):
    """
    Função que informa o percentual e o valor descontado do INSS de acordo com a tabela de
    contribuição dos segurados (EMPREGADO, EMPREGADO DOMÉSTICO E TRABALHADOR AVULSO).

    Args:
        salario_bruto: Valor do salário bruto.

    Returns:
        O percentual e o valor descontado do salário.
    """

    teto_inss = 6101.06

    # Verificando se o salário bruto é maior do que o teto do INSS.
    if salario_bruto > teto_inss:
        salario_bruto = teto_inss

    # TABELA DE CONTRIBUIÇÃO DOS SEGURADOS (EMPREGADO, EMPREGADO DOMÉSTICO E TRABALHADOR AVULSO).
    tabela_inss = (
        {
            'condicao': salario_bruto <= 1045,
            'aliquota': .075,
            'piso': 1045
        },
        {
            'condicao': 1045 < salario_bruto <= 2089.6,
            'aliquota': .09,
            'piso': 1045,
            'teto': 2089.6
        },
        {
            'condicao': 2089.6 < salario_bruto <= 3134.4,
            'aliquota': .12,
            'piso': 2089.6,
            'teto': 3134.4
        },
        {
            'condicao': 3134.4 < salario_bruto <= 6101.06,
            'aliquota': .14,
            'piso': 3134.4,
            'teto': 6101.06
        }
    )

    descontado_inss = 0
    aliquota = None
    # Calculando o valor de desconto do INSS de acordo com as alíquotas progressivas.
    for faixa_salarial in tabela_inss:
        if 'teto' not in faixa_salarial and not faixa_salarial['condicao']:
            descontado_inss += faixa_salarial['piso'] * faixa_salarial['aliquota']
        elif 'teto' not in faixa_salarial and faixa_salarial['condicao']:
            descontado_inss = salario_bruto * faixa_salarial['aliquota']
            aliquota = formata_percentual(faixa_salarial['aliquota'])
            break
        else:
            if faixa_salarial['condicao']:
                descontado_inss += (salario_bruto - faixa_salarial['piso']) * faixa_salarial['aliquota']
                aliquota = formata_percentual(faixa_salarial['aliquota'])
                break
            else:
                descontado_inss += (faixa_salarial['teto'] - faixa_salarial['piso']) * faixa_salarial['aliquota']

    return aliquota, round(descontado_inss, 2)


def calcula_desconto_irrf(salario_bruto: float, desconto_inss: float,
                          quantidade_dependentes: int = 0) -> (float, float):
    """
    Função que calcula o desconto do Imposto de Renda Retido na Fonte.

    Args:
        salario_bruto: Valor do salário bruto.
        desconto_inss: Valor do desconto do INSS.
        quantidade_dependentes: Quantidade de dependentes.

    Returns:
         O percentual e o valor do desconto do IRRF de acordo com a quantidade de dependentes.
    """
    # Aplicando o desconto do INSS no salário bruto.
    salario_bruto -= desconto_inss

    # Aplicando o desconto com base na quantidade de dependentes
    salario_bruto -= quantidade_dependentes * 189.59

    # Tabela de IRRF
    tabela_irrf = (
        {
            'condicao': 0 < salario_bruto <= 1903.98,
            'aliquota': 0,
            'deducao': 0
        },
        {
            'condicao': 1903.98 < salario_bruto <= 2826.65,
            'aliquota': 0.075,
            'deducao': 142.8
        },
        {
            'condicao': 2826.65 < salario_bruto <= 3751.05,
            'aliquota': 0.15,
            'deducao': 354.8
        },
        {
            'condicao': 3751.05 < salario_bruto <= 4664.68,
            'aliquota': 0.15,
            'deducao': 636.13
        },
        {
            'condicao': salario_bruto > 4664.68,
            'aliquota': 0.275,
            'deducao': 869.36
        }
    )

    # Calculando o valor de desconto do IRRF
    for faixa_salarial in tabela_irrf:
        if faixa_salarial['condicao']:
            print(salario_bruto, faixa_salarial['aliquota'], faixa_salarial['deducao'])
            desconto_irrf = (salario_bruto * faixa_salarial['aliquota']) - faixa_salarial['deducao']
            percentual = formata_percentual(faixa_salarial['aliquota'])

            return percentual, round(desconto_irrf, 2)


def calcula_desconto_sindicato(salario_bruto: float) -> float:
    """
    Calcula o desconto do sindicato (5%) de acordo com o salário bruto.

    Args:
        salario_bruto: Valor do salário bruto.

    Returns:
        O valor do desconto do sindicato.
    """
    # Calculando o valor do desconto.
    desconto_sindicato = salario_bruto * .05

    return desconto_sindicato


def calcula_salario_liquido(salario_bruto: float, desconto_inss: float,
                            desconto_irrf: float, desconto_sindicato: float) -> float:
    """
    Função que calcula o salário líquido com base em um salário bruto, levando em conta
    os descontos de imposto de renda, inss e sindicato.

    Args:
        salario_bruto: Valor do salário bruto.
        desconto_inss: Valor de desconto do INSS.
        desconto_irrf: Valor de desconto do Imposto de Renda.
        desconto_sindicato: Valor de desconto do Sindicato.

    Returns:
        O valor do salário líquido levando em conta os descontos.
    """
    # Calculando o salário líquido.
    salario_liquido = salario_bruto - desconto_inss - desconto_irrf - desconto_sindicato

    return round(salario_liquido, 2)


def main() -> None:
    # Inputs do usuário
    valor_hora = float(input('Digite o valor pago por hora: '))
    horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas: '))
    quantidade_dependentes = int(input('Digite a quantidade de dependentes: '))

    # Calculando o salário bruto.
    salario_bruto = valor_hora * horas_trabalhadas

    # Calculando o desconto do INSS
    percentual_inss, desconto_inss = calcula_desconto_inss(salario_bruto)

    # Calculando o desconto do IRRF
    percentual_irrf, desconto_irrf = calcula_desconto_irrf(salario_bruto, desconto_inss,
                                                           quantidade_dependentes)

    # Calculando o desconto do Sindicato
    desconto_sindicato = calcula_desconto_sindicato(salario_bruto)

    # Calculando o salário líquido.
    salario_liquido = calcula_salario_liquido(salario_bruto, desconto_inss, desconto_irrf,
                                              desconto_sindicato)

    # Print para o usuário.
    print(f'Salário Bruto: R$ {salario_bruto}\n'
          f'IR ({percentual_irrf}%): R$ {desconto_irrf}\n'
          f'INSS ({percentual_inss}%): R$ {desconto_inss}\n'
          f'Sindicato (5%): R$ {desconto_sindicato}\n'
          f'Salário Líquido: R$ {salario_liquido}')


if __name__ == '__main__':
    main()

