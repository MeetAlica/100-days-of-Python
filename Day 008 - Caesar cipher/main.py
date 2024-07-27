# Alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Main function
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""

  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)

      if cipher_direction == "encode":
        new_position = position + shift_amount

        if new_position >= len(alphabet):
          new_position -= len(alphabet)

      elif cipher_direction == "decode":
        new_position = position - shift_amount

        if new_position < 0:
          new_position += len(alphabet)

      new_letter = alphabet[new_position]
      end_text += new_letter

    else:
      end_text += char

  print(f"Here's the {cipher_direction}d result: {end_text}")

# Logo
from art import logo
print(logo)

# Loop
should_end = False
while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  while direction not in ["encode", "decode"]:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n")) % 26

  caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

  answer = input("Want to go again? Y/N\n").lower()
  if answer == "n":
    should_end = True
    print("Goodbye!")
