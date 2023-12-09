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
    for a in [True, False]:
        for b in [True, False]:
            print(f"AND({a}, {b}) = {and_gate(a, b)}")

def or_truth_table():
    for a in [True, False]:
        for b in [True, False]:
            print(f"OR({a}, {b}) = {or_gate(a, b)}")

def not_truth_table():
    for a in [True, False]:
        print(f"NOT({a}) = {not_gate(a)}")

def xor_truth_table():
    for a in [True, False]:
        for b in [True, False]:
            print(f"XOR({a}, {b}) = {xor_gate(a, b)}")

def implies_truth_table():
    for a in [True, False]:
        for b in [True, False]:
            print(f"IMPLIES({a}, {b}) = {implies_gate(a, b)}")

def equiv_truth_table():
    for a in [True, False]:
        for b in [True, False]:
            print(f"EQUIV({a}, {b}) = {equiv_gate(a, b)}")

# Call Truth Table Functions
and_truth_table()
or_truth_table()
not_truth_table()
xor_truth_table()
implies_truth_table()
equiv_truth_table()