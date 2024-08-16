from art import logo, vs
from game_data import data
import random

def get_random_name():
  """Returns a random entity from the data list, which is a dictionary with name, follower count, description and country."""
  return random.choice(data)

def compare_names(a: dict, b: dict):
  """Compare 'A' against 'B', and if 'A' has more followers, returns True, else returns False."""
  return a['follower_count'] > b['follower_count']

def game():
  """Main function for the game."""
  score = 0
  should_end = False
  compare_a = get_random_name()
  compare_b = get_random_name()
  while compare_a == compare_b:
    compare_b = get_random_name()

  while not should_end:
    print()
    print(f"Compare A: {compare_a['name']}, a(n) {compare_a['description']} from {compare_a['country']}")
    print(vs)
    print(f"Against B: {compare_b['name']}, a(n) {compare_b['description']} from {compare_b['country']}")

    guess = input("Type 'A' or 'B': ").lower()
    if guess == 'a':
      if compare_names(compare_a, compare_b):
        score += 1
        compare_a = compare_b
        compare_b = get_random_name()
        while compare_a == compare_b:
          compare_b = get_random_name()
      else:
        print(f"Sorry, that's wrong. Your final score: {score}")
        should_end = True
    elif guess == 'b':
      if not compare_names(compare_a, compare_b):
        score += 1
        compare_a = compare_b
        compare_b = get_random_name()
        while compare_a == compare_b:
          compare_b = get_random_name()
      else:
        print(f"Sorry, that's wrong. Your final score: {score}")
        should_end = True

print(logo)
print("Welcome to the Higher or Lower guessing game!\nYou need to guess, 'A' or 'B' have more followers on Instagram.")
game()
