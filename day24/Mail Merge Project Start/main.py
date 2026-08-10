#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


with open("./day24/Mail Merge Project Start/input/Names/invited_names.txt") as file:
  names = file.readlines()

with open("./day24/Mail Merge Project Start/input/letters/starting_letter.txt") as letter_file:
  letter_contents = letter_file.read()
  for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace("[name]",stripped_name)
    with open(f"./day24/Mail Merge Project Start/output/ReadyToSend/letter_for_{name}.txt",mode="w") as send_letter:
        send_letter.write(new_letter)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp