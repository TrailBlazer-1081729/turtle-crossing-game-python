STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)

        self.goto(STARTING_POSITION)

        self.showturtle()
    def starting(self):
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)
    def down(self):
        self.backward(MOVE_DISTANCE)
    def finished(self):
        return self.ycor()>280


