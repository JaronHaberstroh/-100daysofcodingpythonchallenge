# Dictionaries are a key and value pair

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code you can easily call over and over again",
    "Loop": "The action of doing something over and over again",
}

# # Retrieve item from dictionary
# print(programming_dictionary["Function"])

# Adding new items to dictionary
programming_dictionary["Variable"] = "A chosen char or string that will store a value"

# Create empty dictionary
empty_dictionary = {}

# # Wipe a dictionary
# programming_dictionary = {}

# Edit a dictionary
programming_dictionary["Bug"] = "A moth in your computer?"

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])