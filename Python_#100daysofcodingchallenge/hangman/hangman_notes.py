# Hangman notes
import random

# Generate a random word

# Create Variable word_list
word_list = ["bandwagon", "beekeeper", "haphazard", "razzmatazz"]

# Choose random word
word = random.choice(word_list)

# Create list to store image
image = []

for letter in range(len(word)):
    image.append("_")
print(image)

stages = 0

# While loop
while "_" in image and stages < 6:
# Ask user to guess letter
    guess = input("Guess a letter.").lower()

    i = 0

    equal = 0

    for letter in word:
        if letter == guess:
            image[i] = guess
        i += 1
    if guess not in word:
        stages += 1

    print(image)

if stages < 6:
    print("You've won!")
else:
    print("You've lost")
# Generate image

# Create a while loop that determines the end of the game
# While word not guessed or x wrong guess not met continue

# If correct guess continue / draw image
# If wrong guess add to wrong guess variable

# Game ends when word guessed or wrong guess variable exceeded