import random

numbers =['1','2','3','4','5','6','7','8','9']
characters = ['!','@','$','*','(',')']
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z'
]

print("Welcome to strong password generator")
letter_count = int(input("enter no of letters you want in your password: "))
character_count = int(input("enter no of characters you want in your password: "))
number_count = int(input("enter no of number you want in your password: "))
password = []

for _ in range(1,letter_count+1):
  password.append(random.choice(letters))

for _ in range(1,character_count+1):
  password.append(random.choice(characters))

for _ in range(1,number_count+1):
  password.append(random.choice(numbers))

print(password)
random.shuffle(password)

print(password)
strong_password = ""
for char in password:
  strong_password+=char

print(f"password:{strong_password}")