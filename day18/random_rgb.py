from turtle import Turtle,Screen
import random
screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.pensize(15)
tim.speed("fastest")
directions = [0,90,180,270,360]

def random_color():
  r  = random.randint(0,255)
  g  = random.randint(0,255)
  b  = random.randint(0,255)
  random_color =  (r,g,b)
  return random_color




for _ in range(200):
  tim.color(random_color())
  tim.forward(30)
  #To direction of motion of the turtle.
  tim.setheading(random.choice(directions))

screen.exitonclick()