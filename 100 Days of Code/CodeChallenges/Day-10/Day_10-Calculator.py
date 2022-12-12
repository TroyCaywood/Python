
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

# Define calculator function
def calculator():
    print(logo)
    # Get input for num1
    num1 = float(input("What is the first number?: "))
    # Print dictionary of operations
    for symbol in operations:
        print(symbol)
    
    # Create condition variable for while loop
    should_continue = True
    
    # Create while loop for calculations
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        # Prompt for num2
        num2 = float(input("What is the next?: "))
        # Create caclulation_function variable and set it to the opertions dicionary with the operation_symbol as the key. Remember we stored the function names in the dictionary. That means we can call the function using this variable
        calculation_function = operations[operation_symbol]
        # Set answer to calculation_function passing the num1 and num2 variables
        answer = calculation_function(num1, num2)
        # Print answer
        print(f"{num1} {operation_symbol} {num2} = {answer}")
  
        # If statement to check if user wants to continue calculating using the previous answer or start a new calculation. If y, num1 is equal to the previous answer and the while loop starts again.
        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to continue with a new calculationr: ") == "y":
          num1 = answer
        # If n set should_continue to False to stop the loop and call the calculator function to restart the function again with new numbers.
        else:
          should_continue = False
          calculator()

# Call calculator function
calculator()
