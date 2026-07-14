import random
from art import logo

def start_game():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  player_cards = []
  computer_cards =[]
  player_continue = True
  def select_cards(cards):
    '''It takes list cards, select 2 randomly out of them and return selected cards.'''
    selected_cards = []
    for _ in range(2):
      card = random.choice(cards)
      selected_cards.append(card)
    return selected_cards
  print(logo)
#player initial cards
  player_cards = select_cards(cards)
  player_score = sum(player_cards)
  print(f"Your cards {player_cards}, Current score: {player_score}")

  # computer initial cards
  computer_cards = select_cards(cards)
  computer_score = sum(computer_cards)
  first_card = random.choice(computer_cards)
  print(f"Computer's first card: {first_card} ")

  while player_continue:
    get_another_card = input("Type 'y' to get another card or 'n' : ").lower()
    if get_another_card == 'y':
      card = random.choice(cards)
      player_cards.append(card)
      player_score = sum(player_cards)
      print(f"Your cards {player_cards}, Current score: {player_score}")
      print(f"Computer's first card: {first_card} ")
      if player_score > 21:
        print(f"Your final hand: {player_cards}, final score: {player_score} ")
        print(f"computer's final hand: {computer_cards}, final score: {computer_score} ")
        print("you lose")
        player_continue = False

    elif get_another_card == "n":
      print(f"Your final hand {player_cards}, final score: {player_score}")
      while computer_score <17:
        card = random.choice(cards)
        computer_cards.append(card)
        computer_score = sum(computer_cards)
      print(f"computer's final hand: {computer_cards}, final score: {computer_score} ")
      player_continue = False
      if computer_score > 21:
        print("you win")
      elif computer_score == player_score:
        print("it' draw")
      elif computer_score > player_score:
        print("computer win")
      else:
        print("you win")

while input("Do you want to play backjack,'y' or 'no' ? : ").lower() == 'y':
  start_game()
