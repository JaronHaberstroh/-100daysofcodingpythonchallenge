# Create an app that takes user input names and puts out a random name to pay the bill

# Ask for user input()

import random

names_string = input("Give me everybody's names, seperated by a comma. ")

# Split string into list

names = names_string.split(", ")

# Create random number for list index

num = random.randint(0, len(names) -1)

# print() random list index

print(f"{names[num]} is going to buy the meal today!")