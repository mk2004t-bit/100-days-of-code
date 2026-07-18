import random
#GLOBAL VARIABLES CONSTANTS
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
#function to check answer
def check_answer(user_guess, actual_guess):
    if user_guess > actual_guess:
        print("Too High")
    elif user_guess < actual_guess:
        print("Too low")
    else:
        print(f"You got it, the answer was {actual_guess}")
#function to set difficulty
def set_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard' : ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
turns = set_difficulty()

def game(): 
    #starting text
    print("Welcome to number guessing game.")
    print("I am thinking of number between 1 and 100")
    answer = random.randint(1,100)
    print(answer)


    

