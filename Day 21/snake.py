from turtle import Turtle,Screen
import time
screen = Screen()

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.new_t = Turtle()
            self.new_t.shape("square")
            self.new_t.color("white")
            self.new_t.penup()
            self.new_t.goto(position)
            self.segments.append(self.new_t)
            self.head = self.segments[0]
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
