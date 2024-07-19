import random

# Rock Paper Scissors ASCII Art

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

print("Welcome to the Rock Paper Scissors game!")
users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
ai_choice = random.randint(0, 2)

if users_choice > 2:
  print("You selected an invalid number.")
else:
  print(f"Your choice was: {choices[users_choice]}")
  print(f"The computer's choice was: {choices[ai_choice]}")

  if users_choice == ai_choice:
    print("It's a draw!")
  elif (users_choice == 0 and ai_choice == 1) or (users_choice == 1 and ai_choice == 2) or (users_choice == 2 and ai_choice == 0):
    print("You lost this round.")
  else:
    print("You win this round!")