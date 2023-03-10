from random import choice
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal():
    '''Returns a string of two randomly chosen ints from list'''
    dealer = []
    player = []
    for num in range(0, 2):
        dealer.append(choice(cards))
        player.append(choice(cards))
    return dealer, player
    
def hit():
    '''Returns randomly chosen int from list'''
    return choice(cards)

def clear():
    '''Clear console'''
    os.system("clear")

def check_bust(cards):
    '''Takes a list of int as input and returns True if there sum is < 21 and False if > 21'''
    if sum(cards) < 21:
        return True
    elif sum(cards) > 21:
        for index, card in enumerate(cards):
            if card ==11:
                cards[index] = 1
        return False

def blackjack(dealer, player):
    '''Takes 2 lists as input and returns a print statement and True or False depend on if there is a player with 21 or not.'''
    dealer_blackjack = "Dealer has Blackjack. Dealer wins!"
    player_blackjack = "Player has Blackjack. Player wins!"
    push = "Both players have Blackjack. It's a push nobody wins."
    if sum(dealer) == 21 and sum(player) == 21: return push, True
    elif sum(dealer) == 21: return dealer_blackjack, True
    elif sum(player) == 21: return player_blackjack, True
    else: return None, False

