from turtle import Turtle

BALL_X_VEL = 10
BALL_Y_VEL = 10
X_SPEED_INCREASE = 5
Y_SPEED_INCREASE = 1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = BALL_X_VEL
        self.y_move = BALL_Y_VEL

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_collision(self):
        self.y_move *= -1

    def paddle_collision(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        if self.x_move > 0:
            self.x_move = BALL_X_VEL
        else:
            self.x_move = BALL_X_VEL * -1
        if self.y_move > 0:
            self.y_move = BALL_Y_VEL
        else:
            self.y_move = BALL_Y_VEL * -1
        self.x_move *= -1

    def increase_speed(self, x_position, y_position):
        if x_position > 0:
            self.x_move += X_SPEED_INCREASE
        else:
            self.x_move -= X_SPEED_INCREASE

        if y_position > 0:
            self.y_move += Y_SPEED_INCREASE
        else:
            self.y_move -= Y_SPEED_INCREASE
