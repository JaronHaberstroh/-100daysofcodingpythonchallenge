# # If else statments will allow a function to take place if the conditional is met

height = int(input("What is your height in cm?: "))

# if height > 120: # checks that users input meets condition
#     print("You can ride the rollercoaster!")
# else: # else it runs an alternate section of code
#     print("Sorry, you must be taller to ride the ride.")

# # Nested if conditions allow to check for multiple data points

# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?: "))
#     if age >= 18:
#         print("Your ticket price is 12 dollars. Please have your money ready.")
#     elif age >= 12:
#         print("Your ticket price is 7 dollars. Please have your money ready.")
#     else:
#         print("Your ticket price is 5 dollars. Please have your money ready.")
# else:
#     print("Sorry, you must be taller to ride the ride.")

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?: "))
    if age >= 18:
        bill = 12
        print("Your ticket price is 12 dollars.")
    elif age >= 12:
        bill = 7
        print("Your ticket price is 7 dollars.")
    else:
        bill = 5
        print("Your ticket price is 5 dollars.")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}.")
else:
    print("Sorry, you must be taller to ride the ride.")