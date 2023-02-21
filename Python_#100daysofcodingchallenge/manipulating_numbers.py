# Use the round() function to round to whole numbers

print(8 / 3) # gives you a decimal values as a result

print(round(8 / 3)) # will round to the nearest whole number

print(round(8 / 3, 2)) # will round to 2 decimal places

# Floor division resulting in a whole number 

print(type(8 / 3)) # results in a float value

print(type(8 // 3)) # results in an int value and removes the decimal places

print(type(4 / 2)) # even clean division results in float

print(type(4 // 2)) # convert to int with floor division

# Variable math

result = 4 / 2

result /= 2 # Divide by 2 again

print(result) # Result is 1

# f strings

score = 0

possession = True

down = "first"

print(f"your score is {score} it's the {down} down and possession is {possession}")