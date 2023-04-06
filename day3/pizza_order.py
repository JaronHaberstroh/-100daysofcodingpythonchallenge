# Greet user

print("Welcome to python pizza!")

# Ask user for pizza size s/m/l
# Ask user if extra cheese
# Ask user if pepperoni

size = input("Which size pizza would you like? S, M, or L: ")
pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

final = "Your final bill is: $"

if size == "L":
    bill = 25   
    if pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"{final}{bill}")
        else:
            print(f"{final}{bill}")
    else:
        if extra_cheese == "Y":
            bill += 1
            print(f"{final}{bill}")
        else:
            print(f"{final}{bill}")
elif size == "M":
    bill = 20  
    if pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
            print(f"{final}{bill}")
        else:
            print(f"{final}{bill}")
    else:
        if extra_cheese == "Y":
            bill += 1
            print(f"{final}{bill}")
        else:
            print(f"{final}{bill}")
else:
    bill = 15  
    if pepperoni == "Y":
        bill += 2
        if extra_cheese == "Y":
            bill += 1
            print(f"{final}{bill}")
        else:
            print(f"{final}{bill}")
    else:
        if extra_cheese == "Y":
            bill += 1
            print(f"{final}{bill}")
        else:
            print(f"{final}{bill}")