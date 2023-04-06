# # Working with loops allows you to repeat a task numberous times

# # Identify lists in plural

# fruits = ["apple", "peach", "pear"]

# # Give a singular identifier for your loop

# for fruit in fruits:
#     print(fruit)

# # for loops with range

# for num in range(1, 10): #print() all num in range 1-10
#     print(num)

# for num in range(0, 13, 3): #print() all num in range 0-12 in every 3rd position 
#     print(num)

total = 0

for num in range(1, 101):
    total += num

print(total)