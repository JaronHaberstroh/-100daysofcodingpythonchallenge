import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
tim.pensize(15)
tim.hideturtle()
tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


angle = 0
while angle <= 360:
    angle += 5
    tim.seth(angle)
    tim.color(random_color())
    tim.circle(500)

screen = t.Screen()
screen.exitonclick()
# DIRECTION = [90, 180, 270, 0]
# while True:
#     tim.color(random_color())
#     tim.right(random.choice(DIRECTION))
#     tim.forward(100)


# COLOR = ["yellow", "gold", "orange", "black", "maroon", "violet", "magenta", "purple", "navy", "blue",
#          "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray", "white"]


# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(20):
#     tim.forward(20)
#     tim.penup()
#     tim.forward(20)
#     tim.pendown()

# tim.color(choice(COLOR))

# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)

# tim.color(choice(COLOR))

# for _ in range(6):
#     tim.forward(100)
#     tim.right(60)

# tim.color(choice(COLOR))

# for _ in range(8):
#     tim.forward(100)
#     tim.right(45)

# tim.color(choice(COLOR))

# for _ in range(10):
#     tim.forward(100)
#     tim.right(36)


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)


# for shape_side in range(3, 11):
#     tim.color(choice(COLOR))
#     draw_shape(shape_side)
