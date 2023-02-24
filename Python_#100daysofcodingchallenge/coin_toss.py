# Create a coin toss generator

# Create a RNG that picks either 1 or 2

import random

num = random.randint(1, 2)

if num == 1:
    print("You flipped heads.")
else:
    print("You flipped tails.")
