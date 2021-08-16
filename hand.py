class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank is 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        self.value -= self.aces * 10

    def __str__(self):
        return f'The value of the hand is {self.value}'
