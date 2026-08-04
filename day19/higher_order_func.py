from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def draw():
  tim.forward(10)

screen.listen()
#Higher order function. Means on function can work with an other function.
screen.onkey(fun=draw,key="space")
screen.exitonclick()