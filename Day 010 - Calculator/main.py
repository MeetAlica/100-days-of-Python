# Imports
from os import system, name
from art import logo

# Function for clearing console
def clear():
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")

# Operation functions
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# Main function for the app
def calculator():
  """This is the calculator main function's docstring."""
  print(logo)

  num1 = float(input("What's the first number? "))
  for symbol in operations:
    print(symbol)

  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number? "))

    calculation_function = operations[operation_symbol]
    result = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {result}")

    if input(f"Type 'Y' to continue calculating with {result}, or 'N' to start a new calculation: ").lower() == 'y':
      num1 = result
    else:
      should_continue = False
      clear()
      calculator()

calculator()