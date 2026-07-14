print("welcome to the tip calculator➖➕➗✖️🟰🧮")
bill =  float(input("What was the total bill💸\n"))
tip = int(input("What percent tip would you like to give ? 10,20,30\n"))
people = int(input("how many people would want to split the amount\n"))

bill_with_tip = round((bill*(1+tip/100)),2)
bill_per_person = round(bill_with_tip/people,2)

print(f"hey,total amount after the tip is {bill_with_tip} and {people} people can split as {bill_per_person}")
