from cs50 import get_int

# User Inputs
x = get_int("x: ")
y = get_int("y: ")

if x < y:
    print("x is less than y")
elif x > y:
    print("y is less than x")
else:
    print("x is equal to y")