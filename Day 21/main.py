from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen =  Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect the collision
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect the collision with wall

    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or  snake.head.ycor() <-280:
        game_is_on = False
        scoreboard.game_over()

    #Detect the collision with tail
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()

    

class CarManager():
    def __init__(self):
        self.all_cars =[]


    def create_cars(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=2,stretch_len=1)
        new_car.penup()
        new_car.color(R_COLORS)
        random_y = random.randint(250,250)
        new_car.goto(300,random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
R_COLORS = random.choice(COLORS)
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars =[]


    def create_cars(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=2,stretch_len=1)
        new_car.penup()
        new_car.color(R_COLORS)
        random_y = random.randint(250,250)
        new_car.goto(300,random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()


screen.listen()
screen.onkey(player.move,"Up")




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    scoreboard.update_scoreboard()

    if player.ycor() > 280:
        scoreboard.increase_score()
        player.restart()
        car_manager.level_up()








screen.exitonclick()
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars =[]
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance ==1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
    def level_up(self):
        self.car_speed +=MOVE_INCREMENT

    
        


screen.exitonclick()
