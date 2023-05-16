from turtle import Turtle
import random

COLORS = ("yellow", "red", "blue", "maroon", "purple", "orange")
CAR_LENGTH = 4
CAR_WIDTH = 2
CAR_SPAWN_X = 320
CAR_SPAWN_Y = 250
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270
START_MOVE_DIST = 5
CHANCE = 6


class Car_Manager():
    def __init__(self) -> None:
        super().__init__()
        self.all_cars = []
        self.move_distance = START_MOVE_DIST

    def create_car(self):
        if random.randint(1, CHANCE) == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.seth(WEST)
            new_car.shape("square")
            new_car.shapesize(stretch_len=CAR_LENGTH, stretch_wid=CAR_WIDTH)
            new_car.color(random.choice(COLORS))
            new_car.goto(
                CAR_SPAWN_X, random.randrange(-CAR_SPAWN_Y, CAR_SPAWN_Y, 20))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += START_MOVE_DIST
