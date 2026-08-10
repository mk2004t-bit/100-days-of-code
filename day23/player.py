from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def Up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(),y=new_y) 

    def Left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(x=new_x,y=self.ycor())

    def Right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(x=new_x,y=self.ycor())

    def finish(self):
        self.goto(STARTING_POSITION)
        
