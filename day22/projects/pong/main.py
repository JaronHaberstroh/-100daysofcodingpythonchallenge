from turtle import Screen
from time import sleep
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball

GAME_IS_ON = True
PADDLE_FROM_CENTER = 350
PADDLE_COLLISION = 20
RIGHT_PADDLE_LOCATION = (PADDLE_FROM_CENTER, 0)
LEFT_PADDLE_LOCATION = (-PADDLE_FROM_CENTER, 0)
Y_BOUNDRY = 280
X_BOUNDRY = 400


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

scoreboard = ScoreBoard()
r_paddle = Paddle(location=RIGHT_PADDLE_LOCATION)
l_paddle = Paddle(location=LEFT_PADDLE_LOCATION)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

while GAME_IS_ON:
    screen.update()
    ball.move()
    sleep(.1)

    if ball.ycor() > Y_BOUNDRY or ball.ycor() < -Y_BOUNDRY:
        ball.wall_collision()

    if ((ball.distance(r_paddle) < 50 and
            ball.xcor() > PADDLE_FROM_CENTER - PADDLE_COLLISION) or
            (ball.distance(l_paddle) < 50 and
             ball.xcor() < -PADDLE_FROM_CENTER + PADDLE_COLLISION)):
        ball.increase_speed(x_position=ball.xcor(), y_position=ball.ycor())
        ball.paddle_collision()

    if (ball.xcor() > X_BOUNDRY or ball.xcor() < -X_BOUNDRY):
        scoreboard.increase_score(player=ball.xcor())
        ball.reset_position()


screen.exitonclick()
