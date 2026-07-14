# if-else 

print("Welcome to this island 🏝️ ")
height =int(input("Enter your height in feet : "))
age = int(input("Enter your age in years"))
if height > 1.5:
  print("hey,your height is more than 1.5 meters.So, you can enter.")
else:
  print("Sorry,You can't enter. Try again when you are more than 1.5 meter height")


# Nested if 

if height >1.5:
  if age > 5:
    print("you can enter into the island.")
  else :
    print("you are very young age")
else:
  print("you height is doest meet required height")

# if-elif-else
if height > 1.5:
  if age < 5 :
    print("your ticket price is 12rs")
  elif age <18 :
    print("your ticket price is 15rs")
  else :
    print("your ticket price is 18rs")
else:
  print("your are not allowed to buy a ticket.")

# multiple if
if height>1.5:
  print("your are allowed")
else:
  print("your are not allowed")
if age>45:
  print("you are allowed")

print("Welcome to the pizza delivery.")
size = input("What size piza do you want ?S, M or L ? ")
pepperoni = input("Do you want pepperoni on your pizza?Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ? ")
for_pizza = 0
for_cheese = 0
if size == "s":
  for_pizza = 15
  if pepperoni == "y":
    for_pizza +=2
elif size == "m" :
  for_pizza = 20
  if pepperoni == "y":
    for_pizza +=3
elif size == "l" :
  for_pizza = 25
  if pepperoni == "y":
    for_pizza +=3
if extra_cheese == "y":
  for_pizza +=1
print(f"your final bill is {for_pizza}")


  

