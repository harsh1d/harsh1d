# Define Functions
def greet(name):
    return f"Hello, {name}!"

def ask_for_name():
    return input("Please enter your name: ")

# Functional Programming with User Input
def main():
    # Ask user for their name
    name = ask_for_name()

    # Greet the user using their name
    greeting = greet(name)

    # Print the greeting
    print(greeting)

# Call the main function
if __name__ == "__main__":
    main()