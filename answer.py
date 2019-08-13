from cs50 import get_string

c = get_string("Answer: ")

if c == "y" or c == "Y":
    print("Confirmed")
elif c == "n" or c == "N":
    print("Denied")
else:
    print("Please enter Y/N")
