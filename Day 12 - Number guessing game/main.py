from random import randint
import sys

from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number = randint(1, 101)

difficulty = input("Choose a difficulty: type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
  chances = 10
elif difficulty == 'hard':
  chances = 5
else:
  print("Wrong input!")
  sys.exit()

user_guess = 0
while user_guess != number:
  if chances > 0:
    user_guess = int(input(f"You have {chances} attempts remaining to guess the number.\nMake a guess: "))

    if user_guess > number:
      print("Too high!")
      chances -= 1
    elif user_guess < number:
      print("Too low!")
      chances -= 1
    else:
      print(f"You win! The number was {number}.")

  else:
    print(f"You lose! The number was {number}.")
    sys.exit()
