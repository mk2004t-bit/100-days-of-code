from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
#Setting up screen
screen = Screen()
screen.setup(width=800,height=600)
screen.title("The Pong")
screen.bgcolor("black")
#Tracker doesnt the movement of r_paddle from center to its current postition.
screen.tracer(0)

#Creating a r_paddle object from Paddle class
r_paddle = Paddle((350,0))
#Adding eventlisteners to r_paddle
screen.listen()
screen.onkey(r_paddle.Up,"Up")
screen.onkey(r_paddle.Down,"Down")

#Creating a l_paddle object from Paddle class
l_paddle = Paddle((-350,0))
#Adding eventlisteners to l_paddle
screen.onkey(l_paddle.Up,"w")
screen.onkey(l_paddle.Down,"s")

#Creating a ball object using Ball class
ball = Ball()

#There has to some loop because we need to update the screen every certain second in way 0.02 seconds.
game_is_on = True
while game_is_on:
  time.sleep(0.1) #loop wait for 20 milliseconds
  screen.update() #To untrace the screen. Back to visible.
  ball.move()
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce()






screen.exitonclick()