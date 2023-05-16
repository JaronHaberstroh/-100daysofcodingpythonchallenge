import os

def clear():
    os.system("clear")

def take_bids():

    # Create variables
    taking_bids = True
    bids = []

    # While loop to take_bids() while true
    while taking_bids:
        # clear() to hide bids
        clear()

        # Ask for bidder name and amount
        bidder = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))

        # .append() bids list with new bidder info 
        bids.append([{bidder: bid}])

        # Create more_bidders variable
        more_bidders = ""

        # End loop if no new bidders
        while more_bidders != "y" and more_bidders != "n":
            # Ask if new bidder
            more_bidders = input("Is there another bidder? Y or N: ").lower()
            if more_bidders == "n":
                taking_bids = False
                return bids
            elif more_bidders == "y":
                continue
            else:
                print("You must answer either Y or N")

def calc_highest_bid(bids):
    # Create variable to store highest bid
    highest_bid = 0
    winner = ""

    # Loop through list
    for index in range(len(bids)):
        for dic in bids[index]:
            for key in dic:
                if highest_bid < dic[key]:
                    highest_bid = dic[key]
                    winner = key
    return winner, highest_bid