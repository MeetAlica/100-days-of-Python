# Function to clear the console
from os import system, name

def clear():
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")

# Logo for the app
from art import logo
print(logo)

bidders = {}

# Loop for multiple bidders
bidding_finished = False
while not bidding_finished:
  name = input("What is your name?\n").lower().capitalize()
  bid = int(input("What's your bid?\n$"))

  bidders[name] = bid

  should_continue = ""
  while should_continue not in("y", "n"):
    should_continue = input("Are there more bids? 'Y' or 'N'\n").lower()

  if should_continue == "y" or should_continue == "yes":
    clear()
  elif should_continue == "n" or should_continue == "no":
    clear()
    bidding_finished = True

    # Calculating the winner
    winner = list(bidders.keys())[0]
    for key in bidders:
      if bidders[key] > bidders[winner]:
        winner = key

    print(f"The winner is {winner}, with a bid of ${bidders[winner]}.")
