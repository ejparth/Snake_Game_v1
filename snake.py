# import time
from turtle import Screen, Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] #it's used again and again


    def create_snake(self):
        for position in START_POS:
            tim = Turtle("square")
            tim.penup()
            tim.goto(position)
            self.segments.append(tim)  # Update the object with positions in the list

    def move(self):

        # range(start,stop,step)
        # imagine how the caterpillar moves from tail to head
        # take the always changing snake length in the range and move from
        # tail to head
        # update the x and y coordinates for the last to head segments
        # finally move the head element`

        for snake_body_parts in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_body_parts - 1].xcor()
            new_y = self.segments[snake_body_parts - 1].ycor()
            self.segments[snake_body_parts].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)
            self.move()

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
            self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
            self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
            self.move()