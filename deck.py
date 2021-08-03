import random

from card import Card


class Deck:
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in self.suits:
            for rank in self.ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    def __str__(self):
        return 'A deck of ' + str(len(self.deck)) + ' cards'

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
