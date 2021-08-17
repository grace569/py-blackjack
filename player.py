from hand import Hand


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.chips = 100
        self.bet = 0

    def place_bet(self):
        repeat = True
        while repeat:
            try:
                amount = int(input('Please place your bet: '))
            except ValueError:
                print('The bet value must be an integer')
                continue
            if amount > self.chips:
                print('Your chips are not enough to cover the bet')
                continue
            elif amount < 0:
                print('The bet must be greater than 0')
                continue
            elif amount > 0:
                repeat = False
                self.bet = amount
            else:
                continue

    def win_bet(self):
        self.chips += self.bet
        self.bet = 0

    def lose_bet(self):
        self.chips -= self.bet
        self.bet = 0
