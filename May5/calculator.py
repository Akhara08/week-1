def calculator():
    # Display the available operations
    print("Select operation: +, -, *, /")

    # Get the operator input from the user
    op = input("Enter operator: ")

    # Take two numbers as input and convert them to float
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the operation based on the chosen operator
    if op == '+':
        print("Result:", num1 + num2)  # Addition
    elif op == '-':
        print("Result:", num1 - num2)  # Subtraction
    elif op == '*':
        print("Result:", num1 * num2)  # Multiplication
    elif op == '/':
        if num2 != 0:
            print("Result:", num1 / num2)  # Division
        else:
            print("Error: Division by zero!")  # Handle division by zero
    else:
        print("Invalid operator!")  # Handle invalid operator input

# Call the calculator function to start the program
calculator()
