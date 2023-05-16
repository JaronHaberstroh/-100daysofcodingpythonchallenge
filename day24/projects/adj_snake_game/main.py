import time
import turtle as t
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

BOUNDRY = 290
FOOD_COLLISION = 15
SNAKE_COLLISION_SELF = 10
GAME_IS_ON = True

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while GAME_IS_ON:
    screen.update()
    snake.move()
    time.sleep(.2)

    if snake.head.distance(food) < FOOD_COLLISION:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if (snake.head.xcor() > BOUNDRY or snake.head.xcor() < -BOUNDRY
            or snake.head.ycor() > BOUNDRY or snake.head.ycor() < -BOUNDRY):
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < SNAKE_COLLISION_SELF:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
