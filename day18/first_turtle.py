from turtle import Turtle,Screen
import random
tim = Turtle()
colors = ["black","royal blue","magenta","red","purple","bisque","dark slate blue","dark olive green"]
def draw_shape(no_sides):
  angle = 360/no_sides
  for _ in range(no_sides):
    tim.forward(100)
    tim.right(angle)

for shape_side_no in range(3,11):
  tim.color(random.choice(colors))
  draw_shape(shape_side_no)

screen = Screen()
screen.exitonclick()