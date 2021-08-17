from player import Player
from deck import Deck


def take_bet():
    repeat = True
    bet = 0
    while repeat:
        try:
            bet = int(input('Please place your bet: '))
        except ValueError:
            print('The bet value must be an integer')
            continue
        if bet > 0:
            repeat = False
        else:
            continue
    return bet


def hit(deck, hand):
    card = deck.deal()
    hand.add_card(card)


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    playing = True
    choice = input('Would you like to hit or stand? H/S')
    while choice is not 'H' or 'S':
        choice = input('Input invalid. Would you like to hit or stand? H/S')
    if choice == 'H':
        hit(deck, hand)
    elif choice == 'S':
        playing = False


def show_some(player, dealer):
    print('The player hand is: ')
    for card in player.hand.cards:
        print(card)
    print('The dealer hand is: ')
    print('1 hidden card')
    for card in dealer.hand.cards[1:]:
        print(card)


def show_all(player, dealer):
    print('The player hand is: ')
    for card in player.hand:
        print(card)
    print('The dealer hand is: ')
    for card in dealer.hand:
        print(card)


def main():
    # Print an opening statement
    print('Welcome to your 1v1 Blackjack, where you will be playing against the dealer.')
    player_name = input('Please enter a name for your player: ')
    player = Player(player_name)
    dealer = Player('Dealer')

    # Create & shuffle the deck, deal two cards to each player
    game_deck = Deck()
    game_deck.shuffle()
    hit(game_deck, player.hand)
    hit(game_deck, dealer.hand)
    hit(game_deck, player.hand)
    hit(game_deck, dealer.hand)

    # Prompt the Player for their bet
    bet = take_bet()
    player.place_bet(bet)

    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand

        # Show cards (but keep one dealer card hidden)

        # If player's hand exceeds 21, run player_busts() and break out of loop

        break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17

        # Show all cards

        # Run different winning scenarios

        # Inform Player of their chips total

        # Ask to play again

    pass


if __name__ == '__main__':
    main()
