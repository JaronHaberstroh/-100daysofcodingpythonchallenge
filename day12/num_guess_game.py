from functions import clear
# from art import logo
import random

# Create variables for easy and hard game guesses
HARD_GAME = 5
EASY_GAME = 10

# Create variable for win/lose
WIN = "Congratulations, you've corretly guessed the number!"
LOSE = "You've run out of guesses. Better luck next time"

# Create variable for greater/less than guess
GREATER = f"Your guess is greater than the number."
LESS = f"Your guess is less than the number."

# PLAY_AGAIN variable
PLAY_AGAIN = None

def play():
    # Establish random number 0-100
    ran_num = random.randint(1, 100)

    # Determine difficulty level of game
    game_dif = input("Should the game be easy or hard?: ").lower()

    # Set counter to number of guesses for game Hard or Easy
    num_guesses = EASY_GAME if game_dif == "easy" else HARD_GAME

    # Allow player to guess till out of guesses (lose) or num selected (win)
    correct = 0
    clear()
        
    while num_guesses > 0:
        guess = int(input("Guess a number between 1 and 100.: "))

        if guess == ran_num:
            correct = 1
            break
        else:
            num_guesses -= 1
            print(GREATER if guess > ran_num else LESS)


    # print() win/lose
    print(WIN if correct == 1 else LOSE)

    PLAY_AGAIN = play() if input("Would you like to play again? 'Y' or 'N': ").lower() == 'y' else print("Thanks for playing.")

    PLAY_AGAIN

play()