from turtle import Turtle, Screen


def move():
    cursor.forward(10)


def rot_right():
    angle = cursor.heading() - 10
    cursor.seth(angle)


def rot_left():
    angle = cursor.heading() + 10
    cursor.seth(angle)


def reset():
    cursor.home()
    cursor.clear()


cursor = Turtle()
screen = Screen()


screen.listen()
screen.onkey(key="c", fun=reset)
screen.onkey(key="a", fun=rot_left)
screen.onkey(key="d", fun=rot_right)
screen.onkey(key="w", fun=move)

screen.exitonclick()
