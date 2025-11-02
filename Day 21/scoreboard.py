from turtle import Turtle
import random
ALIGN = "center"
FONT = ("Arial",24,"normal")
class Scoreboard(Turtle):
 
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)  # yuqori chap burchak
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER",move=False,align=ALIGN,font=FONT)

    
    
  
    