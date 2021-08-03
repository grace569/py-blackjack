from card import Card


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.chips = 100
        self.bet = 0

    def place_bet(self, amount):
        pass

    def win_bet(self, amount):
        pass

    def lose_bet(self, amount):
        pass
