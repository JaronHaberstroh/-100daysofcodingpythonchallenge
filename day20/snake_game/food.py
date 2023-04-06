from turtle import Turtle
from random import randint

FOOD_BOUNDRY = 270


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randint(a=-FOOD_BOUNDRY, b=FOOD_BOUNDRY)
        random_y = randint(a=-FOOD_BOUNDRY, b=FOOD_BOUNDRY)
        self.goto(random_x, random_y)
