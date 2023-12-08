import math

try:
    math.sqrt(-100)
except ValueError:
    print("Positive number expected for square root operation.")
