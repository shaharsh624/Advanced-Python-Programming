try:
    n=int(input("Enter n:"))
    result=10/n
except ZeroDivisionError:
    print("Cant divide by zero")
except ValueError:
    print("wrong value input")
else:
    print(result)