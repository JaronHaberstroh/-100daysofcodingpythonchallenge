# Print greeting

print("Welcome to Tip Calculator!\n")

# Ask for bill total and convert to float

bill = input("What is the total bill?: ")

bill = float(bill)

# Ask for tip precentage and convert to float

tip = input("What percentage of a tip would you like to leave?: ")

tip = float(tip)

# Convert tip whole number to percentage(decimal) value

tip = tip / 100

# Calculate tip amount

tip = tip * bill

# Ask for number of people to split bill and convert to int

people = input("How many people are splitting the bill?: ")

people = int(people)

# Calculate final amount and round to two decimal places

total = round((bill + tip) / people, 2)

# Print to console

print(total)