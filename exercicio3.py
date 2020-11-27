####################################################################################################

# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

####################################################################################################
def classifica_triangulo(a: float, b: float, c: float) -> None:
    """
    Classifica o triângulo em Equilátero, Isósceles, Escaleno e não é um triângulo.

    Args:
        a: Valor do lado a do triângulo.
        b: Valor do lado b do triângulo.
        c: Valor do lado c do triângulo.
    """
    if a < (b + c) and b < (a + c) and c < (a + b):
        if a == b and a == c:
            print("Triângulo Esquilátero")
        elif a == b or a == c or b == c:
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
    else:
        print("Não é um triângulo")


def main() -> None:
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    classifica_triangulo(a, b, c)


if __name__ == '__main__':
    main()
