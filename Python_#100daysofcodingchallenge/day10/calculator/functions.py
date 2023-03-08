from operations import operators, add, subtract, multiply, divide
from art import logo


# calculator() function
def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for operator in operators:
        print(operator)

    run = True

    while run:
        operation = input("Pick an operation: ")

        num2 = float(input("What's the number?: "))

        answer = operators[operation](num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        finish = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()

        if finish == "n":
            run = False
            calculator()
        elif finish == "y":
            num1 = answer
        else:
            print(f"Please type 'y' to continue with {answer}, or 'n' to start a fresh calculation. Press ctl+c to exit.")