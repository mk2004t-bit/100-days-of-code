from art import logo
import random
print(logo)
print("Welcome to number guess game: ")
print("I am guessing number between 1 and 100")
random_number = random.randint(1,100)

mode = input("choose difficulty, Type 'easy' or 'hard' : ").lower()

def play_game(attempts):
    print(f"You have {attempts} attempts remaining to guess the number.")
    while attempts > 0:
        number = int(input("Make a guess: "))
        if random_number == number:
            return "you have guessed the number. you won !"
        elif number > random_number:
            print("Too High")
            attempts-=1
            print(f"you have only {attempts} attempts to guess the number")
        elif number < random_number:
            print("Too Low")
            attempts-=1
            print(f"you have only {attempts} attempts to guess the number")
    
    return f"You lost guessing the number {random_number}."
    

if mode == "easy":

    print(play_game(10))

elif mode == "hard":
    print(play_game(5))
   
   

     



           
