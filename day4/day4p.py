#RANDOMISATION AND PYTHON LISTS
import random
random_number1 = random.randint(1,10)
print(random_number1)
random_number2 = round(random.random()*10)
print(random_number2)
random_uniform = random.uniform(1,10)
print(random_uniform)

#Python lists
fruits = ["apple","banana","cherry","dragon"]
print(fruits)
#offset
#appending
fruits.append("grapes")
print(f"After appending \"grapes\" : {fruits}")
#extending
fruits.extend(["mango","orange"])
print(f"After extending \"mango\" and \"orange\" :{fruits}")
no_of_items_in_fruits_list = fruits.count("orange")
print(f"no_of_oranges_in_fruits_list : {no_of_items_in_fruits_list}")
#choice
print(random.choice(fruits))

#Nested lists
movies =["Avengers","Marvel","CaptainAmerica","IronMan"]
series =["Smallville","Dark","MoonLight","M.S.Marvel"]

entertainment =[movies,series]
print(entertainment)
#printing movies in entertainment
print(entertainment[0])
#printing series in entertainment
print(entertainment[1])
#printing a single movie [0] at index [0]
print(entertainment[0][0])
#printing a single series [1] at index [0]
print(entertainment[1][0])