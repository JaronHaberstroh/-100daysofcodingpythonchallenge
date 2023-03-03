import function
import art
import time

# print() logo and greeting
print(f"{art.logo}/n/nWelcome to the secret auction!")

# Sleep
time.sleep(3)

# Clear screen
function.clear()

# take_bids()
bids = function.take_bids()

# calc_highest_bid()
winner = function.calc_highest_bid(bids)

function.clear()

print(f"{winner[0]} has won the auction with a bid of {winner[1]}!")