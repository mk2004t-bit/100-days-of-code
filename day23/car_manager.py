from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_Y_POSITIONS = [-280,-200,-120,-40,40,120,200,280]



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.starting_y = random.choice(STARTING_Y_POSITIONS)
        self.goto(x=270,y=self.starting_y)

    def CarMove(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(x=new_x,y=self.ycor())

    def increase_speed(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(x=new_x,y=self.ycor())
        
        



    
