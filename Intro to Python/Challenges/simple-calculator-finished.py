'''
Simple Calculator Challenge
'''

# Add two numbers
def add(x, y):
    return x + y

# Subtract one number from another
def subtract(x, y):
    return x - y

# Multiple two numbers
def multiply(x, y):
    return x * y

# Divide one number from another
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Welcome to the Simple Calculator!")

print() # Display empty line for styling

# Get user inputs
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
operation = input("Select operation (+, -, *, /): ")
result = 0

# Check if operation input is valid
if operation in ('+', '-', '*', '/'):

    if operation == "+":
        result = add(first_number, second_number)

    elif operation == "-":
        result = subtract(first_number, second_number)

    elif operation == "*":
        result = multiply(first_number, second_number)

    elif operation == "/":
        result = divide(first_number, second_number)

    print() # Display empty line for styling

    print("Result:", result)    # Display result

else:
    # If operation input is not valid, inform the user and end program
    print("Invalid operation.")