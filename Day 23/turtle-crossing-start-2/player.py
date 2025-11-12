STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 28
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.right(270)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
    def restart(self):
        self.goto(STARTING_POSITION)



