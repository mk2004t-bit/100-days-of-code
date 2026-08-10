from turtle import Turtle
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(x=-240,y=270)
        self.write(arg=f"level = {self.level}",align="center",font=FONT)

    def update_level(self):
        self.level+=1
        self.write(arg=f"level = {self.level}",align="center",font=FONT)