COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle
class CarManager():
    def __init__(self):
        self.all=[]
        self.speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        choice=random.randint(1,6)
        if choice==1:
            new_c=Turtle("square")
            new_c.hideturtle()
            new_c.penup()
            new_c.turtlesize(1,2)
            new_c.color(random.choice(COLORS))
            y_c=random.randint(-260,260)
            new_c.goto(300,y_c)
            new_c.showturtle()
            self.all.append(new_c)

    def move(self):
        for car in self.all:
            car.backward(self.speed)
    def move_speed(self):
        self.speed*=1.4