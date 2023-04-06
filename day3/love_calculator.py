# create a calculater that determines the number of times the letters 
# t, r, u, e, l, o, v, e occur in 2 names

# print() greeting

print("Welcome to Love Calculator!")

# Ask user for both names

name1 = input("What is your name? \n") 
name2 = input("What is thier name? \n")

# Use lower() to make all letters lower case and easier to count

name1 = name1.lower()
name2 = name2.lower()

# Create variables to store scores

total1 = 0
total2 = 0

# Add together the scores

total1 += (name1 + name2).count("t")
total1 += (name1 + name2).count("r")
total1 += (name1 + name2).count("u")
total1 += (name1 + name2).count("e")
total2 += (name1 + name2).count("l")
total2 += (name1 + name2).count("o")
total2 += (name1 + name2).count("v")
total2 += (name1 + name2).count("e")

# Concatenate the 2 int for your final score

total = int(str(total1) + str(total2))

# print() scores along with message for user
if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
    