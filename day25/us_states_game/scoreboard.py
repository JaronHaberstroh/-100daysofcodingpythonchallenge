from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.score = 0

    def increase_score(self):
        self.score += 1
