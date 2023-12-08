try:
    num=int(input("Enter a number: "))
    result=10/num
    print(result)
except ZeroDivisionError:
    print("Error: Cannot be divide by zero")
except ValueError:
    print("Wrong Value input")