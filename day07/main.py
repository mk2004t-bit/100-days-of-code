from objects import words, hangman, hangman_title
import random
# Getting random word from words list

lives =0
random_word = random.choice(words)
#Giving the hint to user about length of the word
placeholder = ""
for letter in range(len(random_word)):
  placeholder+="_"

#tracking the guessed letters
correct_letters =[]
game_over = False
print(hangman_title)
print("HINT : It's an object")
print(placeholder)
while not game_over:
    print(f"*********************** you life {lives+1}/6*************************")
    display=""
    chosen_letter = input("guess a letter: ").lower()
    if chosen_letter in correct_letters:
       print(f"you've already guessed \" {chosen_letter} \" ")
    for letter in random_word:
      if letter == chosen_letter:
        display+=letter
        correct_letters.append(letter)
      elif letter in correct_letters:
         display+=letter
      
      else:
         display+="_"

    if chosen_letter not in random_word:
         lives+=1
         if lives == 6:

          print(f"you lose,you want to the correct word.Okay it's\"{random_word}\" ")
          game_over = True

    print(hangman[lives])

    if "_" not in display:
         print("game over, you win")
         game_over = True
    print(display)