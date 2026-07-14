#BLind bid
from logo import gavel_logo
#crearting a empty dictoonary
bid_details ={}
should_continue =True


print(gavel_logo)
print("Welcome to blind bid")


def highest_bidder(bidding_details):
  highest_bidder =""
  highest_bidding=0
  for bidder in bidding_details:
    if bidding_details[bidder] > highest_bidding:
      highest_bidding = bidding_details[bidder]
      highest_bidder = bidder
  print(f"The winner is {highest_bidder} with bidding amount ${highest_bidding}.")


while should_continue == True:
  name = input("Enter your name: ")
  bid = int(input("Enter your bid: $"))
  bid_details[name] = bid
  bid_continue = input("Is there anyone to place a bid?yes or no: ").lower()
  if bid_continue == "no":
    should_continue = False
    highest_bidder(bid_details)
  else:
        print("\n"*20)



    



