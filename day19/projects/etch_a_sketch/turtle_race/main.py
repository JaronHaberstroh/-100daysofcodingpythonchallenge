from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []
x_axis = -230
y_axis = -120
for index, color in enumerate(colors):
    name = "turtle" + str(index)
    name = Turtle(shape="turtle")
    name.color(color)
    name.penup()
    all_turtles.append(name)
    name.goto(x=x_axis, y=y_axis)
    y_axis += 50

race_on = True
while race_on:
    for turtle in all_turtles:
        turtle_pos = turtle.position()
        if turtle_pos[0] >= 230:
            race_on = False
            winning_turtle = turtle.pencolor()

        turtle.forward(random.randint(1, 10))


if winning_turtle == user_bet:
    print(f"You've won! The {winning_turtle} turtle is the winner")
else:
    print(f"You've lost. The {winning_turtle} turtle is the winner")

screen.exitonclick()
