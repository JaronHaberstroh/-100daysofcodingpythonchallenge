from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")
SCOREBOARD_LOCATION = (0, 270)
GAME_OVER_LOCATION = (0, 0)


class ScoreBoard(Turtle):
    '''
    controls scoreboard behavior
    '''

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(SCOREBOARD_LOCATION)
        self.update_scoreboard()

    def update_scoreboard(self):
        '''
        updates scoreboard
        '''
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     '''
    #     creates game over text at end game
    #     '''
    #     self.goto(GAME_OVER_LOCATION)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        '''
        increase score and rewrites new score on screen
        '''
        self.score += 1
        self.update_scoreboard()
