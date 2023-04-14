'''
working with files sandbox
'''

# Read file absolute file path
with open("/home/jhspaz988/Documents/python/#100daysofcodingpythonchallenge/day24/working_with_files/my_file.txt") as file:
    contents = file.read()
    print(contents)

# Write to file
# with open("my_file.txt", mode="w") as file:
#     file.write("new text.")


# Append file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nI <3 Python")

# Create file
# with open("new_file.txt", mode="w") as file:
#     file.write("This is a new file created by Python")
