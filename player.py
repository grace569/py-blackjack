from hand import Hand


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.chips = 100
        self.bet = 0

    def place_bet(self, amount):
        if amount > self.chips:
            print('Your chips are not enough to cover the bet')
        else:
            self.chips -= amount
            self.bet = amount

    def win_bet(self):
        self.chips += self.bet
        self.bet = 0

    def lose_bet(self):
        self.chips -= self.bet
        self.bet = 0
