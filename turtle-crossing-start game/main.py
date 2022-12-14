import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle crossing game")
screen.tracer(0)

player=Player()
car_manager=CarManager()
level=Scoreboard()


screen.listen()
screen.onkey(player.up_move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create()
    car_manager.move()
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on=False
            player.collide()

    if player.is_at_finish_line():
        player.go_to_start()
        level.increase()
        car_manager.level_up()
        level.update()

screen.exitonclick()

