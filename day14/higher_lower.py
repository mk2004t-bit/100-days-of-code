from art import logo,vs 
from data import players
import random
#print logo
print(logo)
score = 0
should_continue = True

def format_data(player):
    player_name = player["name"]
    player_desc = player["description"]
    player_country = player["country"]
    return f"{player_name}, a {player_desc}, from {player_country}"

def check_answer(user_guess,a_user_followers,b_user_followers):
    if a_user_followers > b_user_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
player_B = random.choice(players)
while should_continue:    
    player_A = player_B
    player_B = random.choice(players)
    while player_B == player_A:
        player_B = random.choice(players)

    print(f"Compare A : {format_data(player_A)}")
    print(vs)
    print(f"Against B : {format_data(player_B)}")

    a_player_followers = player_A["followers"]
    b_player_followers = player_B["followers"]

    guess = input("Who has more followers? say 'A' or 'B': ").lower()
    is_correct = check_answer(guess,a_player_followers,b_player_followers)
    if is_correct:
        score+=1
        print(f"you're correct! current score: {score} ")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False