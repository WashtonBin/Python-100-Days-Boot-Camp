from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")

  
  
  
def bidder_winner(bidders):
  highest_bid = 0
  winner =""
  for bidder in bidders:
    bid_amount = bidders[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

def bid_process():
  bidders = {}
  next = "yes"
  while next == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    next = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    clear()
  if next == "no":
    bidder_winner(bidders)

bid_process()


