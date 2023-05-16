import time
from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from car_manager import Car_Manager

DIFFICULTY = 5
BORDER = 280
FINISH_LINE = 270

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
scoreboard = ScoreBoard()
car_manager = Car_Manager()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    car_manager.create_car()
    car_manager.move_cars()

    if (player.ycor() > BORDER or player.ycor() < -BORDER or
            player.xcor() > BORDER or player.xcor() < -BORDER):
        player.bounce(border=BORDER)

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            if player.lives == 0:
                game_is_on = False
                scoreboard.game_over()
            else:
                player.lives -= 1
                player.reset_position()
    if player.ycor() > FINISH_LINE:
        scoreboard.increase_score()
        player.reset_position()
        car_manager.increase_speed()


screen.exitonclick()
