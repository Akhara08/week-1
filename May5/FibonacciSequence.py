def fibonacci(n):
    # Initialize the first two numbers in the Fibonacci sequence
    a, b = 0, 1
    print("Fibonacci sequence:")
    
    # Loop to generate n terms of the sequence
    for _ in range(n):
        print(a, end=' ')  # Print the current term
        a, b = b, a + b    # Update values: next term is sum of previous two

    print()  # Print newline after sequence is complete

# Take user input for the number of terms
n = int(input("Enter number of terms: "))

# Call the function to print the Fibonacci sequence
fibonacci(n)
