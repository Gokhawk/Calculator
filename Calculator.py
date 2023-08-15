from art import logo     # Importing logo from art.py

# Add
def add(n1, n2):        # Defining calculation functions
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

# Power
def power(n1, n2):
    return n1 ** n2

# Mod
def mod(n1, n2):
    return n1 % n2

operations = {               # Adding functions in a dictionary with their symbols for easier use 
    "+": add,
    "-": subtract,
    "x": multiply,
    "/": divide,
    "^": power,
    "%": mod
}

def calculate():
    print(logo)
    num1 = float(input("What is the first number ? : "))      # Making numbers float for calculate float numbers if user entered 

    for symbol in operations:   # Printing symbols to show user the options 
        print(symbol)

    should_continue = True

    while should_continue:
        operation = input("Pick an operation : ")    # Asking user to select a operation

        num2 = float(input("What is the next number ? : "))
        calculation_function = operations[operation] # selecting operation from operations dictionary 
        answer = calculation_function(num1, num2)   # Doing the calculation by giving the numbers to calculation_function 

        print(f"{num1} {operation} {num2} = {answer}")  # printing the calculation and the answer 

        another_operation = input("Type 'c' to continue or Type 'r' restart calculation or Type 'e' to exit. : ").lower().strip()   # Asking user to continue calculation or restart calculation or exit. 
        if another_operation == "c":
            num1 = answer      # making num1 is answer because when we continue, the answer we found on last calculation must be our first number now.
        elif another_operation == "r":
            calculate()       # Recalling the calculate function to restart 
        elif another_operation == "e":
            print("Leaving Calculator...")
            should_continue = False   # Making should_continue = False to stop the while loop and exit the calculator app.

calculate()   # Calling calculate() function to start the calculation 