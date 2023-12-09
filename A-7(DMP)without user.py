# Define Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Apply Functions
numbers = [2, 3, 4, 5]

print("Addition:", list(map(add, numbers, numbers)))
print("Subtraction:", list(map(subtract, numbers, numbers)))
print("Multiplication:", list(map(multiply, numbers, numbers)))
print("Division:", list(map(divide, numbers, numbers)))