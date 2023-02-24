# User input() a list of heights

student_heights = input("Input a list of student heights. ").split()

# Convert each string in list student_heights to an int

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Create variables to store info

total = 0
num = 0

# Get the average of all heights

for height in student_heights:
    total += height
    num += 1

average = round(total / num)

print(average)