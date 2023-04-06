import turtle as t
import random

t.colormode(255)

dot_count = 0


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


def move():
    tim.forward(140)


def r_turn(p):
    if p[1] > 600:
        return
    tim.dot(random_color())
    tim.right(90)
    tim.forward(140)
    tim.right(90)
    tim.dot(random_color())
    tim.forward(140)


def l_turn(p):
    if p[1] > 600:
        return
    tim.dot(random_color())
    tim.left(90)
    tim.forward(140)
    tim.left(90)
    tim.dot(random_color())
    tim.forward(140)


tim = t.Turtle()
tim.shape("turtle")
tim.turtlesize(5)
tim.speed(0)
tim.pensize(20)
tim.penup()
tim.goto(x=-600, y=-600)

tim.dot(random_color())
tim.forward(140)
dot_count += 1

while dot_count < 100:
    pos = tim.position()
    if pos[0] <= -600:
        r_turn(pos)
        dot_count += 2
    elif pos[0] >= 600:
        l_turn(pos)
        dot_count += 2
    else:
        tim.dot(random_color())
        dot_count += 1
        tim.forward(140)


screen = t.Screen()
screen.exitonclick()
