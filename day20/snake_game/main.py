import turtle as t
from snake import Snake
import time

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

sprite = Snake()

screen.listen()
screen.onkey(sprite.up, "Up")
screen.onkey(sprite.down, "Down")
screen.onkey(sprite.left, "Left")
screen.onkey(sprite.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    sprite.move()


screen.exitonclick()
