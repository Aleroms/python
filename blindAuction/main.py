from replit import clear
from art import logo

def welcome():
  print(logo)
  print("Welcome to the secret auction program.")

def continueBidding():
  continueBid = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  while continueBid.lower() != "no" and continueBid.lower() != "yes":
    continueBid = ("Invalid input. Please type 'yes' or 'no': ")
  return continueBid.lower() == "yes"

def getBidder():
  name = input("What is your name?: ")
  
  while True:
    try:
      bid = int(input("What is your bid?: $"))
      break
    except ValueError:
      print("You must enter an integer number")
      
  return {"name": name, "bid": bid}

def calculateHighestBidder(bidders):
  highestBidder = {"name": "", "bid": 0}
  for bidder in bidders:
    if bidder["bid"] > highestBidder["bid"]:
      highestBidder = bidder
  return highestBidder
  
def secretAuction():
  bidders = []
  moreBidders = True

  welcome()
  while moreBidders:
    bidders.append(getBidder())
    moreBidders = continueBidding()
    print(moreBidders)
  clear()
  highest_bidder = calculateHighestBidder(bidders)
  print(f"The winner is {highest_bidder['name']} "
  f"with a bid of ${highest_bidder['bid']}")
  
secretAuction()
