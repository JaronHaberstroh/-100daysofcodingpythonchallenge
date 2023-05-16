
# NUMBERS COMPREHENSION

# num_list = [1, 2, 3]

# new_num_list = [n+1 for n in num_list]

# print(new_num_list)


# new_num_list = [n*2 for n in range(1, 5)]

# print(new_num_list)


# LETTERS COMPREHENSION

# name = "Angela"

# let_list = [let for let in name]

# print(let_list)


# TESTING IN COMPREHENSION

names = ["Beth", "Alex", "Jaron", "Charles", "Jordan", "Dave", "Eleanor"]

short_names = [name for name in names if len(name) < 5]

caps_long_names = [name.upper() for name in names if len(name) >= 5]

print(caps_long_names)
