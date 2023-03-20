from data import data
from art import logo, vs
from random import choice
from os import system


def clear():
    system('clear')


def rand_celeb(data, num_of_choice=1):
    '''Takes input of list of dictionaries and return random number of coices determined'''
    person = []
    for num in range(0, num_of_choice):
        person.append(choice(data))
    return person


def display_battle(celebs, score):
    '''Prints to screen current battle using list'''
    print(logo)
    if score > 0:
        print(f"Correct, Your current score is {score}.")
    for num in range(0, len(celebs)):
        if num == 1:
            print(vs)
        print(
            f"{celebs[num]['name']} a {celebs[num]['description']} from {celebs[num]['country']}")


def user_choice(celebs):
    '''Allows user to make a selection between two choices'''
    choice = ""
    while True:
        if choice != "":
            print(
                f"You must choose 'A' for {celebs[0]['name']} or 'B' for {celebs[1]['name']}")
        choice = input(
            "Which has a greater follower count? 'A' or 'B': ").upper()
        if choice == 'A' or choice == 'B':
            return True if choice == 'A' else False


def check_choice(celebs, choice):
    if int(celebs[0]['follower_count']) > int(celebs[1]['follower_count']) and choice == True:
        return 1, True
    elif int(celebs[1]['follower_count']) > int(celebs[0]['follower_count']) and choice == False:
        return 0, True
    else:
        return None, False


def game():
    score = 0
    celebs = rand_celeb(data=data, num_of_choice=2)

    while True:
        # print() person a vs person
        clear()
        display_battle(celebs, score)

        # allow user to choose
        user_input = user_choice(celebs)

        # check choice
        results = check_choice(celebs, user_input)

        # if results False end else redistribute celebs for new battle
        if results[1] == False:
            print(f"Sorry you've chosen wrong. Final score: {score}")
            break
        else:
            score += 1
            del celebs[results[0]]
            celebs += (rand_celeb(data))


game()
