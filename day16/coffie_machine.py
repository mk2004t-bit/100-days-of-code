from resources import reciepe,resources,coins

def report(resources):
    for item in resources["ingredients"]:
        if item == "water" or item == "milk":
            print(f"{item}: {resources["ingredients"][item]}ml")
        elif item == "coffee":
            print(f"{item}: {resources["ingredients"][item]}g")
        else:
            print(f"{item}:${resources["ingredients"][item]}")

def check_resources(resources,order,reciepe):
    avaliability = True
    for item in resources["ingredients"]:
        if int(resources["ingredients"][item]) > int(reciepe[order]["ingredients"][item]):
            print(f"there is enough {item}")
        else:
            print(f"sorry there is not enough {item}")
            avaliability = False
    return avaliability

def insert_coins(reciepe,coins):
    pay = []
    print(f"{order} is ${reciepe[order]["cost"]}")
    print("Insert Coins")
    for coin in coins:
        if coin == "quarters":
            pay.append(0.25 * int(input(f"how many {coin} :")))
        elif coin == "dimes":
            pay.append(0.10 * int(input(f"how many {coin} :")))
        elif coin == "nickles":
            pay.append(0.05 * int(input(f"how many {coin} :")))
        elif coin == "pennies":
            pay.append(0.01 * int(input(f"how many {coin} :")))
    return pay

def deduct_resources(order,reciepe,resources):
    for item in resources["ingredients"]:
        resources["ingredients"][item] = resources["ingredients"][item] - (reciepe[order]["ingredients"][item])
    




off = False
while not off:
    order = input("what would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        report(resources)
    if order == "espresso" or order == "latte" or order == "cappuccino":
        availiability = check_resources(resources,order,reciepe)
        if availiability:
            pay = insert_coins(reciepe,coins)
            if sum(pay) >= reciepe[order]["cost"]:
                resources["money"]+=reciepe[order]["cost"]
                deduct_resources(order,reciepe,resources)
                change = round((sum(pay) - reciepe[order]["cost"] ),2)
                print(f"Here is your {order} ☕ enjoy.")
                print(f"here is your change :${change}")
            else:
                print("money isn't sufficient.")
    if order == "earning":
        print(f"earning is ${resources["money"]}")

    if order == "off":
        off = True
    if order != "report" and order != "espresso" and order != "latte" and order != "cappuccino" and order != "off" and order != "earning":
        print("Enter valid input.")



