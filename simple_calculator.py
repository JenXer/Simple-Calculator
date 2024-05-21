# Function to perform the chosen operation
def calculator():
    # Getting input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    # Performing the operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."
    else:
        result = "Invalid operation."

    # Displaying the result
    print("Result:", result)

# Calling the calculator function
calculator()
