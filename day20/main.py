from turtle import  Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
#it's turns the screen off until we update it.Doesn't shows what happens on the screen.
screen.tracer(0)
# blocks = []
# colors = ["violet","indigo","blue"]
snake = Snake()
screen.listen()
#KEY BINDINGING
screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")

"""

x_position = [0,-20,-40]
for bock_index in range(0,3):
  s = Turtle()
  s.shape("square")
  s.penup()
  s.color(colors[bock_index])
  s.goto(x=x_position[bock_index],y=0)
  blocks.append(s)

  """


"""

while game_is_on:
  #To show the snake after formatted by all segments.
  screen.update()
  #To control the speed of the snake.
  time.sleep(0.1)
  for segment in segments:
    segment.forward(10)
    
"""
#There is better way to move the snake and that is we move the last segment to the position of its previous segment and that segment moves to its previous and last move the first segment to 20 paces.
game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

screen.exitonclick()