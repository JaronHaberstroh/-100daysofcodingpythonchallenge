from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")
SCOREBOARD_LOCATION = (0, 270)
GAME_OVER_LOCATION = (0, 0)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(SCOREBOARD_LOCATION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(GAME_OVER_LOCATION)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
