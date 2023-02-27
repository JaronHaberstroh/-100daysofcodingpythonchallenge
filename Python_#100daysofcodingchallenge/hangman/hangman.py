import random
import art
import wordlist
import functions

# Create game variable
game = True

# Start game
while game:

    functions.clear()

    # Select random word for game
    word = functions.random_word()

    # Create variables for game
    display = functions.create_display(word)
    wrong = 0
    guesses = []

    # Show game logo
    print(f"{art.logo}\n{art.images[wrong]}\n{display}")

# Game logic

    while "_" in display and wrong < 6:
        # Ask user for letter
        guess = input("Guess a letter.:  ").lower()

        functions.clear()

        # Check if guess is in guesses
        if guess not in guesses:
            for index, letter in enumerate(word):
                if guess == letter:
                    display[index] = guess
            if guess not in word:
                wrong += 1
            if guess in word:
                print(f"{art.logo}\n{art.images[wrong]}\n{display}\n{guess} is in the word.")
            else:
                print(f"{art.logo}\n{art.images[wrong]}\n{display}\n{guess} is not in the word")
        else:
            print(f"{art.logo}\n{art.images[wrong]}\n{display}\nYou've alreaded guessed {guess}.")
        guesses.append(guess)

    # Determin if game was won or lost
    if wrong == 6:
        print(f"The word was {word}. Sorry, your man hung so you've lost.")
    else:
        print(f"You correctly guessed {word}. You've saved your man and won.")
    
    # Ask user to play again
    again = input("Would you like to play again? Y or N:").lower()

    if again == "y":
        continue
    elif again == "n":
        game = False
    else:
        print("Perhaps choosing letters is to hard for you!\nWould you like to play again? Y or N:")