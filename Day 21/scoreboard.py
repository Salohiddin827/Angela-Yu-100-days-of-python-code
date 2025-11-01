from turtle import Turtle
import random

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.write(f"Score {self.score}",move=False,align="left",font=("Arial",24,"normal"))
        self.update_score()

    

    def update_score(self):
        self.write(f"Score {self.score}",move=False,align="left",font=("Arial",24,"normal"))
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()
    
    
  
    