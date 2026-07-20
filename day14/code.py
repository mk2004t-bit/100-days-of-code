#print who has more followers Type A or B
User_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
win = False
lose = False

#logic of the programming
def decider(choice):
    global win
    global lose
    if player_A["followers"] > player_B["followers"]:
        win = True
    else:
        lose = True
    if choice == "a":
        return win
    else:
        return lose
score = 0   
correct = True
while correct:
    score+=1
    if win == True:
        player_A = player_A
    else:
        player_A = player_B
    player_B = random.choice(players)
    print(f"compare A : {player_A["name"]}, {player_A["description"]}, from {player_A["country"]}")
    print(vs)
    print(f"compare B : {player_B["name"]}, {player_B["description"]}, from {player_B["country"]}")

    User_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if decider(User_choice) == False:
        correct = False
        print("You'have lost the game")
        print(f"your score is {score}") 