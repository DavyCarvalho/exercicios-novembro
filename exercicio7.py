####################################################################################################

# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em
# branco), conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u.


####################################################################################################
def main() -> None:
    vogais = ('a', 'e', 'i', 'o', 'u')

    frase = input('Digite uma frase: ').lower()

    espacos_em_branco = frase.count(' ')

    quantidade_vogais = 0
    for vogal in vogais:
        quantidade_vogais += frase.count(vogal)

    print(f'Quantidade de espaços em branco: {espacos_em_branco}')
    print(f'Quantidade de vogais: {quantidade_vogais}')


if __name__ == '__main__':
    main()
