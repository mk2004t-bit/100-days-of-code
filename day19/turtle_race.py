from turtle import Turtle,Screen
import random
is_game_on = False
colors = ["violet","indigo","blue","green","yellow","orange","red"]
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="bet",prompt="bet on the turtle by entering there color.")

if user_bet:
  is_game_on = True

screen.listen()
y_position = [-90,-60,-30,0,30,60,90]
all_turtles=[]
#creating seven turtles and set them in their positions.
for turtle_index in range(0,7):
  new_turtle = Turtle(shape="turtle")
  new_turtle.color(colors[turtle_index])
  new_turtle.penup()
  new_turtle.goto(x=-240,y=y_position[turtle_index])
  all_turtles.append(new_turtle)

while is_game_on:
  for current_turtle in all_turtles:
    if current_turtle.xcor() > 230:
      is_game_on = False
      if current_turtle.pencolor() == user_bet:
        print(f"you've won the bet.The {current_turtle.pencolor()}_turtle is the winner")
      else:
        print(f"you've lost the bet.The {current_turtle.pencolor()}_turtle is the winner")
    moving_distance = random.randint(0,10)
    current_turtle.forward(moving_distance)


screen.exitonclick()