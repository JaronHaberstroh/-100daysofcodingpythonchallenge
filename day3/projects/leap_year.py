# Get user input to determine year to check

year = int(input("Which year do you want to check?: "))

# Determine if year is a leap year
# A year that is / by 4 but not / by 100 unless it is / 400
# print() a message to console to let user know if their year is leap

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")