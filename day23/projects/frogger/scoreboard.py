from turtle import Turtle

SB_POSITION = (-250, 260)
GO_POSITION = (0, 0)
ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(SB_POSITION)
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(GO_POSITION)
        self.write("GAME OVER")
