# Recursive Function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Generator Function
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Generator Consumer
def print_fibonacci(n):
    generator = fibonacci_generator()
    for i in range(n):
        print(next(generator))

# Functional Programming with Recursion and Generators
def main():
    # Calculate factorial using recursion
    n = 5
    result = factorial(n)
    print(f"The factorial of {n} is {result}")

    # Print Fibonacci sequence using generator
    print("The first 10 numbers in the Fibonacci sequence are:")
    print_fibonacci(10)

# Call the main function
if __name__ == "__main__":
    main()