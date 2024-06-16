def user_choice():
    print("Enter your choice:")
    print("1. Function")
    print("2. Generator")
    choice = input()
    return choice

def user_input_func():
    print("Enter function details:")
    function_name = input("Function Name: ")
    return function_name

def user_input_generator():
    print("Enter generator details:")
    generator_name = input("Generator Name: ")
    return generator_name

def user_choice_recursive():
    choice = user_choice()
    if choice == "1":
        function_name = user_input_func()
        print(f"Function Name: {function_name}")
        user_choice_recursive()
    elif choice == "2":
        generator_name = user_input_generator()
        print(f"Generator Name: {generator_name}")
        user_choice_recursive()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        user_choice_recursive()

user_choice_recursive()