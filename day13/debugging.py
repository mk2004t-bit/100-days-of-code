#step-1
#Describe the problem
# 1.what is for loop doing 
# 2.when does the print suppose to execute
# 3.what are the assumptions of i

"""def bug():
    for  i in range(1,20): # to get it right need to make the range 1 to 21.
        if i == 20:
            print("You got it.")

bug()"""

#step-2
#Reproduce the bug
  # this bug happens occasionally 
"""import random
dice_images = [1,2,3,4,5,6]
random_dice = random.randint(1,6)   #Here is the bug list index starts from 0 and ends at 5 in the list but, This random function generating number from 1 to 6.

print(dice_images[random_dice])"""

#step-3 
#play a computer 
"""year = int(input("Enter your year of birth: "))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:                  #Here is bug it is there isn't any bucket to catch year 1994.
    print("You are genZ.")
"""
#step-4
#fix the errors 
#Here if we don't use the concept of try-except then when user enter an actually string like "llskd".python doesn't know what to do some it crashes our code while in the air and give valueerror.
"""try:
    age = int(input("Enter your age: "))
except ValueError:
    print("you have entered invalid input. Try again entered valid numerical value like 15 : ")
    age = int(input("Enter your age: "))
if age >= 18:
    print(f"You are {age}.So, You can get license.")
else:
    print(f"You are {age}.You should be 18 or above to get a license. ")"""

#step-5
#print is your friend
#There is a bug in your code. you can find it using print by printing very variable and see whether it printing the value you expected to print.
"""total_words = 0
pages = int(input("Enter no of pages: "))
words_per_page = int(input("Enter words per page: "))

total_words == pages + words_per_page

print(f"Total word is {total_words}")"""

#step-6
#Using debugger 
import maths
import random
a_list =[1,2,3,4,5,6]
def mutate(list):
    b_list =[]
    new_item = 0
    for item in list:
        new_item = item*2
        new_item+=random.randint(1,6)
        new_item+= maths.add(item,new_item)
        b_list.append(new_item)
    print(b_list)

mutate(list=a_list)
