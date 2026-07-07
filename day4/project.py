import random

rock ='''
 ____   ___   ____ _  __
 |  _ \ / _ \ / ___| |/ /
 | |_) | | | | |   | ' /
 |  _ <| |_| | |___| .  
 |_| \_\ \___/ \____|_|\ 
 
'''
paper=''' 
 ____   _    ____  _____ ____
 |  _ \ / \  |  _ \| ____|  _ 
 | |_) / _ \ | |_) |  _| | |_) |
 |  __/ ___ \|  __/| |___|  _ <
 |_| /_/   \_\_|   |_____|_| \_
'''
scissor='''
  ____   ____ ___ ____ ____   ___  ____
 / ___| / ___|_ _/ ___/ ___| / _ \|  _ 
 \___ \| |    | |\___ \___ \| | | | |_) |
  ___) | |___ | | ___) |__) | |_| |  _ <
 |____/ \____|___|____/____/ \___/|_| \_
'''
gameover='''
           \ \  //
      _.--   \ \//   --._
     (  o  )------(  o  )
      `--'   //\ \   `--'
           //  \  

'''
items =[rock,paper,scissor]

player_choice = int(input("choose 0 for rock,1 for paper or 2 for scissor: "))
print("\n")
print("your choice: ")
print(items[player_choice])
computer_choice = random.randint(0,2)
print("Computer choice:")
print(items[computer_choice])
print("Game result:")
if player_choice == computer_choice:
  print("it's draw")
elif player_choice < computer_choice:
  print("you loose - game over")
  print(gameover)
else:
  print("you win")