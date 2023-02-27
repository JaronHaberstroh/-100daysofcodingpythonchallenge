# BMI = weight(kg) / height**2(m**2)

# Get input from user for height and weight

height = input("enter your height in meters: ")

weight = input("enter you height in kilograms: ")

# Type conversion to int your variables

weight = float(weight)

height = float(height)

# print BMI to console using round function to get a whole number

print(round(weight / height ** 2))
