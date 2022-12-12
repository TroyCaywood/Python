
from art import logo

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# Create a dictionary containing symbols as strings for key and function name for value

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What is the first number?: "))
  # Print dictionary of operations
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    # Prompt for num2
    num2 = float(input("What is the next?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to continue with a new calculationr: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

# Call calculator function
calculator()
