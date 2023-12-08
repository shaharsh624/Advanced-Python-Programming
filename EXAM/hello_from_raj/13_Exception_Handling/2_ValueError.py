import math

x = int(input("Please enter a positive number: "))

try:
    print(f"Square Root of {x} is {math.sqrt(x)}")
except ValueError as ve:
    print(f"You entered {x}, which is not a positive number.")
    print(ve)
