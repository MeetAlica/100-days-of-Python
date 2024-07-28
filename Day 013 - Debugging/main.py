############DEBUGGING#####################

# Bug 1:
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# Solution 1:
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# Bug 2:
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# Solution 2:
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# Bug 3:
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# Solution 3:
year = int(input("What's your year of birth? "))
if year >= 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# Bug 4:
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# Solution 4:
age = int(input("How old are you? "))
if age >= 18:
  print(f"You can drive at age {age}.")

# Bug 5:
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Solution 5:
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# Bug 6:
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)
# mutate([1,2,3,5,8,13])

# Solution 6:
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)
mutate([1,2,3,5,8,13])