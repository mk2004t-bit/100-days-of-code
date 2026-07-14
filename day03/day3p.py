#CONDTITONAL STATEMENTS, LOGICAL OPERATORS, CODE BLOCK AND SCOPE
#Conditional Statements
single = True
have_money = True
age = 19
name = "TMK"
print(name.lower())
#multiline string
paragraph = ''' /usr/bin/python3 /Users/tmk/Developer/python/practice/day3/day3p.py
te a girl
You are not single
You can date a girl.
yor are single,but you don't have i think its not possibe to date a girl🥲
you are single,so you can date girl.
You are single.so,you can date a girl
tmk@manikantas-MacBook-Air practice % /usr/bin/python3 /Users/tmk/D
h,so you can date
you can have a girl.
tmk@manikantas-MacBook-Air practice % '''

#if-else
if single == True:
  print("You can date a girl.")
else:
  print("you cannot date a girl")

#Nested if-else
if single == True:
  if have_money == "True":
    print("you are single and have money.So, You can date a girl🍾")
  else:
    print("yor are single,but you don't have i think its not possibe to date a girl🥲")
else:
  print("You are not single")

#if-elif-else
if single ==True:
  print("you are single,so you can date girl.")
elif have_money == True:
  print("you are not single,but you got a lot of money.so you can date more than one girl")
else:
  print("you are not single and you only got little a amount so you can date a single girl")

#multiple if 
if single == True:
  print("You are single.so,you can date a girl")
else:
  print("You are not single ")
if age > 18:
  print("your are over 18 so, you are ligal to have a girlfriend")

#Logical operators
#AND
if single == True and have_money == True:
  print("you are single and have money, You can date a girl")
else:
  print("either you have no money or not single")

#OR
if single == True or have_money == True:
  print("Either you have money or you are single or you are both,so you can date")
else:
  print("you have nothing")

#NOT
if not single:
  print("you can date.cause, you are commited")
else:
  print("you can have a girl.")

