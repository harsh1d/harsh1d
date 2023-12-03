A=5
try:
    A=int(input())
    fact=1
    for i in range(1,A+1):
        fact=fact*i
    print("\n Factioral of ",A,"=",fact)
except ValueError:
    print("\n Invalid input")