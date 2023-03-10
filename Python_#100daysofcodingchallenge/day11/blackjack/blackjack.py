from art import logo
from functions import clear, deal, hit, check_bust, blackjack

def main():
    # clear() console for new games
    clear()

    # print() lgog
    print(logo)
    
    # Create variables for game
    player_bust = False
    dealer_bust = False

    # Deals cards to players
    dealer, player = deal()
    
    # Check for Blackjacks and print winner if theres is one
    statement, winner = blackjack(dealer, player)
    if winner == True: print(statement)

    # Deal player cards so long as no Blackjacks and player hasn't bust.
    while not player_bust and not winner:
        # Check if player bust and if so end the game.
        if check_bust(player) == False:
            print(f"Player shows: {*player,} = {sum(player)}: Player busts")
            player_bust = True
            break
        print(f"Dealer hand: (H, {dealer[1]})\nPlayer hand: {*player,}")
        # Ask player if they would like a card and hit or break loop on stand.
        if input(f"Would you like to hit on {sum(player)}? 'Y' or 'N': ").lower() == "y":
            player.append(hit())
        else: 
            break
    
    # Deal computer cards if no Blackjack and player didn't bust. Dealer stands on 17.
    while not player_bust and sum(dealer) < 17 and not winner:
        dealer.append(hit())
        # Check if dealer bust and end game if so.
        if check_bust(dealer) == False:
            print(f"Dealer shows: {*dealer,} = {sum(dealer)}: Dealer bust")
            dealer_bust = True
            break

    # Check for winners assuming one hasn't already been declared.
    if not dealer_bust and not player_bust and not winner:
        if sum(dealer) == sum(player):
            print(f" Dealer shows: {*dealer,} = {sum(dealer)}\nPlayer shows: {*player,} = {sum(player)}: Player wins on ties.")
        elif sum(dealer) > sum(player):
            print(f"Dealer shows: {*dealer,} = {sum(dealer)}: Dealer wins\nPlayer shows: {*player,} = {sum(player)}")
        else:
            print(f"Dealer shows: {*dealer,} = {sum(dealer)}:\nPlayer shows: {*player,} = {sum(player)}: Player wins")

    # Check if player would like to continue playing. 
    if input("Would you like to play again? 'Y' or 'N': ").lower() == "y":
        main()
       
main()
