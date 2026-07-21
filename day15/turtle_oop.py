'''from turtle import Turtle,Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclic
'''
# Importing external library using <pip install prettytable> and importing it into my file
from prettytable import PrettyTable
#constructiong a object using class PrettyTable
table = PrettyTable()
#Tap into object and acessing methods 
table.add_column("Pokemon Game",["Pikachu","Squirtle","Charmander"])
table.add_column("type",["Electric","water","fire"])
#Tap into object and acessing attributes
table.align = "l"
#printing object
print(table)