from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=1
        self.hideturtle()
        self.penup()
        self.goto(-200,250)
        self.update()
    def update(self):
        self.clear()
        self.write(f"level: {self.score}", align="left", font=FONT)
    def inc_level(self):
        self.score+=1
        self.update()
    def finished(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=FONT)