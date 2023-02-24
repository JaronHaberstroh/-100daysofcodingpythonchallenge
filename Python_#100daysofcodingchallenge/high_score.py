# Write code that determines the highest value amongst input() values

# Ask for user input()

student_scores = input("Input a list of student scores.").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)

# Use a for loop to compare all values and find the highest

# Create variable

n = 0
i = 0

for score in student_scores:
    i += 1
    if student_scores[n] < score:
        n = i - 1
    else:
        continue

# print() highest value "The highest score in the class is: {x}"

print(f"The highest score in the class is: {student_scores[n]}")