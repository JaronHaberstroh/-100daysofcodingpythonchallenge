from turtle import Turtle


PADDLE_LENGTH = 1
PADDLE_WIDTH = 5
PADDLE_MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, location=(0, 0)):
        super().__init__()
        self.penup()
        self.goto(location)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=PADDLE_LENGTH, stretch_wid=PADDLE_WIDTH)

    def move_up(self):
        new_y = self.ycor() + PADDLE_MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - PADDLE_MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
