import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Salohiddin's Turtle Game")
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

    for car in car_manager.all_cars:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        scoreboard.increase_score()
        player.restart()
        car_manager.level_up()








screen.exitonclick()
