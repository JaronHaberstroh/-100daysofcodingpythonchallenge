from os import system
from time import sleep
from data import MENU, resources, operations, COINS


def clear():
    '''clears command line'''
    system('clear')


def main_menu():
    '''generates user main menu and prompts user to provide a valid selection

    Returns:
        str: valid user choice from MENU selection or operations
    '''
    while True:
        choice = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        if choice in MENU or choice in operations:
            return choice


def hidden_op(choice):
    '''Resolves hidden operators.

    Args:
        choice (str): user_choice
    '''
    if choice == "off":
        quit()
    if choice == "report":
        print(resources)
        if input() == "return":
            return
    if choice == "maintain":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        resources.pop("money")


def check_resources(choice):
    '''checks if machine contains enough resources to create coice beverage

    Args:
        choice (str): user beverage choice

    Returns:
        bol: resources low if False else True
    '''
    for key, value in MENU[choice]["ingredients"].items():
        if value > resources[key]:
            return False
    return True


def subtract_resources(choice):
    '''subtract resources from available

    Args:
        choice (str): user beverage choice
    '''
    for key, value in MENU[choice]["ingredients"].items():
        resources[key] -= value


def low_resources(choice):
    '''return list of low resources for user beverage choice

    Args:
        choice (str): user beverage choice

    Returns:
        list: list of all low resources
    '''
    low_list = []
    for key, value in MENU[choice]["ingredients"].items():
        if value > resources[key]:
            low_list.append(key)
    return low_list


def take_money(cost, coins):
    '''takes a list of coins and subtracts their value from cost

    Args:
        cost (int): cost of user beverage choice
        coins (list): list of coins user inserted

    Returns:
        int: remaining cost
    '''
    for coin in coins:
        if coin in COINS:
            cost -= COINS[coin]
    return round(cost, 3)


def return_amount(cost):
    '''determine coins to return based on user instrted coin value

    Args:
        cost (int): amount inserted for payment by user

    Returns:
        list: coins return to user
    '''
    coins_list = []
    cost *= -1
    while cost >= .25:
        coins_list.append("quarter")
        cost -= .25
    while cost >= .10:
        coins_list.append("dime")
        cost -= .1
    while cost >= .05:
        coins_list.append("nickle")
        cost -= .05
    while cost >= .01:
        coins_list.append("penny")
        cost -= .01
    return coins_list


def handle_payment(cost):
    '''handles payments and returns 

    Args:
        cost (int): cost of user selected beverage

    Returns:
        bol: if payment successful 'True' else 'False'
    '''
    total_coins = []
    while True:
        clear()
        insert_coins = []
        insert_coins = input(
            f"You owe ${cost}. Insert change; quarter, dime, nickle, penny): ")
        if insert_coins == "refund":
            print(f"{total_coins} dispensed in coin return.")
            sleep(3)
            break
        insert_coins = insert_coins.split()
        total_coins.append(insert_coins)
        cost = take_money(cost, insert_coins)
        if cost == 0:
            payment_token = True
            break
        elif cost < 0:
            coins_returned = return_amount(cost)
            print(f"{coins_returned} dispensed in coin return")
            payment_token = True
            break
        else:
            payment_token = False
    return payment_token


def main():
    '''
    complete coffee machine logic.
    drink options; espresso/latte/cappuccino. 
    hidden options; off/report(return)/maintain.
    '''
    sales = 0
    while True:
        clear()
        payment = False
        user_choice = main_menu()
        if user_choice in operations:
            hidden_op(user_choice)
            if user_choice == "maintain":
                sales = 0
        if user_choice in MENU:
            if check_resources(user_choice) is True:
                drink_cost = MENU[user_choice]["cost"]
                payment = handle_payment(drink_cost)
                if payment is True:
                    if sales == 0:
                        sales += 1
                        resources["money"] = drink_cost
                    else:
                        sales += 1
                        resources["money"] += drink_cost
                    subtract_resources(user_choice)
                    print(f"Enjoy your {user_choice}. Enjoy!")
                    print(resources)
                    sleep(3)
            else:
                low = low_resources(user_choice)
                print(f"Sorry, not enough {low, }")
                sleep(3)


main()
