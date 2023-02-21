# Data Types

# Strings
# Strings are an array of char 
# Strings start with position 0

print("Hello, World"[4]) # prints "o" which is the 5th char in the 4th position

print("123" + "456") # prints 123456 as a string because "" tells the computer to recognize the value as a string

# Integer

print(123 + 456) # prints 579 because it recognizes the # as int when not held within ""

# Float

print(3.14159) # prints pi a float value given it contains a decimal

# Boolean values are either true or false

True
False

# type() function will tell you which type your variable is

print(type(input("What is your name?: "))) # takes the user input and shows it is class string


# Type Conversions

fav_num = input("What is your fav number?") # input() stores as string type

print(type(fav_num)) # print() type

fav_num = int(fav_num) # convert type to int

print(type(fav_num)) # print() type

dob = int(input("What is your date of birth?: "))
year = int(input("What is the current year?"))
print("You are " + str(year - dob) + " years old")