def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

n = int(input("Enter number of terms: "))
fibonacci(n)
