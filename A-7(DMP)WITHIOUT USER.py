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

# Equivalence and Implication without user interaction
def equiv_implies_without_user():
    a = [True, False]
    b = [True, False]
    print("Equivalence Truth Table:")
    for x in a:
        for y in b:
            print(f"EQUIV({x}, {y}) = {equiv_gate(x, y)}")

    print("\nImplies Truth Table:")
    for x in a:
        for y in b:
            print(f"IMPLIES({x}, {y}) = {implies_gate(x, y)}")

# Run the Program
if __name__ == "__main__":
    equiv_implies_without_user()