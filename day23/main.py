import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
screen.onkey(player.Up,"Up")
screen.onkey(player.Left,"Left")
screen.onkey(player.Right,"Right")
cars = []
for _ in range(20):
    new_car = CarManager()
    cars.append(new_car)
#level 
score = ScoreBoard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.CarMove()
    if player.ycor() > 280:
        player.finish()
        score.clear()
        score.update_level()
        

screen.exitonclick()