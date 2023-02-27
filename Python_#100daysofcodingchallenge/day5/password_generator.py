import random

# Create a password generator

# Create lists of letters, symbols, and numbers

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "+", "<", ">", "?", "/", "~"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# Ask user for number of letters, symbols, and numbers in pass

num_let = int(input("How many letters would you like in your password?\n"))

num_sym = int(input("How many symbols would you like?\n"))

num_num = int(input("How many numbers would you like?\n"))

# Create variable to store pass

password = ""

# Generate pass

for let in range(0, num_let):
    password += random.choice(letters)

for sym in range(0, num_sym):
    password += random.choice(symbols)

for num in range(0, num_num):
    password += random.choice(numbers)

# Scramble pass

password = list(password)
random.shuffle(password)

# print() pass

print(''.join(password))