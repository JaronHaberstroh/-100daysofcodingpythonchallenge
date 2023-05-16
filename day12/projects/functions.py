import random
import os

def sel_ran_num():
    num = random.randint(1, 100)
    return num

def clear():
    os.system('clear')