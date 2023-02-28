import functions
import art

functions.clear()
run = True

while run:
    # Greeting
    print(art.logo)
    print("Welcome to Caesar Cipher!")
    
    # Ask encrypt/decrypt
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    # Ask for message
    text = input("Type your message:\n").lower()

    # Ask for cipher shift amount
    shift = int(input("Type the shift number:\n"))
    # Modify shift by modules 26 if in excess of alphabet
    shift = shift % 26

    # Call Caesar 
    functions.caesar(text=text, shift=shift, direction=direction)

    # Ask user if they would like to continue
    x = ""

    while x is not "y" and x is not "n":
        x = input("Would you like to go again? Y or N:").lower()

        if x == "n":
            run = False
            break
        elif x == "y":
            break
        else:
            print("You need to choose 'Y' if you wish to continue or 'N' if you wish to quit")