from turtle import Turtle

NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180
MOVE_DISTANCE = 20
START_POSITION = (0, -280)
TURTLE_SIZE = 1.5
LIVES = 3


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.lives = LIVES
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.seth(NORTH)
        self.shapesize(TURTLE_SIZE)
        self.goto(START_POSITION)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_up(self):
        self.seth(NORTH)
        self.move_forward()

    def move_down(self):
        self.seth(SOUTH)
        self.move_forward()

    def move_left(self):
        self.seth(WEST)
        self.move_forward()

    def move_right(self):
        self.seth(EAST)
        self.move_forward()

    def bounce(self, border):
        if self.ycor() > border:
            self.sety(border)
        if self.ycor() < -border:
            self.sety(-border)
        if self.xcor() > border:
            self.setx(border)
        if self.xcor() < -border:
            self.setx(-border)

    def reset_position(self):
        self.goto(START_POSITION)
