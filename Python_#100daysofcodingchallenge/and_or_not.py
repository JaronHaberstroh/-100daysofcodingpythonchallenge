# and, or, not allow you to incorporate multiple checks in a single statement

# Ask user for height(cm), age(years), photo(y/n), midlife crisis

height = int(input("What is your height(cm)?: "))

if height >= 120:
    print("You are tall enough to ride the rollercoaster!")

    age = int(input("What is your age?: "))

    photo = input("Would you like a photo taken? Y/N: ")

    if age >= 18:
        if age >= 45 and age <= 55:
            if photo == "Y":
                print("Your total is 3 dollars")
            else:
                print("Your total is 0 dollars.")
        elif photo == "Y":
            print("Your total is 15 dollars.")
        else:
            print("Your total is 12 dollars.")
    elif age >= 12:
        if photo == "Y":
            print("Your total is 10 dollars.")
        else:
            print("Your total is 7 dolalrs.")
    else:
        if photo == "Y":
            print("Your total is 8 dollars.")
        else:
            print("Your total is 5 dolalrs.")
else:
    print("Sorry, you are not tall enough to ride this ride.") 