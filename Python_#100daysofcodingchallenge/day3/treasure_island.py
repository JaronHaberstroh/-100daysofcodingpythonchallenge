# Create a basic game of choice

print("Welcome to Treasure Island!\n Your mission is to make it to the end and find the treasure.")

# User chooses left or right

direction = input("You approach a fork in the road and must choose to go left or right.: ").lower()

if direction == "left":
    print("You've fallen into a pit which brings about the end of your journey. \n Game Over!")
else:   
    # User chooses swim or wait
    print("You continue down the path and through some foliage.")
    stream = input("You come across a stream. Do you choose to swim across or wait?").lower()
    if stream == "swim":
        print("Your strong and impatient. You begin swiming across the river current, but it's more than you expected. Eventutally you grow tired and the river swallows another victim.\n Game Over!")
    else:
        print("You know not if any help will come but the river current is to strong to swim.\n You wait and a boatman comes to farry you across.")
        # user choose between 3 doors
        print("Once across you continue your journey until you come across 3 doors. Standing on their own and presumably leading to nothing.")
        door = input("Which door will you choose to open first? Yellow/Red/blue: ").lower()
        if door == "blue" or door == "red":
            print("You reach for your choosen door and turn the knob. You no sooner have it open and an unknown force pulls you in. You stare off into nothing until everything around you fades to black.\nGame Over!")
        else:
            print("You open your choosen door and turn the knob. Once open you recognize that it truely does lead to nowhere. Although now where once was nothing sits the treasure chect you've been searching for.\nCongrats, You've Won!")