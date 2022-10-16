from replit import clear

from art import logo_bid
print(logo_bid)
print("Welcome stupid!!")

all_bids = {}
Finish = False
while not Finish:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  all_bids[name] = bid
  more_bidders = input("Are there any other bidders? ").lower()
  if more_bidders == "yes":
     clear()
  elif more_bidders == "no":
    Finish = True

max_bid = 0
for bidder in all_bids:
  bid_amount = int(all_bids[bidder])
  if bid_amount > max_bid:
    max_bid = bid_amount
    winner = bidder
clear()

print(f"The winner is {winner} with ${max_bid}")


