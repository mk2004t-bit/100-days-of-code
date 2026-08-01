from turtle import Turtle,Screen
import random
tim = Turtle()
#To generate random colors
colors = ["black","royal blue","magenta","red","purple","bisque","dark slate blue","dark olive green"]
#To generate random directions
directions = [0,90,180,270,360]
#To set thickness/width of the pen
tim.pensize(15)
#To set speed of the turtle
tim.speed("fastest")
#To random rom around
for _ in range(50):
  tim.color(random.choice(colors))
  tim.forward(30)
  #To direction of motion of the turtle.
  tim.setheading(random.choice(directions))





screen = Screen()
screen.exitonclick()