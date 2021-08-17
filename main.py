from player import Player
from deck import Deck
from hand import Hand


def hit(deck, hand):
    card = deck.deal()
    hand.add_card(card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    while True:
        choice = input('Would you like to hit or stand? H/S  ')
        if choice[0].lower() == 'h':
            hit(deck, hand)
            break
        elif choice[0].lower() == 's':
            print('Player stand, dealer\'s play')
            playing = False
            break
        else:
            print('Input invalid, pleas try again. ')
            continue


def show_some(player, dealer):
    print('The player hand is: ')
    for card in player.hand.cards:
        print(card)
    print(f'Player\'s hand value is {player.hand.value}')
    print('The dealer hand is: ')
    print('1 hidden card')
    for card in dealer.hand.cards[1:]:
        print(card)


def show_all(player, dealer):
    print('The player hand is: ')
    for card in player.hand.cards:
        print(card)
    print(f'Player\'s hand value is {player.hand.value}')
    print('The dealer hand is: ')
    for card in dealer.hand.cards:
        print(card)
    print(f'Dealer\'s hand value is {dealer.hand.value}')


def player_busts(player):
    print(f'Player {player.name} busted!')
    player.lose_bet()


def player_wins(player):
    print(f'Player {player.name} won!')
    player.win_bet()


def dealer_busts(player):
    print(f'Dealer busted!')
    player.win_bet()


def dealer_wins(player):
    print(f'Dealer won!')
    player.lose_bet()


def push():
    print('It\'s a draw between the player and dealer. It\'s a push!')


def play_game(player):
    while True:
        player.hand = Hand()
        dealer = Player('Dealer')
        global playing

        # Create & shuffle the deck, deal two cards to each player
        game_deck = Deck()
        game_deck.shuffle()
        hit(game_deck, player.hand)
        hit(game_deck, dealer.hand)
        hit(game_deck, player.hand)
        hit(game_deck, dealer.hand)

        # Prompt the Player for their bet
        player.place_bet()

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(game_deck, player.hand)
            # Show cards (but keep one dealer card hidden)
            show_some(player, dealer)
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player.hand.value > 21:
                player_busts(player)
                break
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player.hand.value <= 21:
            while dealer.hand.value < 17:
                hit(game_deck, dealer.hand)

            # Show all cards
            show_all(player, dealer)
            if dealer.hand.value > 21:
                dealer_busts(player)

            # Run different winning scenarios
            if player.hand.value == dealer.hand.value:
                push()
            elif player.hand.value < dealer.hand.value:
                dealer_wins(player)
            elif player.hand.value > dealer.hand.value:
                player_wins(player)

        print(f'Player {player.name}, you now have {player.chips} chips. ')

        new_game = input('Would you like to play again? Y/N ')
        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    playing = True
    print('Welcome to your 1v1 Blackjack, where you will be playing against the dealer.')
    player_name = input('Please enter a name for your player: ')
    game_player = Player(player_name)
    play_game(game_player)
