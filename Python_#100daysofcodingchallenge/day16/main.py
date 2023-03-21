from time import sleep
from os import system
from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


def clear():
    system("clear")


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    clear()
    choice = input(f"What would you like? {menu.get_items()}: ").lower()
    if choice == "off":
        quit()
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
        sleep(3)
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            sleep(3)
