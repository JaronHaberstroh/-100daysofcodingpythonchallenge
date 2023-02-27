import os
import random
import wordlist

def random_word():
    word = random.choice(wordlist.word_list)
    return word

def create_display(word):
    display = []
    for letter in word:
        display.append("_")
    return display

def clear():
    os.system("clear")
