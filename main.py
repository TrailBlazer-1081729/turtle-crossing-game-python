import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
scoreboard=Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
player=Player()
car=CarManager()
screen.tracer(0)
screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.down,"Down")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    for cars in car.all:
        if cars.distance(player)<20:
            scoreboard.finished()
            game_is_on = False

    if player.finished():
        player.starting()
        car.move_speed()
        scoreboard.inc_level()


screen.exitonclick()