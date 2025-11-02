from turtle import Screen,Turtle
import random

screen = Screen()

screen =  Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)


l_paddle = Turtle()
l_paddle.shape("square")
l_paddle.color("White")
l_paddle.shapesize(stretch_len=1,stretch_wid=5)
l_paddle.penup()
l_paddle.goto(350,0)
screen.tracer(1)



r_paddle = Turtle()
repr_paddle.shape("square")
r_paddle.color("White")
r_paddle.shapesize(stretch_len=1,stretch_wid=5)
r_paddle.penup()
r_paddle.goto(-350,0)
screen.tracer(1)

def go_up():
    new_y = l_paddle.ycor() + 20
    l_paddle.goto(l_paddle.xcor(),new_y)

def go_down():
    new_y = l_paddle.ycor() - 20
    l_paddle.goto(l_paddle.xcor(),new_y)
#R
def go_up():
    new_y = l_paddle.ycor() + 20
    l_paddle.goto(l_paddle.xcor(),new_y)

def go_down():
    new_y = l_paddle.ycor() - 20
    l_paddle.goto(l_paddle.xcor(),new_y)


screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")










screen.exitonclick()