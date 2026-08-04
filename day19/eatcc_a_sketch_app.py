from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()
screen.listen()
def move_forward():
  tim.forward(50)

def move_backword():
  tim.back(50)

def move_left():
  new_heading = tim.heading()+10
  tim.setheading(new_heading)

def move_right():
  new_heading = tim.heading()-10
  tim.setheading(new_heading)
def clear():
  tim.clear()
  tim.penup()
  tim.home()
  tim.pendown()

screen.onkey(key="a",fun=move_forward)
screen.onkey(key="j",fun=move_left)
screen.onkey(key="k",fun=move_right)
screen.onkey(key="s",fun=move_backword)
screen.onkey(key="c",fun=clear)

screen.exitonclick()