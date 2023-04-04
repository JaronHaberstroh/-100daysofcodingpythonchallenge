from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    '''
    defines all snake object features
    '''

    def __init__(self):
        '''
        initalize snake object
        '''
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        '''
        assemble 3 blocks to create snake body
        '''
        for pos in START_POS:
            segment = Turtle("square")
            segment.penup()
            segment.goto(pos)
            segment.color("white")
            self.segments.append(segment)

    def move(self):
        '''
        controls movement for snake
        '''
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(x=new_x, y=new_y)
        self.head.forward(MOVEMENT_DISTANCE)

    def up(self):
        '''
        Change snake heading to up
        '''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        '''
        Change snake heading to down
        '''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        '''
        Change snake heading to left
        '''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        '''
        Change snake heading to right
        '''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
