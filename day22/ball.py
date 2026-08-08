from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.x_add = 10
    self.y_add = 10
    self.move_speed = 0.1

  def move(self):
    new_x = self.xcor() + self.x_add
    new_y = self.ycor() + self.y_add
    self.goto(x=new_x,y=new_y)

  def bounce_y(self):
    self.y_add*= -1
    self.move_speed *= 0.9

  def bounce_x(self):
    self.x_add*= -1
    self.move_speed *=0.9

  def reset_position(self):
    self.move_speed = 0.1
    self.goto(x=0,y =0)
    self.bounce_x()
    

  

