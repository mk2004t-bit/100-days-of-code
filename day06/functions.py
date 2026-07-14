# karel the robot (hurdle 1)
def turn_left():
    print("turn left")

def move():
    print("move")


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def at_goal():
    print("goal reached")

while not at_goal():
    move()
    turn_left()
    move()   
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# hurdle -3
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
def wall_in_front():
    print("there is a wall in the front")   
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
