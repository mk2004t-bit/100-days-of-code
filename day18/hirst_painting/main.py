"""
import colorgram

"""
"""

colors = colorgram.extract("image.jpg",30)

"""
"""

my_colors = []

"""

"""
# I commented it because i dont want to extract the colors from the pic everytime i run the code.

for  color in colors:
  r = color.rgb.r
  g = color.rgb.g
  b = color.rgb.b
  new_color = (r,g,b)
  my_colors.append(new_color)
  
"""
from turtle import Turtle,Screen
import random

extracted_colors = [(227, 224, 219), (157, 146, 133), (239, 230, 235), (227, 237, 231), (230, 233, 241), (149, 86, 50), (52, 28, 15), (24, 32, 51), (42, 101, 155), (128, 170, 192), (224, 208, 113), (186, 155, 36), (132, 183, 160), (193, 151, 167), (144, 66, 91), (162, 20, 6), (173, 11, 27), (66, 106, 90), (26, 43, 32), (45, 24, 29), (201, 80, 113), (60, 177, 112), (44, 52, 107), (216, 176, 187), (214, 87, 59), (157, 214, 197), (225, 175, 169), (24, 97, 37), (76, 73, 28), (34, 167, 190)]

tmk = Turtle()
screen = Screen()
#Set colormode to use rgb colors instead named colors
screen.colormode(255)
#Setting the position
tmk.penup()
tmk.hideturtle()
tmk.speed("fastest")
tmk.setheading(225)
tmk.forward(400)
tmk.setheading(0)
#10*10 pattern
#dot size 20 and gap 50


for dot_count in range(1,101):
  tmk.dot(20,random.choice(extracted_colors))
  tmk.forward(50)
  if dot_count % 10 == 0:
    tmk.setheading(90)
    tmk.forward(50)
    tmk.setheading(180)
    tmk.forward(500)
    tmk.setheading(0)



  




screen.exitonclick()