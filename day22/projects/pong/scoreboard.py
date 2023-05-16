from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
SCOREBOARD_LOCATION = (0, 260)
GAME_END_LOCATION = (0, 0)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_player = 0
        self.score_opponent = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(SCOREBOARD_LOCATION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score_player} : {self.score_opponent}",
                   font=FONT, align=ALIGNMENT)

    def increase_score(self, player=None):
        if player > 0:
            self.score_player += 1
            self.update_scoreboard()
        else:
            self.score_opponent += 1
            self.update_scoreboard()
