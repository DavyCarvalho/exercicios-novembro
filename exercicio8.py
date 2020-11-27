####################################################################################################

# construa um analisador das 5 principais combinações de mãos do poker.
# Para isso utilize como base as classes descritas em:
# https://penseallen.github.io/PensePython2e/18-heranca.html
# considere como regra o poker fechado, em que a mão do jogador, já tem a combinação de 5 cartas :)

####################################################################################################
import random


class Card:
    """Representa uma carta do baralho."""
    suit_names = ['Paus', 'Ouro', 'Copas', 'Espadas']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9',
                  '10', 'Valete', 'Dama', 'Rei']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return f'{Card.rank_names[self.rank]} de {Card.suit_names[self.suit]}'

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank

        return t1 < t2


class Deck:
    """Representa um baralho."""
    def __init__(self):
        self.cards = []

        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()


class Hand(Deck):
    """Representa uma mão de cartas."""
    def __init__(self, cards: list, label: str = ''):
        self.cards = cards or []
        self.label = label

    def print_cards(self):
        for card in self.cards:
            print(card)

    def get_suits(self):
        suits = []
        for card in self.cards:
            suits.append(card.suit)

        return suits

    def get_ranks(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)

        return ranks


def royal_flush(suits: list, ranks: list) -> bool:
    """
    Verifica se a mão é um royal flush. Um royal flush consiste na
    sequência de Ás, Rei, Dama, Valete e Dez do mesmo naipe.

    Args:
        suits: Uma lista com os naipes em números inteiros (0-3).
        ranks: Uma lista com os números das cartas (1-13).

    Returns:
        True se for um Royal Flush, senão, retorna False.
    """
    royal_ranks = [1, 10, 11, 12, 13]

    is_royal = True

    # Verificando se os naipes são iguais.
    if suits.count(suits[0]) != 5:
        is_royal = False

    # Verificando se possui as cartas corretas.
    for rank in ranks:
        if rank not in royal_ranks or ranks.count(rank) > 1:
            is_royal = False
            break

    return is_royal


def straight_flush(suits: list, ranks: list) -> bool:
    """
    Verifica se a mão é um straight flush. Um straight flush consiste
    em 5 cartas em ordem númerica, todas do mesmo naipe.

    Args:
        suits: Uma lista com os naipes em números inteiros (0-3).
        ranks: Uma lista com os números das cartas (1-13).

    Returns:
        True se for um Straight Flush, senão, retorna False.
    """
    is_straight_flush = True

    # Verificando se os naipes são iguais.
    if suits.count(suits[0]) != 5:
        is_straight_flush = False

    # Estabelecendo o menor valor das cartas e criando uma sequencia de 5 cartas a partir disso.
    min_number = min(ranks)
    sequence = range(min_number, min_number + 5)

    # Verificando se os números das cartas estão em sequência.
    for rank in ranks:
        if rank not in sequence or ranks.count(rank) > 1:
            is_straight_flush = False
            break

    return is_straight_flush


def quadra(ranks: list) -> bool:
    """
    Verifica se a mão é uma quadra. Uma quadra consiste em quatro
    cartas de mesmo valor, e uma outra carta como 'Kicker'.
    Args:
        ranks: Uma lista com os números das cartas (1-13).

    Returns:
        True se for uma quadra, senão, retorna False.
    """
    is_quadra = False

    # Verificando se a mão possui quatro cartas com o mesmo valor
    for rank in ranks:
        if ranks.count(rank) == 4:
            is_quadra = True
            break

    return is_quadra


def full_house(ranks: list) -> bool:
    """
    Verifica se a mão é um full house. Um full house consiste em três
    cartas de mesmo valor, e duas outras cartas diferentes de mesmo
    valor.

    Args:
        ranks: Uma lista com os números das cartas (1-13).

    Returns:
        True se for um full house, senão, retorna False.
    """
    for rank in ranks:
        if ranks.count(rank) == 2:
            break
    else:
        return False

    for rank in ranks:
        if ranks.count(rank) == 3:
            break
    else:
        return False

    return True


def flush(suits: list) -> bool:
    """
    Verifica se a mão é um flush. Um flush consiste em cinco cartas
    do mesmo naipe.

    Args:
        suits: Uma lista com os naipes em números inteiros (0-3).

    Returns:
        True se for um flush, senão, retorna False.
    """
    is_flush = True

    if suits.count(suits[0]) != 5:
        is_flush = False

    return is_flush


def main() -> None:
    # Royal Flush

    # Instânciando as cartas
    card1 = Card(1, 1)
    card2 = Card(1, 10)
    card3 = Card(1, 11)
    card4 = Card(1, 12)
    card5 = Card(1, 13)

    # Instânciando a mão
    royal_hand = Hand([card1, card2, card3, card4, card5], 'Royal Flush')

    # Obtendo os naipes e valores das cartas
    ranks, suits = royal_hand.get_ranks(), royal_hand.get_suits()

    # Printando as cartas
    royal_hand.print_cards()

    print('#'*100)

    if royal_flush(suits, ranks):
        print('Royal Flush')
    # ============================================================================================ #
    # Flush

    if flush(suits):
        print('Flush')

    print('#' * 100)
    # ============================================================================================ #
    # Straight Flush

    # Instânciando as cartas
    card1 = Card(1, 9)
    card2 = Card(1, 10)
    card3 = Card(1, 11)
    card4 = Card(1, 12)
    card5 = Card(1, 13)

    # Instânciando a mão
    straight_flush_hand = Hand([card1, card2, card3, card4, card5], 'Straight Flush')

    # Obtendo os naipes e valores das cartas
    ranks, suits = straight_flush_hand.get_ranks(), straight_flush_hand.get_suits()

    # Printando as cartas
    straight_flush_hand.print_cards()

    print('#' * 100)

    if straight_flush(suits, ranks):
        print('Straight Flush')

    print('#' * 100)
    # ============================================================================================ #
    # Quadra

    # Instânciando as cartas
    card1 = Card(1, 7)
    card2 = Card(1, 1)
    card3 = Card(2, 1)
    card4 = Card(0, 1)
    card5 = Card(3, 1)

    # Instânciando a mão
    quadra_hand = Hand([card1, card2, card3, card4, card5], 'Quadra')

    # Obtendo os naipes e valores das cartas
    ranks = quadra_hand.get_ranks()

    # Printando as cartas
    quadra_hand.print_cards()

    print('#' * 100)

    if quadra(ranks):
        print('Quadra')

    print('#' * 100)
    # ============================================================================================ #
    # Full House

    # Instânciando as cartas
    card1 = Card(0, 1)
    card2 = Card(1, 1)
    card3 = Card(2, 1)
    card4 = Card(0, 2)
    card5 = Card(3, 2)

    # Instânciando a mão
    full_house_hand = Hand([card1, card2, card3, card4, card5], 'Full House')

    # Obtendo os naipes e valores das cartas
    ranks = full_house_hand.get_ranks()

    # Printando as cartas
    full_house_hand.print_cards()

    print('#' * 100)

    if full_house(ranks):
        print('Full House')

    print('#' * 100)


if __name__ == '__main__':
    main()



