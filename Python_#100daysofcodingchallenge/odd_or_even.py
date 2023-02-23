# Ask user for a number and convert it to an int

number = int(input("Which number would you like to check if it's odd or even?: "))

# Use modulo operator to determin if the int has a remainder

number = number % 2

# Create an if/else statement that tell the user if their number is odd or even

if number == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
