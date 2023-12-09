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

# Equivalence and Implication with user interaction
def equiv_implies_with_user():
    a = input("Enter first value (True/False): ")
    b = input("Enter second value (True/False): ")
    print("\nEquivalence Truth Table:")
    print(f"EQUIV({a}, {b}) = {equiv_gate(a, b)}")

    print("\nImplies Truth Table:")
    print(f"IMPLIES({a}, {b}) = {implies_gate(a, b)}")

# Run the Program
if __name__ == "__main__":
    equiv_implies_with_user()