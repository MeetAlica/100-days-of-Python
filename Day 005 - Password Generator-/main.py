import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# Easy version

# final_pw = ""

# for letter in range(0, nr_letters):
#   random_letter = letters[random.randint(0, len(letters) - 1)]
#   final_pw += random_letter

# for number in range(0, nr_numbers):
#   random_number = numbers[random.randint(0, len(numbers) - 1)]
#   final_pw += random_number

# for symbol in range(0, nr_symbols):
#   random_symbol = symbols[random.randint(0, len(symbols) - 1)]
#   final_pw += random_symbol

# --------------------------------------------------------------------

# Hard version

password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

final_pw = ''.join(password_list)

print(f"Your password is: {final_pw}")