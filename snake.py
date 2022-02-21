# import time
from turtle import Screen, Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def _self_(self=None):
        self.segments = []
        self.create_snake()

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
