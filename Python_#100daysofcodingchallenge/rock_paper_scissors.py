import random

# Ask user for choice of rock, paper, scissors

user = input("What do you choose? rock, paper, or scissors?").lower()

# RNG for computer choice rock, paper, scissors

computer = random.randint(1, 3)

if computer == 1:
    computer = "rock"
elif computer == 2:
    computer = "paper"
else:
    computer = "scissors"

# print() result 

# user rock

if user == "rock":
    if computer == "paper":
        print("Paper beats rock. You lose.")
    elif computer == "scissors":
        print("Rock beats scissors. You win!")
    else:
        print("You both chose rock. It's a tie.")
# user paper

elif user == "paper":
    if computer == "scissors":
        print("Scissors beats paper. You lose.")
    elif computer == "rock":
        print("Paper beats rock. You win.")
    else:
        print("You both chose paper. It's a tie.")
# user scissors

elif user == "scissors":
    if computer == "rock":
        print("Rock beats scissors. You lose.")
    elif computer == "paper":
        print("Scissors beats paper. You win.")
    else:
        print("You both chose scissors. It's a draw.")
# Invalid choice

else:
    print("Perhaps this choice is too great for you. You might enjoy a simpler game like Tic-Tac-Toe.")