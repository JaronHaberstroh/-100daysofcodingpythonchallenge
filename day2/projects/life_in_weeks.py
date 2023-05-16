# Ask user for age

age = input("What is your current age?: ")

# Create variables to store the remaining number of months, weeks, days,

years = 90 - int(age)

months = years * 12

weeks = years * 52

days = years * 365

# print() remaining number of days, weeks, and months to live to 90

print(f"You have {days} days, {weeks} weeks, and {months} months left.")