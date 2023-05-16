'''
takes in letter and list of names
replaces placeholder [name] with given name
then outputs finished letter
'''
PLACEHOLDER = "[name]"

NAME_PATH = ("Input/Names/invited_names.txt")
LET_PATH = ("Input/Letters/starting_letter.txt")
OUT_PATH = ("Output/ReadyToSend/")

with open(NAME_PATH) as names:
    list_names = names.readlines()

with open(LET_PATH) as file:
    contents = file.read()

for name in list_names:
    new_contents = contents.replace(PLACEHOLDER, name.strip("\n"))
    filename = name.strip("\n") + ".txt"
    with open(OUT_PATH + filename, "w") as output:
        output.write(new_contents)
