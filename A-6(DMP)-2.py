# Propositional Logic Functions
def and_gate(a, b):
    return a and b

def or_gate(a, b):
    return a or b

def not_gate(a):
    return not a

def xor_gate(a, b):
    return a ^ b

def implies_gate(a, b):
    return not a or b

def equiv_gate(a, b):
    return a == b

# Truth Table Functions
def and_truth_table():
    print("AND Truth Table:")
    for a in [True, False]:
        for b in [True, False]:
            print(f"AND({a}, {b}) = {and_gate(a, b)}")

def or_truth_table():
    print("\nOR Truth Table:")
    for a in [True, False]:
        for b in [True, False]:
            print(f"OR({a}, {b}) = {or_gate(a, b)}")

def not_truth_table():
    print("\nNOT Truth Table:")
    for a in [True, False]:
        print(f"NOT({a}) = {not_gate(a)}")

def xor_truth_table():
    print("\nXOR Truth Table:")
    for a in [True, False]:
        for b in [True, False]:
            print(f"XOR({a}, {b}) = {xor_gate(a, b)}")

def implies_truth_table():
    print("\nIMPLIES Truth Table:")
    for a in [True, False]:
        for b in [True, False]:
            print(f"IMPLIES({a}, {b}) = {implies_gate(a, b)}")

def equiv_truth_table():
    print("\nEQUIV Truth Table:")
    for a in [True, False]:
        for b in [True, False]:
            print(f"EQUIV({a}, {b}) = {equiv_gate(a, b)}")

# Main Function
def main():
    while True:
        print("\n1. AND Truth Table")
        print("2. OR Truth Table")
        print("3. NOT Truth Table")
        print("4. XOR Truth Table")
        print("5. IMPLIES Truth Table")
        print("6. EQUIV Truth Table")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            and_truth_table()
        elif choice == '2':
            or_truth_table()
        elif choice == '3':
            not_truth_table()
        elif choice == '4':
            xor_truth_table()
        elif choice == '5':
            implies_truth_table()
        elif choice == '6':
            equiv_truth_table()
        elif choice == '7':
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Please enter a valid choice.")

# Run the Program
if __name__ == "__main__":
    main()