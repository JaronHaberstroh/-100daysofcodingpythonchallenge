# return in functions

# create function that returns value
def my_function():
    result = 3 * 2
    return result

# store output value in variable for later use
output = my_function

# create early return function to exit program early if conditionals aren't met
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "No valid inputs"
    name = f_name.title() + " "
    name += l_name.title()
    return name

print(format_name(input("What is your first name?: "), input("What is your last name?: ")))