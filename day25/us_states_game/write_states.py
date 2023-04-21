from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 8, "normal")


class Writter(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)

    def write_state(self, state, coordinates):
        self.goto(coordinates)
        self.write(arg=state, align=ALIGN, font=FONT)
